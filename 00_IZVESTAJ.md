# 00 — Izveštaj: Gospodarsko pravo (UM EPF), priprema za 1. kolokvijum

Datum: 13. 11. 2026. Pouzdanost: **A** zvanični izvor · **B** studentski materijal · **C** pretpostavka.

## 1. Zaključak u tri rečenice
Zvanične činjenice o predmetu su potvrđene, ali **o današnjem formatu kolokvijuma javno ne postoji ništa** — „računar, ~15 min, 5 ponuđenih, više tačnih" ostaje informacija iz druge ruke. Napravljen je komplet za trening (346 proverenih pitanja, rečnik 333 termina, sažeci, simulator, plan), ali je pisan **po tekstu zakona, ne po udžbeniku i prosojnicama**, jer njih nemamo. Tri stvari koje sve odlučuju — datum, gradivo i bodovanje — može da reši jedan mejl asistentu i Aleksina prijava u e-učionicu.

## 2. Šta je nađeno

| Tema | Nalaz | Pouzd. |
|---|---|---|
| Predmet | U324 Gospodarsko pravo, 5 ECTS, zimski sem., UN program „Ekonomske in poslovne vede"; nosioci Primec i Jovanovič | A |
| VS varijanta | VS „Poslovna ekonomija" nema ovaj predmet nego **Podjetniško pravo (V364)**, 6 ECTS, samo Primec, isti udžbenik, + radno pravo i održivo korporativno upravljanje | A |
| Ocenjivanje | ispit 100 % ili 2 kolokvijuma × 50 %; **jedan** negativan se popravlja seminarskim radom | A |
| Izvođenje | predavanja pon. 14:30–16:00 (PB), do 18. 1. 2027.; sve vaje drži asist. **Nikola Jovanović** | A |
| Rokovi | zimsko ispitno obdobje 25. 1. – 19. 2. 2027.; datumi kolokvijuma i rokovi predmeta nisu javni | A |
| Udžbenik | 4. izd. 2024, XXII + 601 str., ISBN 978-961-96875-0-5; biblioteka EPF ima 23 primerka; kazalo nije javno | A |
| E-učionica | Arnes Učilnice (ucilnice.arnes.si), ne estudij.um.si | A |
| Rečnik na testu | nijedan akt UM ga ne predviđa; pomagala određuje izvođač (Pravilnik, 24. člen) | A |
| AI | UM ne zabranjuje, traži označavanje; na EPF nastavnik bira režim po predmetu — režim ovog predmeta nepoznat | A |
| Stari testovi | samo ugašena „Baza zapiskov" Tutorja EPF (2014–2015): 2 papirna testa (izbor 1 od 3, bez ključa) + studentske rekonstrukcije | B |
| Zakoni | 15 važećih prečišćenih tekstova sa pisrs.si + izvodi PEU/PDEU sa EUR-Lex-a | A |

**Nije nađeno:** današnji Moodle kviz ili ijedno njegovo pitanje; broj pitanja, bodovanje, negativni bodovi, SEB, uređaj; datum i gradivo 1. kolokvijuma; kazalo udžbenika; ko sastavlja kolokvijume. Studocu i Quizlet nisu mogli biti provereni alatom (bot-zaštita).

## 3. Šta je napravljeno

| Fajl | Sadržaj | Stanje |
|---|---|---|
| `01_predmet.md` | činjenice + izvori + pouzdanost | gotovo |
| `02_nalazi_testovi.md` | 24 nalaza, „nije nađeno", dokazi o formatu, 134 doslovna stara pitanja | gotovo |
| `03_teme/` (5 fajlova) | sažeci SL → SR → objašnjenje, 60 podtema | gotovo, po zakonu |
| `04_model_testa.md` | format sa oznakama A/B/C, vremenski budžet, tehnika, zamke | gotovo; format je C |
| `05_recnik.csv`, `05_anki.tsv` | **333 termina** (105 označenih lažnih prijatelja) | gotovo; nije nezavisno proveren |
| `05_lazni_prijatelji.md`, `05_jezik_pitanja.md` | lažni prijatelji + skraćenice; 60 formulacija pitanja | gotovo |
| `06_banka_pitanja.json` | **350 pitanja, 346 proverenih** | gotovo |
| `07_simulator/index.html` | jedan fajl, offline; Učenje / Kolokvij / Šibke točke / Besedišče / Statistika | radi, testiran |
| `08_plan.md` | plan 7 i 14 dana od 13. 11., 2. kolokvijum, rezervni scenariji, ček-lista, mejl | gotovo |
| `09_otvorena_pitanja.md` | šta ko treba da odgovori | gotovo |

**Banka pitanja (346 u simulatoru):**

