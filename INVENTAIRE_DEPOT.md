# INVENTAIRE COMPLET DU DÉPÔT `frfr2026/propheties`

*Analyse réalisée le 27 septembre 2026 sur le commit `3f3d46e` (« Restauration et mise à jour complète du site »), branche de travail `arena/01a0e466-propheties`, strictement identique à `origin/main`.*

---

## 0. État de la synchronisation

| Élément | Valeur |
|---|---|
| Dépôt distant | `https://github.com/frfr2026/propheties.git` (public) |
| Commit analysé | `3f3d46e259252ab299faa42bbc9de44939c30d58` — unique commit de l'historique |
| Écart local ↔ `origin/main` | **aucun** (`git diff --stat HEAD origin/main` vide) |
| Clé API nécessaire ? | **Non** : le dépôt est public, le clonage/`fetch` fonctionne sans authentification |
| Fichiers versionnés | **297** (hors `.git`) — **~33 Mo** |
| `.gitignore` | absent |

**Répartition par type :** 131 HTML · 123 Python · 24 Markdown · 8 PNG · 6 TXT · 4 JSON · 1 CSV.

**Répartition par dossier :**

| Dossier | Fichiers | Poids | Rôle |
|---|---|---|---|
| `/` (racine) | 2 | 92 Ko | README + dossier stratégique |
| `preuves/` | 141 | 15 Mo | Documents de conception, registre, pages HTML livrées |
| `preuves/phase8/` + `data/` | 94 | 7 Mo | Phase 8 : builder + 91 fichiers de données (519 fiches) |
| `preuves/divers/` | 8 | 8,7 Mo | Prompts d'origine et exports de conversations |
| `preuves/fiches/` + `data/` | 24 | 1,2 Mo | Phase 7 : builder, thème CSS, 19 fichiers de données |
| `preuves/livres/` | 4 | 348 Ko | 3 livres A4 + générateur |
| `preuves/visuels/` + `qr/` | 13 | 348 Ko | Frises, cartes, coffret, QR + générateur |
| `preuves/videos/` | 4 | 180 Ko | Scripts, storyboards, prompts + générateur |
| `preuves/collections/` | 3 | 56 Ko | Générateur audio + durées |
| `preuves/cahier/`, `dates/`, `index/`, `site/` | 4 | 116 Ko | Un générateur par livrable |

---

## 1. Ce qu'est ce dépôt (synthèse)

Un **système de production de contenus** en français, conçu comme dossier de travail d'un « pionnier spécial » (Témoins de Jéhovah). Il comporte deux projets :

1. **Projet 1 — Les méthodes** (`00_DOSSIER_10_STRATEGIES.md`) : 10 stratégies de « prédication numérique » encadrées par les règles de l'organisation, la loi française/UE et les CGU des plateformes.
2. **Projet 2 — Les contenus** (`preuves/`) : une chaîne de production en 8 phases dont le pivot est un **registre de 1 000 prophéties bibliques** (P001 → P1000, quatre colonnes : prophétie · teneur · accomplissement · statut), à partir duquel sont générés mécaniquement un site hors-ligne, des livres, des frises, des index, des scripts vidéo, des collections audio, des fiches de dates, un cahier d'exercices, puis des **fiches descriptives détaillées** (phase 7 : 148 fiches thématiques ; phase 8 : 519 fiches, une par entrée du registre, P001 → P519).

**Architecture technique :** le principe « une seule source de vérité » — les fichiers Markdown du registre et les fichiers de données Python (`cat_*.py`, `p8_*.py`) sont la source ; chaque HTML est **régénéré** par un script `build_*.py` (Python 3 standard, sans dépendance). Tous les HTML sont **autonomes** (CSS inline, pas de ressource distante), le thème étant partagé via `fiches/theme.py`. Les liens sortants sont restreints à `jw.org` / `wol.jw.org`.

**Point d'attention :** les dossiers `preuves/images/` (≈ 700 JPG) et `preuves/audio/` (≈ 600 MP3 + 12 `.m3u`) décrits dans le README **ne sont pas versionnés** dans le dépôt. Les HTML y font 1 419 références uniques ; ouvertes depuis ce clone, les pages s'affichent mais sans illustrations ni lecteurs audio fonctionnels.

---

## 2. Racine du dépôt (2 fichiers)

