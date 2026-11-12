#!/usr/bin/env python3
"""Ugradi banku pitanja i rečnik u template.html -> index.html (jedan fajl, bez servera).

Pokretanje:  python3 07_simulator/build.py
U simulator ulaze SAMO pitanja sa "preverjeno": true.
"""
import csv
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SIM = ROOT / "07_simulator"


def js(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def main():
    bank_path = ROOT / "06_banka_pitanja.json"
    voc_path = ROOT / "05_recnik.csv"
    bank_all = json.loads(bank_path.read_text(encoding="utf-8")) if bank_path.exists() else []
    problems = []
    bank = []
    seen = set()
    for q in bank_all:
        qid = q.get("id", "?")
        if qid in seen:
            problems.append(f"{qid}: dupli id")
        seen.add(qid)
        if not q.get("preverjeno"):
            continue
        ans = q.get("odgovori", [])
        n_ok = sum(1 for a in ans if a.get("pravilno"))
        if not q.get("vprasanje_sl") or len(ans) < 2 or n_ok < 1:
            problems.append(f"{qid}: neispravna struktura (odgovora {len(ans)}, tačnih {n_ok})")
            continue
        vir = q.get("vir") or {}
        if not any(vir.get(k) for k in ("literatura_str", "zakon_clen", "url")):
            problems.append(f"{qid}: nema izvora")
            continue
        if not q.get("poreklo"):
            problems.append(f"{qid}: nema porekla")
            continue
        bank.append(q)

    vocab = []
    if voc_path.exists():
        with voc_path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="|"):
                row = {(k or "").strip(): (v or "").strip() for k, v in row.items()}
                if row.get("termin_sl"):
                    vocab.append(row)

    poreklo = {}
    for q in bank:
        poreklo[q["poreklo"]] = poreklo.get(q["poreklo"], 0) + 1
    meta = {
        "built": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "excluded": len(bank_all) - len(bank),
        "poreklo": poreklo,
    }
    html = (SIM / "template.html").read_text(encoding="utf-8")
    html = html.replace("__BANK__", js(bank)).replace("__VOCAB__", js(vocab)).replace("__META__", js(meta))
    (SIM / "index.html").write_text(html, encoding="utf-8")
    print(f"index.html: pitanja {len(bank)} / {len(bank_all)} (izbačeno {meta['excluded']}), rečnik {len(vocab)}, poreklo {poreklo}")
    for p in problems:
        print("PROBLEM:", p, file=sys.stderr)


if __name__ == "__main__":
    main()
