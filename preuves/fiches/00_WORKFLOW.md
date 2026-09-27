# PHASE 7 — FICHES DESCRIPTIVES DE PROPHÉTIES
## Workflow de travail et machine à états

*Document de pilotage. Il décrit comment sont produites les fiches, dans quel ordre,
et à quels contrôles chaque étape est soumise. Il est mis à jour à chaque vague.*

---

## 1. Ce que change cette phase

| Phase précédente (registre P001→P1000) | Cette phase (fiches F001→…) |
|---|---|
| Inventaire **exhaustif** | Sélection **par catégorie** |
| **Aucun commentaire** | Commentaire, contexte, exégèse, interprétation |
| Une entrée = une ligne | Une fiche = dix blocs + chronologie + schéma |
| Objectif : ne rien omettre | Objectif : tout expliquer |

**Le registre reste la source de vérité et reste sans commentaire.** Il n'est jamais modifié
pour faire passer une fiche : c'est la fiche qui se corrige vers le registre (règle héritée des
frises chronologiques, où huit repères « non indexés » avaient été corrigés dans le mauvais sens).

---

## 2. Les catégories

| Code | Catégorie | Entrées visées | État |
|---|---|---|---|
| **A** | Prophéties contre les nations | ~10 | **13 fiches — TERMINÉE (vagues 1 et 3)** |
| **B** | Prophéties sur Jérusalem et Juda (Silo, 70 ans, retour, temple, 70) | ~10 | **9 fiches — TERMINÉE (vague 2 : Silo, 70 ans, Égypte, Cyrus, 2nd temple, rebâtie, siège 70, temple détruit, foulée)** |
| C | Prophéties messianiques — origine, naissance, ministère | ~12 | **14 fiches — TERMINÉE (vagues 3 et 4)** |
| D | Prophéties messianiques — procès, mort, résurrection | ~12 | **12 fiches — TERMINÉE (vagues 5 et 6)** |
| E | Prophéties des empires (Daniel 2, 7, 8, 11) | ~10 | **9 fiches — TERMINÉE (vagues 6 et 7)** |
| F | Prophéties chronologiques (70 ans, 70 semaines, sept temps, 1 290/1 335) | ~8 | **10 fiches — TERMINÉE (vagues 7 et 8)** |
| G | Prophéties de restauration et monde nouveau | ~10 | **9 fiches — TERMINÉE (vagues 8 et 9)** |
| H | Le signe et les derniers jours | ~10 | **10 fiches — TERMINÉE (vagues 9 et 10)** |
| I | Le livre de la Révélation | ~12 | **10 fiches — TERMINÉE (vagues 10 et 11)** |
| J | Personnages et lieux nommés d'avance (Cyrus, Josias, Bethléhem) | ~8 | **12 fiches — TERMINÉE (vagues 11 à 13 : + J012 Gog de Magog)** |
| K | La Bible et la science (cosmologie, cycles, terre) | ~8 | **8 fiches — TERMINÉE (vagues 13 et 14 : + K007 Pierre/jour de Jéhovah, K008 sabbats de la terre)** |
| L | Prophéties géographiques (Samarie, Ninive, Égypte, désolations durables) | ~8 | **10 fiches — TERMINÉE (vagues 14 et 15 : + L008 Syrie, L009 Égypte-Is/Jr44, L010 Babylone-Is/Ps — zéro chevauchement textuel avec A)** |
| R | Reliquats et compléments (Joseph, alliance, promesses, lettres, trône, aller-retour) | ~6 | **6 fiches — TERMINÉE (vague 16 : R001 Joseph, R002 alliance, R003 promesses + Douma, R004 sept lettres, R005 trône/Agneau, R006 Osée/Zacharie)** |
| S | Les Psaumes messianiques (Ps 2, portes/noces/Salomon, Ps 110, Passion, Serviteur, alliance) | ~6 | **6 fiches — TERMINÉE (vague 17 : S001 Ps 2, S002 Ps 24/45/72, S003 Ps 110, S004 Passion, S005 Serviteur, S006 alliance)** |
| T | Jérémie, 1re partie — le jugement (nord, Temple, rois, chute, faux, signes) | ~12 | **6 fiches — 1re PARTIE (vague 18 : T001 nord, T002 Temple, T003 rois, T004 chute, T005 faux, T006 signes ; 2e partie : 48 P à venir)** |

