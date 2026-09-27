#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE A — PROPHETIES CONTRE LES NATIONS
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - une seule chronologie : 607 / 539 / 537 / 455 / 29 / 33 / 36 / 1914
   + dates neutres signalees comme telles ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="A",
    nom="Prophéties contre les nations",
    sous="Tyr, Sidon, Babylone, l'Égypte, Édom, Moab, Ammon, la Philistie, Ninive",
    intro=(
        "Les prophètes hébreux n'ont pas seulement annoncé l'avenir d'Israël. Une part "
        "considérante de leur message concerne les nations voisines : des villes, des "
        "royaumes, des capitales, avec des détails matériels — où tomberont les pierres, "
        "qui viendra, combien de temps durera la désolation, et parfois si le site sera "
        "réhabité. C'est cette catégorie qui se prête le mieux à la vérification : une "
        "prophétie sur une ville se contrôle sur une carte et dans une fouille, pas dans "
        "une opinion. Elle est donc placée en tête."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F001", titre="Tyr — la ville jetée à la mer",
 ref="Ézéchiel 26:1-21 ; 27:1-36 ; 29:17-20",
 statut="Accomplie",
 cat="A", syst="Dates neutres (332, 315)",
 reg="Registre : partie 5 (Ézéchiel), prophéties contre Tyr — P335 à P344",
 texte=[
  "« Ils détruiront les murailles de Tyr et abattront ses tours ; je raclerai sa poussière "
  "et je ferai d'elle le roc nu. » (Éz 26:4)",
  "« On mettra tes pierres, ton bois et ta poussière au milieu des eaux. » (Éz 26:12)",
  "« Tu ne seras plus rebâtie ; car c'est moi, Jéhovah, qui ai parlé. » (Éz 26:14)",
  "« Beaucoup de nations feront monter contre toi des troupes… elles feront la guerre "
  "contre toi. » (Éz 26:3)",
 ],
 contexte=(
  "Ézéchiel écrit depuis Babylone, parmi les exilés. Sa prophétie contre Tyr est datée "
  "de la onzième année de l'exil, soit 591 avant notre ère environ — pendant que "
  "Nabuchodonosor II assiège Tyr depuis le continent. Tyr existe alors en deux parties : "
  "la ville continentale, appelée Ousou dans les textes égyptiens et Palétyr dans les "
  "textes grecs, et la ville insulaire, bâtie sur un rocher à quelque 800 mètres du rivage, "
  "protégée par une double muraille et par deux ports. La ville insulaire passe pour "
  "imprenable : aucun ennemi n'a de flotte."
 ),
 explication=(
  "Le texte décrit une séquence en trois temps, et non un seul événement. (1) Des "
  "« nations » au pluriel monteront contre la ville — Nabuchodonosor n'est donc qu'un "
  "premier acteur. (2) Les matériaux de la ville seront jetés « au milieu des eaux » : ce "
  "n'est pas le vocabulaire d'une prise ordinaire, où le vainqueur réutilise les pierres ; "
  "c'est celui d'une démolition versée à la mer. (3) Le site deviendra un « roc nu », un "
  "« lieu où l'on étendra les filets ». Le verset 14 dit explicitement que la ville "
  "insulaire ne sera pas rebâtie — ce qui distingue la prophétie de Tyr de celle de "
  "Sidon, sa voisine (voir F002)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que la prophétie s'est accomplie en deux "
  "acteurs successifs : Nabuchodonosor détruit la ville continentale après un siège de "
  "treize ans, puis, plus de deux siècles et demi plus tard, Alexandre le Grand prend la "
  "ville insulaire en construisant une digue avec les décombres de la cité continentale. "
  "Les publications retiennent que, pour bâtir cette digue, Alexandre fit racler jusqu'au "
  "roc le sol de la ville continentale — le « roc nu » du verset 4 — et jeta dans la mer "
  "les débris. La Bibliothèque en ligne note que la digue, longue d'environ 800 mètres, "
  "est encore visible aujourd'hui."
 ),
 accomplissement=[
  ("591 av. n. è. env.", "Ézéchiel prononce la prophétie depuis Babylone"),
  ("588-575 av. n. è.", "Siège de treize ans par Nabuchodonosor II : la ville continentale est prise et détruite ; la ville insulaire reste intacte"),
  ("332 av. n. è.", "Alexandre le Grand, ne pouvant approcher l'île, fait construire une digue avec les débris de la cité continentale"),
  ("332 av. n. è.", "Siège de sept mois (Arrien) ; la ville insulaire tombe, 8 000 Tyriens tués, 30 000 vendus comme esclaves"),
  ("315 av. n. è. - aujourd'hui", "La digue s'ensable, les sédiments s'accumulent : l'ancienne île est devenue une presqu'île ; le port antique est sous les eaux"),
 ],
 hist=(
  "Le déroulement est connu par les historiens grecs : Arrien (Anabase, II) décrit la "
  "construction de la chaussée, le siège de sept mois, et les pertes tyriennes. "
  "L'organisation relève que Nabuchodonosor n'avait rien tiré de son long siège — c'est "
  "l'objet même du texte d'Ézéchiel 29:18-20, où Dieu promet l'Égypte à Nabuchodonosor "
  "« en compensation de la peine que lui a coûtée l'attaque de la ville »."
 ),
 geo=(
  "Tyr se trouve sur la côte phénicienne, dans l'actuel Liban, à environ 80 km au sud de "
  "Beyrouth. La ville insulaire occupait un plateau rocheux calcaire séparé du continent "
  "par un détroit d'environ 800 mètres. Deux ports l'encadraient : le port sidonien au "
  "nord, le port égyptien au sud-est. La configuration du site explique à la fois "
  "l'orgueil de Tyr (« je suis parfaite en beauté », Éz 27:3) et la méthode d'Alexandre : "
  "sans flotte, la seule voie d'accès était de fabriquer la terre ferme."
 ),
 sci=(
  "Le point scientifiquement documenté est le devenir de la digue. Construite en 332 "
  "avant notre ère, la chaussée a interrompu le transit sédimentaire littoral ; les sables "
  "transportés par la dérive côtière s'y sont accumulés pendant des siècles jusqu'à "
  "former un isthme définitif. L'ancienne île est aujourd'hui rattachée au continent : le "
  "rocher nu d'Ézéchiel 26:4 a littéralement été recouvert, puis doublé, par les apports "
  "de sable. L'archéologie sous-marine a par ailleurs repéré, dans les bassins portuaires "
  "antiques, les blocs effondrés des murailles — les « pierres, bois et poussière » jetés "
  "au milieu des eaux."
 ),
 limites=(
  "Le texte d'Ézéchiel 26:14 annonce que Tyr « ne sera plus rebâtie ». Or une ville "
  "moderne — es-Sour — occupe aujourd'hui l'emplacement de l'ancienne île et compte "
  "plusieurs milliers d'habitants. Cette fiche ne prétend donc pas que le site est vide ; "
  "elle retient que la ville insulaire antique a été détruite et que la cité moderne est "
  "bâtie sur l'accumulation sédimentaire, non sur les ruines relevées. L'organisation "
  "signale elle-même cet état de fait. Par ailleurs, la date de 332 est une date neutre, "
  "admise par toutes les chronologies."
 ),
 tl=[("591", "Prophétie"), ("588-575", "Siège de 13 ans"), ("332", "Digue d'Alexandre"),
     ("332", "Chute de l'île"), ("Auj.", "Presqu'île ensablée")],
 src=[("Tyr — la prophétie et la digue d'Alexandre", "https://wol.jw.org/fr/wol/d/r30/lp-f/1988286"),
      ("Ézékiel (livre de) — prophéties contre les nations", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990087"),
      ("Tyr, le siège de sept mois (332)", "https://wol.jw.org/fr/wol/d/r30/lp-f/101980849"),
      ("Alexandre a raclé la poussière de Tyr", "https://wol.jw.org/fr/wol/d/r30/lp-f/1959364"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F001_tyr.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F002", titre="Sidon — le jugement sans la désolation définitive",
 ref="Ézéchiel 28:20-24 ; Jérémie 27:3-11 ; Joël 3:4-8",
 statut="Accomplie",
 cat="A", syst="Dates neutres (701, 351)",
 reg="Registre : partie 5 (Ézéchiel), prophéties contre les nations voisines",
 texte=[
  "« Je vais envoyer contre elle la peste, et le sang coulera dans ses rues… et l'on "
  "saura que je suis Jéhovah. » (Éz 28:23)",
  "« Il n'y aura plus pour la maison d'Israël d'épine qui blesse, ni de ronce qui déchire, "
  "parmi tous ceux qui les entourent. » (Éz 28:24)",
 ],
 contexte=(
  "Sidon est la grande rivale de Tyr, sa voisine de trente kilomètres au nord, et son "
  "aînée : c'est d'elle que sont parties la plupart des colonies phéniciennes. Au temps "
  "d'Ézéchiel, les deux cités se partagent la côte et se disputent la prééminence. "
  "Sidon s'est rebellée contre l'Assyrie — elle fut prise par Sennachérib en 701 avant "
  "notre ère, un événement que les annales assyriennes rapportent en détail et que la "
  "chronologie profane retient sans discussion."
 ),
 explication=(
  "Le texte est court — quatre versets — et, fait remarquable, il ne dit pas ce que dit "
  "Tyr. Ézéchiel 28:23 annonce la peste, le sang, l'épée : un jugement exécuté. Mais le "
  "verset 14 du chapitre 26, qui promet à Tyr de ne plus être rebâtie, n'a pas "
  "d'équivalent pour Sidon. La comparaison des deux oracles est l'un des exercices "
  "d'exégèse les plus nets de la Bible : deux villes voisines, deux jugements de forme "
  "presque identique, et une seule clause de désolation définitive. Le prophète distingue "
  "donc, et l'histoire confirme la distinction."
 ),
 interpretation=(
  "La compréhension retenue est celle d'un jugement réellement exécuté sur Sidon, ville "
  "prise et détruite à plusieurs reprises dans l'Antiquité, sans que le texte biblique "
  "n'annonce sa disparition définitive. Sidon existe toujours, sous le nom de Saïda, au "
  "Liban. Cette fiche sert donc de contre-épreuve méthodologique : elle montre que le "
  "dossier ne force pas les textes dans le même moule."
 ),
 accomplissement=[
  ("701 av. n. è.", "Sennachérib prend Sidon ; les annales assyriennes rapportent la campagne (date neutre)"),
  ("VIᵉ siècle av. n. è.", "Domination babylonienne, puis perse : Sidon devient la base de la flotte perse"),
  ("351 av. n. è.", "Artaxerxès III Ochos détruit Sidon après sa révolte (date neutre)"),
  ("333-332 av. n. è.", "Sidon ouvre ses portes à Alexandre sans combat, contrairement à Tyr"),
  ("Aujourd'hui", "Saïda, troisième ville du Liban, occupe le site antique"),
 ],
 hist=(
  "Les annales de Sennachérib, conservées sur plusieurs prismes d'argile, décrivent la "
  "prise de Sidon et l'installation d'un roi vassal. La destruction de 351 par "
  "Artaxerxès III est rapportée par les historiens grecs (Diodore de Sicile). La Bible "
  "avait annoncé pour Sidon un jugement par l'épée et par la peste, non une "
  "disparition ; l'histoire donne des destructions répétées suivies de reconstructions."
 ),
 geo=(
  "Sidon occupe une presqu'île basse de la côte libanaise, à une quarantaine de "
  "kilomètres au sud de Beyrouth. Contrairement à Tyr, elle n'a jamais été une île : "
  "c'est une avancée de terre prolongée par deux caps, avec un port naturel abrité au "
  "nord. Cette configuration — accessible par terre — explique que la ville ait été prise "
  "à plusieurs reprises là où l'île de Tyr résistait."
 ),
 sci=(
  "Les fouilles du site de Saïda, rendues difficiles par l'urbanisme moderne, ont livré "
  "des niveaux d'occupation continus depuis l'âge du bronze : la strate archéologique "
  "confirme que la ville a été détruite et rebâtie, et non abandonnée. C'est précisément "
  "ce que permettait l'absence de clause de désolation définitive dans le texte."
 ),
 limites=(
  "Cette fiche est la plus fragile de la catégorie sur le plan démonstratif, et c'est "
  "volontaire qu'elle y figure en deuxième position : elle montre que le dossier ne "
  "cherche pas à faire coïncider les textes de force. Le texte de Sophonie 2:4-7 et de "
  "Zacharie 9:5-7, qui visent la Philistie, emploient des formules de désolation plus "
  "fortes que celles d'Ézéchiel 28 pour Sidon."
 ),
 tl=[("701", "Sennachérib"), ("VIᵉ s.", "Perse"), ("351", "Artaxerxès III"),
     ("332", "Ouvre ses portes"), ("Auj.", "Saïda")],
 src=[("Sidon (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200014127"),
      ("Ézékiel (livre de) — prophéties contre les nations", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990087"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F002_sidon.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F003", titre="Babylone — la gloire des royaumes devenue un tas de ruines",
 ref="Isaïe 13:1-22 ; 44:27, 28 ; 45:1, 2 ; Jérémie 50:1-46 ; 51:1-64",
 statut="Accomplie",
 cat="A", syst="Dates neutres (539) + système biblique (607)",
 reg="Registre : partie 4 (Jérémie) — P238 à P245 ; P267 à P269",
 texte=[
  "« Babylone, joyau des royaumes… sera comme Sodome et Gomorrhe,que Dieu détruisit. "
  "Elle ne sera jamais habitée. » (Is 13:19, 20)",
  "« Je dessécherai ses fleuves… je mettrai à sec sa source. » (Jér 51:36)",
  "« On ne prendra plus de toi de pierre d'angle, ni de pierre de fondation ; car tu "
  "deviendras des solitudes pour toujours. » (Jér 51:26)",
  "« Je dis aux eaux : ‹Desséchez-vous›… devant Cyrus. » (Is 44:27, 28)",
 ],
 contexte=(
  "Isaïe écrit au VIIIᵉ siècle avant notre ère, à une époque où Babylone n'est pas encore "
  "la puissance qu'elle deviendra : c'est l'Assyrie qui domine. Nommer Babylone comme la "
  "« gloire des royaumes » relève donc de la prédiction, non de la description. Jérémie, "
  "un siècle plus tard, écrit sous la domination babylonienne elle-même et annonce la "
  "chute de l'empire qui tient Juda captif. Isaïe nomme même le libérateur : Cyrus, "
  "plus de cent cinquante ans avant son règne."
 ),
 explication=(
  "Deux prophéties distinctes sont à ne pas confondre. (1) La chute politique de "
  "Babylone, opérée par Cyrus en 539 : c'est l'objet d'Isaïe 44-45 et de Jérémie 51. "
  "(2) La désolation finale du site, annoncée en Isaïe 13:20 et Jérémie 51:26 : « jamais "
  "habitée », « plus de pierre d'angle ». La première s'accomplit en une nuit ; la "
  "seconde s'étale sur des siècles. Le vocabulaire de Jérémie 51:26 — « tu deviendras des "
  "solitudes pour toujours » — porte sur l'emplacement, pas sur l'empire."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que la désolation de Babylone s'est "
  "accomplie progressivement, et non d'un seul coup : après la prise de la ville en 539, "
  "Babylone demeure une cité importante sous les Perses et sous les Séleucides, puis "
  "décline lentement jusqu'à l'abandon. La Bibliothèque en ligne cite le voyageur "
  "Claudius J. Rich qui, en 1811, ne put découvrir la moindre trace des larges murs de "
  "la ville, et nota qu'aucun arbre ne poussait sur ses ruines à l'exception d'un seul, "
  "très vieux, qui rendait la désolation plus apparente."
 ),
 accomplissement=[
  ("VIIIᵉ s. av. n. è.", "Isaïe annonce la gloire puis la chute de Babylone, et nomme Cyrus (Is 44:28 ; 45:1)"),
  ("VIIᵉ-VIᵉ s. av. n. è.", "Babylone devient la puissance dominante ; Nabuchodonosor II détruit Jérusalem en 607"),
  ("539 av. n. è.", "Cyrus prend la ville dans la nuit, le 16 Tashritu, par le lit détourné de l'Euphrate (date neutre)"),
  ("331 av. n. è.", "Alexandre entre à Babylone ; il projette d'en faire sa capitale mais y meurt en 323"),
  ("IIᵉ s. av. n. è. - IIᵉ s. de n. è.", "Déclin progressif sous les Parthes ; la ville se vide"),
  ("1811 de n. è.", "Claudius J. Rich ne retrouve plus trace des murs : le site est un champ de ruines"),
 ],
 hist=(
  "Trois documents profanes convergent. La Chronique de Nabonide, tablette "
  "cunéiforme, rapporte la prise de la ville et situe l'entrée des troupes de Gubaru le "
  "16 Tashritu. Le cylindre de Cyrus, autre document cunéiforme, présente la prise de "
  "Babylone du point de vue perse et confirme la politique de Cyrus envers les dieux des "
  "villes conquises. Hérodote et Xénophon rapportent le détournement du fleuve, que "
  "Xénophon (Cyropédie, VII) décrit comme le passage de l'armée par le lit de "
  "l'Euphrate pendant une fête."
 ),
 geo=(
  "Babylone se trouve à environ 90 km au sud de Bagdad, sur les deux rives de "
  "l'Euphrate, dans une plaine alluviale plate. La ville était traversée par le fleuve, "
  "avec un pont et, selon Hérodote, des quais maçonnés. Son enceinte intérieure "
  "encerclait environ 850 hectares. Le régime hydrique du site est la clé de son abandon : "
  "l'Euphrate a modifié son cours, et la nappe salée est remontée dans les terres "
  "irriguées pendant des siècles."
 ),
 sci=(
  "La salinisation des sols est le mécanisme le mieux documenté de l'abandon de "
  "Babylone. L'irrigation prolongée, sans drainage suffisant, provoque la remontée des "
  "sels par capillarité ; les rendements s'effondrent, les terres sont abandonnées. "
  "L'archéologie ajoute un facteur : les fouilles ont montré que les briques crues des "
  "monuments, une fois les toits effondrés, se dissolvent sous l'effet des pluies et "
  "redeviennent de la terre — d'où l'expression « tas de ruines » de Jérémie 51:37."
 ),
 limites=(
  "Isaïe 13:20 dit « elle ne sera jamais habitée ». Le site de Babylone a pourtant connu "
  "des occupations tardives : un village hellénistique, un camp romain, et aujourd'hui "
  "même une agglomération moderne (Al-Hillah voisine, et le village de Qwaresh sur le "
  "tell). Cette fiche retient la lecture de l'organisation : la ville impériale a cessé "
  "d'être habitée en tant que ville, et son emplacement est resté un champ de ruines "
  "pendant des siècles. La date de 539 est une date neutre."
 ),
 tl=[("VIIIᵉ s.", "Isaïe nomme Cyrus"), ("607", "Jérusalem dévastée"), ("539", "Chute de Babylone"),
     ("323", "Mort d'Alexandre"), ("1811", "Rich : plus de murs")],
 src=[("Quand Jérusalem a-t-elle été dévastée par Babylone ?", "https://wol.jw.org/fr/wol/d/r30/lp-f/101972329"),
      ("Prophéties — tableau d'accomplissements (Babylone, Rich 1811)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Une date pivot de l'Histoire — 537", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F003_babylone.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F004", titre="L'Égypte — quarante ans, puis un royaume qui ne comptera plus",
 ref="Ézéchiel 29:1-21 ; 30:1-26 ; 31:1-18 ; 32:1-32 ; Jérémie 43:8-13 ; 46:1-28",
 statut="Accomplie",
 cat="A", syst="Système biblique (607)",
 reg="Registre : partie 5 (Ézéchiel), prophéties contre l'Égypte",
 texte=[
  "« Pendant quarante ans il ne sera pas habité. Je ferai du pays d'Égypte le plus désert "
  "de tous les pays. » (Éz 29:11, 12)",
  "« Au bout de quarante ans, je rassemblerai les Égyptiens… et là ils deviendront un "
  "royaume insignifiant. » (Éz 29:13, 14)",
  "« Il n'y aura plus de prince du pays d'Égypte. » (Éz 30:13)",
  "« Je donnerai l'Égypte au roi Nabuchodonosor… ce sera un salaire pour son armée. » "
  "(Éz 29:19, 20)",
 ],
 contexte=(
  "Ézéchiel 29 est daté de la dixième année de l'exil, dans le dixième mois : la "
  "prophétie est prononcée alors que Juda, contre l'avis de Jérémie, compte sur l'Égypte "
  "pour résister à Babylone. Après l'assassinat de Guedalia en 607, les rescapés de Juda "
  "fuient en Égypte, emmenant Jérémie de force, malgré l'avertissement du prophète. "
  "Ézéchiel annonce alors que l'Égypte elle-même tombera et que les fugitifs n'y "
  "trouveront pas le refuge espéré."
 ),
 explication=(
  "Le chapitre distingue deux horizons. Le premier est la désolation de quarante ans "
  "(v. 11-12) : une durée chiffrée, comme les soixante-dix ans de Jérusalem. Le second "
  "est un état durable : l'Égypte redeviendra un peuple, mais « un royaume "
  "insignifiant », et « il n'y aura plus de prince » — c'est-à-dire plus de souverain "
  "égyptien sur le trône. Remarque de lecture : le texte ne dit pas que l'Égypte "
  "disparaîtra, comme Édom ; il dit qu'elle cessera de compter. Les deux annonces sont "
  "de nature différente et doivent être évaluées séparément."
 ),
 interpretation=(
  "La compréhension retenue est que les quarante ans firent suite à la conquête de "
  "l'Égypte par Neboukadnetsar, après 607, et que l'Égypte ne retrouva jamais la place "
  "qui était la sienne au temps des grandes dynasties. La Bibliothèque en ligne écrit "
  "expressément : « Même si l'histoire profane ne fournit aucune preuve de cette "
  "désolation, nous pouvons être convaincus qu'elle a bel et bien eu lieu parce que "
  "Jéhovah est Celui qui accomplit toujours ses prophéties. » Cette phrase est citée ici "
  "en entier parce qu'elle définit la nature de l'argument."
 ),
 accomplissement=[
  (" après 607 av. n. è.", "Les rescapés de Juda fuient en Égypte malgré l'avertissement de Jérémie (Jér 42-43)"),
  (" après 607 av. n. è.", "Neboukadnetsar monte contre l'Égypte et la conquiert ; les fugitifs n'échappent pas aux Babyloniens"),
  (" période de 40 ans", "Désolation annoncée par Ézéchiel 29:11, 12"),
  (" au terme des 40 ans", "Retour des déportés égyptiens au pays de Patros ; l'Égypte redevient un royaume, mais insignifiant"),
  ("525 av. n. è.", "L'Égypte est conquise par Cambyse II, fils de Cyrus (date neutre)"),
  ("332 av. n. è.", "L'Égypte passe sous domination grecque, puis romaine ; plus jamais de pharaon indigène sur le trône après Nectanébo II"),
 ],
 hist=(
  "Le fait déclencheur est attesté par la Bible (Jérémie 43-44) et par des inscriptions "
  "égyptiennes du VIᵉ siècle mentionnant des campagnes babyloniennes. En revanche — et "
  "c'est le point d'honnêteté majeur de cette fiche — l'histoire profane ne documente "
  "pas de quarante années de désolation de la vallée du Nil. Les annales égyptiennes de "
  "cette période sont lacunaires, ce qui laisse la place au débat sans le trancher."
 ),
 geo=(
  "Ézéchiel 29:10 borne le pays « de Migdol à Syène, à la frontière de l'Éthiopie » : "
  "soit du delta du Nil, au nord, jusqu'à Assouan (l'ancienne Syène), au sud, sur plus "
  "de 1 000 kilomètres de vallée. Le « pays de Patros » du verset 14 désigne la Haute-"
  "Égypte. La géographie est donc précise et couvre la totalité du pays habité."
 ),
 sci=(
  "La stèle de Mesha n'a rien à voir ici ; le document qui compte est archéologique : les "
  "niveaux de destruction du VIᵉ siècle relevés sur plusieurs sites du delta, et la "
  "disparition quasi totale des archives officielles égyptiennes pour cette période. "
  "L'argumentaire scientifique est donc négatif : absence de preuve, non preuve "
  "d'absence. Cette fiche le dit explicitement."
 ),
 limites=(
  "**C'est la fiche la plus faible de la catégorie sur le plan documentaire**, et elle "
  "doit être présentée comme telle. L'histoire profane ne fournit aucune preuve des "
  "quarante années de désolation ; l'organisation le reconnaît et fonde sa conviction sur "
  "la fiabilité du prophète, non sur un document. En revanche, la seconde partie de la "
  "prophétie — plus de prince égyptien sur le trône — est, elle, vérifiable et vérifiée : "
  "depuis Nectanébo II (IVᵉ siècle avant notre ère), l'Égypte n'a plus eu de souverain "
  "indigène jusqu'à l'époque moderne."
 ),
 tl=[("607", "Fuite en Égypte"), ("après 607", "Conquête babylonienne"), ("40 ans", "Désolation annoncée"),
     ("525", "Cambyse II"), ("332", "Domination grecque")],
 src=[("Points marquants du livre d'Ézékiel — II", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007562"),
      ("Ézékiel (livre de) — prophéties contre Tyr, l'Égypte et Édom", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990087"),
      ("Ézéchiel 29 (texte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/26/29"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F004_egypte.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F005", titre="Édom — le nid d'aigle vidé, et le nom effacé",
 ref="Abdias 1-21 ; Jérémie 49:7-22 ; Ézéchiel 35:1-15 ; Joël 3:19 ; Malachie 1:2-5",
 statut="Accomplie",
 cat="A", syst="Système biblique (607) + dates neutres (105)",
 reg="Registre : partie 6 (les Douze), Abdias — prophétie vers 607",
 texte=[
  "« À cause de ta violence contre ton frère Jacob, tu seras couvert de honte, et tu "
  "seras exterminé pour toujours. » (Abd 10)",
  "« Quand tu placerais ton nid haut comme l'aigle… je t'en ferai descendre. » (Abd 4)",
  "« Il ne sera plus habité ; il ne sera le séjour d'aucun homme. » (Jér 49:18)",
  "« Je ferai de la montagne de Séir une solitude et un désert. » (Éz 35:7)",
  "« S'ils disent : ‹Nous relèverons les ruines›, je renverserai. » (Mal 1:4)",
 ],
 contexte=(
  "Édom descend d'Ésaü, frère jumeau de Jacob ; la parenté est donc de premier degré, et "
  "c'est ce qui donne à l'oracle sa tonalité : l'accusation porte sur une trahison entre "
  "frères. Lors de la chute de Jérusalem en 607, les Édomites se tiennent « comme l'un "
  "d'eux » : ils pillent, ils barrent les routes aux fuyards, ils livrent les rescapés. "
  "Abdias écrit peu après. Leur capitale, Séla — la Pétra des Grecs — est une forteresse "
  "taillée dans le grès, accessible par une seule faille, le Siq."
 ),
 explication=(
  "L'oracle d'Abdias porte sur deux chefs d'accusation : l'orgueil (v. 3-4 : « toi qui "
  "habites les creux des rochers… quand tu placerais ton nid haut comme l'aigle ») et la "
  "violence envers un frère (v. 10-14). La formulation de Malachie est la plus frappante "
  "pour l'exégèse : elle anticipe l'objection — « nous relèverons les ruines » — et y "
  "répond par avance, « je renverserai ». C'est un texte écrit contre une reconstruction "
  "que personne n'a encore tentée au moment où il est rédigé."
 ),
 interpretation=(
  "La compréhension retenue est un accomplissement en deux temps. (1) Cinq ans environ "
  "après la destruction de Jérusalem, les armées de Neboukadnetsar montent contre Édom : "
  "les hauteurs de Pétra ne sauvent personne. (2) Un siècle et demi plus tard, Édom "
  "tente de se relever — c'est l'objet de Malachie — et disparaît. La Bibliothèque en "
  "ligne ajoute que vers 105 de notre ère Rome conquit la capitale nabatéenne, que la "
  "route des caravanes fut abandonnée, et que « l'existence même de Pétra fut oubliée »."
 ),
 accomplissement=[
  ("607 av. n. è.", "Édom se tient aux côtés des Babyloniens lors de la chute de Jérusalem (Abd 11-14)"),
  ("~602 av. n. è.", "Les armées de Neboukadnetsar montent contre Édom, environ cinq ans après la chute de Jérusalem"),
  ("Vᵉ-IVᵉ s. av. n. è.", "Les Nabatéens s'installent à Pétra ; les Édomites sont repoussés vers le Néguev (Idumée)"),
  (" après 443 av. n. è.", "Malachie : Édom dit « nous relèverons les ruines » ; la réponse est « je renverserai »"),
  ("~105 de n. è.", "Rome annexe la capitale nabatéenne ; la route des caravanes est détournée"),
  (" après 70 de n. è.", "Le nom d'Idumée disparaît de l'histoire"),
 ],
 hist=(
  "La disparition du nom est le fait le mieux documenté. Après la destruction de "
  "Jérusalem par les Romains en 70 de notre ère, le nom d'Idumée cesse d'être employé : "
  "aucune source postérieure ne désigne plus un peuple édomite. La Bibliothèque en ligne "
  "relève par ailleurs que le site de Pétra fut oublié au point que les voyageurs "
  "européens ne le redécouvrirent qu'au XIXᵉ siècle."
 ),
 geo=(
  "Édom occupe le plateau montagneux à l'est de la Arabah, entre la mer Morte et le golfe "
  "d'Aqaba : la montagne de Séir, territoire de grès rouge entaillé de gorges. Pétra est "
  "installée dans un cirque rocheux fermé, alimenté par une source (Aïn Mousa) et "
  "accessible par le Siq, une faille de plus d'un kilomètre. La sécurité du site venait "
  "de là : un seul passage, qu'une poignée d'hommes suffisait à tenir."
 ),
 sci=(
  "L'argument scientifique tient à l'hydrologie nabatéenne. Pétra ne vivait pas de la "
  "pluie mais d'un système de barrages, de citernes et de conduites taillées dans la "
  "paroi, qui captaient les crues du wadi et les stockaient pour l'année. Ce système "
  "supposait un entretien permanent. Quand la route des caravanes se déplaça vers le "
  "nord, la population partit, l'entretien cessa, et l'ensemble du dispositif "
  "hydraulique se colmata définitivement."
 ),
 limites=(
  "Abdias 10 dit « tu seras exterminé pour toujours ». Au sens strict, des Édomites ont "
  "survécu : une partie d'entre eux s'est fondue dans la population de Judée sous le nom "
  "d'Iduméens, et Hérode le Grand était d'origine iduméenne. Cette fiche retient donc "
  "l'accomplissement sur le peuple en tant que nation et sur le territoire en tant que "
  "pays : Édom n'existe plus comme royaume, et son sol est resté désolé. L'organisation "
  "emploie d'ailleurs cette nuance quand elle parle d'« Édom typique »."
 ),
 tl=[("607", "Trahison d'Édom"), ("~602", "Neboukadnetsar"), ("Ve s.", "Nabatéens à Pétra"),
     ("105", "Rome annexe"), ("après 70", "Le nom disparaît")],
 src=[("La plus étrange ville bâtie par l'homme (Pétra, Séla)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1957604"),
      ("Prophéties — tableau d'accomplissements (Édom, Jér. 49:17, 18)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ézékiel (livre de) — prophéties contre Édom", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990087"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F005_edom.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F006", titre="Moab — comme Sodome, un lieu d'orties et une mine de sel",
 ref="Isaïe 15:1-9 ; 16:1-14 ; Jérémie 48:1-47 ; Ézéchiel 25:8-11 ; Sophonie 2:8-11 ; Amos 2:1-3",
 statut="Accomplie",
 cat="A", syst="Système biblique (607)",
 reg="Registre : partie 6 (les Douze) et partie 4 (Jérémie 48)",
 texte=[
  "« Moab deviendra comme Sodome… un lieu envahi par les orties, une mine de sel et un "
  "désert permanent. » (Soph 2:9)",
  "« Ar est dévastée, Moab est réduite au silence… Kir est dévastée, Moab est réduite au "
  "silence. » (Is 15:1)",
  "« Nébo sera dévastée… Kiriathaïm sera prise… Beth-Gamul, Beth-Diblaïthaïm… » (Jér 48:1, 22)",
  "« Je ramènerai les captifs de Moab dans la suite des jours. » (Jér 48:47)",
 ],
 contexte=(
  "Moab occupe le plateau à l'est de la mer Morte, entre le wadi Arnon au nord et le "
  "wadi Zered au sud. Le peuple descend de Lot (Genèse 19:37), ce qui en fait un parent "
  "d'Israël — et l'un de ses adversaires les plus constants. Au IXᵉ siècle, le roi Mesha "
  "se libère de la domination d'Israël ; deux siècles plus tard, Moab est l'un des "
  "voisins qui se réjouissent de la chute de Jérusalem. Sophonie écrit avant 648, "
  "Jérémie avant 607."
 ),
 explication=(
  "La particularité de cet oracle est sa précision toponymique : Jérémie 48 nomme une "
  "trentaine de villes moabites, dont plusieurs ne sont connues que par ce texte. Le "
  "verset 47 contient par ailleurs une ouverture inattendue — « je ramènerai les captifs "
  "de Moab dans la suite des jours » — qui montre que l'oracle n'est pas une condamnation "
  "sans appel mais un jugement temporel, comme pour l'Égypte. La formule de Sophonie, "
  "« comme Sodome », est la plus dure du recueil."
 ),
 interpretation=(
  "La compréhension retenue est que la condamnation fut exécutée par les Babyloniens, "
  "puis par les tribus arabes du désert qui achevèrent de dissoudre l'entité nationale "
  "moabite. La Bibliothèque en ligne, dans son article de référence sur Moab, écrit : "
  "« Depuis des siècles, les Moabites ont cessé d'exister en tant que peuple. De nos "
  "jours, il ne reste plus que des ruines sur les sites identifiés comme étant ceux "
  "d'anciennes villes moabites telles que Nébo, Aroër, Bethgamul et Baal-Méon. De "
  "nombreux autres endroits sont aujourd'hui inconnus. »"
 ),
 accomplissement=[
  (" avant 648 av. n. è.", "Sophonie : Moab deviendra comme Sodome, une mine de sel"),
  (" avant 607 av. n. è.", "Jérémie nomme une trentaine de villes moabites et annonce leur dévastation"),
  (" après 607 av. n. è.", "Les Babyloniens de Neboukadnetsar exécutent le jugement annoncé en Jérémie 25 et 27"),
  ("VIᵉ s. av. n. è.", "Invasion de tribus du désert d'Arabie"),
  (" après 537 av. n. è.", "Cyrus autorise vraisemblablement les exilés moabites à rentrer (Jér 48:47)"),
  (" aujourd'hui", "Il ne reste que des ruines : Nébo, Aroër, Bethgamul, Baal-Méon ; de nombreux sites sont inconnus"),
 ],
 hist=(
  "Le document profane décisif est la **stèle de Mesha**, découverte en 1868 à Dhiban et "
  "conservée au Louvre. Gravée vers 840 avant notre ère en alphabet moabite, elle "
  "mentionne le roi Mesha, le dieu Kemosh, le roi d'Israël Omri et le nom de Jéhovah — "
  "c'est la plus ancienne attestation extra-biblique du tétragramme. Elle prouve "
  "l'existence, la langue et la toponymie du royaume de Moab que décrit la Bible."
 ),
 geo=(
  "Le plateau moabite culmine entre 800 et 1 000 mètres, dominant la mer Morte de plus "
  "de 1 200 mètres. C'est une région de hautes terres cultivables, bien arrosée "
  "comparée à la dépression du Rift, ce qui explique la densité des villes mentionnées "
  "par Jérémie. L'Arnon (l'actuel wadi Mujib) entaille le plateau d'une gorge profonde "
  "qui formait la frontière naturelle du royaume."
 ),
 sci=(
  "La formule de Sophonie — « une mine de sel et un désert permanent » — décrit un "
  "mécanisme réel : sur le pourtour aride de la mer Morte, l'évaporation concentre les "
  "sels dans les sols nus, et les terres abandonnées à l'est de la mer Morte se couvrent "
  "d'efflorescences salines qui interdisent durablement la remise en culture. Les "
  "prospections archéologiques du plateau montrent une interruption de l'habitat sédentaire "
  "après l'époque perse."
 ),
 limites=(
  "Sophonie 2:9 dit « un désert permanent ». La région est aujourd'hui partiellement "
  "cultivée et habitée — la ville moderne de Madaba et ses environs sont densément "
  "peuplés. Cette fiche retient l'accomplissement sur le peuple (les Moabites n'existent "
  "plus comme nation) et sur les villes nommées (de nombreux sites ne sont plus "
  "identifiés). Elle ne prétend pas que le territoire est vide."
 ),
 tl=[("av. 648", "Sophonie"), ("av. 607", "Jérémie 48"), ("après 607", "Babyloniens"),
     ("VIᵉ s.", "Tribus arabes"), ("Auj.", "Ruines non identifiées")],
 src=[("Moab (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013028"),
      ("Prophéties — tableau d'accomplissements (Moab et Ammon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Sophonie 2 (texte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/36/2"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F006_moab.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F007", titre="Ammon — Gomorrhe, et le dieu Milcom emmené en exil",
 ref="Jérémie 49:1-6 ; Ézéchiel 25:1-7 ; 21:28-32 ; Sophonie 2:8-11 ; Amos 1:13-15",
 statut="Accomplie",
 cat="A", syst="Système biblique (607)",
 reg="Registre : partie 6 (les Douze) et partie 4 (Jérémie 49)",
 texte=[
  "« Les Ammonites deviendront comme Gomorrhe, un lieu envahi par les orties, une mine "
  "de sel et un désert permanent. » (Soph 2:9)",
  "« Voici que des jours viennent… où je ferai entendre contre Rabba des fils d'Ammon le "
  "cri de guerre ; elle deviendra un tas de ruines. » (Jér 49:2)",
  "« Milcom s'en ira en exil, ses prêtres et ses chefs avec lui. » (Jér 49:3, d'après le texte)",
  "« Après cela, je ramènerai les captifs des fils d'Ammon. » (Jér 49:6)",
 ],
 contexte=(
  "Ammon occupe le plateau au nord-est de Moab, autour de Rabba — l'actuelle Amman, "
  "capitale de la Jordanie. Comme Moab, le peuple descend de Lot (Genèse 19:38). L'histoire "
  "d'Ammon est faite d'affrontements répétés avec Israël : au temps des Juges, sous Saül, "
  "sous David, et encore sous Josaphat. L'oracle de Jérémie porte un grief précis : les "
  "Ammonites se sont approprié l'héritage de la tribu de Gad pendant que celle-ci était "
  "déportée."
 ),
 explication=(
  "Le grief de Jérémie 49:1 est juridique autant que religieux : « Israël n'a-t-il pas de "
  "fils ? Pourquoi Malcam a-t-il pris possession de Gad ? » Le dieu ammonite Milcom — "
  "appelé Malcam, « leur roi », dans un jeu de mots hébreu fréquent — est présenté comme "
  "un usurpateur de territoire. L'annonce que « Milcom s'en ira en exil » est donc "
  "ironique : un dieu qui part en captivité est un dieu qui ne protège pas son peuple. "
  "Comme pour Moab, le verset 6 ouvre sur un retour des captifs, ce qui borne le "
  "jugement dans le temps."
 ),
 interpretation=(
  "La compréhension retenue est que l'oracle s'est accompli par les Babyloniens, puis "
  "par l'absorption progressive du peuple ammonite dans les populations arabes de la "
  "région. La Bibliothèque en ligne indique que Cyrus permit vraisemblablement aux "
  "exilés ammonites de rentrer, en accomplissement de Jérémie 49:6, et que « comme "
  "Sophonie l'avait prophétisé, les fils d'Ammon étaient devenus comme Gomorrhe, une "
  "solitude désolée »."
 ),
 accomplissement=[
  (" avant 648 av. n. è.", "Sophonie : Ammon deviendra comme Gomorrhe"),
  (" avant 607 av. n. è.", "Jérémie annonce la dévastation de Rabba et l'exil de Milcom"),
  (" après 607 av. n. è.", "Les Ammonites se réjouissent de la chute de Jérusalem (Éz 25:3, 6) et sont jugés à leur tour"),
  ("VIᵉ-Vᵉ s. av. n. è.", "Le royaume disparaît comme entité politique"),
  ("IIIᵉ s. de n. è. env.", "La domination ammonite s'efface définitivement"),
  (" aujourd'hui", "Amman, capitale de la Jordanie, occupe le site antique de Rabba"),
 ],
 hist=(
  "Le nom même du dieu Milcom est attesté par l'épigraphie ammonite : plusieurs "
  "inscriptions et sceaux mentionnent Milcom comme divinité nationale, confirmant le "
  "renseignement biblique. La citadelle d'Amman, au sommet du djebel el-Qal'a, conserve "
  "des niveaux ammonites des VIIIᵉ-VIᵉ siècles."
 ),
 geo=(
  "Rabba-Amman est installée sur un site défensif exceptionnel : une acropole dominant "
  "un cirque de collines, à 800 mètres d'altitude, sur le plateau de Transjordanie, "
  "contrôlant la route commerciale qui remontait d'Arabie vers Damas. La ville était "
  "alimentée par le wadi Amman et par des sources. Cette position de carrefour a "
  "toujours été sa richesse — et la cause de sa convoitise."
 ),
 sci=(
  "Comme pour Moab, la formule « une mine de sel et un désert permanent » renvoie à un "
  "processus mesurable : la steppe qui s'étend à l'est d'Amman reçoit moins de 200 mm de "
  "précipitations par an, seuil en dessous duquel l'agriculture sédentaire n'est plus "
  "possible sans irrigation. Les sols y sont riches en carbonates et en sels ; les "
  "terres abandonnées s'y dégradent très vite et ne se restaurent pas seules."
 ),
 limites=(
  "Sophonie 2:9 annonce un « désert permanent » pour Ammon. Or Amman est aujourd'hui une "
  "métropole de plus de quatre millions d'habitants et l'une des capitales les plus "
  "vivantes du Proche-Orient. Cette fiche ne peut donc pas être présentée comme la "
  "preuve d'un vide. Ce qui s'est accompli est la disparition du peuple ammonite en tant "
  "que nation, et la fin de son culte — le dieu Milcom n'a plus d'adorateurs. C'est "
  "l'objet exact de l'oracle, qui vise un peuple et son dieu, non un sol."
 ),
 tl=[("av. 648", "Sophonie"), ("av. 607", "Jérémie 49"), ("après 607", "Jugement"),
     ("Ve s.", "Royaume effacé"), ("Auj.", "Amman, 4 millions")],
 src=[("Ammonites (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010244"),
      ("Prophéties — tableau d'accomplissements (Moab et Ammon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Sophonie 2 (texte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/36/2"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F007_ammon.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F008", titre="La Philistie — quatre villes nommées, et le bord de la mer en pâturages",
 ref="Amos 1:6-8 ; Jérémie 25:20 ; 47:1-7 ; Ézéchiel 25:15-17 ; Sophonie 2:4-7 ; Zacharie 9:5-7",
 statut="Accomplie",
 cat="A", syst="Système biblique (607) + dates neutres (701, 604)",
 reg="Registre : partie 6 (les Douze), Amos et Sophonie",
 texte=[
  "« Gaza sera une ville abandonnée, et Ascalon sera dévastée. Asdod sera chassée en "
  "plein jour, et Ékrôn sera déracinée. » (Soph 2:4)",
  "« Le bord de la mer deviendra des pâturages, avec des puits pour les bergers et des "
  "enclos pour les moutons. » (Soph 2:6)",
  "« Le roi disparaîtra de Gaza, et Ascalon ne sera plus habitée. » (Zach 9:5)",
  "« J'exterminerai d'Asdod les habitants et d'Ascalon celui qui tient le sceptre ;… les "
  "restes des Philistins périront. » (Am 1:8)",
 ],
 contexte=(
  "La Philistie est une pentapole : cinq villes-États sur la plaine côtière du sud — "
  "Gaza, Ascalon, Asdod, Ékron et Gath. Leurs habitants sont arrivés au XIIᵉ siècle "
  "dans le sillage des « peuples de la mer » ; ils ne sont pas sémites, et la Bible "
  "garde la trace de cette origine (Amos 9:7 : « de Caphtor »). Amos écrit vers 804 "
  "avant notre ère, Sophonie avant 648, Jérémie avant 607 — soit trois prophètes sur "
  "deux siècles, tous avec le même message."
 ),
 explication=(
  "Le détail le plus remarquable est toponymique : Zacharie 9:5 omet Gath. Or Gath "
  "disparaît précisément des sources après la campagne de Hazaël d'Aram, à la fin du "
  "IXᵉ siècle — la Bible cesse de la citer comme ville philistine, et le silence de "
  "Zacharie, deux siècles plus tard, enregistre cette disparition sans la commenter. "
  "Autre détail : Sophonie 2:6 prévoit que « le bord de la mer deviendra des pâturages, "
  "avec des puits pour les bergers » — un renseignement sur l'usage futur du sol, et non "
  "sur la destruction des murailles."
 ),
 interpretation=(
  "La compréhension retenue est que l'ensemble de la pentapole a été frappée, conformément aux trois oracles successifs, et que les Philistins ont cessé d'exister comme "
  "peuple distinct. Les publications relèvent que le jugement fut exécuté par vagues : "
  "les Assyriens, puis les Babyloniens, les Grecs et enfin les Hasmonéens."
 ),
 accomplissement=[
  ("804 av. n. è. env.", "Amos : le feu dans les murs de Gaza, les habitants d'Asdod exterminés (Am 1:6-8)"),
  ("701 av. n. è.", "Sennachérib conquiert Ascalon et Ékron (date neutre)"),
  ("604 av. n. è.", "Neboukadnetsar prend Ascalon ; la ville est détruite (date neutre)"),
  (" avant 648 av. n. è.", "Sophonie : Gaza abandonnée, Asdod chassée, Ékron déracinée, le bord de mer en pâturages"),
  (" avant 607 av. n. è.", "Jérémie 47 : « avant que Pharaon ne frappe Gaza » — l'oracle est daté d'un événement contemporain"),
  ("IIᵉ s. av. n. è.", "Les Hasmonéens font disparaître les dernières cités philistines"),
 ],
 hist=(
  "Aucune source profane ne mentionne plus les Philistins après l'époque perse : le nom "
  "même de la région, Palestina, est une survivance toponymique grecque puis romaine du "
  "mot « Philistin », alors que le peuple a disparu depuis longtemps."
 ),
 geo=(
  "La plaine philistine est une bande de plaine côtière sableuse d'une quarantaine de "
  "kilomètres de large, entre le mont Carmel au nord et le désert du Néguev au sud, "
  "coupée de la Judée par les contreforts de la Shéféla. Gaza est le débouché méridional "
  "de la route de l'encens ; Ascalon et Asdod sont des ports. Leur richesse venait du "
  "commerce, et leur vulnérabilité de leur position sur l'axe militaire égypto-assyrien."
 ),
 sci=(
  "Le document décisif est l'**inscription royale d'Ékron**, découverte en 1993 à Tel "
  "Miqne. Gravée dans le calcaire vers le VIIᵉ siècle avant notre ère, elle mentionne "
  "« Ékron » et nomme cinq de ses rois, dont Akish, fils de Padi — le même nom que le roi "
  "d'Ékron mentionné dans les annales assyriennes de Sennachérib et dans la Bible. "
  "L'identification du site est donc assurée par l'épigraphie, et non par une "
  "supposition."
 ),
 limites=(
  "Sophonie 2:4-7 et Zacharie 9:5-7 annoncent que Gaza et Ascalon ne seront plus "
  "habitées. Les deux villes existent aujourd'hui, et Gaza est l'une des agglomérations "
  "les plus densément peuplées du monde. Cette fiche retient l'accomplissement sur les "
  "Philistins en tant que peuple — disparu — et sur la pentapole en tant que système "
  "politique — dissous. La prophétie vise une nation et ses cités-États, pas l'usage "
  "immémorial d'un site côtier."
 ),
 tl=[("804", "Amos"), ("701", "Sennachérib"), ("604", "Neboukadnetsar à Ascalon"),
     ("av. 648", "Sophonie"), ("IIᵉ s.", "Hasmonéens")],
 src=[("Amos (livre d') — article de référence", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002422"),
      ("Sophonie 2 (texte et renvois)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/36/2"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
      ("Prophéties — tableau d'accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F008_philistie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F009", titre="Ninive et l'Assyrie — la cité du sang oubliée sous son propre tell",
 ref="Nahum 1:1-15 ; 2:1-13 ; 3:1-19 ; Sophonie 2:13-15 ; Jonas 3:1-10",
 statut="Accomplie",
 cat="A", syst="Système biblique (632)",
 reg="Registre : partie 6 (les Douze), Nahum — P447 à P450 ; P463 à P469 ; P479 à P482",
 texte=[
  "« Il dévastera Ninive, il la rendra aussi aride que le désert. » (Soph 2:13)",
  "« Des troupeaux se coucheront au milieu d'elle, toutes les bêtes sauvages, en "
  "troupes. » (Soph 2:14)",
  "« La porte des fleuves est ouverte, et le palais s'effondre. » (Nah 2:6)",
  "« Il est dépouillé, il est emmené ; et ses servantes gémissent comme des colombes. » "
  "(Nah 2:7)",
 ],
 contexte=(
  "Ninive est la dernière capitale de l'Assyrie, sur la rive orientale du Tigre, en face "
  "de l'actuelle Mossoul. Elle a mis à sac Samarie en 740, envahi Juda en 732 et fait "
  "plier Jérusalem sous Ézéchias. Nahum écrit avant sa chute, à une date où l'Assyrie est "
  "encore redoutable : annoncer la destruction de Ninive relève de l'invraisemblable. "
  "Jonas, deux siècles plus tôt, y avait prêché, et la ville s'était repentie "
  "temporairement."
 ),
 explication=(
  "Nahum 2:6 est le verset le plus discuté : « la porte des fleuves est ouverte ». "
  "L'expression fait difficulté, mais deux lectures existent — soit les écluses du "
  "système de canaux qui alimentait Ninive, soit une brèche ouverte dans la muraille par "
  "une crue du Tigre. Les historiens grecs (Diodore de Sicile, d'après Ctésias) rapportent "
  "qu'une crue détruisit une portion des remparts, ouvrant la voie aux assiégeants. La "
  "Bible et la tradition grecque se rejoignent donc sur un mode de prise par l'eau."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah retient la date de 632 avant notre ère pour "
  "la chute de Ninive — en appliquant le système chronologique biblique — tout en "
  "signalant que la chronologie profane place l'événement en 612. Cette fiche suit la "
  "règle du dossier : **un seul système chronologique par contenu**. Elle retient 632 et "
  "signale l'écart, ce qui est la pratique constante du dossier pour Ninive."
 ),
 accomplissement=[
  ("844 av. n. è. env.", "Jonas prêche à Ninive ; la ville se repent temporairement"),
  (" avant 632 av. n. è.", "Nahum annonce la dévastation totale de la cité du sang"),
  ("632 av. n. è.", "Ninive tombe devant les Babyloniens et les Mèdes (système biblique ; 612 en chronologie profane)"),
  (" après la chute", "La ville n'est pas relevée ; le site devient un tell inhabité"),
  ("1842-1849 de n. è.", "Botta, puis Layard, cherchent Ninive : l'emplacement avait été oublié"),
 ],
 hist=(
  "La Chronique babylonienne rapporte la prise de la ville et la fin de l'empire "
  "assyrien. Le fait le plus frappant est l'oubli du site : pendant des siècles, on ne "
  "savait plus où était Ninive. Les voyageurs du XVIIIᵉ siècle situaient encore "
  "l'emplacement de la ville ailleurs. Ce n'est qu'au milieu du XIXᵉ siècle que les "
  "fouilles de Paul-Émile Botta et d'Austen Henry Layard révélèrent les palais de "
  "Sennachérib et d'Assurbanipal."
 ),
 geo=(
  "Ninive occupe la rive orientale du Tigre, à l'emplacement des tells de Kuyundjik et de "
  "Nabi Yunus, dans l'agglomération actuelle de Mossoul (Irak). La ville était alimentée "
  "par un réseau de canaux captant les eaux du Tigre et du wadi Khosr, et protégée par "
  "une enceinte de quelque 12 kilomètres de périmètre. Le Khosr traversait la ville — "
  "d'où l'expression de Nahum sur la « porte des fleuves »."
 ),
 sci=(
  "L'archéologie a confirmé le mécanisme de la prise : les fouilles ont révélé, dans les "
  "niveaux correspondant à la chute, des dépôts de crue et des squelettes pris dans les "
  "décombres, ainsi que des traces d'incendie généralisé. L'épaisseur des couches de "
  "destruction est considérable. Les campagnes de dégagement des années 2020 ont de "
  "nouveau mis au jour les bas-reliefs du palais nord, effondrés lors de la prise."
 ),
 limites=(
  "Deux limites. (1) Chronologique : cette fiche retient 632 selon le système biblique et "
  "signale 612 pour la chronologie profane ; les deux ne doivent jamais figurer comme "
  "équivalentes dans un même document. (2) Géographique : Sophonie 2:13-15 annonce une "
  "désolation telle que « des troupeaux se coucheront au milieu d'elle ». Ninive est "
  "aujourd'hui englobée dans l'agglomération de Mossoul : l'accomplissement porte sur la "
  "cité antique, jamais relevée, et non sur l'absence d'habitat moderne autour du tell."
 ),
 tl=[("844", "Jonas"), ("av. 632", "Nahum"), ("632", "Chute"), ("oubli", "Site perdu"),
     ("1842", "Botta et Layard")],
 src=[("Nahum — le livre et son accomplissement", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013302"),
      ("Ninive (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013311"),
      ("Sophonie 2 (texte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/36/2"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_F009_ninive.jpg",
))
