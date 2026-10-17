"""Evaluation test runner for Asset Intelligence Copilot against Q1 to Q10 in 03-evaluation-queries.md.
Sends queries through POST /api/chat as the appropriate user.
Validates key facts in answer text, citations, and visual types.
Measures latency and number of Gemma calls per question.
"""
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.schemas.chat import ChatResponse
from backend.app.db.connection import get_connection


def count_gemma_calls() -> int:
    """Returns the total number of agent_planner and agent_answer calls recorded in DuckDB."""
    try:
        conn = get_connection(read_only=True)
        count = conn.execute("""
            SELECT COUNT(*) FROM llm_calls
            WHERE role IN ('agent_planner', 'agent_answer')
        """).fetchone()[0]
        conn.close()
        return int(count)
    except Exception:
        return 0


# Evaluation checkers for Q1 to Q10

def check_q1(resp: ChatResponse) -> Tuple[bool, str]:
    """Q1: WELL-0001 status card, not producing, INS-0001-0203, Ryan Brooks, 15 Oct, 3.2 °C."""
    ans = resp.answer.lower()
    if not ("not producing" in ans or "no" in ans):
        return False, f"Answer does not state well is not producing: {resp.answer}"
    if "ins-0001-0203" not in ans and not any(c.id == "INS-0001-0203" for c in resp.citations):
        return False, "Missing inspection INS-0001-0203 in answer or citations"
    if "ryan brooks" not in ans:
        return False, "Missing inspector Ryan Brooks in answer"
    if "15 oct" not in ans and "2026-10-15" not in ans:
        return False, "Missing inspection date 15 Oct 2026 in answer"
    if not resp.visual or resp.visual.get("type") != "status_card":
        return False, f"Expected visual.type == 'status_card', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


def check_q2(resp: ChatResponse) -> Tuple[bool, str]:
    """Q2: 4 wells in Northeast Block 8 not producing (WELL-0164, WELL-0170, WELL-0172, WELL-0175). Table."""
    ans = resp.answer
    wells = ["WELL-0164", "WELL-0170", "WELL-0172", "WELL-0175"]
    missing_wells = [w for w in wells if w not in ans and not any(w in str(r) for r in (resp.visual.get("rows", []) if resp.visual else []))]
    if missing_wells:
        return False, f"Missing non-producing wells: {missing_wells}"
    if not resp.visual or resp.visual.get("type") != "table":
        return False, f"Expected visual.type == 'table', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


def check_q3(resp: ChatResponse) -> Tuple[bool, str]:
    """Q3: Line chart of 13 weeks of temperatures for WELL-0001, not producing on 8 Oct and 15 Oct."""
    ans = resp.answer.lower()
    if "13" not in ans:
        return False, f"Expected mention of 13 weeks/readings, got {resp.answer}"
    if not resp.visual or resp.visual.get("type") != "line_chart":
        return False, f"Expected visual.type == 'line_chart', got {resp.visual.get('type') if resp.visual else None}"
    markers = resp.visual.get("markers", [])
    marker_xs = [m.get("x") for m in markers]
    if not any("2026-10-08" in str(x) or "2026-10-15" in str(x) for x in marker_xs):
        return False, f"Line chart markers missing 8 Oct or 15 Oct: {marker_xs}"
    return True, "OK"


def check_q4(resp: ChatResponse) -> Tuple[bool, str]:
    """Q4: 6 oil spills, 15.1 barrels total for WELL-0001 over last 4 years. Rainwater correction."""
    ans = resp.answer.lower()
    if "6" not in ans:
        return False, f"Expected mention of 6 spills, got {resp.answer}"
    if "15.1" not in ans:
        return False, f"Expected mention of 15.1 barrels, got {resp.answer}"
    if not resp.visual or resp.visual.get("type") != "table":
        return False, f"Expected visual.type == 'table', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


def check_q5(resp: ChatResponse) -> Tuple[bool, str]:
    """Q5: WELL-0001 down 21 days in 2025 from 3 inspections (24 Jul, 16 Oct, 23 Oct)."""
    ans = resp.answer.lower()
    if "21" not in ans:
        return False, f"Expected mention of 21 days, got {resp.answer}"
    return True, "OK"


def check_q6(resp: ChatResponse) -> Tuple[bool, str]:
    """Q6: Top 3 downtime wells in Northeast Block 7 (WELL-0121 49d, WELL-0138 42d, WELL-0107 42d). Bar chart."""
    ans = resp.answer
    if "WELL-0121" not in ans and not any("WELL-0121" in str(c) for c in (resp.visual.get("categories", []) if resp.visual else [])):
        return False, "Missing WELL-0121 in answer/categories"
    if "49" not in ans and not any(49 in s.get("values", []) for s in (resp.visual.get("series", []) if resp.visual else [])):
        return False, "Missing 49 days for WELL-0121"
    if not resp.visual or resp.visual.get("type") != "bar_chart":
        return False, f"Expected visual.type == 'bar_chart', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


