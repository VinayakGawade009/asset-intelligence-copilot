"""Stage 5 Evaluation Suite: Memory, Corrections, Shared Facts, and Conflict Resolution.
Evaluates Q11 through Q18 across multiple user personas via POST /api/chat.
Writes progress incrementally to backend/eval/results_stage5.json.
"""
import os
import sys
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.schemas.chat import ChatResponse
from backend.app.db.connection import get_connection

RESULTS_FILE = project_root / "backend" / "eval" / "results_stage5.json"


def count_gemma_calls() -> int:
    """Returns total count of LLM calls in DuckDB."""
    try:
        conn = get_connection(read_only=True)
        count = conn.execute("SELECT COUNT(*) FROM llm_calls").fetchone()[0]
        conn.close()
        return int(count)
    except Exception:
        return 0


def update_results_file(part_key: str, data: Any):
    """Incrementally updates results_stage5.json."""
    existing = {}
    if RESULTS_FILE.exists():
        try:
            with open(RESULTS_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = {}
    existing[part_key] = data
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)


def run_part1(client: TestClient) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    PART 1: private memory + shared facts (Q11, Q16)
    - Q11: Michael Turner asks Q6 (Day 1). In Day 2 new chat, asks repairs cost for 'the three wells we discussed yesterday'.
    - Q16: Jake Morales shares shut-in FYI for WELL-0007. Michael Turner asks about WELL-0007 downtime.
           Jessica Reed asks for 'the three wells we discussed yesterday' -> must get no earlier conversation.
    """
    print("\n" + "=" * 80)
    print("RUNNING PART 1: PRIVATE MEMORY + SHARED FACTS (Q11, Q16)")
    print("=" * 80)
    part_results = []
    all_ok = True

    # -------------------------------------------------------------
    # Q11: Michael Turner (U-201)
    # -------------------------------------------------------------
    print("\n--- Testing Q11 (Private memory across chats) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    # Day 1: Q6 in chat_day1
    resp_day1 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_day1",
        "message": "Which 3 wells in Northeast Block 7 had the most downtime in the last 4 months? Show a bar chart.",
    })
    if resp_day1.status_code != 200:
        print(f"[Q11 - Day 1] HTTP Error {resp_day1.status_code}: {resp_day1.text}")

    # Day 2: Q11 in new chat chat_day2
    resp_day2 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_day2",
        "message": "For the three wells we discussed yesterday, what have repairs cost this year?",
    })
    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q11_pass = False
    q11_reason = "OK"
    if resp_day2.status_code != 200:
        q11_reason = f"HTTP {resp_day2.status_code}"
    else:
        ans2 = resp_day2.json().get("answer", "")
        ans_low = ans2.lower()
        # Expected: WELL-0121: USD 25,794; WELL-0138: USD 46,942; WELL-0107: USD 5,176
        has_121 = "25,794" in ans2 or "25794" in ans2
        has_138 = "46,942" in ans2 or "46942" in ans2
        has_107 = "5,176" in ans2 or "5176" in ans2
        if has_121 and has_138 and has_107:
            q11_pass = True
        else:
            q11_reason = f"Missing repair costs in answer: {ans2}"

    status_str = "PASS" if q11_pass else "FAIL"
    print(f"[Q11] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q11_reason}")
    if not q11_pass:
        all_ok = False
    part_results.append({
        "id": "Q11",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q11_reason,
    })

    # -------------------------------------------------------------
    # Q16: Shared knowledge, private memory
    # -------------------------------------------------------------
    print("\n--- Testing Q16 (Shared knowledge & user isolation) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    # Step 1: Jake Morales shares fact about WELL-0007
    resp_jake = client.post("/api/chat", json={
        "user_id": "U-102",
        "chat_id": "chat_jake_1",
        "message": "FYI for everyone: WELL-0007 will be shut in from 17 Oct for a 10-day planned workover.",
    })

    # Step 2: Michael Turner in new chat asks about WELL-0007 downtime
    resp_turner = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q16",
        "message": "Is any downtime planned for WELL-0007?",
    })

    # Step 3: Jessica Reed asks about yesterday's wells (must not see Turner's wells)
    resp_jessica = client.post("/api/chat", json={
        "user_id": "U-202",
        "chat_id": "chat_jessica_1",
        "message": "For the three wells we discussed yesterday, what have repairs cost this year?",
    })
    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q16_pass = True
    q16_reasons = []

    if resp_turner.status_code != 200:
        q16_pass = False
        q16_reasons.append(f"Turner HTTP {resp_turner.status_code}")
    else:
        ans_t = resp_turner.json().get("answer", "").lower()
        if not ("yes" in ans_t and ("17 oct" in ans_t or "10" in ans_t) and "jake morales" in ans_t):
            q16_pass = False
            q16_reasons.append(f"Turner did not get Jake's shared fact: {ans_t}")

    if resp_jessica.status_code != 200:
        q16_pass = False
        q16_reasons.append(f"Jessica HTTP {resp_jessica.status_code}")
    else:
        ans_j = resp_jessica.json().get("answer", "").lower()
        if not ("no record" in ans_j or "no such" in ans_j or "private" in ans_j or "earlier conversation" in ans_j):
            q16_pass = False
            q16_reasons.append(f"Jessica incorrectly accessed private memory: {ans_j}")

    q16_reason_str = "OK" if q16_pass else "; ".join(q16_reasons)
    status_str = "PASS" if q16_pass else "FAIL"
    print(f"[Q16] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q16_reason_str}")
    if not q16_pass:
        all_ok = False
    part_results.append({
        "id": "Q16",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q16_reason_str,
    })

    update_results_file("PART_1", part_results)
    return all_ok, part_results


def run_part2(client: TestClient) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    PART 2: corrections (Q12, Q13, Q15)
    - Q12: Michael Turner corrects WELL-0164 wellhead to 41.0 °C. Copilot notes 'Pump jack not moving.' note disagrees.
           Then Michael Turner asks Q2 again -> only 3 wells returned (WELL-0170, -0172, -0175).
    - Q13: Michael Turner corrects WELL-0151 spill volume to 5.4 bbl -> reportable, SR-01 notice overdue, MNT-0151-025 outdated, SR-03 due 23 Nov 2026.
    - Q15: Jessica Reed asks if WELL-0164 is producing oil -> yes (Michael Turner correction, pump jack note).
           Laura Simmons asks which spills needed report -> WELL-0151 (5.4 bbl, overdue notice).
    """
    print("\n" + "=" * 80)
    print("RUNNING PART 2: CORRECTIONS (Q12, Q13, Q15)")
    print("=" * 80)
    part_results = []
    all_ok = True

    # -------------------------------------------------------------
    # Q12: Raw data correction & re-evaluation
    # -------------------------------------------------------------
    print("\n--- Testing Q12 (Raw data temperature correction) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    # Step 1: Submit correction
    resp_corr = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q12",
        "message": "The 15 Oct reading for WELL-0164 is wrong. The handheld thermal gun used in that inspection was faulty; the field crew re-measured the wellhead at 41.0 °C.",
    })

    # Step 2: Ask Q2 again
    resp_q2_again = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q12",
        "message": "Which wells in Northeast Block 8 are not producing oil right now, and why? Show them in a table.",
    })
    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q12_pass = True
    q12_reasons = []

    if resp_corr.status_code != 200:
        q12_pass = False
        q12_reasons.append(f"Correction HTTP {resp_corr.status_code}")
    else:
        ans_c = resp_corr.json().get("answer", "").lower()
        if not ("41.0" in ans_c and "24.0" in ans_c and "producing" in ans_c):
            q12_pass = False
            q12_reasons.append(f"Correction text missing 41.0 / 24.0 / producing: {ans_c}")
        if not ("pump jack not moving" in ans_c or "disagree" in ans_c or "confirm" in ans_c):
            q12_pass = False
            q12_reasons.append(f"Correction missing note conflict warning: {ans_c}")

    if resp_q2_again.status_code != 200:
        q12_pass = False
        q12_reasons.append(f"Q2 HTTP {resp_q2_again.status_code}")
    else:
        data_q2 = resp_q2_again.json()
        vis = data_q2.get("visual") or {}
        rows = vis.get("rows", [])
        row_wells = [r.get("well") for r in rows]
        if "WELL-0164" in row_wells or len(rows) != 3:
            q12_pass = False
            q12_reasons.append(f"Expected 3 wells without WELL-0164, got rows: {row_wells}")
        ans_q2 = data_q2.get("answer", "").lower()
        if "well-0164" not in ans_q2 and "0164" not in ans_q2:
            q12_pass = False
            q12_reasons.append("Answer does not explain why WELL-0164 is omitted")

    q12_reason_str = "OK" if q12_pass else "; ".join(q12_reasons)
    status_str = "PASS" if q12_pass else "FAIL"
    print(f"[Q12] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q12_reason_str}")
    if not q12_pass:
        all_ok = False
    part_results.append({
        "id": "Q12",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q12_reason_str,
    })

    # -------------------------------------------------------------
    # Q13: AI analysis correction & breach re-evaluation
    # -------------------------------------------------------------
    print("\n--- Testing Q13 (AI analysis volume correction) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    resp_q13 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q13",
        "message": "The AI estimated the 24 Sep spill at WELL-0151 as 4.5 bbl. The field crew measured 5.4 bbl.",
    })
    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q13_pass = True
    q13_reasons = []

    if resp_q13.status_code != 200:
        q13_pass = False
        q13_reasons.append(f"HTTP {resp_q13.status_code}")
    else:
        ans13 = resp_q13.json().get("answer", "").lower()
        if not ("5.4" in ans13 and "4.5" in ans13):
            q13_pass = False
            q13_reasons.append(f"Missing 5.4 or 4.5: {ans13}")
        if not ("reportable" in ans13):
            q13_pass = False
            q13_reasons.append(f"Missing reportable: {ans13}")
        if not ("overdue" in ans13 or "sr-01" in ans13 or "notice" in ans13):
            q13_pass = False
            q13_reasons.append(f"Missing notice overdue/SR-01: {ans13}")
        if not ("23 nov" in ans13 or "60 days" in ans13 or "sr-03" in ans13):
            q13_pass = False
            q13_reasons.append(f"Missing SR-03 / 23 Nov: {ans13}")

    q13_reason_str = "OK" if q13_pass else "; ".join(q13_reasons)
    status_str = "PASS" if q13_pass else "FAIL"
    print(f"[Q13] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q13_reason_str}")
    if not q13_pass:
        all_ok = False
    part_results.append({
        "id": "Q13",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q13_reason_str,
    })

    # -------------------------------------------------------------
    # Q15: Corrections reach other users (Jessica Reed, Laura Simmons)
    # -------------------------------------------------------------
    print("\n--- Testing Q15 (Corrections reach other users) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    # Step 1: Jessica Reed asks about WELL-0164
    resp_jess = client.post("/api/chat", json={
        "user_id": "U-202",
        "chat_id": "chat_jessica_q15",
        "message": "Is WELL-0164 producing oil right now?",
    })

    # Step 2: Laura Simmons asks about spills needing report
    resp_laura = client.post("/api/chat", json={
        "user_id": "U-401",
        "chat_id": "chat_laura_q15",
        "message": "Which spills in Northeast Block 8 in the last 90 days needed a report to the regulator?",
    })
    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q15_pass = True
    q15_reasons = []

    if resp_jess.status_code != 200:
        q15_pass = False
        q15_reasons.append(f"Jessica HTTP {resp_jess.status_code}")
    else:
        ans_j = resp_jess.json().get("answer", "").lower()
        if not ("yes" in ans_j or "producing" in ans_j):
            q15_pass = False
            q15_reasons.append(f"Jessica did not get producing=true: {ans_j}")
        if not ("41.0" in ans_j or "michael turner" in ans_j or "corrected" in ans_j):
            q15_pass = False
            q15_reasons.append(f"Jessica did not get Michael Turner correction: {ans_j}")

    if resp_laura.status_code != 200:
        q15_pass = False
        q15_reasons.append(f"Laura HTTP {resp_laura.status_code}")
    else:
        ans_l = resp_laura.json().get("answer", "").lower()
        if not ("well-0151" in ans_l and ("5.4" in ans_l or "overdue" in ans_l)):
            q15_pass = False
            q15_reasons.append(f"Laura did not identify WELL-0151 as needing report: {ans_l}")

    q15_reason_str = "OK" if q15_pass else "; ".join(q15_reasons)
    status_str = "PASS" if q15_pass else "FAIL"
    print(f"[Q15] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q15_reason_str}")
    if not q15_pass:
        all_ok = False
    part_results.append({
        "id": "Q15",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q15_reason_str,
    })

    update_results_file("PART_2", part_results)
    return all_ok, part_results


def run_part3(client: TestClient) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    PART 3: type-wide rules (Q14)
    - Michael Turner first asks for RCA on pump jack in Northeast Block 7 -> WELL-0108, WELL-0121, WELL-0138 (3 repairs).
    - Michael Turner sets rule: 'Note for all T350 wells: our team now wants a pump jack root-cause analysis after 2 repairs, not 3.'
    - In a new chat, he asks again -> WELL-0108, WELL-0120, WELL-0121, WELL-0138.
      Says follows Michael Turner's rule, not the manual.
    """
    print("\n" + "=" * 80)
    print("RUNNING PART 3: TYPE-WIDE RULES (Q14)")
    print("=" * 80)
    part_results = []
    all_ok = True

    calls_start = count_gemma_calls()
    t_start = time.time()

    # Step 1: Baseline Q14 query
    resp1 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q14_before",
        "message": "Which wells in Northeast Block 7 need a root-cause analysis on their pump jack?",
    })

    # Step 2: Set rule override for T350
    resp_rule = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q14_before",
        "message": "Note for all T350 wells: our team now wants a pump jack root-cause analysis after 2 repairs, not 3.",
    })

    # Step 3: In a NEW chat, ask again
    resp2 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q14_after",
        "message": "Which wells in Northeast Block 7 need a root-cause analysis on their pump jack?",
    })

    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q14_pass = True
    q14_reasons = []

    if resp1.status_code != 200:
        q14_pass = False
        q14_reasons.append(f"Step 1 HTTP {resp1.status_code}")
    else:
        vis1 = resp1.json().get("visual") or {}
        rows1 = [r.get("well") for r in vis1.get("rows", [])]
        for expected_w in ["WELL-0108", "WELL-0121", "WELL-0138"]:
            if expected_w not in rows1:
                q14_pass = False
                q14_reasons.append(f"Step 1 missing {expected_w}")
        if "WELL-0120" in rows1:
            q14_pass = False
            q14_reasons.append("Step 1 unexpectedly contained WELL-0120 before override")

    if resp2.status_code != 200:
        q14_pass = False
        q14_reasons.append(f"Step 3 HTTP {resp2.status_code}")
    else:
        data2 = resp2.json()
        vis2 = data2.get("visual") or {}
        rows2 = [r.get("well") for r in vis2.get("rows", [])]
        # Must have WELL-0108, WELL-0120, WELL-0121, WELL-0138
        for expected_w in ["WELL-0108", "WELL-0120", "WELL-0121", "WELL-0138"]:
            if expected_w not in rows2:
                q14_pass = False
                q14_reasons.append(f"Step 3 missing {expected_w} in rows: {rows2}")
        if "WELL-0102" in rows2:
            q14_pass = False
            q14_reasons.append("WELL-0102 (T200) was improperly included under T350 override")
        ans2 = data2.get("answer", "").lower()
        if not ("michael turner" in ans2 or "rule" in ans2 or "not the manual" in ans2):
            q14_pass = False
            q14_reasons.append(f"Answer does not cite Michael Turner's rule: {ans2}")

    q14_reason_str = "OK" if q14_pass else "; ".join(q14_reasons)
    status_str = "PASS" if q14_pass else "FAIL"
    print(f"[Q14] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q14_reason_str}")
    if not q14_pass:
        all_ok = False
    part_results.append({
        "id": "Q14",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q14_reason_str,
    })

    update_results_file("PART_3", part_results)
    return all_ok, part_results


def run_part4(client: TestClient) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    PART 4: conflicts (Q17, Q18)
    - Q17: Michael Turner shares planned shut-in for WELL-0175.
           Tyler Hughes claims WELL-0175 is running fine -> 15 Oct inspection shows not producing (0.4 °C delta),
           matches Turner's note, contradicts Hughes. Both kept, marked unconfirmed, ask for confirmation.
           Jake Morales claims WELL-0001 is back online since 14 Oct -> 15 Oct inspection shows not producing,
           note CTX-0001-003 expects return ~20 Oct. Marked unconfirmed.
    - Q18: Disputed spill classification with competing notes:
           'Was the 20 Aug spill at WELL-0101 real oil?' ->
           Yes, 1.0 bbl detected (INS-0101-0197). Notes disagree (Ryan Brooks CTX-0101-002 produced water vs Chris Dalton CTX-0101-003 crude).
           MNT-0101-029 done. Detection stands. Both sources cited, flagged conflict.
    """
    print("\n" + "=" * 80)
    print("RUNNING PART 4: CONFLICTS (Q17, Q18)")
    print("=" * 80)
    part_results = []
    all_ok = True

    # -------------------------------------------------------------
    # Q17: People disagree with the data
    # -------------------------------------------------------------
    print("\n--- Testing Q17 (People disagree with the data) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    # Step 1: Michael Turner states planned work for WELL-0175
    resp_turner = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q17",
        "message": "WELL-0175 has been shut in for planned work since 14 Oct.",
    })

    # Step 2: Tyler Hughes claims WELL-0175 is running fine
    resp_tyler = client.post("/api/chat", json={
        "user_id": "U-204",
        "chat_id": "chat_tyler_q17",
        "message": "WELL-0175 is running fine.",
    })

    # Step 3: Jake Morales claims WELL-0001 is back online
    resp_jake = client.post("/api/chat", json={
        "user_id": "U-102",
        "chat_id": "chat_jake_q17",
        "message": "WELL-0001 is back online since 14 Oct.",
    })

    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q17_pass = True
    q17_reasons = []

    if resp_tyler.status_code != 200:
        q17_pass = False
        q17_reasons.append(f"Tyler HTTP {resp_tyler.status_code}")
    else:
        d_tyler = resp_tyler.json()
        ans_t = d_tyler.get("answer", "").lower()
        flags_t = [f.get("kind") for f in d_tyler.get("flags", [])]
        if not ("0.4" in ans_t or "15 oct" in ans_t or "not producing" in ans_t):
            q17_pass = False
            q17_reasons.append(f"Tyler answer missing 15 Oct inspection / 0.4 °C / not producing: {ans_t}")
        if not ("michael turner" in ans_t or "turner" in ans_t):
            q17_pass = False
            q17_reasons.append(f"Tyler answer missing Michael Turner note: {ans_t}")
        if not ("unconfirmed" in ans_t or "confirm" in ans_t or "verify" in ans_t):
            q17_pass = False
            q17_reasons.append(f"Tyler answer missing unconfirmed / confirm request: {ans_t}")
        if "conflict" not in flags_t:
            q17_pass = False
            q17_reasons.append("Tyler response missing conflict flag")
        if "unconfirmed" not in flags_t:
            q17_pass = False
            q17_reasons.append("Tyler response missing unconfirmed flag")

    if resp_jake.status_code != 200:
        q17_pass = False
        q17_reasons.append(f"Jake HTTP {resp_jake.status_code}")
    else:
        d_jake = resp_jake.json()
        ans_j = d_jake.get("answer", "").lower()
        flags_j = [f.get("kind") for f in d_jake.get("flags", [])]
        if not ("15 oct" in ans_j or "not producing" in ans_j):
            q17_pass = False
            q17_reasons.append(f"Jake answer missing 15 Oct inspection not producing: {ans_j}")
        if not ("20 oct" in ans_j or "ctx-0001-003" in ans_j):
            q17_pass = False
            q17_reasons.append(f"Jake answer missing CTX-0001-003 / 20 Oct return: {ans_j}")
        if not ("unconfirmed" in ans_j or "confirm" in ans_j):
            q17_pass = False
            q17_reasons.append(f"Jake answer missing unconfirmed status: {ans_j}")
        if "conflict" not in flags_j:
            q17_pass = False
            q17_reasons.append("Jake response missing conflict flag")
        if "unconfirmed" not in flags_j:
            q17_pass = False
            q17_reasons.append("Jake response missing unconfirmed flag")

    q17_reason_str = "OK" if q17_pass else "; ".join(q17_reasons)
    status_str = "PASS" if q17_pass else "FAIL"
    print(f"[Q17] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q17_reason_str}")
    if not q17_pass:
        all_ok = False
    part_results.append({
        "id": "Q17",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q17_reason_str,
    })

    # -------------------------------------------------------------
    # Q18: Disputed spill classification with competing notes
    # -------------------------------------------------------------
    print("\n--- Testing Q18 (Disputed spill classification with competing notes) ---")
    calls_start = count_gemma_calls()
    t_start = time.time()

    resp_q18 = client.post("/api/chat", json={
        "user_id": "U-201",
        "chat_id": "chat_turner_q18",
        "message": "Was the 20 Aug spill at WELL-0101 real oil?",
    })

    elapsed = time.time() - t_start
    calls_used = count_gemma_calls() - calls_start

    q18_pass = True
    q18_reasons = []

    if resp_q18.status_code != 200:
        q18_pass = False
        q18_reasons.append(f"HTTP {resp_q18.status_code}")
    else:
        d18 = resp_q18.json()
        ans18 = d18.get("answer", "").lower()
        cites18 = [c.get("id") for c in d18.get("citations", [])]
        cites18_low = [c.lower() for c in cites18]
        flags18 = [f.get("kind") for f in d18.get("flags", [])]

        if not ans18.startswith("yes"):
            q18_pass = False
            q18_reasons.append(f"Answer should start with Yes: {ans18}")
        if not ("1.0" in ans18 or "ins-0101-0197" in ans18):
            q18_pass = False
            q18_reasons.append(f"Answer missing 1.0 bbl / INS-0101-0197: {ans18}")
        if not ("ryan brooks" in ans18 and "chris dalton" in ans18):
            q18_pass = False
            q18_reasons.append(f"Answer missing authors Ryan Brooks and Chris Dalton: {ans18}")
        if not ("ctx-0101-002" in cites18_low and "ctx-0101-003" in cites18_low):
            q18_pass = False
            q18_reasons.append(f"Citations missing CTX-0101-002 or CTX-0101-003: {cites18}")
        if "conflict" not in flags18:
            q18_pass = False
            q18_reasons.append("Response missing conflict flag")

    q18_reason_str = "OK" if q18_pass else "; ".join(q18_reasons)
    status_str = "PASS" if q18_pass else "FAIL"
    print(f"[Q18] {status_str} | Calls: {calls_used} | Latency: {elapsed:.2f}s | Reason: {q18_reason_str}")
    if not q18_pass:
        all_ok = False
    part_results.append({
        "id": "Q18",
        "status": status_str,
        "calls": calls_used,
        "latency": round(elapsed, 2),
        "reason": q18_reason_str,
    })

    update_results_file("PART_4", part_results)
    return all_ok, part_results


def print_final_summary_table():
    """Prints the final formatted Markdown evaluation table for Q11 through Q18."""
    if not RESULTS_FILE.exists():
        print("No results file found.")
        return

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        results = json.load(f)

    all_items = []
    for part in ["PART_1", "PART_2", "PART_3", "PART_4"]:
        for item in results.get(part, []):
            all_items.append(item)

    print("\n" + "=" * 80)
    print("STAGE 5 EVALUATION RESULTS SUMMARY (Q11 - Q18)")
    print("=" * 80)
    print("| Question | Status | Gemma Calls | Latency (s) | Notes |")
    print("|:---|:---:|:---:|:---:|:---|")
    for it in all_items:
        print(f"| {it['id']} | **{it['status']}** | {it['calls']} | {it['latency']:.2f}s | {it['reason']} |")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    client = TestClient(app)
    run_part4(client)
    print_final_summary_table()

