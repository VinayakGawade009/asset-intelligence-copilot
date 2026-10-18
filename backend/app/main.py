"""FastAPI backend application for Asset Intelligence Copilot conforming to UI_CONTRACT.md."""
import json
import uuid
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import duckdb

from backend.app.db.connection import get_connection
from backend.app.db.schema import init_db
from backend.app.derived.views import create_derived_views
from backend.app.agent.agent import AgentRunner
from backend.app.schemas.chat import (
    UserProfile,
    ChatSession,
    ChatMessage,
    ChatDetail,
    ChatRequest,
    ChatResponse,
)

app = FastAPI(
    title="Asset Intelligence Copilot API",
    description="Backend API conforming to UI_CONTRACT.md for autonomous oil & gas asset intelligence.",
    version="1.0.0",
)

# Add CORS for Vite frontend development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent_runner = AgentRunner()


@app.on_event("startup")
def on_startup():
    """Initializes tables and derived views on startup."""
    conn = get_connection(read_only=False)
    init_db(conn)
    create_derived_views(conn)
    conn.close()


@app.get("/api/users", response_model=List[UserProfile])
def get_users():
    """GET /api/users -> [{user_id, name, role, team}]"""
    conn = get_connection(read_only=True)
    rows = conn.execute("""
        SELECT u.user_id, u.name, u.role, COALESCE(t.name, 'Operations') as team
        FROM users u
        LEFT JOIN teams t ON u.team_id = t.team_id
        ORDER BY u.user_id ASC
    """).fetchall()
    conn.close()
    return [
        UserProfile(user_id=r[0], name=r[1], role=r[2], team=r[3])
        for r in rows
    ]


@app.get("/api/chats", response_model=List[ChatSession])
def get_chats(user_id: Optional[str] = Query(None)):
    """GET /api/chats?user_id=<user_id> -> [{chat_id, title, updated_at}]"""
    conn = get_connection(read_only=True)
    if user_id:
        rows = conn.execute("""
            SELECT chat_id, title, updated_at
            FROM chats
            WHERE user_id = ?
            ORDER BY updated_at DESC
        """, [user_id]).fetchall()
    else:
        rows = conn.execute("""
            SELECT chat_id, title, updated_at
            FROM chats
            ORDER BY updated_at DESC
        """).fetchall()
    conn.close()

    return [
        ChatSession(
            chat_id=r[0],
            title=r[1],
            updated_at=r[2].isoformat() if r[2] else None,
        )
        for r in rows
    ]


@app.get("/api/chats/{chat_id}", response_model=ChatDetail)
def get_chat_detail(chat_id: str):
    """GET /api/chats/{chat_id} -> {chat_id, messages: [{role: 'user'|'assistant', text, response?}]}"""
    conn = get_connection(read_only=True)
    rows = conn.execute("""
        SELECT message_id, role, text, response_json, created_at
        FROM chat_messages
        WHERE chat_id = ?
        ORDER BY created_at ASC
    """, [chat_id]).fetchall()
    conn.close()

    messages = []
    for m_id, role, text, resp_json, created_at in rows:
        resp_obj = None
        if resp_json:
            try:
                resp_obj = ChatResponse.model_validate_json(resp_json)
            except Exception:
                pass
        messages.append(ChatMessage(role=role, text=text, response=resp_obj))

    return ChatDetail(chat_id=chat_id, messages=messages)


@app.post("/api/chat", response_model=ChatResponse)
def post_chat(req: ChatRequest):
    """
    POST /api/chat body: {user_id, chat_id | null, message} -> ChatResponse
    """
    chat_id = req.chat_id or f"chat_{uuid.uuid4().hex[:10]}"
    now = datetime.now(timezone.utc)

    # 1. Process with Gemma 4 agent loop
    chat_response = agent_runner.process_query(
        user_message=req.message,
        user_id=req.user_id,
        chat_id=chat_id,
    )

    # 2. Persist in DuckDB
    conn = get_connection(read_only=False)
    # Ensure chat session exists
    chat_row = conn.execute("SELECT chat_id FROM chats WHERE chat_id = ?", [chat_id]).fetchone()
    if not chat_row:
        title = req.message[:40] + ("..." if len(req.message) > 40 else "")
        conn.execute("""
            INSERT INTO chats (chat_id, user_id, title, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """, [chat_id, req.user_id, title, now, now])
    else:
        conn.execute("UPDATE chats SET updated_at = ? WHERE chat_id = ?", [now, chat_id])

    # Store user message
    u_msg_id = f"msg_{uuid.uuid4().hex[:10]}"
    conn.execute("""
        INSERT INTO chat_messages (message_id, chat_id, role, text, response_json, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [u_msg_id, chat_id, "user", req.message, None, now])

    # Store assistant message with serialized ChatResponse
    a_msg_id = f"msg_{uuid.uuid4().hex[:10]}"
    resp_json = chat_response.model_dump_json()
    conn.execute("""
        INSERT INTO chat_messages (message_id, chat_id, role, text, response_json, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [a_msg_id, chat_id, "assistant", chat_response.answer, resp_json, now])

    conn.close()
    return chat_response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
