"""Pydantic schemas conforming strictly to UI_CONTRACT.md."""
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field

class Citation(BaseModel):
    id: str
    kind: Literal["inspection", "maintenance", "regulatory", "note", "document"]
    label: str
    detail: str

class Flag(BaseModel):
    kind: Literal["conflict", "overdue", "unconfirmed", "correction_applied", "no_cause"]
    text: str
    source_ids: List[str] = Field(default_factory=list)

class ChatMeta(BaseModel):
    model: str
    latency_ms: int
    tool_calls: List[str] = Field(default_factory=list)

class ChatResponse(BaseModel):
    chat_id: str
    answer: str
    visual: Optional[Dict[str, Any]] = None
    citations: List[Citation] = Field(default_factory=list)
    flags: List[Flag] = Field(default_factory=list)
    meta: ChatMeta

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    text: str
    response: Optional[ChatResponse] = None

class ChatSession(BaseModel):
    chat_id: str
    title: Optional[str] = None
    updated_at: Optional[str] = None

class ChatDetail(BaseModel):
    chat_id: str
    messages: List[ChatMessage] = Field(default_factory=list)

class ChatRequest(BaseModel):
    user_id: str
    chat_id: Optional[str] = None
    message: str

class UserProfile(BaseModel):
    user_id: str
    name: str
    role: str
    team: str
