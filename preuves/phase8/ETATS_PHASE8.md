# PHASE 8 — Machine à états

## 1. Graphe des états (par fiche)
```
A_PLANIFIER → RECHERCHE → REDACTION → CONTROLE → MEDIAS → PUBLIE
     ↑____________| (retour si échec contrôle : C4–C7, source, statut)
```
- **A_PLANIFIER** : P attribué à une vague, slug réservé.
- **RECHERCHE** : sources jw/wol + web collectées, URLs notées.
- **REDACTION** : data écrite (11 blocs), schéma + limites non vides.
- **CONTROLE** : build OK, validation C4–C7, 0 lien mort img/audio.
- **MEDIAS** : JPG + MP3 générés et appariés (résolveur theme.py).
- **PUBLIE** : page présentée, compteurs à jour.

Règle : on ne passe à l'état suivant que si le précédent est **vérifié**
(commande ou relecture explicite). Tout retour en arrière est noté au journal.

## 2. Compteurs globaux
- Fiches PUBLIE : **505 / 1000** · P couverts : **505 (P001–P505)** · JPG phase 8 : **553 créés (26 présents, dont 7 vignettes)** · MP3 phase 8 : **516 créés (24 pistes présentes, 601,3 s)**
- QC paires nwt (constat du 2026-09-26) : 33 paires sont partagées entre modules des vagues **antérieures** à §3bt (Osée, Daniel, Ézéchiel, Jérémie, Rois, Ruth/Chroniques) — contrôles de collision non systématiques avant §3bt ; **les vagues §3bt à §3cm sont propres** (0 paire partagée, contrôle après §3cm — les 23 paires de ZA3 testées contre les 770 modules antérieurs, les 18 paires de ZA4 contre les 793, puis les 24 paires de ML1 contre les 842 : 0 collision, 0 doublon interne). Correction ponctuelle appliquée : Abdias 44/26 → 44/13.

## 3. Vague P8-1 (GE — Genèse 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE001 | P001 | Gn 3:15 · la postérité écrasera le serpent | PUBLIE |
| GE002 | P002 | Gn 9:25-27 · Canaan, Sem, Japhet | PUBLIE |
| GE003 | P003 | Gn 12:2-3 · toutes les familles bénies | PUBLIE |
| GE004 | P004 | Gn 13:14-17 · la terre pour toujours | PUBLIE |
| GE005 | P005 | Gn 15:4-6 · descendance comme les étoiles | PUBLIE |
| GE006 | P006 | Gn 15:13-14 · 400 ans puis la sortie | PUBLIE |

## 3b. Vague P8-2 (GE — Genèse 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE007 | P007 | Gn 15:16 · retour à la 4e génération | PUBLIE |
| GE008 | P008 | Gn 15:18-21 · frontières aux dix peuples | PUBLIE |
| GE009 | P009 | Gn 16:10-12 · Ismaël : multitude, vie hostile | PUBLIE |
| GE010 | P010 | Gn 17:19-21 · Isaac héritier ; Ismaël béni | PUBLIE |
| GE011 | P011 | Gn 18:10, 14 · Sara enfantera au temps fixé | PUBLIE |
| GE012 | P012 | Gn 21:12 · postérité appelée par Isaac | PUBLIE |

## 3c. Vague P8-3 (GE — Genèse 3)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE013 | P013 | Gn 22:15-18 · serment de Moriya, porte des ennemis | PUBLIE |
| GE014 | P014 | Gn 24:60 · Rébecca : porte des ennemis | PUBLIE |
| GE015 | P015 | Gn 25:23 · deux nations, l'aîné servira | PUBLIE |
| GE016 | P016 | Gn 26:2-5 · Isaac béni à Guérar | PUBLIE |
| GE017 | P017 | Gn 27:27-29 · bénédiction de Jacob | PUBLIE |
| GE018 | P018 | Gn 27:39-40 · Ésaü : épée, joug secoué | PUBLIE |

## 3d. Vague P8-4 (GE — Genèse 4)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE019 | P019 | Gn 28:13-15 · Béthel : terre, postérité, retour | PUBLIE |
| GE020 | P020 | Gn 35:11, 12 · une nation et des nations de Jacob | PUBLIE |
| GE021 | P021 | Gn 37:5-11 · les rêves de Joseph | PUBLIE |
| GE022 | P022 | Gn 40:8-19 · échanson rétabli, panetier pendu | PUBLIE |
| GE023 | P023 | Gn 41:25-32 · sept ans d'abondance, sept ans de famine | PUBLIE |
| GE024 | P024 | Gn 45:7-11 ; 50:20 · la maison de Jacob préservée | PUBLIE |

## 3e. Vague P8-5 (GE — Genèse 5)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE025 | P025 | Gn 46:3, 4 · le visa de Beér-Shéba, Joseph fermera les yeux | PUBLIE |
| GE026 | P026 | Gn 48:19 · Éphraïm plus grand que Manassé | PUBLIE |
| GE027 | P027 | Gn 49:3, 4 · Ruben instable, sans prééminence | PUBLIE |
| GE028 | P028 | Gn 49:5-7 · Siméon et Lévi dispersés en Israël | PUBLIE |
| GE029 | P029 | Gn 49:8-12 · Juda : sceptre, législateur, Shilo | PUBLIE |
| GE030 | P030 | Gn 49:13 · Zabulon près de la mer | PUBLIE |

## 3f. Vague P8-6 (GE — Genèse 6)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE031 | P031 | Gn 49:14, 15 · Issacar et le travail forcé | PUBLIE |
| GE032 | P032 | Gn 49:16-18 · Dan jugera son peuple | PUBLIE |
| GE033 | P033 | Gn 49:19 · Gad harcelé par des bandes | PUBLIE |
| GE034 | P034 | Gn 49:20 · Aser : nourriture riche | PUBLIE |
| GE035 | P035 | Gn 49:21 · Nephtali : belles paroles | PUBLIE |
| GE036 | P036 | Gn 49:22-26 · Joseph : cieux et abîme | PUBLIE |

## 3g. Vague P8-7 (GE — Genèse 7 / transition Exode)
| Fiche | P | Sujet | État |
|---|---|---|---|
| GE037 | P037 | Gn 49:27 · Benjamin le loup qui dévore | PUBLIE |
| GE038 | P038 | Gn 50:24, 25 · remontez mes ossements | PUBLIE |
| GE039 | P039 | Ex 3:12 · vous servirez sur cette montagne | PUBLIE |
| GE040 | P040 | Ex 6:2-8 · sortie d'Égypte et don de la terre | PUBLIE |
| GE041 | P041 | Ex 9:16 · mon nom proclamé par toute la terre | PUBLIE |
| GE042 | P042 | Ex 12:12, 13 · jugement sur les dieux ; le sang signe | PUBLIE |

## 3h. Vague P8-8 (EX — Exode 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EX043 | P043 | Ex 12:14-17 · la Pâque, ordonnance permanente | PUBLIE |
| EX044 | P044 | Ex 14:4 · Pharaon poursuivra Israël | PUBLIE |
| EX045 | P045 | Ex 19:5, 6 · royaume de prêtres, nation sainte | PUBLIE |
| EX046 | P046 | Ex 32:33, 34 · le jour où je ferai rendre des comptes | PUBLIE |
| EX047 | P047 | Ex 33:1-3 · montée vers le pays ; un ange devant | PUBLIE |
| EX048 | P048 | Lé 26:14-39 · épée, peste, famine, dispersion | PUBLIE |

## 3i. Vague P8-9 (EX — Exode 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EX049 | P049 | Lé 26:34, 35, 43 · la terre jouira de ses sabbats | PUBLIE |
| EX050 | P050 | Lé 26:40-45 · confession, retour, souvenir de l'alliance | PUBLIE |
| EX051 | P051 | Nb 14:26-35 · 40 ans : la génération mourra au désert | PUBLIE |
| EX052 | P052 | Nb 23:19-24 · Dieu ne ment pas ; Israël comme un lion | PUBLIE |
| EX053 | P053 | Nb 24:17-19 · une étoile sortira de Jacob | PUBLIE |
| EX054 | P054 | Nb 24:20-24 · Amalek ; navires de Kittim | PUBLIE |

## 3j. Vague P8-10 (DT — Deutéronome 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DT055 | P055 | Nb 33:55, 56 · les non-chassés, des épines | PUBLIE |
| DT056 | P056 | Dt 4:25-31 · dispersion, puis retour | PUBLIE |
| DT057 | P057 | Dt 17:14-20 · le roi : ni chevaux, ni femmes, ni argent | PUBLIE |
| DT058 | P058 | Dt 18:15-19 · un prophète comme Moïse | PUBLIE |
| DT059 | P059 | Dt 21:22, 23 · pendu au bois : maudit | PUBLIE |
| DT060 | P060 | Dt 28:15-68 · siège, dispersion, retour en Égypte | PUBLIE |

## 3k. Vague P8-11 (DT — Deutéronome 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DT061 | P061 | Dt 29:22-28 · les passants demanderont pourquoi | PUBLIE |
| DT062 | P062 | Dt 30:1-10 · rassemblement, cœur circoncis | PUBLIE |
| DT063 | P063 | Dt 31:16-21 · apostasie prévue, cantique témoin | PUBLIE |
| DT064 | P064 | Dt 32:15-43 · cantique : vengeance, nations jugées | PUBLIE |
| DT065 | P065 | Dt 33:1-29 · bénédictions par tribu | PUBLIE |
| DT066 | P066 | Jos 6:26 · Jéricho rebâtie au prix des fils | PUBLIE |

## 3l. Vague P8-12 (SM — Samuel 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| SM067 | P067 | Jos 23:14-16 · malheur si apostasie | PUBLIE |
| SM068 | P068 | 1S 2:27-36 · maison d'Éli jugée, fidèle suscité | PUBLIE |
| SM069 | P069 | 1S 3:11-14 · jugement irréversible sur Éli | PUBLIE |
| SM070 | P070 | 1S 13:13, 14 · royauté de Saül non durable | PUBLIE |
| SM071 | P071 | 1S 15:28 · royaume donné au compagnon | PUBLIE |
| SM072 | P072 | 1S 28:16-19 · Saül et ses fils tomberont | PUBLIE |

## 3m. Vague P8-13 (RO — Rois 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RO073 | P073 | 2S 7:8-16 · maison et trône de David pour toujours | PUBLIE |
| RO074 | P074 | 2S 12:10-12 · l'épée sur la maison de David | PUBLIE |
| RO075 | P075 | 1R 9:3-9 · maison rejetée ; les passants demanderont | PUBLIE |
| RO076 | P076 | 1R 11:29-39 · dix tribus à Jéroboam | PUBLIE |
| RO077 | P077 | 1R 13:2-5 · Josias nommé ; l'autel se déchire | PUBLIE |
| RO078 | P078 | 1R 14:6-16 · Abiya ; maison de Jéroboam effacée | PUBLIE |

## 3n. Vague P8-14 (RO — Rois 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RO079 | P079 | 1R 16:1-4 · maison de Baasha effacée | PUBLIE |
| RO080 | P080 | 1R 17:1 · ni rosée ni pluie, sinon par sa parole | PUBLIE |
| RO081 | P081 | 1R 20:13, 14, 28 · deux victoires sur la Syrie | PUBLIE |
| RO082 | P082 | 1R 21:19-24 · chiens : sang d'Achab, Jézabel mangée | PUBLIE |
| RO083 | P083 | 1R 22:17-23 · dispersés ; esprit de mensonge | PUBLIE |
| RO084 | P084 | 2R 1:3-17 · Achazia ne se relèvera pas | PUBLIE |

## 3o. Vague P8-15 (RO — Rois 3)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RO085 | P085 | 2R 3:16-19 · fosses remplies ; Moab livré | PUBLIE |
| RO086 | P086 | 2R 4:16, 17 · la Sunamite aura un fils | PUBLIE |
| RO087 | P087 | 2R 4:43, 44 · vingt pains : on mangera, il restera | PUBLIE |
| RO088 | P088 | 2R 5:27 · lèpre de Naamân sur Guéhazi | PUBLIE |
| RO089 | P089 | 2R 7:1, 2 · prix effondrés ; l'officier verra sans manger | PUBLIE |
| RO090 | P090 | 2R 8:10-13 · Hazaël roi frappera Israël | PUBLIE |

## 3p. Vague P8-16 (RO — Rois 4)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RO091 | P091 | 2R 9:6-10 · Jéhu effacera la maison d'Achab | PUBLIE |
| RO092 | P092 | 2R 10:30 · tes fils jusqu'à la 4e génération sur le trône | PUBLIE |
| RO093 | P093 | 2R 13:14-19 · trois victoires sur la Syrie, pas plus | PUBLIE |
| RO094 | P094 | 2R 19:6, 7 · Sennachérib rentrera et tombera par l'épée | PUBLIE |
| RO095 | P095 | 2R 19:32-34 · la ville ne sera pas prise : ni flèche, ni remblai | PUBLIE |
| RO096 | P096 | 2R 20:5, 6 · guérison le 3e jour ; 15 années ajoutées | PUBLIE |

## 3q. Vague P8-17 (RO — Rois 5 + CH — Chroniques 1, mixte)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RO097 | P097 | 2R 20:16-18 · trésors et descendants emmenés à Babylone | PUBLIE |
| RO098 | P098 | 2R 21:10-15 · Jérusalem livrée ; le reste rejeté | PUBLIE |
| RO099 | P099 | 2R 22:15-20 · Josias recueilli en paix, ne verra pas le malheur | PUBLIE |
| CH100 | P100 | 2Ch 12:5-8 · Shishaq dominera ; ruine pas complète | PUBLIE |
| CH101 | P101 | 2Ch 20:15-17, 20 · la bataille n'est pas la vôtre | PUBLIE |
| CH102 | P102 | 2Ch 24:20-22 · une petite troupe syrienne vaincra Juda | PUBLIE |

## 3r. Vague P8-18 (CH + ED + NE + IS, mixte 4 livres)
| Fiche | P | Sujet | État |
|---|---|---|---|
| CH103 | P103 | 2Ch 28:9-11 · les 200 000 captifs de Juda renvoyés | PUBLIE |
| CH104 | P104 | 2Ch 36:20-21 · 70 ans, la terre accomplira ses sabbats | PUBLIE |
| ED105 | P105 | Esd 1:1-4 · décret de Cyrus, reconstruction de la maison | PUBLIE |
| NE106 | P106 | Né 1:8, 9 · rassemblement des dispersés vers le lieu choisi | PUBLIE |
| IS107 | P107 | Is 1:7-9 · pays ravagé ; Sion comme un abri de veilleur | PUBLIE |
| IS108 | P108 | Is 2:2-4 · nations affluent ; épées en socs | PUBLIE |

## 3s. Vague P8-19 (IS — Isaïe 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS109 | P109 | Is 5:26-30 · nation lointaine sifflée ; rugissement de lion | PUBLIE |
| IS110 | P110 | Is 6:9-13 · cœur engraissé ; terre déserte ; 10e partie | PUBLIE |
| IS111 | P111 | Is 7:1-7 · la coalition syro-éphraïmite échouera | PUBLIE |
| IS112 | P112 | Is 7:8 · en 65 ans Éphraïm brisé, plus un peuple | PUBLIE |
| IS113 | P113 | Is 7:14 · la jeune femme enfantera Immanuël | PUBLIE |
| IS114 | P114 | Is 7:17-25 · l'Assyrie submergera Juda | PUBLIE |

## 3t. Vague P8-20 (IS — Isaïe 3)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS115 | P115 | Is 8:1-4 · l'enfant « pille-vite » ; Damas et Samarie pillées | PUBLIE |
| IS116 | P116 | Is 8:7, 8 · le Fleuve déborde sur Juda jusqu'au cou | PUBLIE |
| IS117 | P117 | Is 8:14, 15 · pierre de trébuchement, rocher de scandale | PUBLIE |
| IS118 | P118 | Is 8:17, 18 · moi et les enfants donnés : signes en Israël | PUBLIE |
| IS119 | P119 | Is 9:1, 2 · la Galilée verra une grande lumière | PUBLIE |
| IS120 | P120 | Is 9:3-7 · le Prince de la paix ; trône de David pour toujours | PUBLIE |

## 3u. Vague P8-21 (IS — Isaïe 4)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS121 | P121 | Is 10:5-19 · l'Assyrie, bâton de colère, à son tour abattue | PUBLIE |
| IS122 | P122 | Is 10:20-23 · le reste reviendra au Dieu fort | PUBLIE |
| IS123 | P123 | Is 11:1-5 · un rameau sortira de Jessé ; il jugera avec justice | PUBLIE |
| IS124 | P124 | Is 11:6-10 · loup avec l'agneau ; les nations cherchent le rameau | PUBLIE |
| IS125 | P125 | Is 11:11-16 · Jéhovah tendra sa main une seconde fois | PUBLIE |
| IS126 | P126 | Is 13:1-22 · Babylone prise par les Mèdes ; jamais plus habitée | PUBLIE |

## 3v. Vague P8-22 (IS — Isaïe 5)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS127 | P127 | Is 14:1, 2 · Israël rétabli, maître de ses oppresseurs | PUBLIE |
| IS128 | P128 | Is 14:4-23 · le roi de Babylone précipité ; trône renversé | PUBLIE |
| IS129 | P129 | Is 14:24-27 · l'Assyrie brisée dans le pays de Jéhovah | PUBLIE |
| IS130 | P130 | Is 15-16 · Moab dévasté, gloire ruinée en trois ans | PUBLIE |
| IS131 | P131 | Is 17:1-11 · Damas devient un tas de ruines | PUBLIE |
| IS132 | P132 | Is 19:1-17 · l'Égypte livrée à un maître dur | PUBLIE |

## 3w. Vague P8-23 (IS — Isaïe 6)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS133 | P133 | Is 19:18-25 · autel en Égypte ; trio Égypte-Assyrie-Israël béni | PUBLIE |
| IS134 | P134 | Is 20:1-6 · nu et pieds nus : Ashdod tombera (711) | PUBLIE |
| IS135 | P135 | Is 21:1-10 · Babylone est tombée ; le guet voit | PUBLIE |
| IS136 | P136 | Is 21:11, 12 · Duma : veilleur, où en est la nuit ? | PUBLIE |
| IS137 | P137 | Is 21:13-17 · la gloire de Kédar finit en un an | PUBLIE |
| IS138 | P138 | Is 22:1-25 · vallée de la vision ; Shebna arraché, Éliaqim | PUBLIE |

## 3x. Vague P8-24 (IS — Isaïe 7)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS139 | P139 | Is 23:1-18 · Tyr oubliée 70 ans, puis commerce repris | PUBLIE |
| IS140 | P140 | Is 24:1-23 · jugement mondial ; lune et soleil confondus | PUBLIE |
| IS141 | P141 | Is 25:1-12 · la mort engloutie ; repas sur la montagne | PUBLIE |
| IS142 | P142 | Is 26:1-19 · tes morts vivront ; les morts tomberont | PUBLIE |
| IS143 | P143 | Is 27:1-13 · Léviathan frappé ; grande trompette | PUBLIE |
| IS144 | P144 | Is 28:1-4 · couronne d'Éphraïm foulée aux pieds | PUBLIE |

## 3y. Vague P8-25 (IS — Isaïe 8)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS145 | P145 | Is 28:14-22 · la pierre d'angle éprouvée, posée en Sion | PUBLIE |
| IS146 | P146 | Is 29:1-8 · Ariel assiégée, ennemis dispersés comme un rêve | PUBLIE |
| IS147 | P147 | Is 29:9-14 · la sagesse des sages périra ; précepte humain | PUBLIE |
| IS148 | P148 | Is 30:27-33 · l'Assyrie écrasée ; Tophéth en bûcher | PUBLIE |
| IS149 | P149 | Is 31:4-9 · l'Assyrie tombera par une épée non d'homme | PUBLIE |
| IS150 | P150 | Is 33:17-24 · le roi dans sa beauté ; plus de maladie | PUBLIE |

## 3z. Vague P8-26 (IS — Isaïe 9)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS151 | P151 | Is 34:1-17 · Édom désolée pour toujours ; bêtes du désert | PUBLIE |
| IS152 | P152 | Is 35:1-10 · aveugles et sourds ouverts ; route sainte | PUBLIE |
| IS153 | P153 | Is 37:6-7,33-35 · Sanchérib rentrera, mourra par l'épée | PUBLIE |
| IS154 | P154 | Is 38:1-8 · quinze ans ajoutés ; ombre du cadran recule | PUBLIE |
| IS155 | P155 | Is 39:5-7 · tout emporté à Babylone ; fils serviteurs | PUBLIE |
| IS156 | P156 | Is 40:1-11 · voix dans le désert : préparez le chemin | PUBLIE |

## 3aa. Vague P8-27 (IS — Isaïe 10)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS157 | P157 | Is 41:2-4,25 · celui du levant foulera les gouverneurs | PUBLIE |
| IS158 | P158 | Is 42:1-9 · mon serviteur : lumière pour les nations | PUBLIE |
| IS159 | P159 | Is 43:5-7 · rassemblement des fils de toutes directions | PUBLIE |
| IS160 | P160 | Is 44:24-28 · Jérusalem rebâtie ; Cyrus mon berger | PUBLIE |
| IS161 | P161 | Is 45:1-7 · Cyrus oint : portes, trésors, sans combat | PUBLIE |
| IS162 | P162 | Is 46:1,2 · Bel plie, Nebo s'affaisse, idoles en exil | PUBLIE |

## 3ab. Vague P8-28 (IS — Isaïe 11)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS163 | P163 | Is 46:8-11 · j'annonce la fin ; oiseau de proie du levant | PUBLIE |
| IS164 | P164 | Is 47:1-15 · Babylone veuve en un jour ; astrologues impuissants | PUBLIE |
| IS165 | P165 | Is 48:14-15 · l'aimé exécutera son dessein contre Babylone | PUBLIE |
| IS166 | P166 | Is 49:1-7 · serviteur donné comme lumière des nations | PUBLIE |
| IS167 | P167 | Is 49:22-23 · les rois nourriciers de Sion restaurée | PUBLIE |
| IS168 | P168 | Is 50:4-9 · dos livré aux frappeurs ; visage non caché | PUBLIE |

## 3ac. Vague P8-29 (IS — Isaïe 12)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS169 | P169 | Is 52:7-10 · les pieds de celui qui annonce la paix | PUBLIE |
| IS170 | P170 | Is 52:13-15 · le serviteur perspicace sera élevé | PUBLIE |
| IS171 | P171 | Is 53:1-12 · méprisé, transpercé, enseveli, intercesseur | PUBLIE |
| IS172 | P172 | Is 54:1-17 · la stérile enfantera ; aucune arme | PUBLIE |
| IS173 | P173 | Is 55:3-5 · l'alliance sûre de David ; nations appelées | PUBLIE |
| IS174 | P174 | Is 56:4-8 · maison de prière pour tous les peuples | PUBLIE |

## 3ad. Vague P8-30 (IS — Isaïe 13)
| Fiche | P | Sujet | État |
|---|---|---|---|
| IS175 | P175 | Is 59:20 · le Rédempteur viendra à Sion | PUBLIE |
| IS176 | P176 | Is 60:1-22 · gloire de Sion ; richesses des nations | PUBLIE |
| IS177 | P177 | Is 61:1-3 · l'esprit m'a oint pour la bonne nouvelle | PUBLIE |
| IS178 | P178 | Is 63:1-6 · le fouleur du pressoir, vêtements tachés | PUBLIE |
| IS179 | P179 | Is 65:17-25 · nouveaux cieux ; loup et agneau | PUBLIE |
| IS180 | P180 | Is 66:15-24 · jugement par le feu ; nations prosternées | PUBLIE |

## 3ae. Vague P8-31 (JR — Jérémie 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR181 | P181 | Jr 1:13-16 · malheur du nord ; villes livrées à Babylone | PUBLIE |
| JR182 | P182 | Jr 1:17-19 · ils combattront, ne l'emporteront pas | PUBLIE |
| JR183 | P183 | Jr 2:14-19 · Israël serviteur ; mal de l'abandon | PUBLIE |
| JR184 | P184 | Jr 3:14-18 · rassemblement ; arche plus rappelée | PUBLIE |
| JR185 | P185 | Jr 4:5-8 · le lion monte ; désolation du nord | PUBLIE |
| JR186 | P186 | Jr 5:14-17 · nation lointaine mange récoltes et villes | PUBLIE |

## 3af. Vague P8-32 (JR — Jérémie 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR187 | P187 | Jr 6:1-5 · signaux de feu ; bergers et troupeaux | PUBLIE |
| JR188 | P188 | Jr 6:22-26 · peuple du nord ; angoisse du siège | PUBLIE |
| JR189 | P189 | Jr 7:1-15 · le temple ne sauvera pas ; comme Silo | PUBLIE |
| JR190 | P190 | Jr 7:30-34 · Topheth-Hinnom ; voix de joie tues | PUBLIE |
| JR191 | P191 | Jr 8:1-3 · ossements exhumés ; mort préférée | PUBLIE |
| JR192 | P192 | Jr 9:11 · tas de ruines, repaire de chacals | PUBLIE |

## 3ag. Vague P8-33 (JR — Jérémie 3)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR193 | P193 | Jr 9:15-16 · absinthe, eau empoisonnée, dispersion | PUBLIE |
| JR194 | P194 | Jr 9:25-26 · jugement sur Juda et tous ses voisins | PUBLIE |
| JR195 | P195 | Jr 10:11 · les dieux qui n'ont pas fait les cieux périront | PUBLIE |
| JR196 | P196 | Jr 11:21-23 · Anathoth : aucun reste ne subsistera | PUBLIE |
| JR197 | P197 | Jr 12:14-17 · voisins arrachés, puis rétablis s'ils apprennent | PUBLIE |
| JR198 | P198 | Jr 13:9-14 · orgueil abaissé ; cruches brisées | PUBLIE |

## 3ah. Vague P8-34 (JR — Jérémie 4)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR199 | P199 | Jr 13:18-19 · roi et reine mère abaissés ; Négev fermé | PUBLIE |
| JR200 | P200 | Jr 13:24-27 · dispersés comme la paille au vent | PUBLIE |
| JR201 | P201 | Jr 14:10-16 · épée et famine sur les faux prophètes | PUBLIE |
| JR202 | P202 | Jr 15:1-9 · Moïse et Samuel n'intercéderaient pas | PUBLIE |
| JR203 | P203 | Jr 15:11-14 · pays inconnu ; le feu s'allumera | PUBLIE |
| JR204 | P204 | Jr 16:1-9 · signes : morts par maladie, épée, famine | PUBLIE |

## 3ai. Vague P8-35 (JR — Jérémie 5)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR205 | P205 | Jr 16:10-18 · double punition, puis pêcheurs et chasseurs | PUBLIE |
| JR206 | P206 | Jr 17:3, 4 · biens pillés ; feu allumé pour toujours | PUBLIE |
| JR207 | P207 | Jr 17:19-27 · sabbat profané : feu aux portes de Jérusalem | PUBLIE |
| JR208 | P208 | Jr 18:1-12 · le potier et l'argile : malheur préparé | PUBLIE |
| JR209 | P209 | Jr 19:1-13 · la cruche brisée ; ville comme Topheth | PUBLIE |
| JR210 | P210 | Jr 20:1-6 · Pashhour mourra à Babylone | PUBLIE |


## 3aj. Vague P8-36 (JR — Jérémie 6)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR211 | P211 | Jr 21:1-10 · ville livrée ; qui sortira aura la vie sauve | PUBLIE |
| JR212 | P212 | Jr 21:11-14 · le feu dévorera la forêt du palais | PUBLIE |
| JR213 | P213 | Jr 22:1-9 · si non écoutée, cette maison deviendra ruine | PUBLIE |
| JR214 | P214 | Jr 22:10-12 · Shallum mourra en exil | PUBLIE |
| JR215 | P215 | Jr 22:13-19 · Yehoïaqim : sépulture d'un âne | PUBLIE |
| JR216 | P216 | Jr 22:20-23 · bergers emportés ; douleur à venir | PUBLIE |


## 3ak. Vague P8-37 (JR — Jérémie 7)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR217 | P217 | Jr 22:24-30 · Konia : nul descendant sur le trône | PUBLIE |
| JR218 | P218 | Jr 23:1-8 · reste rassemblé ; germe juste | PUBLIE |
| JR219 | P219 | Jr 23:9-40 · faux prophètes nourris d'absinthe | PUBLIE |
| JR220 | P220 | Jr 24:1-10 · bons et mauvais figuiers | PUBLIE |
| JR221 | P221 | Jr 25:1-11 · soixante-dix ans de servitude | PUBLIE |
| JR222 | P222 | Jr 25:12-14 · après 70 ans, Babylone punie | PUBLIE |


## 3al. Vague P8-38 (JR — Jérémie 8)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR223 | P223 | Jr 25:15-26 · coupe de fureur pour toutes les nations | PUBLIE |
| JR224 | P224 | Jr 25:27-38 · bergers hurlants ; pâturages ravagés | PUBLIE |
| JR225 | P225 | Jr 26:1-6 · maison ruine ; ville en malédiction | PUBLIE |
| JR226 | P226 | Jr 26:20-23 · Ouriya mis à mort | PUBLIE |
| JR227 | P227 | Jr 27:1-11 · servir Neboukadnetsar ou périr | PUBLIE |
| JR228 | P228 | Jr 27:16-22 · ustensiles emportés puis rapportés | PUBLIE |


## 3am. Vague P8-39 (JR — Jérémie 9)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR229 | P229 | Jr 28:1-17 · Hanania mourra cette année | PUBLIE |
| JR230 | P230 | Jr 29:1-14 · 70 ans puis retour promis | PUBLIE |
| JR231 | P231 | Jr 29:15-19 · fléaux sur les restants | PUBLIE |
| JR232 | P232 | Jr 29:20-23 · Ahab et Tsidqiya rôtis | PUBLIE |
| JR233 | P233 | Jr 29:24-32 · Shemayah sans postérité | PUBLIE |
| JR234 | P234 | Jr 30:1-11 · détresse de Jacob, délivrance | PUBLIE |


## 3an. Vague P8-40 (JR — Jérémie 10)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR235 | P235 | Jr 30:12-17 · plaie guérie, santé rendue | PUBLIE |
| JR236 | P236 | Jr 30:18-22 · ville rebâtie sur son tell | PUBLIE |
| JR237 | P237 | Jr 31:1-6 · vignes sur Samarie | PUBLIE |
| JR238 | P238 | Jr 31:7-14 · rassemblés du nord, joie | PUBLIE |
| JR239 | P239 | Jr 31:15-17 · Rachel pleure, récompense | PUBLIE |
| JR240 | P240 | Jr 31:18-22 · Éphraïm revient | PUBLIE |


## 3ao. Vague P8-41 (JR — Jérémie 11)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR241 | P241 | Jr 31:23-26 · Juda et ses villes habités | PUBLIE |
| JR242 | P242 | Jr 31:27-30 · semence ; raisins acides | PUBLIE |
| JR243 | P243 | Jr 31:31-34 · alliance nouvelle | PUBLIE |
| JR244 | P244 | Jr 31:35-37 · ordonnances, nation à jamais | PUBLIE |
| JR245 | P245 | Jr 31:38-40 · ville rebâtie, tours | PUBLIE |
| JR246 | P246 | Jr 32:1-5 · Sédécias à Babylone | PUBLIE |


