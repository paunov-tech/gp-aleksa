#!/usr/bin/env python3
"""Spoji delove (S0, T1..T5) u 06_banka_pitanja.json, 05_recnik.csv i 05_anki.tsv.

U banku ulaze SVA pitanja; simulator (07_simulator/build.py) uzima samo "preverjeno": true.
Pitanje čiji izveštaj o proveri još ne postoji (<KOD>_provera.md) ostaje preverjeno=false.
"""
import csv
import json
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent
ROOT = D.parent.parent
KODOVI = ["S0", "T1", "T2", "T3", "T4", "T5"]
# Ručne odluke glavnog agenta (stroža linija od kontrolora):
FORCE_FALSE = {
    "S0-026": "Ključ delom počiva na udžbeničkoj podeli imovinska/upravljačka prava, bez člana zakona za netačne odgovore (odluka glavnog agenta).",
}
FIELDS = ["termin_sl", "prevod_sr", "definicija_sl", "primer_sl", "lazni_prijatelj", "zakon_clen", "tema"]


def main():
    bank, stats = [], {}
    for k in KODOVI:
        p = D / f"{k}_pitanja.json"
        if not p.exists():
            print(f"NEMA: {p.name}", file=sys.stderr)
            continue
        verified_run = (D / f"{k}_provera.md").exists()
        qs = json.loads(p.read_text(encoding="utf-8"))
        ok = 0
        for q in qs:
            if not verified_run:
                q["preverjeno"] = False
                q.setdefault("opomba_preverjanja", "Nezavisna provera još nije završena.")
            if q["id"] in FORCE_FALSE:
                q["preverjeno"] = False
                q["opomba_preverjanja"] = FORCE_FALSE[q["id"]]
            n = len(q["odgovori"])
            c = sum(1 for a in q["odgovori"] if a.get("pravilno"))
            want = 3 if q.get("tip") == "single" else 5
            if n != want or not (1 <= c <= (1 if q.get("tip") == "single" else 4)):
                q["preverjeno"] = False
                q["opomba_preverjanja"] = f"Struktura: {n} odgovora, {c} tačnih."
            ok += bool(q["preverjeno"])
            bank.append(q)
        stats[k] = (len(qs), ok, verified_run)
    ids = [q["id"] for q in bank]
    assert len(ids) == len(set(ids)), "dupli id"
    (ROOT / "06_banka_pitanja.json").write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")

    seen, rows, bad = {}, [], 0
    for k in KODOVI[1:]:
        p = D / f"{k}_recnik.csv"
        if not p.exists():
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for ln in lines[1:]:
            if not ln.strip():
                continue
            parts = [x.strip() for x in ln.split("|")]
            if len(parts) != 7:
                bad += 1
                continue
            key = parts[0].lower()
            if key in seen:
                continue
            seen[key] = 1
            rows.append(parts)
    with (ROOT / "05_recnik.csv").open("w", encoding="utf-8", newline="") as f:
        f.write(" | ".join(FIELDS).replace(" | ", "|") + "\n")
        for r in rows:
            f.write("|".join(r) + "\n")
    with (ROOT / "05_anki.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        for r in rows:
            d = dict(zip(FIELDS, r))
            back = f"<b>{d['prevod_sr']}</b><br>{d['definicija_sl']}<br><i>{d['primer_sl']}</i>"
            if d["lazni_prijatelj"] and not d["lazni_prijatelj"].lower().startswith("ne"):
                back += f"<br>⚠ {d['lazni_prijatelj']}"
            if d["zakon_clen"]:
                back += f"<br><small>{d['zakon_clen']}</small>"
            w.writerow([d["termin_sl"], back, d["tema"]])
    tot = sum(v[0] for v in stats.values())
    okk = sum(v[1] for v in stats.values())
    for k, v in stats.items():
        print(f"{k}: {v[0]} pitanja, potvrđeno {v[1]}, provera završena: {v[2]}")
    print(f"UKUPNO {tot}, potvrđeno {okk}; rečnik {len(rows)} termina (odbačeno loših redova: {bad})")


if __name__ == "__main__":
    main()
