# PHASE 8 — FICHE PAR PROPHÉTIE · Workflow

## 1. Objectif
Une **fiche descriptive complète par prophétie du registre** (P001 → P1000) :
contexte, explication, interprétation, accomplissement détaillé, preuves
historiques / géographiques / scientifiques, schéma, chronologie, sources.
Contenu d'exégète, style professionnel, compréhension des Témoins de Jéhovah.

## 2. Cycle d'une vague (S1–S7)
| Étape | Contenu | Sortie |
|---|---|---|
| S1 Plan | Choisir 6–10 P consécutifs, série (GE, EX…), slugs | § journal |
| S2 Recherche | Internet, forums, YouTube, réseaux + **jw.org / wol.jw.org obligatoires** ; dates, TM, it-*/ad | URLs versées |
| S3 Rédaction | `phase8/data/p8_<serie>.py` : CAT + FICHES (11 blocs) | data |
| S4 Build | `phase8/build_p8.py` (wrapper du builder v2 + thème partagé) | `FICHES8_*.html` |
| S5 Images | **≤ 10 JPG/réponse**, hyperréalistes/cinématographiques, `prophe_<N>_<slug>.jpg` | images/ |
| S6 Audios | **≤ 10/réponse, français uniquement**, `fiche_<ABBR><nn>_<slug>.mp3` + intro | audio/ |
| S7 Contrôles | C4–C7, liens morts (img/audio), MAJ `ETATS_PHASE8.md`, présentation | page livrée |

