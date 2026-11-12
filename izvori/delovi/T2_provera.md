# T2 — izveštaj nezavisne provere ključa

Fajl: `T2_pitanja.json` (55 pitanja, sva `multi`, tema 2 Statusno pravo – splošni del).
Izvori: `zakoni/ZGD-1.md` (čl. 1–63, 71–75, 674–683 pročitani u celini, uklj. ceo 10.a) i `zakoni/ZSReg.md` (čl. 1, 1.a, 2, 2.a, 3, 7, 8).

## Zbir

| Ishod | Broj |
|---|---|
| Potvrđeno bez izmena sadržaja | 53 |
| Ispravljeno i potvrđeno | 2 (T2-005, T2-027) |
| Odbijeno (`preverjeno: false`) | 0 |

Svih 55 ima `preverjeno: true`. Ni kod jednog pitanja ključ (`pravilno`) nije menjan.

## Ispravke

| id | Šta | Zašto | Član |
|---|---|---|---|
| T2-005 | Odgovor 4 (tačan) preformulisan: „Omejitve ustanavljanja ne veljajo za osebo, ki je postala družbenik…" → „Omejitve iz prvega odstavka 10.a člena ne veljajo za osebo, ki je postala družbenik ali podjetnik na podlagi univerzalnega pravnega nasledstva."; prevod i razlaga usklađeni | Izuzetak za univerzalno sledbeništvo pokriva samo ograničenja iz 1. odst.; ograničenje iz 5. odst. (d.o.o. u poslednja tri meseca) ima sopstvene izuzetke u 6. i 7. odst. Stara formulacija je bila preširoka | ZGD-1, 10.a čl., 2., 5., 6. i 7. odst. |
| T2-005 | Razlaga odgovora 3 dopunjena (ograničenje prestaje brisanjem iz kaznene evidencije); `vir.zakon_clen` proširen na 1., 2., 5. i 8. odst. | Autor nije pročitao ceo 10.a | ZGD-1, 10.a čl., 8. odst. |
| T2-027 | `prevod_sr` odgovora „Prodati nepremičnine družbe": „nepokretnost" → „nepokretnosti" | Slovenački original je u množini | — |
| 11 razlaga (više pitanja) | U `razlaga_sr` slovenački veznik u citatima („1. in 2. odst.") zamenjen srpskim („1. i 2. odst.") | Mešanje jezika u srpskom tekstu; isti fajl je na drugim mestima već koristio „i" | — |

## Odbijena

Nema.

## Posebno tražene provere

- **Distraktori „zakon to ne predviđa" (T2-009, T2-011, T2-048; uz to T2-049, T2-047, T2-052)** — prihvaćeni, jer citirani član iscrpno uređuje pitanje:
  - T2-009: 6. čl., 5. odst. sam određuje punovažnost posla (jedini izuzetak: treće lice znalo ili moralo znati), pa su „ništav", „samo ako je delatnost upisana" i „tek po odobrenju skupštine" u suprotnosti sa tekstom.
  - T2-011: pitanje izričito pita „po 8. členu"; 8. čl., 1. odst. ima zatvorenu listu od četiri alineje („in to:"); gubitak u dve godine nije među njima.
  - T2-048: distraktori su suprotni izričitom tekstu 75. čl., 1. odst. (15 dana; najmanje tri dana ranije; obaveza prijave prestanka).
  - T2-049: 75. čl., 2. odst. je taksativna lista (tačke 1–8); gubitak nije razlog.
  - T2-047 (odg. 5, „srednji/veliki preduzetnik u sudski registar"): 74. čl., 1. odst. bez izuzetka + ZSReg 3. čl. nabraja samo pravna lica i njihove delove.
  - T2-052: pitanje je vezano za listu iz 71. čl. (6; 12–23; 29, 30/1, 30.a; 31; 33–37) — 8. i 41. čl. nisu na njoj.
- **T2-005 (čl. 10.a)** — pročitan ceo član (20 stavova); ispravka gore. Ključ ostaje 3 tačna.
- **T2-040–043 (čl. 55, 54, 58)** — brojke doslovno potvrđene: mikro 10 / 900.000 / 450.000; malo 50 / 10.000.000 / 5.000.000; srednje 250 / 50.000.000 / 25.000.000; dva od tri kriterijuma; prerazvrstavanje po dve uzastopne godine (55/6). Primer u T2-041 (40 zaposlenih, 12 mil. prihoda, 4 mil. aktive) = malo društvo: nije mikro (0 od 3), ispunjava 2 od 3 za malo. Rokovi u T2-043: 3 meseca sastavljanje (54/1), 4 meseca konsolidovani (54/2), 8 meseci revidirani AJPES-u (58/1), 3 meseca mala društva i preduzetnici (58/3).
- **T2-027 (čl. 35)** — ključ tačan: posebno ovlašćenje samo za „odsvojitev in obremenitev nepremičnin" (35/1); kupovina nepokretnosti i akcija nije izuzeta; zastupanje pred sudom 35/3.
- **Pitanja `po_zapiskih`** — u fajlu su to T2-019, 024, 027, 028 i **047** (ne 046; T2-046 je `generisano_po_gradivu`). Svih pet (i T2-046) provereno po važećem tekstu: T2-019 čl. 27/1 + 12/2; T2-024 čl. 32/2; T2-027 i T2-028 čl. 35; T2-047 čl. 74/1.

## Zapažanja o jeziku

- Slovenački je gramatički ispravan i prirodan; većina tačnih odgovora je doslovan ili skoro doslovan tekst zakona. Nisam našao slovne ni padežne greške.
- Prevodi na srpski su verni; terminologija dosledna (družbenik = član, podružnica = ogranak, firma = poslovno ime).
- U `razlaga_sr` autor ostavlja slovenačke oznake „člen / odst. / alineja / točka" — dosledno kroz ceo fajl, nije dirano.
- U T2-019 `prevod_sr` odgovora ostaje na slovenačkom (to su nazivi firmi) — ispravno.
- Nekoliko tačnih odgovora je skraćeni citat pravila bez izuzetka iz istog člana (T2-014 odg. 2: čl. 16 bez dela o umrloj osobi; T2-042 odg. 4: pragovi srednjeg društva bez „dva od tri"; T2-054 odg. 4: definicija bez dela o državi članici / trećoj državi). Ostaju tačni kako su napisani; razlage navode ostatak.

## Šta nije provereno

- Zakon o poslovnim tajnama (ZPosS) nije među izvorima; T2-031 je proveren samo prema ZGD-1 čl. 39–40, 58/4 i ZSReg čl. 7.
- ZPRS-1 (Poslovni registar) nije među izvorima; tvrdnje o AJPES-u oslonjene su na ZGD-1 čl. 74–75 i ZSReg čl. 1.a, 2.a.
- `kljucne_besede_sl`, `tezina` i `podtema` nisu sadržinski ocenjivani.

## Provera strukture

Validan JSON; 55 pitanja; jedinstveni id; svako `multi` ima 5 odgovora sa 1–4 tačna; `id`, `tema`, `poreklo` nepromenjeni; nema novih pitanja.
