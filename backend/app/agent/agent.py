"""Gemma 4 agent loop with native function calling and grounded answer generation."""
import os
import sys
import time
import uuid
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import duckdb
from google import genai
from google.genai import types

from backend.app.config import GOOGLE_API_KEY, GEMMA_MODEL_FAST, GEMMA_MODEL_STRONG, TODAY
from backend.app.db.connection import get_connection
from backend.app.agent.llm import GemmaClient
from backend.app.agent.tools import (
    ToolResult,
    determine_visual_type,
    resolve_well_id,
    resolve_area_name,
    tool_well_status,
    tool_area_wells_not_producing,
    tool_well_timeseries,
    tool_downtime_ranking,
    tool_spills_query,
    tool_breaches_check,
    tool_uncontained_spills_query,
    tool_repairs_cost,
    tool_rca_wells_query,
    tool_get_well_context,
    tool_search_documents,
)
from backend.app.schemas.chat import (
    Citation,
    Flag,
    ChatMeta,
    ChatResponse,
)
from backend.app.agent.memory import (
    record_chat_turn_entities,
    handle_memory_extraction_turn,
)

# Declarations of native function tools for Gemma

def well_status(well_id: str, visual_hint: Optional[str] = None) -> str:
    """Get the current operational and production status of a well, including latest inspection, wellhead temperature, and shut-in status."""
    return "ok"

def area_wells_not_producing(area_name: str, visual_hint: Optional[str] = None) -> str:
    """Find wells in a geographic area (e.g. 'Northeast Block 8') that are not producing oil right now and check reasons."""
    return "ok"

def well_timeseries(well_id: str, weeks: int = 13, visual_hint: Optional[str] = None) -> str:
    """Get weekly inspection temperature time-series (wellhead, air) and production status for a well."""
    return "ok"

def downtime_ranking(target: str, window: str = "last 4 months", limit: int = 3, visual_hint: Optional[str] = None) -> str:
    """Rank wells in an area by downtime days in a window, or get downtime days for a single well."""
    return "ok"

def spills_query(target: str, window: str = "last 90 days", min_volume: float = 0.0, visual_hint: Optional[str] = None) -> str:
    """Query oil spills for a well, area, or fleet over a time window with effective volume corrections."""
    return "ok"

def breaches_check(well_id: str, window: str = "last 12 months", visual_hint: Optional[str] = None) -> str:
    """Check regulatory and SOP rule breaches for a well (SR-01, SR-02, SR-03, RC-04, RC-02, RCA) and open fines."""
    return "ok"

def uncontained_spills_query(area_name: str, window: str = "last 90 days", visual_hint: Optional[str] = None) -> str:
    """Find spills in an area that were not contained within the SOP containment time limit."""
    return "ok"

def repairs_cost(wells: List[str], year: Optional[int] = None, visual_hint: Optional[str] = None) -> str:
    """Calculate total repair costs for a list of wells in a given year."""
    return "ok"

def rca_wells_query(area_name: str, equipment_kind: str = "pump_jack", window: str = "last 12 months", visual_hint: Optional[str] = None) -> str:
    """Find wells in an area needing root-cause analysis on equipment (e.g. pump_jack, flowline) due to repeat repairs."""
    return "ok"

def get_well_context(well_id: str, visual_hint: Optional[str] = None) -> str:
    """Retrieve human notes, operator comments, and field context for a well."""
    return "ok"

def search_documents(query: str, visual_hint: Optional[str] = None) -> str:
    """Search manuals, SOPs, rules, and maintenance reports for keywords or topics."""
    return "ok"

TOOL_DECLARATIONS = [
    well_status,
    area_wells_not_producing,
    well_timeseries,
    downtime_ranking,
    spills_query,
    breaches_check,
    uncontained_spills_query,
    repairs_cost,
    rca_wells_query,
    get_well_context,
    search_documents,
]


