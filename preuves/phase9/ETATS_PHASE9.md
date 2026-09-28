# PHASE 9 — Machine à états (fiches manquantes P520 → P1120)

*Généré par `phase9/tools/etat.py md` le 2026-09-28 à partir de `phase9/etat.json` (source de vérité de l'avancement).*

## 1. Graphe des états (par fiche)
```
A_PLANIFIER → RECHERCHE → REDACTION → CONTROLE → MEDIAS → PUBLIE
     ↑____________|___________|__________| (retour d'une étape si un contrôle échoue)
```
- **A_PLANIFIER** : entrée du registre inscrite dans la file d'attente, code de fiche réservé (`<SÉRIE><P>`), type fixé (complète · commune · renvoi).
- **RECHERCHE** : sources officielles (wol.jw.org / jw.org) et web (forums, vidéos, réseaux) collectées ; identifiants de documents notés dans la data.
- **REDACTION** : `phase9/data/p9_<vague>.py` écrit (11 blocs + texte + accomplissement + chronologie + sources).
- **CONTROLE** : `build_p9.py` passe (C4 liens officiels seuls · C5 limites non vides · C6 aucun bloc vide · C7 ≥ 2 sources officielles) ; statut = statut du registre.
- **MEDIAS** : illustration JPG (`images/prophe_<CODE>_<slug>.jpg`) et piste MP3 française (`audio/fiche_<CODE>_<slug>.mp3`) générées, appariées par le résolveur et présentes sur la page.
- **PUBLIE** : page `FICHES9_*.html` construite avec ses médias, présentée, compteurs à jour.

Transitions : une étape à la fois (`etat.py set` refuse les sauts). Tout retour en arrière est journalisé dans `historique`.

## 2. Compteurs globaux

| Indicateur | Valeur |
|---|---|
| Fiches de la file d'attente (P520–P1120) | **601** |
| Fiches PUBLIE | **49** |
| Reste à produire | **552** |
| Par état | A_PLANIFIER 552 · RECHERCHE 0 · REDACTION 0 · CONTROLE 0 · MEDIAS 0 · PUBLIE 49 |
| Par type | complète 492 · commune 59 · renvoi 50 |
| Médias phase 9 présents dans le dépôt de travail | 17 JPG · 17 MP3 |
| Pages produites | 5 |

## 3. Vagues

### P9-1 — GE91 · `FICHES9_GENESE_EXODE_1.html` · 2026-09-27

| Fiche | P | Référence | Type | État | JPG | MP3 |
|---|---|---|---|---|---|---|
| GE1001 | P1001 | Genèse 2:17 | complete | PUBLIE | ✓ | ✓ |
| GE1002 | P1002 | Genèse 3:16-19 | complete | PUBLIE | ✓ | ✓ |
| GE1003 | P1003 | Genèse 6:3 | complete | PUBLIE | ✓ | ✓ |
| GE1004 | P1004 | Genèse 6:13, 17 ; 7:4 | complete | PUBLIE | ✓ | ✓ |
| GE1005 | P1005 | Genèse 8:21, 22 ; 9:11-17 | complete | PUBLIE | ✓ | ✓ |
| GE1006 | P1006 | Genèse 18:20, 21 ; 19:12, 13 | complete | PUBLIE | ✓ | ✓ |
| EX1007 | P1007 | Exode 3:18-22 ; 7:3-5 | complete | PUBLIE | ✓ | ✓ |
| EX1008 | P1008 | Exode 4:21-23 ; 11:4-8 | complete | PUBLIE | ✓ | ✓ |

### P9-2 — EX91 · `FICHES9_EXODE_NOMBRES_1.html` · 2026-09-27

| Fiche | P | Référence | Type | État | JPG | MP3 |
|---|---|---|---|---|---|---|
| EX629 | P629 | Exode 12:46 ; Nombres 9:12 | complete | PUBLIE | ✓ | ✓ |
| EX1009 | P1009 | Exode 7:17 ; 8:2, 21-23 ; 9:3, 4, 18 ; 10:4 ; 11:7 | complete | PUBLIE | ✓ | ✓ |
| EX1010 | P1010 | Exode 14:13, 14, 17, 18 | complete | PUBLIE | ✓ | ✓ |
| EX1011 | P1011 | Exode 15:14-17 | complete | PUBLIE | ✓ | ✓ |
| EX1012 | P1012 | Exode 17:14, 16 ; Deutéronome 25:17-19 | complete | PUBLIE | ✓ | ✓ |
| EX1013 | P1013 | Exode 23:20-31 ; 34:10, 11, 24 | complete | PUBLIE | ✓ | ✓ |
| NB1014 | P1014 | Nombres 16:28-30 | complete | PUBLIE | ✓ | ✓ |
| NB1015 | P1015 | Nombres 20:12, 24 ; 27:12-14 ; Deutéronome 32:48-52 | complete | PUBLIE | ✓ | ✓ |
| NB1016 | P1016 | Nombres 21:8, 9 ; Jean 3:14, 15 ; 8:28 ; 12:32-34 | complete | PUBLIE | ✓ | ✓ |
| GE570 | P570 | Genèse 3:15 | renvoi → P1 | PUBLIE | — | — |
| GE571 | P571 | Genèse 12:3 ; 22:18 | renvoi → P3, P13 | PUBLIE | — | — |
| GE572 | P572 | Genèse 49:10 | renvoi → P29 | PUBLIE | — | — |
| NB573 | P573 | Nombres 24:17 | renvoi → P53 | PUBLIE | — | — |

### P9-3 — DT91 · `FICHES9_DEUTERONOME_JUGES_1.html` · 2026-09-27

| Fiche | P | Référence | Type | État | JPG | MP3 |
|---|---|---|---|---|---|---|
| DT1017 | P1017 | Deutéronome 12:5, 10, 11 | complete | PUBLIE | ✓ | ✓ |
| DT1018 | P1018 | Deutéronome 31:3-8, 23 ; Josué 1:2-9 | complete | PUBLIE | ✓ | ✓ |
| JS1019 | P1019 | Josué 3:10-13 | complete | PUBLIE | ✓ | ✓ |
| JS1020 | P1020 | Josué 6:2-5 | complete | PUBLIE | ✓ | ✓ |
| JG976 | P976 | Juges 1:1, 2 | complete | PUBLIE | ✓ | ✓ |
| JG977 | P977 | Juges 2:1-3 | complete | PUBLIE | ✓ | ✓ |
| JG978 | P978 | Juges 6:14-16 | complete | PUBLIE | ✓ | ✓ |
| JG979 | P979 | Juges 13:3-5 | complete | PUBLIE | ✓ | ✓ |
| JG980 | P980 | Juges 20:18, 28 | complete | PUBLIE | ✓ | ✓ |
| DT628 | P628 | Deutéronome 21:23 | renvoi → P59 | PUBLIE | — | — |

### P9-4 — JG92 · `FICHES9_JUGES_RUTH_SAMUEL_1.html` · 2026-09-27

| Fiche | P | Référence | Type | État | JPG | MP3 |
|---|---|---|---|---|---|---|
| JG1021 | P1021 | Juges 4:6-9 | complete | PUBLIE | ✓ | ✓ |
| JG1022 | P1022 | Juges 7:7, 9-15 | complete | PUBLIE | ✓ | ✓ |
| JG1023 | P1023 | Juges 9:7-20, 56, 57 | complete | PUBLIE | ✓ | ✓ |
| RT520 | P520 | Ruth 4:11, 12 | complete | PUBLIE | ✓ | ✓ |
| RT521 | P521 | Ruth 4:17-22 | complete | PUBLIE | ✓ | ✓ |
| SM1024 | P1024 | 1 Samuel 2:1-10 | complete | PUBLIE | ✓ | ✓ |
| SM1025 | P1025 | 1 Samuel 8:11-18 | complete | PUBLIE | ✓ | ✓ |
| SM1026 | P1026 | 1 Samuel 9:15-17 ; 10:1-9 | complete | PUBLIE | ✓ | ✓ |
| SM574 | P574 | 2 Samuel 7:12-16 | renvoi → P73 | PUBLIE | — | — |

### P9-5 — RO91 · `FICHES9_SAMUEL_ROIS_1.html` · 2026-09-28

| Fiche | P | Référence | Type | État | JPG | MP3 |
|---|---|---|---|---|---|---|
| SM1027 | P1027 | 2 Samuel 12:14 | complete | PUBLIE | ✓ | ✓ |
| RO1028 | P1028 | 1 Rois 3:12, 13 | complete | PUBLIE | ✓ | ✓ |
| RO1029 | P1029 | 1 Rois 13:20-24 | complete | PUBLIE | ✓ | ✓ |
| RO1030 | P1030 | 1 Rois 17:14 | complete | PUBLIE | ✓ | ✓ |
| RO1031 | P1031 | 1 Rois 18:1, 41-45 | complete | PUBLIE | ✓ | ✓ |
| RO1032 | P1032 | 1 Rois 19:15-18 | complete | PUBLIE | ✓ | ✓ |
| RO1033 | P1033 | 1 Rois 21:29 | complete | PUBLIE | ✓ | ✓ |
| RO1034 | P1034 | 2 Rois 2:3, 5, 9, 10 | complete | PUBLIE | ✓ | ✓ |
| RO1035 | P1035 | 2 Rois 8:1-3 | complete | PUBLIE | ✓ | ✓ |

## 4. File d'attente par livre (ordre canonique)

| Livre | Série | Fiches | Publiées | Numéros |
|---|---|---|---|---|
| Genèse | GE | 10 | 9 | P570, P571, P572, P975, P1001, P1002, P1003, P1004, P1005, P1006 |
| Exode | EX | 8 | 8 | P629, P1007, P1008, P1009, P1010, P1011, P1012, P1013 |
| Nombres | NB | 4 | 4 | P573, P1014, P1015, P1016 |
| Deutéronome | DT | 3 | 3 | P628, P1017, P1018 |
| Josué | JS | 2 | 2 | P1019, P1020 |
| Juges | JG | 8 | 8 | P976, P977, P978, P979, P980, P1021, P1022, P1023 |
| Ruth | RT | 2 | 2 | P520, P521 |
| 1 Samuel | SM | 3 | 3 | P1024, P1025, P1026 |
| 2 Samuel | SM | 2 | 2 | P574, P1027 |
| 1 Rois | RO | 6 | 6 | P1028, P1029, P1030, P1031, P1032, P1033 |
| 2 Rois | RO | 4 | 2 | P1034, P1035, P1036, P1037 |
| 1 Chroniques | CH | 2 | 0 | P522, P575 |
| 2 Chroniques | CH | 1 | 0 | P1038 |
| Job | JB | 3 | 0 | P563, P564, P565 |
| Psaume | PS | 76 | 0 | P523 … P1048 (76) |
| Proverbes | PR | 2 | 0 | P566, P567 |
| Ecclésiaste | EC | 1 | 0 | P568 |
| Isaïe | IS | 53 | 0 | P578 … P1080 (53) |
| Jérémie | JR | 3 | 0 | P580, P581, P590 |
| Ézéchiel | EZ | 2 | 0 | P582, P583 |
| Daniel | DN | 7 | 0 | P584, P595, P639, P640, P641, P689, P1081 |
| Osée | OS | 3 | 0 | P591, P1082, P1083 |
| Jonas | JO | 1 | 0 | P644 |
| Michée | MI | 3 | 0 | P585, P589, P1084 |
| Aggée | AG | 1 | 0 | P586 |
| Zacharie | ZA | 6 | 0 | P587, P614, P615, P622, P638, P1085 |
| Malachie | ML | 2 | 0 | P593, P594 |
| Matthieu | MT | 61 | 0 | P647 … P1098 (61) |
| Marc | MC | 13 | 0 | P981 … P993 (13) |
| Luc | LC | 19 | 0 | P652 … P1106 (19) |
| Jean | JN | 15 | 0 | P691 … P1111 (15) |
| Actes | AC | 16 | 0 | P700 … P1115 (16) |
| Romains | RM | 12 | 0 | P723, P724, P725, P726, P727, P728, P729, P730, P731, P732, P733, P1116 |
| 1 Corinthiens | CO | 6 | 0 | P734, P735, P736, P737, P738, P1117 |
| 2 Corinthiens | CO | 3 | 0 | P739, P740, P741 |
| Galates | GA | 3 | 0 | P742, P743, P744 |
| Éphésiens | EP | 5 | 0 | P745, P746, P747, P748, P749 |
| Philippiens | PH | 2 | 0 | P750, P751 |
| Colossiens | CL | 1 | 0 | P994 |
| 1 Thessaloniciens | TH | 4 | 0 | P752, P753, P754, P755 |
| 2 Thessaloniciens | TH | 4 | 0 | P756, P757, P758, P759 |
| 1 Timothée | TM | 1 | 0 | P760 |
| 2 Timothée | TM | 4 | 0 | P761, P762, P763, P764 |
| Tite | TT | 1 | 0 | P765 |
| Hébreux | HE | 8 | 0 | P766, P767, P768, P769, P770, P771, P772, P1118 |
| Jacques | JC | 3 | 0 | P773, P774, P775 |
| 1 Pierre | PI | 5 | 0 | P776, P777, P778, P779, P780 |
| 2 Pierre | PI | 7 | 0 | P781, P782, P783, P784, P785, P786, P1119 |
| 1 Jean | JA | 4 | 0 | P787, P788, P789, P1120 |
| Jude | JU | 2 | 0 | P790, P791 |
| Révélation | RV | 183 | 0 | P792 … P974 (183) |
| Cantique des Cantiques | ?? | 1 | 0 | P569 |

## 5. Règle de priorité de la file

1. Ordre canonique des livres, puis numéro P croissant à l'intérieur d'un livre ; les entrées de la partie 15 (P1001–P1120) sont insérées dans le livre auquel elles appartiennent.
2. Une vague = une page = 6 à 10 fiches d'un même livre (ou de livres voisins), ≤ 10 JPG et ≤ 10 MP3 par réponse.
3. Les entrées de type *renvoi* reçoivent une fiche courte (identification, texte, ce que la relecture messianique ajoute, lien vers la fiche phase 8) ; les entrées *communes* sont traitées sur la fiche de la plus petite entrée du groupe.
