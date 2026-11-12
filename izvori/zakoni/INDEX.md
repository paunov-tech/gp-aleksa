# INDEX — slovenački zakoni za predmet Gospodarsko pravo (izvor: pisrs.si)

Datum pristupa: 2026-11-13. Svi tekstovi su **neuradna prečiščena besedila (NPB) sa pisrs.si** (Pravno-informacijski sistem RS), preuzeti mašinski preko javnog API-ja portala. Nijedan tekst nije sa rezervnog izvora.

## Metod preuzimanja (radi bez browsera, običan HTTP GET)

1. Metapodaci + spisak NPB verzija: `https://pisrs.si/api/rezultat/zbirka/id/<ID>` (npr. `ZAKO4291`); alternativno po SOP: `https://pisrs.si/api/rezultat/zbirka/sop/<SOP>`.
   - `data.besedilo.npbVerzije[]` → `id`, `naziv` (NPB n), `datumZacetkaUporabe`; `data.datoteke[]` → ID-jevi fajlova (HTML/DOCX/PDF) po verziji.
2. Tekst verzije kao JSON (element po element, sa poljem `struktura`: clen/odstavek/alinea/poglavje…): `https://pisrs.si/api/rezultat/neuradno-precisceno-besedilo/<npbVerzijaId>`
3. Fajl (HTML/PDF/DOCX): `https://pisrs.si/api/datoteke/integracije/<fileId>`
4. Pretraga ID-ja po naslovu: `POST https://pisrs.si/api/filter/filter` sa JSON telom `{"simpleSearch":true,"besedilo":{"word1":"<naslov>","word1InTitle":true,"word1InContent":false},"nazivZbirke":["Register predpisov"]}` → `data.seznam[].zunanjiId`.

Izbor verzije: poslednja NPB verzija čiji `datumZacetkaUporabe` nije u budućnosti u odnosu na 2026-11-13.

## Struktura fajlova

- `<KRATICA>.md` — pun tekst; YAML zaglavlje sa metapodacima; naslovi članova kao `### N. člen`; poglavlja kao `## …`.
- `raw/<KRATICA>_<verzija>.json|.html|.pdf` — sirovi fajlovi sa pisrs; `raw/<KRATICA>_meta.json` — metapodaci registra.
- Kontrola kvaliteta: broj naslova članova u .md je upoređen sa nezavisnim brojanjem u sirovom HTML-u (poklapa se za svih 15 fajlova); numeracija osnovnog teksta je proverena na neprekidnost (nema rupa).

## Upozorenja za čitanje

- **OZ i SPZ: naslov člana stoji IZNAD broja člana** (red `**Naslov**` pa `### N. člen`). U ostalim zakonima naslov (u zagradi) je ispod broja.
- Na kraju nekih fajlova (OZ, SPZ, ZSReg, ZZad, ZGZ, ZGJS) nalazi se dodatak „PREHODNE IN KONČNE DOLOČBE …“ gde se **brojevi članova ponavljaju** (članovi novela) — ne mešati sa osnovnim tekstom.
- Članovi označeni `(prenehal veljati)` / `(črtan)` / `(razveljavljen)` imaju naslov ali ne i tekst.
- **Sudovi:** ZS (stari) formalno ne važi od 19.12.2025, ali se primenjuje do 1.1.2027; ZS-1 se primenjuje od 1.1.2027. Za pitanja o vrstama/nadležnosti sudova proveriti na koji se zakon ključ odgovora oslanja.

## Tabela