Chaque catégorie produit **un fichier HTML** (`FICHES_A_NATIONS.html`, etc.) contenant
l'ensemble de ses fiches, plus une chronologie de catégorie et un index.

---

## 3. Les dix blocs obligatoires d'une fiche

Toute fiche, quelle que soit la catégorie, porte ces dix blocs dans cet ordre.
Un bloc manquant fait échouer la validation (contrôle C7).

| N° | Bloc | Contenu |
|---|---|---|
| 1 | **Identification** | N° de fiche, référence, catégorie, statut, système chronologique |
| 2 | **Le texte** | Références complètes + l'énoncé prophétique cité par phrases courtes |
| 3 | **Contexte** | Le moment, le lieu, la situation politique, l'auteur, les destinataires |
| 4 | **Explication du texte** | Vocabulaire, genre littéraire, structure, difficultés du texte |
| 5 | **Interprétation** | La compréhension des Témoins de Jéhovah, **avec sa source** |
| 6 | **L'accomplissement** | Étapes datées, dans l'ordre |
| 7 | **Preuves historiques** | Documents, inscriptions, chroniques, auteurs profanes |
| 8 | **Preuves géographiques** | Le site, le relief, l'hydrographie, les routes |
| 9 | **Preuves scientifiques** | Archéologie, datation, géologie, climatologie, épigraphie |
| 10 | **Limites** | Ce que la fiche ne dit pas — **bloc obligatoire, jamais vide** |

Plus, systématiquement : une **chronologie SVG** inline, un **schéma** quand la fiche s'y prête,
les **sources** (liens wol.jw.org / www.jw.org), et le renvoi vers les entrées du registre.

---

## 4. La machine à états

### 4.1 États

| État | Nom | Travail effectué |
|---|---|---|
| **S0** | ARCHITECTURE | Créer `00_WORKFLOW.md`, `01_PLAN_CATEGORIES.md`, le générateur |
| **S1** | SÉLECTION | Choisir la catégorie, lister les prophéties, estimer la charge |
| **S2** | RECHERCHE | ≥ 4 sources par fiche, dont ≥ 2 sur wol.jw.org / www.jw.org |
| **S3** | RÉDACTION | Remplir les dix blocs dans le fichier de données de la catégorie |
| **S4** | GÉNÉRATION | Exécuter `build_fiches.py` → HTML de catégorie |
| **S5** | VALIDATION | Passer la grille de 12 contrôles (§ 5) |
| **S6** | MÉDIAS | ≤ 10 JPG + ≤ 10 MP3 (français) par réponse |
| **S7** | CLÔTURE | README patché, compteurs, présentation, demande CONTINUER |

### 4.2 Transitions

```
        ┌──────────────────────────────────────────────┐
        │                                              │
   [S0 ARCHITECTURE]                                   │
        │  garde : workflow + plan + générateur écrits  │
        ▼                                              │
   [S1 SÉLECTION]                                      │
        │  garde : liste de fiches arrêtée              │
        ▼                                              │
   [S2 RECHERCHE] ──────── sources < 2 wol/jw.org ──┐  │
        │  garde : ≥ 4 sources par fiche            │  │
        ▼                                            ▼  │
   [S3 RÉDACTION] ◄───────────── [S2 RECHERCHE] ───────┘
        │  garde : 10 blocs remplis, bloc 10 non vide   │
        ▼                                              │
   [S4 GÉNÉRATION]                                     │
        │  garde : exécution sans exception             │
        ▼                                              │
   [S5 VALIDATION] ───────── échec d'un contrôle ──────┘
        │  garde : 12/12 contrôles verts                │
        ▼                                              │
   [S6 MÉDIAS]  (≤ 10 images · ≤ 10 audios par réponse) │
        │  garde : quotas respectés                     │
        ▼                                              │
   [S7 CLÔTURE] ───────────────────────────────────────┘
        │  garde : README à jour, fichier présenté
        ▼
   [S1] catégorie suivante
```

### 4.3 Règles de transition

- **R1** — Aucune transition S3 → S4 si un seul bloc est vide. Le générateur lève une erreur
  et n'écrit rien.
- **R2** — Aucune transition S2 → S3 sans au moins deux sources officielles par fiche
  (wol.jw.org ou www.jw.org). Les sources profanes complètent, elles ne remplacent pas.
- **R3** — Aucune transition S5 → S6 si un contrôle de la grille échoue.
- **R4** — Les quotas médias (10 JPG, 10 MP3) sont **par réponse**, jamais par catégorie :
  une catégorie de 10 fiches se répartit donc sur plusieurs réponses si elle dépasse.