| Tema | Proverenih |
|---|---|
| 1 Temeljni pravni pojmi in pravni sistem (+ sodstvo, arbitraža, EU) | 53 |
| 2 Statusno pravo – splošni del | 59 |
| 3 Statusno pravo – oblike družb in preoblikovanja | 79 |
| 4 Pogodbeno pravo – sklenitev in veljavnost pogodb | 65 |
| 5 Obveznosti, zavarovanje, prenehanje, stvarno pravo | 76 |
| 6 Posamezne pogodbe (2. kolokvijum; samo stara pitanja) | 14 |

- Poreklo: 269 generisano po zakonu · 50 po studentskim zapisima · 27 stvarnih starih (izbor 1 od 3; **ključ smo odredili mi po važećem zakonu, original ga nema**).
- 319 pitanja ima 5 ponuđenih i 1–4 tačna (80 / 114 / 95 / 30); oko 20 % je negativno formulisano.
- Kontrola: svako pitanje je prošlo poseban, nezavisan subagent koji je svaki odgovor uporedio sa tekstom člana. Ishod: **nijedan pogrešan ključ**, 32 pitanja ispravljena (dvosmisleni distraktori, gramatika, prevod, broj člana), 4 odbijena i izbačena iz simulatora. Glavni agent je dodatno ručno proverio uzorak od 8 pitanja — sva tačna.
- Simulator je testiran Playwrightom: ceo kolokvijum do rezultata, sva tri bodovanja u logici, režim bez povratka, automatska predaja kad istekne vreme, pitanja sa jednim odgovorom, kartice, statistika. Nije testirano otvaranje dvoklikom sa diska (alat blokira `file://`, test je išao preko lokalnog servera) ni prikaz na telefonu.

## 4. Koliko su pouzdani zaključci o formatu testa
**Nisko.** Zvanično (A) znamo samo da kolokvijum postoji i nosi 50 %. Računar, 15 minuta, 5 ponuđenih i više tačnih odgovora su iz druge ruke (C). Bodovanje, negativni bodovi, broj pitanja, povratak na pitanja, uređaj i SEB su potpuno nepoznati. Stari testovi (B) su bili na papiru, izbor 1 od 3, sa mnogo negativno postavljenih pitanja i fokusom na razlikovanje oblika društava. Simulator zato ima podesiv broj pitanja, vreme, bodovanje i povratak; trenira se na najstrožem (20 pitanja, sve-ili-ništa).

## 5. Tri najveća rizika za Aleksu

1. **Uči se pogrešno gradivo.** Ne znamo šta ulazi u 1. kolokvijum; indicije se ne slažu (načrt: temeljni pojmovi + statusno; jedna stara generacija: samo pogodbeno). Plan pretpostavlja prvo. Greška ovde košta celu nedelju.
2. **Brzina čitanja pravnog slovenačkog.** Ako je 15–20 pitanja u 15 minuta, to je 40–50 s po pitanju sa pet odgovora — za nekog ko jezik još uči to je usko grlo veće od znanja prava. Negacije (*ni, razen, ne velja*) i lažni prijatelji (*firma, družba, lahko, posest*) su tipične tačke gubitka.
3. **Trening nije isto što i test.** Pitanja su po zakonu; stvarni kviz ide po udžbeniku i prosojnicama, sa teorijom koje u zakonu nema (pojam prava, pravna norma, pretpostavke odgovornosti) i možda sa starijim brojkama. Uz to, slovenački u pitanjima nije lektorisao izvorni govornik. Visok rezultat u simulatoru nije garancija.

## 6. Šta uraditi prvo (redom)

1. **Danas:** Aleksa odgovara na STOP-1 (`09_otvorena_pitanja.md`, deo A) — pre svega: tačan naziv predmeta, datum, teme dosadašnjih predavanja.
2. **Danas:** poslati mejl asistentu (`08_plan.md`, deo E) — format, bodovanje, uređaj, rečnik.
3. **Sutra:** pozajmiti udžbenik u biblioteci EPF; fotografisati kazalo i ubaciti sa prosojnicama u `ulaz/`.
4. **Odmah početi** dnevni blok iz `08_plan.md` (dan 1: `05_jezik_pitanja.md` + lažni prijatelji + tema 1) — ne čekati odgovore.
5. **Kad se Aleksa prijavi u e-učionicu:** Faza 3 (samo čitanje: obaveštenja, prosojnice, opis kviza) → doterati banku po stvarnom gradivu i suziti simulator na prave teme.

## 7. Odstupanja od zadatka
- **Faza 3 (e-učionica) nije rađena** — čeka Aleksinu ručnu prijavu.
- **Tavily:** potrošena 3 poziva (`basic`), po strožem pravilu iz globalnog CLAUDE.md; TASK je dozvoljavao 80. Ostalo je išlo kroz ugrađeni search.
- **Udžbenik nije korišćen** (nema ga u `ulaz/`, a piratske kopije nisu dolazile u obzir) → kazalo nije mapirano na teme.
- VS predmet (V364) je samo identifikovan, nije obrađen.
- Potrošnja i hronologija: `LOG.md`.