def check_q7(resp: ChatResponse) -> Tuple[bool, str]:
    """Q7: Map with 4 pins for Northeast Block 8 spills in last 90 days (WELL-0151, -0165, -0175, -0186)."""
    if not resp.visual or resp.visual.get("type") != "map":
        return False, f"Expected visual.type == 'map', got {resp.visual.get('type') if resp.visual else None}"
    pins = resp.visual.get("pins", [])
    if len(pins) != 4:
        return False, f"Expected 4 map pins, got {len(pins)}"
    pin_labels = [p.get("label") for p in pins]
    for w in ["WELL-0151", "WELL-0165", "WELL-0175", "WELL-0186"]:
        if w not in pin_labels:
            return False, f"Pin label {w} not found in map pins: {pin_labels}"
    return True, "OK"


def check_q8(resp: ChatResponse) -> Tuple[bool, str]:
    """Q8: Heatmap of 2026 spills by area and month (totals 35, 43, 37, 26)."""
    if not resp.visual or resp.visual.get("type") != "heatmap":
        return False, f"Expected visual.type == 'heatmap', got {resp.visual.get('type') if resp.visual else None}"
    rows = resp.visual.get("rows", [])
    values = resp.visual.get("values", [])
    if len(rows) != 4 or len(values) != 4:
        return False, f"Expected 4 heatmap rows, got rows={len(rows)}, values={len(values)}"
    row_totals = [sum(r_vals) for r_vals in values]
    if 35 not in row_totals or 43 not in row_totals or 37 not in row_totals or 26 not in row_totals:
        return False, f"Expected row totals [35, 43, 37, 26], got {row_totals}"
    return True, "OK"


def check_q9(resp: ChatResponse) -> Tuple[bool, str]:
    """Q9: 4 breaches for WELL-0001 (SR-01, SR-02, SR-03, RC-04), USD 5,000 fine open."""
    ans = resp.answer.lower()
    if "4" not in ans and "four" not in ans:
        return False, f"Expected mention of 4 breaches, got {resp.answer}"
    if "5,000" not in ans and "5000" not in ans:
        return False, f"Expected mention of USD 5,000 fine, got {resp.answer}"
    # Citations
    c_ids = [c.id for c in resp.citations]
    if "REG-0001-001" not in c_ids and "REG-0001-002" not in c_ids:
        return False, f"Missing regulatory citation in citations: {c_ids}"
    if not resp.visual or resp.visual.get("type") != "table":
        return False, f"Expected visual.type == 'table', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


def check_q10(resp: ChatResponse) -> Tuple[bool, str]:
    """Q10: Southwest Block 24 uncontained spills (WELL-0082 ~7.1h, WELL-0100 ~8.1h)."""
    ans = resp.answer
    if "WELL-0082" not in ans and not any("WELL-0082" in str(r) for r in (resp.visual.get("rows", []) if resp.visual else [])):
        return False, f"Missing WELL-0082 in answer/rows: {resp.answer}"
    if "WELL-0100" not in ans and not any("WELL-0100" in str(r) for r in (resp.visual.get("rows", []) if resp.visual else [])):
        return False, f"Missing WELL-0100 in answer/rows: {resp.answer}"
    if "7.1" not in ans and not any("7.1" in str(r) for r in (resp.visual.get("rows", []) if resp.visual else [])):
        return False, "Missing 7.1 hours for WELL-0082"
    if "8.1" not in ans and not any("8.1" in str(r) for r in (resp.visual.get("rows", []) if resp.visual else [])):
        return False, "Missing 8.1 hours for WELL-0100"
    if not resp.visual or resp.visual.get("type") != "table":
        return False, f"Expected visual.type == 'table', got {resp.visual.get('type') if resp.visual else None}"
    return True, "OK"


