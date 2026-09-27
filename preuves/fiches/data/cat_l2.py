#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE L, 2e partie (vague 15 — FIN DE LA CATEGORIE L et du projet fiches)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir ;
 - zero chevauchement textuel avec la categorie A (Damas : A010 ; Arabie : A011 ;
   Sidon : F002 ; Babylone-chute Is 13/Jr 50-51 : F003 ; Egypte Ez 29-32/Jr 46 : F004).
"""

CAT = dict(
    code="L",
    nom="Prophéties géographiques (2e partie)",
    vague="15",
    intro=(
        "Dernière vague du projet : trois fiches qui épuisent les reliquats "
        "géographiques sans jamais remordre sur la catégorie A. L008 : la Syrie — "
        "deux victoires d'Achab, trois flèches de Joas, puis l'exil « au-delà de "
        "Damas ». L009 : l'Égypte sous un angle neuf — les dieux jugés dès l'Exode, "
        "le Nil à sec, les maîtres durs, Hophra livré, puis l'autel et la triple "
        "bénédiction. L010 : Babylone sous l'angle d'Isaïe et des Psaumes — le "
        "guetteur qui crie la chute, le roi précipité du ciel dans la Tombe, la dame "
        "veuve en un jour, les harpes suspendues aux peupliers. Mêmes dix blocs, "
        "mêmes règles jusqu'au bout."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L008", titre="La Syrie — deux victoires, trois flèches, puis l'exil au-delà de Damas",
 ref="1 Rois 20:13-30 ; 2 Rois 13:14-25 ; Amos 5:1-27 ; 2 Rois 17:6",
 statut="Accomplie (P081, P093, P435)",
 cat="L", syst="Système guerres araméennes (Apheq ×2 → au-delà de Damas)",
 reg="Registre : Rois/Amos — P081 (1R 20:13-14, 28 : deux victoires sur la Syrie), P093 (2R 13:14-19 : trois victoires, pas plus), P435 (Am 5:1-27 : Samarie tombera, exil au-delà de Damas) ; rappels A010 (P115/P131/P280/P430), L001 (P451)",
 texte=[
  "« As-tu vu cette GRANDE FOULE ? Je vais la livrer en ta MAIN. » (1R 20:13 — P081 !)",
  "« Par QUI ? — Par les jeunes serviteurs des chefs. » (20:14 — la faiblesse !)",
  "« Les Syriens disent : Jéhovah est un dieu des MONTAGNES. » (20:28 — P081 : l'insulte !)",
  "« À APHEQ… le MUR tomba sur 27 000 hommes. » (20:30 — le mur !)",
  "« FLÈCHE de victoire… tu frapperas la Syrie à Apheq. » (2R 13:17 — P093 !)",
  "« Tu as frappé TROIS FOIS : tu ne battras la Syrie que TROIS FOIS. » (13:18-19 — compté !)",
  "« CHERCHEZ-MOI et vivez. » (Am 5:4 — P435 : l'offre !)",
  "« Je vous exilerai AU-DELÀ de Damas. » (5:27 — P435 : plus loin que l'ennemie !)",
 ],
 contexte=(
  "Ben-Hadad de Syrie, à la tête d'une coalition de trente-deux rois, assiège Samarie ; "
  "Achab accepte d'abord, refuse le pillage, puis, guidé par Dieu, surprend l'ennemi par "
  "une ruse de guerre (voir it-1 « Achab », 1200010141). Un siècle plus tard, Joas pleure "
  "sur Élisée mourant (« mon père, chars d'Israël ! » — 13:14, C8) et reçoit l'oracle des "
  "flèches. Un demi-siècle encore, et Amos, le bouvier de Teqoa prophétisant sous Jéroboam "
  "II, offre « cherchez-moi et vivez » (5:4) avant le verdict : l'exil « au-delà de Damas » "
  "(5:27). Trois actes : Dieu donne la victoire (1R 20), Dieu la mesure (2R 13), Dieu la "
  "retire (Am 5). Damas elle-même est jugée en A010 (P131/P280/P430) : cette fiche suit "
  "les ARMÉES, pas la ville."
 ),
 explication=(
  "« Jeunes serviteurs » (20:14) : l'élite par la petitesse — 232 jeunes gens (20:15 — C8) "
  "contre 32 rois : la signature divine. « Dieu des montagnes » (20:28 — P081) : les Syriens "
  "théorisent leur défaite — Jéhovah ne vaudrait qu'en altitude ; ils reviendront en plaine "
  "(Apheq) avec leurs chars — et perdront : la théologie païenne réfutée sur son propre "
  "terrain. « Le mur tomba » (20:30) : 27 000 écrasés — le texte ne dit pas comment (voir "
  "les limites). Flèches (13:15-19 — P093) : Joas frappe le sol trois fois et s'arrête — "
  "Élisée s'irrite : cinq ou six coups auraient valu l'extermination ; trois coups = trois "
  "victoires — la colère du roi mesure la victoire. « Au-delà de Damas » (Am 5:27 — P435) : "
  "plus loin que la capitale ennemie — le comble : Israël dépassera sa rivale sur la route "
  "de l'exil (2R 17:6 — P435 ; voir L001)."
 ),
 interpretation=(
  "Achab épargne Ben-Hadad (20:32-34 — C8) : « ta vie pour sa vie » (20:42 — C8) — la "
  "victoire donnée ne dispense pas d'obéir ; Achab mourra d'une flèche syrienne « tirée "
  "au hasard » (22:34 — C8 ; voir 1200010141 : Micaïah, déguisement, étang de Samarie). "
  "Hazaël, oint par Élie (1R 19:15 — C8, texte vérifié : « tu oindras Hazaël comme roi de "
  "Syrie »), devient le fléau : « Jéhovah m'a révélé que tu seras roi » (2R 8:13 — C8, "
  "texte vérifié ; les 40 chameaux de cadeaux — 8:9, C8). Joas reprend les villes "
  "(13:25 — P093) : trois fois, ni plus ni moins — le compte est bon. Amos : le fruit "
  "trop mûr (voir si-1 « Amos », 1101990091), « je ne le ferai pas revenir » six fois "
  "(Am 1:3—2:1 ; voir 2004844 §8), les maisons d'ivoire en décombres (voir 1101990091) — "
  "puis le torrent emporte « au-delà de Damas »."
 ),
 hist=(
  "Qarqar (853 — repère neutre) : Salmanasar III affronte 12 coalisés ; les annales "
  "nomment Ahabbu — 2 000 chars, 10 000 hommes selon le monolithe de Kurkh (repère) ; "
  "« la plupart des biblistes » y voient Achab — « VOIR cependant l'article SALMANASAR "
  "qui montre que cette identification est sujette à caution » (voir 1200010141 — "
  "prudence gardée en limites). Hazaël (~840 — repère) : la stèle de Tel Dan (« maison "
  "de David » — voir J005/J006) raconte ses victoires. Puis : Adad-Nirari III, "
  "Téglath-Phalazar III (Damas prise, 2R 16:9 — voir A010), Salmanasar V / Sargon (Samarie, "
  "740 — voir L001). Amos « avant quelques années seulement » (voir 1101990091) : "
  "l'exil sous les yeux de la génération."
 ),
 geo=(
  "Samarie assiégée (1R 20:1 — C8) : la colline encerclée par 32 rois. Apheq ×2 : la "
  "plaine — chars syriens chez eux, battus quand même (20:26-30 ; 2R 13:17 — P081, P093). "
  "Damas : le Barada, la Ghouta — « au-delà » = Halah, Habor, Mèdes (2R 17:6 — P435 ; "
  "voir L001). Ramoth de Galaad : Joram blessé par Hazaël (2R 8:28-29 — C8, texte vérifié). "
  "Qarqar : l'Oronte — la coalition arrête l'Assyrie… pour un temps. Teqoa (Am 1:1 — C8) : "
  "le bouvier du sud prophétisant au nord."
 ),
 sci=(
  "Doctrine des chars : engins de plaine, inutiles en montagne — « dieu des montagnes » "
  "(20:28) est une doctrine militaire déguisée en théologie : les Syriens choisissent "
  "Apheq (plaine) pour leurs chars — et y perdent : la plaine ne sauve pas. Poliorcétique : "
  "32 rois coalisés = logistique de siège (fourrage, eau, discorde) — la coalition "
  "s'effondre. Sismologie prudente : le mur d'Apheq (20:30) — effondrement ? Séisme ? "
  "Le texte tait la cause (voir les limites). Épigraphie : Kurkh (chiffres gonflés — "
  "l'orgueil assyrien se mesure), Tel Dan (le vaincu raconte autrement). Pomologie "
  "prophétique : le fruit trop mûr (Am 8 — C8, voir 1101990091) — la décomposition interne "
  "avant la chute."
 ),
 limites=(
  "Ahabbu = Achab : « sujette à caution » (voir 1200010141) — la fiche cite l'hypothèse "
  "majoritaire AVEC sa réserve. 853 : date neutre ; système araméen seul. Le mur d'Apheq "
  "(20:30) : cause non précisée — aucun scénario imposé. 1R 20:15, 23 ; 22:34, 42 ; 2R "
  "8:9, 13, 28-29 ; 1R 19:15 : C8 — aucun P ne les couvre (vérifié). Am 1—2 (P430) = A010, "
  "Am 2:1-5 (P431) = L004 : cette fiche ne traite QUE 1R 20, 2R 13 et Am 5."
 ),
 accomplissement=[("32 rois", "Samarie assiégée (C8)"), ("232 jeunes", "Première victoire (20:13-14)"), ("Apheq", "Dieu des plaines aussi (20:28-30)"),
     ("Qarqar 853 (neutre)", "Ahabbu ? (caution)"), ("3 flèches", "3 victoires, pas plus (13:18-19)"), ("Au-delà de Damas", "Le torrent (Am 5:27 → 2R 17:6)")],
 tl=[("32 rois", "Samarie assiégée (C8)"), ("232 jeunes", "Première victoire (20:13-14)"), ("Apheq", "Dieu des plaines aussi (20:28-30)"),
     ("Qarqar 853 (neutre)", "Ahabbu ? (caution)"), ("3 flèches", "3 victoires, pas plus (13:18-19)"), ("Au-delà de Damas", "Le torrent (Am 5:27 → 2R 17:6)")],
 src=[("Achab — Étude perspicace (32 rois, ruse, Qarqar, Micaïah)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010141"),
      ("Amos — Toute Écriture (au-delà de Damas, fruit mûr, n°30)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990091"),
      ("Le jugement sur les méchants (6 nations, ×6, 2004)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2004844"),
      ("1 Rois 20 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/11/20"),
      ("2 Rois 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/13"),
      ("Amos 5 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/30/5")],
 img="images/prophe_L008_syrie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L009", titre="L'Égypte — les dieux jugés, le Nil à sec, puis l'autel",
 ref="Exode 12:12, 13 ; Ésaïe 19:1-25 ; Jérémie 44:29, 30",
 statut="Accomplie (P042, P132, P270) / 1er accomplissement (P133)",
 cat="L", syst="Système maîtres (Assyrie → Babylone → Perse)",
 reg="Registre : Exode/Ésaïe/Jérémie — P042 (Ex 12:12-13 : jugement sur les dieux, le sang signe), P132 (Is 19:1-17 : maître dur, roi cruel), P133 (Is 19:18-25 : autel, route, triple bénédiction — 1er accomplissement : Ac 2:10 ; 18:24), P270 (Jr 44:29-30 : Hophra livré) ; rappel F004 (Éz 29-32, Jr 43/46 — autre angle)",
 texte=[
  "« J'exécuterai le JUGEMENT contre TOUS LES DIEUX d'Égypte, moi Jéhovah. » (Ex 12:12 — P042 !)",
  "« Jéhovah monté sur un NUAGE RAPIDE arrive en Égypte. » (Is 19:1 — P132 : le nuage !)",
  "« Les dieux SANS VALEUR trembleront… le courage FONDRA. » (19:1 — élilim : dieux-riens !)",
  "« Ville contre ville, ROYAUME contre ROYAUME. » (19:2 — la guerre civile !)",
  "« Je livrerai l'Égypte à un MAÎTRE DUR, un roi CRUEL. » (19:4 — le maître !)",
  "« Le fleuve se DESSÉCHERA et TARIRA… les canaux BAISSERONT. » (19:5-6 — le Nil à sec !)",
  "« Les princes de ZOÂN sont STUPIDES. » (19:11 — Zoân = Tanis !)",
  "« Cinq villes parleront la langue de CANAAN. » (19:18 — P133 : l'hébreu en Égypte !)",
  "« Un AUTEL pour Jéhovah… une COLONNE à sa frontière. » (19:19 — l'autel !)",
  "« Il la FRAPPERA et la GUÉRIRA. » (19:22 — frapper-guérir !)",
  "« BÉNIS soient mon peuple l'ÉGYPTE, l'œuvre de mes mains l'ASSYRIE, mon héritage ISRAËL ! » (19:25)",
  "« Je livrerai Pharaon HOPHRA… comme j'ai livré SIDQIYA. » (Jr 44:30 — P270 : comme Sidqiya !)",
 ],
 contexte=(
  "Trois dates, un pays. Nuit de la Pâque : la dixième plaie est annoncée comme un "
  "procès théologique — « jugement contre tous les dieux » (Ex 12:12 — P042), le sang "
  "signe sur les linteaux (12:13 — P042). VIIIe siècle : Ésaïe prononce la « déclaration "
  "contre l'Égypte » en deux volets — le jugement (19:1-15) puis « l'Égypte apprendra à "
  "connaître Jéhovah » (19:16-25 ; plan de l'édition d'étude, vérifié). Après 607 : les "
  "réfugiés judéens idolâtres en Égypte (voir it-1 « Égypte », 1200001265, avec Jr 44:2-25) "
  "reçoivent un signe : leur protecteur Hophra sera livré « comme Sidqiya » (44:29-30 — "
  "P270). Ézéchiel 29-32 et Jérémie 43/46 sont traités en F004 : cette fiche = Exode 12 + "
  "Ésaïe 19 + Jérémie 44:29-30."
 ),
 explication=(
  "« Dieux sans valeur » (élilim, 19:1) : jeu de mots — élohim (dieux) devenus riens ; "
  "ils « tremblent » pendant que le courage « fond » : dieux et fidèles liquéfiés ensemble. "
  "« Royaume contre royaume » (19:2) : « à cette époque plusieurs dynasties régnèrent en "
  "même temps » (voir 1200001265) — la guerre civile enducedans la lettre. Nil à sec "
  "(19:5-10) : « si le Nil ne montait pas du tout, catastrophe de premier ordre » (voir "
  "1200001265, citant 19:5-7) — pêcheurs, liniers, tisseurs, salariés : toute la chaîne "
  "économique en six versets. Zoân (Tanis) et Noph (Memphis — notes vérifiées) : le Delta "
  "et la tête du Delta — « stupides » et « trompés » (19:11-13). « Tête ou queue, pousse "
  "ou jonc » (19:15) : du haut en bas, du dedans au dehors — paralysie totale. Cinq "
  "villes/hébreu (19:18) : « la langue de Canaan (sans doute l'hébreu) fut parlée par ces "
  "réfugiés » (voir 1200001265). « Ville de la démolition » (19:18, TM) : nom énigme (voir "
  "les limites). Autel + colonne (19:19) : « signe et témoignage » (19:20) — un sauveur "
  "envoyé. Route (19:23) : la Via Maris sanctifiée — Égypte + Assyrie « serviront ensemble ». "
  "Triple titre (19:25) : « MON PEUPLE l'Égypte » — le titre d'Israël prêté à l'ennemie !"
 ),
 interpretation=(
  "Les plaies visent le panthéon : le Nil frappé (Hâpi), les ténèbres (Râ le dieu-soleil), "
  "les premiers-nés (Pharaon, fils de Râ) — voir 1200001265 pour le panthéon (triade "
  "Osiris-Isis-Horus, dieux cosmiques). Maîtres durs (19:4) : les conquérants — Assyrie "
  "(Esarhaddon 671, Assurbanipal — neutres), Babylone (voir F004), Perse (Cambyse 525 — "
  "neutre) : « conquêtes assyriennes et perses » (registre P132). Hophra = Apriès : "
  "« convaincu qu'aucun dieu ne pourrait le faire tomber » (Hérodote, cité en G1), révolte "
  "d'Amasis son officier, bataille perdue, livré à ses sujets (voir 1101965112, Jr 44:30 — "
  "P270). 1er accomplissement (P133) : des Égyptiens à la Pentecôte (Ac 2:10 — registre) "
  "et Apollos d'Alexandrie (Ac 18:24 — registre) — l'autel devenu Église. Temple juif "
  "d'Éléphantine (Ve s., papyrus — repère) et d'Onias au Léontopolis (IIe s., selon Josèphe — "
  "repère) : des autels pour Jéhovah « au milieu de l'Égypte » (19:19)."
 ),
 hist=(
  "Exode : « jugement contre tous les dieux » (12:12 — P042) exécuté la nuit même (12:29 — "
  "C8). 671/663 (neutres) : l'Assyrie prend Memphis puis Thèbes (voir L002 : No-Amôn). 525 "
  "(neutre) : Cambyse — l'Égypte satrapie. Hophra (589-570 — neutre) : « plusieurs années "
  "après [607], les châtiments commencèrent à tomber sur lui » (voir G1) — déposé, livré, "
  "étranglé selon Hérodote (repère). Éléphantine : garnison juive + temple (papyrus "
  "d'Éléphantine — repère archéologique). Onias IV : temple au Léontopolis (Josèphe — repère). "
  "Pentecôte : « Égyptiens » dans la foule (Ac 2:10 — P133) ; Apollos « originaire "
  "d'Alexandrie, éloquent, versé dans les Écritures » (Ac 18:24 — P133)."
 ),
 geo=(
  "Le Nil : 7 branches, le Delta, la crue (nilomètres !) — « mer » (19:5 : le fleuve-mer). "
  "Zoân/Tanis (Delta oriental) : capitale des rois du nord. Noph/Memphis : verrou du Delta. "
  "Thèbes/Nô : le sud (voir L002, F004). Tahpanhès : les réfugiés (Jr 43 — voir F004). "
  "« Ville de la démolition » (19:18) : Héliopolis ? (voir les limites). Éléphantine : "
  "l'île-frontière du sud — Juifs en garnison. Alexandrie : Apollos — la diaspora savante. "
  "La route (19:23) : Égypte → Assyrie — 1 500 km de Via Maris et de Croissant réconciliés."
 ),
 sci=(
  "Hydrologie : crue zéro = famine (voir 1200001265) — le Nilomètre de l'île de Rodah "
  "mesurait la vie et la mort ; « fleuves puants » (19:6) : eutrophisation des bras "
  "stagnants. Économie du lin (19:9) : le byssus égyptien — « lin peigné », « coton blanc "
  "(ou étoffes blanches — note) » : l'industrie textile du Delta, humiliée. Halieutique "
  "(19:8) : hameçons, filets — la pêche fluviale tarie. Médecine de l'image (19:14) : "
  "« ivre qui titube dans son vomissement » — la confusion en symptôme. Linguistique "
  "(19:18) : cinq villes à l'hébreu — îlots linguistiques datables. Astronomie du "
  "panthéon : Râ, lune, ciel (voir 1200001265) — les dieux cosmiques jugés par les "
  "ténèbres."
 ),
 limites=(
  "« Ville de la démolition » (19:18, TM) : les manuscrits varient (« ville du soleil » "
  "selon d'autres leçons) — non tranché. Éléphantine/Onias : repères, pas versets — "
  "l'accomplissement versé au registre est Ac 2:10 ; 18:24 (P133, « 1er accomplissement »). "
  "La route et la triple bénédiction (19:23-25) : avenir du texte — AUCUNE date (règle "
  "d'or). Éz 29-32 + Jr 43/46 = F004 : doublon refusé — cette fiche = Ex 12 + Is 19 + Jr "
  "44:29-30. Dates 671/663/525/589-570 : neutres, système des maîtres seul."
 ),
 accomplissement=[("Pâque", "Jugement sur les dieux (Ex 12:12)"), ("Nuage rapide", "Dieux-riens (Is 19:1)"), ("Nil à sec", "Chaîne brisée (19:5-10)"),
     ("Maîtres durs", "Assyrie → Perse (19:4)"), ("Hophra", "Livré comme Sidqiya (Jr 44:30)"), ("Autel", "Égypte mon peuple (19:19, 25)")],
 tl=[("Pâque", "Jugement sur les dieux (Ex 12:12)"), ("Nuage rapide", "Dieux-riens (Is 19:1)"), ("Nil à sec", "Chaîne brisée (19:5-10)"),
     ("Maîtres durs", "Assyrie → Perse (19:4)"), ("Hophra", "Livré comme Sidqiya (Jr 44:30)"), ("Autel", "Égypte mon peuple (19:19, 25)")],
 src=[("Égypte, Égyptien — Étude perspicace (Nil, dieux, dynasties, langue)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001265"),
      ("Prophéties — tableau (Hophra/Apriès, Amasis, Hérodote)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Exode 12 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/12"),
      ("Ésaïe 19 — Bible d'étude, texte intégral vérifié", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/19"),
      ("Jérémie 44 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/44")],
 img="images/prophe_L009_egypte.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L010", titre="Babylone — le guetteur, le roi précipité, la dame veuve",
 ref="Ésaïe 21:1-10 ; Ésaïe 14:4-23 ; Ésaïe 47:1-15 ; Psaume 137:1-8",
 statut="Accomplie (P135, P128, P164, P559)",
 cat="L", syst="Système chutes (539, 11/12 octobre)",
 reg="Registre : Ésaïe/Psaumes — P135 (Is 21:1-10 : Babylone tombée, Bel brisé), P128 (Is 14:4-23 : roi précipité), P164 (Is 47:1-15 : veuvage en un jour, astrologues), P559 (Ps 137:1-9 : fleuves de Babylone) ; rappels P162 (cité en B), P374/P375 (cités en E), F003 (Is 13/44-45, Jr 50-51 — autre angle)",
 texte=[
  "« Déclaration contre le DÉSERT DE LA MER. » (Is 21:1 — P135 : la Babylonie !)",
  "« MONTE, ÉLAM ! ASSIÈGE, MÉDIE ! » (21:2 — l'ordre !)",
  "« MANGEZ, BUVEZ !… Versez de l'HUILE sur le bouclier ! » (21:5 — le banquet !)",
  "« Poste un GUETTEUR… Sur la TOUR DE GARDE, jour et nuits. » (21:6, 8 — le guetteur !)",
  "« ELLE EST TOMBÉE ! BABYLONE EST TOMBÉE ! » (21:9 — ×2 : certain !)",
  "« Toutes les STATUES de ses dieux à terre, FRACASSÉES ! » (21:9 — Bel brisé !)",
  "« Récite ce PROVERBE MOQUEUR contre le roi. » (Is 14:4 — P128 : mashal !)",
  "« Te voilà tombé du ciel, ASTRE BRILLANT, fils de l'AURORE ! » (14:12 — hélel !)",
  "« Je me rendrai SEMBLABLE au Très-Haut… On te fera DESCENDRE dans la Tombe. » (14:14-15)",
  "« J'effacerai de Babylone NOM et reste, LIGNÉE et descendance. » (14:22 — effacé !)",
  "« Je ne deviendrai pas VEUVE… En UN SEUL JOUR : perte d'enfants et VEUVAGE. » (Is 47:8-9)",
  "« Qu'ils te SAUVENT, ceux qui DIVISENT LE CIEL !… Ils sont comme du CHAUME ! » (47:13-14)",
  "« Près des FLEUVES de Babylone, nous avons PLEURÉ. » (Ps 137:1 — P559 !)",
  "« Comment chanter le chant de Jéhovah sur un SOL ÉTRANGER ? » (137:4 — comment ?)",
 ],
 contexte=(
  "Quatre regards, une ville. Le guetteur (Is 21) : Él? Non — Ésaïe, deux siècles d'avance, "
  "poste la vigie et entend le cri. Le moqueur (Is 14) : un « proverbe moqueur » (mashal — "
  "texte vérifié) chanté le jour du soulagement (14:3 — C8). Le juge (Is 47) : la dame "
  "assise « confiante » (47:8 — texte vérifié) reçoit l'assignation. L'exilé (Ps 137) : le "
  "seul psaume de Babylone — harpes aux peupliers (137:2, note : saules — vérifié). "
  "Isaïe 13 et Jérémie 50-51 sont traités en F003, Isaïe 44-45 (Cyrus) en J001 : cette "
  "fiche = Is 14 + Is 21 + Is 47 + Ps 137. Bel (P135 : « Bel est brisé ») renvoie à P162 "
  "(Is 46:1-2, cité en B) ; le banquet à P374/P375 (Dn 5, cités en E)."
 ),
 explication=(
  "« Désert de la mer » (21:1) : « désigne apparemment la Babylonie antique » (note vérifiée) — "
  "la plaine marécageuse du sud. « Monte, Élam ! Assiège, Médie ! » (21:2) : Perse + Mèdes = "
  "Cyrus (voir J001) — l'ordre de marche deux siècles avant. Le prophète en convulsions "
  "(21:3-4 : « comme une femme qui accouche… le crépuscule me fait trembler » — vérifié) : "
  "le voyant SOUFFRE sa vision. Banquet (21:5 : « mangez, buvez ! » — vérifié) : Daniel 5 "
  "(voir P374/P375, E) — on festoie pendant que l'ennemi marche. Huile sur le bouclier (21:5) : "
  "le cuir se graisse avant le combat — trop tard. Guetteur (21:6-8) : « sur la tour de "
  "garde… constamment » (vérifié) — puis le cri redoublé (21:9) : « tombée » ×2 = certitude "
  "grammaticale, repris en Révélation 14:8 (voir I). « Astre brillant, fils de l'aurore » "
  "(14:12, hélel — vérifié) : Vénus du matin — le roi se croyait l'étoile du jour ; "
  "« montagne de réunion… nord » (14:13 — vérifié) : le panthéon fantasmé. Cinq « je » "
  "(14:13-14 : monterai, élèverai, m'assiérai, monterai, ressemblerai) contre un « on te fera "
  "descendre » (14:15) : l'orgueil compte, Dieu conclut. « Rejeton détesté… cadavre piétiné » "
  "(14:19 — vérifié) : pas de tombe royale (14:18, 20 — vérifié : « tu as détruit ton pays, "
  "tué ton peuple »). Veuve (47:8-9 : « il n'y a que moi… je ne deviendrai pas veuve… en un "
  "seul jour » — vérifié) : « devenir veuve et perdre ses enfants : les pires calamités pour "
  "une femme de l'Orient » (voir ip-2, 1102001028). « Divisent le ciel » (47:13, note — "
  "vérifié) : « partager les cieux en zones afin de tirer les horoscopes » (voir 1102001028). "
  "Chaume (47:14 — vérifié) : les conseillers brûlent les premiers. Harpes aux peupliers "
  "(137:2 — vérifié) : la musique en deuil ; « main droite » (137:5 — vérifié) : la main du "
  "musicien — oublier Jérusalem = perdre son art."
 ),
 interpretation=(
  "539 (11/12 octobre — repère des publications) : Cyrus entre — « même si Babylone montait "
  "aux cieux… les pillards viendront » (voir 1102001028, avec Jr 51:53 — F003). Bel brisé "
  "(21:9 : « statues à terre, fracassées » — P135 ; Is 46:1-2 — P162, cité en B : « Bel plie, "
  "Nebo s'affaisse »). Le roi : Belshazzar tué la nuit du banquet (Dn 5:30 — P135/P128/P164, "
  "registre ; voir P374/P375, E) — « privé de tombe… cadavre piétiné » (14:19). Les "
  "astrologues : « des siècles d'observations » (voir 1102001028) pour ne rien voir venir — "
  "« incapables de se sauver eux-mêmes » (47:14 — vérifié). Édom au pied du mur (137:7 : "
  "« démolissez-la ! » — vérifié ; voir L003). « Fille de Babylone… dévastée » (137:8 — "
  "vérifié) : l'imprécation confie la rétribution (voir les limites ; la justice : I009/I010). "
  "Et la chute « n'était que le prélude » : Révélation reprend 47:8-9 contre Babylone la "
  "Grande (voir 1102001028 §28 ; I007)."
 ),
 hist=(
  "Cyrus (voir J001 : P157/P161 ; P161 : « sans combat ») : 539, diversion de l'Euphrate "
  "(voir F003 pour les eaux), entrée par le lit — la Chronique de Nabonide (repère) "
  "confirme une prise rapide. Nabonide à Téma, Belshazzar régent (repères) : le pouvoir "
  "coupé en deux, la nuit coupée en deux (Dn 5 — voir E). Enuma Anu Enlil : ~70 tablettes "
  "d'omens célestes (repère) — le ciel divisé, l'avenir manqué. Exil 607-537 (P559, "
  "registre — voir B002) : 70 ans entre les harpes suspendues (137:2) et les harpes reprises "
  "(Ps 126:1 — C8 : « nous étions comme des rêveurs »). Cylindre de Cyrus (repère) : le "
  "retour autorisé (voir J001)."
 ),
 geo=(
  "Basse Mésopotamie : le « désert de la mer » (21:1) — marais du sud, Euphrate lent. "
  "Élam (est, Suse) + Médie (nord-est, Ecbatane) : les deux mâchoires sur Babylone. "
  "« Fleuves de Babylone » (137:1) : l'Euphrate et ses canaux (nahr) — les exilés au bord "
  "des eaux courantes. Peupliers (137:2) : Populus euphratica — le peuplier DE l'Euphrate "
  "(voir science). Liban (14:8 : « genévriers et cèdres… aucun bûcheron » — vérifié) : la "
  "forêt respire quand l'empire meurt. Douma/Séïr (21:11-12 — vérifié : « garde, où en est "
  "la nuit ? ») : P136 — versé aux reliquats (voir limites). Kédar (21:16-17 — vérifié : "
  "« un an, comme un salarié ») : voir A011."
 ),
 sci=(
  "Boucliers (21:5) : cuir sur bois — l'huile assouplit et imperméabilise : maintenance "
  "militaire en un verset. Vigie (21:6-8) : tour, jour et nuits, identification des "
  "attelages (21:7 : chevaux, ânes, chameaux — vérifié) — le renseignement visuel antique. "
  "Astronomie (47:13) : « des siècles d'observations » (voir 1102001028) — calendriers, "
  "éclipses calculées — et prédiction nulle : la science du ciel ne voit pas le jugement. "
  "Dendrologie (137:2 ; 14:8) : Populus euphratica (ripisylve), genévriers et cèdres du "
  "Liban — coupes impériales (bois de marine et de palais) puis répit. Musicologie : "
  "kinnôr suspendu (137:2), « instruments à cordes » descendus dans la Tombe (14:11 — "
  "vérifié), main droite (137:5) — l'organe du musicien. Zoologie (14:23 — P128 : "
  "« hérisson et mares d'eau ») : qippōd, comme en Is 34:11 (voir L003)."
 ),
 limites=(
  "Is 14:12 (hélel, « astre brillant ») : le chant vise « le roi de Babylone » (14:4 — "
  "P128) — toute application seconde sort du cadre de cette fiche. Ps 137:9 : non cité — "
  "langage imprécatoire du deuil ; la rétribution appartient à Dieu (voir I009/I010). "
  "Is 13 + Jr 50-51 = F003, Is 44-45 = J001, Dn 5 = E (P374/P375) : cette fiche = Is 14 + "
  "Is 21 + Is 47 + Ps 137 — doublon refusé. P136 (Douma, 21:11-12) : reliquat (voir le "
  "rapport de clôture). Is 14:23 (hérisson, mares) : dans la plage P128 (14:4-23). 539 = 11/12 octobre (publications) ; autres dates : repères signalés."
 ),
 accomplissement=[("Désert de la mer", "Élam + Médie appelés (21:2)"), ("Banquet", "Mangez, buvez ! (21:5 → Dn 5)"), ("Guetteur", "Tombée ×2 (21:9)"),
     ("Astre", "Ciel → Tombe (14:12-15)"), ("Veuve", "En un seul jour (47:9)"), ("Harpes", "Suspendues… puis reprises (Ps 137:2)")],
 tl=[("Désert de la mer", "Élam + Médie appelés (21:2)"), ("Banquet", "Mangez, buvez ! (21:5 → Dn 5)"), ("Guetteur", "Tombée ×2 (21:9)"),
     ("Astre", "Ciel → Tombe (14:12-15)"), ("Veuve", "En un seul jour (47:9)"), ("Harpes", "Suspendues… puis reprises (Ps 137:2)")],
 src=[("Fausse religion : fin retentissante (Is 47, ip-2)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102001028"),
      ("Ésaïe 14 — Bible d'étude, texte vérifié (astre, Tombe)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/14"),
      ("Ésaïe 21 — Bible d'étude, texte intégral vérifié", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/21"),
      ("Ésaïe 47 — Bible d'étude, texte intégral vérifié", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/47"),
      ("Psaume 137 — Bible d'étude, texte intégral vérifié", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/137")],
 img="images/prophe_L010_babylone.jpg",
))
