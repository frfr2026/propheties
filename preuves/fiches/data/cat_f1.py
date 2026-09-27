#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE E-F (vague de transition) — LES EMPIRES (2e partie) + LES CHRONOLOGIES
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="E–F",
    nom="Les empires (2e partie) · Les chronologies",
    vague="7",
    intro=(
        "Cette vague de transition ferme la catégorie E et ouvre la catégorie F. "
        "Côté empires, trois dernières fiches : les rois du nord et du sud au "
        "temps de la fin (avec la position actualisée des publications : "
        "l'identification de 1981 est signalée comme révisée, et les trois "
        "critères de 2020 sont exposés), Daniel 12 (Mikaël, la détresse, les "
        "1 290 et 1 335 jours datés au mois près), et la synthèse des sept "
        "puissances mondiales — dont la septième, prédite avant d'exister, est "
        "la seule purement prophétique. La catégorie E compte ainsi 9 fiches "
        "et est terminée ; le huitième roi appartient à la catégorie I. "
        "Côté chronologies, six fiches : l'arbre de Daniel 4 (le type — le "
        "comput de l'antitype reste à B009, sans doublon), les soixante-dix "
        "semaines (455 → 29 → 33 → 36, et 70 non datée), les 430 ans "
        "(1943 → 1513, jour pour jour), la clé jour-pour-un-an, les 480 ans "
        "(le Temple date l'Exode), et l'an 15 de Tibère (le faisceau de Luc 3, "
        "trois pierres pour six noms)."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E007", titre="Les deux rois au temps de la fin — Nord contre Sud",
 ref="Daniel 11:36-45 ; Daniel 11:35 (charnière, voir E004) ; Révélation 19:20 (renvoi I)",
 statut="En cours (11:44-45 : avenir, sans date)",
 cat="E", syst="Dates neutres (1949, 1991, 2017, 2020)",
 reg="Registre : Daniel — P403 (11:36-45)",
 texte=[
  "« Le roi fera selon son bon plaisir ; il s'élèvera et se grandira au-dessus "
  "de tout dieu. » (Dn 11:36 — le portrait, pas un nom)",
  "« Au temps de la fin, le roi du sud l'attaquera par une poussée ; et le roi "
  "du nord fondra sur lui comme un tourbillon. » (Dn 11:40)",
  "« Il entrera dans le pays de la parure ; Édom, Moab et les chefs d'Ammon "
  "échapperont. » (Dn 11:41)",
  "« Des nouvelles venant de l'est et du nord le troubleront ; il partira en "
  "grande fureur pour supprimer un grand nombre. » (Dn 11:44)",
  "« Il dressera ses tentes entre les mers et la montagne de sainte parure ; "
  "puis il viendra jusqu'à sa fin, et personne ne lui viendra en aide. » "
  "(Dn 11:45)",
 ],
 contexte=(
  "Après « jusqu'au temps de la fin » (11:35 — voir E004), le texte change "
  "d'échelle : plus de noms propres, des titres dont « l'identité et la "
  "nationalité changeraient au cours des siècles » (principe, voir E004). "
  "L'histoire de la compréhension est assumée : en 1981, les publications "
  "identifiaient le Nord au bloc soviétique ; l'URSS s'effondre en 1991 ; en "
  "2020, un article expose trois critères testables et nomme la Russie et ses "
  "alliés. Cette fiche donne les deux états — 1981 et 2020 — sans cacher la "
  "révision."
 ),
 explication=(
  "Le verset 36 peint un profil (exaltation « au-dessus de tout dieu », "
  "« dieu des forteresses » aux versets 38-39 : maozzim — le militarisme "
  "divinisé, les « sommes énormes pour les forces armées »). « Poussée » (11:40, "
  "nagach : heurter comme un bœuf — les « heurts ») : le Sud provoque, le Nord "
  "« inonde » en réponse. « Le pays de la parure » (11:41) : le peuple de Dieu "
  "au milieu, comme en E004 ; Édom, Moab, Ammon épargnés — certains échappent "
  "(application renvoyée, voir Limites). « Nouvelles de l'est et du nord » "
  "(11:44) : le Nord troublé part « supprimer un grand nombre » — vraisemblablement "
  "des serviteurs de Dieu. « Entre les mers et la montagne » (11:45) : la Judée ; "
  "« jusqu'à sa fin, sans aide » : Armaguédon (Ré 19:20) — le Sud encore "
  "« vivant » ce jour-là."
 ),
 interpretation=(
  "La compréhension actuelle des Témoins de Jéhovah (article 2020) tient en "
  "trois critères : pour être le Nord ou le Sud, un pouvoir doit (1) avoir une "
  "influence directe sur les adorateurs de Dieu, (2) se comporter en ennemi de "
  "Jéhovah et de son peuple, (3) rivaliser avec l'autre roi. Bilan : le Nord, "
  "c'est la Russie et ses alliés (persécutions, interdiction de la prédication, "
  "rivalité) ; le Sud, la Puissance anglo-américaine. Daniel 11:34 (« un peu de "
  "secours ») couvre la liberté post-1991 (des centaines de milliers de "
  "proclamateurs). La rivalité 11:40-43 : OTAN (formée en réponse !), course aux "
  "armements, guerres par procuration (Afrique, Asie, Amérique latine), "
  "cyberguerre. Point de continuité avec 1981 : « aucun des deux rois ne "
  "remportera de victoire décisive » — le Nord ne vaincra pas."
 ),
 accomplissement=[
  ("1949 de n. è.", "Le Sud forme l'OTAN : l'alliance-réponse (Washington, 4 avril 1949)"),
  ("1981 de n. è.", "Identification publiée : le Nord = le bloc soviétique (état daté)"),
  ("1991 de n. è.", "Chute de l'URSS ; « un peu de secours » : liberté, prédication (Dn 11:34)"),
  ("2017 de n. è.", "Interdiction en Russie : le critère 1 se vérifie"),
  ("2020 de n. è.", "Article : les trois critères — la Russie et ses alliés, le Nord"),
  ("Avenir", "11:44-45 : fureur, fin sans aide — sans date"),
 ],
 hist=(
  "L'OTAN (4 avril 1949, Washington ; article 5) naît comme réponse du Sud — "
  "exactement le mécanisme de 11:40. L'URSS se dissout fin 1991 (25-26 décembre). "
  "La guerre froide fournit les « heurts » : de la Corée à l'Afghanistan, par "
  "pays interposés. En 2017, la Cour suprême de Russie interdit l'activité — "
  "persécution de centaines de milliers de fidèles sur le territoire du Nord. "
  "La cyberguerre (accusations mutuelles de sabotage informatique des économies) "
  "est citée par l'article 2020 : les « heurts » ont changé d'arme, pas de nature."
 ),
 geo=(
  "Nord et Sud se mesurent depuis le peuple de Dieu (principe E004) — pas depuis "
  "Greenwich. « Entre les mers » (11:45) : la tente finale vise la montagne de "
  "sainte parure — la Judée, encore et toujours l'épicentre (sens détaillé "
  "renvoyé, voir Limites). « Libyens et Éthiopiens à sa suite » (11:43) : le sud "
  "et l'ouest de l'Égypte antique — géographie du texte, application renvoyée. "
  "L'affrontement, lui, est mondial : Europe (OTAN), Afrique, Asie, Amérique "
  "latine, cyberespace."
 ),
 sci=(
  "Pas de science dure : une méthode. Les trois critères de 2020 sont "
  "falsifiables — influence vérifiable, hostilité documentée, rivalité mesurable "
  "(budgets militaires, alliances, cyberattaques attribuées) : l'identification "
  "est testable, pas devinée. La continuité 1981 → 2020 porte sur la structure "
  "(pas de victoire décisive, fin divine du Nord) ; la révision porte sur "
  "l'identité — une mise à jour assumée, pas un effacement : les deux états "
  "sont cités dans cette fiche."
 ),
 limites=(
  "Daniel 11:36-39 (détail verset par verset), 11:41-43 (Édom, Moab, Libye) et "
  "11:45 (« entre les mers ») : applications renvoyées aux publications. "
  "L'article de 1981 (URSS) est cité comme état daté, actualisé en 2020 — "
  "signalé, pas caché. Daniel 11:44-45 est à venir : sans date. Le Sud « vivant » "
  "à Armaguédon (Ré 19:20) : renvoi à la catégorie I pour le détail."
 ),
 tl=[("1949", "OTAN"), ("1981", "Nord = URSS (daté)"), ("1991", "« Un peu de secours »"),
     ("2017", "Interdiction"), ("2020", "Nord = Russie + alliés"), ("Avenir", "11:44-45")],
 src=[("Qui est le roi du Nord aujourd'hui ? (3 critères, 2020)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2020401"),
      ("Le roi du Nord au temps de la fin (11:40-45)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/2020481/6/0"),
      ("Daniel 11 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/11"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E007_nord.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E008", titre="Daniel 12 — Mikaël, la détresse, 1 290 et 1 335 jours",
 ref="Daniel 12 ; Daniel 10:13, 21 (Mikaël) ; Matthieu 24:21 (détresse) ; Jude 9 ; 1 Thessaloniciens 4:16",
 statut="Accomplie (détresse et résurrection : sans date)",
 cat="E", syst="Système 539/537 (vision) · dates neutres (1919-1926)",
 reg="Registre : Daniel — P404 (12:1), P405 (12:2-3), P406 (12:4, 9), P407 (12:7, 11-12)",
 texte=[
  "« En ce temps-là se lèvera Mikaël, le grand prince, le défenseur des fils "
  "de ton peuple ; ce sera un temps de détresse tel qu'il n'y en a pas eu "
  "depuis qu'il existe une nation. » (Dn 12:1)",
  "« Beaucoup de ceux qui dorment dans la poussière se réveilleront, les uns "
  "pour la vie éternelle, les autres pour le mépris éternel. » (Dn 12:2)",
  "« Toi, Daniel, tiens secrètes ces paroles et scelle le livre jusqu'au temps "
  "de la fin. Beaucoup courront çà et là, et la connaissance augmentera. » "
  "(Dn 12:4)",
  "« Depuis le temps où cessera le sacrifice continuel et où sera placée "
  "l'abomination du dévastateur, il y aura 1 290 jours. Heureux celui qui "
  "attendra jusqu'à 1 335 jours ! » (Dn 12:11-12)",
  "« Toi, va vers ta fin ; tu te reposeras, et tu seras debout pour ton "
  "héritage à la fin des jours. » (Dn 12:13)",
 ],
 contexte=(
  "Suite directe de 11:45 (« en ce temps-là »), 3e année de Cyrus (voir E004) : "
  "Daniel, vieillard d'environ quatre-vingt-cinq ans, voit l'homme vêtu de lin "
  "au-dessus du fleuve, deux témoins sur les rives, serment à deux mains levées "
  "(12:5-7). Et Daniel ne comprend pas (12:8) — le prophète lui-même ! « Va, "
  "Daniel » (12:9) : le livre est scellé jusqu'au temps de la fin ; les "
  "méchants ne comprendront pas, « ceux qui ont de l'intelligence comprendront » "
  "(12:10 — les maskilim de 11:33, 35, voir E004). Le livre se ferme sur une "
  "promesse personnelle : repos, puis héritage."
 ),
 explication=(
  "Mikaël (« qui est comme Dieu ? »), « l'un des premiers princes » (10:13), "
  "« votre prince » (10:21) : les publications l'identifient à Jésus-Christ "
  "(archange : Jude 9 ; « voix d'archange » : 1Th 4:16). La détresse « telle "
  "qu'il n'y en a pas eu » est reprise par Jésus (Mt 24:21, « grande tribulation » "
  "— voir la catégorie H). Le livre : les inscrits (Ex 32:32 ; Mal 3:16). "
  "« Beaucoup » (12:2, pas « tous ») : deux issues — « vie éternelle », rare "
  "dans l'Ancien Testament. Les intelligents « resplendiront comme le firmament » "
  "(12:3) : les persécutés de 11:33 deviennent les étoiles. « Scellé » : fermé "
  "jusqu'au temps de la fin — Daniel s'en va sans comprendre : l'humilité du "
  "prophète. Trois temps et demi (12:7) : la même durée qu'en 7:25 — « quand la "
  "force du peuple saint sera entièrement brisée » (années de guerre, détail "
  "renvoyé). 1 290 jours : JOURS LITTÉRAUX — l'abomination (la Société des Nations "
  "proposée, 1919) → + 1 290 jours (3 ans 7 mois) → septembre 1922 (Cedar Point : "
  "condamnation publique de la SDN, sacrifice de louange restauré). 1 335 jours : "
  "comptés depuis la fin des 1 290 → septembre 1922 + 1 335 jours (3 ans "
  "8 mois et demi) → mai 1926 (Londres : purification, « heureux »). « Tu "
  "seras debout » (12:13) : la résurrection de Daniel, nommée."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah lit Daniel 12 en deux volets : "
  "l'intronisation et l'action de Mikaël (1914 — voir B009 — et la délivrance à "
  "venir), puis les deux computs littéraux 1919 → 1922 → 1926 qui prouvent le "
  "déscellement « au temps de la fin ». Le continuel entravé (1914-1919 : "
  "persécution, emprisonnement de juin 1918, libération de mars 1919), puis "
  "restauré : la louange reprend, l'abomination est dénoncée « à sa place indue ». "
  "« Heureux celui qui attend » (12:12) : la béatitude de ceux qui sont restés — "
  "Londres, mai 1926."
 ),
 accomplissement=[
  ("3e année de Cyrus", "La vision au-dessus du fleuve ; le serment ; le sceau (Dn 12:5-9)"),
  ("1914-1918 de n. è.", "Trois temps et demi : le peuple saint brisé (détail renvoyé)"),
  ("1919 de n. è.", "L'abomination proposée (SDN) ; le continuel entravé puis libéré (mars 1919)"),
  ("Septembre 1922", "Cedar Point : + 1 290 jours — la SDN condamnée, la louange restaurée"),
  ("Mai 1926", "Londres : + 1 335 jours — purification, « heureux »"),
  ("Avenir", "Détresse, délivrance des inscrits, résurrection — sans date"),
 ],
 hist=(
  "La Société des Nations (proposée en janvier 1919 à Paris, pacte de juin 1919, "
  "Genève 1920) : le substitut politique au Royaume — « l'abomination ». "
  "Juin 1918 : huit dirigeants emprisonnés (Atlanta) — le continuel entravé ; "
  "26 mars 1919 : libération sous caution — le souffle revient. Cedar Point "
  "(Ohio, 5-13 septembre 1922) : résolution condamnant la SDN et mot d'ordre "
  "« Annoncez le Roi et son Royaume ». Londres (mai 1926, grande assemblée "
  "internationale) : purification de « la ville sainte ». 1919 → 1922 → 1926 : "
  "l'enchaînement au mois près."
 ),
 geo=(
  "Le Tigre (12:5-7) : deux hommes sur les rives, un au-dessus des eaux — la "
  "scène du serment est fluviale, comme à E004. Cedar Point (Ohio) puis Londres : "
  "l'ouest encore (voir E001-E002 : les capitales glissent à l'ouest, les "
  "assemblées aussi). « Beaucoup courront çà et là » (12:4) : voyages ou étude "
  "diligente ? — sens renvoyé aux publications (voir Limites)."
 ),
 sci=(
  "Les computs : 1 290 jours = 43 mois de 30 jours = 3 ans 7 mois "
  "(1919 → septembre 1922) ; 1 335 jours = 44,5 mois = 3 ans 8 mois et demi "
  "(septembre 1922 → mai 1926) — enchaînement exact au mois près, convention "
  "« mois de 30 jours » signalée. Trois temps et demi (12:7) = 1 260 jours : "
  "la même durée qu'en 7:25 — cohérence interne du livre. Daniel est attesté à "
  "Qoumrân (4QDan, voir E001) : le sceau est antique, le déscellement moderne."
 ),
 limites=(
  "Daniel 12:7 (calendrier des trois temps et demi) et 12:4 (« courir çà et là ») : "
  "renvoyés aux publications. Mikaël = Jésus : résumé ici, développement à "
  "l'article Mikaël (Jude 9, 1Th 4:16). La part 1914 / avenir de 12:1 est "
  "renvoyée. Détresse, délivrance, résurrection : sans date. « Beaucoup » (12:2), "
  "pas « tous » : la fiche ne spécule pas."
 ),
 tl=[("3e Cyrus", "Fleuve : serment, sceau"), ("1914-18", "3,5 temps"), ("1919", "SDN : abomination"),
     ("Sept. 1922", "+ 1 290 jours"), ("Mai 1926", "+ 1 335 jours"), ("Avenir", "Détresse, résurrection")],
 src=[("Les 1 290 et 1 335 jours de la prophétie de Daniel", "https://wol.jw.org/fr/wol/d/r30/lp-f/1951525"),
      ("Daniel 12 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/12"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Daniel, un authentique livre de prophéties", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986721")],
 img="images/prophe_E008_daniel12.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E009", titre="Les sept puissances — dont une purement prophétique",
 ref="Révélation 17:10-11 ; Daniel 2 (voir E001) ; Daniel 7 (voir E002) ; Daniel 8:20-21 (voir E003)",
 statut="Accomplie (le 8e roi : renvoi à la catégorie I)",
 cat="E", syst="Système 607/539/1914 · dates neutres (612, 331, 476)",
 reg="Registre : Révélation — P898-P902 (17:1-8) ; 17:10-11 sans entrée (C8)",
 texte=[
  "« Il y a sept rois : cinq sont tombés, un est, l'autre n'est pas encore venu ; "
  "et quand il viendra, il doit rester peu de temps. » (Ré 17:10)",
  "« La bête qui était et qui n'est pas est elle-même un huitième roi ; elle "
  "vient des sept. » (Ré 17:11 — renvoi à la catégorie I)",
  "« C'est toi qui es la tête d'or. » (Dn 2:38 — la liste de Daniel commence à "
  "Babylone : Égypte et Assyrie sont déjà tombées)",
  "« Les pieds, amalgame de fer et d'argile, symbolisent le temps de la puissance "
  "mondiale anglo-américaine. » (compréhension citée)",
 ],
 contexte=(
  "Jean, vers 96 (datation : voir la catégorie I) : « cinq tombés » (Égypte, "
  "Assyrie, Babylone, Médo-Perse, Grèce), « un est » (Rome), « l'autre pas encore "
  "venu » (l'anglo-américaine). Le critère n'est pas la taille : ce sont les "
  "puissances « ayant toutes à faire avec les témoins de Jéhovah » — celles qui "
  "marquent le peuple de Dieu. Daniel (E001-E003) donne les quatre dernières "
  "(l'or commence à Babylone) ; Jean ajoute les deux premières et annonce la "
  "septième — la SEULE mentionnée purement comme prophétie, absente de l'histoire "
  "en 96."
 ),
 explication=(
  "Le tableau : (1) Égypte — l'esclavage, l'Exode 1513 (voir F012) ; "
  "(2) Assyrie — Samarie, Sennachérib, Ninive 612 (voir F009) ; (3) Babylone — "
  "607-539, soixante-huit ans (voir E001, E005) ; (4) Médo-Perse — 539-331 "
  "(voir E002-E003, E006) ; (5) Grèce — 331 et les diadoques (voir E003-E004) ; "
  "(6) Rome — « est » en 96, le fer (voir E001-E003) ; (7) anglo-américaine — "
  "les pieds de fer et d'argile, l'incohésion politico-sociale moderne. "
  "« Peu de temps » (17:10) : qualitatif — pas de comput (voir Limites). "
  "« Vient des sept » (17:11) : le huitième roi (Société des Nations, ONU) est "
  "d'une autre nature — il appartient à la catégorie I, périmètre respecté."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah articule Révélation 17:10 et Daniel 2 : "
  "les quatre derniers métaux (or → pieds) sont les puissances 3 à 7 ; Égypte et "
  "Assyrie, déjà tombées au temps de Daniel, complètent par Jean. Point de "
  "procédure : la réserve d'E001 est levée ici — les pieds de fer et d'argile, "
  "c'est la septième puissance, l'anglo-américaine ; E001 renvoyait au livre "
  "Daniel, E009 tranche avec les sources citées. Les sept têtes du dragon et de "
  "la bête (Ré 12-13, 17) sont ces sept puissances — détail : catégorie I."
 ),
 accomplissement=[
  ("Égypte → 1513 av. n. è.", "1re : l'esclavage, puis la mer Rouge (voir F012)"),
  ("Assyrie → 612 av. n. è.", "2e : Samarie, le siège de 701, Ninive (voir F009)"),
  ("Babylone 607-539", "3e : la tête d'or, soixante-huit ans (voir E001, E005)"),
  ("Médo-Perse 539-331", "4e : l'argent et l'ours (voir E002-E003)"),
  ("Grèce 331-63", "5e : le bronze, le léopard, les quatre (voir E003-E004)"),
  ("Rome (96 : « est »)", "6e : le fer ; 476 : fin de l'Empire d'Occident"),
  ("Anglo-Amérique (moderne)", "7e : les pieds ; « peu de temps » — sans comput"),
 ],
 hist=(
  "Chaque chute est datée : 1513 (mer Rouge), 612 (Ninive), 539 (Babylone), 331 "
  "(Gaugamèles), 63 (Pompée en Judée), 476 (fin de Rome-Occident). La septième "
  "apparaît aux temps modernes (XVIIIe-XIXe siècles — moment précis renvoyé, "
  "voir Limites) et domine le XXe. Sept terrains de fouilles, zéro lacune : "
  "pyramides, Ninive, Babylone, Persépolis, Athènes, Rome — chaque puissance a "
  "ses ruines visitables. La septième, prédite avant d'exister, est le test : "
  "en 96, ni Londres ni Washington ne comptent."
 ),
 geo=(
  "La marche des capitales, toujours vers l'ouest (voir E001-E002) : Memphis et "
  "Thèbes, Ninive, Babylone, Suse et Persépolis, Pella et Alexandrie, Rome, "
  "Londres et Washington — du Nil à l'Atlantique en sept étapes. Patmos, lieu "
  "de la vision : voir la catégorie I. « Les eaux, ce sont des peuples » "
  "(Ré 17:15) : voir la catégorie I."
 ),
 sci=(
  "La méthode : « sept », c'est la plénitude biblique — la liste est fermée, "
  "il n'y a pas de huitième puissance terrestre (le huitième est d'une autre "
  "nature : SDN/ONU — renvoi I). L'archéologie suit le défilé : dariques, "
  "tétradrachmes, deniers, sovereigns (voir E002). Et l'épistémologie : six "
  "puissances vérifiables après coup, une seule prédite avant — la septième "
  "porte seule le poids probant, et elle le porte."
 ),
 limites=(
  "Révélation 17:10-11 sans entrée au registre (C8 — P898-P902 couvrent 17:1-8). "
  "« Peu de temps » : pas de comput, jamais. L'avènement précis de la 7e "
  "(XVIIIe-XIXe s.) est renvoyé aux publications. Le 8e roi : catégorie I "
  "(périmètre). Datation de Révélation (~96) : catégorie I. Rome : la fiche vise "
  "l'Empire du Ier siècle (l'Orient survit jusqu'en 1453 — signalé)."
 ),
 tl=[("Égypte →1513", "1re"), ("Assyrie →612", "2e"), ("Babylone 607-539", "3e"), ("Médo-Perse →331", "4e"),
     ("Grèce", "5e"), ("Rome (« est »)", "6e"), ("Anglo-Amérique", "7e"), ("8e", "renvoi I")],
 src=[("Le lac de feu et sa raison d'être (les sept têtes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1974448"),
      ("Les sept puissances et le huitième roi", "https://wol.jw.org/fr/wol/pc/r30/lp-f/1200023312/4/24"),
      ("Révélation 17 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/17"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E009_puissances.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F010", titre="L'arbre abattu — sept ans de bête pour un roi",
 ref="Daniel 4 ; Daniel 2:28 (Dieu révèle) ; Ézéchiel 31 (l'arbre-assyrien) ; Luc 21:24 (renvoi B009)",
 statut="Accomplie (l'antitype : renvoi B009)",
 cat="F", syst="Dates neutres (605-562) · type (renvoi B009 pour 607/1914)",
 reg="Registre : Daniel — P372 (4:10-27), P373 (4:31-32)",
 texte=[
  "« Voici un arbre au milieu de la terre, d'une hauteur immense ; son feuillage "
  "était beau, son fruit abondant, et tout en tirait nourriture. » (Dn 4:10-12)",
  "« Un veilleur, un saint, descendait des cieux : Abattez l'arbre, mais laissez "
  "en terre la souche avec un lien de fer et de bronze ; que sept temps passent "
  "sur lui. » (Dn 4:13-16)",
  "« C'est toi, ô roi, qui as grandi et qui es devenu fort. » (Dn 4:22 — Daniel "
  "à Neboukadnetsar)",
  "« Au bout de douze mois, le roi se promenait sur le toit : N'est-ce pas ici "
  "Babylone que j'ai bâtie ? » (Dn 4:29-30 — l'orgueil, un an après le rêve)",
  "« Moi, Neboukadnetsar, je loue et j'exalte le Roi des cieux ; ceux qui "
  "marchent dans l'orgueil, il peut les abaisser. » (Dn 4:37 — décret païen)",
 ],
 contexte=(
  "Neboukadnetsar au faîte (règne 605-562, « vers la fin ») : deuxième rêve royal "
  "après la statue (voir E001), sages incapables encore (4:7), appel à Beltshatsar "
  "— « d'après le nom de mon dieu » (4:8, Bel/Marduk : le syncrétisme de cour). "
  "Daniel, troublé une heure (4:19), interprète : l'arbre, c'est le roi. Douze "
  "mois de sursis (4:29), la phrase d'orgueil sur le toit, la voix du ciel "
  "(4:31-32), sept ans avec les bêtes, « à la fin des jours » la raison rendue "
  "(4:34, 36) — et un décret où un roi babylonien prêche Jéhovah à tout empire."
 ),
 explication=(
  "L'arbre-roi : « ta grandeur a grandi » (4:22) — même image pour l'Assyrie "
  "(Éz 31). « Veilleur, saint » (ir weqaddish) : un ange — Daniel est le seul "
  "livre de l'Ancien Testament avec ce titre (4:13, 17, 23). La souche liée "
  "(fer et bronze) : la royauté conservée, pas arrachée — « ton royaume te sera "
  "rendu » (4:26). Sept temps : sept ans — le TYPE littéral. « Afin que les "
  "vivants sachent que le Très-Haut domine » (4:17) : le but, c'est la théologie "
  "pour païens. Bœuf, herbe, rosée, cheveux d'aigle, ongles d'oiseau (4:25, 33) : "
  "le texte décrit ; la fiche ne diagnostique pas (voir Limites). « À la fin "
  "des jours » (4:34) : le terme exact. Le décret (4:34-37) : confession, "
  "louange, leçon — « il peut abaisser »."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah distingue deux accomplissements "
  "(l'arbre, c'est Neboukadnetsar « dans le premier accomplissement » — « premier » "
  "implique un second). Le TYPE : abattu un an après le rêve, fou sept ans, "
  "restauré — « les textes anciens indiquent que Neboukadnetsar est bien tombé "
  "malade vers la fin de son règne » (encyclopédie citée). L'ANTITYPE : "
  "l'interruption de la royauté divine (Jérusalem 607, « trône de Jéhovah » : "
  "1Ch 29:23), sept temps = 2 520 ans, jusqu'en 1914 — RÉSUMÉ ici, COMPUT à B009 "
  "(pas de doublon : cette fiche, c'est le type)."
 ),
 accomplissement=[
  ("605-562 av. n. è.", "Règne de Neboukadnetsar ; le rêve « vers la fin » (non daté)"),
  ("Rêve + 12 mois", "Le toit : « Babylone que j'ai bâtie » — la voix du ciel (4:29-32)"),
  ("7 ans", "Avec les bêtes : herbe, rosée, aigle et oiseau (4:33)"),
  ("« À la fin des jours »", "Raison rendue, trône rendu, « grandeur extraordinaire » (4:34, 36)"),
  ("Décret", "Le Roi des cieux prêché par un roi babylonien (4:34-37)"),
 ],
 hist=(
  "« Babylone que j'ai bâtie » : le roi se vante vrai — briques estampillées à "
  "son nom, porte d'Ishtar, palais, voie processionnelle (Koldewey). Les sages "
  "échouent deux fois (Dn 2, Dn 4) : le monopole de Daniel. « Beltshatsar, "
  "d'après le nom de mon dieu » (4:8) : Daniel porte à la cour le nom de Bel. "
  "Un texte de Qoumrân (4Q242, Prière de Nabonide) raconte un roi babylonien "
  "frappé sept ans à Tayma puis guéri — parallèle débattu (voir Limites) : "
  "confusion de rois ? deux événements ? non tranché."
 ),
 geo=(
  "Le toit du palais (4:29) : la promenade des toits-terrasses mésopotamiens, "
  "d'où l'on domine Babylone — le lieu de l'orgueil. Les champs (4:25) : du "
  "palais au pâturage — la géographie de la chute. Babylone bâtie (Ishtar, "
  "ziggourat, murailles) : le décor de « j'ai bâtie ». La souche reste « en "
  "terre » (4:15) : le royaume attend, lié de fer et de bronze."
 ),
 sci=(
  "La psychiatrie décrit des tableaux voisins (lycanthropie, boanthropy : se "
  "prendre pour un animal) — cités comme tableaux cliniques, JAMAIS appliqués "
  "au roi : pas de diagnostic rétrospectif (voir Limites). La botanique valide "
  "l'image : les souches rejettent — l'arbre lié repousse. Et l'herméneutique : "
  "le type littéral (7 ans) fonde le comput symbolique (voir F013 pour la clé "
  "jour-an, B009 pour les 2 520 ans)."
 ),
 limites=(
  "Le rêve n'est pas daté : pas de dates absolues (« vers la fin du règne »). "
  "Pas de diagnostic rétrospectif : les tableaux cliniques sont cités, non "
  "appliqués. 4Q242 (Nabonide, Tayma) : parallèle débattu — Nabonide n'est pas "
  "Neboukadnetsar. L'antitype (comput 607 → 1914) appartient à B009 : résumé "
  "ici, démontré là-bas."
 ),
 tl=[("605-562", "Règne"), ("Rêve", "L'arbre"), ("+ 12 mois", "« J'ai bâtie »"), ("7 ans", "Bêtes"),
     ("Fin des jours", "Raison, décret")],
 src=[("La prophétie de Daniel : des rêves qui vous concernent (ch. 4)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986720"),
      ("Daniel — Étude perspicace (l'arbre, premier accomplissement)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001117"),
      ("Daniel 4 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/4"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F010_arbre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F011", titre="Les soixante-dix semaines — 455, 29, 33, 36",
 ref="Daniel 9:24-27 ; Néhémie 2:1-8 (455) ; Luc 3:21-22 (29, voir F015) ; Matthieu 27:51 (33)",
 statut="Accomplie (70 non datée d'avance — dit)",
 cat="F", syst="Système 455/29/33/36",
 reg="Registre : Daniel — P384 (9:1-19), P385 (9:24-27), P595 (9:25), P639 (9:26), P640 (9:24), P641 (9:27), P689 (9:26)",
 texte=[
  "« Soixante-dix semaines ont été fixées sur ton peuple et ta ville sainte, "
  "pour finir la transgression, expier la faute, amener la justice éternelle, "
  "sceller vision et prophétie, et oindre le Saint des saints. » (Dn 9:24)",
  "« Depuis la sortie de la parole pour rétablir et rebâtir Jérusalem jusqu'à "
  "Messie le Guide, il y aura sept semaines et soixante-deux semaines ; places "
  "et fossé seront rebâtis, en des temps de détresse. » (Dn 9:25)",
  "« Après les soixante-deux semaines, Messie sera retranché, et il n'aura "
  "rien pour lui ; le peuple d'un guide détruira la ville et le sanctuaire. » "
  "(Dn 9:26)",
  "« Il fera une alliance forte avec beaucoup pendant une semaine ; à la moitié "
  "de la semaine, il fera cesser sacrifice et offrande. » (Dn 9:27)",
 ],
 contexte=(
  "La 1re année de Darius (9:1 — voir E006 !) : Daniel lit Jérémie — les 70 ans "
  "finissent ! — et prie la grande confession (« nous avons péché », 9:3-19). "
  "Gabriel, « volant vite », arrive « au temps de l'offrande du soir » (9:21 — "
  "Daniel prie à l'heure du sacrifice, en exil ; 2e apparition après 8:16, voir "
  "E003). « Au commencement de tes supplications, la parole est sortie » (9:23) : "
  "la réponse précède la fin de la prière. Suit le comput messianique."
 ),
 explication=(
  "Semaines d'années (shavouim — biblistes d'accord ; Maredsous : « semaines "
  "d'années ») : 70 × 7 = 490 ans. Point de départ : la 20e année d'Artaxerxès "
  "(Néh 2:1 : « rétablir et rebâtir Jérusalem ») — 474 = 1re année complète du "
  "roi (« les historiens le confirment »), donc 455. Sept semaines (49 ans, "
  "455 → 406) : « places et fossé » — ville et défense, Néhémie (murs en "
  "52 jours, Néh 6:15 !), Esdras, « temps de détresse » (Sanballat, Tobiya, "
  "Guéshem — voir A011 !). Soixante-deux semaines (→ 29) : « Messie le Guide » — "
  "baptême et onction (Lc 3:21-22 — voir F015 !). « Retranché » (karath : "
  "exécuté), « rien pour lui » (pas de royaume terrestre — 33). « Le peuple "
  "d'un guide » : les Romains — ville et sanctuaire (70, voir B007). Soixante-dixième "
  "semaine (29 → 36) : « alliance forte avec beaucoup » — les Juifs, faveur "
  "exclusive sept ans ; « moitié » (33) : fin du sacrifice — le voile déchiré "
  "« de haut en bas » (Mt 27:51 — voir D) ; 36 : Corneille (voir C012) — fin de "
  "l'exclusivité. « Justice éternelle », « Saint des saints » (9:24) : le but — "
  "application exacte renvoyée (voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah tient le schéma : 455 → + 483 ans "
  "(69 semaines ; calcul : 455 av. → 1 av. = 454 ans, + 29 = 483 — pas d'an 0 !) "
  "→ 29 (Messie) → moitié de la 70e : 33 (retranché) → 36 (Corneille). « Les "
  "Juifs du Ier siècle connaissaient bien cet aspect chronologique » : l'attente "
  "(Lc 3:15, « le peuple était dans l'attente » — voir F015) vient du comput ! "
  "Et l'honnêteté du texte : 70 (Titus) est annoncée (9:26) mais NON datée — "
  "« date qui n'avait pas été révélée à l'avance » : la prophétie date le "
  "Messie, pas Titus."
 ),
 accomplissement=[
  ("538 av. n. è.", "La vision, 1re année de Darius ; Gabriel « volant vite » (Dn 9:1, 21)"),
  ("455 av. n. è.", "20e année d'Artaxerxès : Néhémie autorisé (Néh 2:1-8) — départ"),
  ("406 av. n. è.", "Fin des 7 semaines : ville rebâtie, « places et fossé »"),
  ("29 de n. è.", "69 semaines : baptême — « Messie le Guide » (voir F015)"),
  ("33 de n. è.", "Moitié de la 70e : retranché, voile déchiré"),
  ("36 de n. è.", "Fin de la 70e : Corneille — les nations (voir C012)"),
  ("70 de n. è.", "Ville et sanctuaire (9:26) — annoncée, NON datée d'avance"),
 ],
 hist=(
  "Artaxerxès Ier (474 = 1re année complète — historiens ; 20e = 455) : le départ "
  "est profane et scripturaire à la fois. Néhémie (échanson, Néh 2 : autorisation "
  "+ lettres + bois du parc royal !) rebâtit malgré l'opposition (Guéshem l'Arabe "
  "— voir A011 : la coupe de Tell el-Maskhouta !). Murs en 52 jours (Néh 6:15) : "
  "réparations sur ruines, main-d'œuvre massive — plausible. L'attente messianique "
  "(Lc 3:15) : le comput dans les têtes. Le voile (Mt 27:51) : Dieu déchire « de "
  "haut en bas ». Corneille (Ac 10, 36) : la 70e semaine s'achève sur un centurion."
 ),
 geo=(
  "Babylone (Daniel prie en exil) → Jérusalem (la parole : « places et fossé ») → "
  "le Jourdain (29 : baptême — voir F015) → Césarée (36 : Corneille — voir C012) → "
  "le Temple (voile 33, ruine 70 — voir B007). La 70e semaine est un itinéraire : "
  "Jourdain, Galilée, Golgotha, Césarée."
 ),
 sci=(
  "Le comput : 69 × 7 = 483 ; 455 av. → 1 av. = 454 ans (pas d'an 0 — signalé, "
  "intégré) ; + 29 = 483 — l'arithmétique tombe sur le baptême. Semaines d'années : "
  "le principe est dans la Loi (année sabbatique tous les 7 ans : Ex 23:10-11). "
  "« 52 jours » (Néh 6:15) : faisable en réparations. La méthode est "
  "reproductible : départ profane (474/455), durée scripturaire (483), arrivée "
  "évangélique (29)."
 ),
 limites=(
  "« Saint des saints » (9:24) : application exacte renvoyée aux publications. "
  "70 annoncée mais non datée : dit, pas caché. Le détail des 7 semaines "
  "(455-406) est résumé (exhaustivité renvoyée). « Alliance forte » : "
  "compréhension citée (faveur aux Juifs). Pas d'an 0 : intégré au calcul, "
  "signalé."
 ),
 tl=[("538", "Vision : Gabriel"), ("455", "Parole : Néhémie"), ("406", "Ville rebâtie"), ("29", "Messie"),
     ("33", "Moitié : retranché"), ("36", "Corneille"), ("70", "Non datée")],
 src=[("Sauvés d'une génération méchante (la 70e semaine, 29-36)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1995804"),
      ("Daniel, un authentique livre de prophéties (schéma 455/29/33/36)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986721"),
      ("Daniel 9 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/9"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F011_semaines.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F012", titre="Les 430 ans — jour pour jour, de l'Euphrate au Sinaï",
 ref="Genèse 15:13-18 ; Exode 12:40-41 ; Galates 3:17 ; Genèse 12:4 ; Exode 6:16-20",
 statut="Accomplie",
 cat="F", syst="Système 1943/1513",
 reg="Registre : Genèse — P006 (15:13-14), P007 (15:16), P008 (15:18-21) ; Ex 12:40-41 et Ga 3:17 sans entrée (C8)",
 texte=[
  "« Tes descendants seront étrangers dans un pays qui ne sera pas à eux ; on "
  "les asservira et on les affligera pendant 400 ans. Mais je jugerai la nation "
  "qu'ils serviront, et après ils sortiront avec de grands biens. » (Gn 15:13-14)",
  "« À la quatrième génération, ils reviendront ici, car l'iniquité des Amorites "
  "n'est pas encore à son comble. » (Gn 15:16)",
  "« Le séjour des Israélites en Égypte et au pays de Canaan fut de 430 ans. "
  "Et au bout des 430 ans, en ce jour-là même, toutes les armées de Jéhovah "
  "sortirent d'Égypte. » (Ex 12:40-41)",
  "« La Loi, venue 430 ans après, n'annule pas l'alliance validée par Dieu. » "
  "(Ga 3:17 — Paul tranche)",
 ],
 contexte=(
  "Entre les morceaux (Gn 15:9-17) : animaux partagés, vautours chassés, « profonde "
  "ténèbre », four fumant et torche passant SEULS entre les moitiés — l'alliance "
  "unilatérale : Dieu s'engage seul. Abraham sans enfant (Éliézer héritier ?, "
  "15:2-3) ; « compte les étoiles » (15:5) ; « il crut, et ce lui fut compté "
  "comme justice » (15:6 — Rm 4, Ga 3:6, Jc 2:23 : le verset de la justification !). "
  "1943 : Abraham, 75 ans (Gn 12:4), traverse l'Euphrate — l'alliance entre en "
  "vigueur, les 430 ans commencent."
 ),
 explication=(
  "430 ans : Canaan + Égypte — les Septante (« en Égypte ET au pays de Canaan ») "
  "et le Pentateuque samaritain l'attestent ; le texte massorétique dit « en "
  "Égypte » seul — les deux leçons sont données (voir Limites) ; Paul tranche : "
  "depuis l'alliance validée (1943) jusqu'à la Loi (1513) = 430. « En ce jour-là "
  "même » (Ex 12:41) : au jour près — 430 ans jour pour jour ! 400 ans "
  "d'affliction : depuis le sevrage d'Isaac (~1913) — Ismaël « persécute » "
  "(Ga 4:29 : « celui qui était né selon la chair persécutait ») → 1913-1513 "
  "= 400. Quatrième génération : Lévi → Qehath → Amram → Moïse (Ex 6:16-20 — "
  "quatre noms !). « L'iniquité des Amorites pas à son comble » (15:16) : Dieu "
  "attend quatre siècles avant de juger Canaan — la patience comme justice. "
  "« Grands biens » (15:14) : « ils dépouillèrent les Égyptiens » (Ex 12:36 — "
  "or, argent, vêtements : le salaire de l'esclavage !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1943 (Euphrate franchi, alliance en "
  "vigueur) → 430 ans → 1513 (Exode, puis Sinaï : la Loi) ; moitié-moitié : "
  "215 ans en Canaan (1943-1728), 215 en Égypte (1728-1513) — Jacob entre à 130 "
  "ans (Gn 47:9), né en 1858 (Isaac 1918 + 60) : 1858 − 130 = 1728 — la symétrie "
  "se vérifie ! 400 ans d'affliction (1913 → 1513) ; 4 générations (Lévi-Moïse). "
  "« Jour pour jour » : l'exactitude divine, pas l'à-peu-près."
 ),
 accomplissement=[
  ("1943 av. n. è.", "L'Euphrate franchi (75 ans) ; alliance en vigueur ; départ des 430 ans"),
  ("1918 av. n. è.", "Isaac (1943 − 25) — point de départ des ~450 ans (voir F014)"),
  ("1913 av. n. è. env.", "Sevrage ; persécution d'Ismaël : début des 400 ans (Ga 4:29)"),
  ("1728 av. n. è.", "Jacob (130 ans) entre en Égypte : 215 + 215"),
  ("1513 av. n. è.", "L'Exode « en ce jour-là même » ; Sinaï : la Loi — fin des 430 ans"),
 ],
 hist=(
  "Les Septante (Alexandrie, IIIe-IIe s. av.) avaient le problème et la solution : "
  "« en Égypte et en Canaan » ; le Pentateuque samaritain confirme — double "
  "attestation. Paul (Ga 3:17) tranche en juriste : 430 ans entre deux alliances. "
  "« Dépouillèrent les Égyptiens » (Ex 12:35-36) : or, argent, vêtements réclamés "
  "et obtenus — 15:14 s'accomplit aux portes. Le rite des morceaux (Gn 15) a ses "
  "parallèles proche-orientaux (traités : passer entre les parts = « ainsi à "
  "qui rompra ») — ici, Dieu seul passe."
 ),
 geo=(
  "Ur → Harran → l'Euphrate (1943 : le fleuve franchi !) → Sichem (Moré : 1re "
  "apparition en Canaan, Gn 12:6-7) → Canaan (215 ans) → l'Égypte (Jacob, 1728 ; "
  "215 ans : Goshen) → la mer Rouge (1513 : sortie). Du grand fleuve à la mer : "
  "430 ans d'itinéraire. Sichem (48 km au nord de Jérusalem) : le premier autel."
 ),
 sci=(
  "215 + 215 = 430 : la symétrie se calcule (1943-1728 ; 1728-1513 — Jacob : "
  "1858 − 130 = 1728). Textologie : trois leçons en tableau — massorétique "
  "(« en Égypte »), Septante et samaritain (« en Canaan et en Égypte ») ; "
  "Galates 3:17 arbitre. Généalogies : Lévi 137 ans, Qehath 133, Amram 137 "
  "(Ex 6) — quatre générations pour 215 ans d'Égypte : les longévités portent "
  "la période."
 ),
 limites=(
  "Exode 12:40-41 et Galates 3:17 sans entrée au registre (C8). Texte massorétique "
  "contre Septante+samaritain : les deux leçons données, Paul arbitre. 1913 "
  "(sevrage) : déduit, « environ ». 215+215 : reconstitution généalogique "
  "(système 1943/1513). Les longévités (Ex 6) : citées, non débattues."
 ),
 tl=[("1943", "Euphrate : alliance"), ("1918", "Isaac"), ("1913 env.", "400 ans"), ("1728", "Égypte"),
     ("1513", "« Ce jour-là même »")],
 src=[("Comment situer les événements dans le cours du temps (1943, tableau)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990130"),
      ("Alliance — Étude perspicace (LXX : Égypte et Canaan)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011034"),
      ("Abraham — Étude perspicace (400 ans d'affliction)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000060"),
      ("Exode 12 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/12")],
 img="images/prophe_F012_430.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F013", titre="Un jour pour un an — la clé que Dieu donne lui-même",
 ref="Nombres 14:34 ; Ézéchiel 4:4-6 ; Daniel 9:24 (application, voir F011) ; Luc 21:24 (voir B009)",
 statut="Accomplie (principe + applications)",
 cat="F", syst="Système 1513/1473 (Nb) · 617/613 (Éz)",
 reg="Registre : Nombres — P051 (14:26-35) ; Ézéchiel — P304 (4:1-8), P305 (4:9-17)",
 texte=[
  "« De même que vous avez mis 40 jours à explorer le pays, vous porterez vos "
  "fautes 40 ans — une année pour chaque jour. » (Nb 14:34)",
  "« Couche-toi sur le côté gauche 390 jours, puis sur le côté droit 40 jours : "
  "je t'impose un jour pour chaque année. » (Éz 4:4-6)",
  "« Soixante-dix semaines ont été fixées. » (Dn 9:24 — 490 ans : la clé "
  "appliquée, voir F011)",
  "« Jérusalem sera foulée jusqu'à ce que les temps des nations s'accomplissent. » "
  "(Lc 21:24 — 2 520 ans : la clé appliquée, voir B009)",
 ],
 contexte=(
  "Kadesh (~1512, 2e année de l'Exode) : 12 espions, 40 jours (Nb 13:25 — Hébron, "
  "Éshkol et sa grappe à deux hommes !), 10 découragent, Josué et Caleb tiennent ; "
  "le peuple veut retourner en Égypte ; Moïse intercède ; pardon + peine : "
  "40 ans — « jusqu'à ce que vos cadavres tombent » (14:33), sauf les deux "
  "fidèles. Tel-Abib, au Kébar (613, 5e année de l'exil) : Ézéchiel mime le siège "
  "sur une brique (4:1-3 — avec un mur de fer, une poêle, entre lui et la ville !), "
  "couché 390 + 40 jours, rations pesées, eau mesurée, combustible négocié "
  "(4:12-15 : excréments → bouse de vache — Dieu cède sur le combustible, pas sur "
  "le message !). La Bible en gestes."
 ),
 explication=(
  "Le principe est donné DEUX fois, explicitement : « une année pour chaque jour » "
  "(Nb 14:34), « un jour pour chaque année » (Éz 4:6) — Dieu fournit LUI-MÊME la "
  "clé de lecture. Nombres : la peine épouse la faute — 40 jours d'exploration "
  "→ 40 ans (1512-1473 : Kadesh → Jourdain). Ézéchiel : le corps du prophète = "
  "le calendrier du jugement — 390 (Israël) + 40 (Juda) = 430 jours-années… le "
  "même nombre que F012 ! (coïncidence signalée, pas exploitée — voir Limites). "
  "« Porter l'iniquité » (nasa avon) : le vocabulaire — celui du Serviteur "
  "(Is 53 !). La clé appliquée : Daniel 9 (70 semaines = 490 ans — F011), "
  "Daniel 4 / 7:25 / 12:7 (temps = années → 2 520 — B009), Révélation (1 260 jours "
  "— renvoi H/I)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « en certaines occasions, Jéhovah "
  "emploie le mot jour pour parler d'une année » (Nb 14:34 ; Éz 4:6) — le "
  "principe n'est pas une invention de commentateurs, l'Écriture s'auto-interprète. "
  "Nombres 14 : usage pénal (la génération sort, Josué et Caleb entrent). "
  "Ézéchiel 4 : usage représentatif (le mime-calendrier). Daniel : usage "
  "prophétique (F011, B009). Trois usages, une clé."
 ),
 accomplissement=[
  ("1512 av. n. è. env.", "Kadesh : 40 jours d'exploration (Nb 13:25)"),
  ("1512-1473 av. n. è.", "40 ans : « une année pour chaque jour » — le Jourdain"),
  ("613 av. n. è.", "Tel-Abib : 390 + 40 jours couché (calendrier renvoyé)"),
  ("455-36 de n. è.", "Daniel 9 : 70 semaines = 490 ans (voir F011)"),
  ("607-1914 de n. è.", "Sept temps = 2 520 ans (voir B009)"),
 ],
 hist=(
  "Kadesh-Barnéa (oasis du nord-Sinaï, Aïn el-Qudeirat — identification usuelle) : "
  "la porte de Canaan. Tel-Abib (« colline des épis », Éz 3:15) : le nom repris "
  "par Tel-Aviv moderne (via la traduction hébraïque d'Altneuland) — fait de "
  "toponymie, pas prophétie ! La brique gravée : les Babyloniens écrivent sur "
  "briques — Ézéchiel mime avec le matériau local. Les rations (20 sicles ≈ 230 g, "
  "1/6 de hin ≈ 0,6 L — Éz 4:9-11) : rations de siège — le prophète maigrit pour "
  "de vrai."
 ),
 geo=(
  "Kadesh → le désert (40 ans de boucle) → le Jourdain (1473) : la peine est un "
  "itinéraire. Le Kébar (Babylonie) : l'exil — Ézéchiel mime Jérusalem à 1 500 km "
  "de Jérusalem. Hébron, Éshkol (la grappe) : l'exploration en 40 jours (~400 km "
  "aller-retour — plausible). Tel-Abib → Tel-Aviv : le nom voyage."
 ),
 sci=(
  "40 jours pour ~400 km : plausible en caravane d'exploration. 390 + 40 = 430 : "
  "arithmétique exacte (application renvoyée). Rations : 20 sicles/jour (≈ 230 g "
  "de pain) + 0,6 L d'eau — sous-alimentation chronique documentée par le mime. "
  "Deux occurrences explicites du principe (Nb, Éz) : la clé est scripturaire, "
  "pas conjecturale — méthode reproductible (F011, B009)."
 ),
 limites=(
  "390 + 40 (application calendaire) : renvoyée aux publications. 430 (coïncidence "
  "avec F012) : signalée, pas exploitée. Kadesh-Barnéa : identification usuelle, "
  "non certaine. Tel-Aviv : reprise de nom moderne — pas une prophétie. Rations : "
  "ordres de grandeur (sicle, hin)."
 ),
 tl=[("1512 env.", "Kadesh : 40 jours"), ("1512-1473", "40 ans"), ("613", "Tel-Abib : 390+40"),
     ("Dn 9", "490 ans (F011)"), ("607-1914", "2 520 ans (B009)")],
 src=[("Les jours de la création, selon Dieu (Nb 14:34, Éz 4:6)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1970123"),
      ("Nombres 14 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/14"),
      ("Ézéchiel 4 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/4"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F013_jouran.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F014", titre="Les 480 ans — le Temple date l'Exode",
 ref="1 Rois 6:1 ; 1 Rois 11:42 ; Actes 13:20 ; Exode 12:40 (voir F012)",
 statut="Accomplie",
 cat="F", syst="Système 1513/1034",
 reg="Registre : 1R 6:1 et Ac 13:20 sans entrée (C8)",
 texte=[
  "« Ce fut la 480e année après la sortie d'Égypte, la 4e année du règne de "
  "Salomon, au mois de Ziv, que l'on bâtit la maison de Jéhovah. » (1R 6:1 — "
  "trois dates en un verset)",
  "« Salomon régna 40 ans à Jérusalem sur tout Israël. » (1R 11:42)",
  "« Pendant environ 450 ans, il leur donna des juges jusqu'à Samuel. » "
  "(Ac 13:20 — Paul approxime : 451 ≈ 450)",
  "« En ce jour-là même, les armées de Jéhovah sortirent. » (Ex 12:41 — le point "
  "de départ, voir F012)",
 ],
 contexte=(
  "Salomon (fils de David et Bath-Shéba, règne de 40 ans) : 4e année = 1034, mois "
  "de Ziv (2e mois — avril-mai : on commence au printemps !). Sept ans et demi "
  "de chantier (jusqu'au mois de Bul de la 11e année, 1R 6:38 : 1034 → 1027) — "
  "« ni marteau ni hache ne s'entendirent » (1R 6:7 : pierres taillées à la "
  "carrière — l'acoustique du sacré !). Hiram de Tyr fournit cèdres et artisans "
  "(1R 5 ; 7:13-14 — Tyr au service du Temple : voir F001 !). Le lieu : Moriya "
  "(2Ch 3:1 — Abraham en Gn 22 + l'aire d'Ornan en 2S 24 : triple sainteté !). "
  "Paul, à Antioche de Pisidie (Ac 13:16-22), prêche l'histoire-chiffres."
 ),
 explication=(
  "« La 480e année » — PAS « 480 ans » ! (la précision du comput : 479 ans "
  "révolus : 1513 → 1034). Triple ancrage : Exode + règne + mois — le verset le "
  "plus daté de l'Ancien Testament. « Environ 450 ans » (Ac 13:20) : Paul "
  "compte depuis la naissance d'Isaac (1918 !) jusqu'en 1467 = 451 ans ≈ 450 — "
  "« environ » : l'à-peu-près avoué. Les deux déclarations « concordent et "
  "étayent » 1513 : le Temple date l'Exode — la preuve à rebours ! « Quatrième "
  "génération » (Gn 15:16, voir F012) : au sens strict, Lévi → Moïse = 4 noms ; "
  "au sens large, les publications signalent elles-mêmes la difficulté (plus de "
  "quatre générations en 430 ans) — renvoyée (voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1 Rois 6:1 valide 1513 — on ne date "
  "pas le Temple par l'Exode, on VÉRIFIE l'Exode par le Temple (1034 + 479 = "
  "1513). Actes 13:20 confirme par Paul (~450 : 1918 → 1467). Deux témoins "
  "indépendants (le chroniqueur royal, l'apôtre en sermon), deux périodes "
  "différentes (479, ~450), un seul système : 1513."
 ),
 accomplissement=[
  ("1918 av. n. è.", "Isaac : départ des ~450 ans de Paul (voir F012)"),
  ("1513 av. n. è.", "L'Exode : départ des 479 ans (voir F012)"),
  ("1467 av. n. è.", "Fin des ~450 ans (451 ≈ 450 — juges, Samuel)"),
  ("1034 av. n. è.", "4e année de Salomon, mois de Ziv : le Temple commencé"),
  ("1027 av. n. è.", "11e année, mois de Bul : achevé — 7 ans et demi"),
 ],
 hist=(
  "Hiram de Tyr (1R 5 : alliance, cèdres ; 7:13-14 : Hiram l'artisan — père "
  "tyrien, mère de Nephtali !) : Tyr bâtit le Temple — voir F001. Ziv et Bul : "
  "les vieux noms cananéens des mois (pré-exiliques) — la langue du X e siècle. "
  "« Ni marteau ni hache » (1R 6:7) : taille en carrière, montage silencieux — "
  "technique et théologie. Paul à Antioche (Ac 13) : le sermon-chiffres devant "
  "la synagogue — l'histoire comme preuve, déjà."
 ),
 geo=(
  "Moriya (2Ch 3:1) : le mont du Temple — Gn 22 (Abraham) + 2S 24 (Ornan) + 1R 6 "
  "(Salomon) : trois couches de sainteté sur un lieu. Le Liban → Jaffa par mer "
  "(1R 5:9 : flottage des cèdres !) → Jérusalem : la logistique du chantier. Les "
  "carrières (pierre de Jérusalem, taillée hors site) : le silence vient de là."
 ),
 sci=(
  "1513 − 479 = 1034 : arithmétique exacte. 1918 − 451 = 1467 (≈ 450 : Paul "
  "arrondit — avoué). Ziv 1034 → Bul 1027 : 7 ans et demi de chantier (1R 6:1, "
  "38). Honnêteté de méthode : pas de datation absolue externe du Temple — le "
  "comput est interne-biblique plus synchronismes (rois, Tyr) — dit, pas caché "
  "(voir Limites)."
 ),
 limites=(
  "1 Rois 6:1 et Actes 13:20 sans entrée au registre (C8). « Quatrième génération » "
  "(sens large) : difficulté signalée par les publications elles-mêmes — renvoyée. "
  "Pas de datation externe absolue du Temple : comput interne + synchronismes — "
  "dit. 1034 (4e année de Salomon) : système des rois. Hiram : détail à F001."
 ),
 tl=[("1918", "Isaac : ~450 ans"), ("1513", "Exode : 479 ans"), ("1467", "Fin ~450"),
     ("1034 (Ziv)", "Temple commencé"), ("1027 (Bul)", "Achevé")],
 src=[("Chronologie (1R 6:1 : 480e année, 479 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965039"),
      ("Exode — Étude perspicace (1034, ~450 ans, 4e génération)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001458"),
      ("1 Rois 6 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/11/6"),
      ("Actes 13 — Bible d'étude, notes (Paul : ~450 ans)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/13")],
 img="images/prophe_F014_temple.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F015", titre="L'an 15 de Tibère — six témoins pour l'an 29",
 ref="Luc 3:1-3, 21-23 ; Jean 2:20 ; Daniel 9:25 (voir F011) ; Nombres 4:3 (30 ans)",
 statut="Accomplie",
 cat="F", syst="Système 29/33",
 reg="Registre : Lc 3:1 et Jn 2:20 sans entrée (C8)",
 texte=[
  "« Dans la 15e année du règne de Tibère César, quand Ponce Pilate était "
  "gouverneur de Judée, Hérode tétrarque de Galilée, Philippe son frère "
  "tétrarque d'Iturée, Lysanias tétrarque d'Abilène, sous les grands prêtres "
  "Anne et Caïphe, la déclaration de Dieu vint à Jean dans le désert. » "
  "(Lc 3:1-2 — six synchronismes)",
  "« Jésus lui-même, quand il commença, avait environ trente ans. » (Lc 3:23 — "
  "hosei : « à peu près » — Luc approxime !)",
  "« Il a fallu 46 ans pour bâtir ce temple. » (Jn 2:20 — les Juifs, 1re Pâque)",
  "« Le peuple était dans l'attente. » (Lc 3:15 — le comput de Daniel dans les "
  "têtes — voir F011)",
 ],
 contexte=(
  "Jean (fils de Zacharie et Élisabeth, six mois avant Jésus : Lc 1:26, 36 — "
  "l'Élie promis : Ml 4:5-6, voir C005 ! ; Lc 1:17) prêche « dans le désert » "
  "(3:2-3 : baptême de repentance). La 15e année : automne 28 → automne 29 — Jean "
  "commence au printemps 29, Jésus est baptisé six mois plus tard, automne 29 : "
  "Jean, né six mois avant, commence six mois avant — la symétrie ! « Environ "
  "30 ans » : l'âge lévitique du service (Nb 4:3, 23, 30 — 30 ans : l'âge légal ! "
  "Jésus commence à l'âge requis). Quatre Pâques (Jn 2:13 ; 5:1 ; 6:4 ; 11:55) : "
  "3 ans et demi (29 → 33)."
 ),
 explication=(
  "Six témoins, le faisceau le plus serré du Nouveau Testament : empereur "
  "(Tibère), gouverneur (Pilate), deux tétrarques hérodéens (Antipas, Philippe), "
  "tétrarque d'Abilène (Lysanias), deux grands prêtres (Anne, Caïphe) — Luc "
  "verrouille. 15e année : 17 août 28 → 16 août 29 (comptage sans année "
  "d'accession, depuis août 14 — co-règne de 12 discuté : voir Limites). « C'est "
  "29, et non 14, qui est considéré comme date pivot » : la Bible ne parle pas "
  "du début du règne, mais d'un événement de la 15e année. « Environ trente ans » "
  "(hosei) : Luc approxime — et 30, c'est Nombres 4. Vie de 33 ans et demi "
  "(automne 2 av. → Pâque 33) : la naissance se calcule — automne 2 avant notre "
  "ère. « 46 ans » (Jn 2:20) : chantier d'Hérode (18e année, 20/19 av. selon "
  "Josèphe) — l'ordre de grandeur converge vers la fin des années 20 "
  "(ajustement au mois : voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 29 = date pivot — Jean au printemps, "
  "Jésus à l'automne (onction : le grand temple spirituel « a commencé à remplir "
  "sa fonction en 29 » — voir B005 !). Et la convergence : Daniel 9:25 (69 "
  "semaines → 29 — voir F011) et Luc 3:1 (15e année → 29) arrivent ENSEMBLE — deux "
  "computs indépendants (prophétie vieille de six siècles, synchronismes "
  "impériaux), une seule année. « Le peuple était dans l'attente » (3:15) : "
  "l'attente vient du comput."
 ),
 accomplissement=[
  ("Automne 2 av. n. è.", "Naissance (33,5 ans avant Pâque 33)"),
  ("Automne 28 - automne 29", "15e année de Tibère : les six témoins (Lc 3:1-2)"),
  ("Printemps 29", "Jean commence (baptême de repentance)"),
  ("Automne 29", "Baptême de Jésus : Messie — 69 semaines (voir F011)"),
  ("Pâques 30-33", "« 46 ans » (30) ; 3 ans et demi ; Pâque 33"),
 ],
 hist=(
  "Tibère (19 août 14 — 16 mars 37 ; retiré à Capri dès 26/27 — l'empereur absent, "
  "Séjan à Rome). Pilate (préfet 26-36 — PIERRE DE CÉSARÉE, 1961 : « Ponce Pilate, "
  "préfet de Judée » !). Antipas (4 av. — 39 : il décapitera Jean). Philippe "
  "(4 av. — 34). Lysanias (Abilène — INSCRIPTION D'ABILA : « Lysanias le tétrarque » "
  "— la pierre qui a fait taire les critiques !). Anne (6-15 : destitué par Rome, "
  "« grand prêtre » encore pour les Juifs) et Caïphe (18-36, son gendre — OSSUAIRE "
  "DE CAÏPHE, 1990 : « Joseph fils de Caïphe » !). Trois pierres pour six noms."
 ),
 geo=(
  "Le désert de Judée (Jean) → le Jourdain (le baptême — Béthanie au-delà ? "
  "Jn 1:28) → Jérusalem (« 46 ans » : le chantier !) → Capri et Rome (l'Empire : "
  "l'autre bout du faisceau) → Abilène (Lysanias, Anti-Liban). Du fleuve à "
  "l'Empire : Luc cadre le Jourdain dans le monde."
 ),
 sci=(
  "Épigraphie : pierre de Pilate (1961), inscription de Lysanias (Abila), ossuaire "
  "de Caïphe (1990) — trois pierres, six noms, zéro faute de Luc. Computs : 15e "
  "année = 17.08.28 → 16.08.29 ; vie 33,5 ans → naissance automne 2 av. Méthode : "
  "« environ » (hosei, Lc 3:23) — Luc signale ses approximations ; les Juifs "
  "(Jn 2:20), eux, disent « 46 » sans arrondir — les deux régimes sont distingués "
  "(voir Limites)."
 ),
 limites=(
  "Luc 3:1 et Jean 2:20 sans entrée au registre (C8). Co-règne de Tibère (12) : "
  "discuté entre historiens — les publications comptent depuis 14 (signalé). "
  "« 46 ans » : ajustement au mois renvoyé (convergence : fin des années 20). "
  "« Une fête » (Jn 5:1 : Pâque supposée, pas nommée — signalé). Séjan, Capri : "
  "cadre, pas développé."
 ),
 tl=[("Aut. 2 av.", "Naissance"), ("28/29", "15e année : 6 témoins"), ("Print. 29", "Jean"),
     ("Aut. 29", "Baptême : Messie"), ("Pâques 30-33", "3,5 ans")],
 src=[("Pourquoi 29 est une date pivot (15e année de Tibère)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1991849"),
      ("Quand Jésus est-il né ? (15e année, ~30 ans, 33,5 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1979921"),
      ("Luc 3 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/3"),
      ("Jean 2 — Bible d'étude, notes (« 46 ans »)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/2")],
 img="images/prophe_F015_tibere.jpg",
))
