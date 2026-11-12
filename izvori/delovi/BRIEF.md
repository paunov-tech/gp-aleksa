# BRIEF za izradu sadržaja po temi (Gospodarsko pravo, EPF UM)

## Kontekst
Student Aleksa (maternji srpski, slovenački još uči) sprema 1. kolokvijum iz predmeta Gospodarsko pravo (U324, EPF Univerza v Mariboru; nosioci Primec i Jovanovič; udžbenik Bratina/Jovanovič/Podgorelec/Primec, Osnove gospodarskega pogodbenega in statusnega prava, 4. izd. 2024 — udžbenik NEMAMO). Kolokvijum je navodno Moodle kviz: pitanja sa 5 ponuđenih odgovora, moguće više tačnih, ~15 min. Sve što praviš služi učenju.

## Izvori koje SMEŠ da koristiš kao osnov za ključ odgovora
1. Prečišćeni tekstovi zakona sa pisrs.si u `/home/zlfzr/gospodarsko-pravo/izvori/zakoni/*.md` (pročitaj `INDEX.md` — upozorenja!). U OZ.md i SPZ.md naslov člana stoji IZNAD reda `### N. člen`; u ostalima u zagradi ispod. Na kraju nekih fajlova su prelazne odredbe novela sa ponovljenim brojevima članova — ne mešaj ih sa osnovnim tekstom. Sudovi: danas se primenjuje STARI ZS (ZS.md), ne ZS-1.
2. Za pravo EU: konsolidovani ugovori na eur-lex.europa.eu (PEU/PDEU) — preuzmi tekst (WebFetch/curl) i citiraj član + URL. Ne po sećanju.
3. Stari studentski materijali u `/home/zlfzr/gospodarsko-pravo/izvori/pdf/tutorji_epf/*.txt` i `/home/zlfzr/gospodarsko-pravo/izvori/web/stara_pitanja.json` — SAMO za stil pitanja, izbor tema i terminologiju udžbenika. Oni su iz 2014–2015, delom zastareli i sa greškama; NIKAD nisu osnov za ključ.
Opštepoznata teorija prava (npr. delovi pravne norme) sme u pitanja samo ako je možeš vezati za konkretan član zakona ili za stari studentski materijal kao `literatura_str` (npr. "zapiski Tutorji EPF: povzetki_1_del, str. 3") — i tada pitanje nosi poreklo "po_zapiskih".

## ČVRSTA PRAVILA
- NE IZMIŠLJAJ. Svaki tačan I svaki netačan ponuđeni odgovor mora biti proverljiv u tekstu člana koji navodiš. Pre pisanja pitanja PROČITAJ član u fajlu (grep/awk), ne citiraj po sećanju. Brojke, rokovi, iznosi, većine — doslovno iz zakona.
- Pitanja piši prirodnim pravnim slovenačkim, u stilu zakona i udžbenika. NE prevodi sa srpskog. Pazi na slovenačku gramatiku (dvojina, rodilnik uz negaciju).
- Ne koristi Playwright MCP browser i ne koristi `tvly`/Tavily. Ne preuzimaj piratske kopije udžbenika.
- Piši samo u svoje izlazne fajlove (navedene u zadatku). Ne diraj tuđe.

