# T3 — izveštaj nezavisne provere ključa

Fajl: `T3_pitanja.json` (65 pitanja, sva `multi`, 5 odgovora). Izvori: `zakoni/ZGD-1.md` (NPB 24), `ZZad.md`, `ZZ.md`. Svaki član iz `vir.zakon_clen` i iz `razlaga_sr` otvoren je i pročitan u tekstu zakona; svih 325 odgovora upoređeno je sa tekstom.

## Brojevi

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmene sadržaja | 61 |
| Ispravljeno pa potvrđeno (`preverjeno: true`) | 4 |
| Odbijeno (`preverjeno: false`) | 0 |

Nijedan ključ (`pravilno`) nije promenjen — nije nađen nijedan pogrešno okrenut ključ ni pogrešna brojka.

## Ispravke

| id | Šta | Zašto | Član |
|---|---|---|---|
| T3-012 | Odgovor „Najmanj en družbenik (komanditist) ni odgovoren za obveznosti družbe” preformulisan u „Po opredelitvi iz 135. člena ZGD-1 je v komanditni družbi najmanj en družbenik (komanditist), ki ni odgovoren za obveznosti družbe”; prevod i razlaga usklađeni | Kao samostalna tvrdnja dvosmislen prema 145. členu (odgovornost do visine neuplaćenog uloga); vezan za doslovnu definiciju postaje jednoznačan | ZGD-1 135/1, 145 |
| T3-050 | Odgovor „Odločitve o teh vprašanjih …” → „Odločitve o vprašanjih iz 505. člena ZGD-1 (o katerih sicer odločajo družbeniki) …”; u vir dodat 505. člen | „teh vprašanjih” se pozivalo na drugi odgovor (stajao je čak iza njega) — posle mešanja redosleda nerazumljivo | ZGD-1 526/1–2, 505 |
| T3-061 | Pitanje „Katere trditve so pravilne?” → „Katere trditve o prenosu premoženja in o statusnem preoblikovanju podjetnika so po ZGD-1 pravilne?” (+ prevod) | Pitanje bez predmeta | ZGD-1 640, 579/2, 667 |
| T3-015 | Prevod: „koji je morao uplatiti” → „koji bi morao uplatiti” | Vernost („bi ga moral vplačati”) | ZGD-1 145 |

Dopune `vir.zakon_clen` članovima koji se citiraju u razlagama a nisu bili navedeni (bez uticaja na sadržaj): T3-001 (523), T3-003 (265, 268), T3-005 (144), T3-032 (329/1), T3-036 (405), T3-046 (ZZad 18), T3-061 (580; 3/3), T3-063 (ZGD-1 506), T3-065 (ZGD-1 268).

## Odbijena pitanja

Nema.

## Posebno tražene tačke

1. **Brojke** — sve doslovno potvrđene: 25.000 (171), 7.500 i 50 EUR (475/1), četvrtina + 7.500 (475/4), najviše 50 članova (473), manje od 50 akcionara i 9/10 (648), 1 EUR (172), 5 % (95/1), 6 meseci (106/1), 1 godina (115), mandat do 6 godina (255/1), „već u tri društva” (273/1), 3/4 datih glasova (275/1, 281/5), 3/4 zastupljenog kapitala (329/2, 333/1, 402/1, 585/2), 14 dana (337/1), 30 dana d.d. / 25 dana d.o.o. (297/1, 509/1), desetina (511/1, 521/2), 3/4 glasova svih članova (516/1, 521/1), poslovodja najmanje 2 godine (515/2), isplata 3 / 6 godina (502/5–6), 1 mesec (481/5), 6 meseci i 2 godine (421/1, 425/2), više od četvrtine (531/1), 2 godine u registru (616/2), 3 osnivača i 10 članova zadruge (ZZad 4, 14).
2. **Distraktori „odsustvom odredbe”** — svi prihvaćeni jer je citirana odredba zatvorena lista:
   - d.n.o. bez minimalnog kapitala (T3-001): čl. 76–134 ne propisuju osnovni kapital; 7.500 je izričito d.o.o. (475/1).
   - „isto sedište i delatnost” (T3-053): 527 je taksativna lista od pet alineja, bez „zlasti”.
   - „promena firme ili sedišta” (T3-055): 579/1 taksativno navodi četiri oblika.
   - opoziv člana uprave „kadarkoli, brez razloga” (T3-028): 268/2 navodi zatvorenu listu razloga (četvrta alineja je široka, ali i dalje traži razlog); kontrast 290/8 i 515/3 gde zakon izričito kaže „kadarkoli”.
   - smrt akcionara (T3-035): nije u listi 402/1; pitanje je korektno ograničeno na „zakonski razlog” (402/2 dopušta statutarne razloge).
3. **Komanditist** — T3-012 preformulisan (gore). U T3-014 i T3-016 ista fraza se javlja samo unutar netačnih distraktora čiji je zaključak netačan po 138/3 odnosno 150, pa je ostavljena.
4. **Akcije bez prava glasa** (T3-024) — odgovor je već formulisan „Po 178. členu ZGD-1 … samo prednostne delnice”, a razlaga pominje 317; jednoznačno.
5. **Oblik društvenog ugovora d.o.o. i prenos udela** (T3-042, T3-043, T3-044) — tačno po 474/1 (notarski zapis ILI poseban obrazac, overeni potpisi), 523/1, 481/1–8, 482/1.
6. **Jednodomni/dvodomni sistem i nadležnosti organa** (T3-025–T3-033) — tačno po 253, 255, 257, 265, 266, 268, 273–275, 281/5, 285, 290, 293.

## Zapažanja o kvalitetu

- Slovenački je gramatički ispravan i prirodan; većina tačnih odgovora je doslovan ili gotovo doslovan citat zakona. Prevodi su verni; terminologija dosledna (enotirni/dvotirni = jednodomni/dvodomni, nadzorni svet = nadzorni odbor).
- Negativno formulisana pitanja (NISO / NE / RAZEN / NI) imaju pravilno okrenut ključ, a razlage jasno pišu „Označava se / Ne označava se”.
- Sitnica ostavljena bez izmene: T3-036, „šest mesecev od zadnje objave sklepa o likvidaciji” — zakon (421/1) kaže „od zadnje objave po 405. členu”; 405 uređuje sadržaj odluke o likvidaciji i rok „od objave sklepa”, pa je parafraza prihvatljiva.
- T3-010: zakon kaže „mora … ali” (115/1), odgovori kažu „lahko” — u okviru pitanja „Katere možnosti mu daje zakon” prihvatljivo.
- 16 pitanja ima samo jedan tačan odgovor (u okviru dozvoljenog 1–4).

## Provera strukture

Validan JSON; 65 pitanja; svi `id` jedinstveni; svako `multi` ima 5 različitih odgovora i 1–4 tačna (raspodela: 1 tačan ×16, 2 ×23, 3 ×20, 4 ×6); `id`, `tema`, `poreklo` netaknuti.

## Šta nije provereno

- Ispravnost `vir.url` (nije otvaran pisrs; Playwright/tvly zabranjeni).
- Tekst zakona proveravan samo prema lokalnim NPB fajlovima; nisu proveravane eventualne izmene posle verzije u `INDEX.md`.
- Polja `tezina` i `kljucne_besede_sl` nisu sistematski ocenjivana.
