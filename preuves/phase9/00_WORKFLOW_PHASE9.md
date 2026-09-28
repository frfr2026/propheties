# PHASE 9 — FICHES MANQUANTES (P520 → P1120) · Workflow

## 1. Objectif de la phase
Produire **une fiche descriptive complète pour chaque entrée du registre qui n'en a pas
encore** : les 481 entrées P520–P1000 (la phase 8 s'est arrêtée à P519) et les
120 entrées de la **partie 15** (P1001–P1120), intégrées le 27 septembre 2026 à partir
des priorités A de l'audit de complétude (`AUDIT_COMPLETUDE_REGISTRE.md`,
`24_REGISTRE_PROPHETIES_8.md`). Soit **601 fiches** (file d'attente : `phase9/etat.json`).

Contenu attendu par fiche (gabarit phase 8 conservé, 11 blocs) : contexte du texte,
explication, interprétation (compréhension des Témoins de Jéhovah, sourcée),
accomplissement détaillé, preuves historiques / géographiques / scientifiques, schéma
visuel, limites, chronologie SVG, sources officielles ; **une illustration JPG
hyperréaliste et une piste audio française par fiche**, affichées sur la fiche.

## 2. Ce qui a été fait à l'ouverture de la phase (27/09/2026)
| Étape | Résultat |
|---|---|
| Intégration des priorités A | `24_REGISTRE_PROPHETIES_8.md` — **PARTIE 15, 120 entrées P1001–P1120**, ordre canonique |
| Fusion des entrées similaires | 9 fusions (parallèles synoptiques, type/antitype, oracle/citation apostolique) : Ex 3+7 · Ex 4+11 · Ex 7-11 + Goshèn · Nb 21 + Jn 3/8/12 · Is 45 + Php 2 · Is 48 + 52 · Mt 19/Lc 22 + 1Co 6 · Ac 1 + Hé 9 · Ac 17 + 2Tm 4/Ac 10/1P 4 |
| Propositions B et C | `25_PROPOSITIONS_B_C_EN_ATTENTE.md` — 97 lignes hors registre, à valider |
| Traçabilité | `phase9/tools/correspondance_audit_registre.tsv` (n° audit → n° définitif) |
| Outils | `phase9/tools/build_partie15.py` (registre), `phase9/tools/etat.py` (machine à états), `phase9/build_p9.py` (pages) |

## 3. Cycle d'une vague (S1–S8)
| Étape | Contenu | Sortie / contrôle |
|---|---|---|
| S1 Plan | `etat.py next` → 6 à 10 P consécutifs d'un même livre ; codes `<SÉRIE><P>` ; slugs d'images/audios | `etat.py vague P9-n … --page … --cat …` |
| S2 Recherche | **wol.jw.org / jw.org obligatoires** (Étude perspicace, Tour de Garde, « Livre de la Bible n° »), puis web, forums, vidéos, réseaux ; documents profanes (Josèphe, Strabon, Tacite, tablettes, papyrus) ; état de la recherche scientifique **y compris ses rétractations** | identifiants wol notés dans `src` ; `etat.py set <CODE> RECHERCHE` |
| S3 Rédaction | `phase9/data/p9_<serie><n>.py` : `CAT` + `FICHES` (11 blocs, texte, accomplissement, `tl`, `src`, `P`, `type`) ; statut **recopié du registre** | `etat.py set <CODE> REDACTION` |
| S4 Contrôle | `python3 build_p9.py p9_xxx FICHES9_XXX.html` : C4 (liens officiels seuls), C5 (limites non vides), C6 (aucun bloc vide), C7 (≥ 2 sources officielles) ; relecture des dates (un seul système) | `etat.py set <CODE> CONTROLE` |
| S5 Images | **≤ 10 JPG par réponse**, hyperréalistes, photoréalistes, cinématographiques ; `images/prophe_<CODE>_<slug>.jpg` ; aucune représentation de Dieu, aucune inscription illisible imposée | `etat.py media <CODE> --img …` |
| S6 Audios | **≤ 10 MP3 par réponse, français uniquement**, ≤ 1 500 caractères par piste, voix unique de la phase (voice-00) ; `audio/fiche_<CODE>_<slug>.mp3` | `etat.py media <CODE> --mp3 …` ; `etat.py set <CODE> MEDIAS` |
| S7 Rebuild + liens | rebuild de la page (les médias sont appariés par le résolveur `theme.py`), vérification « 0 lien mort » (`grep src=` + `test -f`) | page définitive |
| S8 Publication | `etat.py set <CODE> PUBLIE` pour chaque fiche, `etat.py md` (tableau de bord), présentation de la page, mise à jour d'`INVENTAIRE_DEPOT.md` si un fichier nouveau apparaît | `ETATS_PHASE9.md` à jour |

Rythme : une vague par réponse (limites médias). Si la réponse atteint sa limite, la
vague est arrêtée proprement à l'état atteint (jamais de page sans validation) et
reprise à la réponse suivante sur demande de l'utilisateur (« continue »).

## 4. Gabarit fiche (11 blocs) et conventions
1. Identification (réf., statut du registre, système chronologique, ligne « Registre », lien vers le fichier de registre, type de fiche)
2. Le texte (versets-clés en phrases courtes, mots hébreux/grecs translittérés — jamais de reproduction longue)
3. Contexte — 4. Explication — 5. Interprétation (sourcée wol) — 6. Accomplissement (tableau Quand/Événement)
7. Preuves historiques — 8. Preuves géographiques — 9. Preuves scientifiques et archéologiques
10. Schéma · l'essentiel (chaîne « A → B → C », rendue en frise visuelle) — 11. Ce que cette fiche ne dit pas (jamais vide)
+ Chronologie SVG (`tl`, 5 à 8 jalons) + Sources (≥ 2 wol/jw.org ; C4 : aucun autre lien).

Types de fiches (`etat.json`) : **complète** (492) · **commune** (59 : mêmes versets qu'une
entrée plus petite de P520–P1120, traitée sur la fiche de celle-ci avec mention) ·
**renvoi** (50 : entrée de la partie 8 messianique qui répète une entrée P001–P519 déjà
dotée d'une fiche phase 8 ; fiche courte + lien).

Mise en œuvre des renvois (depuis P9-2) : le module de données déclare une liste `RENVOIS`
(clés `n, P, ref, type, teneur, statut, note, liens[(texte, url)]`) ; `build_p9.py` la rend en
`<section class="renvois" id="renvois">` (tableau) juste avant `<footer class="site">`. Les liens
pointent vers l'ancre `FICHES8_<LIVRE>_<n>.html#<CODE>` (à vérifier par `grep id="<CODE>"`) et vers
le fichier du registre. Un renvoi n'a **aucun média propre** (ni JPG ni MP3) : il passe
RECHERCHE → REDACTION → CONTROLE → MEDIAS (note « aucun média propre ») → PUBLIE. Une fiche
**commune** n'est publiée qu'avec la fiche de son entrée cible (ex. GE975 avec RV947).

Séries : GE EX LV NB DT JS JG RT SM RO CH ED NE ES JB PS PR EC CT IS JR LM EZ DN OS JL AM
AB JO MI NA HA SO AG ZA ML MT MC LC JN AC RM CO GA EP PH CL TH TM TT PM HE JC PI JA JU RV.
Pages : `FICHES9_<LIVRE>_<n>.html`. Catégories (`CAT.code`) : `<SÉRIE>9<n>` (ex. `GE91`).

## 5. Règles inviolables (héritées des phases 7-8)
- Le **registre est la source de vérité** : statut, teneur, accomplissement recopiés, jamais réinventés.
- Un seul système chronologique par fiche (4026 · 2370 · 1513 · 607 · 539 · 537 · 455 · 29 · 33 · 70 · 1914) ; les dates profanes divergentes sont signalées.
- **Aucune date pour l'avenir. Aucun total dogmatique.**
- Preuves : les faits, les documents, les mesures — et **leurs limites** (une thèse contestée ou rétractée est dite telle).
- Liens exclusivement jw.org / wol.jw.org ; aucun contenu protégé recopié ; aucune donnée personnelle.
- Images : JPG ≤ 10 / réponse · Audios : ≤ 10 / réponse, français uniquement.
- Ne jamais paralléliser deux écritures sur le **même fichier**.
- Médias : `preuves/images/` et `preuves/audio/` ne sont **pas versionnés** (convention du dépôt, `INVENTAIRE_DEPOT.md` § médias) ; ils restent dans l'espace de travail ; en cas de purge, la page reste valide (le lecteur affiche « piste absente »).

## 6. Journal des vagues
| Vague | Date | Série / catégorie | P couverts | Page produite |
|---|---|---|---|---|
| P9-1 | 2026-09-27 | GE91 — Origines : Éden, Déluge, Sodome ; ouverture de l'Exode | P1001–P1008 (8 fiches : GE1001–GE1006, EX1007, EX1008) | `FICHES9_GENESE_EXODE_1.html` (222 Ko, 47 sources) · 8 JPG · 8 MP3 · C4–C7 OK · 0 lien mort · 8 × PUBLIE |
| P9-2 | 2026-09-28 | EX91 — De l'Égypte aux plaines de Moab : plaies annoncées, mer Rouge, cantique, Amalek, l'ange et les frelons, Coré, Meriba/Hor/Nébo, serpent de cuivre | P629, P1009–P1016 (9 fiches complètes : EX629, EX1009–EX1013, NB1014–NB1016) + 4 renvois GE570, GE571, GE572, NB573 (→ GE001, GE003/GE013, GE029, EX053) ; GE975 (commune) reportée à la série Révélation avec P947 | `FICHES9_EXODE_NOMBRES_1.html` (260 Ko, 54 sources) · 9 JPG · 9 MP3 · C4–C7 OK · 5 liens FICHES8 vérifiés · 13 × PUBLIE |
| P9-3 | 2026-09-28 | DT91 — Du Deutéronome aux Juges : lieu du Nom (Silo → Sion), promesse à Josué et bilan, Jourdain arrêté à Adam, Jéricho au 7e jour, « Juda montera », Bokim, Gédéon, Samson, Benjamin (3e montée) | P1017–P1020, P976–P980 (9 fiches complètes : DT1017, DT1018, JS1019, JS1020, JG976–JG980) + 1 renvoi DT628 (→ DT059) | `FICHES9_DEUTERONOME_JUGES_1.html` (267 Ko, 56 sources) · 9 JPG · 9 MP3 · C4–C7 OK · lien FICHES8 vérifié · 10 × PUBLIE |
| P9-4 | 2026-09-28 | JG92 — Des Juges à Samuel : Sisera « dans la main d'une femme », les 300 et le pain d'orge, fable de Yotham, bénédiction de la porte de Bethléhem, généalogie Obed-Jessé-David, prière d'Anne (« corne de son oint »), droit du roi, trois signes de Saül | P1021–P1023, P520, P521, P1024–P1026 (8 fiches complètes : JG1021–JG1023, RT520, RT521, SM1024–SM1026) + 1 renvoi SM574 (→ RO073) ; SM1027 reporté à P9-5 | `FICHES9_JUGES_RUTH_SAMUEL_1.html` (240 Ko, 47 sources) · 8 JPG · 8 MP3 · C4–C7 OK · lien FICHES8 vérifié · 9 × PUBLIE |
| P9-5 | 2026-09-28 | RO91 — De David à Élisha : « le fils qui vient de te naître mourra », sagesse et richesse de Salomon sans égal, l'homme de Dieu de Juda et le lion, la jarre de Tsarphath, la pluie du Carmel, les trois onctions de l'Horeb et les sept mille, le malheur reporté « aux jours de son fils », l'enlèvement d'Élie et la double part, la famine de sept ans | P1027–P1035 (9 fiches complètes : SM1027, RO1028–RO1035) ; aucun renvoi dans ce périmètre | `FICHES9_SAMUEL_ROIS_1.html` (267 Ko, 55 sources) · 9 JPG · 9 MP3 · C4–C7 OK · 9 × PUBLIE |

Prochaines vagues (ordre de la file, `etat.py next`) : P9-6 Rois–Chroniques (RO1036, RO1037, CH522, CH575, CH1038 + renvois de la partie 8 s'il y en a, puis début des Psaumes P523 → …) · P9-7 → Psaumes (suite, P523 → P569 + P1039–P1048) · puis Isaïe (32), Daniel/Douze, Évangiles, Actes, Épîtres, Révélation (GE975 commune traitée avec RV947).