## 3ap. Vague P8-42 (JR — Jérémie 12)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR247 | P247 | Jr 32:6-15 · champ d'Anatoth racheté | PUBLIE |
| JR248 | P248 | Jr 32:28-35 · ville livrée et brûlée | PUBLIE |
| JR249 | P249 | Jr 32:36-44 · rassemblés, champs rachetés | PUBLIE |
| JR250 | P250 | Jr 33:1-9 · santé, ville nom de joie | PUBLIE |
| JR251 | P251 | Jr 33:10-13 · voix de joie, troupeaux | PUBLIE |
| JR252 | P252 | Jr 33:14-16 · germe juste, justice | PUBLIE |


## 3aq. Vague P8-43 (JR — Jérémie 13)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR253 | P253 | Jr 33:17-22 · David toujours un héritier | PUBLIE |
| JR254 | P254 | Jr 33:23-26 · captifs ramenés, compassion | PUBLIE |
| JR255 | P255 | Jr 34:1-7 · Sédécias mourra en paix | PUBLIE |
| JR256 | P256 | Jr 34:8-22 · esclaves repris, ville brûlée | PUBLIE |
| JR257 | P257 | Jr 35:1-19 · Rékabites à jamais | PUBLIE |
| JR258 | P258 | Jr 36 · rouleau brûlé, réécrit augmenté | PUBLIE |


## 3ar. Vague P8-44 (JR — Jérémie 14)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR259 | P259 | Jr 37:6-10 · Égypte repart, ville brûlée | PUBLIE |
| JR260 | P260 | Jr 37:17-21 · pain jusqu'à épuisement | PUBLIE |
| JR261 | P261 | Jr 38:1-4 · qui sort vivra | PUBLIE |
| JR262 | P262 | Jr 38:14-23 · ville prise, famille livrée | PUBLIE |
| JR263 | P263 | Jr 39:15-18 · Ébed-Mélek sauvé | PUBLIE |
| JR264 | P264 | Jr 40:1-6 · Jérémie libéré, Guedalia | PUBLIE |


## 3as. Vague P8-45 (JR — Jérémie 15)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR265 | P265 | Jr 42:1-22 · restez ou mourez en Égypte | PUBLIE |
| JR266 | P266 | Jr 43:1-7 · emmenés de force en Égypte | PUBLIE |
| JR267 | P267 | Jr 43:8-13 · trône sur les pierres de Tahpanhès | PUBLIE |
| JR268 | P268 | Jr 44:1-14 · le reste en Égypte périra | PUBLIE |
| JR269 | P269 | Jr 44:15-28 · la reine du ciel, petit reste | PUBLIE |
| JR270 | P270 | Jr 44:29-30 · Hophra livré, signe | PUBLIE |


## 3at. Vague P8-46 (JR — Jérémie 16)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR271 | P271 | Jr 45:1-5 · Baruch : ta vie pour butin | PUBLIE |
| JR272 | P272 | Jr 46:2 · Karkémish, l'Égypte battue | PUBLIE |
| JR273 | P273 | Jr 46:13-26 · Nô dévastée, dieux exilés | PUBLIE |
| JR274 | P274 | Jr 46:27-28 · Jacob reviendra en sécurité | PUBLIE |
| JR275 | P275 | Jr 47:1-7 · Gaza rasée, Ashkelon dévastée | PUBLIE |
| JR276 | P276 | Jr 48 · Moab dévastée, nation supprimée | PUBLIE |


## 3au. Vague P8-47 (JR — Jérémie 17)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR277 | P277 | Jr 48:47 · Moab restaurée dans l'avenir | PUBLIE |
| JR278 | P278 | Jr 49:1-5 · Rabbah, tell désolé | PUBLIE |
| JR279 | P279 | Jr 49:7-22 · Édom comme Sodome | PUBLIE |
| JR280 | P280 | Jr 49:23-27 · Damas incendiée | PUBLIE |
| JR281 | P281 | Jr 49:28-33 · Kédar et Hatsor frappés | PUBLIE |
| JR282 | P282 | Jr 49:34-39 · Élam brisé puis rétabli | PUBLIE |


## 3av. Vague P8-48 (JR — Jérémie 18)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR283 | P283 | Jr 50:1-3 · Bel honteux, peuple du nord | PUBLIE |
| JR284 | P284 | Jr 50:9-16 · sanctuaire profané vengé | PUBLIE |
| JR285 | P285 | Jr 50:17-20 · Israël rassemblé, pardonné | PUBLIE |
| JR286 | P286 | Jr 50:33-40 · Babylone comme Sodome | PUBLIE |
| JR287 | P287 | Jr 50:41-46 · nul ne tiendra devant lui | PUBLIE |
| JR288 | P288 | Jr 51:1-14 · la coupe d'or brisée | PUBLIE |


## 3aw. Vague P8-49 (JR — Jérémie 19)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR289 | P289 | Jr 51:24-26 · jamais rebâtie, nulle pierre | PUBLIE |
| JR290 | P290 | Jr 51:27-33 · Ararat/Minni/Ashkenaz, gués saisis | PUBLIE |
| JR291 | P291 | Jr 51:34-44 · dévorée, eaux asséchées, dieux jugés | PUBLIE |
| JR292 | P292 | Jr 51:45-48 · sortez du milieu d'elle | PUBLIE |
| JR293 | P293 | Jr 51:49-58 · murailles tombées, portes brûlées | PUBLIE |
| JR294 | P294 | Jr 51:59-64 · le rouleau dans l'Euphrate | PUBLIE |


## 3ax. Vague P8-50 (JR+LM — Jérémie 20 + Lamentations 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JR295 | P295 | Jr 52:7-11 · Tsidqiya capturé, aveuglé | PUBLIE |
| JR296 | P296 | Jr 52:12-27 · Temple brûlé, murs rasés, Ribla | PUBLIE |
| LM297 | P297 | Lm 1:1-5 · assise solitaire, adversaires chefs | PUBLIE |
| LM298 | P298 | Lm 2:15-17 · passants, Jéhovah a exécuté | PUBLIE |
| LM299 | P299 | Lm 4:21-22 · Édom : la coupe passera | PUBLIE |
| LM300 | P300 | Lm 5:19-22 · rétablis-nous, Jéhovah | PUBLIE |


## 3ay. Vague P8-51 (EZ — Ézéchiel 1)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ301 | P301 | Éz 2:3-5 · maison rebelle, un prophète au milieu | PUBLIE |
| EZ302 | P302 | Éz 3:4-11 · front dur, ils n'écouteront pas | PUBLIE |
| EZ303 | P303 | Éz 3:22-27 · langue attachée, muet | PUBLIE |
| EZ304 | P304 | Éz 4:1-8 · siège mimé : 390 + 40 jours | PUBLIE |
| EZ305 | P305 | Éz 4:9-17 · pain au poids, eau avec effroi | PUBLIE |
| EZ306 | P306 | Éz 5:1-17 · tiers peste, tiers épée, tiers dispersé | PUBLIE |


## 3az. Vague P8-52 (EZ — Ézéchiel 2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ307 | P307 | Éz 6:1-14 · hauts lieux désolés, autels ravagés | PUBLIE |
| EZ308 | P308 | Éz 7:1-27 · la fin est venue, or inutile | PUBLIE |
| EZ309 | P309 | Éz 8:1-18 · abominations du Temple, fureur | PUBLIE |
| EZ310 | P310 | Éz 9:1-11 · signe au front, six hommes | PUBLIE |
| EZ311 | P311 | Éz 10:18-19 ; 11:22-23 · la gloire quitte | PUBLIE |
| EZ312 | P312 | Éz 11:1-13 · Pelatya meurt | PUBLIE |


## 3ba. Vague P8-53 (EZ — Ézéchiel 3)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ313 | P313 | Éz 11:16-21 · sanctuaire en exil, rassemblement | PUBLIE |
| EZ314 | P314 | Éz 12:1-16 · le prince part, il ne verra pas | PUBLIE |
| EZ315 | P315 | Éz 12:17-20 · manger avec tremblement | PUBLIE |
| EZ316 | P316 | Éz 12:21-28 · plus de délai | PUBLIE |
| EZ317 | P317 | Éz 13:1-23 · faux prophètes, mur badigeonné | PUBLIE |
| EZ318 | P318 | Éz 14:1-11 · idoles dressées sur le cœur | PUBLIE |


## 3bb. Vague P8-54 (EZ — Ézéchiel 4)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ319 | P319 | Éz 14:12-23 · quatre jugements, un reste survivra | PUBLIE |
| EZ320 | P320 | Éz 15:1-8 · la vigne livrée au feu | PUBLIE |
| EZ321 | P321 | Éz 16:1-58 · Jérusalem dépouillée, lapidée, brûlée | PUBLIE |
| EZ322 | P322 | Éz 16:59-63 · alliance permanente (Accomplie/À venir) | PUBLIE |
| EZ323 | P323 | Éz 17:1-24 · Sédécias emmené, jeune pousse plantée | PUBLIE |
| EZ324 | P324 | Éz 18:1-32 · l'âme qui pèche mourra | PUBLIE |


## 3bc. Vague P8-55 (EZ — Ézéchiel 5)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ325 | P325 | Éz 19:1-14 · lionceaux pris, vigne arrachée | PUBLIE |
| EZ326 | P326 | Éz 20:1-38 · rebelles exclus, rassemblement | PUBLIE |
| EZ327 | P327 | Éz 20:45-49 · feu dans la forêt du sud | PUBLIE |
| EZ328 | P328 | Éz 21:1-32 · l'épée, la croisée des chemins | PUBLIE |
| EZ329 | P329 | Éz 22:1-31 · le creuset, la brèche vide | PUBLIE |
| EZ330 | P330 | Éz 23:1-49 · Oholah et Oholibah jugées | PUBLIE |


## 3bd. Vague P8-56 (EZ — Ézéchiel 6)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ331 | P331 | Éz 24:1-14 · la marmite rouillée | PUBLIE |
| EZ332 | P332 | Éz 24:15-27 · la mort de sa femme, signe | PUBLIE |
| EZ333 | P333 | Éz 25:1-7 · Ammon livrée, Rabbah pâturage | PUBLIE |
| EZ334 | P334 | Éz 25:8-11 · Moab et Séir donnés | PUBLIE |
| EZ335 | P335 | Éz 25:12-14 · Édom, main étendue | PUBLIE |
| EZ336 | P336 | Éz 25:15-17 · Philistins retranchés | PUBLIE |


## 3be. Vague P8-57 (EZ — Ézéchiel 7)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ337 | P337 | Éz 26:1-6 · Tyr raclée, lieu pour les filets | PUBLIE |
| EZ338 | P338 | Éz 26:7-11 · Neboukadnetsar assiègera Tyr | PUBLIE |
| EZ339 | P339 | Éz 26:12-14 · pierres et poussière dans l'eau | PUBLIE |
| EZ340 | P340 | Éz 26:15-21 · les îles tremblent, fosse | PUBLIE |
| EZ341 | P341 | Éz 27:1-36 · lamentation sur Tyr marchande | PUBLIE |
| EZ342 | P342 | Éz 28:1-19 · le chef de Tyr mis à mort | PUBLIE |


## 3bf. Vague P8-58 (EZ — Ézéchiel 8)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ343 | P343 | Éz 28:20-24 · Sidon : peste, sang, épée | PUBLIE |
| EZ344 | P344 | Éz 28:25-26 · Israël rassemblé, en sécurité | PUBLIE |
| EZ345 | P345 | Éz 29:1-16 · Égypte dévastée 40 ans | PUBLIE |
| EZ346 | P346 | Éz 29:17-21 · l'Égypte, salaire de Tyr | PUBLIE |
| EZ347 | P347 | Éz 30:1-19 · jour de Jéhovah sur l'Égypte | PUBLIE |
| EZ348 | P348 | Éz 30:20-26 · bras de Pharaon brisé | PUBLIE |


## 3bg. Vague P8-59 (EZ — Ézéchiel 9)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ349 | P349 | Éz 31:1-18 · Pharaon, cèdre abattu | PUBLIE |
| EZ350 | P350 | Éz 32:1-16 · monstre capturé, terre arrosée | PUBLIE |
| EZ351 | P351 | Éz 32:17-32 · l'Égypte dans la fosse | PUBLIE |
| EZ352 | P352 | Éz 33:1-20 · le guetteur et sa charge | PUBLIE |
| EZ353 | P353 | Éz 33:21-29 · le fugitif : ville frappée | PUBLIE |
| EZ354 | P354 | Éz 33:30-33 · un prophète parmi eux | PUBLIE |


## 3bh. Vague P8-60 (EZ — Ézéchiel 10)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ355 | P355 | Éz 34:1-31 · bergers jugés, David berger | PUBLIE |
| EZ356 | P356 | Éz 35:1-15 · mont Séir en désolation | PUBLIE |
| EZ357 | P357 | Éz 36:1-38 · rassemblés, ruines rebâties | PUBLIE |
| EZ358 | P358 | Éz 37:1-14 · ossements desséchés revivent | PUBLIE |
| EZ359 | P359 | Éz 37:15-28 · deux bois réunis, un roi | PUBLIE |
| EZ360 | P360 | Éz 38:1-23 · Gog de Magog jugé | PUBLIE |


## 3bi. Vague P8-61 (EZ — Ézéchiel 11)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ361 | P361 | Éz 39:1-20 · Gog tombe, festin des oiseaux | PUBLIE |
| EZ362 | P362 | Éz 39:11-16 · sept mois d'ensevelissement | PUBLIE |
| EZ363 | P363 | Éz 39:21-29 · Israël rassemblé, face révélée | PUBLIE |
| EZ364 | P364 | Éz 40-48 · le temple visionnaire mesuré | PUBLIE |
| EZ365 | P365 | Éz 43:1-12 · la gloire revient, loi de la maison | PUBLIE |
| EZ366 | P366 | Éz 47:1-12 · la rivière guérit la mer morte | PUBLIE |


## 3bj. Vague P8-62 (EZ/DN — transition : Shammah + Daniel 1-2)
| Fiche | P | Sujet | État |
|---|---|---|---|
| EZ367 | P367 | Éz 48:35 · Jéhovah-Shammah, nom de la ville | PUBLIE |
| DN368 | P368 | Dn 1:1-7 · ustensiles emportés, jeunes déportés | PUBLIE |
| DN369 | P369 | Dn 1:17-21 · Daniel jusqu'à Cyrus an 1 | PUBLIE |
| DN370 | P370 | Dn 2:1-43 · la statue aux quatre métaux | PUBLIE |
| DN371 | P371 | Dn 2:34-45 · la pierre, le royaume indestructible | PUBLIE |
| DN372 | P372 | Dn 4:10-27 · l'arbre abattu, sept temps | PUBLIE |


## 4. Journal
- 2026-09-25 : création phase 8 (workflow + états + builder) ; vague P8-1 ouverte.
- 2026-09-25 : vague P8-1 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3, 0 lien mort ; `theme.intros` : règle exactitude-d'abord (rebuild phase 7 à prévoir en maintenance).
- 2026-09-25 : vague P8-2 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (1 image régénérée après modération).
- 2026-09-25 : vague P8-3 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (1 image retry après glitch modèle).
- 2026-09-25 : vague P8-4 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (1 image retry après glitch modèle).
- 2026-09-25 : vague P8-5 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios du 1er coup).
- 2026-09-25 : vague P8-6 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios du 1er coup).
- 2026-09-25 : vague P8-7 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (transition Genèse→Exode ; 6/6 images et 6/6 audios du 1er coup).
- 2026-09-25 : vague P8-8 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3 (nouvelle catégorie EX : 7/7 images et 7/7 audios du 1er coup), 0 lien mort.
- 2026-09-25 : vague P8-9 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios du 1er coup ; couv + intro EX réutilisées).
- 2026-09-25 : vague P8-10 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3 (nouvelle catégorie DT : 7/7 images et 7/7 audios du 1er coup), 0 lien mort.
- 2026-09-25 : vague P8-11 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios du 1er coup ; couv + intro DT réutilisées).
- 2026-09-25 : vague P8-12 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3 (nouvelle catégorie SM : 7/7 audios du 1er coup ; 1 image retry après modération), 0 lien mort.
- 2026-09-25 : vague P8-13 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3 (nouvelle catégorie RO : 7/7 images du 1er coup ; 1 audio retry après modération), 0 lien mort.
- 2026-09-25 : vague P8-14 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images du 1er coup ; 1 audio retry après modération ; couv + intro RO réutilisées).
- 2026-09-25 : vague P8-15 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios du 1er coup ; couv + intro RO réutilisées).
- 2026-09-25 : vague P8-16 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (5/6 images du 1er coup, 1 retry modération ; 6/6 audios du 1er coup ; couv + intro RO réutilisées).
- 2026-09-25 : vague P8-17 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3, 0 lien mort (7/7 images et 7/7 audios du 1er coup ; vague mixte RO+CH ; nouvelle catégorie CH : couv + intro créées).
- 2026-09-25 : PURGE médias sur demande (workspace téléchargé) — 385 JPG/MP3 supprimés ; projet 118 Mo → 22 Mo ; pages antérieures déréférencées, compteurs phase 8 = créations cumulées.
- 2026-09-25 : vague P8-18 LIVRÉE — 6/6 PUBLIE, 9 JPG, 10 MP3, 0 lien mort (9/9 images et 10/10 audios du 1er coup ; vague mixte 4 livres CH+ED+NE+IS ; nouvelles catégories ED, NE, IS : couvs + intros créées ; intro CH régénérée).
- 2026-09-25 : vague P8-24 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; 3 slugs audio/image realignés ; couv + intro IS réutilisées ; 97 428 o).
- 2026-09-25 : vague P8-25 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; 2 sources non officielles remplacées par wol ; couv + intro IS réutilisées ; 91 176 o).
- 2026-09-25 : vague P8-26 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; build sans warning ; couv + intro IS réutilisées ; 91 694 o).
- 2026-09-25 : vague P8-27 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : 7 recherches, réassignation par contenu ; couv + intro IS réutilisées ; 91 439 o).
- 2026-09-25 : vague P8-28 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : réassignation par contenu, 0 doublon source ; couv + intro IS réutilisées ; 92 716 o).
- 2026-09-25 : vague P8-29 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : rotation totale + 1 complément IS173, réassignation par contenu ; S3 : module réécrit au format 11 blocs après 1er jet non conforme ; build 1er coup ; couv + intro IS réutilisées ; 85 081 o).
- 2026-09-25 : vague P8-30 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : 3 requêtes sans résultat officiel, patterns wol sûrs ; S3 : 2 coquilles dont 1 cyrillique ; build 1er coup ; couv + intro IS réutilisées ; 83 806 o ; cap P180 atteint).
- 2026-09-25 : vague P8-31 LIVRÉE — 6/6 PUBLIE, 7 JPG, 7 MP3, 0 lien mort (7/7 images du 1er coup ; 6/7 audios voice-01 du 1er coup, JR183 retry 3e personne ; S2 : rotation croisée req3↔req4 ; nouvelle catégorie JR : couv + intro créées ; build 1er coup ; 81 762 o).
- 2026-09-25 : vague P8-32 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : retours décalés, forum TJ repéré non citable, 2 requêtes sans officiel ; S3 : 6 coquilles casse ; build 1er coup ; couv + intro JR réutilisées ; 81 379 o).
- 2026-09-25 : vague P8-33 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images du 1er coup ; 5/6 audios voice-01 du 1er coup, JR196 retry distancié ; S2 : 2 requêtes sans officiel, nwtsty 24/9 non réutilisé ; S3 : 7 coquilles ; build 1er coup ; couv + intro JR réutilisées ; 81 525 o).
- 2026-09-25 : vague P8-34 LIVRÉE — 6/6 PUBLIE (JR199–JR204, Jr 13–16), FICHES8_JEREMIE_4.html 69 Ko, 6 JPG + 6 MP3 1er coup (95 s, moy 15,8 s), 18 sources wol/jw.org, 0 doublon ; coquille HEGlah corrigée ; accomplissement converti en tuples (build).
- 2026-09-25 : vague P8-35 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images du 1er coup ; 5/6 audios voice-01 du 1er coup, JR210 retry distancié ; S2 : nwtsty 24/16 + Rbi8 24/17 déjà pris → patterns ; S3 : 0 coquille ; build 1er coup ; couv + intro JR réutilisées ; 71 806 o).
- 2026-09-25 : vague P8-36 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : nwtsty 24/22 déjà pris (p8_deu2) → nwtsty 24/38 ; S3 : 2 O cyrilliques YEHОAHAZ corrigés ; build 1er coup ; couv + intro JR réutilisées ; 73 Ko).
- 2026-09-25 : vague P8-37 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : Rbi8 24/23 pris (JR216) + 2011736 pris → patterns ; hits : QdL Jr 22:30, Yehoïakîn, Anneau, Berger royal, fruits, 70 ans, prophéties réalisées ; S3 : 1 coquille HAGGoy ; build 1er coup ; couv + intro JR réutilisées ; 74 Ko).
- 2026-09-25 : vague P8-38 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : tout Jr 25 pris + 1101990085/nwt 24/26/1101963018/nwt 15/1 pris → patterns Jr 26/27/28/46/48/49, Ps 78, Esd 1/5 ; S3 : 1 O cyrillique ADMATО + BRVÉ→HORREUR ; build 1er coup ; couv + intro JR réutilisées ; 77 Ko).
- 2026-09-25 : vague P8-39 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : tout Jr 28 pris + 1200001853 pris → Jr 14 ; nwtsty 24/29 pris (JR219) → nwt/Rbi8 24/29 ; 2007202/nwtsty 24/31/nwt 12/10 pris → Rbi8 12/10 ; hits : jw.org EN Jr 29:11, Tsidqiya, Ahab ; S3 : 0 cyrillique ; build 1er coup (syntaxe p8_jr9 + out absolu) ; couv + intro JR réutilisées ; 81 Ko ; audio 171 s).
- 2026-09-25 : vague P8-40 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : Jr 30+31 entièrement pris (3 bibles) + 1001060027 pris → patterns Ex 15, Os 6/11/14, Né 3, Is 43/44/65, Am 9, Dt 30 ; hits : QdL Rachel 402014927 + étude Rachel 1200003621 + Rbi8 Mt 2 ; S3 : 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 76 Ko ; audio 184 s).
- 2026-09-25 : vague P8-41 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : Jr 32 entièrement libre (triplet JR246) ; nwt 24/33 pris → Rbi8 24/33 ; hits : 1998085 + 1101986084 (alliance nouvelle) ; patterns Esd 2, Né 7/12, Éz 18, Dt 24, Gn 1, Ps 89, Za 14, Hé 8 ; S3 : 2 coquilles (NOMAdes, PA youre) ; 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 74 Ko ; audio 185 s).
- 2026-09-25 : vague P8-42 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : Jr 33 entièrement pris + 2R 25 + 2Ch 36 + Jr 23 + Esd 1 pris → patterns Lv 25, Rt 4, Jr 39/52, Né 11/12, Ps 126, Éz 36, Esd 3, Lc 1, Za 6 ; 0 hit wol FR direct ; S3 : 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 79 Ko ; audio 189 s).
- 2026-09-25 : vague P8-43 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (6/6 images et 6/6 audios voice-01 du 1er coup ; S2 : hits Récabites 1200013576 + libération 1979889 + amitiés 2019640 ; nwt+Rbi8 24/34 pris → nwtsty ; Jr 35 libre (triplet) ; nwt 24/36 pris → Rbi8+nwtsty ; patterns 2S 7, Hé 7, Dt 30/15, Éz 39, 2Ch 16/21 ; S3 : 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 83 Ko ; audio 183 s).
- 2026-09-25 : vague P8-44 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (5/6 images du 1er coup, JR259 retry prompt adouci ; 6/6 audios voice-01 du 1er coup ; S2 : hits Ébed-Mélek 2007085 + 1200001247 + guedalia 1200000787 ; nwt+nwtsty 24/38, nwt 23/31, Jr 21, nwt 24/27, nwt 12/24 pris → patterns ; Jr 37/38/40/42 libres (triplets JR259-262/264) ; S3 : 6 coquilles casse corrigées, 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 78 Ko ; audio 130 s).
- 2026-09-25 : vague P8-45 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 0 lien mort (5/6 images du 1er coup, JR270 retry trône vide ; 6/6 audios voice-01 du 1er coup ; S2 : hits 1980165 (Baruch) + 1956361 (reine du ciel) + 1200012020 (Hophra) ; nwt+rbi8 24/42 + nwtsty 24/46 pris → patterns ; Jr 43/44/46 + Éz 29/30/32 + Is 30 + Jr 7 libres ; S3 : 0 coquille, 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 88 Ko ; audio 132 s).
- 2026-09-25 : AUDIT LIENS phase 8 — 173 liens Bible jr4→jr15 réparés (format `/wol/b/nwt/` → `/wol/b/r30/lp-f/nwt/`, `rbi8` → `Rbi8`, livre 34 → 26 Ézéchiel) + 7 remplacements ciblés (JR200 Am 9, JR204/JR205 Éz 47, JR206 Dt 28, JR207 Jr 17, JR267 Éz 29, JR269 Éz 8 ×2) ; 173/173 curl 200 ; 12 HTML JEREMIE_4→15 synchronisés. Dette restante : ~37 doublons historiques préexistants dans les vagues antérieures (ex : nwtsty/1/49 ×11) — maintenance dédiée à prévoir. Règle batteries : pattern `lp-f/TRAD/L/C`.
- 2026-09-25 : vague P8-46 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 18/18 curl 200 (5/6 images du 1er coup, JR272 retry ; 6/6 audios voice-01 du 1er coup ; S2 : hit Kémosh 1200000936 ; 2R 24 + Esd 1 pris 3 trads → 2Ch 35 + Is 45 ; Na 3 + Éz 30 (Nô) ; So 2 + Jr 47 + Am 1 ; Jr 48 nwtsty + Is 15 ; S3 : 2 coquilles, 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 89 Ko ; audio 138 s).
- 2026-09-25 : vague P8-47 LIVRÉE — 6/6 PUBLIE, 6 JPG, 6 MP3, 18/18 curl 200 (5/6 images du 1er coup, JR281 retry ; 5/6 audios du 1er coup, JR281 retry adouci ; S2 : 0 hit wol FR → 100% patterns (Jr 49 ×2, Am 1 ×2, Éz 25/27, Is 16/17/21/34, So 2 ×2, Ab 1, Za 9, Ps 120, Dn 8, Ac 2, Gn 14) ; statuts : 4 Accomplie + 1 À venir + 1 mixte ; S3 : 5 coquilles + 1 caractère non-ASCII, 0 cyrillique ; build 1er coup ; couv + intro JR réutilisées ; 83 Ko ; audio 133 s).

## Journal — P8-48 (JR283–JR288, Jr 50–51, Babylone jugée)
- S1 : registre L141-146 (6× Accomplie) ; §3av + workflow appendés.
- S2 : 6 web_search (1 hit FR 1101963014 Bel/Merodak) ; ~29 URL grep, 0 doublon ; 18/18 curl 200.
- S3 : data/p8_jr18.py (48 808 o, CAT + 6 fiches) ; coquilles corrigées inline ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 82 Ko (déplacé dans preuves/, builder écrit au parent).
- S5 : 6/6 JPG 1er coup (bel/nord/pardon/sodome/peuple/coupe).
- S6 : 6/6 MP3 voice-01 1er coup (0 impératif violent).
- S7 : rebuild 84 Ko ; durées 18.4/16.9/17.7/17.6/18.1/17.8 = 106.4 s.
- S8 : §3av 6/6 PUBLIE → **288/1000** ; 298 JPG créés (190 présents), 299 MP3 (191 pistes, 64,8 min).

## Journal — P8-49 (JR289–JR294, Jr 51:24-64, fin Babylone)
- S1 : registre L147-152 (6× Accomplie, P292 = 1er accomplissement) ; §3aw + workflow appendés.
- S2 : 6 web_search (4 hits FR : 1101963015 nulle pierre+Séraja, 1200000423 Ashkenaz, 1967361 antitype, 1101990085 doublon jr5 écarté) ; 3 batteries grep (~40 URL, 17 doublons anciens écartés) ; 18/18 curl 200 (nwt/11/36 → 400, corrigé : 2Ch=14, Esd=15, Ne=16).
- S3 : data/p8_jr19.py (51 513 o, CAT + 6 fiches) ; coquilles corrigées inline ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 84 Ko (déplacé dans preuves/).
- S5 : 6/6 JPG 1er coup (pierre/ararat/devoree/sortez/murailles/rouleau).
- S6 : 6/6 MP3 voice-01 1er coup (subjonctif « que le peuple sorte », 0 impératif).
- S7 : rebuild 86 Ko ; durées 18.4/17.0/17.3/15.8/16.4/18.4 = 103.3 s.
- S8 : §3aw 6/6 PUBLIE → **294/1000** ; 304 JPG créés (196 présents), 305 MP3 (197 pistes, 66,5 min).

## Journal — P8-50 (JR295–JR296 + LM297–LM300, mixte JR+LM, cap 300)
- S1 : registre L153-154 (Jr 52) + L161-164 (Lm) ; §3ax + workflow (modèle mixte RO+CH : code JR+LM, sans couv).
- S2 : 6 web_search (6 hits FR : nwtsty/24/52, 1200014580 Sédécias, nwtsty/12/25, 1200012382 doublon écarté, Rbi8/25/4 doublon jr14 écarté, d/1001060028) ; 3 batteries grep (~50 URL, ~25 doublons anciens) ; 18/18 curl 200.
- S3 : data/p8_jr20lm1.py (48 425 o) ; coquilles inline (LeFFACEMENT, REVient) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 81 Ko (déplacé dans preuves/).
- S5 : 6/6 JPG 1er coup (tsidqiya/temple/solitaire/passants/edom/retablis).
- S6 : 6/6 MP3 voice-01 1er coup (récit 3e pers. adouci pour Ribla).
- S7 : rebuild 83 Ko ; durées 17.7/19.7/17.3/17.0/18.3/17.3 = 107.4 s.
- S8 : §3ax 6/6 PUBLIE → **300/1000** ; 310 JPG créés (202 présents), 311 MP3 (203 pistes, 68,3 min).

## Journal — P8-51 (EZ301–EZ306, Éz 2-5, nouveau livre EZ)
- S1 : registre L176-181 (6× Accomplie) ; §3ay + workflow (modèle is2 : CAT sans couv, vague P8-51).
- S2 : 6 web_search (5 hits FR : nwtsty/26/2, Rbi8/26/3, nwtsty/26/3, nwtsty/26/4, d/1001060029, d/1200001132 JOUR) ; 2 batteries grep (~35 URL, Éz 2/3/4 nwt+Rbi8 déjà pris, report via Za 7 et Éz 24/33) ; 18/18 curl 200.
- S3 : data/p8_ez1.py (56 666 o) ; coquilles inline (TERRESS→TERRIFIÉ, PÉrira, OPProbre, BIKHNAPhÉKHA) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 88 Ko (déplacé dans preuves/).
- S5 : 6/6 JPG 1er coup (rebelle/front/muet/siege390/pain/tiers).
- S6 : 6/6 MP3 voice-01 1er coup (EZ306 sans cru explicite).
- S7 : rebuild 90 Ko ; durées 16.9/15.6/14.9/14.4/15.6/16.2 = 93.5 s.
- S8 : §3ay 6/6 PUBLIE → **306/1000** ; 316 JPG créés (208 présents), 317 MP3 (209 pistes, 69,9 min).

