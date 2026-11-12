# T5 — izveštaj nezavisne provere ključa

Fajl: `T5_pitanja.json` (62 pitanja, sva `multi`, 5 odgovora; 53 `generisano_po_gradivu`, 9 `po_zapiskih`).
Izvori: `zakoni/OZ.md` (NPB 4) i `zakoni/SPZ.md` (NPB 2), samo osnovni tekst (bez dodatka novela, osim prelazne odredbe SPZ-A čl. 5 kod T5-051).
Metod: za svako pitanje ispisani su svi članovi iz `vir.zakon_clen` i svih 310 odgovora upoređeno je sa tekstom člana (ključ, broj člana/stava u razlagi, prevod, jezik).

## Brojevi

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmene | 57 |
| Potvrđeno uz ispravku/dopunu | 5 |
| Odbijeno (`preverjeno: false`) | 0 |
| **Ukupno `preverjeno: true`** | **62** |

Nijedan ključ (`pravilno`) nije promenjen. Raspodela broja tačnih odgovora: 1 tačan – 15, 2 – 23, 3 – 19, 4 – 5.

## Ispravke i dopune

| id | Šta | Zašto | Član |
|---|---|---|---|
| T5-051 | Pitanje precizirano: „po veljavnem besedilu SPZ (2. člen)“ (+ prevod); razlaga za „Zemljiški dolg“ dopunjena napomenom; `vir` dopunjen | Ključ je jednoznačan po važećem tekstu (čl. 2 ne navodi zemljišni dug; čl. 192–200 su „črtan“). Dodata napomena da ga stariji materijali navode kao stvarno pravo i da za ranije zasnovane zemljišne dugove i dalje važe stare odredbe | SPZ 2; 192–200 (črtani); SPZ-A (91/13) čl. 5 |
| T5-017 | Razlaga odgovora o 8 % dopunjena napomenom („po tekstu OZ“; odredba upućuje na poseban zakon) | Formulacija odgovora je već bila „po OZ … če poseben zakon ne določa drugače“ – doslovno čl. 378/2; ključ ostaje | OZ 378/2 |
| T5-020 | Razlaga, odg. 5: „odustaninu“ → „odustanicu“ | Slovna greška u srpskom | OZ 67 |
| T5-043 | Pitanje: „sta … dogovorili, da“ → „sta se … dogovorili, da“ | Slovenačka gramatika (povratni glagol uz zavisnu rečenicu) | OZ 417/4 |
| T5-059 | U pitanje dodato „po SPZ“ (+ prevod) | Pitanje nije navodilo zakon; rok 10 godina je po SPZ | SPZ 43/2 |

## Odbijena pitanja

Nema.

## Posebno tražene provere

1. **Rokovi i brojke (doslovno po OZ/SPZ)** – sve potvrđeno: opšti rok 5 g. (346); povremena 3 g. (347/1); privredni ugovori 3 g. (349/1); isprava za z.k. 10 g. (350); zakupnina 3 g. (351); odšteta 3/5 g. (352/1–2); jednogodišnji rok (355/1 tč. 1 i 2); sudski utvrđena 10 g. (356/1); regres prema radniku 6 meseci (147/4); zatezna kamata 8 % (378/2); ugovorna kamata 6 % (382/2); ne ultra alterum tantum (382.a); državinska zaštita 30 dana / 1 godina (SPZ 32); održaj 3/10 g. (SPZ 43); nalaz 1 g. (SPZ 52); lična službenost pravnog lica 30 g. (SPZ 227/2).
2. **Hipotetički slučajevi težine 3** (T5-003, 008, 010, 015, 019, 023, 027, 033, 039, 041, 043, 045, 057) – rešenje u svakom jednoznačno sledi iz člana. Računski slučaj zastarelosti je **T5-039** (ne T5-033): šteta mart 2020, saznanje jun 2021 → 3 g. od saznanja = jun 2024, pre objektivnog roka (mart 2025); krivično delo je u pitanju izričito isključeno (čl. 353 se ne primenjuje). T5-027 (uračunavanje 1.000 EUR: 200 troškovi + 800 kamata, glavnica ostaje 10.000) tačno po čl. 288.
3. **Zemljišni dug** je **T5-051** (ne T5-039) – v. tabelu ispravki.
4. **T5-017** – formulacija je „po OZ“; ostavljeno, uz napomenu u razlagi.
5. **9 pitanja `po_zapiskih`** (T5-002, 004, 014, 017, 019, 022, 031, 037, 042) – ključ svih potvrđen tekstom OZ, nezavisno od zapisaka.
6. Negativno formulisana pitanja (T5-007, 011, 013, 016, 018, 030, 032, 037, 044, 049, 051, 060) – ključ je svuda pravilno okrenut, a razlage dosledno koriste „Označava se / Ne označava se“.

## Opšta zapažanja o jeziku i kvalitetu

- Slovenački je gramatički ispravan i prirodan; većina tačnih odgovora je doslovno ili gotovo doslovno preuzeta iz zakona (uključujući dual i zakonsku terminologiju: odstopnik/prevzemnik, porok in plačnik, pobot, prenovitev). Jedina gramatička ispravka: T5-043.
- Prevodi na srpski su verni i terminološki dosledni (cesija – ustupanje, pobot – prebijanje, prenovitev – prenov, poroštvo – jemstvo, posest – državina). Jedna slovna greška (T5-020).
- Razlage navode tačne brojeve članova i stavova; nije nađena nijedna pogrešna referenca.
- Skraćeni citati (npr. T5-003 odg. 1, T5-024 odg. 3, T5-044 odg. 4 izostavljaju deo nabrajanja iz člana) ne menjaju tačnost tvrdnje.

## Ograničenja provere

- Provera je rađena isključivo prema lokalnim NPB tekstovima; nije proveravano da li su ti tekstovi u međuvremenu menjani na pisrs.si.
- T5-017: stvarno primenjiva stopa zatezne kamate iz posebnog zakona nije u izvorima i nije proveravana – pitanje se drži teksta OZ.
- T5-039: eventualni uticaj interventnih propisa iz 2020. na tok rokova nije u izvorima; na rešenje ne utiče (saznanje je jun 2021, a objektivni rok je u svakom slučaju kasniji).
- `T5_recnik.csv` nije bio predmet provere.

## Provera strukture

Validan JSON; 62 jedinstvena id; sva pitanja `multi` sa 5 različitih odgovora i 1–4 tačna; `id`, `tema`, `poreklo` nepromenjeni; nijedno pitanje nije dodato ni obrisano.