## 3. Gabarit fiche (11 blocs)
1. Identification (réf, statut **recopié du registre**, chrono, registre)
2. Le texte (versets-clés, phrases courtes — **jamais de contenu protégé recopié**)
3. Contexte — 4. Explication — 5. Interprétation — 6. Accomplissement (table)
7. Preuves historiques — 8. Preuves géographiques — 9. Preuves scientifiques
10. **Schéma · l'essentiel** (jamais vide) — 11. **Ce que cette fiche ne dit pas** (jamais vide)
+ Chronologie SVG + Sources (**≥ 2 wol/jw.org**, C4 : rien d'autre en lien).

## 4. Règles inviolables
- Le **registre est la source de vérité** ; la fiche se corrige vers lui.
- Statuts, teneurs, accomplissements : **recopiés, pas réinventés**.
- Un seul système chronologique par fiche (607 · 539 · 537 · 455 · 29 · 33…).
- Aucune date pour l'avenir. Aucun total dogmatique. Aucune donnée personnelle.
- Partage privé, un à un ; liens exclusivement jw.org / wol.jw.org.
- Pas de dogmatique interreligieuse : **les faits, les preuves, les limites**.
- Images : JPG ≤ 10/réponse · Audios : ≤ 10/réponse, français uniquement.
- Ne jamais paralléliser deux écritures sur le **même fichier** (lost update).

## 5. Conventions de nommage
- Fiches : `<LETTRES><nnn>` (ex. GE001) ; images `prophe_GE001_eden.jpg` ;
  audios `fiche_GE01_eden.mp3` ; intros `fiche_GE_intro.mp3` ;
  couvertures `prophe_GE_couverture.jpg` ; pages `FICHES8_GENESE_1.html`.
- Séries : GE Genèse, EX Exode, LV Lévitique… (2 lettres, suites du registre).

## 6. Journal des vagues
| Vague | Date | Série | P couverts | Page produite |
|---|---|---|---|---|
| P8-1 | 2026-09-25 | GE — Genèse (1) | P001–P006 | `FICHES8_GENESE_1.html` · 7 JPG · 7 MP3 |
| P8-2 | 2026-09-25 | GE — Genèse (2) | P007–P012 | `FICHES8_GENESE_2.html` · 6 JPG · 6 MP3 |
| P8-3 | 2026-09-25 | GE — Genèse (3) | P013–P018 | `FICHES8_GENESE_3.html` · 6 JPG · 6 MP3 |
| P8-4 | 2026-09-25 | GE — Genèse (4) | P019–P024 | `FICHES8_GENESE_4.html` · 6 JPG · 6 MP3 |
| P8-5 | 2026-09-25 | GE — Genèse (5) | P025–P030 | `FICHES8_GENESE_5.html` · 6 JPG · 6 MP3 |
| P8-6 | 2026-09-25 | GE — Genèse (6) | P031–P036 | `FICHES8_GENESE_6.html` · 6 JPG · 6 MP3 |
| P8-7 | 2026-09-25 | GE — Genèse (7, transition Exode) | P037–P042 | `FICHES8_GENESE_7.html` · 6 JPG · 6 MP3 |
| P8-8 | 2026-09-25 | EX — Exode (1) | P043–P048 | `FICHES8_EXODE_1.html` · 7 JPG · 7 MP3 |
| P8-9 | 2026-09-25 | EX — Exode (2) | P049–P054 | `FICHES8_EXODE_2.html` · 6 JPG · 6 MP3 |
| P8-10 | 2026-09-25 | DT — Deutéronome (1) | P055–P060 | `FICHES8_DEUTERONOME_1.html` · 7 JPG · 7 MP3 |
| P8-11 | 2026-09-25 | DT — Deutéronome (2) | P061–P066 | `FICHES8_DEUTERONOME_2.html` · 6 JPG · 6 MP3 |
| P8-12 | 2026-09-25 | SM — Samuel (1) | P067–P072 | `FICHES8_SAMUEL_1.html` · 7 JPG · 7 MP3 |
| P8-13 | 2026-09-25 | RO — Rois (1) | P073–P078 | `FICHES8_ROIS_1.html` · 7 JPG · 7 MP3 |
| P8-14 | 2026-09-25 | RO — Rois (2) | P079–P084 | `FICHES8_ROIS_2.html` · 6 JPG · 6 MP3 |
| P8-15 | 2026-09-25 | RO — Rois (3) | P085–P090 | `FICHES8_ROIS_3.html` · 6 JPG · 6 MP3 |
| P8-16 | 2026-09-25 | RO — Rois (4) | P091–P096 | `FICHES8_ROIS_4.html` · 6 JPG · 6 MP3 |
| P8-17 | 2026-09-25 | RO+CH — Rois (5) + Chroniques (1, nouv.) | P097–P102 | `FICHES8_ROIS_5_CHRONIQUES_1.html` · 7 JPG · 7 MP3 |
| P8-18 | 2026-09-25 | CH+ED+NE+IS — Chroniques (2) + Esdras (1, nouv.) + Néhémie (1, nouv.) + Isaïe (1, nouv.) | P103–P108 | `FICHES8_CH_ED_NE_IS.html` · 9 JPG · 10 MP3 |
| P8-19 | 2026-09-25 | IS — Isaïe (2) | P109–P114 | `FICHES8_ISAIE_2.html` · 6 JPG · 6 MP3 |
| P8-20 | 2026-09-25 | IS — Isaïe (3) | P115–P120 | `FICHES8_ISAIE_3.html` · 6 JPG · 6 MP3 |
| P8-21 | 2026-09-25 | IS — Isaïe (4) | P121–P126 | `FICHES8_ISAIE_4.html` · 6 JPG · 6 MP3 |
| P8-22 | 2026-09-25 | IS — Isaïe (5) | P127–P132 | `FICHES8_ISAIE_5.html` · 6 JPG · 6 MP3 |
| P8-23 | 2026-09-25 | IS — Isaïe (6) | P133–P138 | `FICHES8_ISAIE_6.html` · 6 JPG · 6 MP3 |
| P8-24 | 2026-09-25 | IS — Isaïe (7) | P139–P144 | `FICHES8_ISAIE_7.html` · 6 JPG · 6 MP3 |
| P8-25 | 2026-09-25 | IS — Isaïe (8) | P145–P150 | `FICHES8_ISAIE_8.html` · 6 JPG · 6 MP3 |
| P8-26 | 2026-09-25 | IS — Isaïe (9) | P151–P156 | `FICHES8_ISAIE_9.html` · 6 JPG · 6 MP3 |
| P8-27 | 2026-09-25 | IS — Isaïe (10) | P157–P162 | `FICHES8_ISAIE_10.html` · 6 JPG · 6 MP3 |
| P8-28 | 2026-09-25 | IS — Isaïe (11) | P163–P168 | `FICHES8_ISAIE_11.html` · 6 JPG · 6 MP3 |
| P8-29 | 2026-09-25 | IS — Isaïe (12) | P169–P174 | `FICHES8_ISAIE_12.html` · 6 JPG · 6 MP3 |
| P8-30 | 2026-09-25 | IS — Isaïe (13) | P175–P180 | `FICHES8_ISAIE_13.html` · 6 JPG · 6 MP3 |
| P8-31 | 2026-09-25 | JR — Jérémie (1) | P181–P186 | `FICHES8_JEREMIE_1.html` · 7 JPG · 7 MP3 |
| P8-32 | 2026-09-25 | JR — Jérémie (2) | P187–P192 | `FICHES8_JEREMIE_2.html` · 6 JPG · 6 MP3 |
| P8-33 | 2026-09-25 | JR — Jérémie (3) | P193–P198 | `FICHES8_JEREMIE_3.html` · 6 JPG · 6 MP3 |
| P8-34 | 2026-09-25 | JR — Jérémie (4) | P199–P204 | `FICHES8_JEREMIE_4.html` · 6 JPG · 6 MP3 |
| P8-35 | 2026-09-25 | JR — Jérémie (5) | P205–P210 | `FICHES8_JEREMIE_5.html` · 6 JPG · 6 MP3 |
| P8-36 | 2026-09-25 | JR — Jérémie (6) | P211–P216 | `FICHES8_JEREMIE_6.html` · 6 JPG · 6 MP3 |
| P8-37 | 2026-09-25 | JR — Jérémie (7) | P217–P222 | `FICHES8_JEREMIE_7.html` · 6 JPG · 6 MP3 |
| P8-38 | 2026-09-25 | JR — Jérémie (8) | P223–P228 | `FICHES8_JEREMIE_8.html` · 6 JPG · 6 MP3 |
| P8-39 | 2026-09-25 | JR — Jérémie (9) | P229–P234 | `FICHES8_JEREMIE_9.html` · 6 JPG · 6 MP3 |
| P8-40 | 2026-09-25 | JR — Jérémie (10) | P235–P240 | `FICHES8_JEREMIE_10.html` · 6 JPG · 6 MP3 |
| P8-41 | 2026-09-25 | JR — Jérémie (11) | P241–P246 | `FICHES8_JEREMIE_11.html` · 6 JPG · 6 MP3 |
| P8-42 | 2026-09-25 | JR — Jérémie (12) | P247–P252 | `FICHES8_JEREMIE_12.html` · 6 JPG · 6 MP3 |
| P8-43 | 2026-09-25 | JR — Jérémie (13) | P253–P258 | `FICHES8_JEREMIE_13.html` · 6 JPG · 6 MP3 |
| P8-44 | 2026-09-25 | JR — Jérémie (14) | P259–P264 | `FICHES8_JEREMIE_14.html` · 6 JPG · 6 MP3 |
| P8-45 | 2026-09-25 | JR — Jérémie (15) | P265–P270 | `FICHES8_JEREMIE_15.html` · 6 JPG · 6 MP3 |
| P8-46 | 2026-09-25 | JR — Jérémie (16) | P271–P276 | `FICHES8_JEREMIE_16.html` · 6 JPG · 6 MP3 |
| P8-47 | 2026-09-25 | JR — Jérémie (17) | P277–P282 | `FICHES8_JEREMIE_17.html` · 6 JPG · 6 MP3 |
| P8-48 | 2026-09-25 | JR — Jérémie (18) | P283–P288 | `FICHES8_JEREMIE_18.html` · 6 JPG · 6 MP3 |
| P8-49 | 2026-09-25 | JR — Jérémie (19) | P289–P294 | `FICHES8_JEREMIE_19.html` · 6 JPG · 6 MP3 |
| P8-50 | 2026-09-25 | JR+LM — Jérémie (20) + Lamentations (1, nouv.) | P295–P300 | `FICHES8_JEREMIE_20_LAMENTATIONS_1.html` · 6 JPG · 6 MP3 |
| P8-51 | 2026-09-25 | EZ — Ézéchiel (1, nouv.) | P301–P306 | `FICHES8_EZECHIEL_1.html` · 6 JPG · 6 MP3 |
| P8-52 | 2026-09-25 | EZ — Ézéchiel (2) | P307–P312 | `FICHES8_EZECHIEL_2.html` · 6 JPG · 6 MP3 |
| P8-53 | 2026-09-25 | EZ — Ézéchiel (3) | P313–P318 | `FICHES8_EZECHIEL_3.html` · 6 JPG · 6 MP3 |
| P8-54 | 2026-09-25 | EZ — Ézéchiel (4) | P319–P324 | `FICHES8_EZECHIEL_4.html` · 6 JPG · 6 MP3 |
| P8-55 | 2026-09-26 | EZ — Ézéchiel (5) | P325–P330 | `FICHES8_EZECHIEL_5.html` · 6 JPG · 6 MP3 |
| P8-56 | 2026-09-26 | EZ — Ézéchiel (6) | P331–P336 | `FICHES8_EZECHIEL_6.html` · 6 JPG · 6 MP3 |
| P8-57 | 2026-09-26 | EZ — Ézéchiel (7) | P337–P342 | `FICHES8_EZECHIEL_7.html` · 6 JPG · 6 MP3 |
| P8-58 | 2026-09-26 | EZ — Ézéchiel (8) | P343–P348 | `FICHES8_EZECHIEL_8.html` · 6 JPG · 6 MP3 |
| P8-59 | 2026-09-26 | EZ — Ézéchiel (9) | P349–P354 | `FICHES8_EZECHIEL_9.html` · 6 JPG · 6 MP3 |
| P8-60 | 2026-09-26 | EZ — Ézéchiel (10) | P355–P360 | `FICHES8_EZECHIEL_10.html` · 6 JPG · 6 MP3 |
| P8-61 | 2026-09-26 | EZ — Ézéchiel (11) | P361–P366 | `FICHES8_EZECHIEL_11.html` · 6 JPG · 6 MP3 |
| P8-62 | 2026-09-26 | EZ/DN — transition (Shammah + Daniel 1-2) | P367–P372 | `FICHES8_TRANSITION_EZDN.html` · 6 JPG · 6 MP3 |
| P8-63 | 2026-09-26 | DN — Daniel (1) | P373–P378 | `FICHES8_DANIEL_1.html` · 6 JPG · 6 MP3 |
| P8-64 | 2026-09-26 | DN — Daniel (2) | P379–P384 | `FICHES8_DANIEL_2.html` · 6 JPG · 6 MP3 |
| P8-65 | 2026-09-26 | DN — Daniel (3) | P385–P390 | `FICHES8_DANIEL_3.html` · 6 JPG · 6 MP3 |
| P8-66 | 2026-09-26 | DN — Daniel (4) | P391–P396 | `FICHES8_DANIEL_4.html` · 6 JPG · 6 MP3 |
| P8-67 | 2026-09-26 | DN — Daniel (5) | P397–P402 | `FICHES8_DANIEL_5.html` · 6 JPG · 6 MP3 |
| P8-68 | 2026-09-26 | DN — Daniel (6, fin du livre) | P403–P407 | `FICHES8_DANIEL_6.html` · 5 fiches · 6 JPG · 5 MP3 |
| P8-69 | 2026-09-26 | OS — Osée (1) | P408–P413 | `FICHES8_OSEE_1.html` · 6 fiches · 7 JPG · 6 MP3 (audio OS409 rattrapé en P8-70) |
| P8-70 | 2026-09-26 | OS — Osée (2) | P414–P419 | `FICHES8_OSEE_2.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-71 | 2026-09-26 | OS/JL — fin d'Osée puis Joël 1 | P420–P423 | `FICHES8_OSEE_3.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-72 | 2026-09-26 | JL — fin de Joël (2-3) | P424–P429 | `FICHES8_JOEL_1.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-73 | 2026-09-26 | AM — ouverture d'Amos (1-5) | P430–P435 | `FICHES8_AMOS_1.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-74 | 2026-09-26 | AM — fin d'Amos (6-9) | P436–P441 | `FICHES8_AMOS_2.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-75 | 2026-09-26 | AB — Abdias (le livre entier) | P442–P446 | `FICHES8_ABDIAS_1.html` · 5 fiches · 6 JPG · 5 MP3 |
| P8-76 | 2026-09-26 | JN — Jonas (le livre entier) | P447–P450 | `FICHES8_JONAS_1.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-77 | 2026-09-26 | MI — Michée (1) | P451–P456 | `FICHES8_MICHEE_1.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-78 | 2026-09-26 | MI — Michée (2, fin du livre) | P457–P462 | `FICHES8_MICHEE_2.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-79 | 2026-09-26 | NA — Nahum (1-2) | P463–P466 | `FICHES8_NAHOUM_1.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-80 | 2026-09-26 | NA — Nahum (3, fin du livre) | P467–P469 | `FICHES8_NAHOUM_2.html` · 3 fiches · 4 JPG · 3 MP3 |
| P8-81 | 2026-09-26 | HA — Habacuc (1-2) | P470–P473 | `FICHES8_HABACUC_1.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-82 | 2026-09-26 | HA — Habacuc (2:18-20 et 3, fin du livre) | P474–P475 | `FICHES8_HABACUC_2.html` · 2 fiches · 3 JPG · 2 MP3 |
| P8-83 | 2026-09-26 | SO — Sophonie (1) | P476–P478 | `FICHES8_SOPHONIE_1.html` · 3 fiches · 4 JPG · 3 MP3 |
| P8-84 | 2026-09-26 | SO — Sophonie (2) | P479–P482 | `FICHES8_SOPHONIE_2.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-85 | 2026-09-26 | SO — Sophonie (3, fin du livre) | P483–P484 | `FICHES8_SOPHONIE_3.html` · 2 fiches · 3 JPG · 2 MP3 |
| P8-86 | 2026-09-26 | AG — Aggée (livre entier) | P485–P489 | `FICHES8_AGGEE_1.html` · 5 fiches · 6 JPG · 5 MP3 |
| P8-87 | 2026-09-26 | ZA — Zacharie 1-3 (les huit visions, les cornes, le cordeau, le Germe) | P490–P494 | `FICHES8_ZACHARIE_1.html` · 5 fiches · 6 JPG · 5 MP3 |
| P8-88 | 2026-09-26 | ZA — Zacharie 4-6 (le chandelier et les deux oints, le rouleau volant, les quatre chars, la couronne du Germe) | P495–P498 | `FICHES8_ZACHARIE_2.html` · 4 fiches · 5 JPG · 4 MP3 |
| P8-89 | 2026-09-26 | ZA — Zacharie 7-10 (les jeûnes, le retour à Sion, le roi sur un âne, le fardeau sur les nations, la pluie) | P499–P505 | `FICHES8_ZACHARIE_3.html` · 7 fiches · 8 JPG · 7 MP3 |
| P8-90 | 2026-09-26 | ZA — Zacharie 11-14 (les trente pièces d'argent, le berger frappé, la source ouverte et le jour de Jéhovah) | P506–P511 | `FICHES8_ZACHARIE_4.html` · 6 fiches · 7 JPG · 6 MP3 |
| P8-91 | 2026-09-26 | ML — Malachie (l'amour de Jacob, le messager du temple, la dîme et le soleil de justice) | P512–P519 | `FICHES8_MALACHIE_1.html` · 8 fiches · 9 JPG · 8 MP3 |