class AgentRunner:
    """Orchestrates the agent loop: tool selection, retry with strong model, and grounded answer generation."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or GOOGLE_API_KEY
        self.model = model or GEMMA_MODEL_FAST
        self.client = genai.Client(api_key=self.api_key)
        self.gemma_wrapper = GemmaClient(api_key=self.api_key)

    def _execute_tool(self, conn: duckdb.DuckDBPyConnection, tool_name: str, args: Dict[str, Any], user_query: str) -> ToolResult:
        """Dispatches tool execution to the appropriate tool implementation."""
        args_with_query = dict(args)
        args_with_query["user_query"] = user_query

        if tool_name == "well_status":
            return tool_well_status(conn, **args_with_query)
        elif tool_name == "area_wells_not_producing":
            return tool_area_wells_not_producing(conn, **args_with_query)
        elif tool_name == "well_timeseries":
            return tool_well_timeseries(conn, **args_with_query)
        elif tool_name == "downtime_ranking":
            return tool_downtime_ranking(conn, **args_with_query)
        elif tool_name == "spills_query":
            return tool_spills_query(conn, **args_with_query)
        elif tool_name == "breaches_check":
            return tool_breaches_check(conn, **args_with_query)
        elif tool_name == "uncontained_spills_query":
            return tool_uncontained_spills_query(conn, **args_with_query)
        elif tool_name == "repairs_cost":
            return tool_repairs_cost(conn, **args_with_query)
        elif tool_name == "rca_wells_query":
            return tool_rca_wells_query(conn, **args_with_query)
        elif tool_name == "get_well_context":
            return tool_get_well_context(conn, **args_with_query)
        elif tool_name == "search_documents":
            return tool_search_documents(conn, **args_with_query)
        else:
            return tool_search_documents(conn, query=user_query, user_query=user_query)

    def _call_planner_model(
        self,
        model_name: str,
        user_message: str,
    ) -> Tuple[str, Dict[str, Any]]:
        """Invokes Gemma model with native tool declarations and logs honest latency and token usage."""
        planner_prompt = (
            "You are the planner for the Asset Intelligence Copilot.\n"
            f"Today is {TODAY}.\n"
            "Select the single best tool and supply its typed arguments to answer the question.\n"
            "Do not calculate numbers yourself. All facts and metrics are retrieved by the tools."
        )

        p_start = time.time()
        in_tok, out_tok = 0, 0
        response = None
        for attempt in range(2):
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=f"{planner_prompt}\n\nQuestion: {user_message}",
                    config=types.GenerateContentConfig(
                        tools=TOOL_DECLARATIONS,
                        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
                    ),
                )
                break
            except Exception as e:
                err_str = str(e).lower()
                if any(k in err_str for k in ["429", "rate", "resource", "quota", "503"]) and attempt < 1:
                    time.sleep(2.0)
                else:
                    break

        p_latency = (time.time() - p_start) * 1000
        if response and hasattr(response, "usage_metadata") and response.usage_metadata:
            in_tok = getattr(response.usage_metadata, "prompt_token_count", 0) or 0
            out_tok = getattr(response.usage_metadata, "candidates_token_count", 0) or 0

        # Log honest call with real measured latency and real token counts
        p_hash = self.gemma_wrapper._compute_prompt_hash(model_name, f"PLANNER::{user_message}")
        self.gemma_wrapper._log_call(
            role="agent_planner",
            model=model_name,
            prompt_hash=p_hash,
            prompt=f"Question: {user_message}",
            latency_ms=p_latency,
            input_tokens=in_tok,
            output_tokens=out_tok,
            cached=False,
        )

        if response:
            function_calls = getattr(response, "function_calls", None)
            if function_calls:
                for fc in function_calls:
                    f_name = fc.name
                    f_args = fc.args or {}
                    if any(t.__name__ == f_name for t in TOOL_DECLARATIONS):
                        return f_name, f_args

        return "", {}

    def process_query(
        self,
        user_message: str,
        user_id: Optional[str] = None,
        chat_id: Optional[str] = None,
    ) -> ChatResponse:
        """Executes the agent loop and returns ChatResponse."""
        t_start = time.time()
        chat_id = chat_id or f"chat_{uuid.uuid4().hex[:10]}"
        tool_calls_executed = []

        # If user_id is missing, look up first active user from DB
        c_user = get_connection(read_only=True)
        try:
            if not user_id:
                u_row = c_user.execute("SELECT user_id FROM users ORDER BY user_id ASC LIMIT 1").fetchone()
                user_id = u_row[0] if u_row else "U-101"
        finally:
            c_user.close()

        # -------------------------------------------------------------
        # STAGE 7: Memory, Shared Facts, Corrections, Rules, Conflicts
        # -------------------------------------------------------------
        c_mem = get_connection(read_only=False)
        try:
            m_resp = handle_memory_extraction_turn(
                conn=c_mem,
                user_id=user_id,
                chat_id=chat_id,
                user_message=user_message,
                model_name=self.model,
                gemma_client=self.gemma_wrapper,
            )
            if m_resp:
                record_chat_turn_entities(c_mem, chat_id, user_id, user_message, m_resp)
                return m_resp
        finally:
            c_mem.close()

        # -------------------------------------------------------------
        # STEP 1: Tool Selection with Native Function Calling (agent_planner)
        # -------------------------------------------------------------
        selected_tool_name, selected_args = self._call_planner_model(self.model, user_message)

        # If fast model returned no valid tool call, retry once with strong model
        if not selected_tool_name:
            selected_tool_name, selected_args = self._call_planner_model(GEMMA_MODEL_STRONG, user_message)

        # If still no valid tool call, answer asking clarifying question
        if not selected_tool_name:
            total_lat = int((time.time() - t_start) * 1000)
            return ChatResponse(
                chat_id=chat_id,
                answer="I could not determine which records to look up. Could you clarify which well, area, or records you would like me to check?",
                visual=None,
                citations=[],
                flags=[],
                meta=ChatMeta(
                    model=self.model,
                    latency_ms=total_lat,
                    tool_calls=[],
                ),
            )

        # Execute selected tool
        tool_calls_executed.append(selected_tool_name)
        c = get_connection(read_only=True)
        try:
            tool_result = self._execute_tool(c, selected_tool_name, selected_args, user_message)
        finally:
            c.close()

        # -------------------------------------------------------------
        # STEP 2: Grounded Answer Generation (agent_answer)
        # -------------------------------------------------------------
        answer_prompt = (
            "You are the Asset Intelligence Copilot.\n"
            f"Today is {TODAY}.\n"
            "Write a clear, concise, 2-5 sentence answer in markdown responding directly to the user's question, "
            "grounded strictly in the tool result below.\n"
            "State the facts, numbers, dates, IDs, and citation references directly from the tool result.\n"
            "Never speculate, contradict the tool result, or invent causes where none are recorded.\n\n"
            f"User Question: {user_message}\n"
            f"Tool Result: {tool_result.summary_text}"
        )

        a_start = time.time()
        in_tok2, out_tok2 = 0, 0
        answer_text = tool_result.summary_text
        resp2 = None
        for attempt in range(2):
            try:
                resp2 = self.client.models.generate_content(
                    model=self.model,
                    contents=answer_prompt,
                )
                break
            except Exception as e:
                err_str = str(e).lower()
                if any(k in err_str for k in ["429", "rate", "resource", "quota", "503"]) and attempt < 1:
                    time.sleep(2.0)
                else:
                    break

        if resp2:
            a_latency = (time.time() - a_start) * 1000
            answer_text = resp2.text.strip() if resp2.text else tool_result.summary_text

            # If tool summary has an omission/correction note not captured in the answer, preserve it
            if "no longer listed" in tool_result.summary_text and "no longer listed" not in answer_text.lower():
                notes = [s.strip() for s in tool_result.summary_text.split(".") if "no longer listed" in s]
                if notes:
                    answer_text += " " + ". ".join(notes) + "."

            # If tool summary has a rule override note not captured in the answer, preserve it
            if "not the manual" in tool_result.summary_text.lower() and "not the manual" not in answer_text.lower():
                notes = [s.strip() for s in tool_result.summary_text.split(".") if "not the manual" in s.lower()]
                if notes:
                    answer_text += " " + ". ".join(notes) + "."

            if hasattr(resp2, "usage_metadata") and resp2.usage_metadata:
                in_tok2 = getattr(resp2.usage_metadata, "prompt_token_count", 0) or 0
                out_tok2 = getattr(resp2.usage_metadata, "candidates_token_count", 0) or 0

            # Log Call 2 honestly with real measured latency and real token counts
            a_hash = self.gemma_wrapper._compute_prompt_hash(self.model, f"ANSWER::{user_message}")
            self.gemma_wrapper._log_call(
                role="agent_answer",
                model=self.model,
                prompt_hash=a_hash,
                prompt=f"Question: {user_message}\nSummary: {tool_result.summary_text}",
                latency_ms=a_latency,
                input_tokens=in_tok2,
                output_tokens=out_tok2,
                cached=False,
            )

        total_latency_ms = int((time.time() - t_start) * 1000)

        # Format citations & flags to Pydantic schema
        citations_list = [
            Citation(
                id=c["id"],
                kind=c["kind"],
                label=c.get("label", c["id"]),
                detail=c.get("detail", ""),
            )
            for c in tool_result.citations
        ]

        flags_list = [
            Flag(
                kind=f["kind"],
                text=f["text"],
                source_ids=f.get("source_ids", []),
            )
            for f in tool_result.flags
        ]

        final_resp = ChatResponse(
            chat_id=chat_id,
            answer=answer_text,
            visual=tool_result.visual,
            citations=citations_list,
            flags=flags_list,
            meta=ChatMeta(
                model=self.model,
                latency_ms=total_latency_ms,
                tool_calls=tool_calls_executed,
            ),
        )

        c_rec = get_connection(read_only=False)
        try:
            record_chat_turn_entities(c_rec, chat_id, user_id, user_message, final_resp)
        finally:
            c_rec.close()

        return final_resp
