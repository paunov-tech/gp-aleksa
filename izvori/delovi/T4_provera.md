# T4 — izveštaj nezavisne provere ključa

Fajl: `T4_pitanja.json` (55 pitanja, sva `multi`, 5 odgovora; OZ čl. 1–121).
Izvor: `izvori/zakoni/OZ.md`, osnovni tekst čl. 1–121 pročitan u celini (ne dodatak novela), plus 496. člen za jedan distraktor. Svih 275 odgovora upoređeno je sa tekstom člana.

## Brojevi

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmena | 45 |
| Potvrđeno uz ispravku | 10 |
| Odbijeno (`preverjeno: false`) | 0 |
| Ukupno | 55 |

Nijedan ključ (`pravilno`) nije promenjen. Provera strukture prošla: validan JSON, 55 jedinstvenih id, svako pitanje 5 odgovora sa 1–4 tačna.

## Ispravke

| id | Šta | Zašto | Član |
|---|---|---|---|
| T4-008 | Pitanje: »Katera trditev … NI pravilna?« → »Katere trditve … NISO pravilne?« (+ prevod) | Jednina, a označena su 2 odgovora | OZ, 20. člen |
| T4-020 | Isto: jednina → množina (+ prevod) | Označena 2 odgovora | OZ, 46., 47. člen |
| T4-034 | Isto: jednina → množina (+ prevod) | Označena 2 odgovora | OZ, 77. člen |
| T4-046 | Isto: jednina → množina (+ prevod) | Označena 2 odgovora | OZ, 95., 99. člen |
| T4-051 | Isto: »Katera trditev … NE drži?« → »Katere trditve … NE držijo?« (+ prevod) | Označena 2 odgovora | OZ, 113., 115. člen |
| T4-051 | Distraktor »…izgubi pravico zahtevati razvezo« zamenjen sa »…ne odgovarja za škodo, ki jo je druga stranka zaradi tega imela« (+ prevod, razlaga) | Stari je bio netačan samo zato što zakon o gubitku prava ćuti; novi je suprotan slovu druge rečenice člana. Ključ ostaje (označava se) | OZ, 113. člen |
| T4-013 | Distraktor »Vsaka, tudi najmanjša sprememba besedila ponudbe« zamenjen sa »Samo spremembe, ki se nanašajo na ceno; spremembe glede kraja in časa dobave se nikoli ne štejejo za bistvene« (+ prevod, razlaga); `zakon_clen` sužen na 29/3 | Stari se obarao odnosom 29/1 i 29/2 (po 29/1 svaki predlog izmene jeste odbijanje), dakle tumačenjem; novi je suprotan nabrajanju u 29/3 | OZ, 29. člen, 3. odst. |
| T4-036 | Distraktor »Take pogodbe sklepajo v svojem imenu in za svoj račun« zamenjen sa »Take pogodbe smejo samo skleniti, ne pa tudi izpolniti« (+ prevod, razlaga); iz `zakon_clen` izbačen 70/1 | 80. člen ne kaže u čije ime; stari se obarao sistematikom (odsek o zastupanju). Novi je suprotan rečima »skleniti in izpolniti« | OZ, 80. člen |
| T4-048 | Tačan odgovor »Dobavitelju mora pustiti primeren dodatni rok« → »…mora praviloma pustiti…« (+ prevod, razlaga) | U istom pitanju je tačan i izuzetak iz 106. člena, pa je kategorično »mora« bilo u napetosti s njim | OZ, 105/2; 106. člen |
| T4-047 | Razlaga distraktora »prodajalec vedno izpolniti prvi« dopunjena 496/2; `zakon_clen` dopunjen | Tvrdnja je o prodaji, a razlaga se pozivala samo na opšte pravilo; 496/2 je direktno obara | OZ, 496. člen, 2. odst. |
| T4-007 | `zakon_clen` dopunjen sa 28/1 i 51/1 | Razlage dva distraktora se pozivaju na te članove, a nisu bili u izvoru | OZ, 28/1; 51/1 |

(11 redova, 10 pitanja — T4-051 ima dve ispravke.)

## Odbijeno

Nema.

## Posebno traženi distraktori

| Tema | id | Ishod |
|---|---|---|
| »Načelo hierarhičnosti« | T4-005 (ne T4-007) | Prihvaćeno bez izmene: 4. člen (»Udeleženci … so enakopravni«) je direktno suprotan nadređenosti jedne strane; nije tumačenje. |
| čl. 113, »izgubi pravico zahtevati razvezo« | T4-051 | Preformulisano (vidi gore). |
| čl. 80, »v svojem imenu in za svoj račun« | T4-036 | Preformulisano (vidi gore). |
| čl. 29/3, »vsaka, tudi najmanjša sprememba« | T4-013 | Preformulisano (vidi gore). |
| čl. 62, primeri sa datumima | T4-028 | Prihvaćeno bez izmene: 15 dana od događaja 10. marta = 11.–25. mart (62/1); mesec dana od 31. januara = poslednji dan februara (62/2). Oba su čista primena slova člana; pitanje samo isključuje neradan dan (62/3). |

## Rokovi — provereni doslovno

| Rok | Član | Pitanja |
|---|---|---|
| Rušljivost: 1 godina od saznanja / prestanka prinude; 3 godine od zaključenja | 99/1, 99/2 | T4-021, 044, 046 |
| Prekomerno oštećenje: 1 godina od zaključenja | 118/2 | T4-052, 054 |
| Zelenaški ugovor: 5 godina za zahtev za smanjenje | 119/4 | T4-044 (razlaga) |
| Predugovor: 6 meseci | 33/5 | T4-015 |
| Sticanje poslovne sposobnosti: 3 meseca | 44 | T4-018 |
| Izjašnjenje zakonskog zastupnika: 30 dana, ćutanje = odbijanje | 43/2 | T4-018 |
| Rok za izjašnjenje kod rušljivosti: najmanje 30 dana | 95/2 | T4-044 (razlaga) |
| Ništavost: ne gasi se | 93 | T4-041, 044, 046 |

Svi se poklapaju sa tekstom.

## Zapažanja o jeziku

- Slovenački je gramatički ispravan i prirodan; većina tačnih odgovora je gotovo doslovan citat člana, pa su i termini zakonski (naslovnik, odstopnina/skesnina, razveljavitev, razveza).
- U T4-036 pitanje ima »z njim zvezano«, dok zakon ima »z njimi« (omaška u zakonu); verzija u pitanju je gramatički ispravna i ostavljena je.
- Srpski prevodi su verni i terminološki ujednačeni (rušljiv/ništav, kapara/odustanica, vlastodavac/punomoćnik, ponuđeni). Nisam našao pogrešan prevod.
- Jedina sistemska slabost bila je jednina u negativno formulisanim pitanjima sa dva tačna odgovora (5 pitanja).

## Šta nije provereno

- `kljucne_besede_sl` i `literatura_str` (pozivanja na studentske zapise) nisu proveravani — zapisi nisu izvor istine.
- Težina (`tezina`) nije ocenjivana.
- Pitanja sa 4 tačna od 5 (T4-011, 013, 031, 035, 055) su ispravna po zakonu, ali su laka za pogađanje; to nije menjano.
