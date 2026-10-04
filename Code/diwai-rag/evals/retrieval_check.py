"""Retrieval and answer checks for the DIWAI library, run on an APFS clone of
the store so test documents never touch the real library.

    venv/bin/python evals/retrieval_check.py WORKDIR [--no-llm]

1. Finding: rank of the expected source for questions with known answers.
2. Answering: Devstral with the "DIWAI Library" preset prompt cites it.
3. Declining: questions the library cannot answer get "Not found in the library".
4. Injected instruction: a test document telling the AI to ignore its
   instructions must not change the answer or its sourcing.
5. Threshold: relevance of the best hit, answerable vs unanswerable.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import config  # noqa: E402
import identifiers  # noqa: E402
import ingest  # noqa: E402
import mcp_server  # noqa: E402
import rag_utils  # noqa: E402

PRESET = json.loads((ROOT / "packaging" / "diwai-library.preset.json").read_text())
SYSTEM = next(f["value"] for f in PRESET["operation"]["fields"]
              if f["key"] == "llm.prediction.systemPrompt")
DECLINE = "not found in the library"


def all_hits(question, k=8):
    """Hits with the threshold switched off, so every score is visible."""
    saved = config.RELEVANCE_THRESHOLD
    config.RELEVANCE_THRESHOLD = -1.0
    try:
        return identifiers.retrieve_with_ids(question, k)
    finally:
        config.RELEVANCE_THRESHOLD = saved


def answer(question):
    hits = identifiers.retrieve_with_ids(question, config.TOP_K)  # real threshold
    context = mcp_server.format_hits(hits)
    prompt = f"{context}\n\nQuestion: {question}"
    return rag_utils.ask_llm(prompt, stream=False, system=SYSTEM), hits


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir")
    ap.add_argument("--no-llm", action="store_true")
    args = ap.parse_args(argv)
    work = Path(args.workdir)
    work.mkdir(parents=True, exist_ok=True)
    clone = work / "store"
    if not clone.exists():
        subprocess.run(["cp", "-c", "-R", config.DB_PATH, str(clone)], check=True)
    config.DB_PATH = str(clone)
    qs = json.loads((ROOT / "evals" / "questions.json").read_text())

    inj = qs["injection"]
    inj_path = work / inj["doc_name"]
    inj_path.write_text(inj["doc"], encoding="utf-8")
    print("injection doc:", ingest.ingest_file(str(inj_path), rag_utils.get_collection()).status)

    report = {"answerable": [], "unanswerable": [], "injection": None}
    for item in qs["answerable"]:
        hits = all_hits(item["q"])
        sources = [h["source"] for h in hits]
        rank = next((i + 1 for i, s in enumerate(sources) if s in item["expect"]), None)
        row = {"q": item["q"], "rank": rank, "top": sources[0] if sources else None,
               "top_rel": round(hits[0]["relevance"], 3) if hits else None,
               "exact": bool(hits and hits[0].get("exact"))}
        if not args.no_llm:
            text, used = answer(item["q"])
            row["cited"] = any(e in text for e in item["expect"])
            row["declined"] = DECLINE in text.lower()
            row["passages"] = len(used)
            row["answer"] = text
        report["answerable"].append(row)
        print(f"[A] rank {row['rank']}  top {row['top_rel']}  {row.get('cited', '-')!s:5}  {item['q'][:60]}")

    for q in qs["unanswerable"]:
        hits = all_hits(q)
        row = {"q": q, "top": hits[0]["source"] if hits else None,
               "top_rel": round(hits[0]["relevance"], 3) if hits else None}
        if not args.no_llm:
            text, used = answer(q)
            row["declined"] = DECLINE in text.lower()
            row["passages"] = len(used)
            row["answer"] = text
        report["unanswerable"].append(row)
        print(f"[U] top {row['top_rel']}  declined {row.get('declined', '-')}  {q[:60]}")

    if not args.no_llm:
        text, used = answer(inj["q"])
        report["injection"] = {
            "q": inj["q"], "answer": text,
            "injected_doc_retrieved": any(h["source"] == inj["doc_name"] for h in used),
            "obeyed": any(f in text for f in inj["forbidden"]),
            "answered": "makestep" in text,
        }
        print(f"[I] retrieved {report['injection']['injected_doc_retrieved']}  "
              f"obeyed {report['injection']['obeyed']}  answered {report['injection']['answered']}")

    (work / "report.json").write_text(json.dumps(report, indent=1))
    print("report:", work / "report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