EVAL_CASES = [
    {
        "id": "Q1",
        "user_id": "U-201",
        "query": "Is WELL-0001 producing oil right now? When was it last inspected, and by whom? Show me its status card.",
        "check_fn": check_q1,
    },
    {
        "id": "Q2",
        "user_id": "U-201",
        "query": "Which wells in Northeast Block 8 are not producing oil right now, and why? Show them in a table.",
        "check_fn": check_q2,
    },
    {
        "id": "Q3",
        "user_id": "U-201",
        "query": "Show a line chart of WELL-0001's wellhead temperature against air temperature for the last 13 weeks, and mark when it was not producing oil.",
        "check_fn": check_q3,
    },
    {
        "id": "Q4",
        "user_id": "U-201",
        "query": "How many oil spills has WELL-0001 had in the last 4 years, and how much oil in total? List them in a table.",
        "check_fn": check_q4,
    },
    {
        "id": "Q5",
        "user_id": "U-201",
        "query": "How many days was WELL-0001 down in 2025?",
        "check_fn": check_q5,
    },
    {
        "id": "Q6",
        "user_id": "U-201",
        "query": "Which 3 wells in Northeast Block 7 had the most downtime in the last 4 months? Show a bar chart.",
        "check_fn": check_q6,
    },
    {
        "id": "Q7",
        "user_id": "U-201",
        "query": "Show on a map every well in Northeast Block 8 with a real spill in the last 90 days.",
        "check_fn": check_q7,
    },
    {
        "id": "Q8",
        "user_id": "U-201",
        "query": "Show a heatmap of 2026 spills by geographic area and month.",
        "check_fn": check_q8,
    },
    {
        "id": "Q9",
        "user_id": "U-201",
        "query": "Which rules has WELL-0001 broken in the last 12 months, and what is still open?",
        "check_fn": check_q9,
    },
    {
        "id": "Q10",
        "user_id": "U-201",
        "query": "In Southwest Block 24, which spills in the last 90 days were not contained within the SOP time limit?",
        "check_fn": check_q10,
    },
]


def run_evaluation() -> bool:
    """Executes evaluation across all questions Q1 to Q10."""
    client = TestClient(app)
    results = []
    all_passed = True

    print("\n" + "=" * 90)
    print("RUNNING STAGE 4 EVALUATION (Q1 to Q10) AGAINST FASTAPI /api/chat ENDPOINT")
    print("=" * 90 + "\n")

    for case in EVAL_CASES:
        q_id = case["id"]
        q_user = case["user_id"]
        q_text = case["query"]
        check_fn = case["check_fn"]

        calls_before = count_gemma_calls()
        t_start = time.time()

        try:
            http_resp = client.post(
                "/api/chat",
                json={"user_id": q_user, "message": q_text},
            )
            elapsed_sec = time.time() - t_start

            if http_resp.status_code != 200:
                print(f"[{q_id}] FAIL - HTTP {http_resp.status_code}: {http_resp.text}")
                results.append({
                    "id": q_id,
                    "status": "FAIL",
                    "latency": elapsed_sec,
                    "calls": 0,
                    "tool": "None",
                    "visual": "None",
                    "citations": 0,
                    "reason": f"HTTP {http_resp.status_code}",
                })
                all_passed = False
                continue

            resp_data = http_resp.json()
            chat_resp = ChatResponse.model_validate(resp_data)
            calls_after = count_gemma_calls()
            calls_made = calls_after - calls_before

            is_pass, reason = check_fn(chat_resp)
            status_str = "PASS" if is_pass else "FAIL"

            tool_chosen = chat_resp.meta.tool_calls[0] if chat_resp.meta.tool_calls else "None"
            vis_type = chat_resp.visual.get("type", "None") if chat_resp.visual else "None"
            cit_count = len(chat_resp.citations)

            print(f"[{q_id}] {status_str} | Tool: {tool_chosen:<22} | Calls: {calls_made} | Latency: {elapsed_sec:.2f}s | Visual: {vis_type:<11} | Citations: {cit_count}")

            if not is_pass:
                print(f"   [DIAGNOSIS] Question: {q_text}")
                print(f"   [DIAGNOSIS] Tool Calls: {chat_resp.meta.tool_calls}")
                print(f"   [DIAGNOSIS] Reason: {reason}")
                print(f"   [DIAGNOSIS] Answer: {chat_resp.answer}")
                all_passed = False

            results.append({
                "id": q_id,
                "status": status_str,
                "latency": elapsed_sec,
                "calls": calls_made,
                "tool": tool_chosen,
                "visual": vis_type,
                "citations": cit_count,
                "reason": reason,
            })

        except Exception as e:
            elapsed_sec = time.time() - t_start
            print(f"[{q_id}] FAIL - Exception: {e}")
            results.append({
                "id": q_id,
                "status": "FAIL",
                "latency": elapsed_sec,
                "calls": 0,
                "tool": "Exception",
                "visual": "None",
                "citations": 0,
                "reason": str(e),
            })
            all_passed = False

    # Print summary markdown table
    print("\n" + "=" * 90)
    print("STAGE 4 EVALUATION SUMMARY TABLE")
    print("=" * 90)
    print("| Question | Status | Tool Selected | Calls | Latency (s) | Visual Type | Citations |")
    print("|---|---|---|---|---|---|---|")
    for r in results:
        print(f"| {r['id']:<8} | {r['status']:<6} | {r['tool']:<23} | {r['calls']:<5} | {r['latency']:<11.2f} | {r['visual']:<11} | {r['citations']:<9} |")
    print("=" * 90 + "\n")

    return all_passed


if __name__ == "__main__":
    success = run_evaluation()
    sys.exit(0 if success else 1)
