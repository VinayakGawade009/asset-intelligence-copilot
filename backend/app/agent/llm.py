import os
import sys
import json
import time
import hashlib
import uuid
import re
from datetime import datetime
from pathlib import Path
from typing import Type, TypeVar, Optional, Any, Dict, Tuple
from pydantic import BaseModel, ValidationError

# Project root path
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from backend.app.config import (
    GOOGLE_API_KEY,
    GEMMA_MODEL_FAST,
    GEMMA_MODEL_STRONG,
    DUCKDB_PATH,
)
from backend.app.db.connection import get_connection
from backend.app.db.schema import init_db

# Cache directory
CACHE_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "llm_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

T = TypeVar("T", bound=BaseModel)

class GemmaClient:
    """Wrapper around google-genai SDK for Gemma models with retry, caching, 

    schema validation, and observability logging in DuckDB.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or GOOGLE_API_KEY
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY / GEMINI_API_KEY is not set.")
        
        from google import genai
        self.client = genai.Client(api_key=self.api_key)
        self._ensure_llm_calls_table()

    def _ensure_llm_calls_table(self):
        """Ensures the llm_calls table exists in DuckDB."""
        try:
            conn = get_connection(read_only=False)
            init_db(conn)
            conn.close()
        except Exception as e:
            print(f"[WARN] Failed to verify llm_calls table: {e}", file=sys.stderr)

    def _compute_prompt_hash(self, model: str, prompt: str) -> str:
        content = f"{model}:::{prompt}"
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def _log_call(
        self,
        role: str,
        model: str,
        prompt_hash: str,
        prompt: str,
        latency_ms: float,
        input_tokens: int,
        output_tokens: int,
        cached: bool,
    ):
        """Logs LLM call metadata into DuckDB."""
        try:
            conn = get_connection(read_only=False)
            call_id = f"call_{uuid.uuid4().hex[:12]}"
            prompt_preview = prompt[:150].replace("\n", " ")
            created_at = datetime.utcnow().isoformat()

            conn.execute(
                """
                INSERT INTO llm_calls (call_id, role, model, prompt_hash, prompt_preview, latency_ms, input_tokens, output_tokens, created_at, cached)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    call_id,
                    role,
                    model,
                    prompt_hash,
                    prompt_preview,
                    float(latency_ms),
                    int(input_tokens or 0),
                    int(output_tokens or 0),
                    created_at,
                    bool(cached),
                ),
            )
            conn.close()
        except Exception as e:
            print(f"[WARN] Failed to log LLM call: {e}", file=sys.stderr)

    def _call_model_with_backoff(self, model: str, prompt: str, max_retries: int = 4) -> Tuple[str, int, int]:
        """Calls the model with exponential backoff on errors."""
        delay = 2.0
        last_exception = None

        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                text = response.text or ""
                
                input_tokens = 0
                output_tokens = 0
                if hasattr(response, "usage_metadata") and response.usage_metadata:
                    input_tokens = getattr(response.usage_metadata, "prompt_token_count", 0) or 0
                    output_tokens = getattr(response.usage_metadata, "candidates_token_count", 0) or 0

                return text, input_tokens, output_tokens
            except Exception as e:
                last_exception = e
                err_str = str(e).lower()
                is_retryable = any(k in err_str for k in ["429", "rate", "resource", "500", "503", "quota", "internal", "overloaded"])
                
                if attempt < max_retries - 1 and is_retryable:
                    time.sleep(delay)
                    delay *= 2.0
                else:
                    if attempt == max_retries - 1:
                        raise e

        raise last_exception or RuntimeError("Model call failed without exception")

    def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        role: str = "general",
        use_cache: bool = True,
    ) -> str:
        """Generates plain text response with caching and call logging."""
        model_name = model or GEMMA_MODEL_FAST
        prompt_hash = self._compute_prompt_hash(model_name, prompt)
        cache_file = CACHE_DIR / f"{prompt_hash}.json"

        if use_cache and cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cached_data = json.load(f)
                self._log_call(
                    role=role,
                    model=model_name,
                    prompt_hash=prompt_hash,
                    prompt=prompt,
                    latency_ms=0.0,
                    input_tokens=cached_data.get("input_tokens", 0),
                    output_tokens=cached_data.get("output_tokens", 0),
                    cached=True,
                )
                return cached_data["text"]
            except Exception:
                pass  # Fallback to fresh generation on corrupted cache

        start_time = time.time()
        text, in_tok, out_tok = self._call_model_with_backoff(model=model_name, prompt=prompt)
        latency_ms = (time.time() - start_time) * 1000

        # Save to cache
        if use_cache:
            try:
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump({"text": text, "input_tokens": in_tok, "output_tokens": out_tok}, f)
            except Exception:
                pass

        self._log_call(
            role=role,
            model=model_name,
            prompt_hash=prompt_hash,
            prompt=prompt,
            latency_ms=latency_ms,
            input_tokens=in_tok,
            output_tokens=out_tok,
            cached=False,
        )
        return text

    def generate_json(
        self,
        prompt: str,
        response_schema: Type[T],
        model: Optional[str] = None,
        role: str = "json_generator",
        use_cache: bool = True,
    ) -> T:
        """Generates a structured JSON response validated against a Pydantic schema.

        Retries once if validation fails, passing the error feedback back to the model.
        """
        model_name = model or GEMMA_MODEL_FAST
        schema_json = json.dumps(response_schema.model_json_schema(), indent=2)

        augmented_prompt = (
            f"{prompt}\n\n"
            f"CRITICAL: Return ONLY a valid JSON object strictly matching this JSON Schema:\n"
            f"```json\n{schema_json}\n```\n"
            f"Do not include any explanation or extra text outside the JSON markdown block."
        )

        raw_response = self.generate(
            prompt=augmented_prompt,
            model=model_name,
            role=role,
            use_cache=use_cache,
        )

        def _clean_json_str(text: str) -> str:
            # Strip markdown code fences if present
            cleaned = text.strip()
            if "```" in cleaned:
                matches = re.findall(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned)
                if matches:
                    cleaned = matches[0].strip()
            return cleaned

        try:
            cleaned_json = _clean_json_str(raw_response)
            parsed_data = json.loads(cleaned_json)
            return response_schema.model_validate(parsed_data)
        except (json.JSONDecodeError, ValidationError) as first_err:
            # Retry once with validation error feedback
            feedback_prompt = (
                f"{augmented_prompt}\n\n"
                f"Your previous attempt produced the following output:\n"
                f"```\n{raw_response}\n```\n"
                f"It failed validation with error: {first_err}\n"
                f"Please fix the error and output ONLY the valid JSON matching the schema."
            )

            second_raw = self.generate(
                prompt=feedback_prompt,
                model=model_name,
                role=f"{role}_retry",
                use_cache=False,  # Do not use old cache on retry
            )

            cleaned_retry = _clean_json_str(second_raw)
            parsed_retry = json.loads(cleaned_retry)
            return response_schema.model_validate(parsed_retry)
