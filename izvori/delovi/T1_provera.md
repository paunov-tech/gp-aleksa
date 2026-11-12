# T1 — izveštaj nezavisne provere ključa

Fajl: `izvori/delovi/T1_pitanja.json` (55 pitanja, sva `multi`, 5 odgovora). Datum: 2026-11-13.
Izvori: `izvori/zakoni/URS.md, ZS.md (stari), ZPP.md, OZ.md, ZGD-1.md, ZZ.md, ZZad.md, ZArbit.md, ZMCGZ.md, EU_PEU_PDEU_izvodi.md`. Svaki citirani član je otvoren i pročitan; studentski zapisi nisu korišćeni.

## Brojevi

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmena (`preverjeno: true`) | 50 |
| Ispravljeno pa potvrđeno (`preverjeno: true`) | 3 |
| Odbijeno (`preverjeno: false` + `opomba_preverjanja`) | 2 |
| Ukupno | 55 |

Nijedan ključ (`pravilno`) nije promenjen — nisam našao pogrešno okrenut ključ ni pogrešan broj člana/stava/alineje.

## Ispravke

| id | Šta | Zašto | Član |
|---|---|---|---|
| T1-005 | Opcija „Učinek … za nazaj je dopusten le, če to zahteva javna korist.” dopunjena sa „… in če se s tem ne posega v pridobljene pravice”; usklađeni `prevod_sr` i `razlaga_sr`. Ključ ostaje `false` (tvrdnja je tačna, pitanje je negativno). | Navodila je samo jedan od dva kumulativna uslova; logički tačno („le, če” = nužan uslov), ali student je može čitati kao nepotpunu, dakle netačnu. Sada je doslovno po tekstu. | URS, 155. člen, 2. odst. |
| T1-020 | Opcija „Zakon samo razveljavi z učinkom med strankama.” → „Zakon razveljavi kar samo, z učinkom med strankama.” | „samo” se u originalu čita kao „jedino”, a mišljeno je „sud sam” (kako stoji i u prevodu). Samo jezička ispravka, ključ `false` ostaje. | URS, 156., 160., 161. člen |
| T1-028 | Pitanje: „po 98. členu” → „po 97. in 98. členu” (+ prevod). | Izraz „sodišča s splošno pristojnostjo” definiše 97. člen (upućujući na 1. odst. 98. člena); sam 98. člen taj izraz ne sadrži. | ZS, 97. člen, 1. odst.; 98. člen, 1. odst. |

## Odbijena

| id | Razlog |
|---|---|
| T1-021 | Sastav pravne norme (hipoteza/dispozicija/sankcija) je opšta teorija prava; nema člana ni u jednom zakonu u `izvori/zakoni`. Jedini oslonac su studentski zapisi. Ključ je u skladu sa uobičajenom udžbeničkom podelom, ali nepotvrđen. |
| T1-023 | Pravna sposobnost rođenjem / potpuna poslovna sa 18 godina — uređuje Družinski zakonik, kojeg nema među izvorima; OZ 41. člen poslovnu sposobnost samo pretpostavlja. Dodatno: po DZ se potpuna poslovna sposobnost može steći i pre 18. godine, pa je odgovor tačan samo kao opšte pravilo. |

## Posebno provereno (sudovi i brojke)

- Sudovi po starom ZS: 97., 98., 100., 101. (III. tačka – sudski registar), 102., 104., 105., 106. (1. odst., 4. tačka), 107., 109., 110. člen — sve se poklapa. Nijedno pitanje se ne oslanja na ZS-1.
- ZPP brojke doslovno: 20.000 EUR (30. člen, 1. odst. „ne presega”; 32. člen, 1. odst. „presega”); 2.000 EUR (443. člen, 1. odst.); 4.000 EUR (495. člen, 1. odst.); „V sporih majhne vrednosti ni revizije” (458. člen). Tačke 30/2 (1–3) i 32/2 (3, 6, 7, 8) tačno navedene; 481. i 482. člen tačno preneti.
- URS: 15. dan (154), 8 dana / 7 dana / većina svih poslanika (91), 40.000 i petina (90), 5.000 (88), 90 poslanika (80), 40 članova i 5 godina (96, 98), dvotrećinska većina svih (3.a), rok do jedne godine (161) — sve tačno; redni brojevi alineja u 90., 97., 107. i 160. členu provereni brojanjem.
- T1-014 (računski slučaj): 44 < 46 od 90 — ključ tačan.
- ZArbit: 3 arbitra (13/2), tri meseca (40/3), većina glasova (33), ex aequo et bono samo uz izričito ovlašćenje (32/3). ZMCGZ: 13. člen tačke b) i e), 17. člen 1.–2. odst.
- EU: PDEU 288 (redosled stavova 1–5), 267, 297; PEU 4, 5, 13, 14, 15, 16, 17 (mandat 5 godina), 19/3(b).

## Zapažanja o kvalitetu

- Slovenački je gramatički ispravan i prirodan; tačni odgovori su uglavnom gotovo doslovni citati zakona, distraktori su verodostojni (zamena organa, roka ili većine). Dvojina korektna (T1-033, T1-041, T1-046). Jedina stvarna jezička dvosmislenost bila je T1-020.
- Prevodi na srpski su verni; terminologija dosledna („sklep” = odluka kod EU akata, „izpodbojna” = rušljiv, „razveljavitev” = ukidanje/poništaj uz original u zagradi).
- Negativno formulisana pitanja (T1-005, 010, 017, 019, 027, 030, 040, 042, 044, 050, 054) imaju ispravno okrenut ključ i dosledne razlage („označava se / ne označava se”).
- Sitne nepreciznosti koje nisam menjao jer ne utiču na ključ: neki tačni odgovori skraćuju zakonski tekst (T1-002 b izostavlja „splošno veljavna načela mednarodnega prava”; T1-019 e izostavlja „v celoti ali delno” i „ali zakonitost”); T1-035 b (vanredni pravni lekovi) je `false` za više sudove po 104. členu ZS, mada 106/1 t. 4 dopušta da o nekom vanrednom leku odlučuje i drugi sud; T1-044 e je netačna tvrdnja kao opšte pravilo (izuzeci u 12. členu, 3. odst.).

## Šta nije provereno

- `vir.url` linkovi nisu otvarani (bez mreže po briefu); `literatura_str` kod T1-021/023 nije proveravan jer zapisi nisu izvor istine.
- Polja `kljucne_besede_sl` i fajl `T1_recnik.csv` NIJE otvaran ni proveravani, ne stavku po stavku.
- Provera strukture: validan JSON, 55 jedinstvenih id, svi `multi` sa 5 odgovora i 1–4 tačna (raspodela: 1 tačan ×14, 2 ×19, 3 ×16, 4 ×6).
