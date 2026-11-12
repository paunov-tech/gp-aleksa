# LOG — Gospodarsko pravo (UM EPF)

## 2026-11-13 00:03 — Faza 0
- Struktura foldera napravljena. `ulaz/` je PRAZAN (Aleksa još ništa nije ubacio).
- Internet: OK (moja.um.si odgovara).
- `tvly`: guard radi, kill-switch off, nema `~/.tavily/DISABLED`. Stanje: 0/40 search danas, 297/1500 mesečno.
- **Odluka o Tavily budžetu:** TASK dozvoljava 80 poziva, ali globalni CLAUDE.md propisuje najviše 3 `tvly search` po zadatku, uvek `--depth basic`. Primenjujem STROŽE pravilo (3 × basic); ostalo ide kroz ugrađeni web search/fetch.
- Playwright: dostupan kao MCP (`mcp__playwright__*`); lokalni npm/python paket nije instaliran. Za Fazu 3 (headed + `.pw-profile/`) proveriti da li MCP browser radi headed.

## Tavily potrošnja
| # | vreme | upit | dubina | keš fajl |
|---|-------|------|--------|----------|
| 1 | 00:06 | gospodarsko pravo EPF Maribor zapiski kolokvij vprašanja Primec Jovanovič Bratina (domeni studocu/quizlet/scribd/docsity/knowt/brainscape) | basic | izvori/tavily/01_platforme_epf_gospodarsko_pravo.json |
| 2 | 00:06 | gospodarsko pravo EPF UM 1. kolokvij vprašanja odgovori zapiski … | basic | izvori/tavily/02_opsta_epf_um_kolokvij_vprasanja.json |
| 3 | 00:10 | gospodarsko pravo EPF kolokvij statusno pravo d.o.o. d.n.o. prokurist firma kartice | basic | izvori/tavily/03_kartice_quizlet_studocu.json |

**Ukupno: 3 poziva (limit 3 po CLAUDE.md; TASK je dozvoljavao 80).**

## 2026-11-13 00:10 — Faza 1 (moja.um.si, Playwright MCP)
- U324 potvrđen (A): 5 ECTS, Primec + Jovanovič, pismeni ispit 100 % ili 2 kolokvijuma × 50 %, jedan negativan → seminarski rad. Dokaz: `izvori/web/moja_um_U324_*`.
- NOVO: VS program „Poslovna ekonomija" nema „Gospodarsko pravo" nego „Podjetniško pravo" V364 (6 ECTS, samo Primec, isti udžbenik, + radno pravo i održivo korp. upravljanje). Dokaz: `izvori/web/moja_um_V364_*`, `moja_um_VS_predmetnik_*`, `moja_um_UN_predmetnik_*`.
- Playwright MCP snima fajlove relativno na /home/zlfzr (ne na projekat) — prvi fajlovi su ručno premešteni.
- Pokrenuta 3 subagenta paralelno: (a) Faza 2 stari testovi, (b) zakoni sa pisrs.si, (c) Faza 1 EPF zvanični izvori (urnik, pravilnik, COBISS).

## 2026-11-13 — Zakoni (subagent, završeno)
- Svih 15 zakona preuzeto sa pisrs.si kao NPB preko javnog API-ja (`/api/rezultat/zbirka/id/<ID>` → `/api/rezultat/neuradno-precisceno-besedilo/<npbId>`). Detalji i metod: `izvori/zakoni/INDEX.md`.
- Ispravke ID-jeva: ZSReg = ZAKO320 (ne ZAKO1041); ZGZ = ZAKO4251; dodat novi ZS-1 (ZAKO8887).
- PAŽNJA za ključ odgovora: (1) sudovi — do 1. 1. 2027. primenjuje se stari ZS, ZS-1 tek od tada; (2) u OZ i SPZ naslov člana stoji IZNAD broja člana; (3) prelazne odredbe novela ponavljaju brojeve članova (odvojene naslovom na kraju fajla).
- Sadržaj članova nije ručno poređen sa PDF-om član po član (konverzija mehanička; broj članova se slaže sa sirovim HTML-om).
- Napisano bez čekanja: `07_simulator/template.html` + `build.py` (netestirano dok nema banke), `05_jezik_pitanja.md` (60 formulacija, pouzdanost C).

## 2026-11-13 — Faza 2 (subagent, završeno)
- Rezultat: `02_nalazi_testovi.md`, `izvori/web/stara_pitanja.json` (134 zapisa, ~95–100 jedinstvenih), originali u `izvori/pdf/tutorji_epf/`.
- Jedini vredan izvor: ugašena „Baza zapiskov študentov EPF" (Tutorji EPF, PDF-ovi 2014–2015, delom zastarelo pravo). 42 pitanja sa dva stara papirna testa BEZ ključa (izbor 1 od 3); 92 studentske rekonstrukcije sa nezvaničnim, mestimično pogrešnim odgovorima.
- NIJE nađeno: današnji Moodle kviz, ijedno pitanje sa više tačnih odgovora, broj pitanja, bodovanje, SEB. Format „~15 min, računar, više tačnih" ostaje iz druge ruke (C).
- Nije uspelo: Studocu (bot-zaštita), Quizlet (403), profesorji.net (503), scribd bez teksta.
- Tavily: 3/3 poziva potrošena (vidi tabelu), svi `--depth basic`.