| Fichier | Taille | Description |
|---|---|---|
| `README.md` | 36 Ko, 133 l. | **Carte du dépôt.** Présente les deux projets, puis un tableau « où est quoi » décrivant chaque livrable de `preuves/` (phases 1 à 7), les 5 règles transversales (un contact à la fois · on ne copie pas, on renvoie · aucun dogme · énoncer les limites · tout aboutit au dispositif officiel) et un plan de démarrage concret. Note : décrit aussi `preuves/audio/` et `preuves/images/`, absents du dépôt. |
| `00_DOSSIER_10_STRATEGIES.md` | 55 Ko, 524 l. | **Projet 1.** Dossier stratégique en 8 parties : cadre de vérité (règles de l'organisation, droit FR/UE 2024-2026 : RGPD, ePrivacy, loi 2024-420 ; 12 lignes rouges), tunnel commun en 6 étapes, les 10 stratégies détaillées (« filtre de confiance », « lien reçu », « profil sobre », « guichet local », « réponse utile », « atelier des questions », « canal du proche », « pont officiel », « IA en coulisses », « traçabilité bienveillante »), boîte à outils, 5 scripts de messages, plan 90 jours, indicateurs, 12 anti-stratégies, matrice risques/parades, sources. |

---

## 3. `preuves/` — Phases 1 à 5 : conception, banques d'idées, coffrets (16 fichiers)

| Fichier | Taille | Description |
|---|---|---|
| `00_PLAN_MAITRE.md` | 17 Ko | Plan directeur du projet « Preuves » : objectif, règle du non-dogme, chaîne des 8 maillons, 12 modules (M1-M12), matrice des formats, entonnoir de diffusion, note de déontologie (abandon du mot « irréfutable »), cadence de production, plan 90 jours. |
| `01_BANQUE_DE_PREUVES.md` | 48 Ko, 64 sections | **Cœur documentaire.** 8 familles de preuves (création, unité interne, prophéties accomplies avec 12 tableaux sourcés, prophéties en cours, préservation du texte, exactitude historique/archéologique, sagesse pratique, diffusion universelle). Pour chacune : textes bibliques, faits vérifiables, donnée récente 2024-2026, script 30 s, objections/réponses, limites honnêtes. |
| `02_FORMATS_ET_SCRIPTS.md` | 21 Ko | 12 gabarits prêts à produire : carrousel 10 vues, vidéos 3 min et 90 s (découpage plan par plan), article 900 mots rédigé, atelier 25 min, quiz, podcast, infographies, checklist finale. |
| `03_FICHE_A4.html` | 20 Ko, sans JS | Fiche imprimable recto/verso : 12 raisons vérifiables, 7 questions, 5 QR vers pages officielles. |
| `04_CARTES_QR.html` | 13 Ko, sans JS | 8 cartes à découper à remettre en main propre, QR vers jw.org uniquement. |
| `05_SERIE_30_JOURS.csv` | 8 Ko, 31 l. | Calendrier éditorial (séparateur `;`) : 30 jours = 30 preuves. Colonnes : Jour · Module · Accroche · Preuve (donnée vérifiable) · Référence biblique · Source externe · Format conseillé · Mode de sortie. |
| `06_KIT_MEDIA.md` | 5 Ko | Kit média : visuels de couverture (M1, M3, M4, M5, M8, M9 — dans `images/`, non versionné), règles d'honnêteté des images, charte graphique, captures audio/vidéo, impression, sauvegarde. |
| `07_BANQUE_IDEES.md` | 25 Ko | 100 idées de contenus en 10 familles : accroche verbatim, mise en forme, levier d'impact, mode de sortie ; liste des 10 idées à produire en premier. |
| `08_MISE_EN_FORME.md` | 13 Ko, 25 sections | « Grammaire » visuelle/narrative : contrainte des 3 secondes, 7 formules de crochet, structure en 4 temps, 12 gabarits (specs, typo, durée de fabrication), format « transférable », nomenclature, mode lot, checklist. |
| `09_IMPACT_MAXIMUM.md` | 15 Ko | Le moteur d'impact : 6 lois, courbe d'attention, règle des 3 passages (mémorisation espacée), partage privé (« dark social »), matrice 1 idée → 12 sorties, séquence des 4 cercles, test des 3 personnes, 5 indicateurs, 12 erreurs fatales, éthique. |
| `10_CATALOGUE.html` | 72 Ko, 3 `<script>` | **Catalogue interactif** des 100 idées : recherche, filtres (famille, format), tri par score d'impact /27, aperçus de mise en forme (carrousel, reel, fiche, carte), moteur d'impact en 3 règles, section « Phase 4 » (10 idées sur la précision des prophéties). |
| `11_PROPHETIES_IDEES.md` | 34 Ko | Dossier « spectaculaire » : 25 détails prophétiques datés et sourcés, 72 idées en 8 familles, score « d'imposité » /25, méthode des trois témoins, répertoire d'objections, garde-fous propres aux prophéties. |
| `12_MISE_EN_OEUVRE_IMPACT.md` | 16 Ko | Mode d'emploi opérationnel des prophéties : loi du détail unique, structure en 3 temps, 9 crochets, 12 gabarits spécialisés, atelier en 5 séquences, 7 leviers, campagne « Une prophétie, un détail » sur 30 jours, 12 erreurs, grille de vérification en 10 points. |
| `13_COFFRET_PROPHETIE.html` | 55 Ko, 1 `<script>` | **Coffret interactif n° 1** : frise cliquable des accomplissements, 5 dossiers dépliables avec sources et limites, les trois témoins, 6 objections/réponses, 9 crochets, grille de contrôle cochable. |
| `14_PROPHETIES_VAGUE_2.md` | 46 Ko, 46 sections | **Vague des archives** : 20 nouveaux cas vérifiés (B01-B20 : reçu de Nebo-Sarsekim, ostraca de Lakish, prisme de Sennachérib, Daniel 11/Raphia, Askalon 604, Thèbes 663, Édom, Éz 12:13…), 75 idées en 9 familles, 12 formes imprimables, atelier « archive », campagne « feuilleton des archives » sur 6 semaines, 12 leviers, 10 objections. |
| `15_COFFRET_PROPHETIE_2.html` | 49 Ko, 1 `<script>` | **Coffret interactif n° 2** : enquête du reçu en 6 étapes, 8 questions-preuves, mur des pièces à conviction, échelle du silence, témoin hostile, 12 leviers, objections + points ouverts, générateur de carte (courte / complète / question seule). |

---

## 4. `preuves/` — Le REGISTRE GÉNÉRAL (8 fichiers, 1 120 entrées vérifiées + 97 propositions en attente)

Source de vérité de toutes les phases suivantes. Chaque ligne : `| Pnnn | Référence | Teneur | Accomplissement | Statut |`. Aucun commentaire. Compte vérifié par script : **exactement 1 000 lignes P, sans trou**.

| Fichier | Taille | Entrées | Parties | Description |
|---|---|---|---|---|
| `16_REGISTRE_PROPHETIES.md` | 43 Ko | P001-P180 (180) | 1-3 | Les 6 règles du registre, plan en 14 parties, puis **Pentateuque** (65), **livres historiques** (41), **Isaïe** (74). |
| `17_REGISTRE_PROPHETIES_2.md` | 54 Ko | P181-P407 (227) | 4-5 | **Jérémie** (116) et **Lamentations** (4) ; **Ézéchiel** (67) et **Daniel** (40) — 70 ans, 539, Hophra, Tyr, ossements, Gog, statue, 2 300 jours, 70 semaines, Daniel 11 verset par verset. |
| `18_REGISTRE_PROPHETIES_3.md` | 40 Ko | P408-P569 (162) | 6-7 | **Les Douze** (112 : Osée → Malachie) et **Psaumes et Écrits** (50 : psaumes messianiques, Job, Proverbes, Ecclésiaste, Cantique). |
| `19_REGISTRE_PROPHETIES_4.md` | 36 Ko | P570-P711 (142) | 8-9 | **Tableau consolidé des prophéties messianiques** (77) et **prophéties énoncées par Jésus** (65 : signe composite, Jérusalem 66-70, moisson, sur lui-même et ses disciples). |
| `20_REGISTRE_PROPHETIES_5.md` | 53 Ko | P712-P920 (209) | 10-12 | **Actes et les apôtres** (80), **Révélation 1** (65 : congrégations, trône, cavaliers, 144 000, trompettes, deux témoins), **Révélation 2** (64 : femme et dragon, bêtes, 666, bols, Babylone la Grande, noces). |
| `21_REGISTRE_PROPHETIES_6.md` | 20 Ko | P921-P975 (55) | 13-14 | **Révélation 3** (Har-Maguédôn, abîme, millénium, épreuve finale, grand trône blanc, Nouvelle Jérusalem) + **tableau récapitulatif final** : index des parties, totaux par corpus, index des statuts, repères chronologiques, 13 garde-fous, sources. |
| `23_REGISTRE_PROPHETIES_7.md` | 6 Ko | P976-P1000 (25) | 14 (compléments) | Compléments : Juges, Marc, Colossiens, Jean + **couverture canonique** (62 livres sur 66 ont une entrée ; Esther, Philémon, 2 Jean, 3 Jean n'en ont aucune). |
| `24_REGISTRE_PROPHETIES_8.md` | 24 Ko | P1001-P1120 (120) | 15 | **Compléments de l'audit, priorité A intégrée** (27/09/2026) : 127 propositions A dont 9 fusionnées (voir `phase9/tools/build_partie15.py`), au format du registre (5 colonnes), sections par livre (Genèse 6, Exode 7, Nombres 3, Deutéronome 2, Josué 2, Juges 3, Samuel 4, Rois 10, Chroniques 1, Psaumes 10, Isaïe 32, Daniel 1, Douze 4, Évangiles 26, Actes 4, Épîtres 5). Prochain numéro libre : P1121. |
| `25_PROPOSITIONS_B_C_EN_ATTENTE.md` | 20 Ko | 97 propositions (82 B + 17 C, moins fusions) | hors registre | Propositions B/C de l'audit **non intégrées**, conservées avec leur justification pour décision ultérieure ; pas de numéro P attribué. |

---

## 5. `preuves/` — Phase 6 : productions dérivées du registre (vagues 1 à 8)

Chaque livrable HTML est produit par un générateur Python dédié qui relit le registre.

### 5.1 Vague 1 — Le Grand Dossier

| Fichier | Taille | Description |
|---|---|---|
| `22_GRAND_DOSSIER.md` | 28 Ko | **Les 12 grandes preuves**, chacune en 8 volets (accroche 3 s · fait vérifiable · prophétie + renvoi registre · accomplissement · sources datées et limites · question qui ouvre · formats · référence officielle) : Cyrus, Babylone 539, Tyr, Ninive, 70 ans, 70 semaines, Daniel 11/Raphia, « sept temps » 607 → 1914, signe composite, Jérusalem 66-70/Pella, Ésaïe 53, en cours/à venir. Mode d'emploi : 5 règles, 8 objections, index croisé, nomenclature. |

### 5.2 Vague 2 — Le site hors-ligne

| Fichier | Taille | Description |
|---|---|---|
| `SITE_LOCAL.html` | 348 Ko, 2 `<script>` | **« REPÈRES » — bibliothèque privée autonome** (un seul fichier, aucune connexion). 7 onglets : Accueil (chiffres, statuts) · Les 1 000 entrées (recherche instantanée + 4 filtres : famille de statut, partie, statut exact, section) · Les 14 parties · Les 12 preuves · Médias (galerie images + lecteurs audio, référencés localement) · Liens officiels · Règles d'usage. |
| `site/build_site.py` | 30 Ko, 459 l. | **Générateur du site** : parse les 7 fichiers du registre (regex sur les lignes `| Pnnn |`), sérialise les 1 000 entrées en JSON embarqué, injecte le thème partagé (`fiches/theme.py`) + CSS spécifique, lit `collections/durations.json` pour les durées audio, écrit `SITE_LOCAL.html`. |

### 5.3 Vague 3 — Les trois livres A4

| Fichier | Taille | Description |
|---|---|---|
| `livres/LIVRE_1_ENQUETE.html` | 40 Ko | **« L'Enquête — les 12 grandes preuves »** : livre A4 imprimable, couverture, sommaire, 12 fiches d'une page en 8 volets, annexes (5 règles, 8 objections, index croisé, nomenclature). |
| `livres/LIVRE_2_LES_1000.html` | 243 Ko | **« Les 1 000 — le registre mis en pages »** : couverture, sommaire des 14 parties, méthode, les 1 000 entrées par partie et section, index alphabétique des sections. (Le `<title>` porte encore « Les 975 ».) |
| `livres/LIVRE_3_DETAIL.html` | 29 Ko | **« Le détail qui change tout — 25 détails datés »** : une fiche par page (datation · référence · prophétie · fait vérifiable · ce que cela ne prouve pas), de Cyrus à la datation 4Q114 (2025). |
| `livres/build_livres.py` | 32 Ko, 426 l. | Générateur des trois livres : relit le registre (16-21, 23) et `22_GRAND_DOSSIER.md`, reconstruit les 3 HTML (polices système, aucun script). |

### 5.4 Vague 4 — Les visuels

| Fichier | Taille | Description |
|---|---|---|
| `visuels/FRISES_CHRONOLOGIQUES.html` | 188 Ko | **12 frises chronologiques** : 12 planches graphiques (ligne de temps, repères alternés) + 12 planches de détails tirées du registre + annexe « couverture canonique » des 66 livres. 258 repères datés renvoyés à une entrée numérotée. |
| `visuels/DECOUVRIR_PAS_A_PAS.html` | 22 Ko | **24 cartes à 3 volets** (contexte · repère · référence · vérifiable · détail · limite · question · lien officiel), 4 par page, à découper. |
| `visuels/COFFRET.html` | 21 Ko | **Le coffret physique** : page de garde (chiffres + 8 QR), 9 étiquettes de dos de classeur, couverture de disque (10 pistes), 24 étiquettes de pochette, colophon. |
| `visuels/CARTES_QR.html` | 15 Ko | **8 cartes de visite** avec QR (accueil · bibliothèque en ligne · Bible et Histoire · Bible et science · cours biblique · demandez une visite · Bible d'étude · questions bibliques). Domaine unique : jw.org / wol.jw.org. |
| `visuels/build_visuels.py` | 61 Ko, 749 l. | Générateur de la vague 4 : relit le registre, construit les 4 HTML, **génère les QR codes en local** (encodeur QR implémenté en pur Python, sortie PNG), compte les médias présents. |
| `visuels/qr/accueil_officiel.png` | 564 o | QR code PNG 330×330 → page d'accueil jw.org. |
| `visuels/qr/biblioth_que_en_ligne.png` | 704 o | QR code PNG 370×370 → wol.jw.org (bibliothèque en ligne). |
| `visuels/qr/la_bible_et_l_histoire.png` | 840 o | QR code PNG 410×410 → rubrique « La Bible et l'Histoire ». |
| `visuels/qr/la_bible_et_la_science.png` | 830 o | QR code PNG 410×410 → rubrique « La Bible et la science ». |
| `visuels/qr/cours_biblique.png` | 957 o | QR code PNG 450×450 → demande de cours biblique. |
| `visuels/qr/demandez_une_visite.png` | 846 o | QR code PNG 410×410 → formulaire « Demandez une visite ». |
| `visuels/qr/bible_d_tude.png` | 840 o | QR code PNG 410×410 → Bible d'étude en ligne. |
| `visuels/qr/questions_bibliques.png` | 811 o | QR code PNG 410×410 → rubrique « Questions bibliques ». |

### 5.5 Vague 5 — Index général et préparation vidéo

| Fichier | Taille | Description |
|---|---|---|
| `INDEX_GENERAL.html` | 83 Ko, sans JS | **7 index mécaniques** sur les 1 000 entrées : par livre (66), par statut exact (40 formulations), par partie, repérages par mot-clé (personnes, lieux, mesures de temps, mentions du futur), index continu P001 → P1000. |
| `index/build_index.py` | 14 Ko, 222 l. | Générateur de l'index : parse le registre, construit les 7 index sans commentaire, écrit `INDEX_GENERAL.html`. |
| `videos/SCRIPTS_VIDEOS.html` | 43 Ko | **Scripts de tournage** : fiche technique (9:16, 1080×1920, 30 i/s, accroche < 3 s, zones sûres, sous-titres), 10 vidéos courtes (30-40 s) + 3 longues (2-3 min), plans détaillés (temps, cadrage, action, texte écran, voix off, son, limite honnête), feuille de tournage. |
| `videos/STORYBOARDS.html` | 51 Ko | **Storyboards** : planches A4, vignettes 9:16 avec lignes de tiers, numéro de plan, durée, cadrage, action, texte, voix off. |
| `videos/LISTE_PLANS_A_GENERER.md` | 46 Ko | **Prompts d'images** : un prompt prêt à l'emploi par plan (61 prompts, convention `plans/vNN_pNN.jpg`), suffixe commun imposant : sans texte, sans logo, sans visage identifiable, 9:16. |
| `videos/build_videos.py` | 35 Ko, 341 l. | Générateur de la vague 5 : une seule structure de données → scripts, storyboards et liste de prompts. |

### 5.6 Vague 6 — Collections audio

| Fichier | Taille | Description |
|---|---|---|
| `COLLECTIONS_AUDIO.html` | 61 Ko, sans JS | **12 collections audio thématiques** (classeur sonore) : ordre d'écoute, titre de piste, nom de fichier, durée réelle, support à ouvrir, phrase à retenir, 2 liens officiels. |
| `PLANS_ECOUTE.html` | 48 Ko, sans JS | **4 parcours d'écoute** (une soirée · 2 semaines · 4 semaines · 12 semaines), 12 fiches d'écoute à cocher, carte de prêt, 6 règles de transmission, 8 liens officiels. |
| `collections/build_collections.py` | 45 Ko, 818 l. | Générateur de la vague 6 : lit `audio/*.mp3` (absent du dépôt) et `durations.json`, produit les 2 HTML et 12 playlists `.m3u` (non versionnées). |
| `collections/durations.py` | 2 Ko, 49 l. | **Calculateur de durée MP3 sans dépendance** : saute le tag ID3, parcourt les trames MPEG-1/2/2.5 Layer III (tables de bitrate/sample rate), somme les durées, écrit `durations.json`. |
| `collections/durations.json` | 732 o | Cache des durées (26 entrées, en secondes) — actuellement des pistes de phase 8 (`fiche_DN373…`, `fiche_ML512…`). |

### 5.7 Vague 7 — Fiches de dates

| Fichier | Taille | Description |
|---|---|---|
| `FICHES_DATES.html` | 40 Ko, sans JS | **8 fiches A4 détachables** — 607 · 539 · 537 · 455 · 29 · 33 · 36 · 1914 : prophétie et référence, **calcul écrit ligne par ligne**, accomplissement, document profane (VAT 4956, Josèphe, tablette Strassmaier, cylindre de Cyrus, 15ᵉ année de Tibère), 27 liens wol.jw.org, « ce que cette fiche ne dit pas ». + page « chaîne complète » et mode d'emploi. |
| `dates/build_dates.py` | 33 Ko, 538 l. | Générateur de la vague 7 : données des 8 fiches en dur, une seule source de vérité pour fiches, chaîne et mode d'emploi. |

### 5.8 Vague 8 — Cahier de l'auditeur

| Fichier | Taille | Description |
|---|---|---|
| `CAHIER_AUDITEUR.html` | 51 Ko, sans JS | **Cahier d'exercices** (7 pages A4 + garde) : A. 8 fiches de dates à trous (42 blancs, corrigé détachable) · B. 13 fiches d'écoute reliées · C. 8 cartes d'objection recto/verso au format poche 85×55 mm. Page « sources et rappels ». |
| `cahier/build_cahier.py` | 31 Ko, 532 l. | Générateur de la vague 8 : fiches à trous, fiches d'écoute, cartes et corrigé depuis une structure unique. |

---

## 6. `preuves/` — Phase 7 : fiches descriptives thématiques (19 HTML + 24 fichiers outillage)

Passage de « l'inventaire sans commentaire » (registre) à « tout expliquer » : chaque fiche = **10 blocs obligatoires** (identification · texte · contexte · explication · interprétation sourcée · accomplissement daté · preuves historiques · géographiques · scientifiques/archéologiques · « ce que cette fiche ne dit pas ») + chronologie SVG inline + ≥ 2 sources officielles. Le builder **refuse d'écrire** si un contrôle échoue (C4 lien hors domaine, C5 limites vides, C6 bloc vide, C7 < 2 sources). **148 fiches** au total (A013, B009, C014, D012, E009, F010, G009, H010, I010, J012, K008, L010, R006, S006, T012 — d'après le workflow).

### 6.1 Outillage phase 7

| Fichier | Taille | Description |
|---|---|---|
| `fiches/00_WORKFLOW.md` | 15 Ko | **Pilotage de la phase 7** : ce que change la phase, tableau des 15 catégories (A → T) avec état, machine à états S0 → S7, 5 règles de transition, grille des 12 contrôles C1-C12, journal des vagues. |
| `fiches/build_fiches.py` | 16 Ko, 352 l. | **Générateur v2** : importe `fiches/data/cat_<x>.py`, applique la grille de validation, produit `FICHES_<CODE>_<NOM>.html` (page de garde, sommaire en cartes, navigation fixe, illustration + lecteur audio par fiche, mise en page écran + impression A4). |
| `fiches/theme.py` | 15 Ko, 364 l. | **Design system partagé** : `THEME_CSS` (palette bleu/blanc/or, cartes, grille auto-fill, clamp(), impression), helpers d'appariement fiche → image/audio, durées, couvertures. Importé par tous les builders (site, fiches, phase 8). |
| `fiches/durations.json` | 2 Ko | Durées (s) des 80 audios de la phase 7 (`fiche_A00_intro_categorie`, `fiche_A01_tyr`, …). |
| `fiches/data/__init__.py` | 0 o | Marqueur de package Python. |

### 6.2 Pages et données de la phase 7 (19 paires)

| # | Page HTML | Données source | Fiches | Nb | Catégorie / contenu |
|---|---|---|---|---|---|
| 1 | `FICHES_A_NATIONS.html` (111 Ko) | `fiches/data/cat_a.py` | F001 → F009 | 9 | **Prophéties contre les nations** — Tyr · Sidon · Babylone · L'Égypte · Édom · Moab · Ammon · La Philistie · Ninive et l'Assyrie |
| 2 | `FICHES_B_JERUSALEM.html` (107 Ko) | `fiches/data/cat_b.py` | B001 → B009 | 9 | **Prophéties sur Jérusalem et Juda** — Silo · Les soixante-dix ans · La fuite en Égypte · Cyrus nommé d'avance · La gloire du second temple · Jérusalem rebâtie · La palissade de pieux · « Pas pierre sur pierre » · Jérusalem foulée aux pieds |
| 3 | `FICHES_C_MESSIE_1.html` (116 Ko) | `fiches/data/cat_c1.py` | A010 → C005 | 9 | **Fin des nations · Le Messie : origine et naissance (1re partie)** — Damas · Kédar et Hatsor · Élam · L'Assyrie · Bethléhem Éphratha · La vierge · D'Égypte j'ai appelé mon fils · Rachel pleure ses fils · Le messager devant lui |
| 4 | `FICHES_C_MESSIE_2.html` (114 Ko) | `fiches/data/cat_c2.py` | C006 → C014 | 9 | **Le Messie : le ministère (2e partie)** — L'entrée triomphale · Ésaïe 61 à Nazareth · La Galilée des nations · Le prophète comme Moïse · Les miracles · Les paraboles · Le Serviteur doux · Il a porté nos maladies · Le Nazaréen |
| 5 | `FICHES_D_PASSION_1.html` (116 Ko) | `fiches/data/cat_d1.py` | D001 → D009 | 9 | **Le Messie : procès, mort, résurrection (1re partie)** — Les trente pièces · Le Psaume 22 · Ésaïe 53 · L'agneau intact · La trahison de l'ami · Le silence et les sévices · La pierre rejetée · La résurrection · À la droite de Dieu |
| 6 | `FICHES_E_EMPIRES_1.html` (121 Ko) | `fiches/data/cat_e1.py` | D010 → E006 | 9 | **Fin du Messie souffrant · Les empires (1re partie)** — Le vinaigre · Le berger frappé · Le serpent d'airain · La statue du songe · Les quatre bêtes · Le bélier et le bouc · Les rois du nord et du sud · La nuit de Belschatsar · Darius le Mède |
| 7 | `FICHES_F_CHRONO_1.html` (121 Ko) | `fiches/data/cat_f1.py` | E007 → F015 | 9 | **Les empires (2e partie) · Les chronologies** — Les deux rois au temps de la fin · Daniel 12 · Les sept puissances · L'arbre abattu · Les soixante-dix semaines · Les 430 ans · Un jour pour un an · Les 480 ans · L'an 15 de Tibère |
| 8 | `FICHES_G_RESTAURATION_1.html` (121 Ko) | `fiches/data/cat_g1.py` | F016 → G005 | 9 | **Les chronologies (2e partie) · Restauration et monde nouveau** — Trois ans et demi, sept fois · Les mille ans · Les fêtes-rendez-vous · Trois jours et trois nuits · La vallée des ossements · L'alliance nouvelle · Le paradis d'Ésaïe · Ils se réveilleront · Toutes choses nouvelles |
| 9 | `FICHES_H_SIGNE_1.html` (122 Ko) | `fiches/data/cat_h1.py` | G006 → H005 | 9 | **Restauration et monde nouveau (2e partie) · Le signe et les derniers jours** — Les 144 000 · La grande foule · Le fleuve et les feuilles · Jéhovah devient Roi · Le cadre des Oliviers · Nation contre nation · Famines, pestes, séismes · Prêchée à toutes les nations · Les traits des derniers jours |
| 10 | `FICHES_I_REVELATION_1.html` (127 Ko) | `fiches/data/cat_i1.py` | H006 → I004 | 9 | **Le signe et les derniers jours (2e partie) · Le livre de la Révélation** — La grande tribulation · « Paix et sécurité ! » · Signes dans le ciel · Faux Christs et vraie venue · Haïs et endurants · La méthode de Révélation · Les sept sceaux · Les sept trompettes · La femme contre le dragon |
| 11 | `FICHES_J_NOMMES_1.html` (127 Ko) | `fiches/data/cat_j1.py` | I005 → J003 | 9 | **Le livre de la Révélation (2e partie) · Personnages et lieux nommés d'avance** — La bête de la mer · La bête de la terre et 666 · Babylone la Grande · La moisson et la vendange · Les bols et Harmaguédon · Le Roi guerrier · Cyrus nommé · Josias nommé · Bethléhem Éphrata |
| 12 | `FICHES_J_NOMMES_2.html` (115 Ko) | `fiches/data/cat_j2.py` | J004 → J011 | 8 | **Personnages et lieux nommés d'avance (2e partie)** — Isaac nommé · Shilo · L'étoile de Jacob · Balaam contraint · La maison de David · La maison d'Éli jugée · Samson annoncé · Houlda à Josias |
| 13 | `FICHES_K_SCIENCE_1.html` (101 Ko) | `fiches/data/cat_k1.py` | J012 → K006 | 7 | **Fin des nommés d'avance · La Bible et la science (1re partie)** — Gog de Magog · Innombrables · L'alliance du jour et de la nuit · Remplissez la terre · Psaume 8 · Le ciel sous parole · Le cadran d'Achaz |
| 14 | `FICHES_L_GEO_1.html` (129 Ko) | `fiches/data/cat_l1.py` | K007 → L007 | 9 | **La Bible et la science (2e partie) · Prophéties géographiques** — Pierre et le jour · Les sabbats de la terre · Samarie · Ninive · Édom · Moab · Tyr · La Philistie · Ammon |
| 15 | `FICHES_L_GEO_2.html` (59 Ko) | `fiches/data/cat_l2.py` | L008 → L010 | 3 | **Prophéties géographiques (2e partie)** — La Syrie · L'Égypte · Babylone |
| 16 | `FICHES_R_RELIQUATS.html` (100 Ko) | `fiches/data/cat_r1.py` | R001 → R006 | 6 | **Reliquats et compléments** — Joseph · Les clauses de l'alliance · Les promesses · Les sept lettres · Le trône et l'Agneau · L'aller et le retour |
| 17 | `FICHES_S_PSAUMES.html` (107 Ko) | `fiches/data/cat_s1.py` | S001 → S006 | 6 | **Les Psaumes messianiques** — Psaume 2 · Portes levées, sceptre de justice, pluie sur le regain · Psaume 110 · Trahi, haï, percé · Offert, gardé, délivré · L'alliance chantée |
| 18 | `FICHES_T_JEREMIE_1.html` (110 Ko) | `fiches/data/cat_t1.py` | T001 → T006 | 6 | **Jérémie, 1re partie — le jugement** — Le malheur vient du nord · Le Temple ne sauvera pas · Quatre rois jugés · Tsidqiya et la chute · Faux prophètes contre Jérémie · Signes en actes |
| 19 | `FICHES_T_JEREMIE_2.html` (121 Ko) | `fiches/data/cat_t2.py` | T007 → T012 | 6 | **Jérémie, 2e partie — restauration** — L'abandon et ses fruits amers · La lettre aux exilés · Consolation · Nouvelle alliance et germe juste · Le reste en Égypte · Babylone jugée |

---

## 7. `preuves/` — Phase 8 : une fiche par prophétie du registre (91 HTML + 94 fichiers outillage)

Objectif : une **fiche complète pour chacune des 1 000 entrées**, en suivant l'ordre du registre. Gabarit en **11 blocs** (les 10 de la phase 7 + « Schéma · l'essentiel en bref »). État actuel : **519 fiches publiées (P001 → P519)**, soit Genèse → Malachie ; les 91 pages couvrent Pentateuque, Samuel/Rois/Chroniques/Esdras/Néhémie, Isaïe, Jérémie, Lamentations, Ézéchiel, Daniel et les Douze.

### 7.1 Outillage phase 8

| Fichier | Taille | Description |
|---|---|---|
| `phase8/00_WORKFLOW_PHASE8.md` | 13 Ko | **Workflow phase 8** : objectif, cycle d'une vague S1-S7 (plan, recherche, rédaction, build, images ≤ 10, audios ≤ 10, contrôles), gabarit 11 blocs, règles inviolables, conventions de nommage (`GE001`, `prophe_GE001_eden.jpg`, `fiche_GE01_eden.mp3`), **journal des 91 vagues** P8-1 → P8-91 (25-26 sept. 2026). |
| `phase8/ETATS_PHASE8.md` | 199 Ko, 1 438 l. | **Machine à états par fiche** (A_PLANIFIER → RECHERCHE → REDACTION → CONTROLE → MEDIAS → PUBLIE), compteurs globaux (505/1000 au dernier pointage), rapport QC des paires de versets, puis un tableau par vague listant chaque fiche (code, P, sujet, état). |
| `phase8/build_p8.py` | 2 Ko, 45 l. | **Wrapper de build** : réutilise `fiches/build_fiches.py` en injectant le 11ᵉ bloc « schéma » et en renumérotant « limites ». Usage : `python3 build_p8.py p8_gen1 FICHES8_GENESE_1.html`. |

### 7.2 Pages et données de la phase 8 (91 paires, dans l'ordre du registre)

Chaque fichier `p8_*.py` contient `CAT` (code, nom, intro, vague) et `FICHES` (liste de dictionnaires : `n`, `titre`, `ref`, `statut`, `syst`, `reg`, `texte`, `contexte`, `explication`, `interpretation`, `accomplissement`, `hist`, `geo`, `sci`, `schema`, `limites`, `chrono`, `sources`).

| # | Page HTML | Données source | Fiches (registre) | Nb | Contenu |
|---|---|---|---|---|---|
| 1 | `FICHES8_GENESE_1.html` (88 Ko) | `phase8/data/p8_gen1.py` | GE001 → GE006 (P001–P006) | 6 | Genèse (1) — les commencements de la promesse |
| 2 | `FICHES8_GENESE_2.html` (86 Ko) | `phase8/data/p8_gen2.py` | GE007 → GE012 (P007–P012) | 6 | Genèse (2) — l'héritier et les nations |
| 3 | `FICHES8_GENESE_3.html` (91 Ko) | `phase8/data/p8_gen3.py` | GE013 → GE018 (P013–P018) | 6 | Genèse (3) — le serment et les jumeaux |
| 4 | `FICHES8_GENESE_4.html` (98 Ko) | `phase8/data/p8_gen4.py` | GE019 → GE024 (P019–P024) | 6 | Genèse (4) — Béthel et Joseph |
| 5 | `FICHES8_GENESE_5.html` (99 Ko) | `phase8/data/p8_gen5.py` | GE025 → GE030 (P025–P030) | 6 | Genèse (5) — le visa et le lit de mort |
| 6 | `FICHES8_GENESE_6.html` (99 Ko) | `phase8/data/p8_gen6.py` | GE031 → GE036 (P031–P036) | 6 | Genèse (6) — les six derniers fils |
| 7 | `FICHES8_GENESE_7.html` (100 Ko) | `phase8/data/p8_gen7.py` | GE037 → GE042 (P037–P042) | 6 | Genèse (7) — Benjamin, les ossements et la sortie |
| 8 | `FICHES8_EXODE_1.html` (102 Ko) | `phase8/data/p8_exo1.py` | EX043 → EX048 (P043–P048) | 6 | Exode (1) — le mémorial et le Royaume |
| 9 | `FICHES8_EXODE_2.html` (97 Ko) | `phase8/data/p8_exo2.py` | EX049 → EX054 (P049–P054) | 6 | Exode (2) — sabbats, désert et étoile |
| 10 | `FICHES8_DEUTERONOME_1.html` (100 Ko) | `phase8/data/p8_deu1.py` | DT055 → DT060 (P055–P060) | 6 | Deutéronome (1) — épines, roi et Prophète |
| 11 | `FICHES8_DEUTERONOME_2.html` (106 Ko) | `phase8/data/p8_deu2.py` | DT061 → DT066 (P061–P066) | 6 | Deutéronome (2) — cantique, tribus et Jéricho |
| 12 | `FICHES8_SAMUEL_1.html` (115 Ko) | `phase8/data/p8_sam1.py` | SM067 → SM072 (P067–P072) | 6 | Samuel (1) — d'Éli à Saül |
| 13 | `FICHES8_ROIS_1.html` (125 Ko) | `phase8/data/p8_roi1.py` | RO073 → RO078 (P073–P078) | 6 | Rois (1) — de David à Jéroboam |
| 14 | `FICHES8_ROIS_2.html` (137 Ko) | `phase8/data/p8_roi2.py` | RO079 → RO084 (P079–P084) | 6 | Rois (2) — Élie et Achab |
| 15 | `FICHES8_ROIS_3.html` (135 Ko) | `phase8/data/p8_roi3.py` | RO085 → RO090 (P085–P090) | 6 | Rois (3) — Élisée |
| 16 | `FICHES8_ROIS_4.html` (114 Ko) | `phase8/data/p8_roi4.py` | RO091 → RO096 (P091–P096) | 6 | Rois (4) — Jéhu à Ézéchias |
| 17 | `FICHES8_ROIS_5_CHRONIQUES_1.html` (114 Ko) | `phase8/data/p8_ro5ch1.py` | RO097 → CH102 (P097–P102) | 6 | Rois (5) + Chroniques (1) — la chute annoncée, les batailles de Jéhovah |
| 18 | `FICHES8_CH_ED_NE_IS.html` (110 Ko) | `phase8/data/p8_ch2edneis.py` | CH103 → IS108 (P103–P108) | 6 | Chroniques (2) + Esdras (1) + Néhémie (1) + Isaïe (1) — retours et restes |
| 19 | `FICHES8_ISAIE_2.html` (109 Ko) | `phase8/data/p8_is2.py` | IS109 → IS114 (P109–P114) | 6 | Isaïe (2) — le sifflement, la souche et l'Emmanuel |
| 20 | `FICHES8_ISAIE_3.html` (93 Ko) | `phase8/data/p8_is3.py` | IS115 → IS120 (P115–P120) | 6 | Isaïe (3) — le pille-vite, le cou épargné et le Prince de paix |
| 21 | `FICHES8_ISAIE_4.html` (89 Ko) | `phase8/data/p8_is4.py` | IS121 → IS126 (P121–P126) | 6 | Isaïe (4) — le bâton brisé, le rameau et Babylone jamais habitée |
| 22 | `FICHES8_ISAIE_5.html` (91 Ko) | `phase8/data/p8_is5.py` | IS127 → IS132 (P127–P132) | 6 | Isaïe (5) — le rétablissement, l'astre tombé et les nations jugées |
| 23 | `FICHES8_ISAIE_6.html` (89 Ko) | `phase8/data/p8_is6.py` | IS133 → IS138 (P133–P138) | 6 | Isaïe (6) — l'autel en Égypte, la chute et le clou |
| 24 | `FICHES8_ISAIE_7.html` (95 Ko) | `phase8/data/p8_is7.py` | IS139 → IS144 (P139–P144) | 6 | Isaïe (7) — Tyr, le jugement mondial et la mort engloutie |
| 25 | `FICHES8_ISAIE_8.html` (89 Ko) | `phase8/data/p8_is8.py` | IS145 → IS150 (P145–P150) | 6 | Isaïe (8) — La pierre d'angle, Ariel et le roi guérisseur |
| 26 | `FICHES8_ISAIE_9.html` (90 Ko) | `phase8/data/p8_is9.py` | IS151 → IS156 (P151–P156) | 6 | Isaïe (9) — Édom, le désert fleuri et la voix |
| 27 | `FICHES8_ISAIE_10.html` (89 Ko) | `phase8/data/p8_is10.py` | IS157 → IS162 (P157–P162) | 6 | Isaïe (10) — Cyrus, le serviteur et la chute des idoles |
| 28 | `FICHES8_ISAIE_11.html` (91 Ko) | `phase8/data/p8_is11.py` | IS163 → IS168 (P163–P168) | 6 | Isaïe (11) — L'oiseau de proie, Babylone veuve et le serviteur frappé |
| 29 | `FICHES8_ISAIE_12.html` (83 Ko) | `phase8/data/p8_is12.py` | IS169 → IS174 (P169–P174) | 6 | Isaïe (12) — Les beaux pieds, le serviteur transpercé et la maison de prière |
| 30 | `FICHES8_ISAIE_13.html` (82 Ko) | `phase8/data/p8_is13.py` | IS175 → IS180 (P175–P180) | 6 | Isaïe (13) — Le Rédempteur, la gloire, l'oint et les nouveaux cieux |
| 31 | `FICHES8_JEREMIE_1.html` (80 Ko) | `phase8/data/p8_jr1.py` | JR181 → JR186 (P181–P186) | 6 | Jérémie (1) — La marmite du nord et la ville fortifiée |
| 32 | `FICHES8_JEREMIE_2.html` (79 Ko) | `phase8/data/p8_jr2.py` | JR187 → JR192 (P187–P192) | 6 | Jérémie (2) — Signaux de feu, Silo et Topheth |
| 33 | `FICHES8_JEREMIE_3.html` (80 Ko) | `phase8/data/p8_jr3.py` | JR193 → JR198 (P193–P198) | 6 | Jérémie (3) — Absinthe, voisins jugés et cruches brisées |
| 34 | `FICHES8_JEREMIE_4.html` (70 Ko) | `phase8/data/p8_jr4.py` | JR199 → JR204 (P199–P204) | 6 | Jérémie (4) — Couronnes tombées et intercesseurs refusés |
| 35 | `FICHES8_JEREMIE_5.html` (72 Ko) | `phase8/data/p8_jr5.py` | JR205 → JR210 (P205–P210) | 6 | Jérémie (5) — Pêcheurs, potier et cruche brisée |
| 36 | `FICHES8_JEREMIE_6.html` (73 Ko) | `phase8/data/p8_jr6.py` | JR211 → JR216 (P211–P216) | 6 | Jérémie (6) — La vie pour butin et les rois jugés |
| 37 | `FICHES8_JEREMIE_7.html` (75 Ko) | `phase8/data/p8_jr7.py` | JR217 → JR222 (P217–P222) | 6 | Jérémie (7) — Konia rejeté, germe promis, Babylone jugée |
| 38 | `FICHES8_JEREMIE_8.html` (77 Ko) | `phase8/data/p8_jr8.py` | JR223 → JR228 (P223–P228) | 6 | Jérémie (8) — La coupe des nations et le joug |
| 39 | `FICHES8_JEREMIE_9.html` (81 Ko) | `phase8/data/p8_jr9.py` | JR229 → JR234 (P229–P234) | 6 | Jérémie (9) — Hanania jugé et lettre aux exilés |
| 40 | `FICHES8_JEREMIE_10.html` (77 Ko) | `phase8/data/p8_jr10.py` | JR235 → JR240 (P235–P240) | 6 | Jérémie (10) — Le livre de la consolation : plaie guérie et retour promis |
| 41 | `FICHES8_JEREMIE_11.html` (75 Ko) | `phase8/data/p8_jr11.py` | JR241 → JR246 (P241–P246) | 6 | Jérémie (11) — L'alliance nouvelle et la ville rebâtie |
| 42 | `FICHES8_JEREMIE_12.html` (80 Ko) | `phase8/data/p8_jr12.py` | JR247 → JR252 (P247–P252) | 6 | Jérémie (12) — Le champ d'Anatoth et le germe juste |
| 43 | `FICHES8_JEREMIE_13.html` (84 Ko) | `phase8/data/p8_jr13.py` | JR253 → JR258 (P253–P258) | 6 | Jérémie (13) — Dynastie garantie, liberté trahie, Parole indestructible |
| 44 | `FICHES8_JEREMIE_14.html` (79 Ko) | `phase8/data/p8_jr14.py` | JR259 → JR264 (P259–P264) | 6 | Jérémie (14) — Le siège : faux espoirs, vraie issue |
| 45 | `FICHES8_JEREMIE_15.html` (88 Ko) | `phase8/data/p8_jr15.py` | JR265 → JR270 (P265–P270) | 6 | Jérémie (15) — Fuite en Égypte : le refuge qui tue |
| 46 | `FICHES8_JEREMIE_16.html` (89 Ko) | `phase8/data/p8_jr16.py` | JR271 → JR276 (P271–P276) | 6 | Jérémie (16) — Baruch, Karkémish et le jugement des nations |
| 47 | `FICHES8_JEREMIE_17.html` (83 Ko) | `phase8/data/p8_jr17.py` | JR277 → JR282 (P277–P282) | 6 | Jérémie (17) — Le jugement des nations : d'Ammon à Élam |
| 48 | `FICHES8_JEREMIE_18.html` (84 Ko) | `phase8/data/p8_jr18.py` | JR283 → JR288 (P283–P288) | 6 | Jérémie (18) — Babylone jugée : Bel confondu, le peuple libéré |
| 49 | `FICHES8_JEREMIE_19.html` (87 Ko) | `phase8/data/p8_jr19.py` | JR289 → JR294 (P289–P294) | 6 | Jérémie (19) — Babylone : nulle pierre, le rouleau englouti |
| 50 | `FICHES8_JEREMIE_20_LAMENTATIONS_1.html` (84 Ko) | `phase8/data/p8_jr20lm1.py` | JR295 → LM300 (P295–P300) | 6 | Jérémie (20) + Lamentations (1, nouv.) — la chute, les larmes, l'espoir |
| 51 | `FICHES8_EZECHIEL_1.html` (90 Ko) | `phase8/data/p8_ez1.py` | EZ301 → EZ306 (P301–P306) | 6 | Ézéchiel (1) — la maison rebelle et les signes du siège |
| 52 | `FICHES8_EZECHIEL_2.html` (95 Ko) | `phase8/data/p8_ez2.py` | EZ307 → EZ312 (P307–P312) | 6 | Ézéchiel (2) — la fin, les abominations et la gloire qui part |
| 53 | `FICHES8_EZECHIEL_3.html` (92 Ko) | `phase8/data/p8_ez3.py` | EZ313 → EZ318 (P313–P318) | 6 | Ézéchiel (3) — le sanctuaire en exil, le prince aveugle, les faux prophètes |
| 54 | `FICHES8_EZECHIEL_4.html` (109 Ko) | `phase8/data/p8_ez4.py` | EZ319 → EZ324 (P319–P324) | 6 | Ézéchiel (4) — les quatre jugements, la vigne au feu, l'alliance permanente |
| 55 | `FICHES8_EZECHIEL_5.html` (118 Ko) | `phase8/data/p8_ez5.py` | EZ325 → EZ330 (P325–P330) | 6 | Ézéchiel (5) — la complainte des princes, le creuset, les deux sœurs |
| 56 | `FICHES8_EZECHIEL_6.html` (95 Ko) | `phase8/data/p8_ez6.py` | EZ331 → EZ336 (P331–P336) | 6 | Ézéchiel (6) — la marmite rouillée, le deuil interdit, les nations jugées |
| 57 | `FICHES8_EZECHIEL_7.html` (124 Ko) | `phase8/data/p8_ez7.py` | EZ337 → EZ342 (P337–P342) | 6 | Ézéchiel (7) — Tyr : le rocher raclé, le siège, la lamentation |
| 58 | `FICHES8_EZECHIEL_8.html` (161 Ko) | `phase8/data/p8_ez8.py` | EZ343 → EZ348 (P343–P348) | 6 | Ézéchiel (8) — Sidon jugée, Israël rassemblé, l'Égypte abaissée |
| 59 | `FICHES8_EZECHIEL_9.html` (223 Ko) | `phase8/data/p8_ez9.py` | EZ349 → EZ354 (P349–P354) | 6 | Ézéchiel (9) — le cèdre abattu, la fosse peuplée, le guetteur |
| 60 | `FICHES8_EZECHIEL_10.html` (343 Ko) | `phase8/data/p8_ez10.py` | EZ355 → EZ360 (P355–P360) | 6 | Ézéchiel (10) — le berger promis, Séir jugée, les ossements revivent |
| 61 | `FICHES8_EZECHIEL_11.html` (253 Ko) | `phase8/data/p8_ez11.py` | EZ361 → EZ366 (P361–P366) | 6 | Ézéchiel (11) — Gog tombe, le temple mesuré, la rivière guérit |
| 62 | `FICHES8_TRANSITION_EZDN.html` (264 Ko) | `phase8/data/p8_ezdn1.py` | EZ367 → DN372 (P367–P372) | 6 | Transition Ézéchiel-Daniel — Shammah, la cour de Babylone, la statue et la pierre |
| 63 | `FICHES8_DANIEL_1.html` (165 Ko) | `phase8/data/p8_dn1.py` | DN373 → DN378 (P373–P378) | 6 | Daniel 4-7 — la raison rendue, l'écriture murale, les bêtes de la mer et la petite corne |
| 64 | `FICHES8_DANIEL_2.html` (167 Ko) | `phase8/data/p8_dn2.py` | DN379 → DN384 (P379–P384) | 6 | Daniel 7-9 — le Trône de feu, le bélier et le bouc, les soixante-dix ans |
| 65 | `FICHES8_DANIEL_3.html` (146 Ko) | `phase8/data/p8_dn3.py` | DN385 → DN390 (P385–P390) | 6 | Daniel 9-11 — soixante-dix semaines, le prince de Perse, les rois du nord et du sud |
| 66 | `FICHES8_DANIEL_4.html` (137 Ko) | `phase8/data/p8_dn4.py` | DN391 → DN396 (P391–P396) | 6 | Daniel 11 — alliances et mariages, Raphia, le pays de la Parure |
| 67 | `FICHES8_DANIEL_5.html` (132 Ko) | `phase8/data/p8_dn5.py` | DN397 → DN402 (P397–P402) | 6 | Daniel 11 — l'exacteur, Antiochus IV et la chose immonde |
| 68 | `FICHES8_DANIEL_6.html` (114 Ko) | `phase8/data/p8_dn6.py` | DN403 → DN407 (P403–P407) | 5 | Daniel 12 — Mikaël, la résurrection, le livre scellé et les jours comptés |
| 69 | `FICHES8_OSEE_1.html` (133 Ko) | `phase8/data/p8_os1.py` | OS408 → OS413 (P408–P413) | 6 | Osée 1-3 — Jezréel, les noms des enfants et l'épouse ramenée |
| 70 | `FICHES8_OSEE_2.html` (133 Ko) | `phase8/data/p8_os2.py` | OS414 → OS419 (P414–P419) | 6 | Osée 4-10 — le procès, la connaissance rejetée et la captivité annoncée |
| 71 | `FICHES8_OSEE_3.html` (109 Ko) | `phase8/data/p8_os3.py` | OS420 → JL423 (P420–P423) | 4 | Osée 11 et 14, puis Joël 1 — « d'Égypte j'ai appelé mon fils », le retour de l'ouest, la rosée, et l'invasion des sauterelles |
| 72 | `FICHES8_JOEL_1.html` (161 Ko) | `phase8/data/p8_jl1.py` | JL424 → JL429 (P424–P429) | 6 | Joël 2 et 3 — le jour de Jéhovah, l'esprit répandu sur toute sorte de chair, et la vallée de la décision |
| 73 | `FICHES8_AMOS_1.html` (154 Ko) | `phase8/data/p8_am1.py` | AM430 → AM435 (P430–P435) | 6 | Amos 1-5 — les jugements des nations, l'oppression dénoncée et la rencontre avec Dieu |
| 74 | `FICHES8_AMOS_2.html` (169 Ko) | `phase8/data/p8_am2.py` | AM436 → AM441 (P436–P441) | 6 | Amos 6-9 — le malheur des gens à l'aise, les visions du prophète et la hutte de David relevée |
| 75 | `FICHES8_ABDIAS_1.html` (131 Ko) | `phase8/data/p8_ab1.py` | AB442 → AB446 (P442–P446) | 5 | Abdias — l'orgueil d'Édom précipité, la violence contre Jacob et le royaume qui revient à Jéhovah |
| 76 | `FICHES8_JONAS_1.html` (118 Ko) | `phase8/data/p8_jn1.py` | JN447 → JN450 (P447–P450) | 4 | Jonas — Ninive, les quarante jours et le signe du Fils de l'homme |
| 77 | `FICHES8_MICHEE_1.html` (164 Ko) | `phase8/data/p8_mi1.py` | MI451 → MI456 (P451–P456) | 6 | Michée 1-4 — Samarie et Sion jugées, la montagne élevée et le rassemblement de la boiteuse |
| 78 | `FICHES8_MICHEE_2.html` (165 Ko) | `phase8/data/p8_mi2.py` | MI457 → MI462 (P457–P462) | 6 | Michée 5-7 — Bethléem et celui dont l'origine remonte aux temps anciens, le procès de Jéhovah et le pardon des péchés |
| 79 | `FICHES8_NAHOUM_1.html` (118 Ko) | `phase8/data/p8_na1.py` | NA463 → NA466 (P463–P466) | 4 | Nahum 1-2 — La vengeance de Jéhovah, le porteur de bonnes nouvelles et la chute de Ninive |
| 80 | `FICHES8_NAHOUM_2.html` (91 Ko) | `phase8/data/p8_na2.py` | NA467 → NA469 (P467–P469) | 3 | Nahum 3 — La ville de sang, No-Amôn et la blessure incurable |
| 81 | `FICHES8_HABACUC_1.html` (118 Ko) | `phase8/data/p8_ha1.py` | HA470 → HA473 (P470–P473) | 4 | Habacuc 1-2 — Jusqu'à quand ? les Chaldéens, le juste vivra par sa fidélité et les malheurs sur Babylone |
| 82 | `FICHES8_HABACUC_2.html` (75 Ko) | `phase8/data/p8_ha2.py` | HA474 → HA475 (P474–P475) | 2 | Habacuc 2:18-20 et 3 — L'idole muette, le silence devant Jéhovah et la prière du prophète |
| 83 | `FICHES8_SOPHONIE_1.html` (101 Ko) | `phase8/data/p8_so1.py` | SO476 → SO478 (P476–P478) | 3 | Sophonie 1 — Le jour de Jéhovah proche, les idolâtres de Jérusalem et le silence devant le Souverain Seigneur |
| 84 | `FICHES8_SOPHONIE_2.html` (123 Ko) | `phase8/data/p8_so2.py` | SO479 → SO482 (P479–P482) | 4 | Sophonie 2 — Cherchez la justice, les villes de la côte, Moab et Ammon, et Ninive dévastée |
| 85 | `FICHES8_SOPHONIE_3.html` (83 Ko) | `phase8/data/p8_so3.py` | SO483 → SO484 (P483–P484) | 2 | Sophonie 3 — La ville rebelle et ses chefs voraces, puis la langue pure et le reste humble et modeste |
| 86 | `FICHES8_AGGEE_1.html` (165 Ko) | `phase8/data/p8_ag1.py` | AG485 → AG489 (P485–P489) | 5 | Aggée — Cinq messages datés au jour près, de la maison en ruine au cachet de Zorobabel |
| 87 | `FICHES8_ZACHARIE_1.html` (159 Ko) | `phase8/data/p8_za1.py` | ZA490 → ZA494 (P490–P494) | 5 | Zacharie 1-3 — Les huit visions de la nuit, les cornes abattues, le cordeau et le Germe |
| 88 | `FICHES8_ZACHARIE_2.html` (124 Ko) | `phase8/data/p8_za2.py` | ZA495 → ZA498 (P495–P498) | 4 | Zacharie 4-6 — Le chandelier et les deux oints, le rouleau volant, les quatre chars et la couronne du Germe |
| 89 | `FICHES8_ZACHARIE_3.html` (201 Ko) | `phase8/data/p8_za3.py` | ZA499 → ZA505 (P499–P505) | 7 | Zacharie 7-10 — Le jeûne devenu fête, le roi humble sur un âne, le rouleau sur les nations et la pluie demandée |
| 90 | `FICHES8_ZACHARIE_4.html` (172 Ko) | `phase8/data/p8_za4.py` | ZA506 → ZA511 (P506–P511) | 6 | Zacharie 11-14 — Les deux bergers, les trente pièces d'argent, le transpercé et le jour de Jéhovah |
| 91 | `FICHES8_MALACHIE_1.html` (264 Ko) | `phase8/data/p8_ml1.py` | ML512 → ML519 (P512–P519) | 8 | Malachie — L'amour de Jacob et la haine d'Ésaü, le messager du temple, les dîmes et le soleil de justice |

### 7.3 Fichier temporaire

| Fichier | Taille | Description |
|---|---|---|
| `_TMP_HA1.html` | 116 Ko | **Brouillon de build** de `FICHES8_HABACUC_1.html` généré **avant** l'appariement des audios (compteur audio à 0, pas de durées « 🎧 »). Doublon obsolète, candidat à la suppression. |

---

## 8. `preuves/divers/` — Prompts d'origine et exports de conversation (8 fichiers, 8,7 Mo)

| Fichier | Taille | Description |
|---|---|---|
| `prophéties.txt` | 44 Ko | **Prompt fondateur du registre** : demande d'inventaire exhaustif des prophéties bibliques et de leurs accomplissements sans commentaire, consignes de recherche (jw.org / wol.jw.org), contraintes médias (≤ 10 images JPG hyperréalistes / réponse, ≤ 10 audios FR), suivi d'une liste de départ à compléter. |
| `prophéties_prompts.txt` | 57 Ko | **« Méga-prompt » XML** (rôle, état d'esprit, mission, contraintes) ayant servi à produire `00_DOSSIER_10_STRATEGIES.md` et la suite du projet ; prompts de relance associés. |
| `etudes.txt` | 59 Ko | Réponse d'IA antérieure : une première version de « 10 stratégies d'évangélisation numérique » (Pont des compétences / micro-mentorat, etc.) — matériau brut ayant précédé le dossier stratégique final. |
| `clattes.txt` | 4,9 Mo, 26 560 l. | Journal texte massif des échanges de production de la **phase 8** (« CONTINUER. Je veux une fiche descriptive complète pour chaque prophétie… ») : prompts + réponses successives. Archive de travail. |
| `cjv.txt` | 719 Ko, 10 756 l. | Export texte d'une conversation arena.ai (mode « direct-battle », 36 messages, 24-26 sept. 2026) — session de conception des phases 1-6. |
| `cjv.json` | 1,0 Mo | Même conversation au format JSON structuré (`exportedAt`, `source`, `recordType: evaluation`, `conversationUrl`, `evaluation`). |
| `g79.txt` | 879 Ko, 8 506 l. | Export texte d'une seconde conversation arena.ai (38 messages, 27 sept. 2026) — session de production des dernières vagues de la phase 8. |
| `g79.json` | 993 Ko | Même conversation au format JSON structuré. |

---

## 9. Observations et points d'attention

1. **Médias non versionnés.** `preuves/images/` (~700 JPG) et `preuves/audio/` (~600 MP3 + `playlists/*.m3u`) sont décrits dans le README et référencés 1 419 fois dans les HTML, mais absents du dépôt (pas de `.gitignore` non plus). À stocker hors Git (LFS ou stockage externe) ou à ajouter si le dépôt doit être autonome.
2. **Fichier temporaire.** `preuves/_TMP_HA1.html` est un doublon pré-audio de `FICHES8_HABACUC_1.html`.
3. **Décalages de comptage dans la documentation.** Le README parle tantôt de 975 tantôt de 1 000 entrées ; `LIVRE_2_LES_1000.html` a pour `<title>` « Les 975 » ; `ETATS_PHASE8.md` affiche 505 fiches publiées alors que les données en contiennent 519 (P8-89 à P8-91 non reportées dans les compteurs). Le registre lui-même compte bien **1 000 entrées**.
4. **Rejouabilité.** Tous les générateurs sont en Python 3 standard (aucun `requirements.txt` nécessaire). Ordre logique : registre → `site/build_site.py`, `livres/build_livres.py`, `visuels/build_visuels.py`, `index/build_index.py`, `videos/build_videos.py`, `dates/build_dates.py`, `cahier/build_cahier.py` ; `collections/build_collections.py` requiert le dossier `audio/` ; `fiches/build_fiches.py` et `phase8/build_p8.py` prennent un module de données en argument.
5. **Reste à produire (phase 8).** P520 → P1000 : Psaumes et Écrits (P520-P569), Messie consolidé (P570-P646), paroles de Jésus (P647-P711), Actes/apôtres (P712-P791), Révélation (P792-P975), compléments (P976-P1000).


---

## Ajouts du 27 septembre 2026 (audit de complétude, non versionnés à ce stade)

| Fichier | Contenu |
|---|---|
| `preuves/AUDIT_COMPLETUDE_REGISTRE.md` | Audit de complétude du registre P001-P1000 : méthode, constat par livre, 226 propositions d'ajout (P1001-P1226) avec priorité et sources (wol.jw.org), passages écartés, doublons internes, comparaison Payne/Edersheim, suites. |
| `preuves/24_REGISTRE_PROPHETIES_8.md` | Partie 15 du registre : les 120 entrées P1001-P1120 issues des propositions A (fusions comprises). Remplace le fichier provisoire `24_REGISTRE_PROPHETIES_8_PROPOSITIONS.md`, supprimé. |
| `preuves/25_PROPOSITIONS_B_C_EN_ATTENTE.md` | Les 97 propositions B/C non intégrées, avec justification et priorité, en attente de décision. |
| `preuves/phase9/00_WORKFLOW_PHASE9.md` | **Workflow phase 9** (fiches P520-P1120) : objectif, actions du 27/09/2026, cycle S1-S8, gabarit 11 blocs, types de fiches (complète / commune / renvoi), séries, règles, journal des vagues (P9-1 faite, P9-2 → P9-5 planifiées). |
| `preuves/phase9/ETATS_PHASE9.md` | **Machine à états phase 9** générée par `tools/etat.py md` : 601 fiches (492 complètes, 59 communes, 50 renvois), compteurs par état, tableau par vague. |
| `preuves/phase9/etat.json` | Données de la machine à états (source de vérité : état, page, catégorie, médias de chaque fiche). |
| `preuves/phase9/tools/etat.py` | CLI de la machine à états : `init`, `set` (transitions un pas à la fois), `vague`, `media`, `stats`, `next`, `md`. |
| `preuves/phase9/tools/build_partie15.py` | Génère la partie 15 (fichier 24), le fichier 25 et `correspondance_audit_registre.tsv` à partir des 226 propositions de l'audit (dictionnaire FUSIONS : 9 fusions). |
| `preuves/phase9/tools/correspondance_audit_registre.tsv` | Table n° de proposition d'audit → numéro P définitif (ou « en attente »). |
| `preuves/phase9/tools/doublons_versets.json` | Passages cités par plusieurs entrées du registre (base des fiches « communes » et « renvois »). |
| `preuves/phase9/build_p9.py` | Wrapper de build phase 9 : réutilise `fiches/build_fiches.py`, injecte le bloc 10 « Schéma », renumérote « limites » en 11, ajoute la frise et le lien vers le registre. Usage : `python3 build_p9.py p9_gen1 FICHES9_GENESE_EXODE_1.html`. |
- `preuves/FICHES9_EXODE_NOMBRES_1.html` — Phase 9, vague P9-2 (28/09/2026) : 9 fiches complètes P629, P1009–P1016 (plaies annoncées, mer Rouge, cantique d'Exode 15, Amalek, l'ange et les frelons, Coré, Meriba/Hor/Nébo, serpent de cuivre) + section « Renvois » (GE570–GE572, NB573 → fiches phase 8) ; 54 sources wol.jw.org ; 9 JPG + 9 MP3.
- `preuves/FICHES9_DEUTERONOME_JUGES_1.html` — Phase 9, vague P9-3 (28/09/2026) : 9 fiches complètes P1017–P1020, P976–P980 (lieu du Nom, promesse à Josué, Jourdain, Jéricho, « Juda montera », Bokim, Gédéon, Samson, Benjamin) + renvoi DT628 → fiche DT059 (phase 8) ; 56 sources wol.jw.org ; 9 JPG + 9 MP3.
- `preuves/FICHES9_JUGES_RUTH_SAMUEL_1.html` — Phase 9, vague P9-4 (28/09/2026) : 8 fiches complètes P1021–P1023, P520, P521, P1024–P1026 (Sisera, les 300, fable de Yotham, Ruth et Boaz, généalogie de David, prière d'Anne, droit du roi, signes de Saül) + renvoi SM574 → fiche RO073 (phase 8) ; 47 sources wol.jw.org ; 8 JPG + 8 MP3.
- `preuves/FICHES9_SAMUEL_ROIS_1.html` — Phase 9, vague P9-5 (28/09/2026) : 9 fiches complètes P1027–P1035 (enfant de Bath-Shéba, sagesse de Salomon, homme de Dieu et lion, jarre de Tsarphath, pluie du Carmel, onctions de l'Horeb, sursis d'Achab, enlèvement d'Élie, famine de sept ans) ; 55 sources wol.jw.org ; 9 JPG + 9 MP3.
| `preuves/phase9/data/p9_gen1.py` | Données de la vague P9-1 : GE1001-GE1006, EX1007, EX1008 (8 fiches complètes, 11 blocs, 47 sources). |
| `preuves/FICHES9_GENESE_EXODE_1.html` | **Première page de la phase 9** (222 Ko) : Éden, sueur du visage, 120 ans, Déluge, arc-en-ciel, Sodome, buisson ardent, minuit — 8 images JPG (`preuves/images/`) et 8 audios MP3 (`preuves/audio/`), 0 lien mort. |
| `preuves/images/prophe_*.jpg`, `preuves/audio/fiche_*.mp3` | Médias de la phase 9 (8 + 8 au 27/09/2026 ; fenêtre glissante : les médias des vagues anciennes peuvent être régénérés à la demande). |
| `preuves/FICHES_MANQUANTES.md` | État des fiches : 519 fiches phase 8 (P001-P519), 150 fiches thématiques ; liste des 481 entrées P520-P1000 sans fiche individuelle (dont 161 sans aucune fiche), recommandations (fiche complète / commune / renvoi), et fiches à prévoir pour P1001-P1226. |
