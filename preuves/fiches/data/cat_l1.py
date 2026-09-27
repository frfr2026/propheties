#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE K-L (vague de transition 14) — FIN DE LA SCIENCE + GEOGRAPHIE
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="K–L",
    nom="La Bible et la science (2e partie) · Prophéties géographiques",
    vague="14",
    intro=(
        "Cette vague de transition ferme la catégorie K et ouvre la catégorie L, la "
        "dernière du projet. Côté K, deux fiches : Pierre et le jour de Jéhovah — le "
        "monde d'alors noyé, les cieux et la terre réservés au feu, les éléments "
        "dissous ; puis les sabbats de la terre — la jachère commandée, violée, et "
        "payée par soixante-dix ans de désolation. Côté L, sept prophéties "
        "géographiques : Samarie réduite en tas de ruines, Ninive ouverte aux portes "
        "des fleuves, Édom le nid d'aigle précipité, Moab ruiné en trois ans, Tyr "
        "oubliée soixante-dix ans, la Philistie rasée ville par ville, Ammon livrée "
        "aux fils de l'Orient. Mêmes dix blocs, mêmes règles : un seul système "
        "chronologique par fiche, aucune date pour l'avenir, et des limites écrites "
        "noir sur blanc."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K007", titre="Pierre et le jour — le monde noyé, les éléments dissous",
 ref="2 Pierre 3:5-10 ; 2 Pierre 3:13 (P786, voir G) ; Matthieu 24:39",
 statut="Accomplie (P783) / À venir (P784, P785)",
 cat="K", syst="Système mondes (alors → maintenant → nouveaux)",
 reg="Registre : Pierre — P783 (2P 3:5-6 : monde d'alors détruit par le déluge), P784 (2P 3:7 : cieux et terre réservés au feu), P785 (2P 3:10 : jour comme un voleur, cieux passés) ; rappel P786 (2P 3:13, cité en G)",
 texte=[
  "« Ils IGNORENT VOLONTAIREMENT : des cieux… une terre hors de l'eau et dans l'eau. » (3:5)",
  "« Le MONDE D'ALORS subit la destruction, INONDÉ par l'eau. » (3:6 — noyé !)",
  "« Les cieux et la terre de MAINTENANT sont amassés pour le FEU. » (3:7 — réservés !)",
  "« Le jour de Jéhovah viendra comme un VOLEUR. » (3:10 — soudain !)",
  "« Les cieux passeront avec FRACAS… les ÉLÉMENTS dissous… la terre DÉCOUVERTE. » (3:10)",
  "« De NOUVEAUX cieux et une NOUVELLE terre, où la JUSTICE habitera. » (3:13 — P786 !)",
 ],
 contexte=(
  "Des moqueurs ricanent : « Où est sa présence promise ? Tout demeure comme depuis le "
  "commencement » (3:4 — C8). Pierre répond en trois mondes : le monde d'alors (noyé), "
  "le monde de maintenant (réservé au feu), les nouveaux cieux et la nouvelle terre "
  "(promis). L'argument est historique : ceux qui nient le jugement à venir « ignorent "
  "volontairement » le jugement passé — le déluge (Gn 7:11-12, 21-23 — P783), que Jésus "
  "lui-même a invoqué : « ils ne se rendirent compte de rien, jusqu'à ce que le déluge "
  "vienne » (Mt 24:39 — P783). « Mille ans comme un jour » (3:8 — C8) : la patience, pas "
  "la lenteur (3:9 — C8)."
 ),
 explication=(
  "« Cieux » au figuré : les puissances dirigeantes placées au-dessus des populations "
  "(voir 2010521 §3, avec Is 14:13-14) — les « cieux qui passeront » sont les autorités "
  "humaines dominant l'actuelle société impie, anéanties « dans un sifflement », donc "
  "très rapidement. « Terre » : la société humaine éloignée de Dieu (voir §4). "
  "« Éléments » (stoicheia) : les rudiments, les fondamentaux — mentalités, objectifs, "
  "manières d'agir — dont « l'esprit du monde » qui opère dans les fils de la "
  "désobéissance (voir §5, avec 1Co 2:12 ; Ép 2:1-3 — C8). « Découverte » : la terre et "
  "ses œuvres « trouvées » par le feu, sans échappatoire. Nouveaux cieux : le Royaume, "
  "établi en 1914 (voir 2010521 §10, et F017) ; nouvelle terre : la société juste "
  "(voir G)."
 ),
 interpretation=(
  "Le déluge est le précédent : « par la même parole » (3:7) — la parole qui noya "
  "brûlera. Différence de rythme : le déluge détruisit d'un coup, la fin viendra par "
  "étapes, au cours de la grande tribulation — d'abord Babylone détruite par les "
  "dirigeants (voir I007), puis Har-Maguédôn (voir I009, I010) — selon l'article (voir "
  "2010521 §4). Les légendes du déluge, sur tous les continents, gardent la mémoire du "
  "précédent (voir 1992041) : Mésopotamie (tablette XI de Gilgamesh), Grèce (Deucalion), "
  "Inde (Manou), Amériques — même trame : eaux, arche, survivants. « Puisque tout doit "
  "se dissoudre, quel genre d'hommes devez-vous être ? » (3:11 — C8) : la physique "
  "débouche sur la conduite."
 ),
 hist=(
  "Déluge : récits parallèles dans des dizaines de cultures (voir 1992041) ; en "
  "Mésopotamie, couches d'inondation à Our, Kish, Shuruppak (Woolley et autres — "
  "repères archéologiques, voir les limites). Néphilim : « géants violents » des "
  "légendes et de Genèse 6:1-4 (voir 1992041, avec 2P 2:4-5 — C8). Date du déluge : le "
  "système biblique interne le place en 2370 (repère des publications — voir F pour les "
  "conversions). Jésus (Mt 24:39 — P783) traite le déluge en fait daté : « les jours de "
  "Noé »."
 ),
 geo=(
  "« Hors de l'eau et dans l'eau » (3:5) : la terre émergée (Gn 1:9-10 — C8) puis "
  "submergée (Gn 7:19-20 — C8 : quinze coudées au-dessus des montagnes). « Monde » "
  "(kosmos) : l'ordre habité, pas la planète — la terre demeure (voir K003 : Ec 1:4). "
  "Ararat : l'échouage (Gn 8:4 — C8). Les légendes : du Tigre au Mexique — une mémoire "
  "mondiale d'eaux mondiales."
 ),
 sci=(
  "Sédimentologie : fossiles marins en montagne, couches sédimentaires continentales — "
  "les faits que toutes les écoles datent, et que le récit rapporte à l'année du "
  "déluge (voir les limites : pas de géologie alternative ici). Philologie : stoicheia "
  "= lettres, rudiments, principes — l'article retient les fondamentaux moraux (§5), pas "
  "les atomes : Pierre ne fait pas de la physique des particules. Chronologie : 3:8 "
  "(mille ans = un jour) parle de patience divine, pas d'équivalence calculable — aucun "
  "« jour-millénium » n'en est tiré (voir les limites). Pyrotechnie : « dissous… fondent » "
  "(3:10, 12) — le feu comme fin de l'ordre, pendant de l'eau du commencement."
 ),
 limites=(
  "Cette fiche ne propose aucune géologie du déluge : couches, fossiles et datations "
  "sont des faits constatés, leur interprétation chronologique appartient aux systèmes "
  "(voir F). 3:8 n'est pas une formule (mille ans ≠ un jour calculable). « Cieux » = "
  "autorités (voir §3) : le ciel physique ne passe pas (voir K002 : les lois "
  "demeurent ; K003 : la terre demeure). P786 (3:13, nouveaux cieux) est cité en G : "
  "cette fiche s'arrête au feu (3:10). Aucune date pour le jour — « comme un voleur » "
  "l'interdit."
 ),
 accomplissement=[("Alors", "Monde inondé (3:6)"), ("Mémoire", "Légendes mondiales"), ("Maintenant", "Réservés au feu (3:7)"),
     ("Patience", "Mille ans = un jour (3:8)"), ("Voleur", "Fracas, dissous (3:10)"), ("Promesse", "Justice habitera (3:13)")],
 tl=[("Alors", "Monde inondé (3:6)"), ("Mémoire", "Légendes mondiales"), ("Maintenant", "Réservés au feu (3:7)"),
     ("Patience", "Mille ans = un jour (3:8)"), ("Voleur", "Fracas, dissous (3:10)"), ("Promesse", "Justice habitera (3:13)")],
 src=[("Ce que le jour de Jéhovah révélera (cieux, éléments, 2010)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2010521"),
      ("Le déluge à travers les légendes du monde (1992)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1992041"),
      ("2 Pierre 3 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/61/3"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_K007_pierre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K008", titre="Les sabbats de la terre — la jachère violée, payée 70 ans",
 ref="Lévitique 26:34, 35, 43 ; 2 Chroniques 36:20, 21 ; Jérémie 25:11 ; Daniel 9:2",
 statut="Accomplie (P049)",
 cat="K", syst="Système sabbatique (7 / 49 / 70)",
 reg="Registre : Lévitique — P049 (Lv 26:34-35, 43 : la terre jouira de ses sabbats pendant la désolation)",
 texte=[
  "« Alors le pays JOUIRA de ses sabbats, pendant tous ces jours de DÉSOLATION. » (26:34)",
  "« Il se REPOSERA pour RÉCUPÉRER ses sabbats. » (26:34 — récupérer !)",
  "« Ce repos qu'il n'avait pu avoir lors de vos sabbats, quand vous y habitiez. » (26:35)",
  "« En leur absence, il jouira de ses sabbats et sera dans la DÉSOLATION. » (26:43)",
  "« Jusqu'à ce que le pays se soit ACQUITTÉ de ses sabbats : 70 ANS. » (2Ch 36:21 — P049 !)",
 ],
 contexte=(
  "Lévitique 26 est le contrat : bénédictions (26:3-13 — pluies, récoltes, paix), puis "
  "sanctions graduées (26:14-39), puis la clause agraire (26:34-35, 43). La loi sabbatique "
  "imposait, chaque septième année : ni cultiver, ni ensemencer, ni tailler, ni moissonner "
  "— la pousse libre restant à tous, propriétaire, esclaves, salariés, étrangers (voir "
  "it-1 « Sabbatique », 1200003780). Il fallait la foi : Dieu promettait une récolte de "
  "sixième année couvrant jusqu'à la huitième (voir 1200003780, avec Lv 25:21 — C8). "
  "Compteur théorique depuis l'entrée (1473 — repère) : 121 sabbatiques + 17 jubilés "
  "avant l'Exil (voir 1200003780). Observance : partielle."
 ),
 explication=(
  "« Jouira » : la terre est sujet — elle JOUIT, se REPOSE, RÉCUPÈRE : le sol est un "
  "ayant droit, pas un outil. « Acquitté » (2Ch 36:21) : vocabulaire de dette — les "
  "sabbats volés sont remboursés en désolation. 70 ans : « les Écritures ne stipulent "
  "nulle part que les Juifs avaient manqué précisément 70 sabbatiques ; mais Jéhovah "
  "imposa 70 années pour compenser toutes les années non observées » (voir 1200003780). "
  "Le non-respect des lois sabbatiques « contribua dans une large mesure à "
  "l'effondrement de la nation » (voir it-1 « Sabbat », 1200003778). Jérémie avait chiffré "
  "(25:11 — P049 ; voir B002), Daniel lut le chiffre (9:2 — P049 ; voir F), "
  "Chroniques constata le paiement (36:20-21 — P049)."
 ),
 interpretation=(
  "La terre a des droits : le repos septennal protège le sol, les pauvres (glanage "
  "libre) et la foi (dépendance annuelle). Violé, il se paie : 70 ans de jachère forcée "
  "pendant l'exil — « le pays se repose » pendant que le peuple est à Babylone. Le "
  "système sabbatique entier (jours et années) prend fin au sacrifice de Christ (voir "
  "1200003778, avec Ac 15:28-29 — C8) : les chrétiens goûtent un « repos de sabbat » de "
  "foi (voir 1200003778, avec Hé 4 — C8), pas un calendrier agraire. Paul : le repos de "
  "Dieu « dure des milliers d'années » (voir 1200003778). La leçon demeure : on ne vole "
  "pas la terre sans facture."
 ),
 hist=(
  "2 Chroniques 36:20-21 (P049) : déportation, désolation de 70 ans, « afin que s'accomplisse "
  "la parole » — le texte lui-même fait le lien avec Lévitique 26. Jérémie 25:11 (P049 ; "
  "voir B002) : « soixante-dix ans » annoncés ; Daniel 9:2 (P049 ; voir F) : Daniel "
  "« discerna par les livres » le nombre. Retour : Cyrus (Esd 1 — C8 ; voir J001) met fin "
  "à la jachère. Jubilés : 17 théoriques (voir 1200003780) — remise des terres et des "
  "dettes tous les 49/50 ans (Lv 25 — C8), pendant social du repos du sol."
 ),
 geo=(
  "Le pays : collines de Juda, plaines côtières, vallée du Jourdain — tout le terroir "
  "en jachère simultanée, du Dan à Beershéba. Babylone : le lieu de l'exil pendant que "
  "le sol se repose — peuple déplacé, terre libérée. « Vos ennemis venus l'habiter en "
  "seront stupéfaits » (26:32 — C8) : la désolation visible depuis la route. Retour : "
  "les mêmes champs, reposés, rendus aux mêmes familles (jubilé — Lv 25 — C8)."
 ),
 sci=(
  "Agronomie : la jachère régénère — azote (légumineuses spontanées), matière organique, "
  "structure, rupture des cycles de parasites et d'adventices : Lv 26 commande ce que "
  "la science mesure. Dette écologique : 70 ans de repos forcé pour des siècles de "
  "surexploitation — le principe pollueur-payeur avant la lettre, appliqué au sol. "
  "Stockage : la récolte triple de sixième année (voir 1200003780) suppose greniers et "
  "conservation sur deux ans — logistique de la foi. Rythme 7 : travail/repos inscrit "
  "dans la semaine (Ex 20 — C8), l'année (Lv 25 — C8) et le siècle (jubilé)."
 ),
 limites=(
  "70 ≠ 70 sabbatiques manquées comptées : l'article le dit noir sur blanc — compensation "
  "globale, pas comptabilité (voir 1200003780). 1473 (entrée) : repère des publications, "
  "système sabbatique seul (voir F pour les conversions). Cette fiche ne fait pas de "
  "Lévitique 26 un traité d'agronomie moderne : la jachère est commandée, ses mécanismes "
  "décrits par la science, sans concordisme forcé. P048 (malédictions) et P050 (retour) "
  "appartiennent à d'autres dossiers (voir le rapport de clôture)."
 ),
 accomplissement=[("1473 (repère)", "Entrée : compteur à zéro"), ("7e année", "Ni semer ni tailler"), ("6e année", "Récolte triple"),
     ("Partielle", "Observance violée"), ("Exil", "70 ans : la terre se repose"), ("Cyrus", "Fin de la jachère (J001)")],
 tl=[("1473 (repère)", "Entrée : compteur à zéro"), ("7e année", "Ni semer ni tailler"), ("6e année", "Récolte triple"),
     ("Partielle", "Observance violée"), ("Exil", "70 ans : la terre se repose"), ("Cyrus", "Fin de la jachère (J001)")],
 src=[("Sabbatique (Année) — Étude perspicace (121+17, triple récolte)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003780"),
      ("Sabbat — Étude perspicace (effondrement, 70 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003778"),
      ("Lévitique 26 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/3/26"),
      ("2 Chroniques 36 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/36")],
 img="images/prophe_K008_sabbats.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L001", titre="Samarie — le tas de ruines et la marche vers Jérusalem",
 ref="Michée 1:2-9 ; Michée 1:10-16 ; 2 Rois 17:5, 6 ; 2 Rois 25:1-11",
 statut="Accomplie (P451, P452)",
 cat="L", syst="Système sièges (740 Samarie → 607/587 Jérusalem)",
 reg="Registre : Michée — P451 (Mi 1:2-9 : tas de ruines, plaies à la porte), P452 (Mi 1:10-16 : Gath, villes livrées, exil) ; rappel P115 (Is 8:1-4, cité en A010)",
 texte=[
  "« Jéhovah SORT de son temple… les montagnes FONDENT, les vallées se FENDENT. » (1:3-4)",
  "« À cause de la TRANSGRESSION de Jacob… les hauts lieux de Juda. » (1:5 — Samarie + Juda !)",
  "« Je ferai de Samarie un TAS DE RUINES de la campagne. » (1:6 — ʿî : monceau !)",
  "« Je ROULERAI ses pierres dans la VALLÉE, je DÉCOUVRIRAI ses fondements. » (1:6)",
  "« Ses images MISES EN PIÈCES, ses salaires BRÛLÉS. » (1:7 — le salaire de prostituée !)",
  "« Sa plaie est INGUÉRISSABLE… elle atteint la PORTE de Jérusalem. » (1:9 — jusqu'à Jérusalem !)",
  "« Ne l'annoncez pas à GATH… à Beth-Leaphra, roule-toi dans la POUSSIÈRE. » (1:10 — P452 !)",
 ],
 contexte=(
  "Michée, contemporain d'Ésaïe et d'Osée, prophétise ≤ 60 ans ; ses oracles contre "
  "Samarie sont antérieurs à 740 (voir si-1 « Mika », 1101990094). Capitale du Nord "
  "depuis Omri (Sichem → Thirtsa → Samarie — voir 1964686), la ville cumule : temple de "
  "Baal d'Achab (1R 16:32 — C8), veaux de Béthel et Dan (1R 12:28-29 — C8 ; voir J002), "
  "alliances égyptiennes d'Osée (2R 17:4 — C8). Le procès s'ouvre à l'échelle cosmique — "
  "« écoutez, peuples » (1:2 — C8) — puis l'arrêt tombe en deux temps : Samarie rasée "
  "(1:6-7), puis la plaie qui marche vers le sud, ville par ville (1:10-16 — P452 : "
  "Gath, Beth-Leaphra, Shaphir, Tsaanan, Beth-Haétsel, Maroth, Lakish, Morésheth, Akzib, "
  "Marésha, Adoullam)."
 ),
 explication=(
  "« Tas de ruines de la campagne » (ʿî haśśadeh) : pas une ruine urbaine relevable, "
  "mais un monceau de pierres en plein champ — la ville rendue à l'agriculture. "
  "« Rouler les pierres dans la vallée » : Samarie est sur une colline (achetée à Shémer, "
  "1R 16:24 — C8) — ses pierres dégringolent la pente, les fondements mis à nu : "
  "description topographique exacte. « Salaires de prostituée » (1:7) : les offrandes "
  "idolâtres, brûlées — le culte paie. « Inguérissable » (1:9) : pas de restauration "
  "pour la capitale du schisme. Puis 1:10-16 : chaque ville est un calembour funèbre "
  "(Shaphir « belle » sort « nue-honteuse », Tsaanan « sortie » ne « sort » pas…) — la "
  "marche assyrienne épelée en jeux de mots, jusqu'à la porte de Jérusalem."
 ),
 interpretation=(
  "Samarie : le schisme jugé — la capitale qui divisa le peuple (voir J002 : Béthel) "
  "est effacée la première. Juda : averti — la même plaie marche vers le sud (1:9 : "
  "« jusqu'à la porte » ; 701 : Sennachérib — voir A013 ; 607/587 : Nébucadnezzar — "
  "2R 25:1-11, P452). Gath : « ne l'annoncez pas » (1:10) — reprise du deuil de David "
  "(2S 1:20 — C8) : que l'ennemi n'apprenne pas. Lakish (1:13) : « commencement du péché "
  "pour Sion » — la contagion du Nord vers le Sud. Morésheth (1:14) : le village de "
  "Michée lui-même (1:1 — C8) — le prophète annonce la ruine de chez lui."
 ),
 hist=(
  "740 (repère des publications) : après 3 ans de siège (2R 17:5 — P451 ; voir 1964686), "
  "Samarie tombe — 6e année d'Ézéchias. Qui prit la ville ? Sargon se vante (« j'assiégeai "
  "et conquis Samerina »), mais c'est probablement Salmanasar V qui acheva (voir "
  "1101990094 ; 1200003842 : chronique babylonienne « il dévasta Samarie », 2R 18:9-10 "
  "« on réussit à s'en emparer »). 27 290 captifs déportés (annales de Sargon — voir "
  "1964686), remplacés par des colons (Babylone et ailleurs — 2R 17:24 — C8). Avant : "
  "Galilée déportée (2R 15:29 — P115, voir A010) et Damas prise (2R 16:9 — P115). Après : "
  "les villes de 1:10-16 (Lakish fouillée : contre-rampe assyrienne — voir A013), puis "
  "Jérusalem (2R 25 — P452)."
 ),
 geo=(
  "Samarie : colline isolée au cœur d'Éphraïm — pierres roulées dans la vallée (1:6) à "
  "la lettre. La marche (1:10-16) : de Gath (Philistie — « ne l'annoncez pas ») vers "
  "l'est puis le sud judéen — Beth-Leaphra, Shaphir, Tsaanan, Maroth, Lakish (verrou du "
  "Shéphéla), Morésheth, Akzib, Marésha, Adoullam — jusqu'à « la porte de Jérusalem » "
  "(1:9). Halah, Habor, Mèdes (2R 17:6 — P451) : les lieux de déportation, en Haute-"
  "Mésopotamie et Médie."
 ),
 sci=(
  "Poliorcétique : 3 ans de siège (2R 17:5) — blocus, famine, brèche : la prise d'une "
  "colline fortifiée sans artillerie. Démographie impériale : 27 290 déportés chiffrés "
  "(Sargon) + colons importés — le transfert de populations assyrien, documenté. "
  "Onomastique : 1:10-16 — onze calembours géographiques, prouesse rhétorique intraduisible "
  "pleinement (Shaphir/shépher, Tsaanan/yātsā'…). Stratigraphie : Samarie (Sébaste) "
  "fouillée — palais d'Omri/Achab (ivoires ! 1R 22:39 — C8), niveaux de destruction "
  "assyriens."
 ),
 limites=(
  "740 : repère des publications (convention courante : 722/720 — signalé, non tranché "
  "ici ; système des sièges seul). Sargon vs Salmanasar : la fiche suit les publications "
  "(vantardise probable de Sargon — voir 1200003842). Les calembours de 1:10-16 sont "
  "donnés en traduction : l'hébreu joue, le français explique. P115 (Damas-Samarie "
  "pillées « avant papa ») est cité en A010 : rappel, pas doublon. 607/587 : voir B002, "
  "non rediscuté ici."
 ),
 accomplissement=[("Omri", "Colline achetée (C8)"), ("Avant papa", "Galilée + Damas (P115/A010)"), ("3 ans", "Siège (2R 17:5)"),
     ("740 (repère)", "Tas de ruines (1:6)"), ("27 290", "Déportés (Sargon)"), ("Marche", "Villes → porte (1:9-16) → 2R 25")],
 tl=[("Omri", "Colline achetée (C8)"), ("Avant papa", "Galilée + Damas (P115/A010)"), ("3 ans", "Siège (2R 17:5)"),
     ("740 (repère)", "Tas de ruines (1:6)"), ("27 290", "Déportés (Sargon)"), ("Marche", "Villes → porte (1:9-16) → 2R 25")],
 src=[("Mika — Toute Écriture (tas de ruines, Sargon, 740)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990094"),
      ("Sargon — Étude perspicace (vantardise, chronique)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003842"),
      ("Veillez à ne pas profaner (3 ans, 27 290, 1964)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1964686"),
      ("Michée 1 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/33/1")],
 img="images/prophe_L001_samarie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L002", titre="Ninive — les portes des fleuves et le palais dissous",
 ref="Nahum 2:1-10 ; Nahum 3:8-13 ; Nahum 1:8 (P463, voir A)",
 statut="Accomplie (P465, P468)",
 cat="L", syst="Système sièges (663 Thèbes neutre → 632 Ninive publications)",
 reg="Registre : Nahoum — P465 (Na 2:1-10 : bouclier rouge, portes des fleuves, palais fondu), P468 (Na 3:8-13 : No-Amôn, figuiers, portes ouvertes) ; rappels P447/P463/P469 (cités en A), P448 (cité en G)",
 texte=[
  "« Le BOUCLIER de ses vaillants est ROUGE… les chars comme des TORCHES. » (2:3)",
  "« Les chars roulent à FOLLE ALLURE… comme des ÉCLAIRS. » (2:4 — la vision !)",
  "« Ils TRÉBUCHENT… se hâtent vers la MURAILLE. » (2:5 — la panique !)",
  "« Les PORTES DES FLEUVES s'ouvrent, le PALAIS SE DISSOUT. » (2:6 — le verrou saute !)",
  "« PILLEZ l'argent, pillez l'or… TRÉSORS SANS FIN. » (2:9 — le butin !)",
  "« VIDE, VACUITÉ, SOLITUDE… cœurs FONDUS. » (2:10 — le triple vide !)",
  "« Es-tu MEILLEURE que NO-AMÔN, assise entre les FLEUVES ? » (3:8 — Thèbes !)",
  "« Tes forteresses : des FIGUIERS aux fruits PRÉCOCES — secoués, ils TOMBENT. » (3:12)",
 ],
 contexte=(
  "Nahoum (« consolation ») : la déclaration contre Ninive (1:1 — P463, voir A), capitale "
  "de la Puissance assyrienne — « ville de meurtres, pleine de tromperie et de rapine » "
  "(3:1 — C8 ; voir 1988127). Prophétie écrite en Juda, lieu d'Elqosh inconnu (voir si-1 "
  "« Nahoum », 1101990095). Le chapitre 2 est une vision de bataille au présent : on voit "
  "les chars, on entend les roues, on assiste à la brèche. Le chapitre 3 argumente par "
  "précédent : Thèbes (No-Amôn), capitale égyptienne assise entre les bras du Nil, "
  "détruite par les Assyriens eux-mêmes (663 — repère neutre) — « es-tu meilleure ? » "
  "(3:8). Les Ninivites avaient enterré Thèbes ; ils seront enterrés pareillement."
 ),
 explication=(
  "« Portes des fleuves » (2:6) : Ninive est traversée par le Khosr (affluent du Tigre) "
  "et bordée par le Tigre — vannes, écluses, canaux : le système hydraulique qui "
  "protège devient la brèche. « Le palais se dissout » (mûg — fondre) : palais de "
  "briques crues (terre séchée) + inondation = dissolution littérale (voir science). "
  "« Comme un étang dont les eaux s'écoulent » (2:8 — C8) : la population fuit comme "
  "l'eau de la brèche — « Arrêtez ! » crie-t-on, « pas un ne se retourne ». Thèbes (3:8-10) : "
  "fleuves, mer, remparts d'eau, Pout et Libyens alliés — et pourtant exil, enfants "
  "écrasés, grands enchaînés (3:10 — C8) : le dossier que Ninive connaît par cœur, "
  "retourné contre elle. Figuiers précoces (3:12) : les forteresses tombent toutes seules "
  "dans la bouche — il suffit de secouer."
 ),
 interpretation=(
  "« L'authenticité de la prophétie de Nahoum est attestée par sa réalisation à la "
  "lettre » (voir 1101990095) : qui aurait osé prédire la brèche hydraulique, le palais "
  "dissous, le vide triple ? Message de consolation pour Juda (voir 202014323 §2 : "
  "« bonne nouvelle pour le peuple ») : l'imprenable tombe comme Thèbes tomba. « La "
  "détresse ne se lèvera pas deux fois » (1:9 — C8, P463) : Ninive ne reviendra pas — "
  "elle fut si bien effacée qu'on la chercha en vain pendant des siècles, et que des "
  "critiques nièrent son existence (voir 1988127). Les ruines prouvent « que Jéhovah "
  "accomplit sa vengeance » (voir 202014323 §1)."
 ),
 hist=(
  "632 (repère des publications — voir 1101990095, 1988127, 202014323) : Mèdes (Cyaxare) "
  "+ Babyloniens (Nabopolassar) — la Chronique babylonienne : « butin incalculable… la "
  "ville changée en amas de ruines » (voir 1988127). Mécanisme : fortes pluies → Tigre "
  "en crue → pan de muraille emporté → conquête rapide (voir 202014323 §3, avec 1:8 ; "
  "2:6). Découverte : Botta (Khorsabad), Layard (Kuyunjik/Nimroud, XIXe s.) — palais de "
  "Sennachérib (bas-reliefs de Lakish ! voir A013) et d'Assurbanipal (bibliothèque : "
  "Gilgamesh). Thèbes 663 (neutre) : Assurbanipal pille No-Amôn — le précédent (3:8-10). "
  "Argent et or « sans fin » (2:9) : les trésors assyriens, dispersés."
 ),
 geo=(
  "Ninive : rive gauche du Tigre (face de l'actuelle Mossoul), traversée par le Khosr — "
  "« portes des fleuves » à la lettre : deux cours d'eau, un système de vannes. Murailles : "
  "plusieurs kilomètres (porte de Mashki, porte d'Adad — fouillées). Kuyunjik + Nebi "
  "Younous : les deux tells. No-Amôn/Thèbes : Haute-Égypte, entre les bras du Nil — "
  "« assise entre les fleuves » (3:8), miroir de Ninive entre Tigre et Khosr. Médie + "
  "Babylone : les deux mâchoires (nord-est et sud)."
 ),
 sci=(
  "Hydraulique : crue du Tigre + Khosr gonflé = pression sur vannes et murailles — "
  "l'eau comme bélier (voir 202014323). Matériaux : briques crues (adobe) — la brique "
  "séchée au soleil FOND à l'eau : « le palais se dissout » (2:6) est de la chimie des "
  "matériaux. Épigraphie : annales assyriennes (orgueil chiffré) + Chronique babylonienne "
  "(chute datée) + stèles — triple verrou documentaire. Taphonomie urbaine : « amas de "
  "ruines » (chronique) = tells — Kuyunjik : 30+ m de stratigraphie."
 ),
 limites=(
  "632 : repère des publications (convention courante : 612 — signalée, non tranchée ; "
  "système des sièges seul). 663 (Thèbes) : date neutre du registre. Le détail tactique "
  "(quelle vanne ? quel pan de mur ?) n'est pas reconstitué : crue + brèche (voir "
  "202014323), sans plus. 1:8 (inondation) appartient à P463 (cité en A) : rappel, pas "
  "doublon. 3:14-19 (P469, cité en A) : l'agonie — voir A. Jonas (P447/A, P448/G) : le "
  "sursis d'un siècle — voir A et G."
 ),
 accomplissement=[("Thèbes 663 (neutre)", "Le précédent (3:8-10)"), ("Vision", "Chars-éclairs (2:3-4)"), ("Panique", "Trébuchent (2:5)"),
     ("Crue", "Portes ouvertes, palais dissous (2:6)"), ("632 (publications)", "Amas de ruines (chronique)"), ("XIXe s.", "Retrouvée (Layard)")],
 tl=[("Thèbes 663 (neutre)", "Le précédent (3:8-10)"), ("Vision", "Chars-éclairs (2:3-4)"), ("Panique", "Trébuchent (2:5)"),
     ("Crue", "Portes ouvertes, palais dissous (2:6)"), ("632 (publications)", "Amas de ruines (chronique)"), ("XIXe s.", "Retrouvée (Layard)")],
 src=[("Nahoum — Toute Écriture (lettre, 632, portes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990095"),
      ("La cruelle Assyrie (chronique, introuvable, 1988)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1988127"),
      ("Nahoum : prends exemple (Thèbes, crue, 2020)", "https://wol.jw.org/fr/wol/d/r30/lp-f/202014323"),
      ("Nahoum 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/34/2")],
 img="images/prophe_L002_ninive.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L003", titre="Édom — le nid d'aigle précipité, la poix et les chacals",
 ref="Ésaïe 34:1-17 ; Jérémie 49:7-22 ; Ézéchiel 25:12-14 ; Abdias 1-4, 15-16 ; Joël 3:19 (P429)",
 statut="Accomplie (P151, P279, P335, P442, P444, P429 partiel)",
 cat="L", syst="Système rochers (Séir → Pétra → désert)",
 reg="Registre : Ésaïe/Jérémie/Ézéchiel/Abdias/Joël — P151 (Is 34 : désolation pour toujours, animaux), P279 (Jr 49:7-22 : Théman, Botsra, comme Sodome), P335 (Éz 25:12-14 : vengeance par Israël), P442 (Ab 1-4 : nid précipité), P444 (Ab 15-16 : comme tu as fait), P429 (Jl 3:19 : Édom désert — v.19 seul ; vv.18-21 voir G008)",
 texte=[
  "« Mon ÉPÉE est IVRE dans les cieux… elle descend sur ÉDOM. » (Is 34:5 — l'épée ivre !)",
  "« Torrents changés en POIX, poussière en SOUFRE… FUMÉE pour toujours. » (34:9-10)",
  "« Le PÉLICAN, le HÉRISSON… le CHACAL, l'AUTRUCHE l'habiteront. » (34:11, 13 — la faune !)",
  "« Quand tu placerais ton NID comme l'AIGLE… je t'en PRÉCIPITERAI. » (Ab 4 — P442 !)",
  "« Ah ! comme ÉSAÜ est FOUILLÉ ! » (Jr 49:10 — fouillé !)",
  "« BOTSRA : stupéfaction… comme SODOME et GOMORRHE. » (49:13, 18 — comme Sodome !)",
  "« Comme tu as FAIT, il te sera FAIT. » (Ab 15 — P444 : la réciprocité !)",
  "« ÉDOM sera un DÉSERT. » (Jl 3:19 — P429 !)",
 ],
 contexte=(
  "Édom (« rouge ») : Ésaü, le frère (Gn 27 — C8 ; voir P018, compléments), devenu "
  "l'ennemi héréditaire — refus du passage (Nb 20:18-21 — C8), « tu as ri » de la chute "
  "de Jérusalem (Ab 11-14 — C8 ; voir P444). Trois griefs : la vengeance exercée (Éz 25:12 — "
  "P335), l'orgueil du roc (Ab 3 — P442 : « creux des rochers »), la sagesse vantée de "
  "Théman (Jr 49:7 — P279). Quatre prophètes, cinq oracles : Ésaïe 34 (le sacrifice de "
  "Botsra), Jérémie 49:7-22 (fouille + Sodome), Ézéchiel 25:12-14 (la main étendue), "
  "Abdias (le nid précipité + la réciprocité), Joël 3:19 (le désert — P429)."
 ),
 explication=(
  "« Nid d'aigle » (Ab 4 ; Jr 49:16 — P279) : Séla/Pétra, ville invisible, accessible "
  "par un défilé — « un ennemi ne pouvait connaître son existence ; l'envahisseur, "
  "dans le passage étroit, risquait de se trouver assiégé » (voir 1957604). « Je t'en "
  "précipiterai » : Dieu fait tomber de haut. « Épée ivre » (Is 34:5) : ivre de sang "
  "avant même de frapper. « Sacrifice à Botsra » (34:6 — C8) : la ville-capitale en "
  "victime. Poix/soufre/fumée (34:9-10) : la chimie de la mer Morte voisine (bitume) "
  "étendue au pays. « Comme Sodome » (Jr 49:18) : la comparaison terminale — pas de "
  "lendemain. « Comme tu as fait » (Ab 15) : la loi du talion entre nations."
 ),
 interpretation=(
  "Cinq ans environ après la destruction de Jérusalem, les armées de Nébucadnezzar "
  "montèrent contre Édom : « rien ne put sauver les Édomites — pas même les hauteurs "
  "de Pétra » (voir 1957604). « Édom a disparu comme nation » (registre P279, P335). "
  "Puis Rome conquiert la capitale nabatéenne (début du IIe s.), la route caravanière "
  "est abandonnée, Pétra périt — « si littéralement que son existence fut oubliée plus "
  "de mille ans » (voir 1957604, avec Jl 3:19 — P429). « Aujourd'hui Pétra est désolée ; "
  "personne n'y vit… repaire d'animaux sauvages » (voir 1957604) : Ésaïe 34:11-13 à la "
  "lettre. Dernier sursaut : un Iduméen sur le trône de Judée (Hérode — Mt 2 — C8), "
  "puis rien."
 ),
 hist=(
  "Nébucadnezzar contre Édom (5e année après Jérusalem — voir 1957604 ; Josèphe, cité "
  "en L004 pour Ammon-Moab, même campagne). Séla prise par Amatsia (2R 14:7 — C8 : la "
  "ville « Roc » déjà convoitée). Nabatéens : successeurs à Pétra (Ier s. — voir les "
  "limites : pas des Édomites). Rome (IIe s.), séisme (IVe s.), oubli (VIIe-XIXe s.), "
  "Burckhardt 1812 (redécouverte — repère). Hérode l'Iduméen (37-4 — repère) : l'épilogue "
  "humain. Malachie 1:3-4 (P151 : « j'ai livré… ils rebâtiront, je démolirai ») : "
  "l'interdit de retour."
 ),
 geo=(
  "Séir : la montagne d'Édom, grès rouge du wadi Araba à l'Aqaba. Théman (nord) : la "
  "sagesse (Jr 49:7). Botsra (nord) : la capitale du sacrifice (Is 34:6). Séla/Pétra : "
  "« généralement identifiée » à Pétra (voir 1957604 — prudence gardée) — le Siq, "
  "défilé de plus d'un kilomètre, 3 à 12 m de large. Dedan (Jr 49:8 — P279) : l'oasis "
  "caravanière complice. Mer Morte : la poix et le soufre d'à côté (Is 34:9)."
 ),
 sci=(
  "Zoologie d'Is 34:11-13 : pélican (qā'āt), hérisson (qippōd), hibou/chouette, corbeau, "
  "chacals, autruches — faune du désert de Judée et d'Araba, constatée : identifications "
  "hébraïques parfois incertaines (voir les limites). Géologie : grès nubien, érosion "
  "éolienne (le Siq), bitume et soufre de la mer Morte (34:9 — « asphaltite »). "
  "Hydraulique nabatéenne (postérieure) : citernes, barrages — la ville vécut d'eau "
  "captée, mourut de route perdue."
 ),
 limites=(
  "Pétra = Séla : « généralement identifiée » (voir 1957604) — la fiche garde la "
  "prudence de l'article. Les Nabatéens (Pétra I, IIe s.) ne sont PAS l'Édom jugée : "
  "successeurs, pas continuateurs — la nation édomite disparaît, le site est réoccupé. "
  "Is 34:14 (faune nocturne) : identifications non tranchées (voir Pétra : « hérisson » "
  "lui-même débattu). « Pour toujours » (34:10) : désolation durable constatée, pas "
  "spéculation. P429 : seul le v.19 (Édom) est versé ici ; vv.18-21 (source, Juda) — "
  "voir G008."
 ),
 accomplissement=[("Séir", "Frère devenu ennemi"), ("Botsra", "Sacrifice (Is 34:6)"), ("Nid", "Séla l'invisible"),
     ("+5 ans (Josèphe)", "Nébucadnezzar précipite"), ("IIe s.", "Rome, puis l'oubli"), ("Aujourd'hui", "Repaire (Is 34:11-13)")],
 tl=[("Séir", "Frère devenu ennemi"), ("Botsra", "Sacrifice (Is 34:6)"), ("Nid", "Séla l'invisible"),
     ("+5 ans (Josèphe)", "Nébucadnezzar précipite"), ("IIe s.", "Rome, puis l'oubli"), ("Aujourd'hui", "Repaire (Is 34:11-13)")],
 src=[("La plus étrange ville bâtie par l'homme (Pétra, 1957)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1957604"),
      ("Abdias — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/31/1"),
      ("Ésaïe 34 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/34"),
      ("Jérémie 49 — Bible d'étude, notes (Édom, v.7-22)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/49")],
 img="images/prophe_L003_edom.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L004", titre="Moab — ruiné en trois ans, transvasé comme un vin",
 ref="Ésaïe 15:1—16:14 ; Jérémie 48:1-47 ; Ézéchiel 25:8-11 ; Amos 2:1-3 (P431) ; 2 Rois 3:16-19 (P085)",
 statut="Accomplie (P130, P276, P334, P431, P085) / Texte reçu (P277)",
 cat="L", syst="Système campagnes (Mésa → Assyrie → Babylone)",
 reg="Registre : Ésaïe/Jérémie/Ézéchiel/Amos/Rois — P130 (Is 15-16 : trois ans exactement), P276 (Jr 48:1-46 : Camosh en exil, nation supprimée), P277 (Jr 48:47 : captifs ramenés — texte reçu), P334 (Éz 25:8-11 : aux fils de l'Orient), P431 (Am 2:1-5 : os brûlés), P085 (2R 3:16-19 : fosses, Moab livré)",
 texte=[
  "« Dans la NUIT, Ar-Moab DÉVASTÉE… Kir-Moab DÉVASTÉE. » (15:1 — en une nuit !)",
  "« Mon CŒUR CRIE sur Moab… fuyards jusqu'à TSOAR. » (15:5 — le cœur du prophète !)",
  "« En TROIS ANS, comme les années d'un SALARIÉ, la gloire de Moab… PETIT RESTE. » (16:14)",
  "« CAMOSH partira en EXIL, ses prêtres et ses princes avec lui. » (Jr 48:7 — le dieu déporté !)",
  "« Moab TRANQUILLE depuis sa jeunesse… jamais TRANSVASÉ. » (48:11 — le vin sur lie !)",
  "« Je lui enverrai des TRANSVASEURS. » (48:12 — on le verse !)",
  "« Moab sera ANÉANTI… il ne sera plus un PEUPLE. » (48:42 — supprimé !)",
  "« Parce qu'il a BRÛLÉ les os du roi d'Édom pour en faire de la CHAUX. » (Am 2:1 — P431 !)",
 ],
 contexte=(
  "Moab : Loth, le neveu (Gn 19 — C8), devenu le voisin hostile — Balaam loué (voir J007), "
  "Baal-Péor (Nb 25 — C8), Eglon (Jg 3 — C8), puis Mésa révolté contre Omri (stèle de "
  "Dibon, 1868 — voir hist). Cinq oracles : Ésaïe 15-16 (le deuil — le prophète PLEURE "
  "Moab, 15:5 ; 16:11 — C8), Jérémie 48 (le procès : 46 versets, le plus long contre "
  "une nation), Ézéchiel 25:8-11 (la livraison), Amos 2:1-3 (le grief : les os brûlés), "
  "2 Rois 3:16-19 (le prélude : fosses et eau). Motif constant : l'orgueil (« nous "
  "avons appris l'orgueil de Moab » — Is 16:6 — C8 ; Jr 48:29 — P276) et Camosh impuissant."
 ),
 explication=(
  "« Trois ans, comme les années d'un salarié » (16:14) : le salarié compte au jour près "
  "(Lv 25:50 — C8 ; Jb 7:1 — C8) — le délai est de précision comptable. « Transvasé » "
  "(48:11-12) : le vin laissé sur sa lie garde un goût ; on le soutire pour l'affiner — "
  "Moab, jamais exilé, jamais affiné : Dieu envoie les « transvaseurs » (déportateurs). "
  "« Honte de Camosh comme Israël de Béthel » (48:13 — C8 ; voir J002) : le dieu "
  "national déçoit comme le veau. « Os brûlés en chaux » (Am 2:1) : profanation de "
  "sépulture + industrie (la chaux vive) — le grief daté du IXe s. Fosses (2R 3:16 — "
  "P085) : creuser sans pluie ni vent — l'eau viendra d'Édom (3:20 — P085)."
 ),
 interpretation=(
  "Le prélude (2R 3:20-25 — P085) : eau à l'aube, Moab trompé (« c'est du sang ! »), "
  "villes détruites, Kir-Haréseth assiégée — Mésa encerclé offre son premier-né sur la "
  "muraille (3:27 — C8 ; voir 1200013028 : SON fils, pas celui d'Édom — « déduction non "
  "plausible » écartée). La sentence (Is 16:14) : trois ans — « 2 Rois 3 ; invasions "
  "assyriennes » (registre P130). L'exécution (Jr 48) : villes prises une à une (Nebo, "
  "Kirjathaïm, Hesbon, Dibon, Aroër… — P276), Camosh exilé (48:7), nation supprimée "
  "(48:42 : « Moab cesse d'être une nation »). La livraison (Éz 25:8-11 — P334) : villes-"
  "joyaux (Beth-Yesimoth, Baal-Meon, Kirjathaïm) aux fils de l'Orient. La fin : Nébucadnezzar, "
  "5e année après Jérusalem, contre Ammon et Moab (Josèphe — voir 1200013028)."
 ),
 hist=(
  "Stèle de Mésa (Dibon/Dhiban, 1868, basalte noir, Louvre) : le roi raconte sa révolte "
  "contre Omri, ordonnée par Camosh (« Va, prends Nebo ! »), vouant Nebo à Ashtar-Camosh "
  "— dialecte quasi-hébreu, « maison de David » lue par plusieurs (voir J005/J006). "
  "Double attestation : la Bible (2R 3) + la stèle (mêmes lieux, mêmes rois) — Mésa "
  "date (~840, repère). Amos 2:1-3 (P431, fin IXe s. — voir 1200013028) : les os du roi "
  "d'Édom en chaux. Archéologie : dévastation confirmée (voir 1200013028 : Interpreter's "
  "Dictionary). Josias avait déjà profané le haut lieu de Camosh (2R 23:13 — C8 ; voir "
  "J002)."
 ),
 geo=(
  "L'Arnon : le fleuve-frontière nord, canyon de 500 m. Ar-Moab, Kir-Moab/Kir-Haréseth "
  "(sud) : les deux capitales du deuil (15:1). Luhith (montée en pleurs) → Horonaïm "
  "(descente en cris) : la pente vers la mer Morte (15:5). Nimrim : les eaux taries "
  "(15:6). Nebo : le mont de Moïse (Dt 34 — C8) en Moab ! Tsoar : le refuge sud (15:5 — "
  "la ville de Loth, Gn 19 — C8). Dibon : la stèle. Villes-joyaux de l'est (Éz 25:9 — "
  "P334) : la vitrine livrée aux nomades."
 ),
 sci=(
  "Œnologie : soutirage (48:11-12) — transvaser pour séparer le vin de sa lie : Moab = "
  "vin jamais soutiré, goût de fange — métaphore technique exacte. Hydrologie : fosses "
  "de 2R 3:16 (citernes sèches remplies sans pluie — ruissellement d'Édom), Nimrim à sec "
  "(15:6 — source tarie). Épigraphie : stèle de Mésa — alphabet, langue, théologie "
  "(Camosh ordonne, comme Jéhovah ordonne : guerre sainte païenne). Pyrotechnie funéraire : "
  "os → chaux vive (Am 2:1 — fours à chaux ; profanation + recyclage industriel)."
 ),
 limites=(
  "Trois ans (16:14) : le texte ne date pas le point de départ — le registre retient "
  "2 Rois 3 + invasions assyriennes, sans convertir (système des campagnes seul). Fils "
  "de Mésa (2R 3:27) : la fiche suit l'article (son propre fils ; l'autre lecture "
  "« non plausible » — voir 1200013028). P277 (48:47, captifs ramenés) : texte reçu, "
  "« à venir selon le texte » (registre) — sens non développé ici. P431 : les v.4-5 "
  "(Juda/Jérusalem, 2R 25:8-9) appartiennent au dossier judéen — versés pour mémoire."
 ),
 accomplissement=[("Mésa (~840, repère)", "Stèle : Camosh ordonne"), ("Fosses (P085)", "Eau, sang, Kir-Haréseth"), ("3 ans (16:14)", "Gloire ruinée"),
     ("Jr 48", "Villes prises, Camosh exilé"), ("+5 ans (Josèphe)", "Nébucadnezzar : fin"), ("Supprimé", "Plus un peuple (48:42)")],
 tl=[("Mésa (~840, repère)", "Stèle : Camosh ordonne"), ("Fosses (P085)", "Eau, sang, Kir-Haréseth"), ("3 ans (16:14)", "Gloire ruinée"),
     ("Jr 48", "Villes prises, Camosh exilé"), ("+5 ans (Josèphe)", "Nébucadnezzar : fin"), ("Supprimé", "Plus un peuple (48:42)")],
 src=[("Moab — Étude perspicace (Mésa, Amos, Josèphe, archéologie)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013028"),
      ("Ésaïe 15 — Bible d'étude (deuil, 3 ans au ch.16)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/15"),
      ("Jérémie 48 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/48"),
      ("Ézéchiel 25 — Bible d'étude (Moab, v.8-11)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/25")],
 img="images/prophe_L004_moab.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L005", titre="Tyr — oubliée 70 ans, puis la harpe de la prostituée",
 ref="Ésaïe 23:1-18 ; Zacharie 9:1-8 (P502, cité en A) ; Ézéchiel 26-28 (voir A-Tyr)",
 statut="Accomplie (P139)",
 cat="L", syst="Système empires (Babylone → Perse → Grèce)",
 reg="Registre : Ésaïe — P139 (Is 23:1-18 : oubliée 70 ans, commerce repris) ; rappels P502 (Za 9, cité en A), A-Tyr (Éz 26-28, Alexandre 332)",
 texte=[
  "« HURLEZ, navires de Tarsis : elle est DÉVASTÉE, plus de maison ! » (23:1 — l'avis aux navires !)",
  "« La MER a dit : je n'ai pas ACCOUCHÉ. » (23:4 — la mer stérile !)",
  "« QUI a décidé cela contre Tyr, DISTRIBUTRICE de couronnes ? » (23:8 — qui ?)",
  "« JÉHOVAH… pour PROFANER l'orgueil de toute beauté. » (23:9 — Jéhovah !)",
  "« Tyr tombera dans l'OUBLI pour 70 ANS, durée de vie d'UN ROI. » (23:15 — 70 ans !)",
  "« Prends une HARPE… chante BEAUCOUP… qu'on se SOUVIENNE de toi. » (23:16 — la chanson !)",
  "« Ses gains deviendront quelque chose de SAINT pour Jéhovah. » (23:18 — saints !)",
 ],
 contexte=(
  "Tyr : l'île-roc phénicienne + sa ville continentale (Oushou) — « distributrice de "
  "couronnes » (23:8 : elle fonde des colonies-royaumes : Kition, Carthage…), "
  "« commerçants = princes » (23:8). Ésaïe 23 est la « déclaration contre Tyr » (suscription "
  "TM). Sa chute continentale viendra des Chaldéens sous Nébucadnezzar (voir it-1 « Isaïe », "
  "1200002205 : « 23:1, 8, 13, 14 »). Puis l'oubli : 70 ans — « la durée d'un roi », "
  "c'est-à-dire de l'empire babylonien : pendant toute la domination de Babylone, "
  "l'île ne sera plus une puissance financière (voir ip-1/EN Tyr, jw.org). Puis la "
  "reprise sous la Perse : Cyrus tolérant, satrapie de Phénicie — Tyr « s'efforce de "
  "regagner la reconnaissance » comme la prostituée sa clientèle (voir jw.org EN). Et "
  "Jéhovah « lui accordera le succès »."
 ),
 explication=(
  "« Navires de Tarsis » (23:1, 14) : les gros porteurs du commerce lointain — avertis "
  "les premiers : plus de port d'attache. « Révélé depuis Kittim » (23:1 — C8 ; voir "
  "J007 : Chypre) : la nouvelle arrive par les relais maritimes. « La mer n'a pas "
  "accouché » (23:4) : Sidon la « forteresse de la mer » se voit stérile — plus de "
  "filles (colonies). « Durée d'un roi » (23:15) : un seul règne-empire — Babylone du "
  "début à la fin (voir jw.org EN). « Harpe » (23:16) : la prostituée oubliée racole en "
  "musique — le commerce comme prostitution (clients = amants, gains = salaire). « Saints "
  "pour Jéhovah » (23:18) : le salaire change de maître — cèdre tyrien pour le second "
  "temple (Esd 3:7 — C8 : Sidoniens et Tyriens fournissent ; voir B005) !"
 ),
 interpretation=(
  "L'orgueil profané (23:9) : la beauté commerciale humiliée — « Tyr sera abaissée, "
  "oubliée pendant 70 ans » (voir 1200002205). L'oubli mesuré : 70 ans pile — ni "
  "destruction définitive (l'île survit), ni continuité (plus de puissance) : une "
  "parenthèse impériale. La reprise accordée : Jéhovah « s'occupera de Tyr » (23:17) — "
  "le commerce reprend « avec tous les royaumes » (mondialisation perse). La "
  "consécration finale (23:18) : les gains « pour ceux qui habitent devant Jéhovah… "
  "manger à satiété, magnifiques vêtements » — le profit païen au service du culte. "
  "Épilogue : l'île elle-même tombera devant Alexandre (332 — voir A-Tyr, P502/Za 9) : "
  "l'oubli babylonien, puis la digue grecque."
 ),
 hist=(
  "Siège continental : 13 ans selon Josèphe (Contre Apion I, 21 — repère) — Nébucadnezzar "
  "prend Oushou, l'île tient (Éz 29:18 — C8 : « le salaire manqué »). 70 ans : la "
  "domination babylonienne (voir jw.org EN : « the duration of one king ») — de la chute "
  "continentale à Cyrus. Satrapie perse : reprise du commerce (voir jw.org EN : « Jehovah "
  "will grant her success »). Esdras 3:7 (C8) : cèdre de Tyr-Sidon pour le temple — "
  "23:18 en acte. Alexandre 332 (repère) : digue de 800 m, île prise en 7 mois (voir "
  "A-Tyr ; Za 9:4 — P502 : « Jéhovah… frappera sa puissance en mer »)."
 ),
 geo=(
  "L'île-roc : ~800 m au large (avant la digue) — forteresse marine. Oushou (Palaetyr) : "
  "la ville continentale, prise par Nébucadnezzar. Sidon : la sœur aînée (« fille de "
  "Sidon » 23:12 — C8). Tarsis : l'ouest lointain (limites : Tartessos ? Sardaigne ? — "
  "non tranché). Kittim : Chypre, le relais (23:1, 12 ; voir J007). Le Nil : « moisson du "
  "Nil » (23:3 — C8) — le blé égyptien via Tyr. La digue : 800 m (repère) — l'île "
  "devenue presqu'île (tombolo actuel)."
 ),
 sci=(
  "Thalassocratie : marine marchande + colonies + comptoirs — le modèle phénicien "
  "(Kition, Carthage, Gadès). Pourpre : le murex — « la pourpre de Tyr », teinture au "
  "coquillage (milliers de murex par gramme — artisanat standard). Organologie : kinnôr "
  "(harpe-lyre, 23:16) — l'instrument du racolage et du psaume. Économie : « gain des "
  "nations » (23:3) — place financière antique ; « salaire » (23:17-18) — comptabilité "
  "de la prostitution commerciale, puis trésorerie du temple."
 ),
 limites=(
  "Tarsis : identification non tranchée (plusieurs ports de l'ouest proposés). 70 ans : "
  "bornes exactes non fixées ici — « durée d'un roi » = l'empire babylonien (voir jw.org "
  "EN) ; système des empires seul, pas de conversion absolue. 23:18 (gains saints) : "
  "lecture proposée via Esdras 3:7, non exclusive. Alexandre (île, 332) : épilogue — "
  "voir A-Tyr (Éz 26-28) et P502 (Za 9, cité en A) : cette fiche s'arrête à la reprise "
  "perse. 13 ans (Josèphe), 800 m (digue) : repères, signalés."
 ),
 accomplissement=[("Oushou", "Continentale prise (Chaldéens)"), ("70 ans", "Oubli : durée d'un roi"), ("Cyrus", "Satrapie : la harpe reprend"),
     ("Esd 3:7 (C8)", "Cèdre : gains saints"), ("Reprise", "Tous les royaumes (23:17)"), ("332 (repère)", "L'île : Alexandre (A-Tyr)")],
 tl=[("Oushou", "Continentale prise (Chaldéens)"), ("70 ans", "Oubli : durée d'un roi"), ("Cyrus", "Satrapie : la harpe reprend"),
     ("Esd 3:7 (C8)", "Cèdre : gains saints"), ("Reprise", "Tous les royaumes (23:17)"), ("332 (repère)", "L'île : Alexandre (A-Tyr)")],
 src=[("Isaïe (Livre d') — Étude perspicace (Tyr 70 ans, Chaldéens)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002205"),
      ("Ésaïe 23 — Bible d'étude, texte intégral", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/23"),
      ("Jehovah Profanes the Pride of Tyre (Isaiah book, jw.org)", "https://www.jw.org/en/library/books/Isaiahs-Prophecy-Light-for-All-Mankind-I/Jehovah-Profanes-the-Pride-of-Tyre/"),
      ("Zacharie 9 — Bible d'étude (Tyr, Philistie, Alexandre)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/9")],
 img="images/prophe_L005_tyr.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L006", titre="La Philistie — Gaza chauve, Ascalon silencieuse, côte retranchée",
 ref="Jérémie 47:1-7 ; Ézéchiel 25:15-17 ; Sophonie 2:4-7 ; Joël 3:1-8",
 statut="Accomplie (P275, P336, P480, P427)",
 cat="L", syst="Système campagnes (604 côte → 332 Gaza)",
 reg="Registre : Jérémie/Ézéchiel/Sophonie/Joël — P275 (Jr 47 : Gaza rasée, Ascalon dévastée), P336 (Éz 25:15-17 : reste de la côte détruit), P480 (So 2:4-7 : les quatre villes), P427 (Jl 3:1-8 : traite aux Grecs, Alexandre)",
 texte=[
  "« Des EAUX viennent du NORD… torrent qui INONDE. » (Jr 47:2 — Babylone en crue !)",
  "« Les PÈRES ne se retourneront même pas pour leurs FILS. » (47:3 — la débandade !)",
  "« Jéhovah ANÉANTIRA les Philistins, derniers de KAFTOR. » (47:4 — Kaftor = Crète !)",
  "« GAZA est devenue CHAUVE… ASCALON réduite au SILENCE. » (47:5 — chauve et muette !)",
  "« ÉPÉE de Jéhovah… frappe ASCALON et le RIVAGE. » (47:7 — l'ordre !)",
  "« Gaza ABANDONNÉE, Ascalon DÉVASTÉE, Asdod CHASSÉE en plein midi, Ékron DÉRACINÉE. » (So 2:4)",
  "« Ils VENDIRENT les fils de Juda aux GRECS. » (Jl 3:6 — P427 : la traite !)",
 ],
 contexte=(
  "La Philistie : 80 km de côte (près de Joppé à Gaza) sur 24 km de profondeur (voir it-2 "
  "« Philistie, Philistins », 1200003469) — la pentapole : Gaza, Askélon, Aschdod, Écron, "
  "Gath (voir ad, 1200013389). Origine : Kaftor/Crète (Jr 47:4, note TM ; Am 9:7 — C8) — "
  "Peuples de la mer (voir J010). Ennemis d'Israël depuis l'Exode (Ex 13:17 — C8) : "
  "Samson (voir J010), Saül (Gilboa — C8), David (Goliath — C8 ; puis suzeraineté), puis "
  "le répit, puis la traite (Jl 3:4-6 — P427 : Tyr, Sidon ET Philistie vendent les Judéens "
  "aux Yavanim/Grecs). Quatre oracles : Jérémie 47 (l'épée), Ézéchiel 25:15-17 (le "
  "retranchemeent — vengeance de la vengeance), Sophonie 2:4-7 (l'appel nominal), Joël 3 "
  "(la traite payée)."
 ),
 explication=(
  "« Avant que Pharaon prenne Gaza » (47:1) : oracle daté d'avant un fait — puis le "
  "vrai choc vient du NORD (47:2 : Babylone, pas l'Égypte). « Chauve » (47:5, note : tête "
  "rasée en deuil et honte) : Gaza en deuil. « Réduite au silence » (47:5 : nidmeta — "
  "anéantie) : Ascalon muette. « En plein midi » (So 2:4) : Asdod chassée à l'heure où "
  "l'on ne combat pas — surprise totale. « Déracinée » (Ékron — 'aqqēr : arracher) : "
  "calembour (Écron/'aqqaron). « Reste de la côte » (Éz 25:16 — P336) : même les "
  "survivants du littoral. « Vendus aux Grecs » (Jl 3:6) : la traite égéenne — « je "
  "vendrai vos fils aux Sabéens » (3:8 — C8) : talion commercial."
 ),
 interpretation=(
  "« Où sont aujourd'hui la Philistie et ses villes ? » (voir w01, 2001124 §15) : "
  "disparues comme nation — la leçon que l'article tire avec Moab, Ammon et l'Assyrie. "
  "Exécution : 604 (repère neutre du registre, P275/P336/P480) — Nébucadnezzar rase "
  "Ascalon puis Ékron, bataille pour Gaza (voir hist). Achèvement : Alexandre (campagne "
  "de Za 9:1-8 — P427, P502) — Gaza résiste et tombe (332, repère). Épuration ethnique "
  "inversée : « le reste de la côte » (Éz 25:16) — il ne reste rien à retrancher. La "
  "côte change de maîtres (Perse, Grèce, Rome) : les Philistins s'y dissolvent — le nom "
  "seul survit (« Palestine » — exonyme romain, voir les limites)."
 ),
 hist=(
  "604 (neutre) : Nébucadnezzar — la Chronique babylonienne rapporte la campagne ; "
  "Ascalon : destruction totale (fouilles Stager : poteries brisées, charbon, briques "
  "vitrifiées, blé carbonisé, toits effondrés), suivie d'un long hiatus avant l'époque "
  "perse. Ékron (Tel Miqne, Dothan) : détruite ensuite — ville de l'huile (des centaines "
  "d'installations oléicoles). Gaza : disputée avec l'Égypte (bataille — Jr 47:1 : "
  "« Pharaon »), puis Alexandre 332 (repère : siège, résistance). Traite (Jl 3:6 — P427) : "
  "esclaves judéens vers Yavan (Grèce) — commerce égéen documenté. Gath : absente des "
  "oracles (tombée plus tôt — voir les limites)."
 ),
 geo=(
  "La côte : 80 × 24 km (voir 1200003469) — Gaza (sud, verrou de la Via Maris — voir "
  "J011), Ascalon (port, 19 km au nord de Gaza), Asdod (port), Ékron (intérieur, 20 km "
  "de la mer), Gath (piémont). Kaftor/Crète (47:4) : l'origine égéenne. Yavan (Jl 3:6) : "
  "la Grèce des acheteurs. Saba (3:8) : le Yémen des revendeurs — la traite dans les "
  "deux sens. Via Maris : la route des armées (nord : Babylone ; sud : Égypte) — la "
  "Philistie écrasée au milieu."
 ),
 sci=(
  "Poliorcétique : chars, cavalerie, sièges (47:3 — sabots, vacarme, fracas) — l'armée "
  "néo-babylonienne. Rites de deuil : tête rasée (47:5, note), entailles sur le corps "
  "(47:5 — interdit à Israël, Lv 19:28 — C8) — anthropologie comparée. Oléiculture : "
  "Ékron — centaines de pressoirs, ~1 000 tonnes/an estimées (repère de fouille) — "
  "première industrie de l'huile d'olive. Céramique : bichrome égéenne (rouge et noir) — "
  "marqueur philistin en stratigraphie. Fer : monopole passé (voir J010 : 1S 13) — la "
  "supériorité technologique ne sauve pas."
 ),
 limites=(
  "« Pharaon » de 47:1 (preneur de Gaza) : lequel ? Non tranché ici. Gath : absente des "
  "quatre oracles — tombée plus tôt (Ozias, 2Ch 26:6 — C8 ?) : question posée, non "
  "tranchée. Chiffres de fouilles (Stager, Dothan) : repères archéologiques, pas "
  "versets. « Palestine » (nom romain de la province) : exonyme administratif postérieur, "
  "pas continuité nationale — la nation philistine disparaît (voir 2001124). Am 9:7 "
  "(Kaftor) : C8 — aucun P ne le couvre."
 ),
 accomplissement=[("Kaftor", "Crète → côte (47:4)"), ("Traite (P427)", "Fils de Juda aux Grecs"), ("Pharaon (?)", "Gaza prise (47:1)"),
     ("604 (neutre)", "Ascalon, Ékron : silence"), ("Appel (So 2:4)", "Quatre villes nommées"), ("332 (repère)", "Gaza : Alexandre")],
 tl=[("Kaftor", "Crète → côte (47:4)"), ("Traite (P427)", "Fils de Juda aux Grecs"), ("Pharaon (?)", "Gaza prise (47:1)"),
     ("604 (neutre)", "Ascalon, Ékron : silence"), ("Appel (So 2:4)", "Quatre villes nommées"), ("332 (repère)", "Gaza : Alexandre")],
 src=[("Philistie, Philistins — Étude perspicace (Crète, 80 km, pentapole)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003469"),
      ("Cherchez Jéhovah avant le jour (où sont-elles ?, 2001)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2001124"),
      ("Jérémie 47 — Bible d'étude, notes (vérifié)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/47"),
      ("Sophonie 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/36/2"),
      ("Joël 3 — Bible d'étude (traite, vérifié)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/29/3")],
 img="images/prophe_L006_philistie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="L007", titre="Ammon — Rabbah pâturage de chameaux, tell désolé",
 ref="Jérémie 49:1-5 ; Ézéchiel 25:1-7 ; Ézéchiel 21:19-23, 28-32 (P328)",
 statut="Accomplie (P278, P333, P328)",
 cat="L", syst="Système carrefours (Rabbah → Philadelphie → Amman)",
 reg="Registre : Jérémie/Ézéchiel — P278 (Jr 49:1-5 : Rabbah tell désolé), P333 (Éz 25:1-7 : fils de l'Orient, pâture), P328 (Éz 21 : carrefour, Ammon jugée)",
 texte=[
  "« Pourquoi MALKAM possède-t-il GAD ? » (Jr 49:1 — le dieu squatteur !)",
  "« RABBAH deviendra un TELL DÉSOLÉ, ses filles BRÛLÉES. » (49:2 — tell !)",
  "« Hurle, HESBON… Aï DÉVASTÉE ! » (49:3 — la panique !)",
  "« Tu te fiais à tes TRÉSORS… QUI viendra contre moi ? » (49:4 — qui ?)",
  "« Parce que tu as RI : Héah ! sur mon SANCTUAIRE profané… » (Éz 25:3 — le rire !)",
  "« Je te livre aux FILS DE L'ORIENT… ils mangeront tes FRUITS, boiront ton LAIT. » (25:4)",
  "« RABBAH : PÂTURE DE CHAMEAUX… villes : BERCAIL. » (25:5 — chameaux !)",
  "« Je te RETRANCHERAI… tu ne seras PLUS. » (25:7 — retranchée !)",
 ],
 contexte=(
  "Ammon : Ben-Ammi, Loth (Gn 19 — C8) — le voisin d'au-delà du Jabbok. Contentieux : "
  "territoire de Gad convoité (Jr 49:1 — P278 ; Jg 11:13 — C8 : Jephté), Malkam/Milcom "
  "le dieu national (1R 11:5-7 — C8 : haut lieu de Salomon ; voir J002 pour Josias), et "
  "surtout le rire : « Héah ! » sur le sanctuaire profané, le pays dévasté, Juda exilé "
  "(Éz 25:3 — P333). Réponse en trois oracles : Jérémie 49:1-5 (le tell), Ézéchiel 25:1-7 "
  "(les nomades), Ézéchiel 21 (le carrefour : Nébucadnezzar hésite entre Rabbah et "
  "Jérusalem — 21:19-23 ; puis Ammon jugée à son tour — 21:28-32, P328). « Circoncis "
  "aux cœurs incirconcis » (Jr 9:25-26 — C8 ; voir 1200010244) : le compte arrive."
 ),
 explication=(
  "« Malkam possède Gad » (49:1) : le dieu a un cadastre — Ammon a annexé le territoire "
  "gadite de l'est ; Malkam « partira en exil » (49:3 — C8) : dieu déporté, comme Camosh "
  "(voir L004). « Tell désolé » (tēl shemamah, 49:2) : Rabbah réduite à son monticule — "
  "un tell = une ville en couches, habitée puis abandonnée. « Fils de l'Orient » (25:4) : "
  "nomades chameliers — campements, tentes, fruits mangés, lait bu : l'économie "
  "sédentaire remplacée par le pastoralisme. « Pâture de chameaux » (25:5) : la capitale "
  "en pré. « Le roi de Babylone arrêté au carrefour… divination : Rabbah ou Juda ? » "
  "(voir 1200010244, avec Éz 21:19-23 — P328) : Juda d'abord (2R 25 — P328), Ammon "
  "ensuite (5e année après Jérusalem, Josèphe — voir L004)."
 ),
 interpretation=(
  "« Les Ammonites commencèrent à boire la coupe » : épée, famine, peste, dévastation "
  "(voir 1200010244). Vérification archéologique : « la Transjordanie fut considérablement "
  "dépeuplée avant le milieu du VIe siècle, et Ammon ne fut pratiquement plus habitée "
  "par des sédentaires jusqu'au IIIe siècle » (voir 1200010244) — « ainsi les Orientaux, "
  "conducteurs de chameaux, purent prendre possession du pays et y dresser leurs tentes » "
  "(Éz 25:4). « Suppression de la nation ammonite » (registre P278, P333). Survivances "
  "sans nation : Tobie l'Ammonite (Né 2:10, 19 — C8) intrigue contre le mur — des "
  "Ammonites, plus d'Ammon. Le site continue : Rabbah → Philadelphie (Ptolémées) → "
  "Amman (capitale actuelle) — continuité du LIEU (voir L : géographie !), pas du "
  "peuple."
 ),
 hist=(
  "Malkam/Milcom : dieu national (1R 11 — C8 ; Jr 49:1, 3 — P278). Carrefour (Éz 21:19-23 — "
  "P328) : hépatoscopie, flèches, téraphim (21:21 — C8) — la divination mésopotamienne "
  "choisit Juda ; 2 Rois 25:1-11 (P328) exécute. Puis Ammon : Josèphe, 5e année après "
  "Jérusalem (même campagne que Moab — voir L004). Tobie (Né 2 — C8, Ve s.) : l'Ammonite "
  "de la restauration — individu, pas nation. Philadelphie : Ptolémée II rebaptise "
  "Rabbah (IIIe s., repère) ; Dèce, Arabie romaine ; Amman : capitale du Jourdain — le "
  "tell (Jebel al-Qal'a, citadelle) toujours occupé."
 ),
 geo=(
  "Rabbah : le tell + la source (« ville des eaux », 2S 12:27 — C8) — aujourd'hui la "
  "citadelle d'Amman. Hesbon, Aï (49:3) : les villes du hurlement. La vallée « féconde » "
  "(49:4) : l'ouadi Amman — greniers d'une capitale. Gad (49:1) : le territoire convoité "
  "à l'ouest. Le Jabbok : la frontière naturelle (Nb 21:24 — C8). L'Orient : le désert "
  "d'où viennent les tentes (25:4) — bédouins d'hier et d'aujourd'hui."
 ),
 sci=(
  "Camélologie : coussinets (sable meuble), callosités poitrine/genoux, dents tout-terrain, "
  "sobre en grain, « végétation commune du désert » (voir it-1 « Chameau », 1200000871 : "
  "« animal très économique ») — le véhicule du jugement (25:5). Tellologie : monticule "
  "stratifié — chaque couche une ville ; « tell désolé » (49:2) = occupation zéro au "
  "sommet. Survey : dépeuplement sédentaire VIe→IIIe s. (voir 1200010244) — prospection "
  "de surface, tessons datants. Économie : sédentaire (fruits, lait des étables — 25:4) "
  "vs nomade (fruits mangés sur place, lait des troupeaux) — le verset décrit la "
  "substitution."
 ),
 limites=(
  "Malkam/Milcom : variantes du nom divin (malk- = roi) — graphies non tranchées. "
  "Divination du carrefour (Éz 21:21) : pratiques rapportées, mécanisme non approuvé ni "
  "décrit — le texte constate le choix (Juda), pas la technique. Tobie (Né 2 — C8) : "
  "des individus survivent — la NATION est supprimée (registre) : la fiche ne confond "
  "pas. Philadelphie/Amman : continuité du SITE (tell occupé) — aucune continuité "
  "nationale ammonite revendiquée. Jr 9:25-26 (C8) : aucun P — vérifié."
 ),
 accomplissement=[("Gad convoité", "Malkam squatte (49:1)"), ("Héah ! (25:3)", "Le rire du sanctuaire"), ("Carrefour (P328)", "Juda d'abord (2R 25)"),
     ("+5 ans (Josèphe)", "Ammon ensuite"), ("VIe→IIIe s.", "Sédentaires : zéro"), ("Rabbah→Amman", "Tell occupé, nation supprimée")],
 tl=[("Gad convoité", "Malkam squatte (49:1)"), ("Héah ! (25:3)", "Le rire du sanctuaire"), ("Carrefour (P328)", "Juda d'abord (2R 25)"),
     ("+5 ans (Josèphe)", "Ammon ensuite"), ("VIe→IIIe s.", "Sédentaires : zéro"), ("Rabbah→Amman", "Tell occupé, nation supprimée")],
 src=[("Ammonites — Étude perspicace (coupe, carrefour, dépeuplée)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010244"),
      ("Chameau — Étude perspicace (Éz 25:5, économique)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000871"),
      ("Ézéchiel 25 — Bible d'étude (Ammon, v.1-7)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/25"),
      ("Jérémie 49 — Bible d'étude (Ammon, v.1-5)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/49")],
 img="images/prophe_L007_ammon.jpg",
))
