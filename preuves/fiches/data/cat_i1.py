#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE H-I (vague de transition) — LE SIGNE (2e partie) + REVELATION
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="H–I",
    nom="Le signe et les derniers jours (2e partie) · Le livre de la Révélation",
    vague="10",
    intro=(
        "Cette vague de transition ferme la catégorie H et ouvre la catégorie I. "
        "Côté signe, cinq dernières fiches : la grande tribulation (Cestius et "
        "Titus, l'ancienne lecture 1914-1918 citée comme révisée, les deux phases "
        "à venir), « paix et sécurité » (le déclencheur hotan, « pendant qu'ils "
        "parlent », et l'honnêteté citée : « nous ne pouvons pas affirmer »), les "
        "signes célestes (aussitôt après, Joël, la révision de 1975 à 1994, ni "
        "fusées ni voyages sur la lune), les faux Christs (localisé contre éclair, "
        "« si possible », le rassemblement de 24:31) et la persécution avec "
        "l'endurance (hupomenô, « rester sous », les deux fins). La catégorie H "
        "compte ainsi 10 fiches et est terminée. Côté Révélation, quatre premières "
        "fiches : la méthode (signes, sept, bientôt, « pas pour effrayer »), les "
        "sceaux (le blanc, c'est Jésus couronné en 1914 ; les âmes ; le silence), "
        "les trompettes (l'emboîtement, le tiers, Jéricho et l'Égypte, les deux "
        "témoins, la septième) et la femme contre le dragon (1914, le tiers tombé "
        "au temps de Noé, le reste). Périmètre : les bêtes, Babylone, les bols et "
        "Harmaguédon appartiennent aux vagues suivantes."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H006", titre="La grande tribulation — Cestius, Titus, et l'entière à venir",
 ref="Matthieu 24:15-22 ; Marc 13:19-20 ; Daniel 12:1 ; Révélation 7:14 ; 18:8",
 statut="Accomplie (70) + à venir (l'entière : Babylone puis Harmaguédon)",
 cat="H", syst="Système 66/70 · phases à venir",
 reg="Registre : Matthieu — P682 (24:15), P683 (24:16-20), P661 (24:21-22) ; Daniel — P404 (12:1) ; Révélation — P835 (7:14) ; Mc 13:19-20 sans entrée (C8)",
 texte=[
  "« Quand vous verrez la chose IMMONDE, dont Daniel a parlé, debout dans un "
  "lieu saint — que le lecteur exerce son discernement. » (Mt 24:15 — bdelugma !)",
  "« Que ceux en Judée FUIENT vers les montagnes ; toits, champs : pas de retour ; "
  "priez : ni hiver, ni sabbat. » (24:16-20 — pheugete !)",
  "« Alors : grande tribulation TELLE qu'il n'y en a pas eu depuis le commencement "
  "— non — et qu'il n'y en aura PLUS. » (24:21 — superlatif ABSOLU !)",
  "« Si ces jours n'étaient ÉCOURTÉS, NULLE chair ne serait sauvée ; mais POUR "
  "les élus, ils seront écourtés. » (24:22 — koloboo ! dia = POUR !)",
  "« Un temps de DÉTRESSE tel qu'il n'y en a pas eu depuis qu'il existe une nation "
  "— ton peuple ÉCHAPPERA, quiconque écrit dans le livre. » (Da 12:1 — Michel !)",
 ],
 contexte=(
  "« Chose immonde » (bdelugma : Da 9:27, 11:31, 12:11 ! — « lieu saint », topos "
  "hagios — parenthèse : « que le lecteur… » — Mc 13:14 aussi !). Cestius Gallus, "
  "66 : l'armée romaine ENCERCLE puis SE RETIRE — la FENÊTRE (voir B007 !). Titus, "
  "70 : printemps-été — la « grande tribulation » antique s'abat. Josèphe : 97 000 "
  "survivants emmenés captifs (Guerre) ; « plus d'un million » de morts — famine, "
  "luttes, Romains. ANCIENNE LECTURE révisée : « on expliquait que la grande "
  "tribulation avait commencé en 1914, arrêtée en novembre 1918, avec un intervalle "
  "pour l'œuvre » — révision CITÉE (voir Limites). L'ENTIÈRE est à venir : l'empire "
  "de la fausse religion D'ABORD, puis la guerre d'Harmaguédon. Deux phases modernes "
  "attendues : l'attaque contre la religion (« en un seul jour », Ré 18:8 !) PUIS "
  "le « telle… jamais plus »."
 ),
 explication=(
  "« Telle… non… plus » (24:21 : ou… oude — NI avant NI après : jamais-égale !). "
  "« Écourtés » (koloboo : AMPUTÉS — voir H002 !). « À cause / POUR » (dia + "
  "accusatif : le grec PERMET « pour les élus » — cité !). « Élus » (eklektoi : "
  "choisis — en 70 : les oints piégés, SAUVÉS par la levée du siège de 66 !). "
  "« Nulle chair » (sarx : AUCUNE — voir H002 !). Daniel 12:1 (« Michel DEBOUT » "
  "— voir I004 ! — « écrit dans le livre » : Mal 3:16 ! Ré 20:12 !). « SORTENT » "
  "(Ré 7:14 : voir G007 — survivent !). « Fuyez » (pheugete : 24:16 — IMMÉDIAT !). "
  "« Ni hiver ni sabbat » (24:20 : prière EXAUCÉE — Cestius se retire en automne 66, "
  "avant l'hiver — voir B007 !). « Malheur aux enceintes » (24:19 : fuite ralentie). "
  "« Chose immonde » (bdelugma : chose DÉTESTABLE — armées païennes au saint lieu !). "
  "« En un seul jour » (Ré 18:8 : rapidité de la phase 1 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : DOUBLE — 70 (Titus : printemps-été, "
  "97 000 captifs, ville et temple détruits « exactement comme annoncé ») + "
  "« accomplissement PRINCIPAL… universel » de nos jours. 66 = la fenêtre (Cestius : "
  "les oints s'échappent — Pella, voir B007 !). Moderne : phase 1 (religion, « en un "
  "seul jour » — « Jéhovah ne permettra pas… anéantisse la congrégation mondiale ») "
  "PUIS phase 2 (« telle… jamais plus »). « Jour de Jéhovah » = la grande tribulation "
  "(« prendra fin à Har-Maguédôn »). Ancienne lecture 1914-1918 : RÉVISÉE — citée, "
  "pas cachée (méthode E007). « Intervalle » actuel : l'œuvre (voir H004 !)."
 ),
 accomplissement=[
  ("66 de n. è.", "Cestius : encercle, se retire — la FENÊTRE (voir B007)"),
  ("70 de n. è.", "Titus : printemps-été — l'antique (97 000 captifs)"),
  ("1914-1918", "Ancienne lecture (« commencé-arrêté ») : RÉVISÉE, citée"),
  ("Maintenant", "Intervalle : l'œuvre avant la dernière partie (voir H004)"),
  ("« Paix et sécurité » (à venir)", "Le cri (voir H007)"),
  ("Phase 1 (à venir)", "Babylone : « en un seul jour » (vagues suivantes)"),
  ("Phase 2 (à venir)", "« Telle… jamais plus » → Harmaguédon"),
 ],
 hist=(
  "Cestius (66 : retraite inexpliquée — voir B007). Titus (70 : printemps-été). "
  "Josèphe (97 000 captifs — Guerre ; « million+ » : famine, luttes, Romains — "
  "ordre, voir Limites). Pella (fuite — voir B007). Novembre 1918 (arrêt WWI — "
  "ancienne lecture). « Jour brûlant comme le four » (Mal 4:1 — cité par article, "
  "sans P)."
 ),
 geo=(
  "Judée → MONTAGNES (24:16 : Pella — voir B007). Jérusalem ENCERCLÉE (66 + 70). "
  "« Toits, champs » : vie quotidienne interrompue. « Lieu saint » : le Temple — "
  "armées païennes (66). Moderne : UNIVERSELLE (« de nos jours… universelle »)."
 ),
 sci=(
  "97 000 (Josèphe, Guerre : captifs — dénombrés). « Million+ » : ordre DÉBATTU "
  "(démographie antique — voir Limites). 66→70 ≈ 3,5 ans : rapprochement NON fait "
  "par les publications — PAS de concordisme (voir Limites). Dia + accusatif : "
  "« à cause / pour » — philologie citée. « Un seul jour » (Ré 18:8 : rapidité)."
 ),
 limites=(
  "Moderne : phases ATTENDUES — aucune date, jamais. 66→70 ≈ 3,5 ans : rapprochement "
  "non fait — anti-concordisme assumé. « Million+ » : ordre débattu. Marc 13:19-20 "
  "sans entrée (C8). Malachie 4:1 : cité par article, sans P."
 ),
 tl=[("66", "Cestius : fenêtre"), ("70", "Titus : antique"), ("1914-18", "Lecture révisée"),
     ("Maintenant", "Intervalle : œuvre"), ("Cri", "« Paix » (H007)"), ("Ph.1", "Babylone : 1 jour"), ("Ph.2", "« Jamais plus »")],
 src=[("Serez-vous sauvé ? (écourtés POUR, 66, 2 phases, 1996)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996603"),
      ("Que le lecteur exerce son discernement (immonde, 1914 révisé, 1999)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1999323"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Daniel 12 — Bible d'étude, notes (détresse, Michel, livre)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/12")],
 img="images/prophe_H006_tribulation.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H007", titre="« Paix et sécurité ! » — le cri, le voleur, et l'honnêteté",
 ref="1 Thessaloniciens 5:1-5 ; Jérémie 6:14 ; Ézéchiel 13:10 ; Sophonie 1:14-18 ; Jérémie 25:32-33",
 statut="À venir (le cri ; « ne pas affirmer » : cité)",
 cat="H", syst="Système 50 · cri à venir",
 reg="Registre : 1 Thessaloniciens — P754 (5:1-3), P755 (5:4-5) ; Ézéchiel — P317 (13:1-23) ; Sophonie — P478 (1:14-18) ; Jr 6:14 sans entrée (C8)",
 texte=[
  "« Les temps et les ÉPOQUES : le jour de Jéhovah vient EXACTEMENT comme un "
  "voleur dans la nuit. » (1Th 5:1-2 — chronos/kairos ! kleptès !)",
  "« QUAND ils diront : PAIX ET SÉCURITÉ ! — alors destruction SOUDAINE sur eux, "
  "comme les DOULEURS sur la femme enceinte ; et ils n'échapperont ABSOLUMENT pas. » "
  "(5:3 — hotan : DÉCLENCHEUR ! ôdin ! double négation !)",
  "« Vous N'ÊTES PAS dans les ténèbres : ce jour ne vous surprendra pas comme des "
  "voleurs — fils du JOUR. » (5:4-5 — huioi photos !)",
  "« Ils guérissent LÉGÈREMENT : Paix, paix ! — et il n'y a PAS de paix. » "
  "(Jr 6:14 — shalom shalom ! C8)",
  "« Le grand jour de Jéhovah est PROCHE — TRÈS proche ; amer : le puissant pousse "
  "des cris. » (So 1:14 — P478 !)",
 ],
 contexte=(
  "Paul, ~50 (Thessalonique : parmi les PREMIÈRES lettres !). « Temps et époques » "
  "(chronos + kairos — Ac 1:7 : « pas à vous » ! — H001 !). « Jour de Jéhovah » "
  "(5:2 : voleur — voir H001 !). CRI « au point culminant de la présence » — pas des "
  "disciples (« ni ceux-ci ni son Royaume ne font partie du monde » : Jn 15:19, "
  "17:14, 18:36 !). « Plus que de simples propos » : une époque où les nations "
  "« sembleront parvenir… d'une façon EXCEPTIONNELLE » — mais APPARENCE : « une paix "
  "qui mène à destruction soudaine » n'est ni paix ni sécurité. NEB : « PENDANT "
  "qu'ils parlent » — la tribulation PENDANT le cri ! HONNÊTETÉ citée : « nous ne "
  "pouvons pas, pour l'instant, AFFIRMER que la situation actuelle réalise la "
  "prophétie — pas plus que… jusqu'à quel point ». Traités (« réduire les armements ») "
  "contre Ps 46:9 + Is 2:2-4 (« détruira TOUTES les armes… causes profondes »)."
 ),
 explication=(
  "« QUAND » (hotan : le DÉCLENCHEUR logique !). « ILS diront » (legôsin : EUX, 3e "
  "personne — pas nous !). « Eirènè » (PAIX : cessation !) + « asphaleia » (SÉCURITÉ : "
  "a-sphallô — NE PAS TRÉBUCHER : stabilité !). « SOUDAINE » (aiphnidios : soudain !). "
  "« Doit être SUR eux » (ephistatai : dessus !). « Ôdin » (DOULEURS — voir H002 : "
  "l'enfantement !). « Ou mè ekphygôsin » (« n'échapperont ABSOLUMENT pas » : DOUBLE "
  "négation grecque !). « Voleur » (kleptès, 5:2 — voir H001 !). « PAS ténèbres » "
  "(5:4 : « vous N'ÊTES PAS » — non surpris !). « Fils du jour » (5:5 : huioi photos "
  "— Ép 5:8 !). « Paix, paix » (Jr 6:14 : shalom redoublé — « LÉGÈREMENT » : "
  "superficiel ! — C8). « Mur de BOUE » (Éz 13:10-11, P317 : « badigeonné » — « pluie "
  "torrentielle » !). So 1:14 (« PROCHE, TRÈS proche » — « amer » — « puissant » !). "
  "Jr 25:33 (« tués… extrémité à extrémité » — « pas lamentés » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : CRI mondial — « à grands cris… un certain "
  "équilibre » — AU point culminant. Monde SEUL (pas les disciples !). Apparence "
  "EXCEPTIONNELLE (jamais vue). « PENDANT » (NEB : tribulation pendant le cri — "
  "voir H006 !). « Courte durée » (« quelles qu'elles soient… manifestement »). "
  "Peuple : « aura IDENTIFIÉ ce cri… à l'ABRI dans le refuge » (So 2:3 — voir H006 !). "
  "« MAIS il y aura des SURVIVANTS » (abandonné les voies, justice — voir G007 !). "
  "« Ne pas affirmer » : la méthode — citée. VRAIE paix : Ps 46:9 (« brise l'arc » !), "
  "Is 2:4 (« socs » !), Mi 4:3 (« plus apprendre la guerre » !)."
 ),
 accomplissement=[
  ("~50 de n. è.", "Lettre : parmi les PREMIÈRES (Thessalonique)"),
  ("Siècles", "« Parlent depuis… la guerre » : paroles anciennes"),
  ("1914 + de n. è.", "SDN, ONU : FAITS — « ne pas affirmer » (voir Limites)"),
  ("CRI (à venir)", "« Paix et sécurité ! » — proclamation mondiale"),
  ("« PENDANT » (à venir)", "Tribulation pendant le cri (voir H006)"),
  ("VRAIE (à venir)", "Ps 46, Is 2 : armes détruites, causes ôtées"),
 ],
 hist=(
  "~50 (Thessalonique : premières lettres). « Depuis… guerre » (paroles de paix "
  "anciennes). SDN/ONU : mentionnées comme FAITS, jamais comme accomplissements "
  "(voir Limites). Traités de désarmement (« réduire » contre « détruire »). NEB "
  "(traduction citée : « pendant »). So 2:3 (refuge : « cachés » — sans P)."
 ),
 geo=(
  "MONDIALE (cri des NATIONS — « à grands cris »). « Extrémité à extrémité » "
  "(Jr 25:33). « Refuge » (So 2:3 : cachés au jour de la colère). VRAIE : « terre "
  "ENTIÈRE » (Royaume — voir G009)."
 ),
 sci=(
  "Hotan : DÉCLENCHEUR (quand → alors). Asphaleia (a-sphallô : stabilité, "
  "non-trébuchement). Double négation (ou mè : ABSOLU). Ôdin (voir H002). NEB : "
  "philologie (« pendant qu'ils parlent »)."
 ),
 limites=(
  "AUCUNE organisation nommée comme accomplissement (« ne pas affirmer » — cité). "
  "Contenu exact du cri INCONNU (« jusqu'à quel point… pourparlers » — cité). "
  "Jérémie 6:14 sans entrée (C8). Sophonie 2:3 : mention sans P."
 ),
 tl=[("50", "Lettre : premières"), ("Siècles", "Paroles"), ("1914 +", "SDN/ONU : faits"),
     ("CRI", "« Paix ! »"), ("PENDANT", "Tribulation"), ("VRAIE", "Ps 46, Is 2")],
 src=[("Ce que dit la Bible de la paix et de la sécurité (pendant, 1991)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1991641"),
      ("La paix qui vient de Dieu : quand ? (cri, culminant, refuge)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986725"),
      ("1 Thessaloniciens 5 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/52/5"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H007_paix.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H008", titre="Signes dans le ciel — aussitôt après, ni fusées ni lune",
 ref="Matthieu 24:29-30 ; Marc 13:24-25 ; Luc 21:25 ; Joël 2:30-31 ; 3:15 ; Ésaïe 13:10 ; Ézéchiel 32:7-8 ; Révélation 6:12-14 ; Amos 5:18",
 statut="Accomplie (70 : modèle) + à venir (« aussitôt après »)",
 cat="H", syst="Dates AT neutres · 70 · à venir",
 reg="Registre : Matthieu — P663 (24:29), P664 (24:30) ; Marc — P987 (13:24-27) ; Luc — P663 (21:25-26) ; Joël — P426 (2:28-32), P428 (3:9-17) ; Ésaïe — P126 (13:1-22) ; Ézéchiel — P350 (32:1-16) ; Révélation — P825 (6:12-14), P826 (6:15-17) ; Am 5:18 sans entrée (C8)",
 texte=[
  "« AUSSITÔT APRÈS la tribulation de ces jours : soleil OBSCURCI, lune SANS "
  "lumière, étoiles TOMBANT, puissances ÉBRANLÉES. » (Mt 24:29 — eutheôs !)",
  "« Il y aura des SIGNES dans le soleil, la lune et les étoiles — et sur la terre "
  "l'ANGOISSE des nations. » (Lc 21:25 — P663 !)",
  "« Sang, FEU, colonnes de FUMÉE ; soleil en TÉNÈBRES, lune en SANG — avant le jour "
  "de Jéhovah, GRAND et REDOUTABLE. » (Jl 2:30-31 — P426 !)",
  "« Soleil et lune S'ASSOMBRIront, étoiles RETIRERONT leur éclat. » (Jl 3:15 — "
  "asaph : RETIRER !)",
  "« Soleil OBSCUR comme un sac de POIL, lune COMME du sang, étoiles comme des "
  "FIGUES secouées, ciel ENROULÉ comme un rouleau. » (Ré 6:12-14 — sakkos ! biblion !)",
  "« MALHEUR à ceux qui désirent le jour de Jéhovah : TÉNÈBRES, et pas lumière. » "
  "(Am 5:18 — C8 !)",
 ],
 contexte=(
  "« AUSSITÔT APRÈS » (eutheôs : IMMÉDIAT — pas des siècles !). w75 RÉVISÉE : « la "
  "tribulation = 70 ; aussitôt = siècles courts aux yeux de Dieu (Rm 16:20, 2P 3:8) » "
  "— 1994 : « examen PLUS APPROFONDI… explication quelque peu DIFFÉRENTE » — révision "
  "CITÉE (méthode E007). Joël : jugement — « jour GRAND et REDOUTABLE » (2:31). 70, "
  "Josèphe : « sang, feu, fumée » — « soleil n'éclairant pas les ténèbres… lune rouge "
  "comme du sang versé » — le MODÈLE. « PAS… durant les nombreuses décennies » : « "
  "l'arsenal des FUSÉES, les VOYAGES SUR LA LUNE et autres » — REJETÉS comme "
  "accomplissements ! EXÉCUTION, pas conclusion : les astres s'éteignent « quand les "
  "forces d'exécution ont marché »."
 ),
 explication=(
  "« Eutheôs » (AUSSITÔT : immédiateté !). « Skotisthèsetai » (OBSCURCI : passif !). "
  "« Ou dôsei » (« ne donnera PAS » : refus !). « Pesountai » (TOMBERONT !). « Dynameis » "
  "(PUISSANCES : astres ? gouvernements ? — sens précis renvoyé, voir Limites). "
  "« Saleuthèsontai » (ÉBRANLÉES — Hé 12:26-27 : « encore une FOIS » !). Joël 2:30 "
  "(« sang, feu, FUMÉE » : colonnes !). « Lune en SANG » (dam, 2:31 !). Joël 3:15 "
  "(« RETIRERONT » : asaph !). Ésaïe 13:10 (contre BABYLONE, P126 : « constellations » "
  "— kesil : ORION ! — « ne feront pas BRILLER »). Ézéchiel 32:7-8 (contre PHARAON, "
  "P350 : « COUVRIRAI » — kasa ! — « étoiles… lune… soleil »). Ré 6:12 (« sac de POIL » "
  "— sakkos : DEUIL ! — « lune COMME sang »). 6:13 (« FIGUES… grand vent » — figuier : "
  "voir H001 !). 6:14 (« ciel ENROULÉ comme ROULEAU » — biblion : papyrus ! — "
  "« montagnes, îles ÔTÉES »). 6:15-17 (« CACHEZ-nous ! » — P826 — « QUI peut "
  "subsister ? » — Ré 7 = RÉPONSE : voir G006-G007 !). Amos 5:18 (« MALHEUR… désirent » "
  "— « TÉNÈBRES, pas lumière » — C8 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : APRÈS la phase (tribulation PUIS signes "
  "— voir H006). « PAS durant les décennies » : fusées et lune REJETÉS. JUGEMENT : "
  "exécution, pas époque — « jour GRAND et REDOUTABLE ». 70 : Josèphe — le modèle "
  "(fumée, lune rouge). « Signe du Fils » (24:30, P664 : « nuées » = invisibilité — "
  "« érkhoménon » — « manifestation SURNATURELLE de son pouvoir royal » — adversaires "
  "« OBLIGÉS de remarquer » — voir H009 !)."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è. ?", "Ésaïe 13 : contre Babylone (539)"),
  ("VIe s. av. n. è. ?", "Ézéchiel 32 : contre Pharaon"),
  ("IXe s. av. n. è. ?", "Joël : sauterelles, jour redoutable"),
  ("70 de n. è.", "Josèphe : sang, feu, fumée — le MODÈLE"),
  ("1975 de n. è.", "w75 : lecture « aussitôt = siècles »"),
  ("1994 de n. è.", "w94 : « plus approfondi… différente » — RÉVISÉE"),
  ("« Aussitôt après » (à venir)", "Signes → « signe du Fils » (voir H009)"),
 ],
 hist=(
  "Babylone (Is 13 : 539 — voir E). Pharaon (Éz 32 : VIe siècle). Joël (sauterelles : "
  "P423-P425 — « jour » !). Josèphe (70 : fumée, lune rouge — cité !). 1969 (voyages "
  "lunaires : REJETÉS comme accomplissements — cité !). w75→w94 (révision citée)."
 ),
 geo=(
  "Babylone (Is 13). Égypte (Éz 32). Jérusalem (70 : fumée sur la ville). « Tribus de "
  "la terre » (24:30 : MONDE). « Montagnes, îles » (Ré 6:14 : relief ôté)."
 ),
 sci=(
  "Kesil (ORION — Is 13:10 !). « Figues-vent » : botanique (figues d'hiver tombant). "
  "Biblion : papyrus ENROULÉ — image du rouleau. « Lune sang » (70 : FUMÉE — pas "
  "astronomie !). Eutheôs : IMMÉDIAT (contre « siècles »)."
 ),
 limites=(
  "Sens symbolique précis (astres ? gouvernements ? les deux ?) : renvoyé aux "
  "publications. Amos 5:18 sans entrée (C8). « Signe du Fils » : détail en H009. "
  "w75 : lecture révisée — citée."
 ),
 tl=[("VIIIe ?", "Is 13 : Babylone"), ("VIe ?", "Éz 32 : Pharaon"), ("IXe ?", "Joël : jour"),
     ("70", "Josèphe : modèle"), ("1975", "w75 : siècles"), ("1994", "w94 : révisée"), ("À venir", "« Aussitôt »")],
 src=[("Dis-nous : quand ? (aussitôt, Joël, pas fusées, 1994)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1994123"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Révélation 6 — Bible d'étude, notes (sac, figues, rouleau)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/6"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H008_signes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H009", titre="Faux Christs et vraie venue — localisé contre éclair",
 ref="Matthieu 24:23-31 ; Marc 13:21-23 ; 2 Thessaloniciens 2:9 ; 1 Jean 4:3 ; Actes 20:29-30",
 statut="En cours (faux : depuis le Ier s. ; venue : à venir)",
 cat="H", syst="Système 33/1914 · exemples neutres",
 reg="Registre : Matthieu — P662 (24:23-25), P664 (24:30), P665 (24:31) ; 2 Thessaloniciens — P757 (2:3), P758 (2:8) ; 1 Jean — P789 (4:3) ; Actes — P719 (20:29-30) ; Mt 24:26-28, 2Th 2:9 sans entrée (C8)",
 texte=[
  "« Si l'on dit : Le Christ est ICI — ou LÀ — NE LE CROYEZ PAS. » (Mt 24:23 — "
  "hôde : LOCALISATION !)",
  "« Faux Christs et faux prophètes : GRANDS miracles et prodiges — pour égarer, "
  "SI POSSIBLE, MÊME les élus. » (24:24 — ei dynaton : CONDITIONNEL !)",
  "« Je vous l'ai annoncé D'AVANCE. » (24:25 — proeirèka : PARFAIT !)",
  "« Désert : N'Y ALLEZ PAS ; chambres : NE CROYEZ PAS — comme l'ÉCLAIR sort de "
  "l'est et brille jusqu'à l'ouest : ainsi la PRÉSENCE. » (24:26-27 — astrapè ! C8)",
  "« Où est le CADAVRE, là se rassembleront les AIGLES. » (24:28 — ptôma ! aetoi ! C8)",
  "« Le SIGNE du Fils dans le ciel ; TOUTES les tribus GEMISSENT ; le Fils sur les "
  "NUÉES, puissance et gloire. » (24:30 — sèmeion ! kop sontai !)",
  "« GRANDE trompette ; anges ; RASSEMBLERONT les élus des 4 VENTS. » (24:31 — "
  "salpinx ! P665 !)",
 ],
 contexte=(
  "« FAITES ATTENTION » (24:4 : blepete — voir H001 !). « Beaucoup… mon nom » (24:5 !). "
  "« Faux prophètes » (24:11, P657 !). Deutéronome 13 (faux prophètes AT : « MÊME si "
  "le signe arrive » — sans P). Matthieu 7:15 (« loups » — sans P). « ÉPROUVEZ les "
  "esprits » (1Jn 4:1 — P789 = 4:3 : « ANTÉCHRIST… DÉJÀ » !). « Du MILIEU de vous » "
  "(Ac 20:30, P719 : ex humôn — INTERNE ! — Milet, ~58 : « après mon départ »). "
  "« Antéchrist » (antichristos : CONTRE + À LA PLACE — 1Jn 2:18, 4:3, 2Jn 7 !). "
  "« Opération de Satan… signes MENSONGERS » (2Th 2:9 — energeia + pseudos — C8 !)."
 ),
 explication=(
  "« ICI / LÀ » (hôde : LOCALISER = suspect !). « Mè pisteusète » (NE CROYEZ PAS : "
  "consigne !). « Pseudochristoi » (FAUX-CHRISTS !) + « pseudoprophètai » "
  "(FAUX-PROPHÈTES !). « Sèmeia megala » (GRANDS miracles !) + « terata » (PRODIGES !). "
  "« EI DYNATON » (« SI POSSIBLE » : conditionnel — élus protégés ? tentés ? — "
  "portée renvoyée, voir Limites). « KAI » (MÊME : jusqu'aux élus !). « Eklektous » "
  "(ÉLUS — voir H006 !). « Proeirèka » (annoncé D'AVANCE : parfait — prévenus = armés !). "
  "« Désert » (erèmia, 24:26 : « N'Y ALLEZ PAS » — C8 !). « Chambres » (tameia : "
  "INTÉRIEUR — « NE CROYEZ PAS » — C8 !). « ÉCLAIR » (astrapè, 24:27 : « est… ouest » "
  "— VISIBLE PARTOUT — C8 !). « Parousia » (PRÉSENCE — voir H001 !). « Cadavre » (ptôma, "
  "24:28 — C8 !). « AIGLES » (aetoi : aigles ? vautours ? — identification renvoyée, "
  "voir Limites — C8 !). « Signe du Fils » (sèmeion, 24:30 — « DANS le ciel » !). "
  "« Kop sontai » (« frapperont la poitrine » — Za 12:10 ! Ré 1:7 !). « Nuées » "
  "(nephelai : INVISIBILITÉ — voir H008 !). « Érkhoménon » (VENANT !). « Salpinx » "
  "(TROMPETTE « GRANDE », 24:31 !). « 4 vents » (akrôn : EXTRÉMITÉS — monde !). "
  "« Antéchrist » (ANTI : contre + remplace ! — « DÉJÀ », 1Jn 4:3 !). « Loups LOURDS » "
  "(bareis, Ac 20:29 : « n'épargnant PAS » — « DU MILIEU » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : LOCALISÉ = faux (désert, chambres : "
  "« n'y allez pas, ne croyez pas »). VISIBLE = vrai (éclair est-ouest : nul besoin "
  "d'indicateur !). « Si possible » : avertissement MAXIMAL — même les élus visés. "
  "« D'avance » : la prévention. INTERNE (Ac 20:30 : « du milieu » — apostasie "
  "intérieure !). « Antéchrist DÉJÀ » (Ier siècle : 1Jn 4:3 !). Venue : « nuées » "
  "(invisible) + « OBLIGÉS de remarquer » (manifestation — voir H008 !). "
  "RASSEMBLEMENT (24:31 : anges + trompette — élus RÉUNIS des extrémités !)."
 ),
 accomplissement=[
  ("33 de n. è.", "« D'avance » : prévenus (Oliviers)"),
  ("Ier s.", "« DÉJÀ » (1Jn 4:3) — « du milieu » (Ac 20:29-30)"),
  ("132 de n. è.", "Bar Kokhba (« fils de l'étoile ») : EXEMPLE, pas accomplissement"),
  ("1914 + de n. è.", "Parousia : présence (voir H001)"),
  ("« Éclair » (à venir)", "Venue : RECONNUE (est-ouest)"),
  ("24:31 (à venir)", "Rassemblés : trompette, 4 vents"),
 ],
 hist=(
  "Bar Kokhba (132 : « fils de l'étoile » — Nb 24:17 ! — EXEMPLE : voir Limites). "
  "Theudas, Judas le Galiléen (Ac 5:36-37 : « 400 / 4 000 » — exemples, sans P). "
  "~58 (Milet : « après mon départ » — Ac 20). ~98 (1Jn : « DÉJÀ »). « Beaucoup » "
  "(24:5 : à travers les siècles)."
 ),
 geo=(
  "« Désert » (erèmia : Judée — cachettes !). « Chambres » (intérieur : secret !). "
  "« Est-ouest » (TOUT le ciel : public !). « 4 vents » (MONDE : extrémités !). "
  "« Cadavre-aigles » (champ : rassemblement !)."
 ),
 sci=(
  "Astrapè : ÉCLAIR — visible partout, sans guide (contre « ici/là »). « Si possible » : "
  "LOGIQUE conditionnelle (portée renvoyée). Aetoi : aigles/vautours — le vautour "
  "repère le cadavre de loin (identification renvoyée). « 4 vents » : 4 points. "
  "ANTI : contre + à la place."
 ),
 limites=(
  "« Si possible » : portée (impossible ? quasi ?) renvoyée aux publications. "
  "« Aigles » (24:28) : identification renvoyée. Bar Kokhba, Theudas : EXEMPLES "
  "historiques, pas accomplissements datés. Matthieu 24:26-28, 2 Thessaloniciens 2:9 "
  "sans entrée (C8). Mc 13:21-23, Dt 13, Mt 7:15 : parallèles sans P vérifié."
 ),
 tl=[("33", "« D'avance »"), ("Ier s.", "« DÉJÀ »"), ("132", "Bar Kokhba : exemple"), ("1914 +", "Parousia"),
     ("À venir", "« Éclair »"), ("24:31", "Rassemblés")],
 src=[("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Marc 13 — Bible d'étude, notes (parallèle : faux, signes)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/41/13"),
      ("1 Jean 4 — Bible d'étude, notes (éprouvez, antéchrist)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/62/4"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H009_faux.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H010", titre="Haïs et endurants — rester sous, jusqu'à la fin",
 ref="Matthieu 24:9-13 ; Luc 21:12-19 ; Matthieu 10:17-23 ; Jean 15:18-16:2 ; Révélation 2:10 ; 2 Timothée 3:12",
 statut="En cours (depuis 33 ; « jusqu'à la fin » : deux fins)",
 cat="H", syst="Système 33/70/1914",
 reg="Registre : Matthieu — P655 (24:9), P656 (24:10), P657 (24:11), P658 (24:12), P659 (24:13) ; Luc — P655 (21:12), P708 (21:12-15) ; Matthieu 10 — P708 (10:17-22) ; Jean — P709 (15:18-16:2) ; Révélation — P806 (2:10) ; Lc 21:16-19 sans entrée (C8)",
 texte=[
  "« On vous PERSÉCUTERA, on vous TUERA — et TOUTES les nations vous HAÏRONT à "
  "cause de mon NOM. » (Mt 24:9 — MONDIAL !)",
  "« Beaucoup TRÉBUCHERONT, se TRAHIRONT, se HAÏRONT ; faux prophètes ; iniquité ; "
  "l'amour du grand nombre REFROIDIRA. » (24:10-12 — skandalizô ! paradidômi ! "
  "psygèsetai !)",
  "« Celui qui aura ENDURÉ jusqu'à la FIN — celui-là sera SAUVÉ. » (24:13 — "
  "hupomeinas !)",
  "« Synagogues, PRISONS, rois, gouverneurs — je vous donnerai BOUCHE et SAGESSE "
  "qu'on ne pourra contredire. » (Lc 21:12-15 — P708 !)",
  "« Livrés par parents, frères, proches ; HAÏS de tous ; pas un CHEVEU perdu ; "
  "par votre ENDURANCE, acquérez vos ÂMES. » (Lc 21:16-19 — C8 !)",
  "« Le monde vous HAIT — vous N'ÊTES PAS du monde ; l'heure vient : qui vous TUERA "
  "croira offrir un SERVICE SACRÉ. » (Jn 15:18-16:2 — latreia !)",
  "« Sois FIDÈLE jusqu'à la MORT : couronne de vie. » (Ré 2:10 — P806 !)",
 ],
 contexte=(
  "« HAÏS PAR TOUS — pas seulement par les Israélites » : MONDIAL — « après sa mort "
  "et sa résurrection » (prédication mondiale !). « Frère livrera FRÈRE » (Mt 10:21, "
  "P708 : famille !). « PRÉDICATION primordiale » : « prudent… liberté… QUAND on vous "
  "persécutera : fuyez dans une AUTRE » (10:23 !). « Pas achevé le tour » (10:23b : "
  "sens renvoyé — voir Limites). « Le disciple n'est PAS au-dessus » (10:24 : comme "
  "le Maître !). « HEURE » (Jn 16:2 : « service SACRÉ » — latreia : tuer = adorer !). "
  "« TOUS… persécutés » (2Tm 3:12 — voir H005 !). « HAINE… MORT » (Mt 5:10-12, 10:22, "
  "Ré 2:10 — « ATTENDONS » !). DEUX FINS : « fin de notre vie OU fin du système » — "
  "dans les deux : fidèles."
 ),
 explication=(
  "« Persécutera… TUERA » (24:9 : thlipsis + apokteinô !). « TOUTES les nations » "
  "(pasôn tôn ethnôn : MONDIAL !). « Mon NOM » (onoma : la CAUSE !). « Trébucheront » "
  "(skandalizô, 24:10 : SCANDALISÉS !). « Trahiront » (paradidômi : LIVRERONT — "
  "comme Judas !). « Iniquité » (anomia, 24:12 : SANS-LOI !). « REFROIDIRA » (psygèsetai : "
  "REFROIDI — amour CONGELÉ !). « HUPOMEINAS » (24:13 : « RESTER SOUS » — littéral ! "
  "— Lc 2:43 ! Ac 17:14 !). « Hupomonè » (ENDURANCE : « COURAGEUSE, FERME, PATIENTE… "
  "ne perd pas ESPOIR » !). « FIN, pas départ » (« ce qui compte : la FIN » !). "
  "« Œuvre COMPLÈTE » (Jc 1:4 : laisser l'épreuve « suivre son cours JUSQU'AU BOUT » "
  "— pas de raccourci contraire aux Écritures !). « Attachement » (eusebeia, 1Tm 6:11 : "
  "« SANS… pas plaire » !). « BOUCHE et SAGESSE » (Lc 21:15 : « ne pourront CONTREDIRE » "
  "— antistènai !). « CHEVEU » (21:18 : HYPERBOLE de protection — C8 !). « ÂMES » "
  "(psychas, 21:19 : VIES acquises !). « Service SACRÉ » (latreia, Jn 16:2 : "
  "meurtre-ADORATION !). « FIDÈLE jusqu'à MORT » (Ré 2:10 : achri thanatou ! — "
  "« COURONNE de vie » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : MONDIAL (« haïs par TOUS » — pas Israël "
  "seul !). PRÉDICATION d'abord (« prudent, liberté, fuir » — 10:23 !). COMME le "
  "Maître (10:24 : « supporter… semblables » !). ENDURANCE = « rester SOUS » : patient, "
  "courageux, ferme — « SANS cette qualité : PAS de vie éternelle » (Rm 2:7, Hé 10:36, "
  "Ré 14:12 !). « FIN, pas départ » : convertis superficiels (« acceptent vite… "
  "renoncent vite » contre « profond intérêt… fermes »). DEUX fins (vie OU système). "
  "« Attachement » ajouté (1Tm 6:11 : sinon « pas plaire »). Famille (« plus dures… "
  "famille, voisins » — collègues, classe : « transiger » !). « ATTENDONS » (jour "
  "proche : So 1:14 ! Jl 1:15 !)."
 ),
 accomplissement=[
  ("33 de n. è.", "Avertis : persécutés, tués, haïs (Oliviers)"),
  ("Ier s.", "Étienne (Ac 7), Jacques (Ac 12) — synagogues, prisons, rois"),
  ("70 de n. è.", "Fuite : Pella (voir B007)"),
  ("Siècles", "Persécutés : « comme le Maître »"),
  ("1914 + de n. è.", "« Haïs par TOUS » : mondial"),
  ("« Fin » (2 fins)", "Vie OU système : endurer → sauvé"),
 ],
 hist=(
  "Étienne (Ac 7 : premier martyr). Jacques (Ac 12 : Hérode). « Synagogues » "
  "(flagellation : 39 coups — 2Co 11:24 !). « Prisons » (Ac 12, 16 : Pierre, Paul). "
  "« Rois » (Paul : Agrippa, César — Ac 25-26 !). Cas modernes PRÉCIS : renvoyés aux "
  "publications — pas de liste ici (voir Limites)."
 ),
 geo=(
  "« Villes d'Israël » (Mt 10:23 : « pas achevé » — sens renvoyé !). « Synagogues… "
  "prisons… rois » : TROIS lieux. « Toutes nations » : MONDE. « Fuyez » : ville → "
  "ville (mobilité !)."
 ),
 sci=(
  "Hupomenô : « RESTER SOUS » (littéral — Lc 2:43, Ac 17:14). Hupomonè : 3 adjectifs "
  "(courageuse, ferme, patiente). « Cheveu » (21:18 : hyperbole — C8). « Bouche et "
  "sagesse » : incontradictoire (21:15). DEUX fins : logique (vie OU système)."
 ),
 limites=(
  "Cas modernes précis : renvoyés aux publications — PAS de liste ici. Matthieu 10:23b "
  "(« pas achevé ») : sens renvoyé. Luc 21:16-19 sans entrée (C8). Mt 10:22, Lc 21:18 : "
  "sans P isolée (couverts par C8)."
 ),
 tl=[("33", "Avertis"), ("Ier s.", "Étienne, Jacques"), ("70", "Pella"), ("Siècles", "Comme Maître"),
     ("1914 +", "« Par TOUS »"), ("Fin", "2 fins : sauvé")],
 src=[("Préparation à la persécution (haïs par tous, fuir, gt 50)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101991052"),
      ("Endurance — Insight (hupomenô, rester sous, fin pas départ)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001360"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Luc 21 — Bible d'étude, notes (prisons, bouche, cheveux)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/21")],
 img="images/prophe_H010_endurance.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I001", titre="La méthode de Révélation — signes, sept, bientôt, courage",
 ref="Révélation 1:1-3, 10-20 ; 2:10 ; 3:10 ; Genèse 40:8 ; 2 Pierre 3:8 ; Daniel 12:4",
 statut="En cours (comprise depuis 1914 ; « bientôt » : rapidité finale)",
 cat="I", syst="Système 96/1914",
 reg="Registre : Révélation — P792 (1:1), P793 (1:3), P794 (1:10-11), P795 (1:12-16), P796 (1:17-18), P797 (1:19-20), P806 (2:10), P809 (3:10)",
 texte=[
  "« Révélation DE Jésus Christ — Dieu la lui donna pour MONTRER à ses esclaves "
  "ce qui doit arriver BIENTÔT — exprimée en SIGNES par son ange à Jean. » "
  "(Ré 1:1 — apokalypsis ! en tachei ! esèmanen !)",
  "« BIENHEUREUX qui LIT, qui ENTENDENT, qui OBÉISSENT — le temps est PROCHE. » "
  "(1:3 — makarios ! tèrountes ! kairos engys ! — 1re des 7 !)",
  "« Au JOUR DU SEIGNEUR, une voix comme une TROMPETTE : écris aux 7 "
  "congrégations. » (1:10-11 — kuriakè hèmera !)",
  "« 7 porte-lampes d'OR ; fils d'homme : yeux FLAMME, voix EAUX, ÉPÉE de la bouche, "
  "visage SOLEIL. » (1:12-16 — luchnia ! rhomphaia !)",
  "« N'AIE PAS PEUR : Premier et Dernier ; VIVANT — MORT — siècles ; CLÉS de la mort "
  "et de l'hadès. » (1:17-18 — kleis !)",
  "« Écris : VUES, SONT, VENIR — 7 étoiles = ANGES ; 7 lampes = CONGRÉGATIONS. » "
  "(1:19-20 — le livre S'EXPLIQUE !)",
 ],
 contexte=(
  "Jean, ~96 (Patmos : « à cause de la parole » — 1:9 ! — Domitien : tradition, voir "
  "Limites). « Esclaves » (douloi : DESTINATAIRES — pas le monde !). « BIENTÔT » (en "
  "tachei : RAPIDITÉ — « un jour = mille ans » (2P 3:8) : « mille ans OU PLUS » !). "
  "« Jour du Seigneur » (kuriakè hèmera : le jour de Jéhovah, temps de la fin — "
  "renvoyé, voir Limites — PAS le dimanche !). Sept congrégations RÉELLES d'Asie "
  "(Éphèse… Laodicée — ch. 2-3 ! — PAS sept époques : renvoyé, voir Limites). « Gardé "
  "de l'HEURE » (3:10, P809 !). « Fidèle jusqu'à MORT » (2:10, P806 — voir H010 !). "
  "« Scellé » (Da 12:4, P406 : « jusqu'au temps de la fin » !)."
 ),
 explication=(
  "« Apokalypsis » (RÉVÉLATION : DÉVOILEMENT — pas « catastrophe » !). « DE Jésus » "
  "(génitif : Dieu → Jésus → ANGE → Jean → ESCLAVES : chaîne à 5 maillons !). « Deixai » "
  "(MONTRER : vision !). « En tachei » (BIENTÔT : rapidité UNE FOIS commencé !). "
  "« Esèmanen » (« exprimées en SIGNES » — sèmainô : SIGNIFIER : TOUT le livre est "
  "signes !). « Makarios » (BIENHEUREUX : 7× — 1:3, 14:13, 16:15, 19:9, 20:6, 22:7, "
  "22:14 !). « Anaginôskôn » (LIT : publiquement !). « Tèrountes » (OBÉISSENT : gardent !). "
  "« Kairos engys » (« temps PROCHE » !). « SEPT » (PLÉNITUDE : sceaux, trompettes, "
  "plaies, lampes, étoiles, tonnerres — 6×7+ ! — « achèvement du SAINT SECRET » !). "
  "« Dieu donne les INTERPRÉTATIONS » (Gn 40:8 ! — Parole + ESPRIT + CANAL + TEMPS + "
  "ATTITUDE !). « Esclave » (nourriture : voir H001 !). « Porte-lampes » (luchnia : "
  "Za 4 ! Ex 25 !). « Étoiles = anges » (1:20 : angelos — surveillants ? messagers ? — "
  "renvoyé, voir Limites). « Épée » (rhomphaia, 1:16 : 19:15 ! — PAROLE !). « Clés » "
  "(kleis : AUTORITÉ — « mort et hadès » : voir G004 !). « PAS pour EFFRAYER » "
  "(« réconforter et ENCOURAGER… avec foi » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : SIGNES — tout est symbolique, et la Bible "
  "s'explique (1:20 : le livre SE DÉCODE !). SEPT = PLÉNITUDE (« achèvement du saint "
  "secret »). « Bientôt » : rapidité finale + mille ans (2P 3:8). « Bienheureux » : "
  "lire + entendre + OBÉIR. « PAS effrayer » : réconfort ! CANAL : Parole, esprit, "
  "instrument terrestre, TEMPS (« nourriture en temps convenable »), attitude. "
  "Congrégations RÉELLES (Asie — « gardé de l'heure », 3:10 ! — « fidèle », 2:10 !)."
 ),
 accomplissement=[
  ("~96 de n. è.", "Patmos : la vision (« à cause de la parole »)"),
  ("Ier s.", "7 congrégations : lettres RÉELLES (Asie)"),
  ("Siècles", "Signes SCELLÉS (Da 12:4 : « temps de la fin »)"),
  ("1914 + de n. è.", "« Temps » : COMPRIS (canal, nourriture)"),
  ("« Bientôt » (à venir)", "Rapidité : une fois commencé"),
 ],
 hist=(
  "Patmos (île Égée : « parole » — 1:9). Domitien : TRADITION — signalée (voir "
  "Limites). Sept villes (Éphèse… Laodicée : ROUTE postale romaine — circuit !). "
  "« Trompette » (1:10 : shofar ? — appel !)."
 ),
 geo=(
  "Patmos (Égée : exil avec vue !). Sept villes (OUEST Asie Mineure : circuit "
  "romain !). « Lampes » (tabernacle : Ex 25 !). « Soleil, étoiles » (ciel : gloire !)."
 ),
 sci=(
  "SEPT : plénitude — 6 séries de 7+ (sceaux, trompettes, plaies, lampes, étoiles, "
  "tonnerres). « Bientôt » (2P 3:8 : 1 jour = 1 000 ans). Chaîne : 5 maillons "
  "(Dieu → esclaves). 7 makarios : liste (1:3… 22:14)."
 ),
 limites=(
  "Domitien : tradition — signalée. « Jour du Seigneur » : sens renvoyé aux "
  "publications (pas le dimanche). « Anges » (1:20) : sens renvoyé. Sept époques : "
  "NON — renvoyé. Détail des bêtes : vagues suivantes (I suite)."
 ),
 tl=[("96", "Patmos : vision"), ("Ier s.", "7 lettres : réelles"), ("Siècles", "Scellés : Da 12"),
     ("1914 +", "Compris : canal"), ("À venir", "« Bientôt »")],
 src=[("Ce que représentent les bêtes (signes, interprétations, bientôt)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1962885"),
      ("Révélation à Jean — Insight (sept, pas effrayer, plan)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013627"),
      ("Révélation 1 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/1"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I001_methode.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I002", titre="Les sept sceaux — le blanc, les âmes, le silence",
 ref="Révélation 5:1-5 ; 6:1-17 ; 8:1 ; 19:11-16 ; Matthieu 25:31-46",
 statut="En cours (chevauchée depuis 1914 ; 6e-7e : à venir)",
 cat="I", syst="Système 33/1914",
 reg="Registre : Révélation — P820 (6:1-2), P821 (6:3-4), P822 (6:5-6), P823 (6:7-8), P824 (6:9-11), P825 (6:12-14), P826 (6:15-17), P828 (8:1) ; ch. 5 sans entrée (contexte)",
 texte=[
  "« BLANC ; arc ; COURONNE DONNÉE ; sorti en VAINQUEUR et pour VAINCRE. » "
  "(Ré 6:2 — leukos ! edothè ! nikôn-nikèsè !)",
  "« ROUX : ôter la PAIX. NOIR : ration. PÂLE : la MORT, le QUART. » (6:3-8 — "
  "voir H002-H003 !)",
  "« ÂMES sous l'autel : COMBIEN, saint et VÉRIDIQUE, avant de VENGER ? — robes "
  "BLANCHES — encore un PEU. » (6:9-11 — psychai ! pôs ! ekdikeô ! mikron !)",
  "« Sac de POIL, lune SANG, FIGUES, ciel ENROULÉ — CACHEZ-nous ! QUI peut "
  "subsister ? » (6:12-17 — voir H008 !)",
  "« SILENCE dans le ciel — environ une DEMI-HEURE. » (8:1 — sigè ! — renvoyé !)",
  "« FIDÈLE et VÉRIDIQUE ; PAROLE de Dieu ; ROI des rois — juge et combat avec "
  "JUSTICE. » (19:11-16 — IDENTIFICATION du blanc !)",
 ],
 contexte=(
  "« Livre… 7 SCEAUX » (5:1 : biblion — « écrit DEDANS et DERRIÈRE » — Éz 2:10 ! — "
  "ch. 5 : contexte, sans P). « DIGNE » (axios, 5:2, 5:5 : « LION de Juda… AGNEAU… "
  "7 CORNES… 7 YEUX » !). L'Agneau OUVRE (6:1 : SEUL digne !). « 4 VIVANTS » (zôa, "
  "4:6-8 : Éz 1 ! — « VIENS » ×4 !). « 24 anciens » (4:4 : couronnes, trônes !). "
  "Chevaux (Za 1:8, 6:1-8 : chars ! — sans P). Blanc : « PAS à la résurrection » — "
  "couronne en 1914, pas en 33 ! Les 3 autres = CONDITIONS mondiales (pas personnes !) : "
  "« touche CHAQUE individu »."
 ),
 explication=(
  "BLANC (leukos : JUSTICE — 3:4, 7:9 !). « Arc » (toxon !). « COURONNE DONNÉE » "
  "(edothè : PASSIF DIVIN — Dieu donne : 1914 !). « Nikôn… nikèsè » (« vainqueur… "
  "VAINCRE » : redondance — acquis + à finir !). « PAROLE de Dieu » (19:11-13 : "
  "LE blanc = Jésus — Jn 1:1 !). « Fidèle… Véritable » (19:11 !). « Roi… Seigneur » "
  "(19:16 !). « Guerre avec JUSTICE » (blanc = juste guerre !). « Achèvera » (« mener "
  "à TERME » : Paradis !). SÉPARATION (Mt 25 : brebis/chèvres — « retranchement… "
  "vie » 25:46 !). ROUX (voir H002 !). NOIR (voir H003 !). PÂLE (voir H003 !). 5e : "
  "« ÂMES » (psychai : VIES — pas immortelles : voir G004 !). « Sous l'AUTEL » (sang "
  "versé : Lv 4:7 !). « CRIENT » (sang d'Abel : Gn 4:10 !). « COMBIEN » (pôs : « jusqu'à "
  "QUAND » — Ps 13:2 ! Ha 1:2 !). « Saint et VÉRIDIQUE » ! « VENGER » (ekdikeô : "
  "faire JUSTICE !). « Robes BLANCHES » (justice !). « Un PEU » (mikron : PATIENCE — "
  "2P 3:8 !). 6e : signes (voir H008 !). 7e : « SILENCE » (sigè, 8:1 — « DEMI-HEURE » : "
  "sens renvoyé, voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : BLANC = JÉSUS (19:11-13 — « Parole » — "
  "guerre JUSTE, « pas malhonnête ni abusive »). COURONNE 1914 (« nouvellement "
  "intronisé » — pas 33 !). « Achèvera sa victoire » (fléaux, famines, guerres "
  "ÔTÉS — Paradis !). SÉPARATION (brebis/chèvres : Mt 25 — « durant la chevauchée » !). "
  "TROIS = conditions MONDIALES (guerre, disette, mort — voir H002-H003). 5e : martyrs "
  "+ « un peu » (patience !). 6e : jour de Jéhovah (voir H008). 7e : → TROMPETTES "
  "(voir I003 !)."
 ),
 accomplissement=[
  ("33 de n. è.", "Agneau : DIGNE d'ouvrir (ch. 5)"),
  ("1914 de n. è.", "COURONNE : la chevauchée commence (voir B009)"),
  ("1914 + de n. è.", "Trois conditions : guerre, disette, mort (H002-H003)"),
  ("« Un peu » (en cours)", "5e sceau : patience (robes blanches)"),
  ("6e (à venir)", "Signes : jour de Jéhovah (voir H008)"),
  ("7e (à venir)", "Silence → trompettes (voir I003)"),
 ],
 hist=(
  "1914 (couronne — voir B009). « Deuxième décennie » (« faits notables » — chevauchée "
  "reconnue). Abel (Gn 4:10 : sang qui CRIE). Lévitique 4:7 (sang SOUS l'autel). "
  "« Brebis/chèvres » (Mt 25:46 : deux sorts)."
 ),
 geo=(
  "« Terre » (conditions MONDIALES — « chaque individu »). « Autel » (sous : le sang). "
  "« 4 vents » (7:1 : voir G006). « Ciel » (silence : 8:1)."
 ),
 sci=(
  "SEPT : plénitude (voir I001). « Couronne DONNÉE » (passif divin : Dieu → Jésus). "
  "« Vainqueur-vaincre » : redondance (acquis + futur). « Un peu » (mikron : relatif "
  "— 2P 3:8). « Demi-heure » : chronométrie CÉLESTE — renvoyée."
 ),
 limites=(
  "Silence (8:1) : sens renvoyé aux publications. « Demi-heure » : renvoyée. « Âmes » "
  "(6:9) : VIES — détail voir G004. Zacharie 1/6, Révélation 5 : mentions sans P "
  "(contexte)."
 ),
 tl=[("33", "Digne : Agneau"), ("1914", "COURONNE !"), ("1914 +", "3 conditions"), ("En cours", "« Un peu »"),
     ("6e", "Signes (H008)"), ("7e", "Silence → trompettes")],
 src=[("Les cavaliers : qui sont-ils ? (blanc = Jésus, 1914, 2017)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2017086"),
      ("Leur chevauchée vous touche (séparation, achèvera, 1986)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986040"),
      ("Révélation 6 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/6"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I002_sceaux.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I003", titre="Les sept trompettes — le tiers, Jéricho, les témoins, le Royaume",
 ref="Révélation 8:1-13 ; 9:1-21 ; 10:1-11 ; 11:1-19 ; Josué 6 ; Exode 7-10",
 statut="En cours (2 témoins : 1914-1918 ; 7e : céleste ; détail : renvoi)",
 cat="I", syst="Système types AT · 96/1914 (F016)",
 reg="Registre : Révélation — P828 (8:1), P837 (8:2-6), P838 (8:7), P839 (8:8-9), P840 (8:10-11), P841 (8:12), P842 (8:13), P843 (9:1-6), P844 (9:7-11), P845 (9:13-16), P846 (9:17-19), P847 (9:20-21), P848 (10:1-2), P849 (10:3-4), P850 (10:6-7), P851 (10:8-11), P852 (11:1-2), P853 (11:3-6), P854 (11:7-10), P855 (11:11-13), P856 (11:15-19) ; Josué — P066 (6:26)",
 texte=[
  "« SILENCE… 7 anges… PRIÈRES des saints… ENCENSOIR jeté : tonnerres, éclairs, "
  "séisme. » (Ré 8:1-6 — 5e sceau EXAUCÉ !)",
  "« Grêle + FEU + SANG : TIERS brûlé. Montagne : TIERS mer. Étoile ABSINTHE : TIERS "
  "eaux AMÈRES. TIERS astres frappé. » (8:7-12 — triton ! apsinthos !)",
  "« AIGLE au ZÉNITH : MALHEUR, MALHEUR, MALHEUR ! » (8:13 — aetos ! ouai ×3 !)",
  "« 5e : puits, SAUTERELLES — pas d'herbe ! — SCEAU — 5 MOIS — scorpions — ABADDON. » "
  "(9:1-11 — CONTRE-nature !)",
  "« 6e : 4 anges de l'EUPHRATE — TIERS tué — heure, jour, mois, année — PAS REPENTIS. » "
  "(9:13-21 — Pharaon !)",
  "« Petit ROULEAU : DOUX puis AMER — prophétiser ENCORE. » (10:8-11 — biblaridion !)",
  "« 2 TÉMOINS : 1 260 jours — TUÉS — 3,5 jours — MONTENT — séisme, 7 000. » "
  "(11:3-13 — voir F016 !)",
  "« 7e : le Royaume EST DEVENU — nations COURROUCÉES — détruire ceux qui DÉTRUISENT "
  "— ARCHE vue. » (11:15-19 — voir G009 !)",
 ],
 contexte=(
  "« 7e sceau → 7 TROMPETTES » (8:1-2 : EMBOÎTEMENT — voir I001-I002 !). « Prières des "
  "saints » (8:3-4 : ENCENS — Ps 141:2 ! — le 5e sceau EXAUCÉ : voir I002 !). « Encensoir "
  "sur la terre » (8:5 : tonnerres, éclairs, séisme !). JÉRICHO (Jos 6 : 7 trompettes, "
  "7 jours — P066 = 6:26 ! — « MURS » !). PLAIEST D'ÉGYPTE (grêle Ex 9 ! eau-sang Ex 7 ! "
  "ténèbres Ex 10 ! sauterelles Ex 10 !). « TIERS » (triton : PARTIEL — pas total : "
  "APPEL !). « 3 MALHEURS » (ouai : 8:13, 9:12, 11:14 !). « 2 témoins » (1914-1918 : "
  "voir F016 !). 7e (11:15 : voir G009 — « ARCHE » 11:19 : Ex 25 !)."
 ),
 explication=(
  "« Trompette » (salpinx : AVERTIR du danger — Éz 33:3-6 : « sang sur LUI » ! — "
  "Nb 10 ! Jl 2:1 !). « Encens » (thymiama : PRIÈRES — Ps 141:2 !). « Grêle+feu+sang » "
  "(8:7 : Ex 9 !). « Montagne EMBRASÉE » (8:8 : Jr 51:25 — « montagne DESTRUCTRICE » !). "
  "« ABSINTHE » (apsinthos, 8:11 : AMER — Jr 9:15, 23:15 ! Lm 3:15 ! — un NOM !). "
  "« Aigle… ZÉNITH » (8:13 : aetos + mesouranèma — VU PARTOUT : voir H004 !). « MALHEUR "
  "×3 » (ouai ouai ouai !). 5e : « étoile TOMBÉE » (9:1 : CLÉ du puits !). « Sauterelles » "
  "(akrides : Jl 1-2 ! — « PAS d'herbe » 9:4 : CONTRE-nature ! — « SCEAU » 9:4 : voir "
  "G006 ! — « 5 MOIS » : saison ! — « SCORPIONS » ! — « Abaddon/Apollyon » 9:11 : "
  "DESTRUCTION / DESTRUCTEUR — Jb 26:6, 28:22 ! Pr 15:11 ! — roi : renvoyé, voir "
  "Limites). 6e : « EUPHRATE » (9:14 : Cyrus — 539 ! — « 4 anges LIÉS » !). « TIERS tué » "
  "(9:15 : « HEURE, jour, mois, année » : PRÉCISION !). « PAS REPENTIS » (9:20-21 : "
  "« ni… ni » ×5 — comme PHARAON !). 10 : « petit rouleau » (biblaridion : Éz 2:9-3:3 ! "
  "— « DOUX… AMER » !). « Plus de DÉLAI » (10:6 : chronos !). « Mystère ACHEVÉ » "
  "(10:7 : à la 7e !). 11 : « MESURÉ » (11:1 : kalamos — Éz 40 ! Za 2 !). 2 témoins "
  "(11:3-12 : « oliviers… lampes » — Za 4 ! — « 3,5 JOURS » ! — « SÉISME… 7 000 » "
  "11:13 : 7×1000 ! — voir F016 !). 7e (11:15 : voir G009 ! — « COURROUCÉES » ! — "
  "« DÉTRUIRE… DÉTRUISENT » — diaphtheirô, 11:18 ! — « ARCHE VUE » 11:19 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : EMBOÎTEMENT (le 7e sceau CONTIENT les 7 "
  "trompettes — voir I001). AVERTISSEMENTS (trompette = danger annoncé — Éz 33 !). "
  "« TIERS » : partiel = APPEL à se repentir (pas extermination !). JÉRICHO : modèle "
  "(7/7 — murs !). ÉGYPTE : modèle (plaies — « pas repentis » = Pharaon !). « Prières "
  "EXAUCÉES » (5e sceau → encensoir — voir I002 !). 2 TÉMOINS : 1914-1918 (voir F016 : "
  "1260 jours, tués, ressuscitent !). 7e : le ROYAUME (voir G009 !). DÉTAIL des "
  "proclamations : renvoyé au livre Révélation (méthode E007 — voir Limites)."
 ),
 accomplissement=[
  ("Exode (AT)", "Plaies : grêle, sang, ténèbres, sauterelles (types)"),
  ("Jéricho (AT)", "7 trompettes, 7 jours : les murs (type)"),
  ("~96 de n. è.", "Vision : les 7 trompettes"),
  ("1914-1918", "2 témoins : 1 260 jours, tués, montent (voir F016)"),
  ("1919 + de n. è.", "Proclamations : DÉTAIL renvoyé au livre Révélation"),
  ("7e (céleste)", "« EST DEVENU » : Royaume (voir G009)"),
  ("« Malheurs » (ouai)", "5e, 6e, 7e : malheur ×3"),
 ],
 hist=(
  "Exode (grêle, sang, ténèbres, sauterelles : 4 plaies reprises !). Jéricho (Jos 6 : "
  "7/7 — P066 !). 1914-1918 (voir F016). Abaddon (Jb 26:6, 28:22 ; Pr 15:11 : "
  "« destruction »). Euphrate (Cyrus : 539 — voir E)."
 ),
 geo=(
  "« Terre, mer, fleuves, ciel » (8:7-12 : QUATRE zones !). Euphrate (9:14 : le fleuve "
  "de Cyrus !). « Sodome, Égypte » (11:8 : « GRANDE ville » — renvoyée, voir Limites). "
  "« Arche » (11:19 : ciel OUVERT !)."
 ),
 sci=(
  "« TIERS » : partiel ×7 — miséricorde MATHÉMATIQUE (pas total !). « 5 mois » : "
  "SAISON des sauterelles. « Heure, jour, mois, année » (9:15 : PRÉCISION). « 7 000 » "
  "(11:13 : 7×1000). « 3,5 jours » (voir F016)."
 ),
 limites=(
  "Abaddon (le roi, 9:11) : identification renvoyée. Proclamations 1919+ : DÉTAIL "
  "renvoyé au livre Révélation (méthode E007). « Grande ville » (11:8) : renvoyée (I "
  "suite). Josué 6 : P066 = 6:26 seulement (trompettes : cross-ref)."
 ),
 tl=[("Exode", "Plaies : types"), ("Jéricho", "7/7 : murs"), ("96", "Vision : 7"), ("1914-18", "Témoins (F016)"),
     ("1919 +", "Proclamations : renvoi"), ("7e", "« EST DEVENU »")],
 src=[("Révélation à Jean — Insight (plan : sceau 7, trompettes, témoins)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013627"),
      ("Révélation 8 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/8"),
      ("Révélation 9 — Bible d'étude, notes (Abaddon, Euphrate)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/9"),
      ("Révélation 11 — Bible d'étude, notes (témoins, 7e, arche)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/11")],
 img="images/prophe_I003_trompettes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I004", titre="La femme contre le dragon — 1914, le tiers, le reste",
 ref="Révélation 12:1-17 ; Genèse 3:15 ; Daniel 12:1 ; 10:13 ; Psaume 2:9",
 statut="En cours (naissance + expulsion : 1914 ; « tête » : à venir)",
 cat="I", syst="Système 1914 (B009)",
 reg="Registre : Révélation — P857 (12:1-2), P858 (12:5), P859 (12:6), P860 (12:7-9), P861 (12:10-12), P862 (12:13-16), P863 (12:17) ; Genèse — P001, P570 (3:15) ; Daniel — P404 (12:1), P386 (10:12-14)",
 texte=[
  "« GRAND signe : FEMME — soleil, lune sous les pieds, 12 ÉTOILES — enceinte, elle "
  "CRIE dans les douleurs. » (Ré 12:1-2 — sèmeion mega ! krazô !)",
  "« Dragon FEU : 7 TÊTES, 10 CORNES, 7 diadèmes ; queue : TIERS des étoiles JETÉ ; "
  "prêt à DÉVORER. » (12:3-4 — pyrros ! kataphagein !)",
  "« FILS MÂLE — FER sur les nations — ENLEVÉ vers Dieu et son trône. » (12:5 — "
  "huios arsen ! Ps 2:9 ! hèrpasthè !)",
  "« Femme au DÉSERT : 1 260 jours, NOURRIE. » (12:6 — voir F016 !)",
  "« GUERRE dans le ciel : MICHEL contre le dragon — PRÉCIPITÉ : serpent ORIGINEL, "
  "Diable, Satan — sur la TERRE. » (12:7-9 — polemos ! eblèthè !)",
  "« SALUT, force, Royaume, autorité du Christ — l'ACCUSATEUR précipité — CIEL, "
  "réjouissez ! — MALHEUR terre et mer : GRANDE colère, PEU de temps. » "
  "(12:10-12 — sôtèria ! katègôr ! oligon !)",
  "« AIGLE : temps, temps, MOITIÉ — FLEUVE de la bouche — TERRE SECOURUT. » "
  "(12:14-16 — voir Da 7:25, 12:7 !)",
  "« Le dragon fait la GUERRE au RESTE : commandements + TÉMOIGNAGE de Jésus. » "
  "(12:17 — loipoi ! martyria !)",
 ],
 contexte=(
  "« GRAND signe » (sèmeion mega, 12:1 — voir I001 : SIGNES !). Genèse 3:15 "
  "(PROTO-évangile : « INIMITIÉ… TALON… TÊTE » — P001 ! — « femme », « postérité » !). "
  "« NAISSANCE » : 1914 — « fin des temps des Gentils » (voir B009 !). « Guerre CIEL » "
  "(12:7 : polemos !). « Court temps » (oligon kairon, 12:12 !). « Reste » (loipoi, "
  "12:17 : « TÉMOIGNAGE de Jésus » !). « Sable de la mer » (12:18 : → la bête du "
  "chapitre 13 — I suite !)."
 ),
 explication=(
  "« Femme » (gunè : organisation CÉLESTE de Jéhovah ! — « SOLEIL » : gloire ! — "
  "« LUNE » sous les pieds ! — « 12 » : peuple — tribus, apôtres !). « CRIE » (krazô : "
  "ôdin — voir H002 !). « Dragon FEU » (pyrros — voir H002 ! — « 7 TÊTES » : détail I "
  "suite — 13:1, 17:9-10 ! — « 10 CORNES » : puissance — Da 7, voir E002 ! — « 7 "
  "diadèmes » : couronnes USURPÉES !). « TIERS des étoiles » (12:4 : ANGES — Jb 38:7 ! "
  "— « jours de NOÉ » : fils de Dieu, Gn 6:1-4 — re-book CITÉ !). « DÉVORER » "
  "(kataphagein : PRÉDATEUR guettant !). « FILS MÂLE » (huios arsen : Ps 2:9 — « FER » "
  "— le Royaume-NÉ !). « ENLEVÉ » (hèrpasthè : RAVI — « vers Dieu… trône » !). « 1260 » "
  "(12:6 : voir F016 — 3,5 ans — « NOURRIE » !). « MICHEL » (MI-KA-EL : « QUI est comme "
  "Dieu » ? — Da 10:13, P386 : « un des PREMIERS princes » ! — Da 12:1, P404 : « DEBOUT » "
  "— voir H006 ! — Jude 9, 1Th 4:16 (« voix D'ARCHANGE ») : sans P — identification "
  "RENVOYÉE, voir Limites). « PRÉCIPITÉ » (eblèthè : JETÉ ! — « serpent ORIGINEL » : "
  "Gn 3 ! — « DIABLE » : calomniateur ! — « SATAN » : opposant ! — « égare la terre "
  "HABITÉE TOUT ENTIÈRE » !). « SALUT » (sôtèria, 12:10 ! — « autorité… CHRIST » !). "
  "« ACCUSATEUR » (katègôr : Jb 1-2 ! Za 3:1 ! — « jour et NUIT » !). « SANG » (12:11 : "
  "« parole de TÉMOIGNAGE » — « pas aimé… ÂMES » : jusqu'à la MORT — voir H010 !). "
  "« MALHEUR » (ouai : terre… MER !). « GRANDE colère » (thymon megan !). « PEU de "
  "temps » (oligon : 1914+ ! — 2P 3:8 !). « AIGLE » (12:14 : Ex 19:4, Dt 32:11, Is 40:31 "
  "— sans P ! — « TEMPS, temps, MOITIÉ » : Da 7:25, voir E005 ! Da 12:7, P407 !). "
  "« FLEUVE » (12:15 : potamos — sens renvoyé I suite, voir Limites). « Terre SECOURUT » "
  "(12:16 : boètheô !). « RESTE » (12:17 : loipoi — les oints ! — « COMMANDEMENTS » — "
  "« TÉMOIGNAGE de Jésus » : martyria — voir H004 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1914 — NAISSANCE du Royaume + expulsion "
  "(« fin des temps des Gentils » — voir B009). DEUX organisations opposées (femme "
  "céleste contre dragon démoniaque — re-book !). « Tiers » : les démons — jours de "
  "Noé (Gn 6 !). « Talon » (Gn 3:15 : Jésus MIS À MORT — Satan « écrasa » !). « Tête » : "
  "ÉCRASEMENT futur (Rm 16:20 — sans P !). « Court temps » : la colère depuis 1914. "
  "« Reste » : les oints persécutés (voir H010 !). « Témoignage » : martyria (voir "
  "H004 !). MICHEL : identification renvoyée aux publications (voir Limites)."
 ),
 accomplissement=[
  ("Éden", "Genèse 3:15 : inimitié, talon, tête (P001)"),
  ("Noé", "« Tiers » : fils de Dieu déchus (Gn 6)"),
  ("33 de n. è.", "TALON : Jésus mis à mort (talon écrasé)"),
  ("1914 de n. è.", "NAISSANCE + expulsion : Michel précipite (voir B009)"),
  ("1914 + de n. è.", "« Peu » : grande colère (terre et mer)"),
  ("En cours", "« Reste » : guerre — commandements, témoignage"),
  ("« Tête » (à venir)", "ÉCRASEMENT : Satan (Rm 16:20, sans P)"),
 ],
 hist=(
  "1914 (voir B009 : fin des temps des Gentils). Noé (Gn 6 : fils de Dieu — le tiers !). "
  "Job 1-2 (l'accusateur : « jour et nuit »). Zacharie 3:1 (Joshua accusé). « Sable » "
  "(12:18 : → chapitre 13 — I suite)."
 ),
 geo=(
  "« Ciel » (la GUERRE — 12:7). → « Terre… mer » (le MALHEUR — 12:12). « Désert » "
  "(la femme : 12:6, 14). « Sable » (le dragon : 12:18)."
 ),
 sci=(
  "« Tiers » : FRACTION des anges déchus (Noé). « 1260 » (voir F016). « Temps ×2,5 » "
  "(Da 7:25, 12:7 — voir E005, H006). « Peu » (oligon : relatif — 2P 3:8). MI-KA-EL : "
  "« QUI comme Dieu » — une QUESTION en nom."
 ),
 limites=(
  "Michel = Jésus : identification RENVOYÉE aux publications. « Fleuve » (12:15) : "
  "sens renvoyé (I suite). « 7 têtes » : détail renvoyé (ch. 13, 17 — I suite). "
  "Ex 19:4, Jude 9, 1Th 4:16, Rm 16:20 : mentions sans P (cross-refs)."
 ),
 tl=[("Éden", "3:15 : talon/tête"), ("Noé", "Tiers : déchus"), ("33", "TALON : mort"), ("1914", "NAISSANCE !"),
     ("1914 +", "« Peu » : colère"), ("En cours", "« Reste » : guerre"), ("À venir", "« Tête » : écrasé")],
 src=[("Questions des lecteurs (1914, Michel, talon, abîme)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1980932"),
      ("Révélation — livre : le tiers des étoiles (anges, Noé)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/1200270066/193/2"),
      ("Révélation 12 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/12"),
      ("Genèse 3 — Bible d'étude, notes (3:15, talon, tête)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/3")],
 img="images/prophe_I004_femme.jpg",
))
