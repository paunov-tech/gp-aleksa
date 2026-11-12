# S0 — izveštaj nezavisne provere ključa

Fajl: `S0_pitanja.json` (58 pitanja: 29 single iz starih testova, 29 multi po studentskim zapisima).
Izvori: `izvori/zakoni/ZGD-1.md`, `OZ.md`, `SPZ.md` (osnovni tekst, ne dodaci novela). Svaki član iz `vir.zakon_clen` i iz razlaga otvoren je i pročitan.

## Brojevi

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmena | 49 |
| Potvrđeno uz ispravku | 8 |
| Odbijeno (`preverjeno: false`) | 1 |
| Ukupno | 58 |

Nijedan ključ (`pravilno`) nije promenjen. Provera strukture prošla: validan JSON, 58 jedinstvenih id, single = 3 odgovora / 1 tačan, multi = 5 odgovora / 1–4 tačna.

## Ispravke

| id | Šta | Zašto | Član |
|---|---|---|---|
| S0-002 | `prevod_sr` pitanja: »nadzornog odbora« → »nadzornog saveta« | Ujednačavanje sa ostatkom fajla (svuda drugde »nadzorni savet«) | ZGD-1, 281. člen |
| S0-005 | Razlaga tačnog odgovora i `zakon_clen` dopunjeni 842. členom | Obaveza posrednika je izričito u 842/1, ne samo u definiciji iz 837 | OZ, 842. člen, 1. odst. |
| S0-026 | Razlaga odgovora »prednostna pravica« preformulisana | Zakon ne deli prava na imovinska i upravljačka; razlaga je to tvrdila kao da stoji u 337. členu | ZGD-1, 337/1; 176/2 |
| S0-029 | Razlaga za »dvojna družba« dopunjena, `zakon_clen` dopunjen | Razlaga je pokrivala samo komplementara; smrt komanditora rešava 151. člen | ZGD-1, 151. i 152. člen |
| S0-039 | `besedilo_sl` i `prevod_sr` 3. odgovora: »šele ko plača« → »šele ko kupec plača« | Gramatički subjekat je bio prodavac (ispadalo da prodavac plaća cenu) | OZ, 520. člen, 1. odst. |
| S0-041 | Tekst pitanja: »Kdaj se krivda predpostavlja (domneva)?« → »Kdaj se krivda domneva in kdaj se odgovarja ne glede na krivdo?« (+ prevod) | Odgovor o objektivnoj odgovornosti označen je kao tačan, a na staro pitanje nije odgovor (tamo se krivica ne pretpostavlja, nego je nebitna) | OZ, 131. člen, 1. i 2. odst. |
| S0-050 | `besedilo_sl` i `prevod_sr` 5. odgovora: »druga stranka« → »stranka, ki je dala aro« | U pitanju je »druga stranka« primalac kapare, a u odgovoru se mislilo na davaoca | OZ, 64. člen, 3. odst.; 68. člen |
| S0-054 | Razlaga za »Zastaranje« i `zakon_clen`: 346. → 335. člen | Odeljak »Zastaranje« počinje 335. členom; 346. je samo opšti rok | OZ, 335. člen |

Ispravka u S0-041 je izmena teksta pitanja, veća od slovne greške. Urađena je jer su svi ključevi po zakonu tačni kao tvrdnje, a alternativa je bilo odbijanje.

## Odbijeno

| id | Razlog |
|---|---|
| S0-025 | Odgovori »osebna odgovornost« (naslov 100. člena ZGD-1, preko 135/2) i »neomejena odgovornost« (»z vsem svojim premoženjem«, 135/1) sami su za sebe tačni po slovu zakona, a u ključu su netačni. Treći odgovor je samo najpotpuniji. |

## Pitanja koja je autor označio kao diskutabilna

| id | Ishod | Obrazloženje |
|---|---|---|
| S0-005 | Potvrđeno | Druga dva odgovora su izričito netačna (837. i 839. člen OZ). Termin »komitent« u tačnom odgovoru je iz originalnog testa i nije zakonski (zakon: »naročitelj«); razlaga to navodi. |
| S0-011 | Potvrđeno | 825. člen OZ (»Pridobitev pravice do plačila«) vezuje sticanje za izvršenje posla, ne za zaključenje. |
| S0-013 | Potvrđeno | 471/1 ZGD-1 doslovno: »osnovni kapital sestavljajo osnovni vložki«; poslovni delež se po 471/2 stiče na osnovu uloga. |
| S0-014 | Potvrđeno | 176/2 i 231/1 ZGD-1. Odgovor o prioritetnim akcijama nije definicija dividende. |
| S0-019 | Potvrđeno | 230/3 ZGD-1 doslovno daje organima vođenja ili nadzora odluku o delu čiste dobiti. Skupština (bilansna dobit, 230/5 i 293/1) nije ponuđena. |
| S0-024 | Potvrđeno | 35. člen ZGD-1 nosi naslov »obseg prokure«; ograničenje nema dejstvo prema trećima. |
| S0-025 | Odbijeno | Vidi gore. |
| S0-026 | Potvrđeno, granično | Tačan odgovor (pravo glasa) ima oslonac u 176/2, 1. alineja. Da je pravo prečeg upisa imovinsko pravo zakon ne kaže — to je teorijska podela. |
| S0-033 | Potvrđeno | 131/1 daje štetu, uzročnost i krivicu; 137/3 pokazuje da poslovna sposobnost nije uslov. |
| S0-054 | Potvrđeno uz ispravku | Sledi iz strukture II. poglavja OZ (5 odeljaka); zastarelost i prebijanje su u IV. poglavju. |
| S0-056 | Potvrđeno | 349/1 OZ: tri godine. |

## Pitanja teme 6 (provereno prema OZ)

S0-003 do S0-011, S0-031, S0-039, S0-044, S0-051, S0-058: svi ključevi potvrđeni prema 435, 442, 459, 461, 488, 519, 520, 522–524, 788, 798, 799, 807, 809, 823, 825, 837, 839, 841, 847. Za S0-039 korišćen i SPZ, 40. i 60. člen. Jedina ispravka je jezička, u S0-039.

## Zapažanja o jeziku i kvalitetu

- Slovenački je gramatički ispravan i prirodan; formulacije u multi pitanjima su uglavnom doslovno preuzete iz zakona. Nađene su dve dvosmislenosti subjekta (S0-039, S0-050).
- Prevodi su verni. Jedina nedoslednost bila je »nadzorni odbor« naspram »nadzorni savet« (S0-002).
- Brojevi članova u razlagama su tačni, osim 346 umesto 335 u S0-054.
- U više multi pitanja neki tačni odgovori su istinite tvrdnje koje ne odgovaraju strogo na postavljeno pitanje (S0-037 odgovor 5, S0-038 odgovor 5, S0-052 odgovori 3 i 4, S0-051 odgovor 5). Ostavljeno, jer ne protivreče pitanju; ispravljeno samo u S0-041, gde je protivrečnost bila stvarna.

## Šta nije provereno

- Doslovnost teksta 29 single pitanja prema originalnim PDF testovima — originali nisu otvarani; proveravani su samo ključ, razlaga i prevod.
- Navodi u `vir.literatura_str` (brojevi pitanja u studentskim zapisima) i URL-ovi.
- Tvrdnja u razlazi S0-016 da je izuzetak po veličini »ostatak starog uređenja« — iz važećeg teksta se vidi samo da 74. člen takav izuzetak nema.