## 2026-11-13 — Faza 1 EPF (subagent, završeno)
- `izvori/web/faza1_epf_nalazi.md`, 13 PDF-ova u `izvori/pdf/`. Ključno prepisano u `01_predmet.md` §6.
- Nađeno: urnik (wise-tt), asistent Nikola Jovanović drži sve vaje, koledar, kontakti, pravilnik UM, smernice AI, COBISS, e-učionica = Arnes Učilnice (ne estudij.um.si).
- NIJE nađeno: datumi kolokvijuma/rokovi (nisu javni), kazalo udžbenika, pravilo o rečniku za strane studente, AI režim predmeta, SEB. old.epf.um.si ima neispravan TLS sertifikat — nije zaobilaženo.
- Pokrenuto 6 subagenata za sadržaj (T1–T5 pitanja+rečnik+sažeci po zakonu; S0 = obrada stvarnih starih pitanja). Zajednički brief: `izvori/delovi/BRIEF.md`.
- STOP-1 pitanja poslata korisniku; rad se nastavlja sa pretpostavkama (C) dok ne stignu odgovori.
- Napisano: `04_model_testa.md`, `08_plan.md` (varijante 7 i 14 dana od 13. 11.; nacrt mejla asistentu), `05_lazni_prijatelji.md`.

## 2026-11-13 — Sadržaj i provere (u toku)
- Generisano po zakonu: T1 55, T2 55, T4 55, T5 62 pitanja (+ rečnik i sažeci); S0 = 58 stvarnih starih pitanja u formatu banke (22 odbačena, razlozi u `izvori/delovi/S0_odbacena.md`). T3 se još piše.
- Nezavisne provere ključa (poseban subagent po delu, izveštaji `izvori/delovi/*_provera.md`):
  - S0: 57/58 potvrđeno (S0-025 odbijen); glavni agent dodatno odbio S0-026 (ključ delom na udžbeničkoj teoriji) → 56.
  - T1: 53/55 (T1-021, T1-023 odbijeni — nema člana zakona); 3 jezičke/sadržinske ispravke, nijedan ključ pogrešan.
  - T2: 55/55; ispravljen T2-005 (preširok tačan odgovor o čl. 10.a).
  - T4, T5: provera u toku.
- `izvori/delovi/merge.py` spaja delove u `06_banka_pitanja.json`, `05_recnik.csv`, `05_anki.tsv`.
- **Simulator testiran Playwrightom** (preko lokalnog http servera jer MCP blokira `file://`): Učenje (prevod, provera, objašnjenja), ceo Kolokvij od 15 pitanja do rezultata i analize, blokada promene taba tokom kolokvijuma, Šibke točke, Besedišče, Statistika, istorija simulacija. Jedina greška u konzoli: favicon 404 (bezopasno). Screenshot: `LOG/simulator_kolokvij_rezultat.png`. Nije testirano: istek tajmera do nule, otvaranje dvoklikom sa diska (file://), mobilni prikaz.

## 2026-11-13 00:40 — Završetak (bez Faze 3)
- Provere ključa završene za sve delove: T3 65/65 (4 ispravke), T4 55/55 (10 ispravki, 3 distraktora preformulisana), T5 62/62 (5 ispravki). Nijedan ključ nije bio pogrešan ni u jednom delu.
- Konačno: `06_banka_pitanja.json` 350 pitanja, 346 `preverjeno: true` (odbijena: S0-025, S0-026, T1-021, T1-023). `05_recnik.csv` 333 termina (posle uklanjanja duplikata između tema), `05_anki.tsv` 333 reda.
- Glavni agent ručno proverio uzorak od 8 pitanja prema tekstu članova — sva tačna.
- Simulator ponovo izgrađen (346 pitanja) i ponovo testiran: 20 pitanja, negativni bodovi, bez povratka, automatska predaja po isteku vremena (10 tačnih od 20 → 50 %), pitanje tipa „single". Screenshot: `LOG/simulator_ucenje_final.png`. Lokalni test-server ugašen.
- Napisano: `00_IZVESTAJ.md`, `09_otvorena_pitanja.md`.
- NIJE urađeno: Faza 3 (čeka Aleksinu prijavu na ucilnice.arnes.si); mapiranje kazala udžbenika; lektura slovenačkog od izvornog govornika; nezavisna provera rečnika; VS predmet V364; tema 6 (2. kolokvijum) sistematski.
- Ponovno građenje posle izmena: `python3 izvori/delovi/merge.py && python3 07_simulator/build.py`.

## 2026-11-13 00:56 — Objavljeno na netu (odluka korisnika: javna stranica, sa svim izvorima)
- Repo: https://github.com/paunov-tech/gp-aleksa — **JAVAN** (GitHub plan ne dozvoljava Pages iz privatnog repoa; pokušano prvo privatno → 422).
- Stranica: https://paunov-tech.github.io/gp-aleksa/ (Jekyll, tema primer; `README.md` = početna). Simulator: `/07_simulator/index.html`.
- Dodato: `robots.txt` (Disallow: /), `noindex` u simulatoru, `_config.yml`. Commit autor koristi GitHub noreply adresu.
- Provereno u pregledaču: svi linkovi sa početne vraćaju 200; simulator na javnoj adresi učitava 346 pitanja i 333 termina.
- Korisnik javio: kolokvijum je za 7 dana (~20. 11.) → važi varijanta 7 dana iz `08_plan.md`.
- Ažuriranje sajta: `python3 izvori/delovi/merge.py && python3 07_simulator/build.py && git add -A && git commit && git push` (Pages se sam ponovo gradi za ~1 min).
- ZA KASNIJE (zaključavanje samo za Aleksu): repo vratiti na private (Pages se tada gasi na ovom planu) → ili GitHub Pro, ili dodati Aleksu kao saradnika.