| Zakon | Pun naziv | ID | URL | Verzija / važi od | Broj članova u fajlu | Status |
|---|---|---|---|---|---|---|
| ZGD-1 | Zakon o gospodarskih družbah (ZGD-1) | ZAKO4291 | https://pisrs.si/pregledPredpisa?id=ZAKO4291 | NPB 24 / važi od: 2026-07-24; posl. izmena u registru: Ur. l. RS 1270/26 | 843 (od toga 2 prestalo/črtano; raspon 1. člen – 709. člen) + 0 u dodatku novela | OK — 843 naslova članova = 1–709 + umetnuti (npr. 10.a, 70.a–70.e...); 2 člana prestala da važe (49, 703). NPB 24 obuhvata ZGD-1O (Ur. l. 1270/26). |
| OZ | Obligacijski zakonik (OZ) | ZAKO1263 | https://pisrs.si/pregledPredpisa?id=ZAKO1263 | NPB 4 / važi od: n/n; posl. izmena u registru: Ur. l. RS 20/18 – OROZ631 | 1060 (od toga 0 prestalo/črtano; raspon 1. člen – 1059. člen) + 5 u dodatku novela | OK — Naslovi članova stoje IZNAD broja člana. Poslednja stavka registra (20/18 – OROZ631) je autentično tumačenje čl. 631, ne menja tekst; NPB 4 zato završava sa 64/16 (odl. US, čl. 184 razveljavljen). Čl. 1060–1062 (prehodne in končne) su u dodatku. |
| SPZ | Stvarnopravni zakonik (SPZ) | ZAKO3242 | https://pisrs.si/pregledPredpisa?id=ZAKO3242 | NPB 2 / važi od: n/n; posl. izmena u registru: Ur. l. RS 23/20 | 272 (od toga 0 prestalo/črtano; raspon 1. člen – 265. člen) + 19 u dodatku novela | OK — Naslovi članova stoje IZNAD broja člana. Čl. 266–276 (prehodne in končne določbe) su u dodatku na kraju fajla. |
| URS | Ustava Republike Slovenije (URS) | USTA1 | https://pisrs.si/pregledPredpisa?id=USTA1 | NPB 12 / važi od: 2025-12-01; posl. izmena u registru: Ur. l. RS 98/25 – UZ74a | 178 (od toga 0 prestalo/črtano; raspon 1. člen – 174. člen) + 0 u dodatku novela | OK — Ceo tekst Ustave (ne samo relevantni delovi); 174 člana + 3.a, 62.a, 70.a, 74.a. Obuhvata UZ74a (98/25). |
| ZSReg | Zakon o sodnem registru (ZSReg) | ZAKO320 | https://pisrs.si/pregledPredpisa?id=ZAKO320 | NPB 14 / važi od: n/n; posl. izmena u registru: Ur. l. RS 102/23 – ZViS-M | 76 (od toga 0 prestalo/črtano; raspon 1. člen – 53. člen) + 40 u dodatku novela | OK — ID u zadatku (ZAKO1041) je bio pogrešan (to je MKUNM); tačan ID je ZAKO320. Većina članova nema naslov. Prelazne odredbe novela u dodatku. |
| ZS | Zakon o sodiščih (ZS) | ZAKO332 | https://pisrs.si/pregledPredpisa?id=ZAKO332 | NPB 30 / važi od: n/n; posl. izmena u registru: Ur. l. RS 100/25 – ZS-1 | 182 (od toga 34 prestalo/črtano; raspon 1. člen – 135. člen) + 0 u dodatku novela | OK — PAŽNJA: ZS je prestao da važi 19.12.2025 (zamenjen ZS-1, Ur. l. 100/25), ali se JOŠ PRIMENJUJE do 1.1.2027 — na dan pristupa ovo je propis koji se primenjuje. NPB 30 ne obuhvata ZS-1 (logično). |
| ZS-1 | Zakon o sodiščih (ZS-1) | ZAKO8887 | https://pisrs.si/pregledPredpisa?id=ZAKO8887 | Osnovni / važi od: n/n; posl. izmena u registru: Ur. l. RS 1568/26 – ZSOKOK | 175 (od toga 0 prestalo/črtano; raspon 1. člen – 175. člen) + 0 u dodatku novela | OK — Novi zakon: važi od 19.12.2025, PRIMENJUJE SE tek od 1.1.2027. Preuzet osnovni tekst (Ur. l. 100/25); na pisrs postoji i NPB 1 (posle ZSOKOK, Ur. l. 1568/26) sa početkom primene 1.7.2027 — nije preuzet. |
| ZPP | Zakon o pravdnem postopku (ZPP) | ZAKO1212 | https://pisrs.si/pregledPredpisa?id=ZAKO1212 | NPB 30 / važi od: n/n; posl. izmena u registru: Ur. l. RS 92/24 – odl. US | 554 (od toga 43 prestalo/črtano; raspon 1. člen – 503. člen) + 0 u dodatku novela | OK — Ceo zakon (ne samo nadležnost). 43 člana prestala da važe/črtana (npr. 54–56, 406–423, 459–479). Većina članova bez naslova. Obuhvata odl. US 92/24. |
| ZArbit | Zakon o arbitraži (ZArbit) | ZAKO5288 | https://pisrs.si/pregledPredpisa?id=ZAKO5288 | NPB 1 / važi od: n/n; posl. izmena u registru: Ur. l. RS 100/25 – ZS-1 | 52 (od toga 0 prestalo/črtano; raspon 1. člen – 52. člen) + 0 u dodatku novela | OK — Obuhvata izmenu kroz ZS-1 (100/25). |
| ZMCGZ | Zakon o mediaciji v civilnih in gospodarskih zadevah (ZMCGZ) | ZAKO5289 | https://pisrs.si/pregledPredpisa?id=ZAKO5289 | Osnovni / važi od: n/n; posl. izmena u registru: Ur. l. RS št. 56/08 | 20 (od toga 0 prestalo/črtano; raspon 1. člen – 20. člen) + 0 u dodatku novela | OK — Nema novela — važi osnovni tekst (Ur. l. 56/08); zato nema NPB, preuzet "Osnovni". |
| ZFPPIPP | Zakon o finančnem poslovanju, postopkih zaradi insolventnosti in prisilnem prenehanju (ZFPPIPP) | ZAKO4735 | https://pisrs.si/pregledPredpisa?id=ZAKO4735 | NPB 27 / važi od: n/n; posl. izmena u registru: Ur. l. RS 100/25 – ZS-1 | 611 (od toga 4 prestalo/črtano; raspon 1. člen – 500. člen) + 0 u dodatku novela | OK — Ceo zakon. Obuhvata izmenu kroz ZS-1 (100/25). 4 člana črtana/prestala. |
| ZZad | Zakon o zadrugah (ZZad) | ZAKO217 | https://pisrs.si/pregledPredpisa?id=ZAKO217 | NPB 6 / važi od: n/n; posl. izmena u registru: Ur. l. RS 121/21 | 145 (od toga 0 prestalo/črtano; raspon 1. člen – 70. člen) + 23 u dodatku novela | OK — 1–70 + mnogo umetnutih članova (46.a…, 56.a…); prelazne odredbe novela u dodatku. |
| ZGZ | Zakon o gospodarskih zbornicah (ZGZ) | ZAKO4251 | https://pisrs.si/pregledPredpisa?id=ZAKO4251 | NPB 2 / važi od: n/n; posl. izmena u registru: Ur. l. RS 77/11 | 25 (od toga 0 prestalo/črtano; raspon 1. člen – 25. člen) + 20 u dodatku novela | OK — ID nije bio dat; pronađen pretragom: ZAKO4251. Prelazne odredbe u dodatku. |
| ZZ | Zakon o zavodih (ZZ) | ZAKO10 | https://pisrs.si/pregledPredpisa?id=ZAKO10 | NPB 3 / važi od: 2007-03-07; posl. izmena u registru: Ur. l. RS 127/06 – ZJZP | 72 (od toga 1 prestalo/črtano; raspon 1. člen – 72. člen) + 0 u dodatku novela | OK — Članovi nemaju naslove. Čl. 60 prestao da važi. |
| ZGJS | Zakon o gospodarskih javnih službah (ZGJS) | ZAKO272 | https://pisrs.si/pregledPredpisa?id=ZAKO272 | NPB 3 / važi od: n/n; posl. izmena u registru: Ur. l. RS 57/11 – ORZGJS40 | 67 (od toga 0 prestalo/črtano; raspon 1. člen – 67. člen) + 20 u dodatku novela | OK — Poslednja stavka registra (57/11 – ORZGJS40) je autentično tumačenje čl. 40, ne menja tekst. |