## IZLAZ 1 — pitanja: `/home/zlfzr/gospodarsko-pravo/izvori/delovi/<KOD>_pitanja.json`
JSON lista objekata, tačno ova šema:
```json
{
  "id": "<KOD>-001",
  "tema": "<tačan naziv teme iz zadatka>",
  "podtema": "kratko, na slovenačkom",
  "tezina": 1,
  "tip": "multi",
  "vprasanje_sl": "",
  "prevod_sr": "",
  "odgovori": [
    { "besedilo_sl": "", "prevod_sr": "", "pravilno": true, "razlaga_sr": "" }
  ],
  "kljucne_besede_sl": [],
  "vir": { "literatura_str": "", "zakon_clen": "ZGD-1, 475. člen, 1. odst.", "url": "https://pisrs.si/pregledPredpisa?id=ZAKO4291" },
  "poreklo": "generisano_po_gradivu",
  "preverjeno": false
}
```
- Tačno 5 ponuđenih odgovora, 1 do 4 tačna ("tip":"multi"). Raspodela broja tačnih: otprilike 25 % sa 1, 35 % sa 2, 30 % sa 3, 10 % sa 4. Redosled tačnih nasumičan.
- `tezina`: 1 = definicija/pojam, 2 = razlikovanje sličnih instituta/brojke, 3 = primena na kratak primer. Otprilike 40/40/20 %.
- Oko 20 % pitanja formuliši negativno ("Kaj od navedenega NE velja…", "Katera trditev ni pravilna…", "… razen") — tada su "pravilno": true oni odgovori koje treba označiti.
- Distraktori moraju biti uverljivi: zamena sličnih instituta, pogrešna brojka/rok, apsolutni kvantifikator (vedno, samo, izključno), obrnuta uloga strana. Ne pravi očigledne gluposti i ne pravi dvosmislene odgovore — svaki odgovor mora biti jednoznačno tačan ili netačan prema citiranom članu.
- `razlaga_sr`: za SVAKI odgovor 1–2 rečenice na srpskom (latinica) ZAŠTO je tačan/netačan, sa članom zakona (npr. "Netačno: osnovni kapital d.o.o. je najmanje 7.500 EUR, ne 25.000 (ZGD-1, 475. člen); 25.000 važi za d.d. (171. člen).").
- `prevod_sr`: veran prevod pitanja i svakog odgovora na srpski (latinica).
- `vir.zakon_clen`: svi članovi na kojima počiva ključ (kratica, član, po potrebi stav). `vir.url`: pisrs URL zakona iz zaglavlja .md fajla.
- `poreklo`: "generisano_po_gradivu" (tvoje pitanje po zakonu) ili "po_zapiskih" (ako prerađuješ pitanje iz starih studentskih materijala — tada u `vir.literatura_str` upiši fajl). Nikad "stvarno_staro" osim ako zadatak to izričito traži.
- `preverjeno` ostavi false — proveru radi drugi agent.
- Bez duplikata i bez dva pitanja koja ispituju potpuno istu činjenicu na isti način.

## IZLAZ 2 — rečnik: `/home/zlfzr/gospodarsko-pravo/izvori/delovi/<KOD>_recnik.csv`
UTF-8, separator `|` (uspravna crta), BEZ navodnika, bez znaka `|` unutar polja, prvi red zaglavlje:
`termin_sl|prevod_sr|definicija_sl|primer_sl|lazni_prijatelj|zakon_clen|tema`
- Broj termina naveden u zadatku. Termini koji se STVARNO pojavljuju u tvojim pitanjima i u članovima zakona za tvoju temu (imenice, glagoli, tipične sintagme).
- `definicija_sl`: kratka, proste rečenice (nivo A2–B1), po smislu verna zakonu. `primer_sl`: jedna prosta rečenica sa terminom. `lazni_prijatelj`: "ne" ili "da – <kratka napomena na srpskom šta liči a šta stvarno znači>". `zakon_clen`: gde je termin definisan/korišćen (može prazno za opšte reči). `tema`: naziv tvoje teme.

## IZLAZ 3 — sažetak teme: `/home/zlfzr/gospodarsko-pravo/03_teme/<KOD>_<slug>.md`
Za svaku podtemu (6–12 podtema) blok:
```
## <Podtema>
**SL:** kratak pasus (3–6 prostih rečenica) na jednostavnom slovenačkom, sa **podebljanim** ključnim terminima i članom zakona u zagradi.
**SR:** veran prevod na srpski (latinica).
**Objašnjenje:** 2–5 rečenica na srpskom: šta je bitno, sa čim se meša, tipična zamka na testu.
```
Na vrhu fajla: naslov teme, lista korišćenih zakona sa URL-ovima i datum pristupa 2026-11-13, i napomena "Sažetak je napisan po zakonu, ne po udžbeniku (udžbenik nije bio dostupan)."

## Samoprovera pre predaje
- `python3 -I -c "import json;d=json.load(open('<fajl>'));..."` — validan JSON, traženi broj pitanja, svako ima 5 odgovora i 1–4 tačna, jedinstveni id, sva polja popunjena.
- CSV: svaki red ima tačno 7 polja.
- Nasumično uzmi 10 svojih pitanja i ponovo uporedi svaki odgovor sa tekstom člana.
Vrati kratak rezime (srpski): broj pitanja/termina/podtema, raspodela broja tačnih, koje članove pokrivaš, i POŠTENO šta je nesigurno ili nije potkrepljeno.
