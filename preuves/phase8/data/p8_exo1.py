#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 8 · vague P8-8 · EX — Exode (1) : P043-P048."""
# pylint: disable=invalid-name,line-too-long

CAT = dict(
    code="EX",
    nom="Exode (1) — le mémorial et le Royaume",
    intro=("La Pâque devient mémorial perpétuel avant même la sortie ; Pharaon poursuit "
           "comme annoncé et la mer se referme ; au Sinaï, l'offre du royaume de prêtres "
           "est lancée — puis le veau d'or attire la menace du livre, l'ange prend la "
           "tête de la montée, et le Lévitique déploie le terrible catalogue des "
           "malédictions en cas de rupture."),
    vague="P8-8",
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX043", titre="La Pâque : mémorial pour des temps indéfinis",
    ref="Exode 12:14-17",
    statut="Accomplie",
    cat="EX", syst="Pâque perpétuelle (mémorial → Guilgal → Josias → Cène)",
    reg="Registre : Exode — P043 (12:14-17 : la Pâque, ordonnance permanente) ; accomplissement Jos 5:10 ; 2R 23:21-23 ; Lc 22:19, 20",
    texte=[
        "« CE JOUR devra vous servir de MÉMORIAL (zikkaron). » (12:14 — mémorial !)",
        "« Vous le célébrerez comme une FÊTE pour Jéhovah. » (12:14 — fête !)",
        "« Dans toutes vos générations, ORDONNANCE PERMANENTE. » (12:14 — permanente !)",
        "« SEPT JOURS vous mangerez des pains sans levain. » (12:15 — sept jours !)",
        "« Quiconque mangera du levé sera RETRANCHÉ. » (12:15 — retranché !)",
        "« Car CE JOUR-LÀ MÊME j'ai fait sortir vos armées. » (12:17 — ce jour-là même !)",
        "« Vous observerez ce jour dans vos générations, ORDONNANCE PERMANENTE. » (12:17 — permanente !)",
        "« Ils célébrèrent la Pâque à GUILGAL, le 14e jour. » (Jos 5:10 — GUILGAL !)",
        "« On n'avait pas célébré une telle Pâque depuis les juges. » (2R 23:22 — depuis les juges !)",
        "« Faites ceci EN SOUVENIR DE MOI. » (Lc 22:19 — en souvenir !)",
    ],
    contexte=(
        "Goshen, 14 Nisan 1513 — AVANT la nuit du jugement (P042), Dieu institue le "
        "SOUVENIR de la nuit : la Pâque est un mémorial programmé avant l'événement — "
        "on prépare la commémoration pendant qu'on prépare l'agneau. « Zikkaron » "
        "(12:14, mémorial) : monument de mémoire (cf. l'autel « témoin » de Jos 22:34, "
        "les pierres du Jourdain, Jos 4:7 : Israël jalonne sa mémoire). « Hag » "
        "(12:14, fête) : fête de pèlerinage, danse sacrée — la sortie sera dansée "
        "tous les ans. « Huqqat olam » (12:14, 17, ordonnance permanente — « pour des "
        "temps indéfinis, aussi longtemps que je vous le dirai », 402013925) : "
        "répété DEUX fois en 4 versets (12:14, 17) — l'insistance fait l'institution. "
        "Et les pains sans levain (12:15-20) : 7 jours de purge — « pas de levé chez "
        "toi » (12:19) : la maison passée au crible, comme le pays passé au jugement."
    ),
    explication=(
        "« CE JOUR (hayyom hazzeh) » (12:14) : démonstratif — le 14 Nisan, daté (12:6), "
        "calé sur la sortie (12:17, « ce jour-là même j'ai fait sortir vos armées » : "
        "betsem hayyom — la formule de l'échéance, cf. 12:41, 51 !). « RETRANCHÉ "
        "(nikhrat) » (12:15, 19) : retrancher = excommunier, exclure du peuple (voire "
        "mettre à mort selon les cas) — manger du levé pendant la fête, c'est se "
        "mettre hors du mémorial : le levain exclut. « SEPT JOURS » (12:15) : semaine "
        "complète (14 Nisan la Pâque + 15-21 les azymes, Lv 23:5-6) — assemblées "
        "saintes le 1er et le 7e jour (12:16), « aucune œuvre » : la semaine "
        "s'ouvre et se ferme en sabbat. Le LEVAIN (se'or/hamets) : la fermentation — "
        "symbole de corruption (« un peu de levain fait lever toute la pâte », "
        "1Co 5:6 — Paul, en pleine Pâque !) : la purge domestique figure la purge "
        "morale."
    ),
    interpretation=(
        "GUILGAL (Jos 5:10 — P043) : 40 ans après, « le 14e jour du mois, au soir, "
        "dans les plaines de Jéricho » — première Pâque EN Canaan, après la "
        "circoncision de masse (5:2-9, « j'ai roulé la honte de l'Égypte » !) ; « dès "
        "le lendemain, la manne CESSA » (5:11-12) : le désert nourri cède au pays "
        "cultivé — la Pâque marque le changement d'ère. JOSIAS (2R 23:21-23 — P043) : "
        "622 av. n. è., après la découverte du Livre (22:8) — « on n'avait pas "
        "célébré une telle Pâque depuis les jours des juges » : 800 ans après "
        "l'institution, la fête bat son record de ferveur. LA CÈNE (Lc 22:19-20 — "
        "P043) : Jésus célèbre la Pâque « comme le prescrivait la Loi » (1993089, "
        "Lc 22:7-8, Pierre et Jean envoyés) PUIS institue le Repas du Seigneur — "
        "« continuez à faire ceci en souvenir de moi » : le mémorial mosaïque enfante "
        "le mémorial chrétien (1Co 11:23-26, « chaque fois que »). ÉZÉCHIAS (2Ch 30, "
        "2e mois, « grande assemblée ») et le RETOUR (Esd 6:19-22) : la chaîne ne "
        "rompt jamais."
    ),
    hist=(
        "DÉSERT : 2e Pâque au Sinaï (Nb 9:1-5, an 2) + disposition du 2e MOIS pour "
        "impurs et voyageurs (Nb 9:10-11 — « caractère exceptionnel », 1993089 : la "
        "Loi prévoit les empêchés sans banaliser la date). ÉZÉCHIAS (~732, 2Ch 30) : "
        "Pâque au 2e mois (prêtres non sanctifiés, peuple non rassemblé — 30:3), "
        "courriers dans tout Israël, « grande joie à Jérusalem » (30:26) : le "
        "réveil utilise la fête. JOSIAS (622, 2R 23 + 2Ch 35 : 30 000 agneaux du roi "
        "lui-même, 35:7 !) : centralisation (Dt 16:2, « au lieu choisi ») + ferveur — "
        "« telle Pâque » = ampleur + pureté. RETOUR (516, Esd 6:19-22) : Pâque après "
        "le Temple rebâti — « Jéhovah les avait rendus joyeux ». JÉSUS (33 de n. è., "
        "Lc 22) : dernière Pâque légale + première Cène — le mémorial change de "
        "contenu (agneau → Christ, 1Co 5:7) sans changer de date (14 Nisan !)."
    ),
    geo=(
        "GOSHEN (institution, 1513) → SINAÏ (Nb 9) → GUILGAL (Jos 5:10, plaines de "
        "Jéricho — « campèrent à Guilgal » : premier camp cananéen, douze pierres du "
        "Jourdain, 4:20) → SILO → JÉRUSALEM (centralisation, Dt 16:5-6 : « au lieu que "
        "Jéhovah choisira » — Josias 2R 23, Ézéchias 2Ch 30 : TOUT Israël monte) → "
        "CHAMBRE HAUTE (Lc 22:12, « grande chambre garnie » à Jérusalem : la Cène "
        "naît dans la ville de la Pâque). GUILGAL (« roulement » : la honte roulée, "
        "5:9) : circoncision + Pâque + blé du pays (5:11, « vieux blé, grain rôti ») — "
        "triple inauguration : corps, culte, table. La MANNE CESSE (5:12) : « ils "
        "n'eurent plus de manne » — 40 ans de pain du ciel (Ex 16:35) s'arrêtent au "
        "lendemain de la Pâque : le mémorial clôt le désert."
    ),
    sci=(
        "Calendrier : 14 Nisan (Abib, « épis » — Ex 13:4, mois des orges mûres : "
        "calendrier agricole !), pleine lune — la Pâque est une fête de PRINTEMPS "
        "lunaire (cf. Pâques chrétienne : même ancrage). Fermentation : se'or (levain, "
        "pâte fermentée) vs hamets (levé) vs matsah (azyme) — la purge (bi'ur hamets : "
        "recherche du levé à la bougie, tradition juive) élimine TOUTE fermentation "
        "domestique 7 jours : hygiène + symbole (Paul : « purifiez-vous du vieux "
        "levain », 1Co 5:7). «betsem hayyom» (ce jour-là même, 12:17, 41, 51) : "
        "formule d'exactitude calendaire (cf. Gn 7:13, déluge ! Lé 23:28-30) — "
        "l'échéance au jour près, trois fois soulignée. Démographie : 30 000 agneaux "
        "de Josias (2Ch 35:7) + milliers de prêtres — logistique d'une fête "
        "nationale (abattage, rôtissage, distribution en un soir !)."
    ),
    schema=(
        "Avant la nuit : le SOUVENIR programmé (zikkaron + hag + huqqat olam × 2) → "
        "7 jours sans levain (purge : retranché si levé !) → « Ce jour-là même » "
        "(formule d'échéance) → Sinaï an 2 (Nb 9 + 2e mois des empêchés) → GUILGAL "
        "(1re en Canaan + manne cesse !) → Ézéchias (réveil, 2e mois) → JOSIAS "
        "(record depuis les juges, 30 000 agneaux) → Retour (joie, Esd 6) → "
        "CHAMBRE HAUTE (Lc 22 : Pâque légale + Cène instituée) → « En souvenir de moi »."
    ),
    limites=(
        "« Permanente » (olam) : temps indéfinis, « aussi longtemps que je vous le "
        "dirai » (402013925) — la Pâque mosaïque s'achève en Christ (Hé 8:13, "
        "alliance ancienne « près de disparaître » ; Col 2:16-17, « ombre ») : la "
        "fiche suit cette lecture (registre : Lc 22:19-20 comme accomplissement). "
        "« Depuis les juges » (2R 23:22) : formule — même pas sous David/Salomon une "
        "telle Pâque ? La fiche lit : ampleur + centralisation + ferveur inégalées "
        "(2Ch 35 détaille), sans exclure des Pâques régulières avant. 2e mois (Nb 9) : "
        "exception (impureté, voyage lointain), pas option libre (1993089) — Ézéchias "
        "l'utilise pour retard collectif (2Ch 30:2-3 : cas limite, Dieu pardonne, 30:20 !)."
    ),
    accomplissement=[(("1513 (institution)", "Mémorial + fête + permanente × 2 (12:14-17)")),
                     (("1512 (Sinaï)", "2e Pâque + 2e mois des empêchés (Nb 9)")),
                     (("~1473 (Guilgal)", "1re en Canaan ; manne cesse (Jos 5:10-12)")),
                     (("~732 (Ézéchias)", "Réveil au 2e mois ; grande joie (2Ch 30)")),
                     (("622 (Josias)", "Record depuis les juges ; 30 000 agneaux (2R 23 ; 2Ch 35)")),
                     (("516 (retour)", "Pâque du Temple rebâti (Esd 6:19-22)")),
                     (("33 (Cène)", "Pâque légale + « en souvenir de moi » (Lc 22:19-20)"))],
    tl=[(("1513", "Mémorial institué")),
        (("Guilgal", "Manne cesse")),
        (("Ézéchias", "Réveil")),
        (("622 (Josias)", "Record")),
        (("516", "Retour")),
        (("33 (Cène)", "Souvenir de moi"))],
    src=[("Exode 12 — Bible d'étude (14-17, mémorial permanent)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/12"),
         ("« Ce jour devra vous servir de mémorial » (ordonnance, générations)", "https://wol.jw.org/fr/wol/d/r30/lp-f/402013925"),
         ("Questions de lecteurs (Pâque, 2e mois, Cène, Lc 22:19)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1993089")],
    img="images/prophe_EX043_memorial.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX044", titre="Il les poursuivra : le piège de Pi-Hahiroth",
    ref="Exode 14:4",
    statut="Accomplie",
    cat="EX", syst="Mer Rouge (poursuite annoncée → gloire → savoir)",
    reg="Registre : Exode — P044 (14:4 : Pharaon poursuivra Israël) ; accomplissement Ex 14:8-10, 23-28",
    texte=[
        "« Campez devant PI-HAHIROTH, entre Migdol et la mer. » (14:2 — le piège !)",
        "« Pharaon dira : le désert S'EST REFERMÉ sur eux ! » (14:3 — refermé !)",
        "« Je laisserai son cœur S'OBSTINER, et IL LES POURSUIVRA. » (14:4 — IL POURSUIVRA !)",
        "« Je me GLORIFIERAI par Pharaon et toute son armée. » (14:4 — glorifierai !)",
        "« Et les Égyptiens SAURONT que je suis Jéhovah. » (14:4 — sauront !)",
        "« 600 chars d'élite + tous les chars d'Égypte. » (14:7 — 600 + tous !)",
        "« Israël sortait LA MAIN LEVÉE. » (14:8 — main levée !)",
        "« Ils les rattrapèrent près de la mer. » (14:9 — rattrapés !)",
        "« Les Égyptiens entrèrent derrière eux DANS la mer. » (14:23 — dans la mer !)",
        "« Les eaux revinrent : PAS UN SEUL ne resta. » (14:28 — pas un seul !)",
    ],
    contexte=(
        "Bord de la mer, 1513 — une semaine après la Pâque. Israël est sorti « la main "
        "levée » (14:8, TM : litt. « la main levée » — poing levé, assurance, défi !), "
        "600 000 hommes + multitude + troupeaux. Et Dieu ORDONNE le demi-tour : "
        "« qu'ils retournent camper devant Pi-Hahiroth » (14:2) — face à la mer, dos "
        "au désert, flancs aux défilés : position militairement ABSURDE, « le désert "
        "s'est refermé » (14:3, sagar : fermé, verrouillé — Pharaon lira la carte "
        "comme un piège… pour Israël !). C'est un piège, en effet — mais pour "
        "Pharaon : Dieu ANNONCE la poursuite avant qu'elle commence (« il les "
        "poursuivra », 14:4), avec son BUT (« je me glorifierai ») et son RÉSULTAT "
        "(« ils sauront »). La prophétie est un plan de bataille révélé d'avance."
    ),
    explication=(
        "« Je laisserai S'OBSTINER (ahazzeq, j'affermirai) » (14:4) : même verbe "
        "qu'en 9:12 (hazaq) — la séquence continue (P041) : Pharaon a choisi, Dieu "
        "affermit le choix jusqu'au bout — JUSQUE DANS LA MER (14:17, « j'affermirai "
        "le cœur des Égyptiens pour qu'ils y entrent » : l'obstination mène au "
        "fond). « Je me GLORIFIERAI (ikkavda) » (14:4, 17, 18 — TROIS fois !) : "
        "kaved = lourd/gloire — MÊME racine que le cœur « appesanti » (kaved, 7:14, "
        "8:15…) ! Le poids du cœur rebelle devient le POIDS de la gloire divine : "
        "calembour théologique — Dieu pèse lourd où Pharaon pesait lourd. « Ils "
        "SAURONT que je suis Jéhovah » (14:4, 18) : la formule de connaissance (6:7 ; "
        "Éz 36:23…) — les Égyptiens « sauront » en se noyant (14:25, « fuyons ! "
        "Jéhovah combat pour eux ! » — confession des chars enlisés !)."
    ),
    interpretation=(
        "LA POURSUITE (14:8-10 — P044) : « Jéhovah affermit le cœur de Pharaon… il "
        "poursuivit » — 600 chars d'ÉLITE (bahur, choisis, 14:7) + « tous les chars » "
        "+ cavaliers + « officiers » (shalishim) : l'armée professionnelle au complet "
        "contre des esclaves à pied — « ils les rattrapèrent » (14:9, au campement, "
        "Pi-Hahiroth face à Baal-Tsephôn). L'ENTRÉE (14:23 — P044) : « tous les "
        "chevaux, chars et cavaliers entrèrent derrière eux AU MILIEU de la mer » — "
        "l'obstination annoncée (14:4, 17) marche entre deux murs d'eau. LA NUIT : "
        "colonne entre les deux camps (14:19-20, ténèbres d'un côté, lumière de "
        "l'autre !), veille du matin (14:24, TM : « 2h à 6h environ »), roues ôtées "
        "(14:25, « il fit dévier les roues »), confession (« fuyons ! »), eaux "
        "revenues (14:26-28) — « PAS UN SEUL ne resta » (14:28 — P044 : exhaustivité "
        "du jugement)."
    ),
    hist=(
        "CHARS (14:7, 600 bahur + tous) : le char égyptien (XVIIIe dynastie : caisse "
        "légère, 2 chevaux, arc composite — arme absolue du Bronze récent) — Pharaon "
        "engage son arme stratégique contre des piétons : disproportion maximale, "
        "défaite maximale (Ps 20:8, « les uns les chars… nous le nom ! »). « MAIN "
        "LEVÉE » (14:8, beyad rama) : sortir en vainqueurs (cf. Nb 33:3, même formule "
        "pour la sortie !) — puis la peur au rattrapage (14:10-12, « laisse-nous "
        "servir ! ») : la main levée retombe, Dieu la relève (14:13-14, « Jéhovah "
        "combattra pour vous »). CANTIQUE (Ex 15) : « le cheval et son cavalier, il "
        "les a jetés à la mer » (15:1, 21 — refrain de Moïse ET de Miriam : la "
        "poursuite devient chant). RAHAB (Jos 2:10) : « nous avons appris » — 40 ans "
        "après, Canaan récite 14:28."
    ),
    geo=(
        "PI-HAHIROTH (« bouche des gorges » ? — 14:2, 9) : entre MIGDOL (forteresse, "
        "« tour ») et la mer, « en face de BAAL-TSEPHÔN » (14:2, 9 — dieu cananéen de "
        "la tempête, « maître du nord » !) : Israël campe FACE au dieu des orages — "
        "et c'est Jéhovah qui soulève la tempête (14:21, vent ; 15:10, « ton souffle » !) : "
        "le toponyme EST la polémique. MER DES JONCS (yam-suf, 13:18 ; 15:4) : « mer "
        "Rouge » (LXX : erythra) — golfe de Suez ? lacs Amers ? (voir limites). "
        "ITINÉRAIRE : Ramsès → Souccoth → Étham (13:20, « au bord du désert ») → "
        "DEMI-TOUR vers Pi-Hahiroth (14:2) : Dieu fait rebrousser chemin — « pour "
        "que Pharaon dise… » (14:3) : la géographie est un appât. « MURS » (14:22, "
        "homah : muraille — à droite et à gauche : architecture liquide, pas "
        "gué asséché."
    ),
    sci=(
        "Vent d'est TOUTE LA NUIT (14:21, ruah qadim : vent d'est fort — le moyen "
        "naturel affiché !) : le récit DONNE le mécanisme (vent + nuit + refoulement) "
        "ET le miracle (murs, timing, retour commandé 14:26 — « étends ta main… que "
        "les eaux reviennent » : la mer obéit au bâton, pas au vent). Théories "
        "naturalistes (vent sur lagune — « wind setdown », modèles Drews 2010 sur un "
        "bras du Nil !) : compatibles avec le MOYEN (vent), jamais avec les MURS "
        "ni le TIMING (nuit exacte, retour sur ordre, « pas un seul ») — la fiche "
        "cite les modèles comme « moyen plausible », le miracle comme « commande ». "
        "Chars enlisés (14:25) : roues de bronze/cuir sur fond marin détrempé — "
        "physique exacte de l'enlisement (puis les murs reviennent : 14:28). Veille "
        "du matin (2h-6h, TM) : 4e veille — l'attaque à l'aube, heure classique "
        "(cf. Jg 7:19, Gédéon ; 1S 11:11, Saül)."
    ),
    schema=(
        "Sortie la MAIN LEVÉE (14:8) → DEMI-TOUR ordonné (14:2 : position absurde) → "
        "« Le désert s'est refermé » (lecture de Pharaon, 14:3) → ANNONCE : il "
        "poursuivra + je me GLORIFIERAI (kaved !) + ils SAURONT (14:4) → 600 chars "
        "d'élite + tous (14:7) → Rattrapage (14:9) → Peur (« laisse-nous servir ! », "
        "14:12) → « Jéhovah combattra » (14:14) → Colonne (ténèbres/lumière, 14:19-20) "
        "→ Vent + murs (14:21-22) → Entrée des Égyptiens (14:23) → 2h-6h : roues, "
        "« fuyons ! » (14:24-25) → Retour : PAS UN SEUL (14:28) → Cantique (ch. 15)."
    ),
    limites=(
        "Localisation du passage : golfe de Suez, lacs Amers, golfe d'Aqaba — DÉBAT "
        "OUVERT ; Pi-Hahiroth, Migdol, Baal-Tsephôn : identifications proposées, "
        "aucune certaine — la fiche cite les noms, pas les coordonnées. « Chars au "
        "fond de la mer » (prétendues découvertes : roues, ossements — Wyatt et "
        "autres) : NON VÉRIFIÉ, la fiche ne les cite pas comme preuves (ni pour ni "
        "contre : silence). Pharaon noyé ? Ex 14:28 dit l'armée (« pas un seul » des "
        "poursuivants) ; Ps 106:11 (« pas un seul ») et Ps 136:15 (« précipita "
        "Pharaon ») incluent le roi — la fiche note les deux niveaux (récit : armée ; "
        "psaumes : roi inclus). Modèles de vent : moyen, pas miracle — distinction "
        "maintenue."
    ),
    accomplissement=[(("14:2 (piège)", "Demi-tour : Pi-Hahiroth, face à Baal-Tsephôn")),
                     (("14:4 (annonce)", "Il poursuivra + gloire + savoir")),
                     (("14:7-9 (chasse)", "600 élite + tous ; rattrapage (P044)")),
                     (("14:13-14 (foi)", "« Tenez-vous… Jéhovah combattra »")),
                     (("14:19-22 (mer)", "Colonne + vent + murs")),
                     (("14:23 (entrée)", "Tous derrière eux dans la mer (P044)")),
                     (("14:24-25 (nuit)", "2h-6h : roues, « fuyons ! »")),
                     (("14:28 (retour)", "« Pas un seul » (P044)")),
                     (("Ex 15 (chant)", "Cheval et cavalier jetés"))],
    tl=[(("14:2 (piège)", "Demi-tour")),
        (("14:4 (annonce)", "Il poursuivra")),
        (("14:9 (chasse)", "Rattrapés")),
        (("14:22 (murs)", "À pied sec")),
        (("14:23 (entrée)", "Derrière eux")),
        (("14:28 (retour)", "Pas un seul"))],
    src=[("Exode 14 — Bible d'étude (4, poursuite ; 23-28, retour)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/14"),
         ("Exode 14 — lecture (Pi-Hahiroth, chars, mer)", "https://wol.jw.org/fr/wol/b/r30/lp-f/Rbi8/2/14"),
         ("Exode — Aperçu et texte (14, gloire sur Pharaon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001061106")],
    img="images/prophe_EX044_poursuite.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX045", titre="Un royaume de prêtres et une nation sainte",
    ref="Exode 19:5, 6",
    statut="Accomplie (application spirituelle)",
    cat="EX", syst="Alliance du Sinaï (offre → condition → accomplissement spirituel)",
    reg="Registre : Exode — P045 (19:5, 6 : Israël, royaume de prêtres, nation sainte) ; accomplissement 1P 2:9 ; Ré 5:10 [application spirituelle]",
    texte=[
        "« SI vous écoutez ma voix et gardez mon alliance. » (19:5 — SI !)",
        "« Vous serez pour moi un TRÉSOR PARTICULIER (segullah). » (19:5 — trésor !)",
        "« Car TOUTE LA TERRE est à moi. » (19:5 — toute la terre !)",
        "« Vous serez pour moi un ROYAUME DE PRÊTRES. » (19:6 — ROYAUME DE PRÊTRES !)",
        "« Et une NATION SAINTE. » (19:6 — sainte !)",
        "« Vous êtes une race choisie, une PRÊTRISE ROYALE. » (1P 2:9 — royale !)",
        "« Une NATION SAINTE, un peuple acquis. » (1P 2:9 — sainte !)",
        "« Tu en as fait un ROYAUME et des PRÊTRES. » (Ré 5:10 — royaume et prêtres !)",
        "« Et ils RÉGNERONT sur la terre. » (Ré 5:10 — régneront !)",
    ],
    contexte=(
        "Sinaï, 1513 — 3e mois (19:1), AVANT le Décalogue (ch. 20) et l'alliance (ch. 24). "
        "Dieu fait une OFFRE : « si… vous serez » (19:5-6) — proposition d'alliance à "
        "la nation entière, apportée par Moïse aux anciens (19:7), acceptée d'avance "
        "(« tout ce que Jéhovah a dit, nous le ferons », 19:8 — engagement PRÉALABLE, "
        "renouvelé en 24:7 !). « Segullah » (19:5, trésor particulier) : le trésor "
        "PRIVÉ du roi (cf. Qo 2:8, « trésors des rois » ; 1Ch 29:3, David donne sa "
        "segullah personnelle pour le Temple — or et argent MIS À PART !) : Israël "
        "sera le coffret réservé de Dieu. « Car toute la terre est à moi » (19:5) : "
        "le Propriétaire universel se choisit un trésor particulier — élection DANS "
        "l'universalité (cf. Dt 10:14-15, même logique !). L'offre est CONDITIONNELLE "
        "(« SI vous écoutez… SI vous gardez ») : alliance à clause."
    ),
    explication=(
        "« Mamlekhet kohanim » (19:6, royaume de prêtres) : génitif double — un ROYAUME "
        "composé de PRÊTRES (tout le peuple exerce la prêtrise !) ou un royaume "
        "POSSÉDÉ par des prêtres (souveraineté sacerdotale) : les deux sens convergent "
        "(pas de caste : TOUT Israël mêle couronne et encensoir). « Goy qadosh » "
        "(19:6, nation sainte) : qadosh = mis à part, séparé pour Dieu (cf. le "
        "« diadème saint » du grand prêtre, 28:36, « sainteté à Jéhovah » !) : la "
        "nation entière porte le diadème. « Race choisie, PRÊTRISE ROYALE (basileion "
        "hierateuma), nation sainte » (1P 2:9) : Pierre REPREND Ex 19:6 en grec (LXX : "
        "basileion hierateuma !) et l'applique aux CHRÉTIENS — citation formelle, "
        "transfert explicite. « Royaume et prêtres… ils régneront » (Ré 5:10) : Jean "
        "VOIT l'accomplissement — les achetés « de toute tribu, langue, peuple, "
        "nation » (5:9) règnent : le trésor s'est mondialisé."
    ),
    interpretation=(
        "ISRAËL CHARNEL : « Israël se voyait offrir la possibilité et l'honneur "
        "exceptionnels… à la condition expresse d'obéir. Mais Israël n'a pas rempli "
        "cette condition » (2014764) — « l'Israël selon la chair n'est jamais devenu "
        "et n'aurait jamais pu devenir une nation dont tous les membres fussent rois "
        "et prêtres » (1989084) : royauté (Juda/David) et prêtrise (Lévi/Aaron) "
        "restent SÉPARÉES — l'offre échoue au « SI ». LA NOUVELLE NATION : Pentecôte 33 "
        "(Ac 2 : 3 000 !) — « une nouvelle nation voit le jour » (2014764) : les "
        "oints deviennent « cohéritiers de Christ » (Rm 8:17), « prêtrise royale » "
        "(1P 2:9 — P045), « achetés avec le sang » (Ré 5:9 — P045) : 144 000 rois-prêtres "
        "(Ré 7:4 ; 14:1 ; 20:6, « ils régneront avec lui »). « La nouvelle alliance "
        "produit une nation sainte dont les membres ont l'honneur de devenir rois "
        "et prêtres dans le Royaume céleste » (2014764) — Ex 19:6 s'accomplit EN "
        "ESPRIT (registre : « application spirituelle »)."
    ),
    hist=(
        "SINAÏ 1513 (offre) → VEAU D'OR (rupture immédiate ! ch. 32 — le « si » "
        "trahi en 40 jours) → PRÊTRISE LÉVITIQUE (Aaronides + Lévites : prêtrise "
        "RESTREINTE, substitut de l'offre universelle — « la prêtrise demeura dans la "
        "lignée d'Aaron », it Prêtre) → ROYAUTÉ DAVIDIQUE (~1077 : couronne à Juda, "
        "encensoir à Lévi — jamais fusionnés ; Ozias frappé de lèpre pour avoir "
        "encensé, 2Ch 26:16-21 : la fusion est INTERDITE sous la Loi !) → "
        "PENTECÔTE 33 (Ac 2 : nouvelle nation, « prêtrise royale ») → 144 000 scellés "
        "(Ré 7 ; 14 — « achetés d'entre les hommes », 14:4) → RÈGNE (Ré 5:10 ; 20:6). "
        "MELCHISÉDEK (Gn 14:18, roi-PRÊTRE !) : le seul précédent de fusion — « à la "
        "manière de Melchisédek » (Ps 110:4 ; Hé 7) : Christ fusionne, les 144 000 "
        "suivent."
    ),
    geo=(
        "SINAÏ (offre, 19:5-6) → SION (Pentecôte, Ac 2 : la nouvelle nation naît à "
        "Jérusalem !) → « TOUTE TRIBU, LANGUE, PEUPLE, NATION » (Ré 5:9 : le trésor "
        "était national, il devient mondial) : la géographie de l'offre s'élargit en "
        "trois cercles (montagne → ville → monde). « Toute la terre est à moi » "
        "(19:5) : le Propriétaire parle du Sinaï mais possède le globe — l'élection "
        "d'Israël servait les nations (cf. Gn 12:3, « toutes les familles bénies » : "
        "le trésor est un INSTRUMENT, pas un bijou). Le TEMPLE (lieu de la prêtrise "
        "restreinte) → le CIEL (lieu de la prêtrise royale, Hé 8:1-2, « ministre du "
        "sanctuaire véritable ») : le sanctuaire suit le transfert."
    ),
    sci=(
        "Traités de suzeraineté (Hittites, Bronze récent — Mendenhall) : préambule "
        "(« je suis Jéhovah », 20:2) + prologue historique (« qui t'ai fait sortir », "
        "20:2 ; 19:4, « vous avez vu » !) + stipulations (Décalogue + Livre de "
        "l'alliance) + bénédictions/malédictions (Lv 26 ; Dt 28) : Ex 19-24 SUIT le "
        "genre diplomatique du IIe millénaire — structure d'époque, pas de rédaction "
        "tardive (argument d'authenticité formelle). « Segullah » : trésor privé "
        "royal (attesté : Qo 2:8 ; 1Ch 29:3 ; Mal 3:17, « mon trésor » eschatologique !) "
        "— topique du Proche-Orient (trésors de Toutânkhamon : le pharaon a sa "
        "segullah funéraire ; Jéhovah a la sienne vivante). LXX : « basileion "
        "hierateuma » (Ex 19:6) = 1P 2:9 mot pour mot : Pierre cite la SEPTANTE — "
        "filiation textuelle grecque établie."
    ),
    schema=(
        "Sinaï 3e mois : OFFRE (« si… vous serez ») → Trésor privé (segullah) car "
        "toute la terre est à moi → ROYAUME DE PRÊTRES + NATION SAINTE → « Nous "
        "ferons » (19:8, engagement préalable) → 40 jours : VEAU (le « si » trahi) → "
        "Prêtrise restreinte (Aaron) + royauté séparée (David) — jamais fusionnées "
        "(Ozias frappé !) → Pentecôte 33 : NOUVELLE NATION → 1P 2:9 (citation "
        "formelle !) → 144 000 achetés (Ré 5:9) → « Royaume et prêtres… ils "
        "régneront » (Ré 5:10)."
    ),
    limites=(
        "Statut « application spirituelle » (registre) : l'accomplissement LITTÉRAL "
        "national n'a pas eu lieu (Israël charnel : échec au « si ») — la fiche suit "
        "le registre (1P 2:9 ; Ré 5:10). 144 000 : nombre de Ré 7:4 et 14:1 — littéral "
        "pour les sources citées (1989084 : « l'ensemble des 144 000 ») ; autres "
        "lectures (symbolique) existantes — la fiche suit ses sources, sans "
        "polémique. Traités hittites : parallélisme de GENRE (structure), pas de "
        "dépendance (contenu : l'alliance biblique est unique par son monothéisme) — "
        "distinction maintenue. Ozias (2Ch 26) : preuve de la SÉPARATION sous la Loi — "
        "fait, pas interprétation."
    ),
    accomplissement=[(("1513 (offre)", "« Si… royaume de prêtres, nation sainte » (19:5-6)")),
                     (("1513 (oui)", "« Tout… nous le ferons » (19:8 ; 24:7)")),
                     (("1513 (rupture)", "Veau d'or : le « si » trahi en 40 jours (ch. 32)")),
                     (("Aaron/David", "Prêtrise + royauté SÉPARÉES (Ozias frappé, 2Ch 26)")),
                     (("33 (Pentecôte)", "Nouvelle nation : 3 000 (Ac 2)")),
                     (("1P 2:9", "« Prêtrise royale, nation sainte » (citation !)")),
                     (("Ré 5:9-10", "Achetés de toutes nations ; « ils régneront »")),
                     (("Ré 20:6", "« Prêtres… régneront avec lui »"))],
    tl=[(("1513 (offre)", "Si… vous serez")),
        (("Veau", "Le « si » trahi")),
        (("Aaron/David", "Séparés")),
        (("33", "Nouvelle nation")),
        (("1P 2:9", "Prêtrise royale")),
        (("Ré 5:10", "Ils régneront"))],
    src=[("Exode 19 — Bible d'étude (5-6, royaume de prêtres)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/19"),
         ("Vous deviendrez « un royaume de prêtres » (offre, condition, oints)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2014764"),
         ("Prêtre — Étude perspicace (privilège, prêtrise chrétienne, Ré 5)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003553")],
    img="images/prophe_EX045_pretres.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX046", titre="Le jour où je demanderai des comptes",
    ref="Exode 32:33, 34",
    statut="Accomplie",
    cat="EX", syst="Veau d'or (livre → ange → échéance → désert)",
    reg="Registre : Exode — P046 (32:33, 34 : le jour où je ferai rendre des comptes) ; accomplissement Ex 32:35 ; Nb 14:26-35",
    texte=[
        "« Fais-nous un dieu qui MARCHERA DEVANT nous ! » (32:1 — devant nous !)",
        "« Aaron façonna un VEAU avec un burin. » (32:4 — un veau !)",
        "« Voici tes dieux, Israël, qui t'ont fait monter ! » (32:4 — voici !)",
        "« Efface-MOI de ton livre, sinon ! » (32:32, Moïse — moi !)",
        "« C'est celui qui a PÉCHÉ que j'effacerai de MON LIVRE. » (32:33 — mon livre !)",
        "« Mon ange MARCHERA en avant de toi. » (32:34 — en avant !)",
        "« Et le JOUR où je demanderai des comptes (paqod), je les PUNIRAI. » (32:34 — LE JOUR !)",
        "« Jéhovah se mit à FRAPPER le peuple. » (32:35 — frappa !)",
        "« Vos CADAVRES tomberont dans ce désert. » (Nb 14:29 — cadavres !)",
        "« QUARANTE ANS, un an par jour. » (Nb 14:33-34 — quarante ans !)",
    ],
    contexte=(
        "Sinaï, 1513 — Moïse est sur la montagne depuis 40 jours (24:18). En bas, "
        "l'angoisse : « fais-nous un dieu qui MARCHERA DEVANT nous » (32:1 — devant : "
        "ils veulent un guide VISIBLE, un totem de tête de colonne !). Aaron cède : "
        "boucles d'or fondues, veau au burin (32:2-4), autel, « fête pour Jéhovah » "
        "(32:5 — syncrétisme : le veau AU NOM de Jéhovah ! « demain, fête »), puis "
        "orgie (« le peuple s'assit pour manger et boire, puis se leva pour s'amuser », "
        "32:6 — Paul citera : « ne devenons pas idolâtres », 1Co 10:7 !). Dieu voit "
        "(« ton peuple s'est corrompu », 32:7 — « TON peuple » : distanciation !), "
        "Moïse intercède (« efface-moi », 32:32 — offrande de soi, cf. Paul Rm 9:3 !), "
        "Dieu répond en TROIS points : le LIVRE (responsabilité), l'ANGE (conduite), "
        "le JOUR (échéance)."
    ),
    explication=(
        "« MON LIVRE (siphri) » (32:33) : le registre des vivants-approuvés (cf. Ps "
        "69:29, « effacés du livre des vivants » ; Da 12:1, « écrit dans le livre » ; "
        "Ré 20:12, « livres ouverts ») — « Jéhovah possède un livre où il écrit le nom "
        "des fidèles » (1987648) ; « celui qui a PÉCHÉ… j'effacerai » : responsabilité "
        "INDIVIDUELLE (cf. Dt 24:16 ; Éz 18:4, 20 — pas de condamnation collective "
        "aveugle : chacun répond) ; « même après inscription, Dieu PEUT effacer » "
        "(1987648 : pas de prédestination verrouillée — le salut se GARDE, cf. Ré 3:5, "
        "« je n'effacerai pas » !). « Le JOUR (beyom) où je demanderai des comptes » "
        "(32:34, paqad : visiter/inspecter/punir — MÊME verbe que Joseph, 50:24 ! « "
        "Dieu vous visitera » : la visite qui sauve (Joseph) et la visite qui punit "
        "(veau) partagent le mot — Dieu visite, en bien ou en jugement). Triple "
        "réponse : justice (livre) + grâce (ange : la marche continue !) + échéance "
        "(jour : la dette reste inscrite)."
    ),
    interpretation=(
        "FRAPPE IMMÉDIATE (32:35 — P046) : « Jéhovah frappa (yiggoph, plaie) le peuple, "
        "parce qu'ils avaient fait le veau » — acompte (après les 3 000 des Lévites, "
        "32:28 : glaive PUIS plaie — double acompte). ÉCHÉANCE DIFFÉRÉE (Nb 14:26-35 "
        "— P046) : à Qadès, 2 ans plus tard, les espions font « murmurer » (14:2, 27) — "
        "« le JOUR » arrive : « vos cadavres tomberont dans ce désert » (14:29, 32), "
        "« 40 ans… UN AN PAR JOUR » (14:33-34 : les 40 jours d'exploration convertis "
        "en 40 ans — tarif affiché !), « vous saurez ce que c'est que mon OPPOSITION » "
        "(14:34 — même mot qu'en Lé 26, qeri !). Le veau (Sinaï) et les espions "
        "(Qadès) : même incrédulité, même génération — le « jour » de 32:34 s'exécute "
        "en 14:26-35 : TOUTE la génération de la sortie meurt au désert (sauf Josué et "
        "Caleb, 14:30, 38 — les deux fidèles survivent : le LIVRE distingue !). "
        "SYMÉTRIE : 3 000 tués au Sinaï (32:28) / 3 000 sauvés à la Pentecôte (Ac 2:41) "
        "— lecture proposée (même chiffre, alliance ancienne/nouvelle)."
    ),
    hist=(
        "VEAU (eguel, 32:4) : taurillon — Apis de Memphis ? taureau de culte cananéen ? "
        "(les deux : Israël sort d'Égypte avec des yeux égyptiens — « dieux d'or », "
        "32:31 : pluriel !). TABLES BRISÉES (32:19) : Moïse « jeta les tablettes » "
        "(vues du camp en fête !) — l'alliance brisée AVANT d'être lue : 40 jours "
        "d'écriture divine (31:18, « écrites du doigt de Dieu » !) fracassées en un "
        "geste. POUDRE BUE (32:20) : veau brûlé, broyé, dispersé sur l'eau, « il en "
        "fit boire » — épreuve d'ordalie ? (cf. Nb 5, eaux amères de la femme "
        "soupçonnée : même procédure !). LÉVITES (32:26-29, « pour Jéhovah ! » — "
        "3 000 morts, « consacrez-vous » : le sacerdoce lévitique NAÎT du glaive, "
        "cf. P028 !). QADÈS (Nb 13-14, an 2) : 12 espions, 40 jours, 10 décourageurs "
        "(« nous étions comme des sauterelles », 13:33 !) → 40 ans."
    ),
    geo=(
        "SINAÏ (crime, 32:1-6) : AU PIED de la montagne de l'alliance (ch. 19-24 en "
        "haut, veau en bas — simultanéité : Dieu écrit PENDANT qu'ils dansent ! "
        "32:7-8, « descends, car ton peuple… »). HOREB (deuil, 33:6, « ils ôtèrent "
        "leurs parures » — les parures du veau (32:2-3, boucles !) ôtées pour deuil : "
        "l'or de l'idole devient l'or du deuil). QADÈS-BARNÉA (sentence, Nb 13:26 ; "
        "14:26-35) : oasis du Néguev, porte sud de Canaan — « 11 journées d'Horeb » "
        "(Dt 1:2) : 11 jours de marche, 40 ans de cadavres (Dt 1:46 ; 2:14, « 38 ans » "
        "de Qadès au torrent de Zéred !). DÉSERT-CIMETIÈRE : « vos cadavres tomberont » "
        "(14:29) — le désert devient nécropole nationale (Ps 95:10-11, « 40 ans cette "
        "génération m'a écœuré » — repris en Hé 3:17 !)."
    ),
    sci=(
        "Métallurgie : « façonna avec un BURIN (heret) » (32:4) — fonte + ciselure : "
        "orfèvrerie du Bronze récent (moules, burins de bronze — ateliers attestés ; "
        "veau d'or de Béthel/Dan, 1R 12:28 : même technique, 500 ans plus tard !). "
        "« Maggefa » (32:35, frappe/plaie) : épidémie punitive (cf. Nb 11:33, cailles ; "
        "16:46-50, Coré : 14 700 morts ! ; 25:9, Baal-Péor : 24 000 !) — le désert "
        "compte ses plaies. Arithmétique pénale : 40 jours → 40 ans (Nb 14:34, « un "
        "an par jour » — yamim/shanim : la proportion est AFFICHÉE comme tarif : "
        "justice mesurée, pas arbitraire). Ps 95 / Hé 3-4 : « aujourd'hui, si vous "
        "entendez » — la génération du désert devient CAS D'ÉCOLE permanent (le "
        "« jour » de 32:34 enseigne encore : « prenez garde », Hé 3:12 !)."
    ),
    schema=(
        "40 jours d'attente → « Fais-nous un dieu DEVANT ! » (guide visible) → Boucles "
        "fondues + burin = VEAU → « Voici tes dieux ! » + « fête pour Jéhovah » "
        "(syncrétisme !) → « Ton peuple s'est corrompu » (distanciation) → « Efface-MOI "
        "(Moïse s'offre) → TRIPLE réponse : LIVRE (chacun répond) + ANGE (la marche "
        "continue) + JOUR (dette inscrite, paqad !) → Tables brisées + 3 000 + plaie "
        "(acomptes, 32:19-35) → Qadès : murmure → LE JOUR : cadavres + 40 ans "
        "(Nb 14:26-35) → Josué/Caleb survivent (le livre distingue !)."
    ),
    limites=(
        "Nature de la plaie (32:35) : non décrite (maggefa : frappe — maladie ? "
        "calamité ?) — la fiche cite le mot, pas de diagnostic. Lien 32:34 → Nb 14 : "
        "établi PAR LE REGISTRE (P046 : 32:35 + Nb 14:26-35) — la fiche suit (le « jour » "
        "= Qadès, 2 ans plus tard ; la dette du veau s'ajoute au murmure). 3 000 / "
        "3 000 (Sinaï/Pentecôte) : symétrie PROPOSÉE (même chiffre, Ac 2:41), signalée "
        "comme lecture — pas comme verset. Ordalie (poudre bue, 32:20 // Nb 5) : "
        "rapprochement suggéré (procédure analogue), pas affirmé. Livre : métaphore "
        "du souvenir/approbation (1987648), pas registre matériel."
    ),
    accomplissement=[(("1513 (veau)", "« Fais-nous un dieu DEVANT ! » + burin (32:1-6)")),
                     (("1513 (rupture)", "« Ton peuple corrompu » ; tables brisées (32:7-19)")),
                     (("1513 (offre)", "« Efface-MOI » (32:32)")),
                     (("1513 (réponse)", "LIVRE + ANGE + JOUR (paqad, 32:33-34)")),
                     (("1513 (acomptes)", "3 000 (v. 28) + plaie (v. 35)")),
                     (("1512 (Qadès)", "Espions : murmure, « sauterelles » (Nb 13-14)")),
                     (("Nb 14:26-35", "LE JOUR : cadavres + 40 ans (P046)")),
                     (("Josué/Caleb", "Survivent : le livre distingue (14:30, 38)"))],
    tl=[(("1513 (veau)", "« Devant nous ! »")),
        (("Tables", "Brisées")),
        (("32:33-34", "Livre + ange + jour")),
        (("32:35", "Plaie")),
        (("Qadès", "Murmure")),
        (("Nb 14", "40 ans"))],
    src=[("Exode 32 — Traduction du monde nouveau (33-34, livre, jour)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/2/32"),
         ("Questions de lecteurs (livre de vie, noms écrits et effacés)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1987648"),
         ("Nombres 14 — Bible d'étude (26-35, cadavres, 40 ans)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/14")],
    img="images/prophe_EX046_comptes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX047", titre="Pars : un ange devant toi vers le lait et le miel",
    ref="Exode 33:1-3",
    statut="Accomplie",
    cat="EX", syst="Montée promise (ange → chasse → héritage → repos)",
    reg="Registre : Exode — P047 (33:1-3 : montée vers le pays ; un ange devant eux) ; accomplissement Jos 1:2-6 ; 11:23",
    texte=[
        "« PARS d'ici, avec le peuple que TU as fait sortir. » (33:1 — pars !)",
        "« Vers le pays que j'ai JURÉ à Abraham, Isaac et Jacob. » (33:1 — juré !)",
        "« J'ENVERRAI UN ANGE DEVANT TOI. » (33:2 — un ange !)",
        "« Et je CHASSERAI les six peuples. » (33:2 — chasserai !)",
        "« Vers un pays RUISSELANT DE LAIT ET DE MIEL. » (33:3 — lait et miel !)",
        "« Car je ne monterai pas au milieu de toi. » (33:3 — pas au milieu !)",
        "« Peuple au COU RAIDE, je t'exterminerais en chemin. » (33:3 — cou raide !)",
        "« LÈVE-TOI, PASSE ce Jourdain. » (Jos 1:2 — passe !)",
        "« TOUT lieu que foulera votre pied, je vous le donne. » (Jos 1:3 — tout lieu !)",
        "« Josué prit TOUT le pays… et le pays fut EN REPOS. » (Jos 11:23 — EN REPOS !)",
    ],
    contexte=(
        "Sinaï, 1513 — après le veau (ch. 32), après l'intercession (32:30-34), après "
        "le deuil (33:4-6, parures ôtées « depuis Horeb » !). ORDRE DE DÉPART : « pars "
        "d'ici » (33:1, lekh : marche ! — même verbe qu'à Abraham, Gn 12:1, « va » ! : "
        "l'Exode reprend la Genèse). MAIS avec une clause terrible : « le peuple que "
        "TU as fait sortir » (33:1 — TU, pas « mon » : distanciation post-veau, cf. "
        "32:7 !) et « je ne monterai pas au milieu de toi » (33:3 — présence RETIRÉE : "
        "l'ange suffira, Dieu se retire pour ne pas consumer !). Moïse NÉGOCIE "
        "(33:12-17 : « si ta face ne vient pas, ne nous fais pas partir ! » — marchandage "
        "des pronoms : « TON peuple » (33:12) contre « TU » (33:1) !) et obtient « ma "
        "FACE ira » (33:14, panay : face/présence — TM : « ma face » !). Le départ "
        "est relancé — avec l'ange DEVANT et la face DEDANS."
    ),
    explication=(
        "« J'ENVERRAI (veshalahti) un ange (malakh) DEVANT (lephanekha) toi » (33:2) : "
        "le MÊME ange qu'en 23:20 (« voici, j'envoie un ange devant toi pour te garder "
        "en chemin ») et 32:34 (« mon ange marchera en avant ») — « mon nom est EN "
        "LUI » (23:21 !) : l'ange porte le Nom, il est plénipotentiaire (« ne "
        "l'irrite pas, il ne pardonnera pas », 23:21 : pleins pouvoirs !). « Je "
        "CHASSERAI (vegerashti) » (33:2) : Dieu chasse (l'ange ouvre, Dieu expulse — "
        "division du travail : 23:27-30, « terreur… frelons… petit à petit » !). SIX "
        "peuples (33:2 : Cananéens, Amorites, Hittites, Perizzites, Hivites, Jébuséens — "
        "la liste standard ; Dt 7:1 ajoute les Girgashites = 7 ; Gn 15:19-21 en "
        "compte 10 ! — listes conventionnelles, voir limites). « LAIT ET MIEL » "
        "(33:3, halav udevash) : pâturages (lait) + vergers/abeilles (miel — ou sirop "
        "de dattes, dibs !) : double richesse, pastorale ET sédentaire. « COU RAIDE » "
        "(33:3, qeshé-oref : nuque dure — bœuf qui refuse le joug : Né 9:16-17 "
        "reprendra l'image !)."
    ),
    interpretation=(
        "L'ORDRE À JOSUÉ (Jos 1:2-6 — P047) : 40 ans après, « Moïse mon serviteur est "
        "mort : LÈVE-TOI, passe ce Jourdain… TOUT lieu que foulera la plante de votre "
        "pied, je vous le donne, comme je l'ai dit à Moïse » — la promesse traverse "
        "le désert intacte (Moïse meurt, l'ordre survit : « comme dit à Moïse » !). "
        "LE REPOS (Jos 11:23 — P047) : « Josué prit TOUT le pays, selon tout ce que "
        "Jéhovah avait dit à Moïse… et le pays fut EN REPOS (shaqat) de la guerre » — "
        "l'ange a marché (le Chef de l'armée apparaît à Josué, 5:13-15, ÉPÉE DÉGAINÉE "
        "— « comme chef de l'armée de Jéhovah, je viens » !), les peuples sont "
        "chassés (Jéricho, Aï, Gabaon, Hesbon : Jos 6-11), le lait et le miel coulent "
        "(Guilgal : blé du pays, 5:11 !). « Et le pays fut en repos » — Hé 4:8 "
        "médiera : « si Josué leur avait donné le repos… » (le repos terrestre pointe "
        "le repos céleste !)."
    ),
    hist=(
        "NÉGOCIATION DES PRONOMS (33:1-17) : Dieu dit « TU as fait sortir » (33:1), "
        "« TON peuple » (32:7) ; Moïse répond « TON peuple » (33:12, 16), « TU m'as "
        "dit : je te connais par nom » (33:12) — Moïse rend à Dieu SON peuple à force "
        "de « ton » : joute grammaticale, victoire pastorale (« je ferai ce que tu "
        "dis », 33:17 !). TENTE HORS DU CAMP (33:7-11) : Moïse dresse la tente de "
        "réunion HORS du camp — « Jéhovah parlait à Moïse face à face » (33:11) ; "
        "Josué « ne s'éloignait pas » (33:11 — Rbi8 : le futur conquérant apprend "
        "dans la tente !). DEUIL (33:4-6) : « personne ne mit ses parures » — l'or "
        "du veau (32:2-3) devient le deuil d'Horeb : parures ôtées « depuis » ce jour. "
        "38 ANS (Dt 2:14, de Qadès à Zéred) : la montée promise en 33:1 attend la mort "
        "des murmureurs — l'ange patiente."
    ),
    geo=(
        "HOREB → QADÈS : « 11 JOURNÉES » (Dt 1:2 !) — le voyage promis tient en 11 "
        "jours de marche (~350 km) : la montée de 33:1 est un ordre de QUINZAINE, "
        "exécuté en 40 ANS (détour par le murmure !). SIX PEUPLES EN CARTE : Hittites "
        "(nord, empire — Hatsor ?), Cananéens (plaines et côtes), Amorites (montagnes), "
        "Perizzites (villages ouverts ?), Hivites (Gabaon, Sichem), Jébuséens "
        "(Jérusalem !) — Canaan morcelée en cités (lettres d'Amarna : roitelets "
        "quémandant Pharaon !) : pays divisé = pays prenable (stratégie divine : "
        "« petit à petit », 23:30 !). JOSUÉ 1-11 : Jourdain (3-4) → Jéricho (6) → Aï "
        "(7-8) → Gabaon (9-10, « soleil, arrête-toi ! ») → Hesbon (11) → REPOS (11:23) : "
        "l'itinéraire de l'ange, étape par étape. LAIT ET MIEL : pâturages de Galaad "
        "+ ruchers et dattes du Jourdain — écologie de l'abondance."
    ),
    sci=(
        "Amarna (XIVe s.) : ~350 lettres des vassaux cananéens à Pharaon (Abdi-Heba "
        "de Jérusalem ! Labaya de Sichem !) — Canaan divisée, suppliante, infiltrée "
        "d'Habiru : le contexte géopolitique de la conquête (pays morcelé, Égypte "
        "absente) — cadre cohérent, pas preuve directe. « Devash » (miel) : miel "
        "d'abeilles (ruchers : Jg 14:8, Samson ! 1S 14:25-27, Jonathan !) OU sirop de "
        "dattes (dibs — Tell… : production du Jourdain ; Dt 8:8, « miel » parmi les 7 "
        "produits !) — les deux lectures existent (la fiche cite les deux). « Panay » "
        "(face, 33:14, TM) : face = présence (cf. Ps 27:8, « cherche ma face » ; "
        "Nb 6:25, « fasse briller sa face ») — l'hébreu pense la présence en visage. "
        "Frelons (23:28, tsir'ah : frelons ? panique ? découragement ? — les trois "
        "lectures existent !) : la fiche note, ne tranche pas."
    ),
    schema=(
        "Veau → « Pars ! » (lekh, comme Abraham !) → MAIS « TON peuple » + « je ne "
        "monterai pas » (retrait !) → Deuil : parures ôtées (l'or du veau en deuil) → "
        "Tente hors camp : face à face + Josué apprenti → NÉGOCIATION (« TON peuple ! "
        "» × n) → « Ma FACE ira » (panay !) → ANGE devant (Nom en lui, 23:21) + "
        "6 peuples chassés (petit à petit !) → 11 journées… en 40 ans → « LÈVE-TOI, "
        "PASSE » (Jos 1:2) → Chef à l'épée (5:13) → Jéricho → Gabaon → Hesbon → "
        "REPOS (11:23)."
    ),
    limites=(
        "L'ange : « mon nom en lui » (23:21) — plénipotentiaire ; la fiche CITE, "
        "n'identifie pas au-delà (pas de christophanie dogmatisée dans cette fiche : "
        "hors registre). Listes des peuples : 6 (Ex 33:2), 7 (Dt 7:1, + Girgashites), "
        "10 (Gn 15:19-21 !) — VARIATION conventionnelle (listes formulaires, pas "
        "recensements) : la fiche le note comme fait littéraire, pas comme "
        "contradiction. « Devash » : abeilles ou dattes — débattu, les deux cités. "
        "Frelons (23:28) : insectes, panique ou découragement — non tranché. Amarna : "
        "cadre (XIVe s., postérieur à l'Exode 1513 dans la chronologie suivie — "
        "Canaan divisée AVANT et APRÈS : continuité du morcellement, pas datation)."
    ),
    accomplissement=[(("23:20 (annonce)", "« J'envoie un ange devant toi » + Nom en lui")),
                     (("1513 (ordre)", "« PARS » + ange + 6 peuples + lait/miel (33:1-3)")),
                     (("1513 (retrait)", "« Je ne monterai pas » ; deuil (33:3-6)")),
                     (("1513 (négo)", "« Ma FACE ira » (33:14-17)")),
                     (("1512-1473", "40 ans : l'ange patiente (murmure)")),
                     (("1473 (Josué)", "« LÈVE-TOI, PASSE » + tout lieu (Jos 1:2-6)")),
                     (("1473-1467", "Chef à l'épée ; Jéricho → Hesbon (Jos 5-11)")),
                     (("Jos 11:23", "TOUT le pays + REPOS (P047)"))],
    tl=[(("1513 (ordre)", "Pars + ange")),
        (("Retrait", "Je ne monterai pas")),
        (("Négo", "Ma face ira")),
        (("40 ans", "L'ange patiente")),
        (("Jos 1", "Lève-toi, passe")),
        (("Jos 11:23", "Repos"))],
    src=[("Exode 33 — lecture + notes (1-3, ange, lait et miel)", "https://wol.jw.org/fr/wol/b/r30/lp-f/Rbi8/2/33"),
         ("Exode 33 — Bible d'étude (pars, ange, cou raide)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/2/33"),
         ("Exode — Aperçu et texte (23:20 ; 33:1-2, ange devant)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001061106")],
    img="images/prophe_EX047_montee.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="EX048", titre="Si vous marchez en opposition : épée, peste, dispersion",
    ref="Lévitique 26:14-39",
    statut="Accomplie",
    cat="EX", syst="Malédictions de l'alliance (gradation → sièges → exils)",
    reg="Registre : Lévitique — P048 (26:14-39 : malédictions, épée, peste, famine, dispersion parmi les nations) ; accomplissement 2R 17:5-23 ; 25:1-11 ; Lm 4:9, 10",
    texte=[
        "« MAIS SI vous ne m'écoutez pas. » (26:14 — mais si !)",
        "« J'enverrai la TERREUR, la PHTISIE, la FIÈVRE. » (26:16 — terreur !)",
        "« Vous serez BATTUS devant vos ennemis. » (26:17 — battus !)",
        "« Je vous châtierai SEPT FOIS PLUS. » (26:18 — sept fois !)",
        "« Votre ciel sera de FER, votre terre d'AIRAIN. » (26:19 — fer et airain !)",
        "« J'enverrai les BÊTES SAUVAGES. » (26:22 — bêtes !)",
        "« L'ÉPÉE qui exécute la VENGEANCE DE L'ALLIANCE. » (26:25 — vengeance !)",
        "« J'enverrai la PESTE au milieu de vous. » (26:25 — peste !)",
        "« Vous mangerez la CHAIR de vos fils et de vos filles. » (26:29 — chair !)",
        "« Je vous DISPERSERAI parmi les nations. » (26:33 — DISPERSÉS !)",
        "« Le pays jouira de SES SABBATS. » (26:34 — ses sabbats !)",
        "« Les femmes ont CUIT leurs enfants. » (Lm 4:10 — cuit !)",
    ],
    contexte=(
        "Sinaï, 1513 — FIN du Lévitique : après les bénédictions (26:3-13, pluie, paix, "
        "poursuites victorieuses — « cinq de vous en poursuivront cent ! », 26:8), le "
        "VOLET SOMBRE de l'alliance (26:14-39) — structure de TRAITÉ (cf. Dt 28 ! "
        "traités hittites : bénédictions PUIS malédictions : le genre diplomatique du "
        "Bronze récent). GRADATION en 5 vagues (26:14-17, 18-20, 21-22, 23-26, 27-39), "
        "chacune : « SI… je frapperai SEPT FOIS PLUS » (26:18, 21, 24, 28 — crescendo : "
        "maladie → sécheresse → bêtes → guerre/peste/famine → cannibalisme/dispersion). "
        "« Qeri » (26:21, 23-24, 27-28 : marcher avec moi « en OPPOSITION / par hasard » "
        "— même mot pour l'hostilité et le hasard : traiter Dieu par-dessus l'épaule, "
        "comme un hasard !) : « si vous marchez avec moi par qeri, JE marcherai avec "
        "vous par qeri » (26:23-24 : réciprocité — le hasard rendu au hasard !)."
    ),
    explication=(
        "« SEPT FOIS (sheva) » (26:18, 21, 24, 28) : sept = plénitude (pas ×7 "
        "arithmétique : châtiment COMPLET, à chaque degré). « Ciel de FER, terre "
        "d'AIRAIN » (26:19) : métaux impénétrables — plus de pluie (ciel fermé), plus "
        "de labour (sol fermé) : sécheresse ABSOLUE (cf. Dt 28:23, même image !). "
        "« ÉPÉE VENGERESSE DE L'ALLIANCE (herev noqemet neqam-berit) » (26:25) : "
        "formule UNIQUE — l'alliance violée SE VENGE par l'épée (l'épée est "
        "l'huissier du contrat !). « DIX femmes cuiront dans UN four » (26:26) + "
        "« pain au POIDS » (rationné !) : famine quantitative (un four suffit — plus "
        "rien à cuire) ET qualitative (pesé — disette comptée). « SABBATS DU PAYS » "
        "(26:34-35) : le pays « jouira » (tirtseh : prendra plaisir !) de ses sabbats "
        "— l'exil est une JOIE pour la terre (enfin en repos !) : 2Ch 36:21 compte : "
        "70 ANS (607→537 : sabbats non observés rattrapés !). « DISPERSERAI (zariti) » "
        "(26:33, + « épée TIRÉE derrière vous » : exilés POURSUIVIS — pas de refuge !)."
    ),
    interpretation=(
        "SAMARIE (2R 17:5-23 — P048) : 740-718 — siège de 3 ANS (17:5), déportation "
        "(17:6 : Halah, Habor, Gozan, Médie — adresses de l'exil !), réquisitoire "
        "(17:7-23 : « à cause des péchés… ils rejetèrent ses ordonnances… Jéhovah "
        "rejeta toute la race » — le tribunal CITE la Loi : Lé 26 au banc des "
        "accusés !), colons païens (17:24 : Samaritains — syncrétisme : « ils "
        "craignaient Jéhovah ET servaient leurs dieux », 17:33 !). JÉRUSALEM (2R 25:1-11 "
        "— P048) : 609-607 — siège de 18 MOIS (25:1-2), « plus de pain » (25:3, "
        "famine ABSOLUE : Lé 26:26 !), brèche, fuite, Sédécias aveuglé (25:7), Temple "
        "BRÛLÉ (25:9 : « maison de Jéhovah » en cendres — 26:31, « je désolerai vos "
        "sanctuaires » !). CANNIBALISME (Lm 4:9-10 — P048) : Jérémie témoin — « mieux "
        "valent les morts de l'ÉPÉE que de la FAIM… les femmes ont CUIT leurs enfants » "
        "(Lé 26:29 mot pour mot : « vous mangerez la chair » !). DISPERSION (26:33) : "
        "Assyrie (nord) + Babylone (sud, 617/607/582) + Égypte (fuite, Jr 43-44 : "
        "« épée tirée derrière » — même en Égypte, poursuivis !)."
    ),
    hist=(
        "FAMINE DE SAMARIE (2R 6:25, siège de Ben-Hadad, ~850 : tête d'âne 80 sicles, "
        "fiente de colombe 5 sicles ! — 1001061116 : AVANT-GOÛT du catalogue, 130 ans "
        "avant la chute !). SALMANASAR/SARGON (740-720 : Osée vassal puis rebelle, "
        "17:3-4 — tribut puis complot avec l'Égypte : la corde se noue !). "
        "NABUCHODONOSOR (609-607 : 9e année de Sédécias, 10e mois, 10e jour — 25:1 : "
        "date au JOUR près ! — 11e année, 4e mois, 9e jour : brèche, 25:2-4). 70 ANS "
        "(2Ch 36:21 : « jusqu'à ce que le pays ait joui de ses sabbats » — 607→537 : "
        "la jachère forcée solde les sabbats volés !). RETOUR (537, Cyrus, Esd 1 — "
        "fin de la dispersion : Lé 26:40-45 prévoit le RETOUR si confession ! « je me "
        "souviendrai de mon alliance avec Jacob… Isaac… Abraham », 26:42 — les "
        "patriarches nommés à l'envers : Jacob d'abord !)."
    ),
    geo=(
        "DISPERSION EN CARTE : NORD → Halah, Habor (Khabour), Gozan, villes de Médie "
        "(2R 17:6 — haute Mésopotamie + Iran : ~1 500 km !) ; SUD → Babylone (Tell-Abib "
        "au Kébar, Éz 1:1-3 — l'exil a ses canaux !) ; FUITE → Égypte (Tahpanhès, Jr 43:7 "
        "— « épée tirée derrière » : Jr 44:27, « je veillerai sur eux pour le mal » !). "
        "PAYS « EN DÉSOLATION » (26:32-33) : « vos ennemis qui y habiteront en seront "
        "ÉTONNÉS » (26:32 — les colons stupéfaits du vide !) ; Gedaliah assassiné "
        "(2R 25:25), « du petit au grand » en Égypte (25:26) : le pays VIDE — sabbats "
        "intégraux. SIÈGES : Samarie (3 ans, 17:5), Jérusalem (18 mois, 25:1-3 — mur "
        "de siège, « plus de pain ») : la famine comme ARME (assiégeants assyriens et "
        "babyloniens : bas-reliefs de Lakish — le siège en images !)."
    ),
    sci=(
        "Poliorcétique : siège = famine programmée (mur de circonvallation, 25:1-2 ; "
        "stocks épuisés, « plus de pain », 25:3 ; prix délirants, 6:25 ; cannibalisme "
        "terminal, Lm 4:10 — SÉQUENCE documentée dans TOUS les sièges antiques : "
        "Josèphe, Guerre VI (Marie fille d'Éléazar, 70 de n. è. !) — parallèle, pas "
        "preuve). Épidémiologie : « peste au milieu de vous, rassemblés dans vos "
        "villes » (26:25) — promiscuité + famine + cadavres = épidémies : triade "
        "siège (guerre-peste-famine : les 4 cavaliers groupés, cf. Éz 14:21, « mes 4 "
        "jugements » !). Agronomie : « semerez en vain » (26:16, ennemis mangent), "
        "« force consumée pour rien » (26:20) — économie de la malédiction (cf. Aggée "
        "1:6, « bourse percée » !). 70 ans : 607→537 (chronologie suivie) — sabbats "
        "annuels manqués (~1/7 ans sur ~490 ans = 70 : 2Ch 36:21 fait le compte !)."
    ),
    schema=(
        "Sinaï 1513 : bénédictions (26:3-13) PUIS « MAIS SI… » (26:14) → 5 vagues × "
        "« SEPT FOIS PLUS » (maladie → sécheresse → bêtes → épée/peste/famine → "
        "cannibalisme/dispersion) → « Vengeance de l'alliance » (l'épée-huissier) → "
        "Samarie : 3 ans, déportés, réquisitoire citant la Loi (2R 17) → Jérusalem : "
        "18 mois, plus de pain, Temple brûlé (2R 25) → « Les femmes ont cuit » "
        "(Lm 4:10 = Lé 26:29 !) → Dispersion + épée tirée (Assyrie, Babylone, Égypte) "
        "→ 70 ans : le pays jouit (2Ch 36:21) → « Je me souviendrai » (26:42-45 : "
        "retour prévu !)."
    ),
    limites=(
        "Cannibalisme (26:29 ; Lm 4:10) : textes CITÉS sobrement — horreur de siège "
        "documentée (faits, pas complaisance) ; la fiche ne détaille pas au-delà des "
        "versets. « Sept fois » : plénitude symbolique, pas coefficient ×7 — lecture "
        "classique, signalée. 70 ans / 607 : chronologie suivie par les sources du "
        "projet (2Ch 36:21 ; Jr 25:11-12 ; 29:10) — autres datations (587/586) "
        "existantes en critique : la fiche suit son corpus, sans polémique (débats "
        "datationnels hors sujet : voir fiches Jr). Josèphe (70 de n. è.) : PARALLÈLE "
        "typologique (siège → famine → cannibalisme), jamais preuve de Lé 26 — "
        "distinction maintenue."
    ),
    accomplissement=[(("1513 (catalogue)", "5 vagues × sept fois ; vengeance ; dispersion (26:14-39)")),
                     (("~850 (avant-goût)", "Samarie : tête d'âne 80 sicles (2R 6:25)")),
                     (("740-718 (nord)", "3 ans ; déportés ; réquisitoire-Loi (2R 17:5-23)")),
                     (("609-607 (sud)", "18 mois ; plus de pain ; Temple brûlé (2R 25:1-11)")),
                     (("607 (témoin)", "« Les femmes ont cuit » (Lm 4:9-10)")),
                     (("Dispersion", "Assyrie + Babylone + Égypte (épée tirée)")),
                     (("607-537 (sabbats)", "70 ans : le pays jouit (2Ch 36:21)")),
                     (("537 (retour)", "« Je me souviendrai » (26:42-45 ; Esd 1)"))],
    tl=[(("1513 (catalogue)", "5 vagues × 7")),
        (("740-718", "Samarie tombe")),
        (("609-607", "Jérusalem brûle")),
        (("Lm 4:10", "Elles ont cuit")),
        (("Dispersion", "3 exils")),
        (("607-537", "70 sabbats"))],
    src=[("Lévitique 26 — Bible d'étude (14-39, malédictions)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/3/26"),
         ("Lévitique 26 — lecture (qeri, vengeance, dispersion)", "https://wol.jw.org/fr/wol/b/r30/lp-f/Rbi8/3/26"),
         ("Deuxième livre des Rois (17, Samarie ; 25, Jérusalem)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001061116")],
    img="images/prophe_EX048_dispersion.jpg",
))