## Journal — P8-52 (EZ307–EZ312, Éz 6-11, fin/abominations/gloire)
- S1 : registre L182-187 (6× Accomplie, P310 = 1er accomplissement) ; §3az + workflow.
- S2 : 6 web_search (4 hits FR : 1101971007 Éz 6, nwtsty/26/7, 1964805+ nwtsty/26/8) ; 3 batteries grep (~25 URL, 4 doublons) ; 18/18 curl 200.
- S3 : data/p8_ez2.py (62 819 o) ; coquilles inline (SYNC RÉTISME, SOUPirent, TOMBERez×2) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 93 Ko (déplacé dans preuves/).
- S5 : 6/6 JPG 1er coup (hauts/fin/abominations/signe/gloire/pelatya).
- S6 : 5/6 MP3 1er coup + retry EZ310 adouci (« le jugement s'exécute », sans « frapper ») → 6/6.
- S7 : rebuild 95 Ko ; durées 16.9/15.2/16.1/14.9/15.4/15.7 = 94.3 s.
- S8 : §3az 6/6 PUBLIE → **312/1000** ; 322 JPG créés (214 présents), 323 MP3 (215 pistes, 71,5 min).
## Journal — P8-53 (EZ313–EZ318, Éz 11-14, sanctuaire/prince/faux)
- S1 : registre L188-193 (6× Accomplie) ; §3ba + workflow.
- S2 : 6 web_search (1 hit wol FR : nwtsty/26/13) ; 3 batteries grep (~51 patterns, ~32 rejets : Éz 11/12/2R 25/Jr 39/Jr 52 pris, Rbi8/24/1+nwtsty/24/1×5) ; 18/18 curl 200.
- S3 : data/p8_ez3.py (57 712 o) ; coquilles (ALL IANCE, YO_YAKIN, DÉSolation×2, AIL LEURS) ; tokens doublons recalés (SOURIS→MUSARAIGNE, 612/592→SIXIÈME-ANNÉE) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 89 Ko (direct preuves/).
- S5 : 6/6 JPG 1er coup (sanctuaire/prince/tremblement/delai/faux/idoles).
- S6 : 6/6 MP3 1er coup (récit indirect, 0 verbe de frappe).
- S7 : reg EZ317 recalé (Éz 13:23 ajouté) ; rebuild 91 Ko ; durées 17.6/15.2/14.0/12.4/13.0/13.1 = 85.3 s.
- S8 : §3ba 6/6 PUBLIE → **318/1000** ; 328 JPG créés (6 présents), 329 MP3 (6 pistes, 85,3 s) ; §3bb P8-54 ouvert (EZ4, P319–P324).
## Journal — P8-54 (EZ319–EZ324, Éz 14-18, jugements/vigne/alliance)
- S1 : registre L194-199 (5× Accomplie + P322 mixte) ; §3bb + workflow.
- S2 : 6 web_search (3 hits wol FR : 1957725 Noé/Daniel/Job, 1967246 + 1989280 prostituée) ; 4 batteries grep (~46 patterns, Jr 15/21/24/31, Is 5, 2R 24 pris) ; 2 URL malformées par moi (préfixe b/ sur d/) re-testées 200 ; 18/18 curl 200.
- S3 : data/p8_ez4.py (69 328 o) ; coquilles (VERMOUlU, MOQUIS, SABbATIQUE, ALLiance, FLOttE, AUJOURD…HUI, CADette, BANNEŠÉKH, YÈS…) ; tokens recalés (NÉSHER→RAPACE-IMPÉRIAL, QADIM→VENT-ORIENT) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 106 Ko (direct preuves/).
- S5 : 6/6 JPG 1er coup (jugements/vigne/prostituee/alliance/aigles/ame).
- S6 : 6/6 MP3 1er coup (récit indirect).
- S7 : mutagen réinstallé (non persisté) ; glob EZ32* avait raté EZ319 → correctif ; rebuild 108 Ko ; durées 15.5/16.7/13.7/13.1/13.1/13.5 = 85.6 s.
- S8 : §3bb 6/6 PUBLIE → **324/1000** ; 334 JPG créés (12 présents), 335 MP3 (12 pistes, 85,3 + 85,6 s) ; §3bc P8-55 ouvert (EZ5, P325–P330).
## Journal — P8-55 (EZ325–EZ330, Éz 19-23, princes/creuset/sœurs)
- S1 : registre L200-205 (6× Accomplie) ; §3bc + workflow.
- S2 : 6 web_search (0 hit wol FR → 100% patterns) ; 3 batteries grep (~40 patterns, Jr 22/31, Is 5, 2R 24 pris) ; 18/18 curl 200.
- S3 : data/p8_ez5.py (75 718 o, record) ; coquilles (HOUlETTE, INSTRuITES, RONgÉS) ; tokens recalés (TÉMAN→TÉMAN-SUD, QÉSÉM→QÉSÉM-SORT, SHASHAR→SHASHAR-ROUGE, VENT-ORIENT→QADIM-BRÛLANT ; double-suffixe TÉMAN-SUD-SUD corrigé) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 115 Ko (direct preuves/).
- S5 : 6/6 JPG 1er coup (lionceaux/rebelles/foret/epee/creuset/soeurs).
- S6 : 6/6 MP3 1er coup (récit indirect).
- S7 : rebuild 117 Ko ; durées 12.4/13.6/14.2/12.0/12.1/14.6 = 78.9 s.
- S8 : §3bc 6/6 PUBLIE → **330/1000** ; 340 JPG créés (18 présents), 341 MP3 (18 pistes, 85,3 + 85,6 + 78,9 s) ; §3bd P8-56 ouvert (EZ6, P331–P336).
## Journal — P8-56 (EZ331–EZ336, Éz 24-25, marmite/nations)
- S1 : registre L206-216 (6 lignes exactes, 6× Accomplie, § transition Éz 25-48) ; §3bd + workflow.
- S2 : 6 web_search (0 hit wol FR → 100% patterns) ; 5 batteries grep ; chapitres 3-trads épuisés (Jr 6/16/48/49, Am 1, So 2, Ab 1) ; 18/18 curl 200.
- S3 : data/p8_ez6.py (59 136 o) ; coquilles (MARmite, LAMENTeRAS, MAHmAD, VAA DABBÉR, BA ÉRÉB, AMAtsIA, JUDAïSÉE) ; 2× cwd /home/user (heredoc relancé phase8) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 95 Ko (sorti ../, replacé preuves/).
- S5 : 7/7 JPG 1er coup (marmite/veuve/ammon/moab/edom/philistins + vignette) ; sortis /home/user/preuves/, déplacés.
- S6 : 6/6 MP3 1er coup (voice-02, récit indirect) ; renommés fiche_* ; durées 25.7/28.7/22.1/25.8/27.4/25.3 = 155.0 s ; durations.json → 64 entrées.
- S7 : rebuild 95 Ko (36 liens wol = 18×2, 6 audio, 13 img) ; purge P8-53 (EZ313-318).
- S8 : §3bd 6/6 PUBLIE → **336/1000** ; 347 JPG créés (19 présents), 347 MP3 (18 pistes, 85,3 + 85,6 + 78,9 + 155,0 s) ; §3be P8-57 ouvert (EZ7, P337–P342, Tyr).
## Journal — P8-57 (EZ337–EZ342, Éz 26-28, Tyr)
- S1 : registre L217-222 (6 lignes exactes, 6× Accomplie) ; §3be + workflow.
- S2 : 6 web_search (3 hits wol EN : Tyr, 2 TG ; BPC 671, preceptaustin, apologetics, Arrien, CEREGE) ; 5 batteries grep ; chapitres 3-trads épuisés (Jr 25/50/51, Dn 5, Ap 18, Ha 2) ; 18/18 curl 200.
- S3 : data/p8_ez7.py (86 498 o, record) ; coquilles (ÉLÈvera, LÈvera, VESHAphAKH, SOLeLAH, ASSYrie, FAillite, NAPhALU, OU BLIÉE, TREMBlENT, RECOMMenCENT, VATTOmÉR, KElÉB, OP PROBRE, TITTÉKHA) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 124 Ko (record ; sorti ../, replacé preuves/).
- S5 : 7/7 JPG 1er coup (chemins absolus OK).
- S6 : 6/6 MP3 1er coup (voice-03) ; durées 27.0/26.5/31.7/27.1/30.6/29.0 = 171.9 s ; durations.json → 70 entrées.
- S7 : rebuild 124 Ko (36 liens wol = 18×2, 6 audio, 13 img) ; purge P8-54 : pattern EZ3[12] a mordu P8-55 (EZ325-329) → 5 JPG régénérés ; fenêtre restaurée (19 JPG + 18 MP3).
- S8 : §3be 6/6 PUBLIE → **342/1000** ; 359 JPG créés (19 présents, dont 5 régén.), 353 MP3 (18 pistes, 78,9 + 155,0 + 171,9 s) ; §3bf P8-58 ouvert (EZ8, P343–P348, Sidon+Égypte).
## Journal — P8-58 (EZ343–EZ348, Éz 28-30, Sidon/Égypte)
- S1 : registre L223-228 (6 lignes exactes, 6× Accomplie) ; §3bf + workflow.
- S2 : 6 web_search (1 hit wol FR : aperçu Éz 28 ; registre cour babylonien, tablette 568/567 British, Britannica, KUB incertain) ; 6 batteries grep ; chapitres 3-trads épuisés (Is 11/19/45, Jr 30/31/43/44/46, Éz 17/36, Na 3, Esd 1, Jl 3) ; 18/18 curl 200.
- S3 : data/p8_ez8.py (123 080 o, record absolu) ; coquilles (TRANSp…×2, ÉLÈvera, FAillite, LOuxor, UTOTPIE, DIVIN-pathétique, REViennent, HAHazaQAH) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 161 Ko (record ; sorti ../, replacé preuves/).
- S5 : 5/7 1er coup + 2 bloquées modération (sang/gémissement) → régénérées adoucies ; chemins absolus OK.
- S6 : 6/6 MP3 1er coup (voice-04) ; durées 21.2/22.9/23.2/22.3/25.4/21.9 = 136.9 s ; durations.json → 76 entrées.
- S7 : rebuild 161 Ko (36 liens wol = 18×2, 6 audio, 13 img) ; purge P8-55 patterns précis (leçon P8-57) + vignette EZ7 → fenêtre exacte (19 JPG + 18 MP3).
- S8 : §3bf 6/6 PUBLIE → **348/1000** ; 366 JPG créés (19 présents), 359 MP3 (18 pistes, 155,0 + 171,9 + 136,9 s) ; §3bg P8-59 ouvert (EZ9, P349–P354, cèdre/guetteur).
## Journal — P8-59 (EZ349–EZ354, Éz 31-33, cèdre/fosse/guetteur)
- S1 : registre L229-234 (P349 Accomplie, P350 Accomplie, P351 Accomp/À venir, P352 Accomp-déclaration 33:6-7, P353 Accomplie, P354 Accomplie) ; §3bg + workflow.
- S2 : 6 web_search (0 hit wol FR direct ; séculiers riches) ; 5 batteries grep + 1 remplacement (Jl 4 = 400 en nwt → Am 8 Rbi8) ; chapitres 3-trads épuisés (Is 10/21, Éz 3, 2R 25, Jr 39/52, 2Ch 36, Jr 40/41, Lm 1...) ; 18/18 curl 200.
- S3 : data/p8_ez9.py (180 826 o, record absolu) ; ~35 coquilles (ENGLISH/CLOSED, AC COMPLI, FRAis, GABAHta, REDemandé, VATTA VO, HATSOPHEH, KESHIR, DABORD, DOÙ, LUN...) ; QC : AST OK, 0 cyrillique, 18 http.
- S4 : build 1er coup → 222 Ko (record ; sorti ../, replacé preuves/).
- S5 : 7/7 images 1er coup ; voice-05 (battle 05) ; 5/6 MP3 1er coup + EZ352 bloqué modération (mort/mourra) → régénéré adouci.
- S6 : durées 10.3/8.8/11.7/10.5/9.7/9.7 = 60.7 s ; durations.json → 82 entrées.
- S7 : rebuild 222 Ko (39 liens wol, 6 audio, 6 img) ; purge P8-56 patterns précis + vignette EZ8 → fenêtre exacte (19 JPG + 18 MP3).
- S8 : §3bg 6/6 PUBLIE → **354/1000** ; 373 JPG créés (19 présents), 365 MP3 (18 pistes, 171,9 + 136,9 + 60,7 s) ; §3bh P8-60 ouvert (EZ10, P355–P360, bergers/Séir/ossements/Gog).
## Journal — P8-60 (EZ355–EZ360, Éz 34-38, bergers/Séir/ossements/Gog)
- S1 : registre P355–P360 ; 6 web_search (1 wol LSF + séculiers) ; statuts : 1 Accomp/À venir + 2 Accomplie + 1 Accomp/À venir + 2 À venir.
- S2 : 18/18 triplets clos (B1 4×0 + B2–B6 grep data : nwt 19/23, 33/5, 43/10, 23/63, 38/8, 27/12, 23/26, 43/5, 49/2, 66/20, 38/12 ; Rbi8/nwtsty 26/25, 15/3, 38/10 ; nwtsty 38/14) ; curl 18/18 200.
- S3 : p8_ez10.py 299 386 o (record) — EZ355 HOY/HINENI/ABDI-DAVID/BERIT-SHALOM ; EZ356 ÉYBAT-OLAM/LEDAM/SHIMMOT-OLAM ; EZ357 NASATI/QÉREBU/HADASH/ÉDÉN ; EZ358 BAHARUGIM/PHOTÉAH-QIBROT ; EZ359 VEQARAB/JÉCONIA/MIQDASHI ; EZ360 HAHIM/TABBUR/6 fléaux.
- S4 : 35 coquilles corrigées (ÉPAISANTES, CAVERNE, OSSEMENTS, CHARNIERS, PUBLICITÉ, MONERGISTIQUE, RANCUNES, TABBUR…) ; 9 motifs dette déjà propres ; build 342 Ko (record : 39 wol, 6 audio, 6 img).
- S5/S6 : 6/6 JPG + vignette EZ10 (médias d'abord sous /home/user/preuves → mv projet) ; 6/6 MP3 voice-05 du 1er coup = 101,4 s ; durations.json 82→88.
- S7 : rebuild 342 Ko ; purge P8-57 motifs exacts (6 JPG EZ337–342 + 6 MP3) + vignette EZ9 → fenêtre exacte (19 JPG + 18 MP3).
- S8 : §3bh 6/6 PUBLIE → **360/1000** ; 380 JPG créés (19 présents), 371 MP3 (18 pistes, 136,9 + 60,7 + 101,4 s) ; §3bi P8-61 ouvert (EZ11, P361–P366, Gog enseveli/temple/rivière).
## Journal — P8-61 (EZ361–EZ366, Éz 39-47, Gog/temple/rivière)
- S1 : registre P361–P366 ; 6 web_search (2 hits wol : Éz 39 nwt + aperçu Éz 47) ; statuts : 5 À venir + 1 mixte.
- S2 : 18/18 triplets tout-nwt, 0 friction (B1 12×0 + B2 10×0 ; réserve : 24/7, 2/25, 2/40, 37/2) ; curl 18/18 200.
- S3 : p8_ez11.py 214 240 o — EZ361 VESHISHS·ARC/ZÉBAH (Ap 19 jumeau) ; EZ362 HAMON-GOG/TSIYYUN/HAMONAH (Rizpa+Acan) ; EZ363 VELO-OTIR/SHAPHAKHTI-RUHI ; EZ364 BISHNAT-573/UQNÉH/YEHOVAH-SHAMMAH ; EZ365 MIDDÉRÉKH-HAQQADIM/ZOT-TORAT×2 ; EZ366 ÉLÉPH×4/VENIRPEU/LITERUPHAH (Ap 22 jumeau).
- S4 : 75 subs (JOUR型 + R начина cyrilliques éliminés, BAGGoyim, 70+ casses/tirets) + rewrite limites EZ365 (méta-scolie supprimée) → 0 cyrillique/CJK ; build 252 Ko.
- S5/S6 : 6/6 JPG + vignette EZ11 (chemins absolus projet OK) ; 6/6 MP3 voice-05 du 1er coup = 94,4 s ; durations.json 88→94.
- S7 : rebuild 252 Ko (39 wol, 6 audio, 6 img) ; purge P8-58 motifs exacts (6 JPG EZ343–348 + 6 MP3) + vignette EZ10 → fenêtre exacte (19 JPG + 18 MP3).
- S8 : §3bi 6/6 PUBLIE → **366/1000** ; 387 JPG créés (19 présents), 377 MP3 (18 pistes, 60,7 + 101,4 + 94,4 s) ; §3bj P8-62 ouvert (transition EZ/DN, P367–P372, Shammah + Daniel 1-2).
## Journal — P8-62 (EZ367+DN368–DN372, Éz 48 + Dn 1-2, 4, Shammah/statue/pierre/arbre)
- S1 : registre P367–P372 ; 6 web_search depth 2 (1 hit jw.org : Dn 4/1914, arbre + temps des nations) ; statuts : 4 Accomplie + 1 À venir + 1 mixte.
- S2 : 18/18 triplets tout-nwt, 0 friction (B1 12×0 + B2 10×0 ; réserve : 23/44, 1/49, 40/21, 19/126 ; chapitres épuisés évités : 2R 24, Esd 1, Jr 25, Éz 17) ; curl 18/18 200.
- S3 : p8_ezdn1.py 220 Ko — EZ367 YEHOVAH-SHAMMAH/SABIB-18000 (Ap 21 jumeau, portes-tribus) ; DN368 BEHÉYKHAL/SHÉMOT (605, BM 21946, rations Yaukin) ; DN369 ÉSSÉR-YADOT/AD-SHENAT-AHAT (oct 539 Goubaru, cylindre Cyrus, Is 45) ; DN370 TSÉLÉM 4 métaux (603, or→fer-argile, MITHARABIN) ; DN371 HITGUEZERET/BÉYADAYIN-LAV (Mt 21:44, Ac 4, Armageddon) ; DN372 ILANA/IQQAR/NETALTU (12 mois, 7 iddanin, boanthropic, Magnificat).
- S4 : 92 subs effectives (84 coquilles rédactionnelles + 8 police : BELTESHATSAR×3, DIODORE, MÉMORIAL, GREC, POINDRA, SOLLICITÉ ; 2 passes no-op identiques écartées) → 0 cyrillique/CJK, 0 espace exotique, 0 espace-avant-… ; build 263 Ko.
- S5/S6 : 6/6 JPG du 1er coup (shammah, déportation, Cyrus, statue, pierre, arbre) ; 6/6 MP3 voice-05 du 1er coup = 54,0 s (9,9 · 9,5 · 7,7 · 10,3 · 8,6 · 8,0) ; durations 24→18 pistes (fenêtre).
- S7 : rebuild 263 Ko (39 wol, 6 audio, 6 img) ; purge P8-59 motifs exacts (6 JPG EZ349–354 + 6 MP3) → fenêtre exacte (19 JPG + 18 MP3).
- S8 : §3bj 6/6 PUBLIE → **372/1000** ; 393 JPG créés (19 présents), 383 MP3 (18 pistes, 101,4 + 94,4 + 54,0 s) ; §3bk P8-63 ouvert (Daniel, P373–P378, muraille/lions/bêtes).
## 3bk. Vague P8-63 (DN — Daniel : écriture murale, fosse aux lions, quatre bêtes)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN373 | P373 | Dn 4:31-32 · la raison rendue, le Très-Haut domine | PUBLIÉE |
| DN374 | P374 | Dn 5:5-28 · la main écrit, royaume divisé aux Mèdes et Perses | PUBLIÉE |
| DN375 | P375 | Dn 5:23-24 · Balthazar jugé, les dieux d'argent ne sauvent pas | PUBLIÉE |
| DN376 | P376 | Dn 6:24 · les accusateurs jetés aux lions avec leurs familles | PUBLIÉE |
| DN377 | P377 | Dn 7:1-7 · quatre bêtes sortant de la mer | PUBLIÉE |
| DN378 | P378 | Dn 7:8, 24-26 · la petite corne, les saints livrés | PUBLIÉE |

## Journal — P8-63 (DN373–DN378, Dn 4-7, raison rendue/muraille/lions/bêtes) — EN COURS
- S1 : registre L258-268 (statuts : 5 Accomplie + 1 mixte) ; §3bk + workflow ouverts ; 6 web_search depth 2 (hits wol : « Qui dominera le monde ? » 1101999028, « Quatre mots qui changèrent le monde » 1101999026, « Le saviez-vous ? Balthazar » 2020287, « La lutte contre deux bêtes féroces » 1101988028) ; curl 4/4 200.
- S2 : 18/18 triplets tout-nwt, 0 friction (B1 12×0 + B2 10×0 + B3 9/10 ; B4 : 18 chapitres testés) ; chapitres épuisés évités (Jr 50/51, Ap 14, Ps 137, Is 44, Ps 74, Dn 9, Dn 12, Za 11) ; curl 18/18 200. Triplets : DN373 19/75+18/42+19/33 · DN374 18/31+19/90+42/12 · DN375 19/115+24/10+11/18 · DN376 17/7+19/7+20/26 · DN377 28/13+66/13+66/12 · DN378 53/2+62/2+41/13 ; réserve : 61/2, 65/1, 62/4, 5/4, 19/135.
- S3a : p8_dn1.py (CAT DN1) — DN373 (4 src : triplet + Dn 4) et DN374 (5 src : triplet + Dn 5 + wol 1101999026) ; réparation du `texte` DN374 par splice (3 SyntaxError successifs : L312 chaîne coupée, L330 `)`/`[`, L328 guillemet) ; build de contrôle `_TMP_DN1.html` 63 Ko — validation OK (11 blocs, liens conformes), 2 fiches, 9 sources.
- S3b : DN375 (5 src : triplet + Dn 5 + wol 2020287) — `texte` resplicé (L591) ; DN376 (4 src : triplet + Dn 6) ; 2 retouches rédactionnelles (6:23 « aucune blessure » ; « personnage composite ») ; 4 fiches = DN373 13776 o · DN374 13629 o · DN375 ≈13 000 o · DN376 ≈13 500 o ; QC : py_compile OK, 0 lien non officiel, blocs 1 249–2 661 car.
- S4 (médias) : 6/6 JPG générés du 1er coup (raison, muraille, idoles, lions, betes, corne) — 1408×768 (bêtes/corne 1376×768), 195–261 Ko ; en place dans preuves/images/.
- S3c : DN377 (6 src : triplet Os 13/Ap 13/Ap 12 + Dn 7 + 2 wol) et DN378 (5 src : triplet 2Th 2/1Jn 2/Mc 13 + Dn 7 + wol 1101999028) — 1 SyntaxError (L1093 chaîne coupée) réparé + 1 tuple accidentel (hist DN378 en virgule terminale) corrigé ; 6 substitutions (D'HUMME, administrativе cyrillique, du Nubie, TRIBUNaux, PRAYEZ, JUDEÉ) ; QC final : 6 fiches = 81 135 o de contenu, 29 sources, 0 non-officiel, 0 cyrillique/CJK, blocs 1 249–2 661 car (texte araméen translittéré + jumeaux).
- S4b : build de contrôle 163 Ko (6 fiches, 29 sources, 6/6 images liées, 0 « SANS IMAGE »).
- S5/S6 : 7e image `prophe_DN1_vignette.jpg` (trône de feu + bêtes + Fils de l'homme) ; 6/6 MP3 voice-05 (1 refus >1500 car. sur DN378 → réécrit) = 35,3 · 39,3 · 38,7 · 39,6 · 41,8 · 38,4 s = **233,1 s** ; total fenêtre 381,5 s.
- S7 : purge P8-60 motifs exacts (6 JPG EZ355–EZ360 + 6 MP3) + vignette EZ11 → fenêtre exacte (19 JPG + 18 MP3) ; build final `preuves/FICHES8_DANIEL_1.html` 156 Ko (160 075 o) — 58 liens wol (29×2), 6 balises audio, 6 images distinctes, 11 blocs par fiche, 0 cyrillique/CJK.
- S8 : §3bk 6/6 PUBLIÉE → **378/1000** ; 400 JPG créés (19 présents dont vignette DN1), 389 MP3 (18 pistes) ; §3bl P8-64 ouvert (DN2, P379–P384, Trône de feu / saints / bélier-bouc / 2 300 jours / soixante-dix ans).

## 3bl. Vague P8-64 (DN2 — Daniel 7-9 : Trône de feu, bélier et bouc, soixante-dix semaines)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN379 | P379 | Dn 7:9-14 · le Trône de feu ; le Fils de l'homme reçoit la domination | PUBLIÉE |
| DN380 | P380 | Dn 7:27 · le royaume donné aux saints du Très-Haut | PUBLIÉE |
| DN381 | P381 | Dn 8:1-8, 20, 21 · le bélier Médo-Perse abattu par le bouc de Grèce | PUBLIÉE |
| DN382 | P382 | Dn 8:8, 22 · le grand royaume divisé en quatre royaumes inférieurs | PUBLIÉE |
| DN383 | P383 | Dn 8:9-14, 23-25 · la petite corne ; 2 300 jours du soir et du matin | PUBLIÉE |
| DN384 | P384 | Dn 9:1-19 · les soixante-dix ans de Jérémie reconnus dans la prière | PUBLIÉE |

Statuts du registre : DN379 À venir (Mt 26:64 ; Ap 5:9, 10) · DN380 À venir (Ap 22:3-5) · DN381–DN383 Accomplie (Alexandre, partage de 301, Antiochus IV et 1 Maccabées) · DN384 Accomplie (Dn 9:2 ; Jr 25:11 ; 29:10).
## Journal — P8-64 (DN379–DN384, Dn 7-9, Trône de feu/bélier et bouc/2 300 jours/prière)
- S1 : registre L269-274 (statuts : 2 À venir + 4 Accomplie) ; §3bl + workflow ouverts ; 5 web_search depth 2 → hits wol : « Fils de l'homme » 1200004183 (Dn 7:13-14 appliqué au Messie, Soncino rabbinique, Rév 12:5-10), « Livre de la Bible numéro 27 — Daniel » 1101990088 (7:27 : les saints du Suprême partagent le Royaume avec Christ), notes nwt 27/7 (ʿAttiq yomin, kevar ʾenash) ; exégèse : trônes pluriels = juges associés (Annotée : saints, Mt 19:28 ; Ap 20:4), nuées = privilège exclusif de Dieu (Ps 18 ; 97 ; Na 1:3), Dn 8 AELF/DAB (bélier 2 cornes inégales, bouc sans toucher le sol), 2300 soirs et matins (1 150 jours pleins ou 2 300 offrandes — Bible Annotée, biblestudytools, débat adventiste 457 av.), Dn 9 (lecture de Jérémie, sac et cendre, décret de Cyrus 538/537).
- S2 : 3 batteries grep (30+30+30 chapitres testés) → 18 chapitres libres retenus ; curl 18/18 → 200. Triplets : DN379 19/110+58/1+26/1 · DN380 19/145+19/96+66/5 · DN381 4/24+15/7+19/103 · DN382 11/12+12/14+19/118 · DN383 3/16+58/9+27/10 · DN384 15/9+16/1+19/51 ; réserve : 19/22, 19/130, 24/3, 4/28, 2/26, 2/24, 1/11, 7/8, 23/27, 19/102.
- S3 : data/p8_dn2.py 155 Ko — CAT DN2 ; **leçon de méthode appliquée : chaînes monolignes** (fin des SyntaxError de `texte`) ; DN379 (5 src : triplet + Dn 7 + wol 1200004183) · DN380 (5 src : triplet + Dn 7 + wol 1101990088) · DN381 (4 : triplet + Dn 8) · DN382 (4 : triplet + Dn 8) · DN383 (4 : Lv 16/Hé 9/Dn 10 + Dn 8) · DN384 (5 : Esd 9/Ne 1/Ps 51 + Dn 9 + wol 1101990088) ; 4 coquilles (SER VAIENT, AFF ERMI, TRANSEUPHRATE, Couché→COUCHÉ).
- QC : 6 fiches, 72 968 o de contenu, types str vérifiés sur les 8 blocs, 27 sources toutes jw.org, 0 cyrillique/CJK, blocs 1 058–2 110 car, tl 5, accomplissement 5 par fiche.
- S4 : build de contrôle `_TMP_DN2.html` 165 Ko — validation OK (6 fiches, 27 sources), 0 image au moment du contrôle.
- S5/S6 : 7 JPG du 1er coup (trone, saints, belier, quatre, sanctuaire, priere + vignette `prophe_DN2_vignette.jpg`) ; 6/6 MP3 voice-05 du 1er coup = 39,1 · 39,3 · 38,4 · 39,0 · 37,2 · 36,6 s = **229,6 s** ; fenêtre 18 pistes = 516,7 s.
- S7 : purge P8-61 motifs exacts (6 JPG EZ361–366 + 6 MP3) + vignette DN1 → fenêtre exacte (19 JPG + 18 MP3) ; build final `preuves/FICHES8_DANIEL_2.html` 156 Ko (160 586 o) — 54 liens wol (27×2), 6 balises audio, 6 images, 11 blocs par fiche, 0 cyrillique/CJK.
- S8 : §3bl 6/6 PUBLIÉE → **384/1000** ; 407 JPG créés (19 présents dont vignette DN2), 395 MP3 (18 pistes) ; §3bm P8-65 ouvert (DN3, P385–P390, soixante-dix semaines / prince de Perse / rois du nord et du sud).

## 3bm. Vague P8-65 (DN3 — Daniel 9-11 : soixante-dix semaines, princes et rois)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN385 | P385 | Dn 9:24-27 · soixante-dix semaines ; le Messie retranché ; la ville détruite | PUBLIÉE |
| DN386 | P386 | Dn 10:12-14, 21 · vingt et un jours de retard ; le prince de Perse ; Mikaël | PUBLIÉE |
| DN387 | P387 | Dn 11:2 · quatre rois de Perse ; le quatrième soulèvera tout contre la Grèce | PUBLIÉE |
| DN388 | P388 | Dn 11:3 · un roi puissant, Alexandre, agira selon son bon plaisir | PUBLIÉE |
| DN389 | P389 | Dn 11:4 · son royaume brisé et divisé vers les quatre vents | PUBLIÉE |
| DN390 | P390 | Dn 11:5 · le roi du sud devient fort ; un prince plus fort que lui | PUBLIÉE |

Statuts du registre : DN385 Accomplie (Luc 3:1, 21, 22 ; 70 de n. è. ; Luc 19:43, 44 ; 21:20) · DN386 Accomplie (récit, Dn 10:13, 21) · DN387–DN390 Accomplie (Xerxès 480, Alexandre, partage de 301, Ptolémée Ier et Séleucus Ier).

## Journal — P8-65 (DN385–DN390, Dn 9-11, soixante-dix semaines/prince de Perse/rois du nord et du sud)
- S1 : 5 web_search depth 2 → hits wol : « Soixante-dix semaines » 1200003915 (69 semaines = 483 ans depuis 455 av. n. è. → 29 ; « retranché » à la moitié), « Le moment de la venue du Messie est révélé » 1101999030 (division 7+62+1 = 49/434/7 ans ; Pâque printemps 33), « Le Messie — que devait-il accomplir et quand ? » 101976247 (mashiaḥ sans qualificatif une seule fois, en Dn 9), « L'Histoire écrite à l'avance avec précision » 1977603 (quatre généraux : Séleucus Nicator, Cassandre, Ptolémée Lagus/Soter, Lysimaque), « Deux rois en conflit » 1101999032 (tableau nord/sud 11:5-19), « Oulaï » 1200004502 (Karkheh ou canal au N. de Suse) ; comparateurs de versions (Dn 10:13 ; 11:2) et notes : Xerxès = Ahasuérus d'Esther, 2 641 610 hommes annoncés par Hérodote, Salamis ; Annotée « ne parle que de quatre rois ».
- S2 : grep 35 chapitres (motif data/) → 21 libres ; curl 21/21 → 200. Triplets : DN385 23/53+19/69+44/3 · DN386 7/6+66/10+19/34 · DN387 17/1+15/4+19/20 · DN388 10/8+11/4+19/44 · DN389 14/13+1/10+10/3 · DN390 1/15+20/25+26/45 ; 1 chapitre nwt par fiche (Dn 9, 10, 11).
- S3 : data/p8_dn3.py — CAT DN3 + DN385 (6 src : triplet + Dn 9 + 2 wol) ; **1 SyntaxError L30 (`) ,` orphelin fermant mal la liste `texte`)** réparé par remplacement exact du fragment ; puis _dn3b.py (DN386 4 src : triplet + Dn 10 · DN387 4 src : triplet + Dn 11) et _dn3c.py (DN388 5 src · DN389 6 src · DN390 6 src) concaténés par `cat >>`, scratch supprimés, py_compile OK à chaque étape.
- QC : 6 fiches = 60 071 o de contenu ; types str vérifiés sur les 8 blocs + schema ; blocs 828–2 018 car. ; 31 sources (6/4/4/5/6/6) toutes jw.org ; tl 5 et accomplissement 5 par fiche ; 0 cyrillique/CJK ; 0 lien non officiel.
- S4 : build de contrôle `_TMP_DN3.html` 143 Ko — validation OK (11 blocs, 6 fiches, 31 sources) ; **statut « Accomplie (récit) » (DN386) accepté par la validation**.
- S5/S6 : 7 JPG du 1er coup (semaines, prince, perse, alexandre, quatre_royaumes, deux_rois + vignette `prophe_DN3_vignette.jpg`) ; 6/6 MP3 voice-05 du 1er coup = 19,0 · 21,1 · 21,0 · 23,2 · 23,5 · 21,5 s = **129,3 s** ; fenêtre 18 pistes = 592,0 s.
- S7 : purge P8-62 motifs exacts (6 JPG EZ367 + DN368–DN372 et 6 MP3 homonymes) + vignette DN2 → fenêtre exacte (19 JPG + 18 MP3) ; build final `preuves/FICHES8_DANIEL_3.html` 145 Ko (140 905 car. / 149 452 o) — 65 mentions wol (31×2 liens + 3 en clair), 6 balises audio, 6 images, 11 blocs par fiche, 0 cyrillique/CJK.
- S8 : §3bm 6/6 PUBLIÉE → **390/1000** ; 414 JPG créés (19 présents dont vignette DN3), 401 MP3 (18 pistes) ; §3bn P8-66 ouvert (DN4, P391–P396, Daniel 11:6-17).

## 3bn. Vague P8-66 (DN4 — Daniel 11 : alliances, Raphia, le pays de la Parure)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN391 | P391 | Dn 11:6 · alliance par mariage ; la fille du roi est livrée | PUBLIÉE |
| DN392 | P392 | Dn 11:7-9 · une branche de sa racine s'élèvera et l'emportera | PUBLIÉE |
| DN393 | P393 | Dn 11:10-13 · les fils du roi du nord lèvent une grande armée | PUBLIÉE |
| DN394 | P394 | Dn 11:11, 12 · le roi du sud s'irrite ; des dizaines de milliers tombent | PUBLIÉE |
| DN395 | P395 | Dn 11:14-16 · beaucoup se dressent ; le pays de la Parure est pris | PUBLIÉE |
| DN396 | P396 | Dn 11:17 · il donne la fille de sa femme pour la détruire | PUBLIÉE |

Statuts du registre : DN391 Accomplie (Ptolémée II, Bérénice, Antiochus II) · DN392 Accomplie (Ptolémée III Évergète, 245 av. n. è.) · DN393 Accomplie (Séleucus III, Antiochus III, quatrième guerre de Syrie) · DN394 Accomplie (Raphia 217 av. n. è.) · DN395 Accomplie (Antiochus III, Palestine) · DN396 Accomplie (Cléopâtre I et Ptolémée V, 193 av. n. è.).

## Journal — P8-66 (DN391–DN396, Dn 11:6-17, alliances/mariages, Raphia, le pays de la Parure)
- S1 : 7 web_search depth 2 + fetch_page wol 1101999032 « Deux rois en conflit » (chunks 0-3/5 lus). Faits : Bérénice/Laodice/Antiochus II (≈250 ; répudiation, dot partielle, meurtres de 246, poison) ; Ptolémée III Évergète (246-221) : Antioche, Laodice mise à mort, butin 40 000 talents et 2 500 images (idoles de Cambyse), jusqu'à Suse, sédition en Égypte, riposte manquée de Séleucus II vers 242 ; Séleucus III assassiné (<3 ans) puis Antiochus III (223-187) : Séleucie, Coelé-Syrie, Tyr, Ptolémaïs, villes de Juda, retrait vers la forteresse au printemps 217 ; Raphia (22 juin 217) : 75 000 vs 68 000 selon la Bibliothèque en ligne, Polybe 70 000/5 000/73 vs 62 000/6 000/102, pertes 10 000 + 300 + 4 000 prisonniers, traité (Séleucie gardée, Phénicie et Coelé-Syrie perdues) ; 16 ans plus tard, Philippe V, tuteur Agathocle, Ptolémée V (5 ans) ; Panéas/Scopas, rempart de siège, Sidon 198, Jérusalem 198 ; Rome, Cléopâtre Ire « la fille des femmes », mariage 193, provinces non remises, Égypte aux côtés de Rome, Magnésie 190, Élymaïs 187, Séleucus IV.
- S2 : balayage des 362 chapitres nwt déjà référencés (motif data/) → 630 chapitres libres (livres 1-27 × 30) ; sélection des 18 triplets ; curl 19/19 → 200 (18 + Dn 27/11). Triplets : DN391 1/2+14/18+17/2 · DN392 9/5+11/2+13/18 · DN393 5/20+12/16+19/21 · DN394 9/15+13/21+20/16 · DN395 6/23+25/3+26/15 · DN396 11/11+22/6+26/16 ; + Dn 11 et wol 1101999032 par fiche (+ wol 1977603 pour DN395 et DN396).
- S3 : data/p8_dn4.py — CAT DN4 + DN391-393 (write_file) puis _dn4b.py (DN394-396) concaténé par `cat >>` et supprimé ; py_compile OK ; 1 parasite (`interprétation" if False else`) réparé avant concaténation ; 2 coquilles corrigées (SIXTZE→SEIZE, DETAINS→DÉTAILS) ; « práctica »→« pratique ».
- QC : 6 fiches = 60 991 o de contenu ; blocs 972-1 736 car. ; src 5/5/5/5/6/6 = 32 (jw.org uniquement) ; tl 5 et accomplissement 5 par fiche ; texte 2 blocs ; 0 cyrillique/CJK ; 0 lien non officiel.
- S4 : build de contrôle `_TMP_DN4.html` 135 Ko — validation OK (11 blocs, 6 fiches, 32 sources) — « SANS AUDIO / SANS IMAGE » attendu à ce stade.
- S5/S6 : 7 JPG (mariage, evergete, armee, raphia, panias, cleopatre + vignette `prophe_DN4_vignette.jpg`) — raphia d'abord bloquée par la modération, reformulée sans violence et acceptée ; 6/6 MP3 voice-05 = 32,2 · 28,6 · 31,3 · 28,9 · 30,6 · 28,9 s = **180,5 s** (DN394 réenregistré pour remplacer « débaissée » par « dissolue ») ; fenêtre 18 pistes = **643,2 s**.
- S7 : build final `preuves/FICHES8_DANIEL_4.html` 137 Ko (135 465 car.) — 67 mentions wol (32×2 + 3 en clair), 6 balises audio, 6 images distinctes, 12 fichiers liés, 11 blocs par fiche, 0 cyrillique/CJK ; purge P8-65 motifs exacts (6 JPG DN385–DN390 + `prophe_DN3_vignette.jpg` + 6 MP3 homonymes) → fenêtre exacte 19 JPG / 18 MP3.
- S8 : §3bn 6/6 PUBLIÉE → **396/1000** ; 421 JPG créés (19 présents dont vignette DN4), 407 MP3 (18 pistes) ; §3bo P8-67 ouvert (DN5, P397–P402, Daniel 11:18-35 — Rome et Antiochus IV ; DN402 au statut mixte « Accomplie (1er accomplissement) / À venir » à valider au build).

## 3bo. Vague P8-67 (DN5 — Daniel 11 : Rome, l'exacteur, Antiochus IV et la chose immonde)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN397 | P397 | Dn 11:18, 19 · sa face vers les îles, puis la chute sur son propre sol | PUBLIÉE |
| DN398 | P398 | Dn 11:20 · l'exacteur passe par la gloire du royaume ; brisé en quelques jours | PUBLIÉE |
| DN399 | P399 | Dn 11:21-24 · un homme méprisé s'élève en temps de paix, agit avec ruse | PUBLIÉE |
| DN400 | P400 | Dn 11:25-27 · guerre contre le sud ; des complots ; le mensonge entre les deux rois | PUBLIÉE |
| DN401 | P401 | Dn 11:28-30 · il revient contre l'alliance ; les navires de Kittim viennent contre lui | PUBLIÉE |
| DN402 | P402 | Dn 11:31-35 · la chose immonde qui cause la désolation ; les hommes de perspicacité | PUBLIÉE |

Statuts du registre : DN397 Accomplie (Magnésie, 190-188) · DN398 Accomplie (Séleucus IV et l'exacteur ; Dn 11:20) · DN399 Accomplie (Antiochus IV Épiphane, 175) · DN400 Accomplie (campagnes contre l'Égypte) · DN401 Accomplie (« journée d'Éleusis ») · DN402 Accomplie (premier accomplissement) et À venir (1 Maccabées 1:20-64 ; Josèphe, Antiquités 12.5.4 ; Matthieu 24:15).

## Journal — P8-67 (DN397–DN402, Dn 11:18-35, Magnésie, l'exacteur, Antiochus IV, Éleusis, la chose immonde)
- S1 : 4 web_search depth 2 + fetch_page wol 1101999032 (chunk 4/5, fin du document : Séleucus IV, Héliodore, Antiochus IV, Zeus, Hanoukka, Maccabées, Pompée/Hérode) et wol 1101999036 (chunks 0-1/5 : versets 32-35 et 36-40 appliqués au roi du nord moderne, tableaux, références Jean 10:22 / Mt 24:15). Faits retenus : Séleucus IV (187-175), tribut de 1 000 talents/an, Héliodore et 2 Maccabées 3, mort par poison (ni colère ni guerre) ; Antiochus IV (175-164) : Démétrius otage à Rome, appui d'Eumène II et Attale, Onias III écarté, Jason puis Ménélas, largesses et butin ; 6e guerre de Syrie (170-169) : Péluse, Memphis, complots des courtisans, « mensonge à une même table », second Ptolémée à Alexandrie ; 168 : « journée d'Éleusis », Popillius Laenas et le cercle, navires de Kittim ; 169-167 : retour contre l'alliance, Ménélas et les hellénisateurs ; décembre 167 : autel sur le grand autel, Zeus, dix jours plus tard le sacrifice ; 1 Maccabées 1:20-64, Josèphe Antiquités 12.5.4 ; 164 : Hanoukka (25 Kislev) ; 161 traité avec Rome, 104 royaume hasmoneen, 63 Pompée, 37 Hérode. Bonus méthodologique : vérification dans fiches/build_fiches.py — le statut est libre (aucune contrainte), le statut mixte du registre P402 est donc affichable.
- S2 : recensement des 362 chapitres déjà référés → 630 libres ; 18 triplets choisis puis curl 19/19 → 200 (18 + Dn 27/11). Triplets : DN397 6/1+24/4+20/1 · DN398 12/11+2/25+3/27 · DN399 2/1+20/29+18/19 · DN400 2/5+20/12+18/24 · DN401 2/14+20/21+24/12 · DN402 3/6+13/22+20/24 ; + Dn 11 par fiche (+ wol 1101999036 pour DN401 et DN402).
- S3 : data/p8_dn5.py — CAT DN5 + DN397-399 (write_file) puis _dn5b.py (DN400-402) concaténé et supprimé ; 2 correctifs de frappe avant/après concaténation (« M EMPHIS »→MEMPHIS, « PTO LÉMÉE »→PTOLÉMÉE, ANTIOCHèNE→ANTIOCHÈNE).
- QC : 6 fiches = 55 810 o de contenu ; blocs 887-1 499 car. ; src 5/5/5/5/6/6 = 32 (jw.org uniquement) ; tl 5, accomplissement 5, texte 2 blocs ; 0 cyrillique/CJK ; 0 lien non officiel ; statut DN402 « Accomplie (1er accomplissement) / À venir » conforme au registre.
- S4 : build de contrôle `_TMP_DN5.html` 129 Ko — validation OK (11 blocs, 6 fiches, 32 sources) ; statut mixte accepté (aucune contrainte sur le statut dans fiches/build_fiches.py).
- S5/S6 : 7 JPG (magnesie, heliodore, epiphane, egypte, kittim, immonde + vignette `prophe_DN5_vignette.jpg`) — magnesie bloquée une fois par la modération puis reformulée en tableau sans combat et acceptée ; 6/6 MP3 voice-05 = 30,6 · 27,7 · 29,5 · 27,7 · 28,2 · 27,9 s = **171,6 s** ; fenêtre 18 pistes = **634,3 s**.
- S7 : build final `preuves/FICHES8_DANIEL_5.html` 131 Ko (130 092 car. / 134 752 o) — 67 mentions wol (32×2 + 3 en clair), 6 balises audio, 6 images, 12 fichiers liés, 11 blocs par fiche, 0 cyrillique/CJK ; purge P8-66 motifs exacts (6 JPG DN391–DN396 + `prophe_DN4_vignette.jpg` + 6 MP3 homonymes) → fenêtre exacte 19 JPG / 18 MP3.
- S8 : §3bo 6/6 PUBLIÉE → **402/1000** ; 428 JPG créés (19 présents dont vignette DN5), 413 MP3 (18 pistes) ; §3bp P8-68 ouvert (DN6, P403–P407 — Daniel 11:36-12:12 : le roi qui s'élève au-dessus de tout dieu, Mikaël, la résurrection, le livre scellé, les 1 290 et 1 335 jours).

## 3bp. Vague P8-68 (DN6 — Daniel 11:36-12:12 : la fin du roi, Mikaël, la résurrection, le livre scellé, les jours comptés)
| Fiche | P | Sujet | État |
|---|---|---|---|
| DN403 | P403 | Dn 11:36-45 · le roi selon son bon plaisir ; le dieu des forteresses ; les tentes-palais ; la fin sans secours | PUBLIÉE |
| DN404 | P404 | Dn 12:1 · Mikaël se lève ; un temps de détresse sans précédent ; ton peuple échappera | PUBLIÉE |
| DN405 | P405 | Dn 12:2, 3 · les dormeurs de la poussière se réveillent : vie ou honte ; les perspicaces brillent | PUBLIÉE |
| DN406 | P406 | Dn 12:4, 9 · le livre scellé jusqu'au temps de la fin ; la vraie connaissance deviendra abondante | PUBLIÉE |
| DN407 | P407 | Dn 12:7, 11, 12 · un temps, des temps et une moitié ; 1 290 et 1 335 jours | PUBLIÉE |

Statuts du registre : DN403 À venir · DN404 À venir (Matthieu 24:21, 22 ; Révélation 12:7) · DN405 À venir (Jean 5:28, 29 ; Actes 24:15) · DN406 En cours (Daniel 12:4, 9) · DN407 À venir (Dn 12:7, 11, 12). Note d'alignement : le tableau ci-dessus a été corrigé en S8 pour reprendre exactement les cinq entrées du registre (P403 = Dn 11:36-45, non scindée) ; la vague compte donc 5 fiches, et le livre de Daniel est clos au registre à P407.

## Journal — P8-68 (DN403–DN407, Dn 11:36-12:12 — clôture du livre de Daniel)
- S1 : 4 web_search depth 2 + 3 fetch_page. Documents wol lus : 1101999036 (chunks 0-2/5 : versets 28-45 appliqués au roi du Nord moderne — pays de la Parure = domaine spirituel du peuple de Jéhovah ; Édom/Moab/Ammôn ; Égypte ; démantèlement de l'URSS en décembre 1991 avec « il est sage de ne pas spéculer » ; nouvelles du levant = destruction de Babylone la Grande, Rév 16:12 ; tentes-palais entre la mer et la montagne sainte), 1101999037 « L'identification des vrais adorateurs au temps de la fin » (dp chap. 17 : Mikaël = Jésus Chef céleste, « se tient là » depuis 1914, « se lèvera » = événement ; Rév 11:3, 9, 11 ; les oints reprennent vie au sens spirituel), 1993802 « Les jours prophétiques annoncés par Daniel, et notre foi » (w93 1/11 : 12:4 scellé jusqu'au temps de la fin, temps de la fin à partir de 1914 ; 1 260 jours = décembre 1914 → 21 juin 1918 ; libération le 26 mars 1919 ; 1 290 jours = janvier 1919 → septembre 1922 (Cedar Point) ; 1 335 jours = septembre 1922 → fin du printemps 1926 (Londres, livre Délivrance)).
- S2 : recensement des chapitres nwt déjà référencés → 3 substitutions après contrôle (5/28, 18/19 et 19/49 déjà consommés) : 5/29, 18/14, 19/22 ; curl 16/16 → 200 (5/29 20/15 18/36 2/17 7/5 18/15 18/14 19/17 19/22 19/12 20/2 1/20 5/30 9/17 12/2 27/12). Triplets (esprit du texte, registre reste source de vérité) : DN403 5/29+20/15+18/36 · DN404 2/17+7/5+18/15 · DN405 18/14+19/17+19/22 · DN406 19/12+20/2+1/20 · DN407 5/30+9/17+12/2 ; + Dn 27/12 par fiche (+ wol de référence).
- S3 : data/p8_dn6.py — CAT DN6 + DN403-405 (write_file) puis _dn6b.py (DN406-407) concaténé et supprimé ; 1 correction de source avant build (référence Nombres 24 → Deutéronome 29, 5/29 vérifié 200).
- QC : 5 fiches = 48 051 o de contenu ; blocs 982-1 684 car. ; src 5/5/5/5/6 = 26 (jw.org uniquement) ; tl 5, accomplissement 5, texte 2 blocs ; statuts conformes au registre : 4 « À venir » + 1 « En cours » (DN406) ; 0 cyrillique/CJK ; 0 lien non officiel.
- S4 : build de contrôle `_TMP_DN6.html` 112 Ko — validation OK (11 blocs, 5 fiches, 26 sources) ; les 5 images sont liées (aucune ligne « SANS IMAGE »).
- S5/S6 : 6 JPG (tentes, mikael, resurrection, livre, jours + vignette `prophe_DN6_vignette.jpg`) — vignette refusée une fois (« no images ») puis acceptée après reformulation ; 5/5 MP3 voice-05 = 32,4 · 29,3 · 27,6 · 28,8 · 31,3 s = **149,4 s** ; fenêtre 17 pistes = **612,1 s**.
- S7 : build final `preuves/FICHES8_DANIEL_6.html` 114 Ko (113 008 car. / 116 836 o) — 55 mentions wol (26×2 + 3 en clair), 5 balises audio, 5 images, 10 fichiers liés, 11 blocs par fiche, 0 cyrillique/CJK ; purge P8-67 motifs exacts (6 JPG DN397–DN402 + `prophe_DN5_vignette.jpg` + 6 MP3 homonymes) → fenêtre **18 JPG / 17 MP3** (vague de 5 fiches ; la fenêtre repassera à 19/18 à la première vague de 6 fiches suivante).
- S8 : §3bp **5/5 PUBLIÉE** et tableau corrigé sur le mapping exact du registre → **407/1000** ; **le livre de Daniel est clos au registre (P407 = dernière entrée)** ; compteurs : 434 JPG créés (18 présents dont vignette DN6), 418 MP3 (17 pistes) ; §3bq P8-69 ouvert — **sortie du livre de Daniel** : partie 6 du registre, « les Douze », première vague Osée 1-3 (P408–P413).

## 3bq. Vague P8-69 (OS1 — Osée 1-3 : Jezréel, l'épouse infidèle, le retour)
| Fiche | P | Sujet | État |
|---|---|---|---|
| OS408 | P408 | Os 1:4, 5 · la fin de la royauté d'Israël ; l'arc brisé dans la vallée de Jezréel | PUBLIÉE |
| OS409 | P409 | Os 1:6, 7 · « Pas de miséricorde » pour Israël ; miséricorde pour Juda | PUBLIÉE |
| OS410 | P410 | Os 1:9-11 · « Vous n'êtes pas mon peuple » ; ils seront appelés fils du Dieu vivant | PUBLIÉE |
| OS411 | P411 | Os 2:2-13 · jugement sur l'épouse infidèle ; ses fêtes arrêtées | PUBLIÉE |
| OS412 | P412 | Os 2:14-23 · « je l'attirerai » ; l'alliance et les fiançailles pour toujours | PUBLIÉE |
| OS413 | P413 | Os 3:4, 5 · longtemps sans roi ni sacrifice ; ensuite ils chercheront Jéhovah et David leur roi | PUBLIÉE |

Statuts du registre : OS408 Accomplie (2 Rois 17:5, 6, 22, 23) · OS409 Accomplie (2 Rois 19:34, 35) · OS410 Accomplie (Romains 9:25, 26 ; 1 Pierre 2:10) · OS411 Accomplie (2 Rois 17:7-18) · OS412 Accomplie / À venir (Romains 9:25, 26) · OS413 Accomplie / À venir (2 Rois 17:6, 23 ; Osée 3:5).
Chapitres nwt : univers à re-grepper avant réservation (règle P8-63) — la vague ouvre le livre d'Osée (28/…), dont aucun chapitre n'a encore été consommé par les fiches.

## Journal — P8-69 (OS408–OS413 — Osée 1-3, première vague hors Daniel)
- S1 : 3 web_search depth 2 + exploration du portail Osée de la Bibliothèque en ligne (wol 1001070132) : note « Jezréel = ville royale où résidaient les rois d'Israël, le royaume du Nord, bien que Samarie fût leur capitale » ; notes des noms (Lo-Rouhama « on ne lui a pas fait miséricorde » ; Lo-Ami « pas mon peuple ») ; texte de 3:4, 5 ; contextes 2 Rois 17, Romains 9:25-26, 1 Pierre 2:10 ; Ézéchiel 34:23, 24 et 37:24 pour « David leur roi » ; Bible annotée sur l'éphod et les théraphim.
- S2 : recensement complet (412 chapitres nwt déjà référencés) → 20 chapitres libres sélectionnés puis curl 21/21 → 200 (28/1, 28/3, 12/15, 12/13, 11/14, 30/7, 30/6, 23/12, 23/3, 23/25, 19/30, 19/16, 24/3, 45/9, 60/2, 33/1, 33/7, 14/36, 26/20, 40/1 + wol Osée 1001070132). Contrôle : 28/2 et 12/18 déjà consommés (p8_ez4.py) → évités.
- S3 : data/p8_os1.py — CAT OS1 + OS408-410 (write_file) puis _os1b.py (OS411-413) concaténé et supprimé ; 1 coquille corrigée (« LES VEaux D'OR »).
- QC : 6 fiches = 55 494 o de contenu ; blocs 832-1475 car. ; src 5 par fiche = 30 (jw.org uniquement) ; tl 5, accomplissement 5, texte 2 blocs ; statuts conformes au registre (4 Accomplie, 2 Accomplie / À venir) ; 0 cyrillique/CJK ; 0 lien non officiel.
- S4 : build de contrôle `_TMP_OS1.html` 131 Ko — validation OK (11 blocs, 6 fiches, 30 sources).
- S5/S6 : 7 JPG (jezreel, larouhama, loami, epouse, fiancailles, david + vignette `prophe_OS1_vignette.jpg`), générées au premier essai ; 5/6 MP3 voice-05 générés (26,5 · 27,8 · 28,8 · 30,5 · 30,5 s = 144,1 s) — **l'audio d'OS409 a été refusé 4 fois puis bloqué par le plafond de 10 clips/tour : à produire au début du prochain tour et à réintégrer par un simple rebuild** (fichier attendu : `audio/fiche_OS409_larouhama.mp3`).
- S7 : build final `preuves/FICHES8_OSEE_1.html` 132 Ko (131 025 car. / 135 976 o) — 63 mentions wol (30×2 + 3 en clair), 5 balises audio, 6 images, 11 fichiers liés, 11 blocs par fiche, 0 cyrillique/CJK ; purge P8-68 motifs exacts (5 JPG DN403–DN407 + `prophe_DN6_vignette.jpg` + 5 MP3 homonymes) → fenêtre **19 JPG / 17 MP3** (repassera à 19/18 dès l'audio OS409).
- S8 : §3bq 6/6 PUBLIÉE → **413/1000** ; compteurs : 441 JPG créés (19 présents dont vignette OS1), 423 MP3 (17 pistes) ; §3br P8-70 ouvert — suite d'Osée (OS414+) : chapitres 4 à 14, dont le procès du peuple, « mon peuple périt faute de connaissance », la semence de justice, et la promesse finale « je les rachèterai du schéol ». Chapitres nwt 28/4+ déjà disponibles (univers Osée largement libre).

## 3br. Vague P8-70 (OS2 — Osée 4-10 : le procès, la connaissance rejetée et la captivité annoncée)
| Fiche | P | Sujet | État |
|---|---|---|---|
| OS414 | P414 | Os 4:6-19 · « mon peuple est détruit faute de connaissance » ; Éphraïm en disgrâce | PUBLIÉE |
| OS415 | P415 | Os 5:8-15 · je dévasterai Éphraïm ; comme un lion pour Éphraïm et pour Juda | PUBLIÉE |
| OS416 | P416 | Os 7:8-16 · Éphraïm se mêle aux peuples ; ils retourneront au pays d'Assyrie | PUBLIÉE |
| OS417 | P417 | Os 8:1-14 · le veau porté en Assyrie ; un vase sans usage parmi les nations | PUBLIÉE |
| OS418 | P418 | Os 9:1-17 · ils ne demeureront pas dans le pays de Jéhovah ; errants parmi les nations | PUBLIÉE |
| OS419 | P419 | Os 10:1-15 · le veau de Béthel emporté au grand roi ; le roi d'Israël retranché | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md) : OS414–OS419 = Accomplie ×6 (références : 2 Rois 17:6-20 ; 17:6 + 25:1-11 ; 17:6, 23 ; 17:6 ; 17:6, 23 + Osée 9:17 ; 17:6 + Osée 10:6, 7, 15). Note d'alignement : le tableau provisoire rédigé en S8 de P8-69 annonçait d'autres versets (4:1-6, 5:8-15, 6:1-3, 8:1-14, 10:1-15) : il a été corrigé en S8 de P8-70 sur le mapping exact du registre, y compris la référence à la fiche P419 (Osée 10). Les entrées restantes d'Osée (P420 Osée 11:1 ; P421 Osée 11:5-11 ; P422 Osée 14:1-9) et l'ouverture de Joël (P423 Joël 1:4-20) forment la vague suivante.
Rappel d'exécution : produire d'abord `audio/fiche_OS409_larouhama.mp3` (texte déjà rédigé, à reformuler sans termes bloquants) puis `python3 build_p8.py p8_os1 FICHES8_OSEE_1.html` pour rafraîchir la fiche 1.

## Journal — P8-70 (OS414–OS419 — Osée 4-10, le procès et la captivité annoncée)
- Rattrapage en ouverture de tour : audio `fiche_OS409_larouhama.mp3` (30,1 s) produit après quatre refus de modération puis plafond atteint au tour précédent — texte recentré sur le nom Lo-Rouhama et le contraste avec Juda, sans récit de campagne militaire ; rebuild immédiat de `FICHES8_OSEE_1.html` (133 Ko) qui intègre désormais 6 audios et 6 images.
- S1 : 2 web_search depth 2 (Osée 4:6 ; Osée 10:5-8, veau de Beth-Aven et offrande au roi d'Assyrie, note de la Bible annotée sur « Shalman ») + exploitation du portail Osée déjà lu (wol 1001070132) ; faits retenus : responsabilité des prêtres dans l'enseignement de la loi, Bet-Aven = sobriquet de Béthel, portage des statues divines comme pratique assyrienne standard, débat sur l'identification de Beth-Arbel.
- S2 : recensement complet → chapitres libres retenus : 28/4, 28/5, 28/7, 28/9, 28/8 et 28/10 (chapitres-miroirs de la prophétie, vérifiés), 5/4, 5/8, 5/12, 24/5, 19/18, 23/28, 23/4, 14/30, 26/2, 30/3, 33/2, 33/4, 12/12, 28/12 ; curl 20/20 → 200.
- S3 : data/p8_os2.py — CAT OS2 + OS414-416 (write_file) puis _os2b.py (OS417-419) concaténé et supprimé ; 4 coquilles corrigées avant/après concaténation (LA PRÊT RISE, LES VEaux, PublIcat, EN OFFrande).
- QC : 6 fiches = 53 370 o de contenu ; blocs 847-1 354 car. ; src 5 par fiche = 30 (20 URL uniques, jw.org uniquement) ; tl 5, accomplissement 5, texte 2 blocs ; statuts = Accomplie ×6 conformes au registre ; 0 cyrillique/CJK ; 0 lien non officiel.
- S4 : build de contrôle `_TMP_OS2.html` 131 Ko — validation OK (11 blocs, 6 fiches, 30 sources).
- S5/S6 : 7 JPG (connaissance, lion, colombe, aigle, errants, veau + vignette `prophe_OS2_vignette.jpg`) — 6/6 au premier essai, vignette acceptée après une première tentative sans image ; 6/6 MP3 voice-05 = 27,2 · 31,4 · 28,7 · 28,5 · 27,7 · 31,1 s = **174,6 s** (OS419 reformulé après un refus, en évitant le récit de butin) ; fenêtre 18 pistes = **637,3 s**.
- S7 : build final `preuves/FICHES8_OSEE_2.html` 133 Ko (131 206 car. / 136 285 o) — 63 mentions wol (30×2 + 3 en clair), 6 balises audio, 6 images, 12 fichiers liés, 11 blocs par fiche, 0 cyrillique/CJK ; purge P8-69 motifs exacts (6 JPG OS408–OS413 + `prophe_OS1_vignette.jpg` + 6 MP3 homonymes) → fenêtre exacte **19 JPG / 18 MP3**.
- S8 : §3br 6/6 PUBLIÉE et tableau corrigé sur le mapping exact du registre → **419/1000** ; compteurs : 448 JPG créés (19 présents dont vignette OS2), 430 MP3 (18 pistes) ; §3bs P8-71 ouvert — **fin d'Osée et ouverture de Joël** (P420–P423).

## 3bs. Vague P8-71 (OS3/JL1 — Osée 11 et 14, puis Joël 1 : « d'Égypte j'ai appelé mon fils », le retour de l'ouest, la guérison, les sauterelles)
| Fiche | P | Sujet | État |
|---|---|---|---|
| OS420 | P420 | Os 11:1 · « d'Égypte j'ai appelé mon fils » ; le Fils appelé hors d'Égypte (Matthieu 2:14, 15) | PUBLIÉE |
| OS421 | P421 | Os 11:5-11 · « l'Assyrien sera son roi » ; je ferai revenir mes fils de l'ouest | PUBLIÉE |
| OS422 | P422 | Os 14:1-9 · « je guérirai leur infidélité » ; la rosée, le lis et le cyprès toujours vert | PUBLIÉE |
| JL423 | P423 | Jl 1:4-20 · l'invasion des sauterelles ; les offrandes retranchées ; « le jour de Jéhovah est proche » | PUBLIÉE |

Statuts du registre : OS420 Accomplie (Matthieu 2:14, 15) · OS421 Accomplie (2 Rois 17:6 ; Osée 11:10, 11) · OS422 Accomplie / À venir (Osée 14:4-7) · JL423 Accomplie (1er accomplissement) (Joël 1:4-7, 10-12 ; application spirituelle Joël 2:25).
Chapitres nwt : §3bs a réservé **18 paires** (19/105, 19/130, 19/133, 19/147, 2/10, 2/13, 2/4, 20/19, 20/30, 23/27, 23/66, 33/6, 38/1, 39/4, 40/2, 45/8, 5/11, 66/9) — contrôle re-vérifié le 2026-09-26 : 0 collision ; §3bt P8-72 ouvert — **Joël, seconde partie** (JL424-JL429, P424-P429 : la trompette sur Sion et le jour de Jéhovah, « revenez à moi de tout votre cœur », l'esprit répandu sur toute chair, le rassemblement des nations, la vallée de la décision et la source sortant de la maison de Jéhovah).

## 3bt. Vague P8-72 (JL2 — Joël 2 et 3 — le jour de Jéhovah, l'esprit répandu sur toute sorte de chair, et la vallée de la décision)
⚠ NOTE DE RECONSTRUCTION (2026-09-26) : les sections §3bt à §3cd ont été perdues lors d'un incident d'ancrage d'un script de clôture et reconstruites depuis les modules `phase8/data/p8_*.py` (source de vérité) et les livrables ; tables, statuts, sources et paires sont vérifiés, les détails de journal non conservés sont signalés « (non reporté) ». Deux corrections d'intégrité ont été appliquées : (1) la paire nwt **44/26** (Actes 26), partagée entre Abdias et Jonas, a été corrigée dans `p8_ab1.py` (remplacée par **44/13**, Actes 13) et `FICHES8_ABDIAS_1.html` a été régénéré ; (2) le compteur des fiches publiées, décalé de 4 depuis §3ca (report de 462 au lieu de 466), est corrigé en cascade : §3ca **466**, §3cb **469**, §3cc **473**, §3cd **475**.
| Fiche | P | Sujet | État |
|---|---|---|---|
| JL424 | P424 | Joël 2:1-11 · « Le jour de Jéhovah est proche » : l'armée innombrable qui monte sur Sion (Joël 2:1-11) | PUBLIÉE |
| JL425 | P425 | Joël 2:12-27 · « Revenez à moi de tout votre cœur » : le cœur déchiré et les années rendues par les sauterelles (Joël 2:12-27) | PUBLIÉE |
| JL426 | P426 | Joël 2:28-32 · « Je répandrai mon esprit sur toute sorte de chair » : de la Pentecôte de l'an 33 au grand jour (Joël 2:28-32) | PUBLIÉE |
| JL427 | P427 | Joël 3:1-8 · Le verdict contre Tyr, Sidon et la Philistie : « vous avez vendu les fils de Juda aux Grecs » (Joël 3:1-8) | PUBLIÉE |
| JL428 | P428 | Joël 3:9-17 · « Multitudes, multitudes dans la vallée de la décision » : la faucille, le pressoir et le refuge (Joël 3:9-17) | PUBLIÉE |
| JL429 | P429 | Joël 3:18-21 · « Une source sortira de la maison de Jéhovah » : le pays arrosé et Juda habité pour toujours (Joël 3:18-21) | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Joël ») : JL424 Accomplie (1er accomplissement) / À venir · JL425 Accomplie (1er accomplissement) · JL426 Accomplie (1er accomplissement) · JL427 Accomplie · JL428 À venir · JL429 À venir. §3bu P8-73 ouvert — **Amos, première partie** (AM430-AM435, P430-P435 : le rugissement de Jéhovah depuis Sion, Damas et les nations jugées, l'oppression des justes, les maisons d'ivoire et la rencontre avec son Dieu).
Chapitres nwt : 23 paires réservées (12/8, 14/2, 19/36, 19/65, 19/76, 19/87, 23/22, 23/32, 23/51, 23/57, 23/58, 26/26, 26/28, 26/47, 32/3, 35/3, 37/2, 38/4, 44/12, 44/4, 45/10, 66/15, 66/16), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Joël », P424-P429) ; sources officielles conservées dans les fiches : 1200002482, 1200012428, 1200276265, 1951761, 2007722 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **23 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_jl1.py` — CAT JL2 + 6 fiches ; total **67 161 caractères de texte**, blocs > 700 car., **31 sources** officielles, Joël 2:1-11, Joël 2:12-27, Joël 2:28-32, Joël 3:1-8, Joël 3:9-17, Joël 3:18-21.
- S5/S6 : 7 JPG (trompette, repentir, esprit, ports, vallee, source + vignette `prophe_JL2_vignette.jpg`) ; 6 MP3 voice-05 = fiche_JL424_trompette.mp3, fiche_JL425_repentir.mp3, fiche_JL426_esprit.mp3, fiche_JL427_ports.mp3, fiche_JL428_vallee.mp3, fiche_JL429_source.mp3 — tous acceptés au premier essai (durées d'époque non reportées dans la reconstruction).
- Médias de la vague : JPG prophe_JL424_trompette.jpg, prophe_JL425_repentir.jpg, prophe_JL426_esprit.jpg, prophe_JL427_ports.jpg, prophe_JL428_vallee.jpg, prophe_JL429_source.jpg ; MP3 fiche_JL424_trompette.mp3, fiche_JL425_repentir.mp3, fiche_JL426_esprit.mp3, fiche_JL427_ports.mp3, fiche_JL428_vallee.mp3, fiche_JL429_source.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3bu. Vague P8-73 (AM1 — Amos 1-5 — les jugements des nations, l'oppression dénoncée et la rencontre avec Dieu)
| Fiche | P | Sujet | État |
|---|---|---|---|
| AM430 | P430 | Amos 1:3-15 · « À cause de trois transgressions… et à cause de quatre » : le rugissement de Sion contre Damas, Gaza, Tyr, Édom et Ammon | PUBLIÉE |
| AM431 | P431 | Amos 2:1-5 · Moab et Juda devant le même verdict : « j'enverrai un feu dans Juda, et il dévorera les palais de Jérusalem » | PUBLIÉE |
| AM432 | P432 | Amos 2:6-16 · « Ils vendent le juste pour de l'argent » : l'oppression dénoncée et la fuite impossible | PUBLIÉE |
| AM433 | P433 | Amos 3:1-15 · « Je vous ai connus, vous seuls » : les autels de Béthel, les maisons d'ivoire et le lion qui a rugi | PUBLIÉE |
| AM434 | P434 | Amos 4:1-13 · « Prépare-toi à rencontrer ton Dieu » : les génisses de Bashân et les calamités demeurées inutiles | PUBLIÉE |
| AM435 | P435 | Amos 5:1-27 · « Cherchez-moi et vous vivrez » : la vierge d'Israël tombée, les Pléiades et Orion, l'exil au-delà de Damas | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Amos — prophète de Tekoah, vers 804 av. n. è. ») : AM430 Accomplie · AM431 Accomplie · AM432 Accomplie · AM433 Accomplie · AM434 Accomplie · AM435 Accomplie. §3bv P8-74 ouvert — **Amos, seconde partie** (AM436-AM441, P436-P441 : l'ivoire et la ville de sang, le plomb sur la muraille, Amatsia et le sanctuaire, la corbeille de fruits d'été, la famine de la parole et la hutte de David relevée).
Chapitres nwt : 24 paires réservées (11/15, 11/17, 11/19, 12/3, 12/7, 14/15, 14/19, 14/24, 14/33, 14/34, 19/50, 19/94, 23/4, 23/42, 23/52, 23/64, 26/22, 26/35, 38/2, 39/2, 44/7, 45/3, 66/8, 7/7), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Amos — prophète de Tekoah, vers 804 av. n. è. », P430-P435) ; sources officielles conservées dans les fiches : 1200010251, 2007722 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **24 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_am1.py` — CAT AM1 + 6 fiches ; total **62 811 caractères de texte**, blocs > 700 car., **31 sources** officielles, Amos 1:3-15, Amos 2:1-5, Amos 2:6-16, Amos 3:1-15, Amos 4:1-13, Amos 5:1-27.
- S5/S6 : 7 JPG (damas, chaux, oppression, ivoire, rencontre, orion + vignette `prophe_AM1_vignette.jpg`) ; 6 MP3 voice-05 = fiche_AM430_damas.mp3, fiche_AM431_chaux.mp3, fiche_AM432_oppression.mp3, fiche_AM433_ivoire.mp3, fiche_AM434_rencontre.mp3, fiche_AM435_orion.mp3 — tous acceptés au premier essai (durées d'époque non reportées dans la reconstruction).
- Médias de la vague : JPG prophe_AM430_damas.jpg, prophe_AM431_chaux.jpg, prophe_AM432_oppression.jpg, prophe_AM433_ivoire.jpg, prophe_AM434_rencontre.jpg, prophe_AM435_orion.jpg ; MP3 fiche_AM430_damas.mp3, fiche_AM431_chaux.mp3, fiche_AM432_oppression.mp3, fiche_AM433_ivoire.mp3, fiche_AM434_rencontre.mp3, fiche_AM435_orion.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3bv. Vague P8-74 (AM2 — Amos 6-9 — le malheur des gens à l'aise, les visions du prophète et la hutte de David relevée)
| Fiche | P | Sujet | État |
|---|---|---|---|
| AM436 | P436 | Amos 6:1-14 · « Malheur à ceux qui sont à l'aise en Sion » : les lits d'ivoire, la coupe de vin et la grande maison réduite en ruines | PUBLIÉE |
| AM437 | P437 | Amos 7:1-9 · Les trois visions du prophète : les sauterelles dévorantes, le feu de l'abîme et le fil à plomb posé au milieu d'Israël | PUBLIÉE |
| AM438 | P438 | Amos 7:10-17 · Amos devant Amatsia : « je n'étais pas prophète… Jéhovah m'a pris de derrière le petit bétail » | PUBLIÉE |
| AM439 | P439 | Amos 8:1-10 · La corbeille de fruits d'été : « la fin est venue » ; le soleil se couchera en plein midi et les chants du palais deviendront des gémissements | PUBLIÉE |
| AM440 | P440 | Amos 8:11-14 · « Non pas la disette du pain, mais la faim d'entendre les paroles de Jéhovah » : les errants d'une mer à l'autre | PUBLIÉE |
| AM441 | P441 | Amos 9:1-15 · « Je relèverai la hutte de David tombée » : le crible qui ne perd aucun grain et la vigne replantée pour toujours | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Amos — prophète de Tekoah, vers 804 av. n. è. ») : AM436 Accomplie · AM437 Accomplie · AM438 Accomplie · AM439 Accomplie · AM440 Accomplie / À venir · AM441 Accomplie (1er accomplissement). §3bw P8-75 ouvert — **Abdias** (P442-P446 : l'orgueil d'Édom précipité, le jour de la calamité de Jacob, « comme tu as fait il te sera fait », les rescapés du mont Sion, les libérateurs et le royaume à Jéhovah).
Chapitres nwt : 24 paires réservées (11/10, 14/31, 14/32, 26/3, 26/48, 44/11, 44/15, 44/6, 44/8, 44/9, 45/1, 45/15, 45/2, 48/1, 60/1, 60/4, 61/1, 61/2, 66/1, 66/3, 66/4, 66/6, 8/2, 8/3), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Amos — prophète de Tekoah, vers 804 av. n. è. », P436-P441) ; sources officielles conservées dans les fiches : 1200010251 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **24 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_am2.py` — CAT AM2 + 6 fiches ; total **73 180 caractères de texte**, blocs > 700 car., **30 sources** officielles, Amos 6:1-14, Amos 7:1-9, Amos 7:10-17, Amos 8:1-10, Amos 8:11-14, Amos 9:1-15.
- S5/S6 : 7 JPG (ivoire, plomb, amatsia, corbeille, famine, hutte + vignette `prophe_AM2_vignette.jpg`) ; 6 MP3 voice-05 = fiche_AM436_ivoire.mp3, fiche_AM437_plomb.mp3, fiche_AM438_amatsia.mp3, fiche_AM439_corbeille.mp3, fiche_AM440_famine.mp3, fiche_AM441_hutte.mp3 — tous acceptés au premier essai (durées d'époque non reportées dans la reconstruction).
- Médias de la vague : JPG prophe_AM436_ivoire.jpg, prophe_AM437_plomb.jpg, prophe_AM438_amatsia.jpg, prophe_AM439_corbeille.jpg, prophe_AM440_famine.jpg, prophe_AM441_hutte.jpg ; MP3 fiche_AM436_ivoire.mp3, fiche_AM437_plomb.mp3, fiche_AM438_amatsia.mp3, fiche_AM439_corbeille.mp3, fiche_AM440_famine.mp3, fiche_AM441_hutte.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3bw. Vague P8-75 (AB — Abdias — l'orgueil d'Édom précipité, la violence contre Jacob et le royaume qui revient à Jéhovah)
| Fiche | P | Sujet | État |
|---|---|---|---|
| AB442 | P442 | Abdias 1-9 · « L'orgueil de ton cœur t'a égaré » : le creux des rochers, le nid de l'aigle et les sages de Téman | PUBLIÉE |
| AB443 | P443 | Abdias 10-14 · « À cause de la violence faite à ton frère Jacob » : le jour où Édom se tint à l'écart et livra les rescapés | PUBLIÉE |
| AB444 | P444 | Abdias 15, 16 · « Comme tu as fait, il te sera fait » : le jour de Jéhovah sur toutes les nations et la coupe bue sur la montagne sainte | PUBLIÉE |
| AB445 | P445 | Abdias 17-20 · « Sur le mont Sion il y aura des rescapés » : la maison de Jacob comme un feu, Joseph comme une flamme et le retour des captifs | PUBLIÉE |
| AB446 | P446 | Abdias 21 · « Des libérateurs monteront sur le mont Sion… et le royaume sera à Jéhovah » : la conclusion du livre d'Abdias | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Abdias — prophète d'Édom, vers 607 av. n. è. ») : AB442 Accomplie · AB443 Accomplie · AB444 Accomplie / À venir · AB445 Accomplie (1er accomplissement) · AB446 À venir. §3bx P8-76 ouvert — **Jonas** (JN447-JN450 : « lève-toi, va à Ninive », les quarante jours et la repentance, la miséricorde de Dieu pour la grande ville, et le signe de Jonas appliqué au Fils de l'homme).
Chapitres nwt : 20 paires réservées (1/25, 1/27, 1/36, 18/39, 19/108, 19/60, 26/40, 44/13, 44/17, 44/20, 44/22, 45/12, 45/13, 45/14, 45/4, 45/6, 46/1, 46/2, 48/3, 60/5), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Abdias — prophète d'Édom, vers 607 av. n. è. », P442-P446) ; sources officielles conservées dans les fiches : 1101986085, 1200010251, 1200274174, 1200274175, 1989289 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **20 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_ab1.py` — CAT AB + 5 fiches ; total **54 947 caractères de texte**, blocs > 700 car., **30 sources** officielles, Abdias 1-9, Abdias 10-14, Abdias 15, 16, Abdias 17-20, Abdias 21.
- S5/S6 : 6 JPG (sela, carrefour, coupe, sion, liberateurs + vignette `prophe_AB1_vignette.jpg`) — 6/6 au premier essai, aucun refus ; 5/5 MP3 voice-05 = 31,1 · 30,7 · 27,0 · 32,8 · 31,2 s = **152,8 s**, tous acceptés au premier essai ; 24 pistes avant purge.
- S7 : build final `preuves/FICHES8_ABDIAS_1.html` 130 Ko — 63 mentions wol (30×2 + 3 en clair), 5 balises audio, 11 images, 11 blocs par fiche, 10 fichiers médias liés tous présents, 0 lien non officiel ; purge P8-74 motifs exacts (6 JPG AM436-AM441 + `prophe_AM2_vignette.jpg` + 6 MP3 homonymes) → fenêtre **18 JPG / 17 MP3** ; `collections/durations.py` régénéré → 17 pistes / **617,4 s**. Correction d'intégrité (2026-09-26) : `p8_ab1.py` corrigé (44/26 → **44/13**) et livrable régénéré (**133 707 o**, 63 mentions wol, 5 lecteurs audio, 11 images) ; Jonas conserve 44/26, citée dans son texte.
- S8 : §3bw 5/5 PUBLIÉE → **446/1000** ; compteurs : **480 JPG créés** (18 présents dont vignette AB1), **457 MP3** (17 pistes).
- Médias de la vague : JPG prophe_AB442_sela.jpg, prophe_AB443_carrefour.jpg, prophe_AB444_coupe.jpg, prophe_AB445_sion.jpg, prophe_AB446_liberateurs.jpg ; MP3 fiche_AB442_sela.mp3, fiche_AB443_carrefour.mp3, fiche_AB444_coupe.mp3, fiche_AB445_sion.mp3, fiche_AB446_liberateurs.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3bx. Vague P8-76 (JN — Jonas — Ninive, les quarante jours et le signe du Fils de l'homme)
| Fiche | P | Sujet | État |
|---|---|---|---|
| JN447 | P447 | Jonas 1:1-17 · « Lève-toi, va à Ninive, la grande ville » : la fuite vers Tarsis, la tempête et le grand poisson | PUBLIÉE |
| JN448 | P448 | Jonas 3:1-10 · « Encore quarante jours, et Ninive sera renversée » : la repentance du roi, du peuple et des bêtes | PUBLIÉE |
| JN449 | P449 | Jonas 4:1-11 · « Je savais que tu es un Dieu miséricordieux » : la cabane, le ricin et la dernière question posée au prophète | PUBLIÉE |
| JN450 | P450 | Matthieu 12:39, 40 ; 16:4 ; Luc 11:29, 30 · « Le signe de Jonas » : trois jours et trois nuits dans le cœur de la terre | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Jonas — prophète, vers 844 av. n. è. ») : JN447 Accomplie (mission exécutée) · JN448 Accomplie (délai écoulé sans ruine, après repentance) · JN449 Accomplie · JN450 Accomplie. §3by P8-77 ouvert — **Michée, première partie** (MI451-MI456, P451-P456 : Samarie en tas de ruines, ne l'annoncez pas à Gath, malheur à ceux qui complotent l'injustice, Sion labourée comme un champ, la montagne de la maison élevée avec les socs et les épées, le rassemblement de la boiteuse).
Chapitres nwt : 16 paires réservées (19/139, 19/86, 2/34, 2/9, 32/1, 32/4, 38/3, 40/12, 40/16, 42/11, 44/10, 44/26, 45/5, 46/13, 48/2, 62/1), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Jonas — prophète, vers 844 av. n. è. », P447-P450) ; sources officielles conservées dans les fiches : 1200001701, 1200012450, 1200013190, 1976207 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **16 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_jn1.py` — CAT JN + 4 fiches ; total **50 343 caractères de texte**, blocs > 700 car., **20 sources** officielles, Jonas 1:1-17, Jonas 3:1-10, Jonas 4:1-11, Matthieu 12:39, 40 ; 16:4 ; Luc 11:29, 30.
- S5/S6 : 5 JPG (ninive, repentir, ricin, signe + vignette `prophe_JN1_vignette.jpg`) — 5/5 au premier essai, aucun refus ; 4/4 MP3 voice-05 = 32,6 · 33,2 · 35,1 · 29,2 s = **130,1 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_JONAS_1.html` 117 Ko (**120 503 o**) — 43 mentions wol (20×2 + 3 en clair), 4 balises audio, 9 images, 11 blocs par fiche, 8 fichiers médias liés tous présents, 0 lien non officiel ; purge P8-75 motifs exacts (5 JPG AB442-AB446 + `prophe_AB1_vignette.jpg` + 5 MP3 homonymes) → fenêtre **17 JPG / 16 MP3** ; `collections/durations.py` régénéré → 16 pistes / **592,8 s**. Jonas conserve la paire 44/26 (Actes 26), citée dans sa chronologie ; la correction d'intégrité du 2026-09-26 porte sur Abdias.
- S8 : §3bx 4/4 PUBLIÉE → **450/1000** ; compteurs : **485 JPG créés** (17 présents dont vignette JN1), **461 MP3** (16 pistes).
- Médias de la vague : JPG prophe_JN447_ninive.jpg, prophe_JN448_repentir.jpg, prophe_JN449_ricin.jpg, prophe_JN450_signe.jpg ; MP3 fiche_JN447_ninive.mp3, fiche_JN448_repentir.mp3, fiche_JN449_ricin.mp3, fiche_JN450_signe.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3by. Vague P8-77 (MI1 — Michée 1-4 — Samarie et Sion jugées, la montagne élevée et le rassemblement de la boiteuse)
| Fiche | P | Sujet | État |
|---|---|---|---|
| MI451 | P451 | Michée 1:2-9 · « Je ferai de Samarie un tas de pierres dans un champ » : la plaie qui atteint jusqu'à la porte de Jérusalem | PUBLIÉE |
| MI452 | P452 | Michée 1:10-16 · « Ne l'annoncez pas à Gath » : la complainte sur les villes de Juda et le jeu des noms de la poussière | PUBLIÉE |
| MI453 | P453 | Michée 2:1-13 · « Malheur à ceux qui complotent l'injustice » : les champs convoités, le cordeau tiré et le rassemblement du reste | PUBLIÉE |
| MI454 | P454 | Michée 3:1-12 · « Sion sera labourée comme un champ » : les juges pour des présents, les prophètes pour de l'argent et la montagne du temple couverte de forêt | PUBLIÉE |
| MI455 | P455 | Michée 4:1-5 · « La montagne de la maison de Jéhovah sera élevée » : les nations qui affluent et les épées forgées en socs | PUBLIÉE |
| MI456 | P456 | Michée 4:6-13 · « Je rassemblerai celle qui boite » : la tour du troupeau, la captivité à Babylone et la corne de fer de la fille de Sion | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Michée — prophète, avant 717 av. n. è. ») : MI451 Accomplie · MI452 Accomplie · MI453 Accomplie · MI454 Accomplie · MI455 En cours · MI456 Accomplie. §3bz P8-78 ouvert — **Michée, seconde partie** (MI457-MI462, P457-P462 : Bethléem et celui dont l'origine remonte aux temps anciens, le reste comme la rosée, chevaux et idoles retranchés, le procès de Jéhovah et les balances fausses, le fils qui méprise le père, « qui est un Dieu comme toi » et les péchés jetés dans les profondeurs de la mer).
Chapitres nwt : 24 paires réservées (10/22, 13/11, 16/2, 17/9, 18/12, 19/102, 19/27, 19/47, 19/68, 19/72, 20/8, 21/3, 26/38, 4/25, 4/33, 4/36, 44/21, 44/23, 44/28, 48/6, 49/5, 6/21, 7/4, 9/7), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Michée — prophète, avant 717 av. n. è. », P451-P456) ; sources officielles conservées dans les fiches : 1102000024, 1200003033, 1200012964 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **24 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_mi1.py` — CAT MI1 + 6 fiches ; total **71 130 caractères de texte**, blocs > 700 car., **30 sources** officielles, Michée 1:2-9, Michée 1:10-16, Michée 2:1-13, Michée 3:1-12, Michée 4:1-5, Michée 4:6-13.
- S5/S6 : 7 JPG (samarie, lakish, heritage, labour, montagne, boiteuse + vignette `prophe_MI1_vignette.jpg`) — 7/7 au premier essai, aucun refus ; 6/6 MP3 voice-05 = 11,7 · 10,9 · 13,2 · 12,7 · 12,2 · 12,3 s = **73,0 s** (scripts volontairement resserrés sur l'essentiel de chaque fiche), tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_MICHEE_1.html` 164 Ko (**168 143 o**) — 63 mentions wol, 6 balises audio, 13 images, 11 blocs par fiche, 12 fichiers médias liés tous présents (6 JPG + 6 MP3), 0 lien non officiel ; purge P8-76 motifs exacts (4 JPG JN447-JN450 + `prophe_JN1_vignette.jpg` + 4 MP3 homonymes) → fenêtre **19 JPG / 18 MP3** ; `collections/durations.py` régénéré → 18 pistes / **535,7 s**.
- S8 : §3by 6/6 PUBLIÉE → **456/1000** ; compteurs : **492 JPG créés** (19 présents dont vignette MI1), **467 MP3** (18 pistes).
- Médias de la vague : JPG prophe_MI451_samarie.jpg, prophe_MI452_lakish.jpg, prophe_MI453_heritage.jpg, prophe_MI454_labour.jpg, prophe_MI455_montagne.jpg, prophe_MI456_boiteuse.jpg ; MP3 fiche_MI451_samarie.mp3, fiche_MI452_lakish.mp3, fiche_MI453_heritage.mp3, fiche_MI454_labour.mp3, fiche_MI455_montagne.mp3, fiche_MI456_boiteuse.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3bz. Vague P8-78 (MI2 — Michée 5-7 — Bethléem et celui dont l'origine remonte aux temps anciens, le procès de Jéhovah et le pardon des péchés)
| Fiche | P | Sujet | État |
|---|---|---|---|
| MI457 | P457 | Michée 5:2 · « Et toi, Bethléhem Éphrata… » : la petite ville des milliers de Juda, le berger David et celui dont l'origine remonte aux temps anciens | PUBLIÉE |
| MI458 | P458 | Michée 5:4-8 · « Il se tiendra et il paîtra avec la force de Jéhovah » : celui qui est la paix, le reste comme la rosée et comme un lion | PUBLIÉE |
| MI459 | P459 | Michée 5:9-15 · « Je retrancherai tes chevaux et je démolirai tes forteresses » : l'appareil de guerre, les sorcelleries et les poteaux sacrés ôtés du milieu du… | PUBLIÉE |
| MI460 | P460 | Michée 6:1-16 · Le procès de Jéhovah : les montagnes appelées à entendre, l'épha réduit, les balances fausses et les statuts d'Omri | PUBLIÉE |
| MI461 | P461 | Michée 7:1-7 · « Mais moi, je guetterai Jéhovah » : l'homme de bonté disparu du pays, le fils qui méprise le père et le Dieu qui entend | PUBLIÉE |
| MI462 | P462 | Michée 7:8-20 · « Qui est un Dieu comme toi ? » : mon ennemie tombera, les murs seront rebâtis et les péchés jetés dans les profondeurs de la mer | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Michée — prophète, avant 717 av. n. è. ») : MI457 Accomplie · MI458 Accomplie / À venir · MI459 Accomplie / À venir · MI460 Accomplie · MI461 Accomplie (citation) · MI462 Accomplie (1er accomplissement) / À venir. §3ca P8-79 ouvert — **Nahoum, première partie** (NA463-NA466, P463-P466 : la vengeance de Jéhovah et le flot débordant, « voici sur les montagnes les pieds du porteur de bonnes nouvelles », le bouclier rouge et les portes des fleuves, « où est le repaire des lions ? »).
Chapitres nwt : 24 paires réservées (16/13, 16/4, 16/8, 19/132, 20/11, 20/20, 3/19, 40/10, 42/2, 42/24, 43/1, 43/13, 43/7, 5/17, 52/4, 58/11, 58/6, 6/24, 64/1, 65/1, 66/2, 7/17, 7/18, 9/16), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Michée — prophète, avant 717 av. n. è. », P457-P462) ; sources officielles conservées dans les fiches : 1102017573, 1200003033, 1200012964, 1994765, 2011242 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **24 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_mi2.py` — CAT MI2 + 6 fiches ; total **72 284 caractères de texte**, blocs > 700 car., **30 sources** officielles, Michée 5:2, Michée 5:4-8, Michée 5:9-15, Michée 6:1-16, Michée 7:1-7, Michée 7:8-20.
- S5/S6 : 7 JPG (bethlehem, berger, idoles, balances, guetteur, pardon + vignette `prophe_MI2_vignette.jpg`) — 7/7 au premier essai, aucun refus ; 6/6 MP3 voice-05 = 11,5 · 11,7 · 12,8 · 13,1 · 12,8 · 13,3 s = **75,2 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_MICHEE_2.html` 165 Ko (**163 538 o** au build ; **169 286 o** revérifiés le 2026-09-26) — 63 mentions wol, 6 balises audio, 13 images, 11 blocs par fiche, 12 fichiers médias liés tous présents (6 JPG + 6 MP3), 0 lien non officiel ; purge P8-77 motifs exacts (6 JPG MI451-MI456 + `prophe_MI1_vignette.jpg` + 6 MP3 homonymes) → fenêtre **19 JPG / 18 MP3** ; `collections/durations.py` régénéré → 18 pistes / **537,9 s**.
- S8 : §3bz 6/6 PUBLIÉE → **462/1000** ; compteurs : **499 JPG créés** (19 présents dont vignette MI2), **473 MP3** (18 pistes).
- Médias de la vague : JPG prophe_MI457_bethlehem.jpg, prophe_MI458_berger.jpg, prophe_MI459_idoles.jpg, prophe_MI460_balances.jpg, prophe_MI461_guetteur.jpg, prophe_MI462_pardon.jpg ; MP3 fiche_MI457_bethlehem.mp3, fiche_MI458_berger.mp3, fiche_MI459_idoles.mp3, fiche_MI460_balances.mp3, fiche_MI461_guetteur.mp3, fiche_MI462_pardon.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3ca. Vague P8-79 (NA1 — Nahum 1-2 — La vengeance de Jéhovah, le porteur de bonnes nouvelles et la chute de Ninive)
| Fiche | P | Sujet | État |
|---|---|---|---|
| NA463 | P463 | Nahum 1:2-8 · « Par l'inondation qui passe, il fera une extermination » : le Dieu lent à la colère, maître des mers, forteresse au jour de la détresse | PUBLIÉE |
| NA464 | P464 | Nahum 1:9-15 · « Voici sur les montagnes les pieds du porteur de bonnes nouvelles » : le joug brisé, les fêtes de Juda et la fin de l'oppresseur | PUBLIÉE |
| NA465 | P465 | Nahum 2:1-10 · « Les portes des fleuves sont ouvertes et le palais se fond » : le bouclier rouge, les chars dans les rues et le pillage de Ninive | PUBLIÉE |
| NA466 | P466 | Nahum 2:11-13 · « Où est le repaire des lions ? » : le lion dévoré par l'épée, les chars brûlés et les messagers réduits au silence | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Nahum — prophète, avant 632 av. n. è. ») : NA463 Accomplie · NA464 Accomplie · NA465 Accomplie · NA466 Accomplie. §3cb P8-80 ouvert — **Nahum 3, fin du livre** (NA467-NA469, P467-P469 : la ville de sang et les jupes relevées, « es-tu meilleure que No-Amôn ? » et le sac de Thèbes en 663 av. n. è. (date neutre), « puise de l'eau », le feu qui dévore, la blessure incurable et la ville jamais relevée).
Chapitres nwt : 16 paires réservées (10/1, 14/1, 18/1, 21/1, 41/11, 46/15, 47/1, 49/1, 50/1, 51/1, 53/1, 54/1, 55/1, 56/1, 59/2, 9/1), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : recherches et lecture du registre (section « Nahum — prophète, avant 632 av. n. è. », P463-P466) ; sources officielles conservées dans les fiches : 1101990095, 1200000447, 1960165, 1981648 (détail du journal d'époque non reporté).
- S2 : recensement régénéré → **16 paires réservées** dans le stock libre, **0 doublon interne** ; contrôle re-vérifié le 2026-09-26 : 0 collision.
- S3 / QC : `data/p8_na1.py` — CAT NA1 + 4 fiches ; total **49 884 caractères de texte**, blocs > 700 car., **20 sources** officielles, Nahum 1:2-8, Nahum 1:9-15, Nahum 2:1-10, Nahum 2:11-13.
- S5/S6 : 5 JPG (flot, messager, siege, lions + vignette `prophe_NA1_vignette.jpg`) — 5/5 au premier essai, aucun refus ; 4/4 MP3 voice-05 = 13,9 · 13,2 · 13,0 · 10,6 s = **50,7 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_NAHOUM_1.html` 118 Ko (**117 240 o** au build ; **120 882 o** revérifiés le 2026-09-26) — 43 mentions wol, 4 balises audio, 9 images, 11 blocs par fiche, 8 fichiers médias liés tous présents (4 JPG + 4 MP3), 0 lien non officiel ; purge P8-78 motifs exacts (6 JPG MI457-MI462 + `prophe_MI2_vignette.jpg` + 6 MP3 homonymes) → fenêtre **17 JPG / 16 MP3** ; `collections/durations.py` régénéré → 16 pistes / **513,4 s**.
- S8 : §3ca 4/4 PUBLIÉE → **466/1000** (compteur corrigé ; l'état d'origine portait 462 par erreur de report) ; compteurs : **504 JPG créés** (17 présents dont vignette NA1), **477 MP3** (16 pistes).
- Médias de la vague : JPG prophe_NA463_flot.jpg, prophe_NA464_messager.jpg, prophe_NA465_siege.jpg, prophe_NA466_lions.jpg ; MP3 fiche_NA463_flot.mp3, fiche_NA464_messager.mp3, fiche_NA465_siege.mp3, fiche_NA466_lions.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3cb. Vague P8-80 (NA2 — Nahum 3 — La ville de sang, No-Amôn et la blessure incurable)
| Fiche | P | Sujet | État |
|---|---|---|---|
| NA467 | P467 | Nahum 3:1-7 · « Malheur à la ville de sang ! » : le fouet, les cadavres entassés et la prostituée maîtresse de sorcelleries dépouillée devant les nations | PUBLIÉE |
| NA468 | P468 | Nahum 3:8-13 · « Es-tu meilleure que No-Amôn ? » : Thèbes assise au bord du Nil, Koush et l'Égypte, Put et les Libyens, puis les figuiers précoces | PUBLIÉE |
| NA469 | P469 | Nahum 3:14-19 · « Il n'y a pas de remède à ta blessure » : puise de l'eau pour le siège, les sauterelles qui s'envolent, les bergers qui sommeillent et la ville… | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Nahum — prophète, avant 632 av. n. è. ») : NA467 Accomplie · NA468 Accomplie · NA469 Accomplie. §3cc P8-81 ouvert — **Habacuc, première partie** (HA470-HA473, P470-P473 : jusqu'à quand, ô Jéhovah ? le tumulte et la violence, la réponse « regardez les nations et soyez stupéfaits », le juste vivra par sa fidélité, le malheur à qui amasse par la rapine, les cinq malheurs et la connaissance de la gloire de Jéhovah).
Chapitres nwt : 12 paires réservées (1/4, 17/3, 19/3, 19/5, 2/2, 21/2, 4/35, 5/1, 5/5, 6/2, 7/3, 9/2), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : 3 recherches approfondies (Nahum 3:1-7 — « malheur à la ville de sang », le fouet et les cadavres, la prostituée maîtresse de sorcelleries, la nudité montrée aux nations et l'absence de consolateurs ; Nahum 3:8-13 — « es-tu meilleure que No-Amôn ? », Thèbes assise au bord du Nil, le sac par Assurbanipal en 663 av. n. è., les figuiers précoces, la datation du livre entre 663 et 632/612 ; Nahum 3:14-19 — le moule à briques, le feu, les sauterelles qui s'envolent, la blessure incurable et les applaudissements) + lecture du registre (section « Nahum », P467-P469) ; documents wol : réutilisation des 4 documents vérifiés en P8-79 (**1101990095**, **1960165**, **1200000447** employés dans ce module ; 1981648 cité en note) et rappel du contexte de 663 av. n. è. (date neutre du registre).
- Faits retenus : No-Amôn = « la ville d'Amôn », c'est-à-dire Thèbes (Jérémie 46:25 ; Ézéchiel 30:14-16 emploient « No ») ; le sac de Thèbes par Assurbanipal en 663 av. n. è. est présenté comme un fait passé, ce qui fournit le terminus a quo du livre ; les alliés nommés — Koush, l'Égypte, Put, les Libyens — correspondent à la XXVe dynastie nubienne ; les travaux de réfection des murailles de briques crues (eau, boue, argile, moule) sont des opérations réelles de siège ; Ninive ne fut jamais relevée, Xénophon n'en voit que des ruines en 401 av. n. è.
- S2 : recensement régénéré (632 paires consommées hors module) → contrôle en masse des candidats thématiques : **tous les miroirs proches déjà pris** (Isaïe 47, Jérémie 46/50-51, Lamentations 1-5, Ézéchiel 16/23/29/30, Sophonie 1-3, Révélation 16-20) ; **12 paires retenues** dans le stock restant : 19/5, 1/4, 5/5, 4/35 (NA467) ; 5/1, 6/2, 2/2, 9/2 (NA468) ; 7/3, 17/3, 19/3, 21/2 (NA469).
- S3 : `data/p8_na2.py` — CAT NA2 + NA467 (lot 1) puis NA468-469 (lot 2) concaténés ; 1 coquille corrigée (« PREUves » → « PREUVES ») et 1 chaîne multiligne corrigée dans le `schema` de NA469.
- QC : 3 fiches = **7 783 caractères de texte** (blocs 919 à 1 625 car., tous > 700) ; src 15 (5 par fiche), toutes officielles ; tl 6, accomplissement 6, texte 2 blocs par fiche ; **12 chapitres nwt tous uniques**, 0 doublon avec les 632 autres paires du corpus ; 0 cyrillique/CJK ; statuts conformes au registre (3 « Accomplie », mention « sac de Thèbes en 663 av. n. è. (date neutre) » conservée mot pour mot).
- S4 : build de contrôle `_TMP_NA2.html` 89 Ko — validation OK (11 blocs, 3 fiches, 15 sources).
- S5/S6 : 4 JPG (ville_sang, thebes, briques + vignette `prophe_NA2_vignette.jpg`) — 4/4 au premier essai, aucun refus ; 3/3 MP3 voice-05 = 14,5 · 12,5 · 14,2 s = **41,2 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_NAHOUM_2.html` 90 Ko (**90 339 o** au build ; **93 110 o** revérifiés le 2026-09-26) — 33 mentions wol, 3 balises audio, 7 images, 11 blocs par fiche, 6 fichiers médias liés tous présents (3 JPG + 3 MP3), 0 lien non officiel ; purge P8-79 motifs exacts (4 JPG NA463-NA466 + `prophe_NA1_vignette.jpg` + 4 MP3 homonymes) → fenêtre **16 JPG / 15 MP3** ; `collections/durations.py` régénéré → 15 pistes / **503,9 s**.
- S8 : §3cb 3/3 PUBLIÉE → **469/1000** (compteur corrigé) ; **le livre de Nahum est clos au registre (dernière entrée P469)** ; compteurs : **508 JPG créés** (16 présents dont vignette NA2), **480 MP3** (15 pistes).
- Médias de la vague : JPG prophe_NA467_ville_sang.jpg, prophe_NA468_thebes.jpg, prophe_NA469_briques.jpg ; MP3 fiche_NA467_ville_sang.mp3, fiche_NA468_thebes.mp3, fiche_NA469_briques.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3cc. Vague P8-81 (HA1 — Habacuc 1-2 — Jusqu'à quand ? les Chaldéens, le juste vivra par sa fidélité et les malheurs sur Babylone)
| Fiche | P | Sujet | État |
|---|---|---|---|
| HA470 | P470 | Habacuc 1:5-11 · « Regardez parmi les nations et soyez stupéfaits » : les Chaldéens, les chevaux plus rapides que les léopards et les prisonniers ramassés comme… | PUBLIÉE |
| HA471 | P471 | Habacuc 1:12-17 · « Tes yeux sont trop purs pour voir le mal » : le méchant qui avale un plus juste que lui, l'hameçon et les filets | PUBLIÉE |
| HA472 | P472 | Habacuc 2:1-4 · « Écris la vision… car le juste vivra par sa fidélité » : la réponse du poste de garde et le verset cité trois fois dans les Écritures grecques | PUBLIÉE |
| HA473 | P473 | Habacuc 2:5-17 · « Malheur à celui qui amasse le butin d'autrui » : les malheurs sur le Chaldéen, la pierre qui crie du mur et la gloire qui remplit la terre | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Habacuc — prophète, vers 628 av. n. è. ») : HA470 Accomplie · HA471 Accomplie · HA472 Accomplie / En cours · HA473 Accomplie. §3cd P8-82 ouvert — **Habacuc, seconde partie** (HA474-HA475 : le malheur à celui qui dit au bois « réveille-toi » et le silence devant Jéhovah dans son saint temple, puis la prière du chapitre 3 : Dieu vient de Théman, sa splendeur couvre les cieux, les montagnes éternelles s'écroulent, « l'Éternel est ma force »).
Chapitres nwt : 16 paires réservées (19/4, 19/73, 20/3, 20/4, 46/3, 47/2, 47/3, 48/4, 5/2, 58/10, 59/1, 59/4, 6/3, 62/3, 7/1, 7/2), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : 4 recherches approfondies (Habacuc 1:1-11 — « jusqu'à quand, ô Jéhovah ? », la violence, la loi sans force, puis la réponse : les Chaldéens, « nation amère et impétueuse », chevaux plus rapides que les léopards, loups du soir, aigle sur sa proie, prisonniers comme du sable ; Habacuc 1:12-17 — « n'es-tu pas dès les temps anciens ? », le méchant qui avale un plus juste que lui, l'hameçon, le filet, la senne et le sacrifice au filet ; Habacuc 2:1-4 — le poste de garde, « écris la vision… afin que celui qui la lit la lise couramment », le temps fixé qui ne mentira pas, « le juste vivra par sa fidélité » cité en Romains 1:17, Galates 3:11 et Hébreux 10:36-39 ; Habacuc 2:5-17 — les malheurs, « la pierre crie depuis la muraille », 2:14, le renversement de Babylone en 539 av. n. è.) + lecture du registre (section « Habacuc — prophète, vers 628 av. n. è. », P470-P475) ; documents wol relevés et vérifiés (200) : 1101990096, 1200011742, 2000083, 1981569 ; portail 35 trouvé par recherche (1200011742).
- S2 : recensement régénéré (modules clos = **644 paires**) → **16 paires réservées dans les 71 libres** : 19/4, 5/2, 6/3, 7/2 (HA470) ; 19/73, 20/3, 20/4, 7/1 (HA471) ; 58/10, 59/1, 62/3, 48/4 (HA472) ; 47/2, 47/3, 46/3, 59/4 (HA473). Test en masse avant rédaction : **16 chapitres uniques**, 0 doublon interne, 0 collision avec les 644.
- S3 : `data/p8_ha1.py` — chunk `_ha1a.py` (CAT HA1 + HA470 + HA471) concaténé avec `_ha1b.py` (HA472 + HA473), chunks supprimés ; 0 coquille détectée (contrôle des collages) ; 1 schéma complété (celui de HA472, porté au-delà de 700 caractères).
- S4 : build de contrôle `_TMP_HA1.html` 116 Ko — validation OK (11 blocs, 4 fiches, 20 sources) ; supprimé après contrôle.
- S5/S6 : 5 JPG (chaldeens, filets, vision, pierre + vignette `prophe_HA1_vignette.jpg`) — 5/5 au premier essai, aucun refus ; 4/4 MP3 voice-05 = 13,5 · 12,1 · 12,0 · 11,6 s = **49,2 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_HABACUC_1.html` 118 Ko (**120 713 o**, revérifié le 2026-09-26) — 43 mentions wol, 4 balises audio, 9 images, 11 blocs par fiche, 8 fichiers médias liés tous présents (4 JPG + 4 MP3), 0 lien non officiel ; purge P8-80 motifs exacts (4 JPG NA467-NA469 + `prophe_NA2_vignette.jpg` + 3 MP3 homonymes) → fenêtre **17 JPG / 16 MP3** ; `collections/durations.py` régénéré → **16 pistes / 511,9 s**.
- S8 : §3cc 4/4 PUBLIÉE → **473/1000** (compteur corrigé) ; compteurs : **513 JPG créés** (17 présents dont vignette HA1), **484 MP3** (16 pistes).
- Médias de la vague : JPG prophe_HA470_chaldeens.jpg, prophe_HA471_filets.jpg, prophe_HA472_vision.jpg, prophe_HA473_pierre.jpg ; MP3 fiche_HA470_chaldeens.mp3, fiche_HA471_filets.mp3, fiche_HA472_vision.mp3, fiche_HA473_pierre.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3cd. Vague P8-82 (HA2 — Habacuc 2:18-20 et 3 — L'idole muette, le silence devant Jéhovah et la prière du prophète)
| Fiche | P | Sujet | État |
|---|---|---|---|
| HA474 | P474 | Habacuc 2:18-20 · « Malheur à celui qui dit au bois : réveille-toi ! » : l'idole muette, l'or et l'argent sans souffle, et Jéhovah dans son saint temple | PUBLIÉE |
| HA475 | P475 | Habacuc 3:1-19 · « Le Souverain Seigneur Jéhovah est ma force » : la prière de Habacuc, Dieu venant de Théman, les montagnes éternelles brisées et les pieds… | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Habacuc — prophète, vers 628 av. n. è. ») : HA474 Accomplie / À venir · HA475 À venir. §3ce P8-83 ouvert — **Sophonie, première partie** (SO476-SO478, P476-P478 : « je supprimerai tout de dessus la surface du sol », le jour de Jéhovah proche et les princes punis, « un jour de détresse » où ni l'argent ni l'or ne délivrent).
Chapitres nwt : 8 paires réservées (19/135, 19/77, 19/84, 19/93, 19/98, 43/4, 46/10, 62/5), toutes uniques — contrôle re-vérifié le 2026-09-26 : 0 collision avec le corpus hors module.
- S1 : 4 recherches approfondies (Habacuc 2:18-20 — la statue sculptée et la statue moulée, « malheur à celui qui dit au bois : réveille-toi ! », l'or et l'argent sans souffle, Jéhovah dans son saint temple et le silence de toute la terre ; Habacuc 3:1-10 — la prière « sous forme de complaintes », « ravive ton œuvre au milieu des années », Dieu venant de Théman et le Saint du mont Paran, les rayons de sa main, la peste et la fièvre ; Habacuc 3:8-15 — les chevaux et les chars victorieux, les fleuves et la mer, le soleil et la lune arrêtés, « tu es sorti pour le salut de ton peuple, pour sauver ton oint » ; Habacuc 3:16-19 — l'effroi du prophète, le figuier stérile et la vigne sans récolte, « j'exulterai en Jéhovah », les pieds comme ceux des biches) + lecture du registre (section « Habacuc — prophète, vers 628 av. n. è. », P474-P475) ; lecture de la section suivante du registre (**Sophonie — prophète, avant 648 av. n. è.**, P476-P484) pour ouvrir §3ce.
- S2 : recensement régénéré (modules clos = **660 paires**) → **8 paires réservées dans la liste des libres** : 19/135, 46/10, 62/5, 43/4 (HA474) ; 19/77, 19/93, 19/98, 59/5 (HA475). Test en masse avant rédaction : 8 chapitres uniques, 0 doublon interne, 0 collision avec les 660.
- S3 : `data/p8_ha2.py` — chunk `_ha2a.py` (CAT HA2 + HA474) concaténé avec `_ha2b.py` (HA475), chunks supprimés ; 1 correction (marqueur de rédaction « SHADDAI? » remplacé par « SHADDAI… LE TOUT-PUISSANT »).
- QC : 2 fiches = **29 049 caractères de texte** (HA474 13 141 ; HA475 15 908) ; blocs de prose tous > 700 car. (831 à 2 147) ; src 5 par fiche (10, toutes officielles), tl 6 et 7, accomplissement 6, texte 2 blocs par fiche ; 0 collage, 0 cyrillique/CJK ; statuts conformes au registre (« Accomplie / À venir » pour HA474, « À venir » pour HA475).
- S4 : build de contrôle `_TMP_HA2.html` 74 Ko — validation OK (11 blocs, 2 fiches, 10 sources) ; supprimé après contrôle.
- S5/S6 : 3 JPG (idole, biches + vignette `prophe_HA2_vignette.jpg`) — 3/3 au premier essai, aucun refus ; 2/2 MP3 voice-05 = 11,3 · 14,6 s = **25,9 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_HABACUC_2.html` 75 Ko (**76 568 o**, revérifié le 2026-09-26) — 23 mentions wol, 2 balises audio, 5 images, 11 blocs par fiche, 4 fichiers médias liés tous présents (2 JPG + 2 MP3), 0 lien non officiel ; purge P8-81 motifs exacts (4 JPG HA470-HA473 + `prophe_HA1_vignette.jpg` + 4 MP3 homonymes) → fenêtre **15 JPG / 14 MP3** ; `collections/durations.py` régénéré → **14 pistes / 488,6 s**.
- S8 : §3cd 2/2 PUBLIÉE → **475/1000** (compteur corrigé) ; compteurs : **516 JPG créés** (15 présents dont vignette HA2), **486 MP3** (14 pistes) ; **le livre de Habacuc est clos au registre (dernière entrée P475)**.
- Médias de la vague : JPG prophe_HA474_idole.jpg, prophe_HA475_biches.jpg ; MP3 fiche_HA474_idole.mp3, fiche_HA475_biches.mp3 (purgés selon la fenêtre glissante à la vague suivante).

## 3ce. Vague P8-83 (SO1 — Sophonie 1 : le jour de Jéhovah proche et le silence devant le Souverain Seigneur)
| Fiche | P | Sujet | État |
|---|---|---|---|
| SO476 | P476 | Sophonie 1:2-6 · « je supprimerai tout de dessus la surface du sol » : ceux qui se détournent, les prêtres étrangers et ceux qui n'ont pas cherché Jéhovah | PUBLIÉE |
| SO477 | P477 | Sophonie 1:7-13 · « le jour de Jéhovah est proche » : les princes, les fils du roi, ceux qui disent « Jéhovah ne fera ni bien ni mal », le seuil et le poisson de la porte | PUBLIÉE |
| SO478 | P478 | Sophonie 1:14-18 · « un jour de détresse » : le jour de la colère, la trompette et le cri de guerre, ni argent ni or ne pourront les délivrer | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Sophonie — prophète, avant 648 av. n. è. ») : SO476 **Accomplie / À venir** (Sophonie 1:2, 3 ; 2 Rois 25) · SO477 **Accomplie** (2 Rois 25:1-11 ; Sophonie 1:12, 13) · SO478 **Accomplie / À venir** (2 Rois 25:8-11 ; Sophonie 1:18) · SO479 Accomplie (invitation) · SO480 Accomplie (prise d'Ashkelon et destruction d'Ékron en 604 av. n. è., date neutre) · SO481 Accomplie · SO482 Accomplie (chute de Ninive) · SO483 Accomplie · SO484 Accomplie (1er accomplissement) / À venir.
- S1 : 3 recherches approfondies (Sophonie 1:2-6 — « je vais tout faire disparaître de la surface du sol », les restes de Baal, les prêtres des dieux étrangers, les prosternements sur les toits devant l'armée du ciel, le double serment à Jéhovah et à Malkam, ceux qui se détournent ; Sophonie 1:7-13 — « silence devant le Souverain Seigneur Jéhovah », le sacrifice préparé et les invités sanctifiés, les princes et les fils du roi, les vêtements étrangers, ceux qui sautent par-dessus le seuil, la porte des Poissons, le second quartier, Maktèsh et les peseurs d'argent, « je fouillerai Jérusalem avec des lampes » et les hommes figés sur leur lie ; Sophonie 1:14-18 — la litanie du jour de Jéhovah, la trompette et le signal d'alarme contre les villes fortifiées, les hommes marchant comme des aveugles, « ni leur argent ni leur or ne pourront les sauver ») + lecture du registre (section « Sophonie — prophète, avant 648 av. n. è. », P476-P484) ; documents wol : **1101990097** (« Livre de la Bible numéro 36 — Tsephania », vérifié 200), **1981608** (« Cachés au jour de la colère de Jéhovah », w81 1/11 — découvert par recherche et vérifié 200), nwtsty 36/1 et nwt 36/1 (200).
- Faits retenus : le nom du prophète signifie « Jéhovah a caché » et il était « le descendant du fidèle roi Ézéchias à la troisième génération », « un prophète de sang royal » qui dut « faire preuve de courage pour proclamer les jugements ardents de Jéhovah contre les princes de Juda » (1981608) ; « Sophonie prophétisa pendant la première partie du règne de Josias, roi de Juda, règne qui commença en 659 avant notre ère, soit une cinquantaine d'années avant que Jéhovah dévaste Juda et Jérusalem » ; « la conduite juste de Josias n'effaça pas la méchanceté… ni ne fit propitiation pour les péchés de son grand-père, Manassé, qui avait “rempli Jérusalem de sang innocent” (II Rois 24:3, 4) » ; « Aux jours de Sophonie, Jéhovah procéda à un examen complet de ceux qui disaient l'adorer » ; la question des valeurs matérielles (« compte en banque, stock d'or, grande propriété, abri souterrain ») appelle la réponse « À rien », suivie de Soph. 1:18 cité mot pour mot ; Bible Annotée : Genèse 6:7 comme arrière-plan de 1:2, 3 ; « les membres des familles riches, qui introduisaient dans le pays des mœurs en même temps que des cultes étrangers » (vêtements) ; « pénétrer violemment dans les maisons pour s'emparer du bien d'autrui » (seuil) ; « afin de découvrir les coupables dans leurs repaires les plus secrets » (lanternes) et le rapprochement avec le récit de Josèphe ; « ils assimilent l'Éternel aux idoles qui ne font ni bien ni mal (Ésaïe 41:23) » ; Joël 2:1, 2 comme source littéraire de 1:15, 16, Deutéronome 28:30 pour 1:13.
- S2 : recensement régénéré (modules clos = **669 paires**) → **12 paires réservées dans les libres** : 44/14, 19/125, 19/101, 62/4, 1101990097 (SO476) ; 52/5, 44/24, 50/3, 51/2, 1981608 (SO477) ; 40/6, 58/12, 19/112, 58/13 (SO478) ; contrôle : 12 chapitres uniques, 0 doublon interne, 0 collision avec les 669.
- S3 : data/p8_so1.py — chunk `_so1a.py` (CAT SO1 + SO476) concaténé avec `_so1b.py` (SO477 + SO478), chunks supprimés ; 0 coquille, 0 collage, 0 cyrillique.
- QC : 3 fiches = **40 264 caractères de texte** (SO476 12 751 ; SO477 14 239 ; SO478 13 274) ; blocs de prose tous > 700 car. (SO476 syst 941 ; SO477 1 164 ; SO478 966) ; src 5 par fiche (15, toutes officielles), tl 7/7/8, accomplissement 7 par fiche, texte 2 blocs par fiche ; statuts conformes au registre : SO476 « Accomplie / À venir », SO477 « Accomplie », SO478 « Accomplie / À venir ».
- S4 : build de contrôle `_TMP_SO1.html` 99 Ko — validation OK (11 blocs, 3 fiches, 15 sources) ; supprimé après contrôle.
- S5/S6 : 4 JPG (toits, lampes, trompette + vignette `prophe_SO1_vignette.jpg`) — 4/4 au premier essai, aucun refus ; 3/3 MP3 voice-05 = 14,3 · 15,7 · 12,3 s = **42,3 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_SOPHONIE_1.html` 100 Ko (**103 344 o**) — 33 mentions wol, 3 balises audio, 7 images, 11 blocs par fiche, 6 fichiers médias liés tous présents (3 JPG + 3 MP3), 0 lien non officiel ; purge P8-82 motifs exacts (2 JPG HA474-HA475 + `prophe_HA2_vignette.jpg` + 2 MP3 homonymes) → fenêtre **16 JPG / 15 MP3** ; `collections/durations.py` régénéré → **15 pistes / 505,0 s**.
- S8 : §3ce 3/3 PUBLIÉE → **478/1000** ; compteurs : **520 JPG créés** (16 présents dont vignette SO1), **489 MP3** (15 pistes) ; **Sophonie 1 est couvert (P476-P478)** ; §3cf P8-84 ouvert — **Sophonie, seconde partie** (SO479-SO482, P479-P482 : « cherchez la justice, cherchez l'humilité », Gaza, Ashkelon, Ashdod et Ékron, l'outrage de Moab et les injures d'Ammon, Ninive devenue une solitude). Après Sophonie 2 viendront SO483-SO484 (Sophonie 3).

## 3cf. Vague P8-84 (SO2 — Sophonie 2 : cherchez la justice, les villes de la côte, Moab et Ammon, Ninive dévastée)
| Fiche | P | Sujet | État |
|---|---|---|---|
| SO479 | P479 | Sophonie 2:1-3 · « cherchez Jéhovah, cherchez la justice, cherchez l'humilité » : peut-être serez-vous cachés au jour de la colère de Jéhovah (nom du prophète : « Jéhovah a caché ») | PUBLIÉE |
| SO480 | P480 | Sophonie 2:4-7 · Gaza abandonnée, Ashkelon dévastée, Ashdod chassée, Ékron déracinée : le sort des Philistins et le reste de la maison de Juda | PUBLIÉE |
| SO481 | P481 | Sophonie 2:8-11 · « j'ai entendu l'outrage de Moab et les injures d'Ammon » : le reste de mon peuple les pillera et se prosternera devant Jéhovah | PUBLIÉE |
| SO482 | P482 | Sophonie 2:12-15 · Ninive deviendra une solitude, une terre aride comme le désert ; les troupeaux s'y coucheront, tous les passants siffleront devant ses ruines | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Sophonie — prophète, avant 648 av. n. è. ») : SO479 **Accomplie (invitation)** (Sophonie 2:3) · SO480 **Accomplie** (prise d'Ashkelon et destruction d'Ékron en 604 av. n. è. (date neutre)) · SO481 **Accomplie** (Sophonie 2:9, 10) · SO482 **Accomplie** (chute de Ninive ; ruines pâturées). Suite (§3cg, P8-85) : SO483-SO484 (Sophonie 3 — la ville rebelle et les princes lions rugissants, puis « je donnerai aux peuples des lèvres pures » et le rassemblement) ; après Sophonie, la section suivante du registre est **Aggée (P485-P489)**.
- S1 : 4 recherches approfondies (Sophonie 2:1-3 — l'appel au rassemblement, le décret, le jour qui passe comme la bale, les trois recherches et le « probablement » ; 2:4-7 — Gaza, Ascalon, Asdod, Ékrôn, la nation des Keréthiens, les pâturages, les puits des bergers et le reste de la maison de Juda ; 2:8-11 — les injures de Moab et les insultes d'Ammon, Sodome et Gomorrhe, la mine de sel, « moi, et rien que moi » écarté, l'hommage des îles des nations ; 2:12-15 — les Koushites, Ninive dévastée, le pélican et le porc-épic, les lambris de cèdre, « la ville joyeuse ») + lecture du registre (section « Sophonie — prophète, avant 648 av. n. è. », P479-P484) ; documents wol vérifiés 200 : **1993921** (« Cherchez Jéhovah, vous tous, humbles de la terre », w93 15/12 — nouveau document découvert par recherche), **1981608** (« Cachés au jour de la colère de Jéhovah » — porte sur Sophonie 2:3), **1101990097** (numéro 36), **nwtsty/36/2**, ainsi que **1960165** et **1101990095** (Ninive, pour SO482).
- S2 : recensement régénéré (modules clos = **681 paires**) → **16 paires réservées dans les libres** : 58/2, 44/16, 19/121, 19/123 (SO479) ; 26/43, 60/3, 19/129, 45/16 (SO480) ; 19/104, 19/113, 46/4, 48/5 (SO481) ; 19/134, 19/136, 26/46, 58/3 (SO482) ; secours libres testés : 19/122, 44/18, 44/25, 19/124. Collision détectée en cours de route : **40/6** (déjà consommée par `p8_so1.py`) → remplacée par **19/123** ; contrôle final : 16 paires uniques, 0 doublon interne, 0 collision avec les 681.
- S3 : `data/p8_so2.py` — chunk `_so2a.py` (CAT SO2 + SO479 + SO480) concaténé avec `_so2b.py` (SO481 + SO482), chunks supprimés ; `py_compile` OK ; **80 139 o**.
- S4 : QC — 4 fiches, corps de prose (9 blocs) = **48 531 caractères** ; tous les blocs de prose > 700 car. (le schéma de SO480 a été étendu à 921 car. pour repasser le seuil) ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; schéma, chronologie et accomplissement renseignés par fiche ; 0 collage, 0 CJK ; build de contrôle `_TMP_SO2.html` 121 Ko (validation OK : 11 blocs, 4 fiches, 22 sources, liens conformes) puis supprimé.
- S5/S6 : **5 JPG** (rassemblement des humbles à la porte de la ville, plaine philistine aux ruines pâturées, plateau de Moab au sel et aux orties, ruines de Ninive au bord du Tigre, plus la vignette `prophe_SO2_vignette.jpg`) — 5/5 au premier essai ; **4/4 MP3** voice-05 = 11,0 · 11,5 · 10,3 · 10,2 s = **43,0 s**, tous acceptés au premier essai (aucun refus).
- S7 : build final `preuves/FICHES8_SOPHONIE_2.html` **125 662 o** — 47 mentions wol, 4 balises audio, 9 images, 4 fichiers médias de fiche référencés et tous présents (4 JPG + 4 MP3), 0 lien non officiel. Fenêtre médias : décision de **conserver SO1 + SO2** (aucune purge des médias de SO1, pour ne pas rompre les liens du livrable présenté au tour précédent) → **21 JPG / 19 MP3** présents ; `collections/durations.py` régénéré → **19 pistes / 548,0 s** (9,1 min) ; règle retenue pour la suite : fenêtre = archive Daniel + les deux dernières vagues, la purge des médias de SO1 interviendra à la livraison de SO3.
- S8 : §3cf 4/4 PUBLIÉE → **482/1000** ; compteurs : **525 JPG créés** (21 présents, dont 2 vignettes), **493 MP3** (19 pistes, 548,0 s) ; **Sophonie 2 est couvert (P479-P482)** ; §3cg ouvert — **Sophonie 3** (SO483-SO484 : la ville rebelle et les princes lions rugissants ; « je donnerai aux peuples des lèvres pures » et le rassemblement du reste humble et modeste). Après Sophonie viendra **Aggée (P485-P489)**.
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — **les livres de Nahoum, Jonas, Michée et Habacuc sont entièrement consommés** ; pour Sophonie 2, tester les miroirs (Sophonie 3, Ézéchiel 25/26/28, Isaïe 15/16/17/21/23, Jérémie 47/48/49, Amos 1-2, Nahoum 1-3, Psaume 83, Ésaïe 47) et puiser dans le stock libre restant (Psaumes 19/101-150 libres hors les paires déjà réservées, Actes 14/16/18/24/25/27, 1 Corinthiens 4-12, 2 Corinthiens 4-6/11-12, Éphésiens 4, Philippiens 3-4, Colossiens 2-3, 1 Thessaloniciens 5, 2 Timothée 4, Tite 3, Philémon 1, Hébreux 2-5/12-13, Jacques 2-5, 1 Pierre 2-3/5, 2 Pierre 2, 1 Jean 4-5, 2 Jean 1, 3 Jean 1, Jude 1, Romains 12-16, Ézéchiel 32-48, Isaïe 40-66) en vérifiant chaque paire par le glob. Documents wol disponibles : **1101990097** (numéro 36), **1981608** (« Cachés au jour de la colère de Jéhovah », qui porte précisément sur Sophonie 2:3), **1101990095** et **1960165** (Ninive, réutilisables pour SO482), **1200000447** (Philistie/Assyrie à vérifier), plus les portails « Sophonie » et « Philistie » à contrôler par curl avant rédaction.

## 3cg. Vague P8-85 (SO3 — Sophonie 3 : la ville rebelle et les princes lions rugissants, puis les lèvres pures et le rassemblement)
| Fiche | P | Sujet | État |
|---|---|---|---|
| SO483 | P483 | Sophonie 3:1-7 · la ville rebelle et souillée, les princes lions rugissants, les juges loups du soir, les prophètes présomptueux, « elle n'a pas écouté la voix » ; « Jéhovah s'est levé de bonne heure » | PUBLIÉE |
| SO484 | P484 | Sophonie 3:8-20 · « je donnerai aux peuples des lèvres pures », le reste humble et modeste, le rassemblement des dispersés, « je ferai de vous un nom et une louange » | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Sophonie — prophète, avant 648 av. n. è. ») : SO483 **Accomplie** · SO484 **Accomplie (1er accomplissement) / À venir**. Après Sophonie 3, la section suivante du registre est **Aggée (P485-P489)**.
- S1 : 4 recherches approfondies (Sophonie 3:1-7 — la ville rebelle, souillée et oppressive, les quatre refus, les princes lions rugissants, les juges loups du soir, les prophètes insolents et les prêtres profanateurs, la justice de Jéhovah « matin après matin », les nations détruites comme avertissement ; 3:8-20 — « attendez-moi », le jour du butin, les lèvres pures et le service « d'une seule épaule », l'offrande d'au-delà des fleuves de Koush, le reste humble et modeste, les boiteux et les chassés rassemblés, « un nom et une louange ») + lecture du registre (section « Sophonie — prophète, avant 648 av. n. è. », P483-P484) ; documents wol vérifiés 200 : **1101990097** (numéro 36 — §10 sur la réforme de Yoshiya et §« Jéhovah s'en prend à Jérusalem, la rebelle »), **1981608**, **1993921**, **nwtsty/36/3**, **nwt/36/3**, **1101990095** (Nahoum), et **1988364** (« Servons Jéhovah d'un commun accord », w88 15/5 — nouveau document découvert par recherche et vérifié 200), **1200000447** re-testé 200.
- S2 : recensement régénéré (modules clos = **697 paires**) → **12 paires réservées dans les libres** : 46/5, 51/3, 59/3, 63/1, 19/146, 53/3 (SO483) ; 19/99, 19/100, 19/149, 19/150, 44/18, 54/2 (SO484) ; contrôle : 12 chapitres uniques, 0 doublon interne, 0 collision avec les 697 (toutes vérifiées 200 par curl).
- S3 : `data/p8_so3.py` — chunk `_so3a.py` (CAT SO3 + SO483) concaténé avec `_so3b.py` (SO484), chunks supprimés ; `py_compile` OK ; **52 546 o** ; correction de coquilles de casse dans le bloc consonantique (OFFrande → OFFRANDE ×3, TAIra → TAIT, SAFah → SAFAH, LEShon → LESHON).
- S4 : QC — 2 fiches, corps de prose (9 blocs) = **30 451 caractères** (SO483 14 277 ; SO484 16 174) ; tous les blocs de prose > 700 car. (SO484 schema 1 115 ; SO483 schema 874) ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; build de contrôle `_TMP_SO3.html` 82 Ko (validation OK : 11 blocs, 2 fiches, 16 sources) puis supprimé.
- S5/S6 : **3 JPG** (place du jugement à Jérusalem avec les dignitaires hautains ; foule immense et diverse au lever du soleil avec un boiteux soutenu ; plus la vignette `prophe_SO3_vignette.jpg`) — 3/3 au premier essai ; **2/2 MP3** voice-05 = 12,3 · 11,2 s = **23,5 s**, acceptés au premier essai.
- S7 : build final `preuves/FICHES8_SOPHONIE_3.html` **85 453 o** — 35 mentions wol, 2 balises audio, 5 images, 4 fichiers médias de fiche référencés et tous présents (2 JPG + 2 MP3), 0 lien non officiel. **Purge SO1 appliquée** (motifs exacts : prophe_SO476_toits.jpg, prophe_SO477_lampes.jpg, prophe_SO478_trompette.jpg, prophe_SO1_vignette.jpg + 3 MP3 homonymes) → fenêtre = archive Daniel + SO2 + SO3 = **20 JPG / 18 MP3** ; `collections/durations.py` régénéré → **18 pistes / 529,2 s** (8,8 min). Note de continuité : la purge était différée à la livraison de SO3 pour préserver les liens du livrable SO1 présenté au tour précédent ; les URL restent identiques, seul le fichier média a été retiré du dossier.
- S8 : §3cg 2/2 PUBLIÉE → **484/1000** ; compteurs : **528 JPG créés** (20 présents, dont 3 vignettes), **495 MP3** (18 pistes, 529,2 s) ; **Sophonie est intégralement couvert (P476-P484)** ; §3ch ouvert — **Aggée (P485-P489)**. Après Aggée viendra **Zakharia (P490-P498)** selon le registre.
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — les livres de Nahoum, Jonas, Michée, Habacuc et **les chapitres 1 et 2 de Sophonie** sont consommés ; tester les miroirs (Sophonie 1-2, Ésaïe 12/25/26/29/30/35/40-66, Jérémie 30/31/33, Ézéchiel 34/36/37, Joël 2/3, Michée 4/5/7, Psaumes 22/34/37/68/72/96-100/102/103/113/134/145-150) et le stock libre restant (Actes 16/18/25/27, 1 Corinthiens 4-12, 2 Corinthiens 4-6/11-12, Éphésiens 4, Philippiens 3-4, Colossiens 2-3, 1-2 Thessaloniciens, 2 Timothée 4, Tite 3, Philémon 1, Hébreux 2-5/12-13, Jacques 2-5, 1 Pierre 2-3/5, 2 Pierre 2, 1 Jean 4-5, 2 Jean 1, 3 Jean 1, Jude 1, Romains 12-16, Ézéchiel 32-48) en vérifiant chaque paire par le glob. Documents wol disponibles : **1101990097** (numéro 36), **1981608**, **1993921** (Sophonie 2:3 — à réutiliser pour la conclusion du livre), plus les portails « Sophonie » et « Jérusalem » à contrôler par curl avant rédaction.

## 3ch. Vague P8-86 (AG — Aggée : cinq messages datés au jour près, de la maison en ruine au cachet de Zorobabel)
| Fiche | P | Sujet | État |
|---|---|---|---|
| AG485 | P485 | Aggée 1:2-11 · « le temps n'est pas venu » : les maisons lambrissées, la maison en ruine, les cinq constats du travail qui rapporte peu et la sécheresse appelée sur le pays | PUBLIÉE |
| AG486 | P486 | Aggée 1:12-15 · « je suis avec vous » : Zorobabel, Yehoshoua et tout le reste du peuple écoutent, craignent, et se mettent à l'ouvrage le 24e jour du 6e mois | PUBLIÉE |
| AG487 | P487 | Aggée 2:1-9 · « sois fort… et travaillez » : la question aux anciens, l'ébranlement des nations et « la gloire de cette dernière maison sera plus grande que la première ; je donnerai la paix » | PUBLIÉE |
| AG488 | P488 | Aggée 2:10-19 · la question posée aux prêtres, la sainteté qui ne se transmet pas et la souillure qui se propage : « dès ce jour je vous bénirai » | PUBLIÉE |
| AG489 | P489 | Aggée 2:20-23 · « je te prendrai, Zorobabel, mon serviteur, et je te ferai comme un cachet » : l'ébranlement des royaumes et la lignée messianique | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Aggée — prophète, 520 av. n. è. ») : AG485 **Accomplie** (Aggée 1:10, 11 ; Esdras 5:1, 2) · AG486 **Accomplie** (Aggée 1:14, 15 ; Esdras 3:8 ; 5:2) · AG487 **Accomplie (1er accomplissement)** (Aggée 2:9 ; Esdras 6:14-16) · AG488 **Accomplie** (Aggée 2:19 ; Esdras 6:14, 15) · AG489 **Accomplie (1er accomplissement)** (Aggée 2:23 ; lignée messianique — Matthieu 1:12, 13 ; Luc 3:27).
- S1 : 4 recherches approfondies (Aggée 1:1-11 — la datation impériale, les maisons lambrissées, les cinq constats économiques, la sécheresse appelée et le jeu d'assonance ruine/sécheresse ; 1:12-15 — l'écoute, la crainte, le titre de « messager de Jéhovah », le réveil de l'esprit et les 23 jours ; 2:1-9 — les anciens et la première gloire, le triple « sois fort », l'ébranlement, les « choses désirables » et la paix ; 2:10-19 — la question aux prêtres, la dissymétrie sainteté/impureté, « depuis ce jour je bénirai » ; 2:20-23 — le sceau, le renversement de Jérémie 22:24 et la lignée messianique) + lecture du registre (P485-P489) ; documents wol vérifiés 200 : **1101990098** (« Livre de la Bible numéro 37 — Haggaï », si p. 166-168), **1975561** (« Le soutien de Dieu bannit la crainte »), **2001124**, **1996162**, **nwtsty 37/1-2**, **nwt 37/1-2**.
- Faits retenus : Haggaï, « dixième des petits prophètes » et « premier des trois prophètes qui sont entrés en activité après le retour des Juifs dans leur pays en 537 av. n. è. », son nom signifiant « [Né un jour de] Fête » ; quatre messages « échelonnés sur une période de 112 jours », « dans les 38 versets de son livre, Haggaï cite 35 fois le nom de Jéhovah, et il utilise 14 fois l'expression “Jéhovah des armées” » ; « les fondations du temple étaient à peine posées (en 536 av. n. è.) », l'interdiction obtenue par les opposants « en 522 », la reprise en 520 ; « Ils se mettent à l'ouvrage 23 jours seulement après le début de l'activité prophétique de Haggaï, et en dépit de l'interdiction prononcée par le gouvernement perse » ; « en quatre ans et demi le temple était achevé » (Esdras 6:14, 15) ; la citation d'Aggée 2:6 par Paul en Hébreux 12:26 ; la leçon du sceau chez 1975561 (« Zorobabel devint très précieux aux yeux de Jéhovah, aussi précieux qu'un anneau à cachet dans la main droite de Jéhovah des armées ») ; Bible Annotée : assonance ḥarev/ḥorev, « l'état de ruine du sanctuaire attire la ruine sur vous et vos biens », « ce n'est pas ici une vengeance de la part de l'Éternel, mais en châtiant il a pour but de ramener Israël à la conscience de ce qui lui manque ».
- S2 : recensement régénéré (modules clos = **709 paires**) → **22 paires réservées dans les libres** : 16/6, 13/29, 19/24, 46/6 (AG485) ; 19/122, 46/7, 47/4, 50/4 (AG486) ; 46/8, 47/5, 52/3, 56/3 (AG487) ; 46/9, 47/6, 46/11, 44/25 (AG488) ; 46/12, 47/11, 47/12, 44/27, 49/4, 52/1 (AG489) ; le stock libre restant est désormais quasi épuisé (il faut élargir les miroirs pour P8-87) ; contrôle : 22 chapitres uniques, 0 doublon interne, 0 collision avec les 709.
- S3 : `data/p8_ag1.py` — trois chunks (`_ag1a.py` : CAT AG1 + AG485 ; `_ag1b.py` : AG486 + AG487 ; `_ag1c.py` : AG488 + AG489), concaténés puis supprimés ; `py_compile` OK ; **112 762 o** ; corrections de casse et de coquilles dans les blocs consonantiques (IMPURETÉ, ANNEAUX À CACHET, YEHUD) et d'un faux ami (« époque ferroviaire » → « époque perse »).
- S4 : QC — 5 fiches, corps de prose (9 blocs) = **70 217 caractères** (AG485 14 842 ; AG486 13 323 ; AG487 14 436 ; AG488 13 674 ; AG489 13 942) — **la vague la plus volumineuse de la phase 8** ; tous les blocs de prose > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; build de contrôle `_TMP_AG1.html` 162 Ko (validation OK : 11 blocs, 5 fiches, 28 sources) puis supprimé.
- S5/S6 : **6 JPG** (intérieur lambrissé face au sanctuaire en ruine ; rassemblement des rapatriés à l'aube avec outils ; vieillards contemplant le chantier, plus les 5 illustrations de fiche, + la vignette `prophe_AG1_vignette.jpg`) — 6/6 au premier essai ; **5/5 MP3** voice-05 = 9,3 · 10,3 · 10,9 · 10,2 · 9,3 s = **50,0 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_AGGEE_1.html` **168 474 o** — 59 mentions wol, 5 balises audio, 11 images, 10 fichiers médias de fiche référencés et tous présents (5 JPG + 5 MP3), 0 lien non officiel ; **purge SO2 appliquée** (motifs exacts : prophe_SO479_caches.jpg, prophe_SO480_philistins.jpg, prophe_SO481_moab.jpg, prophe_SO482_ninive.jpg, prophe_SO2_vignette.jpg + 4 MP3 homonymes) → fenêtre = archive Daniel + SO3 + AG1 = **21 JPG / 19 MP3** ; `collections/durations.py` régénéré → **19 pistes / 536,2 s** (8,9 min).
- S8 : §3ch 5/5 PUBLIÉE → **489/1000** ; compteurs : **534 JPG créés** (21 présents, dont 4 vignettes), **500 MP3** (19 pistes, 536,2 s) ; **Aggée est intégralement couvert (P485-P489)** ; §3ci ouvert — **Zacharie (P490-P511, 22 entrées)**, à découper en quatre vagues : Zc 1-3 (P490-P494), Zc 4-6 (P495-P498), Zc 7-11 (P499-P505), Zc 12-14 (P506-P511).
## 3ci. Vague P8-87 (ZA1 — Zacharie 1-3 : les chevaux, les cornes, le cordeau et le Germe)
| Fiche | P | Sujet | État |
|---|---|---|---|
| ZA490 | P490 | Zacharie 1:2-6 · « revenez à moi » : vos pères, où sont-ils ? les prophètes vivent-ils pour toujours ? | PUBLIÉE |
| ZA491 | P491 | Zacharie 1:7-17 · l'homme sur le cheval roux parmi les myrtes ; « je suis revenu à Jérusalem avec miséricorde » ; le cordeau sera tendu | PUBLIÉE |
| ZA492 | P492 | Zacharie 1:18-21 · les quatre cornes qui ont dispersé Juda et les quatre artisans venus les abattre | PUBLIÉE |
| ZA493 | P493 | Zacharie 2:1-13 · l'homme avec le cordeau à mesurer ; Jérusalem habitée comme une ville sans muraille | PUBLIÉE |
| ZA494 | P494 | Zacharie 3:1-10 · la saleté ôtée de Yehoshoua le grand prêtre ; « voici le Germe, mon serviteur » | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Zacharie — prophète, 518 av. n. è. ») : ZA490 **Accomplie** (1:6) · ZA491 **Accomplie** (1:16 ; Esdras 3:8-13 ; 6:14) · ZA492 **Accomplie** (1:20, 21) · ZA493 **Accomplie** (2:4-13 ; Néhémie 3-12) · ZA494 **Accomplie** (3:8, 9 ; Esdras 5:1, 2 ; ligne messianique). Suite (§3cj) : Zc 4-6 (P495-P498) ; puis Zc 7-11 et Zc 12-14.
- S1 : 3 recherches approfondies (Zc 1:2-6 — le retour au pays et l'appel « revenez à moi », les pères et les prophètes ; 1:7-21 — l'homme sur le cheval roux parmi les myrtes, les patrouilles, « je suis revenu à Jérusalem avec miséricorde », les quatre cornes et les quatre artisans ; 2:1-13 puis 3:1-10 — le cordeau à mesurer, la ville sans muraille, la muraille de feu, « que toute chair fasse silence », le procès de Yehoshoua et le Germe) ; lecture du registre (l. 157-172 : P490-P500) ; `fetch_page` de **1101990099** (« Livre de la Bible numéro 38 — Zekaria », si p. 168-172) — cadre historique, la 2e année de Darius (520-518), le nom du prophète, la valeur probante du livre (Tyr, le Messie) ; documents wol vérifiés 200 : **1101990099**, **1975561**, **2007882**, **2017607**, **1200004682**, **1200000447**, **nwtsty 38/1-5**, **nwt 38/1-3**.
- S2 : recensement régénéré (modules clos = **731 paires**) ; scan élargi à 66 livres → 478 chapitres libres ; pools testés un par un contre le corpus : ZA490 (14/6, 13/17, 18/5) · ZA491 (15/8, 15/10, 18/5, 40/3, 41/1) · ZA492 (40/4, 41/2, 43/2, 44/1, 42/3) · ZA493 (41/3, 16/5, 14/3, 18/23, 45/7) ; tests complémentaires de libération (21/12, 19/14, 20/28, 58/4, 40/9, 42/15 libres) ; constat d'épuisement du bassin : privilégier désormais les livres voisins (Aggée, Esdras, Néhémie, Daniel 7-12, Ézéchiel 40-48).
- S3 : `data/p8_za1.py` — trois chunks (`_za1a.py` : CAT ZA1 + ZA490 + ZA491 ; `_za1b.py` : ZA492 + ZA493 ; `_za1c.py` : ZA494), concaténés puis supprimés ; `py_compile` OK ; **106 706 o** ; corrections de casse et de coquilles dans les blocs consonantiques (TAHAT, TERRIFIER, TENDRE) et nettoyage d'une URL source écrite sous forme d'expression (`"…" .replace(…)`) ramenée à un lien littéral — c'est ce nettoyage qui a fait tomber le contrôle « 0 lien non officiel » à zéro.
- S4 : QC — 5 fiches ; corps de prose (9 blocs) = **64 161 caractères** (ZA490 12 851 ; ZA491 13 154 ; ZA492 12 217 ; ZA493 12 375 ; ZA494 13 564) ; tous les blocs de prose > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; **25 paires nwt réservées, 0 doublon interne, 0 collision avec les 731** ; 0 CJK ; 0 lien non officiel ; build de contrôle `_TMP_ZA1.html` 157 Ko (11 blocs, 5 fiches, 33 sources) puis supprimé. **Correction appliquée** : la paire 18/5, initialement présente dans ZA490 et ZA491, a été remplacée dans ZA490 par 19/14, puis la fiche a reçu 18/5 (Job 5 — le sort des méchants et le châtiment qui ramène, cité en Zc 1:6), 18/26 et 18/33 pour homogénéiser le lot.
- S5/S6 : **6 JPG** (appel au retour sur la place de Jérusalem ; l'homme au cheval roux parmi les myrtes ; les quatre cornes et les quatre artisans devant la forge ; l'homme au cordeau surplombant la ville ouverte ; Yehoshoua, les habits souillés et le messager lumineux ; + la vignette `prophe_ZA1_vignette.jpg`) — 6/6 au premier essai ; **5/5 MP3** voice-05 = 11,1 · 14,2 · 11,1 · 13,4 · 13,5 s = **63,3 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_ZACHARIE_1.html` **162 792 o** — 69 mentions wol, 5 balises audio, 11 images, 10 fichiers médias de fiche référencés et tous présents (5 JPG + 5 MP3), 0 lien non officiel ; **purge SO3 appliquée** (motifs exacts : prophe_SO483_rebelle.jpg, prophe_SO484_levres.jpg, prophe_SO3_vignette.jpg + 2 MP3 homonymes) → fenêtre = archive Daniel + AG1 + ZA1 = **24 JPG / 22 MP3** ; `collections/durations.py` régénéré → **22 pistes / 576,0 s** (9,6 min) ; aucun `.bak`.
- S8 : §3ci 5/5 PUBLIÉE → **494/1000** ; compteurs : **540 JPG créés** (24 présents, dont 5 vignettes), **505 MP3** (22 pistes, 576,0 s) ; **Zacharie 1-3 est couvert (P490-P494)** ; §3cj ouvert — **Zc 4-6 (P495-P498)**, puis Zc 7-11 (P499-P505) et Zc 12-14 (P506-P511), avant **Malachie (8 entrées)**.
Chapitres nwt : **le stock libre est presque épuisé** (les 23 derniers candidats ont été consommés par AG1) — pour Zacharie, tester les miroirs (Aggée 1-2 — livre voisin, Esdras 1-10 et Néhémie 1-13 entiers, Daniel 7-12, Ézéchiel 1-3/8-11/37/40-48, Isaïe 1-14/21-23/40-66, Jérémie 23-33/46-51, Psaumes 2/45/72/89/110/118/132/145-150, Matthieu 1-2/21-25, Luc 1-3/21-24, Hébreux 6-10, Révélation 1-22) en vérifiant chaque paire par le glob **avant** réservation ; les livres de Sophonie et d'Aggée sont entièrement consommés. Documents wol à tester par curl : « Livre de la Bible numéro 38 — Zekaria », portails « Zacharie » et « Zorobabel », articles sur Josué/Yehoshoua le grand prêtre et sur le Germe (voir aussi 1975561, déjà vérifié 200).

## 3cj. Vague P8-88 (ZA2 — Zacharie 4-6 : le chandelier et les deux oints, le rouleau volant, les quatre chars, l'homme dont le nom est Germe)
| Fiche | P | Sujet | État |
|---|---|---|---|
| ZA495 | P495 | Zacharie 4:1-14 · « ni par puissance ni par force, mais par mon esprit » : le chandelier d'or à sept lampes, les deux oliviers et les deux oints ; les mains de Zorobabel achèveront | PUBLIÉE |
| ZA496 | P496 | Zacharie 5:1-11 · le rouleau volant : le voleur et celui qui jure faussement seront retranchés ; l'épha au couvercle de plomb emportée à Shinéar | PUBLIÉE |
| ZA497 | P497 | Zacharie 6:1-8 · les quatre chars et les chevaux qui sortent d'entre deux montagnes de bronze pour parcourir toute la terre | PUBLIÉE |
| ZA498 | P498 | Zacharie 6:9-15 · « voici l'homme dont le nom est Germe » : la couronne d'argent et d'or, le temple bâti, le roi-prêtre | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Zacharie — prophète, 518 av. n. è. ») : ZA495 **Accomplie** (Zacharie 4:6-9, 14 ; Esdras 6:14, 15) · ZA496 **Accomplie** (Zacharie 5:4, 11) · ZA497 **Accomplie** (Zacharie 6:7, 8) · ZA498 **Accomplie** (Zacharie 6:12, 13 ; Jésus, Roi-Prêtre — Hébreux 6:20 ; 7:1-3, 15-17). Suite (§3ck) : Zc 7-11 (P499-P505) ; puis Zc 12-14 (P506-P511) et Malachie (8 entrées).
- S1 : 3 recherches approfondies (Zc 4 — le chandelier d'or, la coupe et les sept conduits, les deux oliviers, « ni par puissance ni par force », la grande montagne, la pierre du faîte, le jour des petits commencements, les deux oints ; Zc 5 — le rouleau de vingt coudées, les deux crimes, l'épha, la femme, le talent de plomb, les ailes de cigogne et Shinéar ; Zc 6 — les quatre chars, les deux montagnes de bronze, les quatre vents, le pays du nord, la couronne d'argent et d'or, le Germe roi-prêtre et « ceux qui sont loin ») ; lecture du registre (l. 167-178 : P495-P506) ; **document 2017607** (« Des chars et une couronne te protègent », w17 octobre p. 26-30) lu intégralement (chunks 0-1) : montagnes = royaumes (Daniel 2:35, 45), cuivre = souveraineté et Royaume, conducteurs = anges (Hébreux 1:7, 14 ; Malachie 3:6 ; Psaume 34:7 ; 2 Rois 6:15-17), mission de protection contre Babylone « le pays du nord » et promesse de non-retour en esclavage, application à Babylone la Grande et à 1919 (Révélation 18:4), le couronnement de Yoshoua expliqué aux Juifs de l'époque, Yoshoua non-roi car non descendant de David, « Germe » = Jésus Christ (Isaïe 11:1 ; Matthieu 2:23, note), Jésus bâtisseur du temple spirituel, affinage (Malachie 3:1-3), 144 000 rois et prêtres (Révélation 14:1-4 ; 20:6) ; documents wol vérifiés 200 : **2017607**, **2007882**, **1200014577** (« Zacharie (Livre de) » Auxiliaire), **1101990099** ; `nwtsty 38/6` et `nwt 38/6` → 200 ; `38/4-5` → 404 (non utilisé).
- S2 : recensement régénéré (modules clos = **756 paires**, 87 modules) ; scan sur 66 livres → **433 chapitres libres** ; sélection par fiche : ZA495 (16/10 Esdras 10 gratuit ; 41/4 Marc 4 ; 19/8) · ZA496 (38/5 Zekaria 5 ; 40/7 Matthieu 7 ; 19/9) · ZA497 (19/10, 19/11, 42/4 ; puis 19/13 après incident) · ZA498 (43/3, 43/6, 44/19 ; puis 43/12 après incident) ; contrôle : 14 paires uniques, 0 doublon interne, 0 collision.
- S3 : `data/p8_za2.py` — deux chunks (`_za2a.py` : CAT ZA2 + ZA495 + ZA496 ; `_za2b.py` : ZA497 + ZA498), concaténés puis supprimés ; ajout de l'en-tête `FICHES = []` (le contrôle d'import a révélé son absence — les chunks précédents le portaient en tête) ; `py_compile` OK ; **79 436 o**. Incidents corrigés en cours de route : la paire **38/6** se trouvait déjà dans **§3ez (p8_ez11)** et **§3jr (p8_jr12)** — retirée de ZA498 puis remplacée par **43/12** (Jean 12) ; restant en collision pour ZA497, la paire a été remplacée par **19/13** (Psaume 13) ; contrôle final : 0 collision.
- S4 : QC — 4 fiches ; corps de prose (9 blocs) = **49 559 caractères** (ZA495 12 756 ; ZA496 11 901 ; ZA497 12 461 ; ZA498 12 441) ; tous les blocs > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; **14 paires nwt, 0 doublon interne, 0 collision avec les 756** ; 0 CJK ; 0 lien non officiel ; build de contrôle `_TMP_ZA2.html` 125 255 o (11 blocs, 4 fiches, 27 sources) puis supprimé.
- S5/S6 : **5 JPG** (le chandelier d'or alimenté par les deux oliviers avec le fil à plomb ; le rouleau volant au-dessus des toits, le disque de plomb et l'épha emporté ; les quatre chars de guerre entre les deux montagnes de bronze ; le couronnement de Yehoshoua devant la souche qui repousse ; + la vignette `prophe_ZA2_vignette.jpg`) — 5/5 au premier essai ; **4/4 MP3** voice-05 = 11,5 · 12,5 · 10,6 · 12,1 s = **46,7 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_ZACHARIE_2.html` **126 719 o** — 57 mentions wol, 4 balises audio, 9 images, 8 fichiers médias de fiche référencés et tous présents (4 JPG + 4 MP3), 0 lien non officiel ; **purge ZA1 appliquée** (motifs exacts : prophe_ZA490_revenez.jpg, prophe_ZA491_myrtes.jpg, prophe_ZA492_cornes.jpg, prophe_ZA493_mesure.jpg, prophe_ZA494_germe.jpg, prophe_ZA1_vignette.jpg + 5 MP3 homonymes) → fenêtre = archive Daniel + AG1 + ZA2 = **23 JPG / 21 MP3** ; `collections/durations.py` régénéré → **21 pistes / 559,4 s** (9,3 min).
- S8 : §3cj 4/4 PUBLIÉE → **498/1000** ; compteurs : **545 JPG créés** (23 présents, dont 6 vignettes), **509 MP3** (21 pistes, 559,4 s) ; **Zacharie 1-6 est couvert (P490-P498)** ; §3ck ouvert — **Zc 7-11 (P499-P505, 7 fiches)**, puis Zc 12-14 (P506-P511), avant **Malachie (8 entrées)**.
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — le stock libre du tour est très réduit (**478 chapitres libres** au total sur 66 livres au dernier scan, à recompter) ; livres entiers consommés : Sophonie, Aggée ; tester en priorité **Esdras 1-10**, **Néhémie 1-13**, **Daniel 7-12**, **Ézéchiel 40-48**, **Isaïe 1-14/40-66**, **Jérémie 23-33**, **Psaumes 2/45/72/89/110/118/132**, **Matthieu 21-25**, **Luc 21-24**, **Hébreux 6-10**, **Révélation 1-22**, puis les épîtres non consommées (Actes 16/18/25/27, 1 Corinthiens 4-12, Éphésiens 4, Philippiens 3-4, Colossiens 2-3, 1-2 Thessaloniciens, 2 Timothée 4, Tite 3, Philémon 1, Hébreux 2-5/12-13, Jacques 2-5, 1 Pierre 2-3/5, 2 Pierre 2, 1 Jean 4-5, 2 Jean 1, 3 Jean 1, Jude 1, Romains 12-16). Documents wol disponibles : **1101990099** (chunks 1-4 non lus), **2007882** (« Points marquants d'Haggaï et de Zekaria »), **2017607** (« Des chars et une couronne te protègent » — à réutiliser pour ZA497/ZA498), **1200004682**, **nwtsty 38/4-5** ; à tester : **1200014577** (« Zacharie (Livre de) » Auxiliaire).

## 3ck. Vague P8-89 (ZA3 — Zacharie 7-10 : le jeûne devenu fête, le roi humble sur un âne, le fardeau sur les nations, la pluie demandée)
| Fiche | P | Sujet | État |
|---|---|---|---|
| ZA499 | P499 | Zacharie 7:1-14 · la délégation de Béthel et la question sur les jeûnes : « est-ce pour moi que vous avez jeûné ? » ; « je ne répondrai pas quand ils crieront » et la dispersion parmi les nations | PUBLIÉE |
| ZA500 | P500 | Zacharie 8:1-17 · « je reviendrai à Sion » : les vieillards et les enfants dans les rues, la ville de vérité, les paroles de paix et de jugement | PUBLIÉE |
| ZA501 | P501 | Zacharie 8:18-23 · les jeûnes changés en fêtes joyeuses ; « dix hommes de toutes les langues saisiront le pan du vêtement d'un Juif » | PUBLIÉE |
| ZA502 | P502 | Zacharie 9:1-8 · le fardeau sur Hadrac, Damas, Hamath, Tyr, Sidon et Gaza ; « je camperai pour ma maison » | PUBLIÉE |
| ZA503 | P503 | Zacharie 9:9 · « voici ton roi qui vient à toi, humble et monté sur un âne » | PUBLIÉE |
| ZA504 | P504 | Zacharie 9:10-17 · le char de guerre retranché, la domination d'une mer à l'autre, le sang de l'alliance et les pierres de la couronne | PUBLIÉE |
| ZA505 | P505 | Zacharie 10:1-12 · « demandez la pluie » : le rassemblement de Juda, le retour d'Égypte et d'Assyrie, la force dans Jéhovah | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Zacharie — prophète, 518 av. n. è. ») : ZA499 **Accomplie** (7:13, 14 ; dispersion) · ZA500 **Accomplie** (8:3-8, 16, 17 ; Esdras-Néhémie) · ZA501 **Accomplie (1er accomplissement)** (8:23 ; application spirituelle — Actes 2 ; Romains 2:28, 29) · ZA502 **Accomplie** (concordance avec la campagne d'Alexandre en Syrie, Phénicie et Philistie) · ZA503 **Accomplie** (Matthieu 21:4, 5 ; Jean 12:14, 15) · ZA504 **Accomplie / À venir** (9:10, 11 ; application messianique) · ZA505 **Accomplie (1er accomplissement)** (10:6-10). Suite (§3cl) : Zc 12-14 (P506-P511) ; puis Malachie (8 entrées).
- S1 : 3 recherches approfondies (Zc 7 — la délégation de Béthel, la question du jeûne du cinquième mois, « est-ce pour moi que vous avez jeûné ? », le cœur de diamant et la dispersion ; Zc 8 — « je suis revenu à Sion », les vieillards et les enfants dans les rues, la ville de vérité, les quatre jeûnes changés en fêtes, les dix hommes et le pan du vêtement ; Zc 9-10 — le fardeau sur Hadrac, Damas, Hamath, Tyr, Sidon et les cités philistines, le roi humble monté sur un âne, le char de guerre retranché, le sang de l'alliance, la demande de pluie et le double rassemblement d'Égypte et d'Assyrie) ; lecture du registre (l. 173-186 : P501-P511) ; **lecture du document 1101990099** (« Livre de la Bible numéro 38 — Zekaria »), chunk 1 : les huit visions détaillées, les chapitres 6:9–7:14, et le fait capital retenu pour la vague suivante : l'explication du nom « Jérémie » employé par Matthieu en 27:9 — Jérémie figurait parfois en tête des prophètes dits postérieurs, et Matthieu a pu suivre la coutume juive de désigner toute une section par le nom de son premier livre, comme Jésus emploie « Psaumes » en Luc 24:44 ; le document précise aussi que « le changement de sujet justifie amplement le changement de style » à partir du chapitre 9. Documents wol vérifiés 200 : **1101990099**, **2007882**, **1200014577**, **2017607**, **1200004682**.
- S2 : recensement régénéré (modules clos = **770 paires**) ; **constat : les 14 chapitres de Zekaria (38/1-38/14) sont tous pris** → sources prises dans les évangiles, les psaumes et les épîtres : ZA499 (40/9, 42/19, 58/5, 19/15) · ZA500 (20/17, 43/14, 41/9, 19/16) · ZA501 (59/5, 46/14, 19/45) · ZA502 (40/8, 42/10, 19/52) · ZA503 (40/21, 43/11, 41/10) · ZA504 (40/22, 42/13, 58/4) · ZA505 (42/14, 43/17, 19/67) ; contrôle : **23 paires uniques, 0 doublon interne, 0 collision avec les 770**.
- S3 : `data/p8_za3.py` — quatre chunks (`_za3a.py` : CAT ZA3 + ZA499 + ZA500 ; `_za3b.py` : ZA501 + ZA502 ; `_za3c.py` : ZA503 + ZA504 ; `_za3d.py` : ZA505), concaténés puis supprimés ; `py_compile` OK ; **131 961 o** ; correction d'une coquille (« provinies » → « provinces »).
- S4 : QC — 7 fiches ; corps de prose (9 blocs) = **79 005 caractères** (ZA499 11 976 ; ZA500 11 553 ; ZA501 11 216 ; ZA502 11 018 ; ZA503 10 653 ; ZA504 10 893 ; ZA505 11 696) ; tous les blocs > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; **23 paires nwt, 0 doublon interne, 0 collision avec les 770** ; 0 CJK ; 0 lien non officiel ; build de contrôle `_TMP_ZA3.html` 203 088 o (11 blocs, 7 fiches, 40 sources) puis supprimé.
- S5/S6 : **8 JPG** (la délégation de Béthel devant les prêtres et le prophète ; la rue de Jérusalem avec les vieillards assis et les enfants qui jouent ; la place en fête et les dix hommes saisissant le pan d'un vêtement ; Tyr insulaire assiégée et son môle, colonnes de fumée ; l'entrée de Jésus sur un ânon au milieu des rameaux ; les chars et chevaux transformés en outils agricoles devant les vignes et la mer ; la pluie sur les collines et le berger les bras ouverts ; + la vignette `prophe_ZA3_vignette.jpg`) — 8/8 au premier essai ; **7/7 MP3** voice-05 = 11,9 · 14,4 · 14,8 · 13,2 · 11,0 · 13,4 · 9,9 s = **88,6 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_ZACHARIE_3.html` **205 611 o** — 83 mentions wol, 7 balises audio, 15 images, 14 fichiers médias de fiche référencés et tous présents (7 JPG + 7 MP3), 0 lien non officiel ; **purge ZA2 appliquée** (motifs exacts : prophe_ZA495_chandelier.jpg, prophe_ZA496_rouleau.jpg, prophe_ZA497_chars.jpg, prophe_ZA498_couronne.jpg, prophe_ZA2_vignette.jpg + 4 MP3 homonymes) → fenêtre = archive Daniel + AG1 + ZA3 = **26 JPG / 24 MP3** ; `collections/durations.py` régénéré → **24 pistes / 601,3 s** (10,0 min).
- S8 : §3ck 7/7 PUBLIÉE → **505/1000** ; compteurs : **553 JPG créés** (26 présents, dont 7 vignettes), **516 MP3** (24 pistes, 601,3 s) ; **Zacharie 7-10 est couvert (P499-P505)** ; §3cl ouvert — **Zc 11-14 (P506-P511, 6 fiches)**, dernière vague du livre, avant **Malachie (8 entrées)**.
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — le stock libre du tour est de **433 chapitres** (à recompter) ; livres entiers consommés : Sophonie, Aggée ; **Zekaria 1-6 désormais pris (38/1 à 38/6)** ; tester en priorité **Zekaria 7-14 (38/7 à 38/14 à vérifier)**, **Malachie 1-4 (39/1-4 à réserver avant Malachie)**, **Esdras 1-10**, **Néhémie 1-13**, **Daniel 7-12**, **Ézéchiel 40-48**, **Isaïe 1-14/40-66**, **Jérémie 23-33**, **Psaumes 2/45/72/89/110/118/132**, **Matthieu 21-25**, **Luc 21-24**, **Jean 8-21**, **Hébreux 6-13**, **Révélation 1-22**, puis les épîtres non consommées (Actes 20-21, 1 Corinthiens 4-12, Éphésiens 4, Philippiens 3-4, Colossiens 2-3, 1-2 Thessaloniciens, 2 Timothée 4, Tite 3, Philémon 1, Hébreux 2-5/12-13, Jacques 2-5, 1 Pierre 2-3/5, 2 Pierre 2, 1 Jean 4-5, 2 Jean 1, 3 Jean 1, Jude 1, Romains 12-16).
Documents wol disponibles : **2017607** (lu, à réutiliser pour ZA503 — le couronnement et la protection), **2007882**, **1200014577**, **1200004682**, **1101990099** (chunks 1-4 non lus), **nwtsty 38/6** ; à tester : `1101990100` et suivants, portails « Alexandre le Grand », « Tyr », « âne », numéro 38 (fin du livre), plus les articles sur le jeûne et sur les trente pièces d'argent.

## 3cl. Vague P8-90 (ZA4 — Zacharie 11-14 : les trente pièces d'argent, le berger frappé, la source ouverte et le jour de Jéhovah)
| Fiche | P | Sujet | État |
|---|---|---|---|
| ZA506 | P506 | Zacharie 11:4-11 · les trois bergers retranchés en un mois ; « je brisai mon bâton nommé Grâce » et les brebis de mauvaise volonté | PUBLIÉE |
| ZA507 | P507 | Zacharie 11:12, 13 · les trente pièces d'argent, « le prix auquel j'ai été estimé » ; jetées dans la maison de Jéhovah pour le potier | PUBLIÉE |
| ZA508 | P508 | Zacharie 12:1-9 · Jérusalem, coupe d'étourdissement pour les peuples ; les chefs comme des torches dans les gerbes ; la pierre pesante | PUBLIÉE |
| ZA509 | P509 | Zacharie 12:10-14 · « ils verront celui qu'ils ont transpercé et ils pleureront comme sur un fils unique » | PUBLIÉE |
| ZA510 | P510 | Zacharie 13:1-9 · une source ouverte pour laver le péché ; « frappe le berger, et les brebis seront dispersées » ; le tiers passé par le feu | PUBLIÉE |
| ZA511 | P511 | Zacharie 14:1-21 · voici, un jour vient pour Jéhovah ; les pieds sur le mont des Oliviers ; Jéhovah deviendra roi sur toute la terre | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md) : ZA506 **Accomplie** (11:10, 11) · ZA507 **Accomplie** (Matthieu 26:15 ; 27:3-10 ; Matthieu 27:9 attribue le texte à Jérémie — point reconnu comme discuté) · ZA508 **Accomplie / À venir** (12:3-9) · ZA509 **Accomplie (1er accomplissement) / À venir** (Jean 19:34, 37 ; Révélation 1:7) · ZA510 **Accomplie** (Matthieu 26:31 ; Marc 14:27) · ZA511 **À venir** (14:9 ; Révélation 19:11-21 ; 21:3).
- S1 : 3 recherches approfondies (Zc 11 — le berger du troupeau vendu à la tuerie, les trois bergers en un mois, les deux bâtons « Charme » et « Union », les trente pièces d'argent jetées au trésor et le potier ; Zc 12 — Jérusalem coupe qui donne le vertige et pierre pesante, les chefs comme des torches dans les gerbes, le deuil sur « celui qu'ils ont transpercé », la maison de David et la maison de Nathan ; Zc 13-14 — la source ouverte pour le péché, le berger compagnon frappé et les brebis dispersées, le tiers affiné, le jour de Jéhovah, le mont des Oliviers fendu, les eaux vives vers l'est et l'ouest, « vraiment Jéhovah deviendra roi sur toute la terre ») ; lecture du registre (l. 173-186 : P499-P511) ; **lecture du document 1101990099** (« Livre de la Bible numéro 38 — Zekaria »), chunk 2 (par. 20-22) : le berger vendu à la tuerie, l'ironie « ce prix magnifique auquel j'ai été estimé », le bâton « Union » brisé (fraternité Juda/Israël), « Celui qu'ils ont transpercé », les idoles et les faux prophètes retranchés, la « troisième partie » affinée (« C'est mon peuple » / « Jéhovah est mon Dieu »), le jour de Jéhovah (14:1-9), les nations montant « d'année en année » (14:16) et les « plus de 50 fois » où revient l'expression « Jéhovah des armées ». Documents wol vérifiés 200 : **1101990099** (chunks 1-2 lus), **2007882**, **1200014577**, **2017607**, **1200004682**.
- S2 : recensement régénéré (modules clos = **793 paires**) ; **constat : les 14 chapitres de Zekaria (38/1-38/14) sont tous pris** → sources prises dans les évangiles, les psaumes et les épîtres : ZA506 (40/23, 19/28, 21/4) · ZA507 (40/27, 43/18, 19/41) · ZA508 (19/40, 40/17, 20/18) · ZA509 (43/19, 19/42, 40/28) · ZA510 (41/14, 19/32, 19/26) · ZA511 (42/22, 19/63, 43/21) ; contrôle : **18 paires uniques, 0 doublon interne, 0 collision avec les 793**.
- S3/S4 : `data/p8_za4.py` — trois chunks (`_za4a.py` : CAT ZA4 + ZA506 + ZA507 ; `_za4b.py` : ZA508 + ZA509 ; `_za4c.py` : ZA510 + ZA511), concaténés puis supprimés ; `py_compile` OK ; **112 472 o** ; corrections ciblées avant concaténation (« FUIRAIREZ » → « FUIRIEZ », « s'y dérobé » → « s'y dérobe » en ZA511, « presence » → « présence » en ZA508). QC — 6 fiches ; corps de prose (9 blocs) = **64 342 caractères** ; tous les blocs > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; **18 paires nwt, 0 doublon interne, 0 collision avec les 793** ; 0 CJK ; 0 lien non officiel ; build de contrôle `_TMP_ZA4.html` 173 509 o (11 blocs, 6 fiches, 33 sources) puis supprimé.
- S5/S6 : **7 JPG** (le berger au bâton brisé devant les brebis de mauvaise volonté ; les trente pièces d'argent jetées dans la maison de Jéhovah ; Jérusalem, coupe qui donne le vertige et pierre pesante pour les peuples ; le regard vers celui qui a été transpercé ; la source ouverte qui lave le péché ; le mont des Oliviers fendu et les eaux vives ; + la vignette `prophe_ZA4_vignette.jpg`) — 7/7 au premier essai ; **6/6 MP3** voice-05 = 11,7 · 10,4 · 10,8 · 9,9 · 13,5 · 12,8 s = **69,1 s** — 5/6 au premier essai, le texte de ZA508 d'abord refusé par la modération, accepté après reformulation adoucie.
- S7 : build final `preuves/FICHES8_ZACHARIE_4.html` **175 697 o** — 36 mentions wol, 6 balises audio, 12 fichiers médias de fiche référencés et tous présents (6 JPG + 6 MP3), 0 lien non officiel, vignette ZA4 non liée ; **purge ZA3 appliquée** (8 JPG + 7 MP3) → fenêtre = 12 JPG/12 MP3 (archives Daniel) + 6 JPG/5 MP3 (Aggée) + 7 JPG/6 MP3 (ZA4) = **25 JPG / 23 MP3** ; `collections/durations.py` régénéré → **23 pistes / 581,8 s** (9,7 min).
- S8 : §3cl 6/6 PUBLIÉE → **511/1000** ; compteurs : **560 JPG créés** (25 présents, dont 2 vignettes), **522 MP3** (23 pistes, 581,8 s) ; **Zacharie 1-14 est couvert (P490-P511), le livre est complet** ; §3cm ouvert — **Malachie (P512-P519, 8 entrées)** ; ensuite la suite de la « PARTIE 7 — LES PSAUMES ET LES ÉCRITS ».
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — le stock libre recensé après §3cl est de **369 chapitres** (sur 1 189) ; livres entiers consommés : Sophonie, Aggée, Zekaria (38/1-38/14) ; **Malachie 1-4 (39/1-39/4) est déjà pris** (p8_gen3, p8_jr20lm1, p8_am1, p8_ez5, p8_os3 — vagues antérieures à §3bt) → pour §3cm, puiser dans les passages libres en lien : **Nombres 18** (dîmes et Lévi), **Nombres 3/8** (service des Lévites), **Matthieu 19** (le divorce), **Luc 7** (le messager et Jean le Baptiste), **Lévitique 27** (vœux et dîmes, à tester), **Deutéronome 18** (à tester), **1 Chroniques / Esdras / Néhémie** restants, puis tester **Isaïe 40-66 partiels (23/40 pris, 23/45/60-66 pris)**, **Ézéchiel 34-39**, **Daniel 7-12**, **Joël 3**, **Révélation 1-22**, avant les épîtres non consommées.

Documents wol disponibles : **1101990099** (« Livre de la Bible numéro 38 — Zekaria », chunks 1-2 lus ; chunks 3-4 non lus) ; **2007882** ; **1200004682** ; **1200014577** ; **2017607** (chunk 2 non lu) ; à tester : « Livre de la Bible numéro 39 — Malachie », les articles « dîme », « Élie », « soleil de justice », « livre de souvenir ».

## 3cm. Vague P8-91 (ML — Malachie : l'amour de Jacob, le messager du temple, la dîme et le soleil de justice)
| Fiche | P | Sujet | État |
|---|---|---|---|
| ML512 | P512 | Malachie 1:2-5 · « j'ai aimé Jacob, j'ai haï Ésaü » ; Édom dit : « nous rebâtirons » — ils bâtiront, je démolirai | PUBLIÉE |
| ML513 | P513 | Malachie 1:6-14 · « vous méprisez mon nom » ; les animaux boiteux et malades offerts sur l'autel | PUBLIÉE |
| ML514 | P514 | Malachie 2:1-9 · l'alliance avec Lévi ; « vous avez fait trébucher beaucoup dans la loi » | PUBLIÉE |
| ML515 | P515 | Malachie 2:10-17 · « j'ai été témoin entre toi et la femme de ta jeunesse » ; « je hais le divorce » | PUBLIÉE |
| ML516 | P516 | Malachie 3:1-6 · « j'envoie mon messager qui préparera le chemin » ; il viendra soudain à son temple | PUBLIÉE |
| ML517 | P517 | Malachie 3:7-12 · « apportez les dîmes » ; la bénédiction jusqu'à ce qu'il n'y ait plus de pénurie | PUBLIÉE |
| ML518 | P518 | Malachie 3:13-18 · un livre de souvenir écrit devant lui pour ceux qui craignent Jéhovah | PUBLIÉE |
| ML519 | P519 | Malachie 4:1-6 · le jour brûlant comme un four ; le soleil de justice ; Élie envoyé avant le grand jour | PUBLIÉE |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, section « Malachie — prophète, après 443 av. n. è. ») : ML512 **Accomplie** (Édom jamais rétabli ; Nabatéens au IVe s. av. n. è.) · ML513 **Accomplie (déclaration)** (1:8-14) · ML514 **Accomplie (déclaration)** (2:8, 9) · ML515 **Accomplie (déclaration)** (2:14, 16) · ML516 **Accomplie** (Matthieu 11:10 ; Marc 1:2, 3 ; Luc 1:76 ; 7:27) · ML517 **Accomplie (condition)** (3:10) · ML518 **En cours** (3:16) · ML519 **Accomplie (1er accomplissement) / À venir** (Luc 1:17 ; Matthieu 11:14 ; 17:11-13 — Jean le Baptiste).

- S1 : 3 recherches approfondies (Malachie 1 — l'amour de Jacob et la haine d'Ésaü, la déclaration d'Édom « nous rebâtirons », la disparition du pays et l'installation des Nabatéens ; Malachie 2 — les animaux tarés, l'alliance de Lévi, la femme de la jeunesse et le divorce ; Malachie 3-4 — le messager du temple, l'affineur, les dîmes, le livre de souvenir, le soleil de justice et Éliya) ; lecture du registre (l. 186-198 : P512-P519) ; **lecture du document 1101990100** (« Livre de la Bible numéro 39 — Malaki », 3 chunks) : rédaction après 443 av. n. è. sous un gouverneur, situation des prêtres, les six disputations, le nom divin 48 fois dans quatre chapitres, « un livre de souvenir commença à être écrit », « le soleil de la justice se lèvera à coup sûr » et l'identification d'Éliya à Jean le baptiseur avec un accomplissement encore à venir au jour de jugement ; **lecture du document 1200002861** (« Malaki (Livre de) », Étude perspicace des Écritures, vol. 2, p. 197, 2 chunks) : situation au temps de Malaki, date de rédaction, harmonie avec le reste des Écritures, encadré « MALAKI — POINTS PRINCIPAUX ». Documents wol vérifiés 200 : **1101990100**, **1200002861**, **2007927**, **1200012800**, **1987443**, **1989489**.
- S2 : recensement régénéré (**842 paires** dans les 90 modules clos) ; constat : **les 4 chapitres de Malachie (39/1-39/4) sont tous pris** par cinq modules antérieurs à §3bt → sources puisées dans des chapitres libres et en lien : ML512 (1/32, 4/20, 4/21) · ML513 (3/1, 3/22, 4/18) · ML514 (2/28, 3/8, 5/10) · ML515 (40/19, 20/5, 22/8) · ML516 (40/14, 42/7, 43/8) · ML517 (5/14, 5/26, 47/9) · ML518 (19/56, 19/138, 54/6) · ML519 (40/20, 41/12, 42/23) ; contrôle : **24 paires uniques, 0 doublon interne, 0 collision avec les 842** ; stock de chapitres libres recensé : **369 sur 1 189**.
- S3/S4 : `data/p8_ml1.py` — quatre chunks (`_ml1a.py` : CAT ML1 + ML512 + ML513 ; `_ml1b.py` : ML514 + ML515 ; `_ml1c.py` : ML516 + ML517 ; `_ml1d.py` : ML518 + ML519), concaténés puis supprimés ; `py_compile` OK ; **186 500 o**. QC — 8 fiches ; corps de prose (9 blocs + texte) = **148 318 caractères** ; tous les blocs > 700 car. ; 10e bloc « ce que cette fiche ne dit pas » présent et non vide partout ; **24 paires nwt, 0 doublon interne, 0 collision avec les 842** ; 0 CJK ; 0 lien non officiel ; statuts conformes au registre (ML512/516 Accomplie ; ML513/514/515 Accomplie (déclaration) ; ML517 Accomplie (condition) ; ML518 En cours ; ML519 Accomplie (1er accomplissement) / À venir).
- S5/S6 : **9 JPG** (les montagnes d'Édom désolées et les ruines de Séir ; le prêtre présentant un animal taré devant l'autel du temple restauré ; le Lévite enseignant la Loi sous l'olivier ; la femme en larmes au pied de la muraille du temple ; l'affineur assis devant le creuset d'argent ; les chars et les jarres de la dîme apportés au magasin sous les écluses ouvertes ; le scribe écrivant le livre de souvenir à la lampe ; le soleil de justice se levant sur Jérusalem avec les veaux qui bondissent ; + la vignette `prophe_ML1_vignette.jpg`) — 9/9 au premier essai ; **8/8 MP3** voice-05 = 14,0 · 13,0 · 12,8 · 15,2 · 14,3 · 12,8 · 13,6 · 14,3 s = **110,0 s**, tous acceptés au premier essai.
- S7 : build final `preuves/FICHES8_MALACHIE_1.html` **270 411 o** — 51 mentions wol, 8 balises audio, 16 images référencées (8 JPEG de fiche + pictogrammes), 8 fichiers audio et 8 fichiers image de fiche référencés et tous présents, 0 lien non officiel, vignette ML1 non liée ; **purge AG1 appliquée** (6 JPG + 5 MP3 : prophe_AG1_vignette, prophe_AG485_maison … prophe_AG489_cachet et leurs 5 MP3) → fenêtre = 12 JPG/12 MP3 (Daniel) + 7 JPG/6 MP3 (ZA4) + 9 JPG/8 MP3 (ML1) = **28 JPG / 26 MP3** ; `collections/durations.py` régénéré → **26 pistes / 641,8 s** (10,7 min).
- S8 : §3cm 8/8 PUBLIÉE → **519/1000** ; compteurs : **569 JPG créés** (28 présents, dont 2 vignettes), **530 MP3** (26 pistes, 641,8 s) ; **Malachie est couvert en entier (P512-P519) et les douze « petits prophètes » sont achevés** ; §3cn ouvert — **P520-P527 : Ruth 4:11, 12 ; Ruth 4:17-22 ; 1 Chroniques 22:9, 10 ; Psaumes 2:1-6, 2:7, 2:8-12, 8:4-8, 16:8-11 (8 entrées)** — début de la « PARTIE 7 — LES PSAUMES ET LES ÉCRITS ».
Chapitres nwt : re-grepper `phase8/data/*.py` avant réservation — le stock libre recensé après §3cm est de **369 chapitres** (sur 1 189) ; livres entiers consommés : Sophonie, Aggée, Zekaria, Malachie ; pour §3cn, les passages utiles sont à chercher en priorité dans les chapitres libres : **Ruth 1** (pour le cadre du livre), **1 Samuel 16-17** (David, à tester), **2 Samuel 7** (pris ?), **1 Chroniques 17/28-29**, **Matthieu 1** (généalogie — à tester), **Luc 3** (généalogie — à tester), **Actes 13** (pris), **Hébreux 1** (pris), **1 Corinthiens 15** (pris), **Actes 2** (pris), **Matthieu 22** (pris), **Jean 15** (pris), **Révélation 2/19** (pris) ; puis puiser dans les chapitres libres restants : **Psaumes 2/8/16** sont eux-mêmes libres (19/2 pris, 19/16 pris, 19/8 pris — vérifier avant réservation), **Nombres 18**, **Deutéronome 18**, **Lévitique 27**, **Ézéchiel 34-39**, **Daniel 7-12**, **Joël 3**, **Révélation restants**.

Documents wol disponibles : **1101990100** (« Livre de la Bible numéro 39 — Malaki », 3 chunks lus, complet) ; **1200002861** (it-2 « Malaki (Livre de) », 2 chunks lus, complet) ; **2007927** (TG 2007, « Points marquants du livre de Malaki ») ; **1200012800** (Auxiliaire) ; **1987443**, **1989489** ; non lus : **1101990099** (chunks 3-4), **2017607** (chunk 2) ; à tester : « Livre de la Bible numéro 40 » (Matthieu) et les portails sur les Psaumes, David et Bethléem.

## 3cn. Vague P8-92 (RT — Ruth, Chroniques et les premiers Psaumes messianiques : la maison de Pérets, le fils qui bâtira la maison, et le roi installé sur Sion)
| Fiche | P | Sujet | État |
|---|---|---|---|
| RT520 | P520 | Ruth 4:11, 12 · « que Jéhovah fasse de cette femme comme Rachel et Léa » ; « que ta maison soit comme celle de Pérets » | A_PLANIFIER |
| RT521 | P521 | Ruth 4:17-22 · Obed, père de Jessé, père de David ; la généalogie jusqu'au roi | A_PLANIFIER |
| CH522 | P522 | 1 Chroniques 22:9, 10 · « un fils naîtra : Salomon ; il bâtira une maison à mon nom » | A_PLANIFIER |
| PS523 | P523 | Psaume 2:1-6 · les rois de la terre se massent contre Jéhovah et son oint ; « j'ai installé mon roi sur Sion » | A_PLANIFIER |
| PS524 | P524 | Psaume 2:7 · « tu es mon fils ; moi, aujourd'hui, je suis devenu ton père » | A_PLANIFIER |
| PS525 | P525 | Psaume 2:8-12 · « demande-moi, je te donnerai les nations » ; le sceptre de fer | A_PLANIFIER |
| PS526 | P526 | Psaume 8:4-8 · « tu l'as fait un peu inférieur aux anges » ; tout mis sous ses pieds | A_PLANIFIER |
| PS527 | P527 | Psaume 16:8-11 · « tu ne laisseras pas mon âme au Schéol » ; le fidèle ne verra pas la corruption | A_PLANIFIER |

Statuts du registre (18_REGISTRE_PROPHETIES_3.md, partie « LES PSAUMES ET LES ÉCRITS ») : RT520 **Accomplie** (Ruth 4:13-17 ; lignée de David) · RT521 **Accomplie** (Matthieu 1:5, 6 ; Luc 3:31, 32) · CH522 **Accomplie** (1 Rois 5:5 ; 6:1, 38 ; 2 Samuel 7:13) · PS523 **Accomplie** (Actes 4:25-28) · PS524 **Accomplie** (Actes 13:33 ; Hébreux 1:5 ; 5:5) · PS525 **À venir** (Révélation 2:26, 27 ; 19:15) · PS526 **Accomplie** (Hébreux 2:6-8 ; 1 Corinthiens 15:27) · PS527 **Accomplie** (Actes 2:25-32 ; 13:34, 35).

Chapitres nwt : re-grepper avant réservation ; réserver en priorité les chapitres libres liés à Ruth, aux Chroniques et aux Psaumes 2/8/16, puis les renvois du registre (Actes 4, 13 ; Hébreux 1, 2, 5 ; 1 Corinthiens 15 ; Révélation 2, 19 — tous pris) à remplacer par des chapitres libres équivalents.

Documents wol à tester : « Livre de la Bible numéro 8 — Ruth » et « Livre de la Bible numéro 12 — 1 Chroniques » (codes à découvrir), portails sur les Psaumes et le Messie ; réutiliser **1101990100**, **1200002861**, et les documents sur David et Bethléem.