- **R5** — En cas de saturation de la réponse, la machine s'arrête **proprement en S7** :
  le fichier est écrit, validé, présenté, et l'état est sauvegardé ici même.
- **R6** — Les scripts de clôture écrivent chaque fichier avec sa propre variable :
  jamais de `write(s)` sur le workflow (incident vague 3, fichier reconstruit à la vague 4).

### 4.4 État courant

| Champ | Valeur |
|---|---|
| État | **S7 — CLÔTURE de la vague 18 (T, Jérémie 1re partie) — 2e partie : 48 P Jérémie** |
| Catégorie en cours | T — Jérémie, 1re partie — le jugement (nord, Temple, rois, chute, faux, signes) |
| Fiches produites | **F001-F009** (cat. A, 12 pages, 36 sources) + **B001-B009** (cat. B, 12 pages, 36 sources) + **A010-A013, C001-C005** (transition A–C, 13 pages, 36 sources) + **C006-C014** (ministère, 13 pages, 36 sources) + **D001-D009** (procès-mort-résurrection, 13 pages, 36 sources) + **D010-D012, E001-E006** (transition D–E, 12 pages, 36 sources) + **E007-E009, F010-F015** (transition E–F, 12 pages, 36 sources) + **F016-F019, G001-G005** (transition F–G, 12 pages, 36 sources) + **G006-G009, H001-H005** (transition G–H, 12 pages, 36 sources) + **H006-H010, I001-I004** (transition H–I, 12 pages, 36 sources) + **I005-I010, J001-J003** (transition I–J, 12 pages, 36 sources) + **J004-J011** (J suite, 11 pages, 32 sources) + **J012, K001-K006** (transition J–K, 10 pages, 29 sources) + **K007-K008, L001-L007** (transition K–L, 10 pages, 37 sources) + **L008-L010** (L 2e partie, 4 pages, 16 sources) + **R001-R006** (reliquats, 7 pages, 27 sources) + **S001-S006** (psaumes, 7 pages, 30 sources) + **T001-T006** (Jérémie 1, 7 pages, 26 sources) = **144 fiches** |
| Prochaine étape | Vague 19 : T 2e partie — Jérémie restauration, Égypte, Babylone (48 P). |
| Prochaine transition | Aucune. |

---

## 5. Grille de validation (12 contrôles)

| N° | Contrôle | Seuil |
|---|---|---|
| C1 | Balises HTML non fermées | 0 |
| C2 | Erreurs de structure HTML | 0 |
| C3 | Ressources distantes chargées (`src`, feuille de style) | 0 |
| C4 | Liens externes non conformes (hors jw.org / wol.jw.org) | 0 |
| C5 | Fiches dont le bloc **Limites** est vide | 0 |
| C6 | Fiches dont un des dix blocs est vide | 0 |
| C7 | Fiches avec moins de 2 sources wol/jw.org | 0 |
| C8 | Références bibliques non rattachées à une entrée du registre | signalées |
| C9 | Dates pour l'avenir | 0 |
| C10 | Systèmes chronologiques mélangés dans une même fiche | 0 |
| C11 | Images non légendées « Illustration » | 0 |
| C12 | Compteurs README cohérents avec le disque | obligatoire |

---

## 6. Contraintes permanentes (héritées des phases précédentes)

1. **Un seul système chronologique par fiche** : 607 · 539 · 537 · 455 · 29 · 33 · 36 · 1914.
   Les dates neutres (701, 663, 604, 539, 332, 217, 168) sont communes à toutes les chronologies
   et sont signalées comme telles.
2. **Aucune date pour l'avenir.** Ce qui n'est pas accompli reste sans date.
3. **Aucun total dogmatique.** La Bibliothèque en ligne écrit qu'il est préférable de ne pas se
   montrer trop affirmatif quant au nombre exact des prophéties messianiques.
4. **Aucun contenu protégé reproduit.** Les références bibliques sont citées par phrases courtes ;
   aucune publication n'est recopiée ni hébergée.
5. **Liens exclusivement** vers www.jw.org et wol.jw.org.
6. **Aucun site critique ou apostat** comme source.
7. **Images** : JPG haute qualité, hyperréalistes, cinématographiques, **≤ 10 par réponse**,
   toujours légendées « Illustration » — jamais présentées comme des documents.
