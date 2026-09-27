#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 8 · vague P8-9 · EX — Exode (2) : P049-P054."""
# pylint: disable=invalid-name,line-too-long

CAT = dict(
    code="EX",
    nom="Exode (2) — sabbats, désert et étoile",
    intro=("Après le catalogue des malédictions, le Lévitique annonce la jachère forcée "
           "de la terre et la porte du retour ; aux portes de Canaan, la génération de "
           "l'Exode est condamnée à mourir au désert — et c'est un devin païen, Balaam, "
           "qui, contraint par Jéhovah, bénit Israël, voit l'étoile sortir de Jacob et "
           "prononce la fin d'Amalek et l'assaut des navires de Kittim."),
    vague="P8-9",
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX049", titre="La terre jouira de ses sabbats",
    ref="Lévitique 26:34, 35, 43",
    statut="Accomplie",
    cat="EX", syst="Sabbats de la terre (dette → jachère 70 ans → retour 537)",
    reg="Registre : Lévitique — P049 (26:34, 35, 43 : la terre jouira de ses sabbats) ; accomplissement 2Ch 36:20, 21 ; Jr 25:11 ; Dn 9:2",
    texte=[
        "« ALORS la terre jouira de ses SABBATS, tous les jours de sa désolation. » (26:34 — ALORS !)",
        "« Vous serez dans le pays de vos ennemis : ALORS elle se reposera. » (26:34 — se reposera !)",
        "« Tous les jours de sa désolation elle se reposera, faute des sabbats. » (26:35 — faute des sabbats !)",
        "« La terre abandonnée jouira de ses sabbats pendant qu'elle sera désolée. » (26:43 — abandonnée !)",
        "« Et EUX agréeront le châtiment de leur faute. » (26:43 — agréeront !)",
        "« Jusqu'à ce que le pays eût JOUIR DE SES SABBATS : il se reposa 70 ANS. » (2Ch 36:21 — 70 ans !)",
        "« Tout ce pays deviendra une désolation, et ces nations serviront 70 ANS. » (Jr 25:11 — 70 ans !)",
        "« Moi, Daniel, je DISCERNAI par les livres le nombre des années : 70 ANS. » (Dn 9:2 — discerna !)",
    ],
    contexte=(
        "Sinaï, 1513 — au cœur des malédictions (EX048), une clause saisissante : la "
        "terre elle-même a une créance. La Loi ordonnait l'année sabbatique tous les "
        "7 ans — « le pays observera un sabbat pour Jéhovah » (Lv 25:2-5) : pas de "
        "semailles, pas de taille de vigne, la pousse spontanée pour les pauvres et "
        "les bêtes. Or Israël multipliant les violations, les sabbats non observés "
        "s'accumulent comme une dette — et Jéhovah annonce qu'Il la recouvrera par "
        "une jachère forcée : la désolation. « ALORS (az) » (26:34) : l'adverbe du "
        "basculement — quand le peuple partira en exil, la terre entrera en sabbat. "
        "La punition du peuple est le repos du sol : un seul événement, deux "
        "bénéficiaires inverses."
    ),
    explication=(
        "« JOUIRA (tirtseh) » (26:34, 35, 43) : le verbe ratsah — agréer, prendre "
        "plaisir, mais aussi S'ACQUITTER, solder : la terre « agréera » ses sabbats "
        "comme on agrée un paiement — la jachère solde l'arriéré. Le même verbe "
        "revient au v.43 pour le peuple — « ils agréeront (yirtsu) le châtiment » : "
        "parallèle calculé, la terre et le peuple soldent chacun leur compte, l'une "
        "en repos, l'autre en exil. « Tous les jours de sa DÉSOLATION (shammah) » "
        "(26:34) : le mot des villes rasées (cf. EX048, 26:31-33) — la désolation "
        "n'est pas seulement ruine, elle est sabbat imposé. « FAUTE DES sabbats où "
        "vous vous reposiez quand vous habitiez sur elle » (26:35) : la dette est "
        "nommée — les sabbats que vous n'avez PAS gardés. Et le v.43 précise le "
        "mécanisme : « la terre abandonnée (ne'ezavah)… pendant que vous serez dans "
        "le pays de vos ennemis » — l'exil du peuple EST le sabbat de la terre."
    ),
    interpretation=(
        "2 CHRONIQUES 36:20-21 (P049) : le bilan inspiré — « il emmena captifs à "
        "Babylone… jusqu'à ce que le pays eût joui de ses sabbats ; tous les jours "
        "de la désolation il se reposa, JUSQU'À L'ACCOMPLISSEMENT DE 70 ANS » : le "
        "chroniqueur cite la prophétie en la déclarant accomplie — « afin que "
        "s'accomplît la parole de Jéhovah par Jérémie ». JÉRÉMIE 25:11 (P049) : le "
        "chiffre, un siècle avant — « tout ce pays deviendra une solitude, une "
        "désolation, et ces nations serviront le roi de Babylone 70 ANS » : "
        "Jérémie date la jachère. DANIEL 9:2 (P049) : le lecteur de la prophétie — "
        "« moi, Daniel, je discernais (binoti) par les livres le nombre des années… "
        "70 ans » : en exil, Daniel CALCULE sur Jérémie, et sa prière de confession "
        "(9:3-19) déclenche la suite (9:20-27). Chaîne complète : Lévitique annonce "
        "le principe, Jérémie chiffre, les Chroniques constatent, Daniel compte — "
        "quatre livres, une seule dette soldée."
    ),
    hist=(
        "607 AV. N. È. (datation de l'organisation) : chute de Jérusalem, le pays "
        "se vide — « il ne resta que les plus pauvres pour être vignerons et "
        "laboureurs » (2R 25:12 : une poignée, pas une agriculture). 537 AV. N. È. "
        ": les exilés sont de retour pour l'autel (Esd 3:1-6) — 70 ans après 607, "
        "« la plupart des spécialistes admettent » le retour en 537 (2011736). Le "
        "canon de Ptolémée et les historiens classiques proposent d'autres dates, "
        "mais « la fiabilité de leurs écrits suscite des doutes sérieux » "
        "(2011736) — la chronologie biblique tient par ses amarres internes "
        "(Cyrus 539, Darius, Artaxerxès 455). Le cylindre de Cyrus (539, "
        "proclamation de retour des cultes) illustre la politique perse du retour — "
        "le décret pour les Juifs (Esd 1:1-4) s'inscrit dans une pratique impériale "
        "attestée."
    ),
    geo=(
        "Le PAYS DE JUDA : collines cultivées en terrasses, vignes et oliviers — "
        "70 ans sans taille ni semailles : les terrasses s'effondrent, la garrigue "
        "reprend, les bêtes sauvages reviennent (« je rendrai le pays désolé, et "
        "vos ennemis s'en étonneront », 26:32). JÉRUSALEM : ville rasée, temple "
        "brûlé — le sabbat du pays a pour capitale une ruine. BABYLONE : le pays "
        "« de vos ennemis » (26:34) — les exilés y cultivent une terre étrangère "
        "(Jr 29:5 : « bâtissez des maisons, plantez des jardins ») pendant que la "
        "leur se repose : le paradoxe géographique de la prophétie — travailler "
        "ailleurs pour que le pays se repose ici. Le RETOUR (Esd 2) : caravanes de "
        "Babylone à Jérusalem, ~1 500 km — la jachère prend fin quand les "
        "laboureurs reviennent."
    ),
    sci=(
        "L'AGRONOMIE DE LA JACHÈRE : laisser la terre au repos restaure sa "
        "fertilité — les sols cultivés sans relâche s'épuisent (azote, matière "
        "organique), la jachère les régénère ; la Loi imposait tous les 7 ans ce "
        "que l'agronomie moderne redécouvre (rotation, repos des sols). La "
        "prophétie fait de cette sagesse agricole une horloge judiciaire : 70 ans "
        "de repos forcé — la plus longue jachère datée de l'histoire du Levant. "
        "L'ARITHMÉTIQUE : 607 − 70 = 537 — trois dates solidaires (chute, durée, "
        "retour), vérifiables par recoupement (Cyrus 539 entre les deux : la chute "
        "de Babylone précède de 2 ans la fin des 70 ans, exactement le temps du "
        "décret et du voyage). Le CHIFFRE 70 : une vie humaine (« les jours de nos "
        "années : 70 ans », Ps 90:10) — toute une génération naît et meurt en exil ; "
        "nul de ceux qui partirent adultes ne revient jeune : la dette se paie en "
        "durée d'une vie."
    ),
    schema=(
        "LA DETTE SOLDÉE : sabbats violés (dette) → exil du peuple (paiement) = "
        "repos de la terre (créance honorée). Trois témoins : Lévitique (le "
        "principe) → Jérémie (le chiffre : 70) → Chroniques (le constat : soldé). "
        "Et un lecteur : Daniel (le calcul : binoti — je discernai)."
    ),
    limites=(
        "La Bible NE DIT PAS combien de sabbats furent violés : le calcul « 70 "
        "sabbats manqués = 490 ans » est une spéculation de commentateurs, jamais "
        "affirmée par le texte — la fiche ne la reprend pas. 2 Rois 25:12 (les "
        "pauvres restés) ne contredit pas la désolation : une poignée de vignerons "
        "n'est pas une agriculture nationale. La date de 607 suit la chronologie "
        "de l'organisation ; la chronologie profane courante place la chute en "
        "587/586 — l'écart est signalé, non tranché ici (voir 2011736). Enfin, le "
        "« souvenir » de l'alliance (v.42, 44-45) appartient à la fiche suivante "
        "(EX050) : ne pas mélanger la dette et la grâce."
    ),
    accomplissement=[(("1513 (Sinaï)", "La terre jouira de ses sabbats (26:34-35, 43)")),
        (("~627-607", "Jérémie chiffre : 70 ans (Jr 25:11)")),
        (("607", "Désolation : le sabbat forcé commence (2R 25)")),
        (("~539", "Daniel discerne les 70 ans par les livres (Dn 9:2)")),
        (("537", "Retour : la jachère prend fin (Esd 1-3 ; 2Ch 36:21 soldé)"))],
    tl=[(("1513", "Dette annoncée")),
        (("627", "70 ans chiffrés")),
        (("607", "Jachère forcée")),
        (("539", "Daniel calcule")),
        (("537", "Retour, dette soldée"))],
    src=[("Quand l'ancienne Jérusalem a-t-elle été détruite ? (70 ans, sabbats, 607→537)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
        ("Sabbat — Étude perspicace (années sabbatiques, désolation 70 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013688"),
        ("Lévitique 26 — Bible d'étude (notes 26:34-43)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/3/26")],
    img="images/prophe_EX049_sabbats.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX050", titre="Confession, retour et souvenir de l'alliance",
    ref="Lévitique 26:40-45",
    statut="Accomplie",
    cat="EX", syst="Retour promis (confession → souvenir → Cyrus 537)",
    reg="Registre : Lévitique — P050 (26:40-45 : confession, retour, souvenir de l'alliance) ; accomplissement Esd 1:1-4 ; Né 1:8-9",
    texte=[
        "« Ils CONFESSERONT leur faute et la faute de leurs pères. » (26:40 — confesseront !)",
        "« Leur CŒUR INCIRCONCIS S'HUMILIERA. » (26:41 — s'humiliera !)",
        "« ALORS je me souviendrai de mon alliance avec JACOB… ISAAC… ABRAHAM. » (26:42 — ALORS !)",
        "« Je ne les REJETTERAI pas, je ne les aurai pas en DÉGOÛT pour les EXTERMINER. » (26:44 — pas exterminer !)",
        "« Car je suis Jéhovah leur Dieu. » (26:44 — leur Dieu !)",
        "« Je me souviendrai de l'ALLIANCE DES ANCÊTRES, que j'ai fait sortir d'Égypte. » (26:45 — ancêtres !)",
        "« La PREMIÈRE ANNÉE de Cyrus… afin que s'accomplît la parole : Jéhovah RÉVEILLA son esprit. » (Esd 1:1 — réveilla !)",
        "« Si vous revenez à moi… je vous RASSEMBLERAI, même du BOUT DES CIEUX. » (Né 1:8-9 — bout des cieux !)",
    ],
    contexte=(
        "Sinaï, 1513 — aussitôt la dette soldée (EX049), la porte s'ouvre : les "
        "6 derniers versets du chapitre 26 sont la sortie de secours gravée DANS "
        "le code pénal. La structure est un chiasme : CONFESSION du peuple "
        "(26:40-41) → SOUVENIR de Dieu (26:42) → non-rejet garanti (26:44) → "
        "SOUVENIR de Dieu (26:45). Le v.43 fait charnière (la terre jouit — EX049) "
        "entre le châtiment et le retour. Notez le « EUX » du v.40 : « ils "
        "confesseront » — après des versets de « je » divin (je frapperai, "
        "j'enverrai), le sujet change : le retour commence par une parole HUMAINE, "
        "la confession. Dieu a tout dit ; il attend un mot : « nous avons péché »."
    ),
    explication=(
        "« CŒUR INCIRCONCIS (levav he'arel) » (26:41) : le cœur a un prépuce — "
        "image-choc : l'organe de l'écoute est bouché ; « s'humiliera (yikkana') » "
        ": le verbe de la soumission forcée (cf. EX042, les dieux jugés) — "
        "l'humiliation précède le souvenir, jamais l'inverse. « Je me SOUVIENDRAI "
        "(zakhar) » (26:42, 45) : zakhar n'est pas un rappel de mémoire — c'est "
        "l'acte qui suit la mémoire : se souvenir = intervenir (cf. Gn 8:1, Dieu "
        "« se souvint » de Noé — et le vent souffla ; EX038, paqod). L'ORDRE "
        "INVERSÉ — « Jacob, Isaac, Abraham » (26:42) : remontée généalogique, du "
        "fils au père — comme si Dieu feuilletait l'alliance à rebours jusqu'à "
        "l'original. « Je ne les aurai pas en DÉGOÛT (lo ghe'altim) » (26:44) : "
        "le verbe de la nausée (cf. 26:11, 15, 30 — le même verbe pour Israël "
        "rejetant Dieu !) : Dieu refuse le dégoût symétrique — Il ne vomit pas "
        "son peuple. DEUX alliances (26:42, 45) : celle des PATRIARCHES (le "
        "serment) et celle des ANCÊTRES sortis d'Égypte (l'Exode) — le retour "
        "honore les deux contrats à la fois."
    ),
    interpretation=(
        "ESDRAS 1:1-4 (P050) : « la PREMIÈRE ANNÉE de Cyrus, roi de Perse, afin que "
        "s'accomplît la parole de Jéhovah par Jérémie, Jéhovah RÉVEILLA (he'ir) "
        "l'esprit de Cyrus » — le verbe du réveil : Dieu réveille un païen comme "
        "on réveille un dormeur ; le décret suit : « qu'il monte à Jérusalem… et "
        "qu'il bâtisse ». Le retour n'est pas une permission, c'est une "
        "résurrection impériale. NÉHÉMIE 1:8-9 (P050) : Néhémie PLAIDE la "
        "prophétie devant Dieu — « souviens-toi de la parole… si vous revenez à "
        "moi, je vous rassemblerai, même si vos dispersés sont au BOUT DES CIEUX "
        "» : la prière cite le contrat (Dt 30:1-4, écho de Lv 26) et Dieu paie — "
        "lettres royales, escorte, bois (Né 2:7-8). DANIEL 9 (filigrane) : la "
        "confession-modèle — « nous avons péché » (9:5, 8, 11, 15) : Daniel "
        "prononce le mot attendu depuis Lv 26:40, et l'ange Gabriel arrive « "
        "pendant que je parlais encore » (9:21) : le souvenir suit la confession "
        "en temps réel."
    ),
    hist=(
        "539 : Cyrus prend Babylone (16 Tishri) — l'empire qui déporta tombe. 537 "
        ": décret de retour, 1re caravane — Zorobabel (prince davidique) et Josué "
        "fils de Yehotsadaq (grand prêtre) : les deux oints, couronne et tiare "
        "côte à côte. L'AUTEL d'abord (Esd 3:1-6), le TEMPLE ensuite (achevé 515, "
        "6e année de Darius, Esd 6:15) : le culte précède la pierre. VAGUES du "
        "retour : 537 (Zorobabel, ~50 000 — Esd 2:64-65 : 42 360 + 7 337 "
        "serviteurs + 200 chantres), 467 (Esdras, le scribe), 455 (Néhémie, la "
        "muraille en 52 jours — Né 6:15). Le cylindre de Cyrus atteste la "
        "politique perse de restauration des cultes locaux — le décret biblique "
        "s'inscrit dans une pratique impériale documentée. « L'Éternel réveilla "
        "l'esprit de Cyrus » (2Ch 36:22) — Esdras relie explicitement la fin des "
        "70 ans au décret (2011736)."
    ),
    geo=(
        "BABYLONE → JÉRUSALEM : ~1 500 km par le Croissant fertile (remontée de "
        "l'Euphrate, traversée de la Syrie, descente par Damas) — Esdras met "
        "4 mois (1er mois au 5e, Esd 7:8-9), caravane avec enfants, trésor et "
        "gardes jeûnés (Esd 8:21-23 : « j'eus honte de demander une escorte »). "
        "Les « BOUTS DES CIEUX » (Né 1:9) : les exilés sont dispersés dans tout "
        "l'empire — Suse (Néhémie échanson), Babylone, l'Égypte (Éléphantine : "
        "garnison juive avec temple, papyri araméens — la dispersion est "
        "archéologiquement attestée). JÉRUSALEM 537 : ruines depuis 70 ans — on "
        "rebâtit l'autel AVANT les maisons ; la muraille attendra 455 (Néhémie) : "
        "le retour tient en trois chantiers — autel (culte), temple (présence), "
        "muraille (sécurité)."
    ),
    sci=(
        "LA COMPTABILITÉ D'ESDRAS 2 : 42 360 Israélites + 7 337 serviteurs + 200 "
        "chantres + 736 chevaux + 245 mulets + 435 chameaux + 6 720 ânes — un "
        "recensement chiffré au détail près, avec noms de familles et totaux "
        "partiels : la marque d'une administration réelle, pas d'un récit "
        "légendaire (les légendes arrondissent, les scribes comptent). La "
        "DIPLOMATIQUE PERSÉ : les décrets cités en araméen officiel (Esd 4-6 : "
        "mémoires de cour, lettres de satrapes, rescrits de Darius) portent les "
        "formules de la chancellerie achéménide — langue, protocole et procédure "
        "conformes à ce que l'épigraphie perse atteste. La DÉMOGRAPHIE : 50 000 "
        "retournants sur une population exilée bien plus nombreuse — la plupart "
        "RESTENT (Esther, Mardochée, Néhémie d'abord) : le retour est un reste, "
        "exactement comme annoncé (« le reste reviendra », Is 10:21)."
    ),
    schema=(
        "LE CONTRAT EN 4 TEMPS : confession humaine (« nous avons péché ») → "
        "humiliation (cœur incirconcis soumis) → SOUVENIR divin (zakhar = "
        "intervenir) → retour impérial (Cyrus réveillé). Deux alliances honorées "
        "d'un coup : les patriarches (le serment) + l'Exode (la sortie). « Je ne "
        "les exterminerai pas » (26:44) : le plancher garanti sous le jugement."
    ),
    limites=(
        "« Je me souviendrai » n'implique PAS que Dieu oublie puis se rappelle : "
        "anthropopathisme — le souvenir divin, c'est l'intervention, non la "
        "mémoire retrouvée. La promesse ne garantit pas l'absence de TOUT jugement "
        "futur : 70 de n. è. (Titus) frappera encore Jérusalem — Lv 26:40-45 "
        "vise le retour de Babylone, pas une immunité perpétuelle. Ne pas "
        "confondre les alliances : 26:42 (patriarches) et 26:45 (sortie d'Égypte) "
        "sont deux contrats distincts, honorés ensemble. Enfin, le décret de "
        "Cyrus (Esd 1) autorise le retour ET le temple : réduire le retour à un "
        "rapatriement civil, c'est manquer son centre — l'autel rebâti avant les "
        "maisons."
    ),
    accomplissement=[(("1513 (Sinaï)", "Confession → souvenir → non-extermination (26:40-45)")),
        (("~539", "Daniel confesse : « nous avons péché » (Dn 9:5)")),
        (("539", "Cyrus prend Babylone ; empire déportateur tombé")),
        (("537", "Décret de Cyrus : retour + temple (Esd 1:1-4)")),
        (("467 / 455", "Esdras puis Néhémie : « bout des cieux » rassemblé (Né 1:8-9)"))],
    tl=[(("1513", "Porte du retour")),
        (("539", "Confession + chute")),
        (("537", "Décret de Cyrus")),
        (("515", "Temple achevé")),
        (("455", "Muraille (52 j)"))],
    src=[("Quand l'ancienne Jérusalem a-t-elle été détruite ? (Cyrus, retour 537)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
        ("Esdras 1 — Bible d'étude (décret de Cyrus, 1re année)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/15/1"),
        ("Néhémie 1 — Bible d'étude (8-9 : rassemblés du bout des cieux)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/16/1")],
    img="images/prophe_EX050_retour.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX051", titre="Quarante ans : la génération mourra au désert",
    ref="Nombres 14:26-35",
    statut="Accomplie",
    cat="EX", syst="Jugement de Kadès (40 jours → 40 ans → 2e recensement)",
    reg="Registre : Nombres — P051 (14:26-35 : 40 ans, la génération mourra au désert) ; accomplissement Nb 26:63-65 ; 32:10-13 ; Dt 2:14",
    texte=[
        "« JUSQU'À QUAND cette méchante assemblée murmurera-t-elle contre moi ? » (14:27 — jusqu'à quand !)",
        "« Aussi vrai que je suis VIVANT… je vous ferai AINSI QUE VOUS AVEZ PARLÉ. » (14:28 — ainsi !)",
        "« Vos CADAVRES tomberont dans ce désert. » (14:29 — cadavres !)",
        "« Tous les RECENSÉS, depuis 20 ANS et au-dessus, qui avez murmuré. » (14:29 — 20 ans !)",
        "« Vos fils seront NOMADES 40 ANS, et porteront vos infidélités. » (14:33 — 40 ans !)",
        "« UNE ANNÉE POUR CHAQUE JOUR : 40 jours → 40 ans. » (14:34 — année pour jour !)",
        "« Vous connaîtrez ce que c'est que MON OPPOSITION. » (14:34 — mon opposition !)",
        "« AUCUN d'eux ne restait… sauf CALEB et JOSUÉ. » (26:65 — aucun !)",
        "« Le temps que nous mîmes de Kadès au Zéred : 38 ANS. » (Dt 2:14 — 38 ans !)",
    ],
    contexte=(
        "Kadès-Barnéa, été ~1512 (2e année après l'Exode) : les 12 espions "
        "reviennent après 40 jours (13:25) — 10 sèment la panique (« nous étions "
        "comme des sauterelles », 13:33), 2 tiennent bon (Caleb : « montons ! », "
        "13:30 ; Josué joint sa voix, 14:6-9). Le peuple veut LAPIDER Moïse, "
        "Aaron, Josué et Caleb (14:10) et SE DONNER UN CHEF POUR RETOURNER EN "
        "ÉGYPTE (14:4) : la rébellion comble — préférer les chaînes au lait et au "
        "miel. La gloire de Jéhovah paraît (14:10), Moïse intercède (14:13-19 — "
        "« pardonne ! »), Dieu pardonne LA DESTRUCTION IMMÉDIATE mais prononce "
        "LE JUGEMENT DIFFÉRÉ : ils vivront — et mourront au désert. Le pardon "
        "épargne le châtiment instantané, pas les conséquences : pardonnés, mais "
        "condamnés à errer."
    ),
    explication=(
        "« JE VOUS FERAI AINSI QUE VOUS AVEZ PARLÉ » (14:28) : le talion verbal — "
        "ils avaient dit « si seulement nous étions morts dans ce désert ! » "
        "(14:2) : Dieu exauce la malédiction qu'ils se sont jetée — « aussi vrai "
        "que je suis vivant (hay ani) » : serment sur la vie divine, irrévocable. "
        "« UNE ANNÉE POUR CHAQUE JOUR (shanah layyom) » (14:34) : la proportion "
        "judiciaire — 40 jours d'exploration méprisée = 40 ans de désert ; le "
        "temps du mépris devient le temps de la peine, multiplié par 365. « MON "
        "OPPOSITION (tenu'ati) » (14:34) : terme RARE (rupture, aliénation) — ils "
        "connaîtront ce que coûte d'avoir Dieu CONTRE soi après L'avoir eu POUR "
        "soi. « Depuis 20 ANS et au-dessus » (14:29) : l'âge du recensement "
        "militaire (Nb 1:3) — l'armée qui refusa de combattre mourra sans "
        "combattre ; les ENFANTS (« vos petits, dont vous disiez qu'ils seraient "
        "une proie », 14:31) entreront : ceux qu'on disait perdus sont les élus. "
        "DT 2:14 — « 38 ANS de Kadès au Zéred » : pas de contradiction — 40 ans "
        "depuis l'EXODE (1513→1473), 38 depuis le DÉCRET de Kadès : deux points "
        "de départ, une seule arrivée."
    ),
    interpretation=(
        "NOMBRES 26:63-65 (P051) : le procès-verbal d'exécution — « parmi eux il "
        "n'y avait AUCUN des fils d'Israël recensés par Moïse et Aaron au désert "
        "du Sinaï… car Jéhovah avait dit : ils mourront dans le désert ; et il "
        "n'en resta AUCUN, sauf Caleb et Josué » : le 2e recensement (601 730) "
        "atteste, effectif contre effectif, que la génération a été REMPLACÉE à "
        "nombre quasi égal (603 550 au 1er — Nb 1:46). NOMBRES 32:10-13 (P051) : "
        "Moïse RÉUTILISE le précédent — Ruben et Gad veulent rester en Trans-"
        "jordanie ; Moïse : « ferez-vous comme vos pères… ? Jéhovah les fit errer "
        "40 ans jusqu'à la fin de la génération » : le jugement devient "
        "jurisprudence. DEUTÉRONOME 2:14 (P051) : « jusqu'à ce que toute la "
        "génération des hommes de guerre eût disparu… comme Jéhovah le leur avait "
        "juré » : Moïse, à 120 ans, clôt le dossier — le serment de 14:28 (« "
        "aussi vrai que je suis vivant ») est soldé au dernier cadavre."
    ),
    hist=(
        "Les DEUX RECENSEMENTS encadrent le jugement : Nb 1 (Sinaï, 2e mois an 2 "
        ": 603 550 hommes 20+) → Nb 26 (plaines de Moab, an 40 : 601 730) — "
        "« aucun des dénombrés du premier n'est encore en vie, à l'exception de "
        "Josué et de Caleb » (2004565). JOSUÉ ET CALEB : survivants promis "
        "(14:30), chefs de la conquête — Caleb prend Hébron à 85 ans (Jos 14:10-12 "
        ": « donne-moi cette montagne »), Josué distribue le pays : les deux "
        "espions fidèles héritent ce que les dix lâches ont fait perdre. Les 10 "
        ": frappés de la plaie « devant Jéhovah » (14:37) — exécution immédiate "
        "des meneurs, attrition lente des suiveurs. KIBROTH-HATTAAVAH (« tombes "
        "de convoitise », Nb 11:34) : le désert devient cimetière AVANT même "
        "Kadès — le jugement de Nb 14 généralise ce que Nb 11 inaugurait."
    ),
    geo=(
        "KADÈS-BARNÉA (Aïn el-Qudeirat, Négev) : oasis aux sources abondantes, "
        "porte sud de Canaan — le décret y est prononcé à portée de vue du pays "
        "refusé : on voit Hébron depuis les hauteurs, on n'y entrera pas. Le "
        "DÉSERT DE PARAN : 38 ans d'errance entre Kadès et le Zéred (Dt 2:14) — "
        "l'itinéraire de Nb 33 jalonne 40+ campements (Rithma, Rimmon-Pérets, "
        "Libna, Rissa, Qehélatha…) : la géographie du jugement est tracée "
        "étape par étape. Le TORRENT DE ZÉRED : frontière de Moab — quand la "
        "génération est éteinte, on franchit : « alors nous passâmes le torrent "
        "de Zéred » (Dt 2:13) — le gué ne s'ouvre qu'aux morts enterrés. Les "
        "PLAINES DE MOAB : le 2e recensement s'y tient face à Jéricho (Nb 26:3) "
        "— le jugement prononcé au sud s'achève à l'est, aux portes de l'entrée."
    ),
    sci=(
        "LA DÉMOGRAPHIE DU REMPLACEMENT : 603 550 → 601 730 en 40 ans — une "
        "population maintenue à effectif constant malgré la mortalité totale des "
        "adultes : il a fallu ~600 000 naissances de garçons survivant jusqu'à "
        "20 ans en 40 ans, soit ~15 000 par an — taux compatible avec une "
        "population totale de ~2 millions (familles nombreuses, fécondité "
        "élevée). 40 ANS = UNE GÉNÉRATION : la durée biblique du renouvellement "
        "(Ps 95:10-11 : « 40 ans j'eus cette génération en dégoût » — le psaume "
        "cite Kadès). LA MANNE 40 ANS (Ex 16:35 : « jusqu'à leur arrivée ») : la "
        "logistique du jugement — Dieu nourrit pendant 40 ans ceux qu'Il a "
        "condamnés : la peine n'abolit pas la providence. L'ARCHÉOLOGIE : 40 ans "
        "de nomadisme laissent peu de traces (tentes, foyers éphémères) — "
        "l'absence de vestiges massifs est l'attente normale, non une anomalie "
        "(voir limites)."
    ),
    schema=(
        "LE MIROIR DE KADÈS : 40 JOURS d'exploration méprisée → 40 ANS de désert "
        "subi. « Si seulement nous étions morts ! » (14:2) → « vos cadavres "
        "tomberont » (14:29) : Dieu exauce la parole des murmures. Deux "
        "recensements, deux générations : 603 550 (condamnés) → 601 730 "
        "(héritiers) — le désert comme sas de remplacement."
    ),
    limites=(
        "« Il n'est précisé nulle part la façon dont ils sont morts » — mort "
        "naturelle progressive sur 40 ans, la Bible ne détaille pas : ne pas "
        "inventer de plaies annuelles. Les 38 ans (Dt 2:14) et les 40 ans (Nb "
        "14:33) ont des points de départ différents (Kadès vs Exode) : les "
        "opposer, c'est confondre deux mesures. L'itinéraire de Nb 33 ne permet "
        "pas de localiser chaque campement avec certitude — les identifications "
        "modernes (Aïn el-Qudeirat = Kadès) sont probables, non prouvées. "
        "L'absence de traces archéologiques massives ne prouve ni ne réfute : "
        "des nomades en tentes ne bâtissent pas de tells. Enfin, Moïse et Aaron "
        "meurent aussi avant l'entrée — mais pour Meriba (Nb 20:12), PAS pour "
        "Kadès : deux jugements distincts."
    ),
    accomplissement=[(("~1512 (Kadès)", "Décret : 40 ans, cadavres au désert (14:26-35)")),
        (("~1512", "Les 10 espions frappés devant Jéhovah (14:37)")),
        (("1512→1474", "38 ans de Kadès au Zéred (Dt 2:14)")),
        (("1474/1473", "2e recensement : aucun survivant sauf 2 (26:63-65)")),
        (("1473", "Entrée : les « petits » héritent (Jos 3-5)"))],
    tl=[(("1513", "Exode (an 1)")),
        (("1512", "Décret de Kadès")),
        (("1474", "Zéred : génération éteinte")),
        (("1473", "2e recensement")),
        (("1473", "Entrée en Canaan"))],
    src=[("Points marquants du livre des Nombres (40 ans, 2e recensement)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2004565"),
        ("Courageux grâce à la foi (Josué et Caleb, 40 ans promis)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2006724"),
        ("Nombres 14 — Bible d'étude (notes 14:26-35)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/14")],
    img="images/prophe_EX051_desert.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX052", titre="Dieu n'est pas un homme pour mentir ; le lion se lève",
    ref="Nombres 23:19-24",
    statut="Accomplie",
    cat="EX", syst="Oracle de Balaam 2 (Dieu parle → Dieu fait → lion)",
    reg="Registre : Nombres — P052 (23:19-24 : Dieu ne ment pas ; Israël comme un lion) ; accomplissement Nb 24:1-9 ; 2S 8:1-14",
    texte=[
        "« DIEU N'EST PAS UN HOMME POUR MENTIR, ni fils d'homme pour AVOIR DU REGRET. » (23:19 — pas un homme !)",
        "« A-t-il DIT, et ne le FERA-t-il pas ? A-t-il PARLÉ, et ne l'accomplira-t-il pas ? » (23:19 — dit et fait !)",
        "« Il n'a pas aperçu de MALHEUR en Jacob, ni vu de MISÈRE en Israël. » (23:21 — pas aperçu !)",
        "« Jéhovah son Dieu est AVEC LUI ; l'acclamation d'un ROI est chez lui. » (23:21 — avec lui !)",
        "« Il n'y a pas de DIVINATION contre Jacob, pas de PRÉSAGE contre Israël. » (23:23 — pas de divination !)",
        "« Voici un peuple qui se lève comme une LIONNE, se dresse comme un LION. » (23:24 — lion !)",
        "« Il ne se couche pas qu'il n'ait DÉVORÉ sa proie et BU le sang des tués. » (23:24 — dévoré !)",
        "« Que tes TENTES sont belles, ô Jacob ! » (24:5 — belles !)",
        "« David BATTIT les Philistins, Moab, les Syriens… Jéhovah le GARDAIT partout. » (2S 8 — gardait !)",
    ],
    contexte=(
        "Plaines de Moab, ~1473 : BALAK, roi de Moab, a loué BALAAM, devin de "
        "Pethor sur l'Euphrate — « maudis-les pour moi » (22:6). Premier poème "
        "(23:7-10) : bénédiction. Balak change de LIEU (champ de Tsophim, sommet "
        "du Pisga, 23:13-14 — « tu n'en verras qu'une partie » : superstition "
        "géographique — changer d'angle pour changer l'oracle !), rebâtit 7 "
        "autels, réoffre 7 taureaux et 7 béliers — et le 2e poème tombe, plus "
        "tranchant : non seulement Israël est béni, mais Dieu NE PEUT PAS se "
        "dédire. « Lève-toi, Balak, écoute ! » (23:18) : le devin payé fait la "
        "leçon au roi payeur. Jéhovah « mit une parole dans la bouche de Balaam » "
        "(23:5, 16) : le devin est un porte-voix — l'oracle passe par lui MALGRÉ "
        "lui (« Jéhovah a obligé Balaam à prononcer sur Israël une bénédiction », "
        "1978288)."
    ),
    explication=(
        "« EL LO ISH » (23:19 — Dieu n'est pas un homme) : la négation porte sur "
        "la NATURE — mentir (kazav) et « avoir du regret » (TM : « qui a du "
        "regret », hitnahem) sont des modes HUMAINS que Dieu n'emprunte pas quand "
        "Il a promis ; le parallélisme est un chiasme : DIT → FERA / PARLÉ → "
        "ACCOMPLIRA — parole et acte soudés. « Il n'a pas APERÇU (hibbit) de "
        "malheur en Jacob » (23:21) : le regard de L'ALLIANCE — après le veau "
        "d'or, après Kadès, Dieu voit Israël à travers la promesse, pas à travers "
        "le dossier ; « l'acclamation (terou'ah) d'un ROI est chez lui » : "
        "Jéhovah est le roi acclamé au milieu du camp — le trône est DANS les "
        "tentes. « Pas de DIVINATION (nahash)… pas de PRÉSAGE (qesem) » (23:23) : "
        "les deux métiers de Balaam déclarés NULS contre Israël — le devin "
        "prononce sa propre inutilité ! « Comme une LIONNE (lavi)… comme un LION "
        "(ari) » (23:24) : le couple lionne-lion — la bête qui se lève ne se "
        "recouche que repue : l'appétit militaire d'Israël est programmé."
    ),
    interpretation=(
        "NOMBRES 24:1-9 (P052) : le 3e poème AMPLIFIE — « que tes tentes sont "
        "belles » (24:5), « il se couche comme un lion, comme une lionne : qui "
        "le fera lever ? » (24:9 : le lion de 23:24 s'est couché repu — "
        "l'accomplissement est déjà décrit au passé de l'oracle !), « béni qui "
        "te bénit, maudit qui te maudit » (24:9) : un DEVIN PAÏEN réédite Genèse "
        "12:3 — l'alliance abrahamique confirmée par la bouche de l'ennemi. "
        "2 SAMUEL 8:1-14 (P052) : le lion se lève — Philistins battus, Moab "
        "« mesuré au cordeau » (8:2 : deux cordeaux à mort, un à vie — le lion "
        "compte ses proies), Syriens et Édomites soumis, « Jéhovah gardait David "
        "partout où il allait » (8:6, 14 — refrain × 2 : la garde divine, "
        "l'accomplissement de « Jéhovah son Dieu est avec lui », 23:21). Balak "
        "« fulmina » et congédia Balaam (1978288) : la commande « maudis » livra "
        "« bénis » trois fois — le devin repartit sans salaire, l'oracle sans "
        "appel."
    ),
    hist=(
        "BALAAM DE PETHOR : devin mésopotamien de renom (« je sais que celui que "
        "tu bénis est béni », 22:6 — Balak connaît ses tarifs et sa réputation) ; "
        "cupide (« Balaam désirait toujours la récompense », 1978288), il "
        "conseillera ensuite la séduction de Baal-Peor (Nb 25 ; 31:16) et mourra "
        "par l'épée d'Israël (Nb 31:8) : l'oracle était vrai, l'homme était faux. "
        "DEIR ALLA (Jordanie, 1967) : inscription araméenne sur plâtre — « "
        "Balaam fils de Beor, voyant des dieux » : la tradition de Balaam est "
        "attestée hors Bible, dans la région même de l'oracle, ~800 av. n. è. "
        "BALAK FILS DE TSIPPOR : roi de Moab ~1473, contemporain de la fin de "
        "l'Exode ; les 7 autels × 3 sites (Bamoth-Baal, Tsophim-Pisga, Peor) : "
        "21 taureaux, 21 béliers — le budget de la malédiction, dépensé en pur "
        "bénédiction. DAVID (XIe s.) : 2S 8 exécute le programme du lion en une "
        "campagne."
    ),
    geo=(
        "PETHOR SUR L'EUPHRATE : ~600 km des plaines de Moab — Balak fait venir "
        "son devin de Mésopotamie : la peur de Moab paie le voyage. Les TROIS "
        "SITES : Bamoth-Baal (hauts lieux de Baal — on maudit sous les auspices "
        "du dieu local), champ de TSOPHIM au sommet du PISGA (« tu n'en verras "
        "qu'une partie » — la superstition veut qu'un Israël partiel soit "
        "maudissable), mont PEOR face au désert (23:28) : trois angles de vue, "
        "trois échecs — la géographie ne change pas la parole. « Du SOMMET DES "
        "ROCHERS je les vois » (23:9) : le camp israélite déployé dans les "
        "plaines — ~2 millions d'hommes en ordre de tribus (Nb 2), visible "
        "comme une marée de tentes. Le LION : bête de Canaan et du Jourdain "
        "(« fourrés du Jourdain », Jr 49:19) — l'image est prise au pays même "
        "qu'Israël va prendre."
    ),
    sci=(
        "LA POÉSIE DU CHIASME (23:19) : dit/fera // parlé/accomplira — structure "
        "ABBA de la certitude : le vers se referme sur lui-même comme un sceau ; "
        "la forme EST le message : parole bouclée, acte garanti. Le TAUREAU "
        "SAUVAGE (re'em, 23:22 : « cornes de taureau sauvage ») : l'aurochs (Bos "
        "primigenius), disparu en 1627 — la force de l'Exode comparée à une bête "
        "alors vivante au Proche-Orient : l'image date l'oracle (on ne compare "
        "pas à une bête éteinte). Le LION ASIATIQUE : présent au Levant dans "
        "l'Antiquité (reliefs assyriens de chasse au lion, os en Canaan) — "
        "l'oracle décrit un prédateur que les Moabites connaissaient. La "
        "PSYCHOLOGIE DE BALAK : changer de lieu pour changer l'oracle (23:13, "
        "27) — biais cognitif du devin-client : quand le message déplaît, on "
        "change le médium au lieu d'écouter."
    ),
    schema=(
        "LA COMMANDE INVERSÉE : Balak commande « maudis » (× 3 sites, 21 "
        "taureaux) → Jéhovah livre « bénis » (× 3 poèmes). 23:19 est la facture : "
        "Dieu a DIT (bénédiction, Gn 12:3) → Dieu FERA (impossible de se "
        "dédire). Le devin païen devient témoin à charge de son client : « pas "
        "de divination contre Jacob » — Balaam signe sa propre faillite."
    ),
    limites=(
        "« Il n'a pas aperçu de malheur en Jacob » (23:21) ne NIE PAS les péchés "
        "d'Israël — Nb 25 (Baal-Peor, 24 000 morts) suit de près : le regard de "
        "l'alliance n'est pas de l'aveuglement, c'est de la fidélité au serment. "
        "Balaam reste « ce faux-jeton au cœur tortueux » (2P 2:15-16 ; Jude 11 ; "
        "Ré 2:14) : Dieu parle par un corbeau sans approuver le corbeau — "
        "l'oracle vrai ne canonise pas l'orateur. 23:19 (« pas de regret ») se "
        "lit AVEC Gn 6:6 (« Jéhovah regretta ») : deux anthropomorphismes "
        "complémentaires — Dieu ne se dédit pas de Ses promesses, et Il « "
        "regrette » le mal des hommes : la fiche ne tranche pas au-delà du "
        "texte. Le lion (23:24) vise les conquêtes davidiques, pas une férocité "
        "sans loi : Israël reste lié par les règles de guerre (Dt 20)."
    ),
    accomplissement=[(("~1473 (Moab)", "2e poème : Dieu dit = Dieu fait ; le lion (23:19-24)")),
        (("~1473", "3e poème : lion couché repu ; béni/maudit (24:1-9)")),
        (("~1473", "Balaam congédié sans salaire ; conseil de Peor (Nb 25 ; 31:8, 16)")),
        (("XIe s.", "David : Philistins, Moab, Syrie, Édom (2S 8:1-14)")),
        (("~800", "Deir Alla : « Balaam fils de Beor » attesté hors Bible"))],
    tl=[(("1473", "Balak loue Balaam")),
        (("1473", "3 poèmes : bénis ×3")),
        (("1473", "Peor : le conseil")),
        (("XIe s.", "Le lion se lève (2S 8)")),
        (("800", "Deir Alla"))],
    src=[("Un homme qui s'opposa à la volonté de Dieu (Balaam, bénédictions forcées)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1978288"),
        ("Questions de lecteurs (Balaam : paroles imposées, récompense)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1955331"),
        ("Nombres 23 — Bible d'étude (notes 23:19-24)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/23")],
    img="images/prophe_EX052_lion.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX053", titre="Une étoile sortira de Jacob",
    ref="Nombres 24:17-19",
    statut="Accomplie / À venir",
    cat="EX", syst="Oracle de Balaam 4 (étoile + sceptre → David → Messie)",
    reg="Registre : Nombres — P053 (24:17-19 : étoile de Jacob, sceptre d'Israël) ; accomplissement 2S 8:2, 14 ; Ps 2 ; Ré 22:16",
    texte=[
        "« Je le vois, mais PAS MAINTENANT ; je le contemple, mais PAS DE PRÈS. » (24:17 — pas maintenant !)",
        "« Une ÉTOILE sortira de Jacob, un SCEPTRE se lèvera d'Israël. » (24:17 — étoile et sceptre !)",
        "« Il FRAPPERA les TEMPES de Moab. » (24:17 — tempes !)",
        "« Il détruira tous les FILS DU TUMULTE. » (24:17 — tumulte !)",
        "« Édom sera une POSSESSION, Séir une possession de ses ennemis. » (24:18 — possession !)",
        "« De Jacob sortira un DOMINATEUR ; il fera PÉRIR le reste des villes. » (24:19 — dominateur !)",
        "« Il mit des GARNISONS en Édom ; tous les Édomites furent ASSUJETTIS. » (2S 8:14 — assujettis !)",
        "« TU LES BRISERAS avec un sceptre de fer. » (Ps 2:9 — briseras !)",
        "« Moi, Jésus… l'ÉTOILE BRILLANTE DU MATIN. » (Ré 22:16 — du matin !)",
    ],
    contexte=(
        "Plaines de Moab, ~1473 — 4e poème, le plus lointain : « je vais "
        "t'annoncer ce que ce peuple fera à ton peuple À LA FIN DES JOURS "
        "(be'aharit hayyamim — TM : « à la fin des jours ») » (24:14). Balaam "
        "congédié (24:11 : « file chez toi ! ») prononce un surplus d'oracle — "
        "l'horizon dépasse Balak, dépasse Moab, dépasse le siècle : « pas "
        "maintenant, pas de près » — la prophétie à double foyer, proche (David) "
        "et lointain (Messie). L'ÉTOILE (kokab) et le SCEPTRE (shevet) : le "
        "ciel et le trône en un vers — le roi à venir est annoncé par un devin "
        "païen qui ne le verra jamais. Statut registre : Accomplie / À venir — "
        "la fiche tient les deux bouts."
    ),
    explication=(
        "« Pas MAINTENANT (attah)… pas DE PRÈS (qarov) » (24:17) : double "
        "négation temporelle ET spatiale — l'objet est loin dans le temps et "
        "loin dans l'espace : la formule même de la prophétie messianique. « "
        "ÉTOILE (kokab)… SCEPTRE (shevet) » : shevet = bâton, sceptre, TRIBU — "
        "un mot, trois sens : le bâton de Juda (Gn 49:10 : « le sceptre ne "
        "s'écartera pas de Juda » — P8-5 !) devient tribu royale ; l'étoile "
        "couronne le sceptre — le roi terrestre a un signe céleste. « Les "
        "TEMPES (pa'ate) de Moab » (TM : « les tempes ») : pa'ah = côté, tempe, "
        "frontière — frapper les « tempes », c'est frapper aux points vitaux ET "
        "aux frontières : Moab atteint au front et aux marches. « Fils du "
        "TUMULTE » (TM : « fils du tumulte » — bene-Sheth lu comme tumulte) : le "
        "chaos personnifié, voué à la destruction. « DOMINATEUR (yird) » "
        "(24:19) : le verbe de la domination royale (cf. Ps 72:8) — pas un chef "
        "de raid, un souverain."
    ),
    interpretation=(
        "DAVID — 1er accomplissement : 2S 8:2 (Moab « mesuré au cordeau », "
        "assujetti au tribut — les « tempes de Moab » frappées) et 8:14 "
        "(« garnisons dans tout Édom ; tous les Édomites furent assujettis à "
        "David » — « Édom sera une possession », 24:18, mot pour mot). Quatre "
        "siècles après l'oracle (~1473 → XIe s.), un roi de Juda exécute le "
        "programme : Moab + Édom, les deux voisins visés. LE MESSIE — portée "
        "finale : PSAUME 2 (P053) — « tu les briseras avec un sceptre de fer » "
        "(2:9 : le shevet de Nb 24:17 devenu fer) ; RÉVÉLATION 22:16 (P053) — "
        "« MOI, JÉSUS… L'ÉTOILE BRILLANTE DU MATIN » : Jésus S'IDENTIFIE à "
        "l'étoile — l'auto-exégèse tranche : le kokab de Jacob, c'est Lui. "
        "BAR KOKHBA (« fils de l'étoile », 132 ap. n. è.) : le faux messie qui "
        "s'arrogea le titre — preuve que les Juifs lisaient Nb 24:17 comme "
        "messianique, et contre-exemple : l'étoile autoproclamée s'éteignit à "
        "Béthar (135)."
    ),
    hist=(
        "DAVID (XIe s. av. n. è.) : roi à Hébron puis Jérusalem, 40 ans de règne "
        "— ses campagnes (2S 8, 10, 12) soumettent le croissant : Philistins "
        "ouest, Moab est, Syriens nord, Édom sud — l'empire davidique réalise "
        "« de Jacob sortira un dominateur ». La STÈLE DE TEL DAN (IXe s., « "
        "maison de David » — bytdwd) atteste la dynastie hors Bible. BAR KOKHBA "
        "(132-135 ap. n. è.) : acclamé messie (Rabbi Aqiba), titré « fils de "
        "l'étoile » d'après Nb 24:17 — frappe monnaie (« an 1 de la rédemption "
        "d'Israël »), tient 3 ans, écrasé par Hadrien : 580 000 morts (Dion "
        "Cassius) — le prix d'une étoile usurpée. L'ÉTOILE ROYALE au Proche-"
        "Orient : les rois s'associent aux astres (étendards, sceaux, « étoile "
        "du roi ») — l'oracle parle le langage du temps : un roi-étoile, "
        "compréhensible de Pethor à Moab."
    ),
    geo=(
        "MOAB : plateau à l'est de la mer Morte (Dibon, Médeba) — « tempes » "
        "frappées par David : Moab devient tributaire, corvéable (« apportant "
        "des présents », 2S 8:2). ÉDOM/SÉIR : montagnes du sud (Bozra, Séla) — "
        "« possession » : garnisons davidiques sur les routes du cuivre et des "
        "caravanes (Etsion-Guéber, port de Salomon — 1R 9:26 : la possession "
        "d'Édom donne à Israël la mer Rouge !). Le REGARD DE BALAAM : depuis "
        "les hauteurs de Moab, il voit le camp d'Israël — et, « pas de près », "
        "au-delà des siècles, l'étoile : la géographie de l'oracle (plaines de "
        "Moab) est le tremplin de sa chronologie (fin des jours). BÉTHLEHEM : "
        "la ville d'où sort le sceptre (Mi 5:1) — David ET Jésus, natifs du "
        "même bourg : l'étoile a une adresse."
    ),
    sci=(
        "L'ASTRONOMIE DE L'IMAGE : « l'étoile brillante du matin » (Ré 22:16) — "
        "VÉNUS à l'aube, l'astre le plus brillant après soleil et lune, héraut "
        "du jour : Jésus-étoile annonce le Jour — l'astronomie porte la "
        "théologie (cf. 2P 1:19 : « l'étoile du matin se lève dans vos cœurs »). "
        "La PHILOLOGIE DE SHEVET : bâton → sceptre → tribu — un seul mot couvre "
        "l'instrument, le pouvoir et le peuple : la langue hébraïque fait du "
        "bâton de berger de Juda un emblème dynastique. La CRITIQUE TEXTUELLE : "
        "« fils de Sheth / du tumulte » — les versions hésitent (LXX, Vulgate, "
        "TM : « fils du tumulte ») : la fiche signale l'hésitation au lieu de "
        "la masquer (voir limites). La NUMISMATIQUE : monnaies de Bar Kokhba "
        "frappées « an 1 / an 2 de la rédemption » — l'usurpation messianique a "
        "laissé des pièces : on peut tenir en main une fausse étoile."
    ),
    schema=(
        "L'ÉTOILE À DOUBLE FOYER : oracle ~1473 (« pas maintenant ») → FOYER "
        "PROCHE : David (Moab + Édom, XIe s.) → FOYER LOINTAIN : Jésus (« moi… "
        "l'étoile brillante du matin », Ré 22:16) → « fin des jours » (Ps 2 : "
        "le sceptre de fer). ÉTOILE (signe céleste) + SCEPTRE (pouvoir "
        "terrestre) = ROI MESSIANIQUE. Bar Kokhba : la fausse étoile qui "
        "prouve, par contraste, la vraie."
    ),
    limites=(
        "L'ÉTOILE DES MAGES (Mt 2:1-12) est un AUTRE astre, 15 siècles plus tard "
        ": ne pas confondre le kokab-oracle (Nb 24) et le kokab-guide "
        "(Matthieu) — deux étoiles, deux dossiers. « Fils de Sheth / du "
        "tumulte » (24:17) : le texte est discuté — la fiche suit TM (« fils du "
        "tumulte ») en signalant l'alternative (Seth, fils d'Adam = "
        "l'humanité). Bar Kokhba prouve la lecture messianique juive, pas la "
        "validité du prétendant — ni, à lui seul, celle de Jésus : c'est Ré "
        "22:16 (auto-identification) qui tranche pour le chrétien. La part « À "
        "venir » (Ps 2, règne du sceptre de fer) N'EST PAS DATÉE : « fin des "
        "jours » (24:14) reste ouvert — aucun calendrier dans cette fiche."
    ),
    accomplissement=[(("~1473 (Moab)", "4e poème : étoile + sceptre, fin des jours (24:14-19)")),
        (("XIe s.", "David : Moab au cordeau, garnisons en Édom (2S 8:2, 14)")),
        (("~1040?", "Psaume 2 : le sceptre de fer (oint de Jéhovah)")),
        (("132-135 n. è.", "Bar Kokhba : la fausse étoile (contre-exemple)")),
        (("~96 n. è. → fin", "« Moi, Jésus, l'étoile du matin » (Ré 22:16) ; Ps 2 À venir"))],
    tl=[(("1473", "« Pas maintenant »")),
        (("XIe s.", "David : Moab+Édom")),
        (("132", "Fausse étoile")),
        (("96", "« Moi, Jésus… »")),
        (("fin", "Sceptre de fer"))],
    src=[("Nombres 24 — Bible d'étude (notes 24:14-19, fin des jours)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/24"),
        ("Révélation 22 — Bible d'étude (22:16, étoile du matin)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/22"),
        ("2 Samuel 8 — Bible d'étude (Moab, Édom assujettis)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/10/8")],
    img="images/prophe_EX053_etoile.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX054", titre="Amalek finira ; les navires de Kittim",
    ref="Nombres 24:20-24",
    statut="Accomplie",
    cat="EX", syst="Oracles-nations (Amalek → Kénien → Kittim → lui-même)",
    reg="Registre : Nombres — P054 (24:20-24 : Amalek finira ; Kittim humiliera Assour et Éber) ; accomplissement 1S 15:7, 8 ; 1Ch 4:41-43 ; conquêtes grecques",
    texte=[
        "« AMALEK est la PREMIÈRE des nations, mais sa FIN sera la DESTRUCTION. » (24:20 — première… destruction !)",
        "« Ton NID est posé sur le ROC… mais le Kénien sera consumé. » (24:21-22 — nid sur roc !)",
        "« Quand Dieu fera cela, QUI VIVRA ? » (24:23 — qui vivra !)",
        "« Des NAVIRES viendront de la côte de KITTIM. » (24:24 — navires !)",
        "« Ils AFFLIGERONT ASSOUR et affligeront ÉBER. » (24:24 — affligeront !)",
        "« Et LUI AUSSI périra. » (24:24 — lui aussi !)",
        "« Saül BATTIT Amalek de HAVILA jusqu'à SHUR. » (1S 15:7 — battit !)",
        "« Ils frappèrent le RESTE D'AMALEK à la montagne de SÉIR. » (1Ch 4:43 — reste !)",
        "« Les navires de Kittim viendront contre lui. » (Dn 11:30 — contre lui !)",
    ],
    contexte=(
        "Plaines de Moab, ~1473 — suite du 4e poème : après l'étoile (EX053), "
        "Balaam tourne son regard vers les NATIONS, une à une — « il vit Amalek… "
        "il vit les Kéniens… » (24:20-21) : oracles à vue, le devin prophétise "
        "sur ce qu'il désigne. TROIS oracles en escalade : AMALEK (l'ennemi "
        "héréditaire, Ex 17 — décret d'extermination déjà prononcé, Ex 17:14, "
        "Dt 25:19), le KÉNIEN (l'allié ambigu — les Kéniens, beaux-frères de "
        "Moïse par Hobab, nichés au sud), KITTIM (l'inconnu de l'ouest — "
        "l'horizon s'ouvre à 1 200 ans : les empires maritimes). Le v.23 fait "
        "charnière — « hélas ! qui vivra quand Dieu fera cela ? » : le frisson "
        "du devin devant sa propre vision — Balaam s'effraie de ce qu'il voit."
    ),
    explication=(
        "« PREMIÈRE (reshit) des nations » (24:20) : reshit = prémices, "
        "commencement — Amalek est le PREMIER peuple à attaquer Israël (Ex 17:8, "
        "Rephidim) : « premier » en hostilité, premier au jugement — « sa fin "
        "(aharit) : DESTRUCTION (oved) » : le premier ennemi aura une fin "
        "définitive (le verbe oved = périr sans reste). « Ton NID (qen) sur le "
        "ROC (sela') » (24:21) : jeu de mots — QENIEN (Qayin) / nid (qen) : le "
        "nom du peuple EST son image ; « mais… Ashur t'emmènera captif » (24:22) "
        ": le nid le plus haut n'échappe pas à l'aigle assyrien. « Des NAVIRES "
        "(tsiyim) de la côte de KITTIM » (24:24) : Kittim = Chypre (Kition), "
        "puis par extension l'Occident maritime — TM renvoie à it-1 680, 1087 "
        "et it-2 95 ; « ils AFFLIGERONT (innu) Assour et Éber » : le verbe de "
        "l'humiliation — l'est (Assyrie) et les Hébreux (Éber) affligés par "
        "l'ouest. « Et LUI AUSSI (gam hu) périra » : la chute est transitive — "
        "l'instrument du jugement sera jugé."
    ),
    interpretation=(
        "AMALEK — exécution en 3 actes : SAÜL (1S 15:7-8, P054) — « il battit "
        "Amalek de Havila jusqu'à Shur… il prit vivant Agag » : l'anathème est "
        "EXÉCUTÉ mais INCOMPLET (Agag épargné, le meilleur du bétail — 15:9) → "
        "Samuel achève Agag (15:33 : « comme ton épée a privé des femmes de "
        "leurs enfants… ») et le ROYAUME est retiré à Saül (15:28) : la "
        "désobéissance sur Amalek coûte la couronne. DAVID (1S 30 : Tsiklag "
        "pillée par les Amalécites, reprise + butin) : la guerre d'usure. "
        "SIMÉONITES (1Ch 4:41-43, P054) — « au temps d'Ézéchias… ils frappèrent "
        "le RESTE d'Amalek à la montagne de Séir » : le mot « reste » (she'erit) "
        "est l'acte de décès — « depuis ce temps-là, aucune autre allusion à "
        "Amalek n'est faite ni dans la Bible ni dans l'histoire profane » "
        "(1963644). KITTIM (P054) : Chypre → ALEXANDRE — 120 navires chypriotes "
        "au siège de Tyr (332, 7 mois — 2007764), Strabon (flotte démontée, "
        "Thapsaque en 7 jours) : « ils affligeront Assour » — l'empire perse "
        "(héritier d'Assour) balayé par l'ouest ; Dn 11:30 (« les navires de "
        "Kittim » = les ROMAINS, Rbi8 : LXX « les Romains ») : la prophétie "
        "traverse les empires — Grèce puis Rome, Kittim est un titre, pas un "
        "peuple."
    ),
    hist=(
        "AGAG : roi d'Amalek capturé par Saül (~XIe s.) — « Agag s'avança vers "
        "lui d'un air joyeux » (1S 15:32 : « sûrement l'amertume de la mort est "
        "passée ») : la dernière illusion d'Amalek, tranchée par Samuel. HAMAN "
        "L'AGAGUITE (Est 3:1) : le titre rattache probablement Haman à la "
        "lignée d'Agag — le génocide manqué de Pourim (~475) serait la dernière "
        "tentative d'Amalek contre les Juifs, retournée (Haman pendu à sa propre "
        "potence, Est 7:10) : Amalek périt par son propre piège — « sa fin : "
        "destruction » jusqu'au bout (lien probable, voir limites). ALEXANDRE "
        "(332) : Tyr assiégée 7 mois avec 120 trirèmes chypriotes (2007764) — "
        "l'île forteresse tombe, la côte phénicienne passe à l'ouest : "
        "l'affliction d'Assour commence au large de Tyr. « Lui aussi périra » : "
        "les empires occidentaux eux-mêmes passeront — Grèce, puis Rome (Dn "
        "11:30)."
    ),
    geo=(
        "AMALEK : le NÉGEV et le nord-Sinaï — Havila→Shur (1S 15:7 : de "
        "l'Arabie à la frontière d'Égypte), mont SÉIR (1Ch 4:42 : le dernier "
        "« reste » traqué jusque chez Édom) : la carte d'Amalek se rétrécit "
        "d'oracle en oracle — Négev → Havila-Shur → Séir → RIEN. KITTIM = "
        "CHYPRE (Kition, côte sud-est) : l'île du cuivre, carrefour "
        "phénicien-grec — « la côte de Kittim » (24:24) : le seul littoral "
        "nommé de l'oracle, face à Tyr. TYR (332) : île forteresse à 800 m du "
        "rivage — Alexandre y bâtit une digue (le tombolo existe encore : la "
        "géographie garde la cicatrice du siège). THAPSAQUE/TIPHSAH (1R 4:24 : "
        "limite de Salomon !) : les navires démontés d'Alexandre y parviennent "
        "en 7 jours (Strabon, 2007764) — l'ouest atteint en une semaine la "
        "frontière orientale de l'empire davidique : la boucle Salomon-Alexandre "
        "se referme sur l'Euphrate."
    ),
    sci=(
        "LA MARINE ANTIQUE (2007764) : trirèmes de combat — ~150 rameurs, peu de "
        "cale, escales obligées (îles Égéennes : ravitaillement, réparations) ; "
        "« légers et faciles à DÉMONTER » (Strabon) : on portait les coques "
        "par voie de terre — la logistique qui permet à Kittim de frapper "
        "l'intérieur (Thapsaque). La SÉMANTIQUE DIAKHRONIQUE : Kittim = Chypre "
        "(Gn 10:4, fils de Yavan) → Occident maritime (Dn 11:30, « gens de "
        "l'ouest arrivant par bateaux », BFC) : le nom S'ÉTEND avec l'horizon "
        "d'Israël — la prophétie utilise un terme à focale variable, valide "
        "pour Alexandre ET pour Rome. L'ÉPIGRAPHIE : Kition documentée (rois "
        "phéniciens de Chypre, inscriptions) ; Deir Alla (Balaam, EX052) "
        "ancre l'oracle dans la région ; la stèle de Mésha (Moab, ~840) "
        "confirme le contexte moabite. Le SILENCE comme preuve : « aucune "
        "autre allusion à Amalek ni dans la Bible ni dans l'histoire profane » "
        "(1963644) — une disparition totale, exactement comme annoncé (« "
        "périr », oved)."
    ),
    schema=(
        "TROIS ORACLES, UNE ESCALADE : AMALEK (l'ennemi proche — fin : "
        "destruction totale, exécutée Saül → David → Ézéchias) → KÉNIEN "
        "(l'allié haut perché — fin : l'Assyrie l'emmène) → KITTIM (l'inconnu "
        "lointain — il afflige Assour et Éber, PUIS périt lui-même). Chaque "
        "jugement déborde le précédent : le proche, le haut, le lointain — "
        "personne hors d'atteinte. « Et lui aussi périra » : le boomerang "
        "final — tout instrument de jugement sera jugé."
    ),
    limites=(
        "HAMAN « Agaguite » (Est 3:1) : le lien généalogique avec Agag est "
        "PROBABLE (titre ethnique) mais non prouvé formellement — la fiche le "
        "présente comme hypothèse, pas comme chaînon. « ÉBER » (24:24) : les "
        "Hébreux ou la Trans-Euphrate (« au-delà ») ? Les deux lectures "
        "existent ; le registre retient « Assour et Éber » sans trancher "
        "davantage — la fiche non plus. Le KÉNIEN emmené par Ashur (24:22) : "
        "l'accomplissement précis n'est pas daté dans la Bible — les Kéniens, "
        "absorbés dans Juda (Jg 1:16 ; 1Ch 2:55), disparaissent par assimilation "
        "plus que par déportation attestée : ne pas sur-affirmer. « Lui aussi "
        "périra » (24:24) vise le cycle des empires occidentaux, pas une date : "
        "aucun calendrier dans cette fiche. Enfin, l'oracle contre Amalek "
        "(anathème total) se lit dans son cadre judiciaire antique (Dt 25:17-19 "
        ": Amalek attaqua les faibles à l'arrière) — pas comme un modèle "
        "transposable."
    ),
    accomplissement=[(("~1473 (Moab)", "Oracles : Amalek, Kénien, Kittim (24:20-24)")),
        (("XIe s.", "Saül : Havila→Shur, Agag pris (1S 15:7-8) ; Samuel achève")),
        (("~XIe-Xe s.", "David : Tsiklag, guerre d'usure (1S 30)")),
        (("~Ézéchias", "Siméonites : le « reste » à Séir (1Ch 4:41-43) ; silence total")),
        (("332 → Rome", "120 navires chypriotes à Tyr ; Dn 11:30 : Kittim = Romains"))],
    tl=[(("1473", "3 oracles-nations")),
        (("XIe s.", "Saül : Agag")),
        (("Ézéchias", "Le « reste » frappé")),
        (("332", "Tyr : 120 navires")),
        (("Rome", "Lui aussi"))],
    src=[("Les Amalécites : une leçon (extermination, silence total)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1963644"),
        ("Les navires de Kittim sillonnent les mers (Alexandre, Tyr, Strabon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007764"),
        ("Nombres 24 — Bible d'étude (notes 24:20-24, Kittim)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/24")],
    img="images/prophe_EX054_kittim.jpg",
))
