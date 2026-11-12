# BRIEF za NEZAVISNU proveru ključa odgovora

Ti si kontrolor kvaliteta. Dobijaš fajl sa pitanjima koji je napisao DRUGI agent. Pretpostavi da ima grešaka — tvoj posao je da ih nađeš, ne da potvrdiš.

Izvori istine (jedini): prečišćeni zakoni u `/home/zlfzr/gospodarsko-pravo/izvori/zakoni/*.md` (pročitaj `INDEX.md`: u OZ.md i SPZ.md naslov člana je IZNAD reda `### N. člen`; prelazne odredbe novela na kraju fajlova ponavljaju brojeve članova — ne mešaj; za sudove važi stari ZS.md) i `EU_PEU_PDEU_izvodi.md` ako postoji. Stari studentski materijali NISU izvor istine. Ne koristi Playwright ni tvly.

Za SVAKO pitanje i SVAKI ponuđeni odgovor:
1. Otvori član(ove) iz `vir.zakon_clen` u fajlu zakona (grep/awk) i pročitaj tekst. Ne sudi po sećanju.
2. Proveri: (a) da li član postoji i govori o tome; (b) da li je `pravilno` za taj odgovor tačno prema tekstu; (c) da li je odgovor JEDNOZNAČAN (nije "zavisi", nije delimično tačan, nije tačan po jednom a netačan po drugom stavu); (d) kod negativno formulisanih pitanja da li je ključ okrenut kako treba; (e) da li `razlaga_sr` tačno prenosi član i navodi pravi broj; (f) da li je slovenački gramatički ispravan i prirodan; (g) da li je `prevod_sr` veran.
3. Ishod po pitanju:
   - Sve potvrđeno → `"preverjeno": true`.
   - Sitna greška koju možeš NEDVOSMISLENO ispraviti iz teksta zakona (pogrešan broj člana, slovna/gramatička greška, netačan prevod, razlaga sa pogrešnom brojkom, pogrešno okrenut ključ koji je po zakonu jasan) → ispravi, `"preverjeno": true`, i zabeleži ispravku u izveštaju.
   - Ključ ne možeš potvrditi tekstom zakona, odgovor je dvosmislen, oslanja se samo na udžbeničku teoriju bez člana, ili pitanje ima 0 ili 5 tačnih posle ispravke → `"preverjeno": false` i dodaj polje `"opomba_preverjanja": "<razlog na srpskom>"`. NE briši pitanje.
4. Ne menjaj `id`, `tema`, `poreklo`. Ne dodaj nova pitanja.

Izlaz: prepiši ISTI fajl sa ažuriranim poljima (validan JSON, ista šema + opciono `opomba_preverjanja`), i napiši izveštaj `/home/zlfzr/gospodarsko-pravo/izvori/delovi/<KOD>_provera.md`: broj potvrđenih / ispravljenih / odbijenih, tabela ispravki (id, šta, zašto, član), tabela odbijenih (id, razlog), i opšta zapažanja o kvalitetu jezika.
Na kraju pokreni proveru strukture (validan JSON; multi = 5 odgovora sa 1–4 tačna; single = 3 odgovora sa 1 tačnim; jedinstveni id). Vrati kratak rezime sa brojevima i najvažnijim nalazima — pošteno, uključujući ono što nisi stigao da proveriš.