8. **Audios** : français uniquement, **≤ 10 par réponse**.
9. **Découpage** : la réponse s'arrête et demande CONTINUER avant la saturation.

---

## 7. Journal des vagues

| Vague | Date | Catégorie | Fiches | Fichier produit |
|---|---|---|---|---|
| 1 | 2026-09-24 | A — Prophéties contre les nations | F001-F009 | `FICHES_A_NATIONS.html` (101 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 2 | 2026-09-24 | B — Prophéties sur Jérusalem et Juda | B001-B009 | `FICHES_B_JERUSALEM.html` (97 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 3 | 2026-09-24 | A–C — Fin des nations + Messie (1re partie) | A010-A013, C001-C005 | `FICHES_C_MESSIE_1.html` (106 Ko, 13 pages) · 10 JPG · 10 MP3 |
| 4 | 2026-09-24 | C — Le Messie : le ministère (2e partie) | C006-C014 | `FICHES_C_MESSIE_2.html` (104 Ko, 13 pages) · 10 JPG · 10 MP3 |
| 5 | 2026-09-24 | D — Procès, mort, résurrection (1re partie) | D001-D009 | `FICHES_D_PASSION_1.html` (106 Ko, 13 pages) · 10 JPG · 10 MP3 |
| 6 | 2026-09-24 | D–E — Fin du Messie + Empires (1re partie) | D010-D012, E001-E006 | `FICHES_E_EMPIRES_1.html` (111 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 7 | 2026-09-24 | E–F — Fin des empires + Chronologies (1re partie) | E007-E009, F010-F015 | `FICHES_F_CHRONO_1.html` (111 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 8 | 2026-09-24 | F–G — Fin des chronologies + Restauration (1re partie) | F016-F019, G001-G005 | `FICHES_G_RESTAURATION_1.html` (111 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 9 | 2026-09-24 | G–H — Fin de la restauration + Le signe (1re partie) | G006-G009, H001-H005 | `FICHES_H_SIGNE_1.html` (112 Ko, 12 pages) · 10 JPG · 10 MP3 |
| 10 | 2026-09-24 | H–I — Fin du signe + Révélation (1re partie) | H006-H010, I001-I004 | `FICHES_I_REVELATION_1.html` (117 Ko, 12 pages) · 10 JPG · 10 MP3 (H10 régénéré vague 11) |
| 11 | 2026-09-24 | I–J — Fin de la Révélation + Nommés d'avance (1re partie) | I005-I010, J001-J003 | `FICHES_J_NOMMES_1.html` (117 Ko, 12 pages) · 10 JPG · 10 MP3 (J003 livré en vague 12) |
| 12 | 2026-09-24 | J — Nommés d'avance (2e partie) | J004-J011 | `FICHES_J_NOMMES_2.html` (106 Ko, 11 pages) · 9 JPG · 10 MP3 (J003 inclus) |
| 13 | 2026-09-24 | J–K — Fin des nommés + Science (1re partie) | J012, K001-K006 | `FICHES_K_SCIENCE_1.html` (92 Ko, 10 pages) · 8 JPG · 8 MP3 |
| 14 | 2026-09-24 | K–L — Fin de la science + Géographie (1re partie) | K007-K008, L001-L007 | `FICHES_L_GEO_1.html` (119 Ko, 10 pages) · 10 JPG · 10 MP3 |
| 15 | 2026-09-24 | L — Géographie (2e partie, FIN) | L008-L010 | `FICHES_L_GEO_2.html` (52 Ko, 4 pages) · 4 JPG · 4 MP3 |
| 16 | 2026-09-24 | R — Reliquats et compléments (FIN) | R001-R006 | `FICHES_R_RELIQUATS.html` (92 Ko, 7 pages) · 7 JPG · 7 MP3 |
| 17 | 2026-09-24 | S — Psaumes messianiques (FIN) | S001-S006 | `FICHES_S_PSAUMES.html` (99 Ko, 7 pages) · 7 JPG · 7 MP3 |
| 18 | 2026-09-24 | T — Jérémie 1re partie : le jugement | T001-T006 | `FICHES_T_JEREMIE_1.html` (101 Ko, 7 pages) · 7 JPG · 7 MP3 |
| 19 | 2026-09-24 | T — Jérémie 2e partie : la restauration (FIN) | T007-T012 | `FICHES_T_JEREMIE_2.html` (113 Ko, 7 pages) · 7 JPG · 7 MP3 |
