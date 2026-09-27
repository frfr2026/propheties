#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE I-J (vague de transition) — REVELATION (2e partie) + NOMMES D'AVANCE
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="I–J",
    nom="Le livre de la Révélation (2e partie) · Personnages et lieux nommés d'avance",
    vague="11",
    intro=(
        "Cette vague de transition ferme la catégorie I et ouvre la catégorie J. "
        "Côté Révélation, six dernières fiches : la bête de la mer (composite de "
        "Daniel 7, six têtes nommées, le coup mortel de 1914-1918), la bête de la "
        "terre et 666 (deux cornes d'agneau, le feu, l'image, la marque sur les "
        "actes et les pensées, 6 inférieur à 7 trois fois — variante 616 signalée), "
        "Babylone la Grande (le mystère, les eaux expliquées, les rois qui pleurent "
        "par égoïsme, « sortez », la meule), la moisson et la vendange (les trois "
        "anges, le mûr, le pressoir, les 1 600 stades), les bols et Harmaguédon "
        "(les dernières plaies, l'Euphrate, les grenouilles, le hapax, le tell de "
        "20 mètres, pas de guerre nucléaire) et le Roi guerrier (Alléluia, les "
        "noces, le ciel ouvert, le lac, les mille ans). La catégorie I compte ainsi "
        "10 fiches et est terminée. Côté nommés d'avance, trois premières fiches : "
        "Cyrus (deux siècles, berger et oint, « appelle ce qui n'est pas », le "
        "Grand Cyrus), Josias (300 ans, l'autel de Béthel debout trois siècles, la "
        "sépulture épargnée) et Bethléhem (Éphrata qui précise, les origines des "
        "temps indéfinis, le recensement qui fait monter). Périmètre : la suite de "
        "J et les catégories K-L appartiennent aux vagues suivantes."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I005", titre="La bête de la mer — composite, couronnée, blessée, adorée",
 ref="Révélation 13:1-10 ; Daniel 7:2-8, 21, 25 ; Ésaïe 57:20 ; Luc 4:6 ; Jérémie 15:2",
 statut="En cours (chevauchée politique ; 8e : voir I007)",
 cat="I", syst="Système puissances · 1914",
 reg="Registre : Révélation — P864 (13:1-2), P865 (13:3), P866 (13:4), P867 (13:5-6), P868 (13:7-8), P869 (13:8), P870 (13:9-10), P871 (13:1)",
 texte=[
  "« Une bête sauvage MONTE DE LA MER : 10 cornes, 7 têtes, DIADEMES sur les cornes, "
  "NOMS BLASPHÉMATOIRES sur les têtes. » (Ré 13:1 — le sable de 12:18 !)",
  "« LÉOPARD, pieds d'OURS, gueule de LION — le DRAGON lui DONNE puissance, trône, "
  "grand pouvoir. » (13:2 — composite de Daniel 7 ! edôken !)",
  "« Une tête MORTELLEMENT blessée — GUÉRIE — toute la terre suit avec ADMIRATION. » "
  "(13:3 — sphagmenèn !)",
  "« Ils adorent le DRAGON… ils adorent la BÊTE : QUI comparable ? QUI peut "
  "combattre ? » (13:4 — double adoration !)",
  "« GUEULE orgueilleuse, BLASPHÈMES — 42 MOIS — nom, TENTE, ciel blasphémés. » "
  "(13:5-6 — 1 260 jours !)",
  "« GUERRE aux saints — les VAINCRE — TOUTE tribu, peuple, langue, nation — tous "
  "adorent, sauf le ROULEAU de vie. » (13:7-8 — Da 7:21 !)",
  "« OREILLE : captivité… ÉPÉE… — ENDURANCE et FOI des saints. » (13:9-10 — "
  "hupomonè ! Jr 15:2 !)",
 ],
 contexte=(
  "« Sable de la mer » (12:18 — voir I004 : le dragon sur le sable → la bête sort "
  "de la mer !). « MER » (Is 57:20 : « les méchants… MER AGITÉE » ! — Is 17:12, Da 7:2 : "
  "voir E002 !). COMPOSITE : Daniel 7 (lion, ours, léopard, terrible — voir E002 !) — "
  "13:2 en reprend TROIS. « Dragon DONNE » (edôken, 13:2 — Lc 4:6 : « LIVRÉE » ! — Jn "
  "12:31, 14:30 !). « 7 TÊTES » (comme le dragon, 12:3 ! — « 7 ROIS », 17:9-10 : voir "
  "I007 ! — SIX nommées par l'illustration : ÉGYPTE, ASSYRIE, BABYLONIE, MÉDO-PERSE, "
  "GRÈCE, ROME — 7e : voir I007 !). « 10 cornes » (Da 7:7 — voir E002 !). « DIADEMES » "
  "(13:1 : SUR LES CORNES — dragon : sur les TÊTES, 12:3 — différence renvoyée, voir "
  "Limites). « NOMS blasphématoires » (« lutté… PRÉTENDU faire… ce que SEUL le Royaume » "
  "!). « Blessure MORTELLE » (« coup d'ÉPÉE », 13:14 — WWI : « coup MORTEL pendant le "
  "PREMIER conflit international » — guérie : voir I006 !). « 42 MOIS » (1 260 jours : "
  "voir F016 — Da 7:25 : voir E005 !). « VAINCRE » (Da 7:21 — voir E005 ! — 1918 : voir "
  "F016 !). « ROULEAU de vie » (Da 12:1 — voir H006 ! — « fondation… Agneau TUÉ » !). "
  "« Captivité… épée » (Jr 15:2, 43:11 ! — « ENDURANCE… FOI » : voir H010 !). Note "
  "catholique 1914 (Murphy : « 5 tombées… Rome… » — CITÉE comme parallèle !)."
 ),
 explication=(
  "« Monte » (anabainon : ÉMERGE !). « Thèrion » (BÊTE SAUVAGE !). « Diadèma » "
  "(DIADEMES : royauté !). « Blasphèmia » (noms CONTRE Dieu !). « Léopard-ours-lion » "
  "(Da 7 INVERSÉ : vitesse + force + gueule !). « Edôken » (DONNA : le dragon INVESTIT "
  "!). « Sphagmenèn » (ÉGORGÉE : 13:3 ! — « mortelle… GUÉRIE » : résurrection "
  "POLITIQUE !). « Thaumazô » (ADMIRATION : 13:3 !). « Tis homoios » (« QUI "
  "comparable » : 13:4 — chant de CULTE !). « Stoma » (GUEULE : 13:5 !). « Megala » "
  "(ORGUEILLEUSES : grandes !). « 42 MOIS » (3,5 ans : F016 !). « Skènè » (TENTE : "
  "13:6 — voir G005 !). « Polemos » (GUERRE : 13:7 !). « Nikèsai » (VAINCRE : aoriste !). "
  "« Pasa phylè » (TOUTE : 4 termes — voir G007 !). « Biblion » (ROULEAU : 13:8 !). "
  "« Ous » (OREILLE : 13:9 — « qui a » !). « Aichmalôsia » (CAPTIVITÉ : 13:10 !). "
  "« Machaira » (ÉPÉE : 13:10 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : l'organisation POLITIQUE — visible, "
  "terrestre (« forme CONTINUE… siècles… puissances SUCCÉDÉ »). « 7 têtes = 7 "
  "puissances » (SIX : Égypte → Rome — 7e : voir I007). « Cornes » (« avancer et "
  "COMBATTRE… au nom des sept »). « Noms » (prétention blasphématoire). « Coup mortel » "
  "(WWI : premier conflit INTERNATIONAL). « Guérie » (1920 : voir I006 — SDN !). "
  "« 42 mois » (voir F016). « Vaincre » (1918 : voir F016). « Adorent » (culte du "
  "politique : 13:4, 8 !)."
 ),
 accomplissement=[
  ("Égypte → Rome", "Six têtes : les puissances (illustration citée)"),
  ("~96 de n. è.", "« L'un EST » : Rome (voir I007)"),
  ("1914-1918", "Coup MORTEL : premier conflit international"),
  ("1920 de n. è.", "Guérie : l'image (voir I006)"),
  ("1914-1918", "42 mois : vaincre (voir F016)"),
  ("En cours", "« Adorent » : culte du politique"),
  ("8e (voir I007)", "« Était… n'est pas » : l'image montée"),
 ],
 hist=(
  "Six puissances (Égypte, Assyrie, Babylonie, Médo-Perse, Grèce, Rome — illustration "
  "CITÉE). WWI (« premier conflit INTERNATIONAL »). SDN (1920 : Genève — voir I006). "
  "Note Murphy 1914 (catholique : « 5… Rome… Antéchrist » — parallèle cité). Rome "
  "(~96 : « l'un est » — voir I007)."
 ),
 geo=(
  "« MER » (humanité détachée : Is 57:20 !). « Toute tribu… nation » (MONDE). « Sable » "
  "(12:18 : le dragon regarde). « Ciel » (blasphème : « ceux qui HABITENT »)."
 ),
 sci=(
  "SEPT : plénitude (voir I001). DIX : plénitude (voir I001). 42 mois = 1 260 jours "
  "(voir F016). Diadèma : ROYAUTÉ (grec). Biblion : ROULEAU (papyrus)."
 ),
 limites=(
  "Diadèmes (cornes contre têtes, 13:1 contre 12:3) : différence non expliquée ici — "
  "renvoyée. 7e tête : voir I007. Guérie (SDN) : détail voir I006. « Image » : voir I006."
 ),
 tl=[("Égypte", "Tête 1"), ("Rome", "Tête 6 : « est »"), ("1914-18", "Coup MORTEL"), ("1920", "Guérie : image"),
     ("42 mois", "Vaincre (F016)"), ("En cours", "« Adorent »")],
 src=[("Les bêtes de l'Apocalypse (mer, 7 rois, coup WWI, 1986)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986081"),
      ("Éviter la marque (mer = humanité, 7 têtes, 666, 1966)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1966405"),
      ("Révélation 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/13"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I005_bete.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I006", titre="La bête de la terre et 666 — l'agneau qui parle dragon",
 ref="Révélation 13:11-18 ; 1 Rois 18:38 ; Deutéronome 6:8 ; Exode 13:9 ; Ésaïe 6:3",
 statut="En cours (image : 1920+ ; « parle » : à venir)",
 cat="I", syst="Dates neutres (1919-1945) · symboles",
 reg="Registre : Révélation — P872 (13:11), P873 (13:12-13), P874 (13:14), P876 (13:16-17), P877 (13:18)",
 texte=[
  "« Une AUTRE bête monte de la TERRE : 2 cornes comme un AGNEAU — et elle PARLE "
  "comme un DRAGON. » (Ré 13:11 — contraste !)",
  "« Toute l'autorité de la première — faire ADORER la première, la GUÉRIE. » "
  "(13:12 — exousia !)",
  "« GRANDS signes : du FEU DESCEND du ciel aux YEUX des hommes. » (13:13 — "
  "sèmeia megala ! pyr ! — Élie, 1R 18 !)",
  "« Elle ÉGARE… : faites une IMAGE de la bête — ANIMÉE, elle PARLE, elle fait "
  "TUER les refusants. » (13:14-15 — eikôn ! pneuma !)",
  "« MARQUE sur main droite ou FRONT — sans elle : ni ACHETER ni VENDRE — nom ou "
  "NOMBRE du nom. » (13:16-17 — charagma !)",
  "« SAGESSE : CALCULE — nombre HUMAIN : 666. » (13:18 — sophia ! psèphizatô ! "
  "anthrôpou !)",
 ],
 contexte=(
  "« TERRE » (gè : contre MER — sens renvoyé, voir Limites). « 2 CORNES » (duo : la "
  "double puissance anglo-américaine — renvoi nominal !). « AGNEAU » (arnion : DOUCEUR "
  "apparente — « PARLE dragon » : paroles sataniques !). « FEU du ciel » (13:13 : Élie, "
  "1R 18:38 ! — « aux YEUX » : spectacle ! — voir H009 : signes !). « IMAGE » (eikôn, "
  "13:14 : SDN 1920 → ONU 1945 — renvoi nominal pour le détail !). « ANIMÉE » (pneuma : "
  "SOUFFLE — « PARLE » : laléô !). « Premier conflit » : GB + USA « favorisé "
  "l'ADORATION… amenant les nations à FAIRE UNE IMAGE » (après WWI !). « MARQUE » "
  "(charagma : gravure — CONTREFAÇON du sceau, voir G006 ! — Dt 6:8, Ex 13:9 : main + "
  "front du COMMANDEMENT !). « ACHETER… VENDRE » (agorazô : marché — voir G006 ! — "
  "PRESSION économique !). « 616 » (variante manuscrite : signalée, NON retenue — voir "
  "Limites)."
 ),
 explication=(
  "« DUO » (deux : DOUBLE puissance !). « Arnion » (AGNEAU : doux !). « Lalei » (PARLE : "
  "dragon !). « Exousia » (AUTORITÉ : de la première !). « Proskuneô » (ADORER : culte !). "
  "« Sèmeia megala » (GRANDS signes — voir H009 !). « Pyr » (FEU : 1R 18 ! — imitation "
  "d'Élie !). « Planaô » (ÉGARE — voir H009 !). « Eikôn » (IMAGE : copie — SDN→ONU : "
  "renvoi !). « Pneuma » (SOUFFLE : animée !). « Apokteinô » (TUER : les refusants !). "
  "« Charagma » (MARQUE : gravure, sceau !). « MAIN » (ACTES !) + « FRONT » (PENSÉES !) "
  "— CITÉ : « diriger nos vies… nos actions… notre pensée » ! « Agorazô » (ACHETER : "
  "marché !). « Sophia » (SAGESSE : 13:18 !). « Psèphizatô » (CALCULE : compter — "
  "psèphos : caillou !). « Anthrôpou » (HUMAIN : entité HUMAINE — pas démon !). « 666 » "
  "(6 < 7, voir I001 ! — ×3 : Is 6:3, triple SAINT — CONTRASTE : imperfection "
  "ACCENTUÉE — « jamais 7 » ! — « hauteur d'imperfection » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : DEUX cornes (double puissance : renvoi "
  "nominal). « Favorisé » (GB + USA après WWI : l'image !). FEU (imitation d'Élie — "
  "spectacle !). IMAGE (SDN → ONU : renvoi nominal). MARQUE (main = actes, front = "
  "pensées — « PAS laisser… diriger » !). 666 (HUMAIN ! — 6 contre 7, trois fois : "
  "imperfection accentuée !). « Acheter/vendre » (pressions quotidiennes : ENDURER — "
  "voir H010 !). 616 (variante : signalée — texte reçu : 666 !)."
 ),
 accomplissement=[
  ("1914-1918", "Coup mortel : voir I005"),
  ("1919-1920", "GB + USA : « favorisé » — IMAGE (SDN, Genève)"),
  ("1945 de n. è.", "ONU : San Francisco (renvoi nominal)"),
  ("En cours", "« Marque » : pressions acheter/vendre"),
  ("« Parle » (à venir)", "Image : tuer les refusants (I suite)"),
 ],
 hist=(
  "SDN (1920 : Genève — « image »). ONU (1945 : San Francisco — renvoi). GB + USA "
  "(1919 : « favorisé l'adoration »). Élie (1R 18 : feu du ciel !). Dt 6:8, Ex 13:9 "
  "(main + front : le commandement — CONTREFAÇON !). 616 (variante : signalée)."
 ),
 geo=(
  "« TERRE » (contre mer : renvoyé). « Ciel » (le feu DESCEND). « Marché » (acheter + "
  "vendre : MONDE). Genève, San Francisco (images : faits)."
 ),
 sci=(
  "6 < 7 : arithmétique SYMBOLIQUE (voir I001). ×3 : INSISTANCE (Is 6:3 : triple saint "
  "— contraste). 616 : VARIANTE manuscrite (signalée, non retenue). Psèphos : caillou "
  "à compter (CALCULE). Charagma : gravure, sceau (MARQUE)."
 ),
 limites=(
  "« Terre » (contre mer) : sens renvoyé. Double puissance : renvoi nominal. SDN → ONU : "
  "renvoi nominal pour le détail. 616 : signalée, non retenue (gématrie : non faite). "
  "« Image parle » : vagues suivantes."
 ),
 tl=[("1914-18", "Coup (I005)"), ("1919-20", "IMAGE : SDN"), ("1945", "ONU : renvoi"), ("En cours", "« Marque »"),
     ("À venir", "« Parle »")],
 src=[("Éviter la marque (image, marque, 666, calcul, 1966)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1966405"),
      ("Points marquants Révélation II (13:16-17, main, front, 2009)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2009124"),
      ("Révélation 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/13"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I006_666.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I007", titre="Babylone la Grande — le mystère, les eaux, la meule",
 ref="Révélation 17:1-18 ; 18:1-24 ; Ésaïe 21:9 ; Jérémie 50-51 ; 51:63-64",
 statut="En cours (« sortez » ; « une heure » : à venir)",
 cat="I", syst="Système Babel/539/1919",
 reg="Registre : Révélation — P898 (17:1-2), P899 (17:3-4), P900 (17:5), P901 (17:6), P902 (17:8), P903 (17:9-11), P904 (17:12-14), P905 (17:15-16), P906 (17:17), P907 (18:1-2), P908 (18:3), P909 (18:4-5), P910 (18:6-8), P911 (18:9-11), P912 (18:12-17), P913 (18:17-19), P914 (18:20), P915 (18:21-22), P916 (18:23-24) ; Ésaïe — P135 (21:1-10) ; Jérémie — P288 (51:1-14), P292 (51:45-48), P293 (51:49-58) ; 17:7, 18 sans entrée (C8)",
 texte=[
  "« La grande PROSTITUÉE assise sur les EAUX : rois FORNIQUÉ, habitants ENIVRÉS du "
  "VIN. » (Ré 17:1-2 — pornè !)",
  "« DÉSERT : femme sur bête ÉCARLATE — POURPRE, OR, perles — COUPE d'immondices — "
  "MYSTÈRE : Babylone la Grande, MÈRE des prostituées. » (17:3-5 — mustèrion !)",
  "« IVRE du SANG des saints, du SANG des témoins de Jésus. » (17:6 — methyô !)",
  "« ÉTAIT, N'EST PAS, monte de l'ABÎME, va à la DESTRUCTION. » (17:8 — logique "
  "temporelle !)",
  "« 7 MONTAGNES… 7 ROIS : 5 TOMBÉS, 1 EST, 1 À VENIR (peu) — la bête : 8e ROI. » "
  "(17:9-11 — orè !)",
  "« 10 cornes : PAS ENCORE rois — UNE HEURE avec la bête — MÊME intention — "
  "combattent l'AGNEAU — l'Agneau VAINCRA. » (17:12-14 — arnion !)",
  "« Les EAUX = peuples, foules, nations, langues. » (17:15 — le livre S'EXPLIQUE !)",
  "« Les cornes HAÏRONT : NUE, CHAIRS mangées, BRÛLÉE — Dieu a mis dans leur CŒUR. » "
  "(17:16-17 — phase 1, voir H006 !)",
  "« EST TOMBÉE… démons… SORTEZ d'elle, mon peuple — UN SEUL JOUR — UNE SEULE HEURE. » "
  "(18:2-10 — epesen ! exelthate ! — Is 21:9 !)",
  "« MEULE jetée : JAMAIS retrouvée — PHARMAKEIA : toutes nations ÉGARÉES — SANG des "
  "tués. » (18:21-24 — mulinos !)",
 ],
 contexte=(
  "« Ange aux BOLS » (17:1 — voir I009 : « VIENS, je te MONTRERAI » !). « DÉSERT » "
  "(17:3 : erèmos — lieu du jugement !). « ÉCARLATE » (kokkinos : la bête COPIE 13:1 !). "
  "« MYSTÈRE » (mustèrion, 17:5 !). « MÈRE » (mètèr : « DIRIGE l'institution » !). "
  "« IVRE » (methyô, 17:6 !). « ÉTAIT/N'EST PAS » (17:8 : SDN→ONU ? — « ABÎME » : "
  "1939-1945 ? — renvoi nominal !). « 7 MONTAGNES » (17:9 : orè — PAS Rome : « Rome… "
  "FER… LOI » — Rome MILITAIRE ≠ prostituée !). « 7 ROIS » (17:10 : 5 TOMBÉS — "
  "Égypte→Grèce, voir I005 ! — 1 EST : Rome, ~96 ! — 1 À VENIR : « peu » !). « 8e » "
  "(17:11 : l'image — renvoi !). « 10 cornes » (17:12 : « PAS ENCORE… UNE HEURE » !). "
  "« AGNEAU » (arnion, 17:14 — « Seigneur… Roi… VAINCRA » !). « Dieu CŒUR » (17:17 : "
  "« SON intention » — phase 1, voir H006 !). « GRANDE VILLE » (17:18 : polis — C8 !). "
  "18 : « TOMBÉE » (epesen, 18:2 — Is 21:9, P135 ! — « DÉMONS… OISEAUX » !). « SORTEZ » "
  "(exelthate, 18:4 — « mon PEUPLE » ! — Jr 51:45, P292 ! Is 48:20, sans P !). « UN JOUR » "
  "(18:8 — voir H006 !). « UNE HEURE » (18:10 — 17:12 !). « Marchands » (18:11-17 : "
  "luxe ! — « ÂMES » — 18:13 : sômata… psychas : TRAITE — corps ET âmes !). « MEULE » "
  "(mulinos, 18:21 — Jr 51:63-64, sans P : Seraya JETTE le livre ! — « JAMAIS » !). "
  "« PHARMAKEIA » (18:23 : SPIRITES — « TOUTES… ÉGARÉES » !). « SANG » (18:24 : "
  "« prophètes… saints… TUÉS » !)."
 ),
 explication=(
  "« Pornè » (PROSTITUÉE — contre l'ÉPOUSE, 19:7 : voir I010 !). « Kathèmai » (ASSISE : "
  "trône !). « Porneuô » (FORNIQUÉ : avec les ROIS !). « Oinos » (VIN : enivrant !). "
  "« Porphyra » (POURPRE : royal !). « Chrysos » (OR : richesse !). « Potèrion » "
  "(COUPE : immondices !). « Mustèrion » (MYSTÈRE : front !). « Mètèr » (MÈRE : source !). "
  "« Methyô » (IVRE : de sang !). « Abyssos » (ABÎME : 17:8 !). « Orè » (MONTAGNES : "
  "17:9 !). « Hora » (HEURE : 17:12 !). « Gnômè » (INTENTION : 17:13 !). « Nikèsai » (VAINCRA : l'Agneau !). « Hudata » (EAUX : 17:15 — 4 termes !). "
  "« Miseô » (HAÏRONT : 17:16 !). « Gymnè » (NUE : dépouillée !). « Katakaiô » "
  "(BRÛLÉE : complètement !). « Kardia » (CŒUR : Dieu met !). « Epesen » (TOMBÉE : "
  "18:2 !). « Exelthate » (SORTEZ : 18:4 !). « Mulinos » (MEULE : énorme !). "
  "« Pharmakeia » (SPIRITES : drogues + sortilèges !). « Planaô » (ÉGARÉES : 18:23 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « l'empire UNIVERSEL de la FAUSSE "
  "RELIGION » (« partie IMMONDE » du système !). « Milliers… NON regroupés » (« unis : "
  "OBJECTIFS + ACTIONS » !). « PAS Rome » (militaire de fer !). « Influence "
  "GOUVERNEMENTS » (considérable !). « Rois PLEURENT » (« ÉGOÏSTES » : « PARAVENT… "
  "RECRUTEMENT… SOUMISSION » — CITÉ !). « Gouvernements S'EN PRENDRONT » (« BIENTÔT » — "
  "« Dieu VEILLERA » !). « SORTEZ » (« AVANT qu'il soit TROP TARD » !). « JAMAIS "
  "retrouvée » (18:21 !)."
 ),
 accomplissement=[
  ("Babel (Gn 10-11)", "Nimrod : confusion — la « mère »"),
  ("AT", "Jr 50-51, Is 13, 21, Da 5 : Babylone jugée"),
  ("~96 de n. è.", "Vision : le mystère expliqué"),
  ("Siècles", "« Mère » : les filles (fornication, vin)"),
  ("1919 de n. è.", "Grand Cyrus : délivrance (voir J001)"),
  ("En cours", "« SORTEZ » : mon peuple (18:4)"),
  ("« Une heure » (à venir)", "Cornes : nue, mangée, brûlée (phase 1)"),
  ("« JAMAIS » (à venir)", "Meule : jamais retrouvée (18:21)"),
 ],
 hist=(
  "Babel (Gn 11 : confusion des langues !). 539 (chute AT — voir J001). 1919 "
  "(délivrance — Grand Cyrus, voir J001). Note Murphy 1914 (voir I005). Luxe antique "
  "(18:12-13 : cargaisons !). Seraya (Jr 51:63-64 : livre JETÉ dans l'Euphrate — "
  "sans P !)."
 ),
 geo=(
  "« EAUX » (peuples : 17:15 !). « DÉSERT » (17:3 : jugement !). « MONTAGNES » (17:9). "
  "« Grande VILLE » (17:18 — C8 !). « Marchands… MER » (18:17-19 : capitaines, "
  "matelots !)."
 ),
 sci=(
  "« Était/pas » : LOGIQUE temporelle (17:8). « UNE heure » : unanimité INSTANTANÉE "
  "(17:12). Meule : moulin ANTIQUE (énorme — 18:21). Pharmakeia : PHARMACIE (drogues + "
  "sortilèges). « Âmes » (18:13 : TRAITE — corps + âmes)."
 ),
 limites=(
  "7e et 8e rois : renvoyés aux publications. « Abîme » (17:8) : renvoi nominal. "
  "Jr 51:63-64, Is 48:20 : mentions sans P. Révélation 17:7, 18 sans entrée (C8)."
 ),
 tl=[("Babel", "« Mère »"), ("AT", "Jugée : Jr 51"), ("96", "Mystère"), ("Siècles", "Filles"),
     ("1919", "Grand Cyrus"), ("En cours", "« SORTEZ »"), ("À venir", "« 1 heure »"), ("« JAMAIS »", "Meule")],
 src=[("Babylone la Grande — Insight (description, pas Rome, marchands)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000531"),
      ("Un mystère : qui est Babylone ? (eaux, rois, mère, 1989)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1989240"),
      ("Points marquants Révélation II (rois pleurent, Q, 2009)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2009124"),
      ("Révélation 17 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/17")],
 img="images/prophe_I007_babylone.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I008", titre="La moisson et la vendange — mûre, pressoir, 1 600 stades",
 ref="Révélation 14:6-20 ; Joël 3:13 ; Ésaïe 63:1-6 ; Matthieu 13:39",
 statut="En cours (« dès maintenant » ; « mûre » : à venir)",
 cat="I", syst="Système 1914 · mesures",
 reg="Registre : Révélation — P880 (14:6-7), P881 (14:8), P882 (14:9-11), P883 (14:12), P884 (14:13), P885 (14:14-16), P886 (14:17-20) ; Joël — P428 (3:9-17) ; Mt 13:39 sans entrée (C8, voir H004)",
 texte=[
  "« ÉVANGILE ÉTERNEL… HEURE du jugement : CRAIGNEZ, ADOREZ le CRÉATEUR. » "
  "(Ré 14:6-7 — voir H004 ! hôra !)",
  "« Babylone la GRANDE est TOMBÉE : VIN CAPITEUX de son impudicité à TOUTES. » "
  "(14:8 — voir I007 ! Is 21:9 !)",
  "« Bête, image, MARQUE : VIN de Dieu SANS MÉLANGE — TOURMENT, FUMÉE, PAS DE REPOS. » "
  "(14:9-11 — akratou ! basanismos ! — renvoyé !)",
  "« ENDURANCE des saints : COMMANDEMENTS + FOI de Jésus. » (14:12 — hupomonè ! "
  "voir H010 !)",
  "« HEUREUX les morts… DÈS MAINTENANT : REPOSENT — leurs œuvres les SUIVENT. » "
  "(14:13 — aparti ! 2e makarios !)",
  "« NUÉE blanche : fils d'homme, COURONNE, FAUCILLE — LANCE : la moisson est MÛRE. » "
  "(14:14-16 — stephanos ! exèranthè !)",
  "« VENDANGE : RAISINS mûrs — jetée dans le GRAND PRESSOIR — HORS de la ville — "
  "SANG jusqu'aux MORS, 1 600 STADES. » (14:17-20 — lènos ! chalinos !)",
 ],
 contexte=(
  "« 3 ANGES » (14:6, 8, 9 : Éternel ! Tombée ! Marque !). « HEURE » (hôra, 14:7 !). "
  "« VIN » (oinos, 14:8, 10 : « CAPITEUX » !). « SANS MÉLANGE » (akratou, 14:10 : PUR !). "
  "« TOURMENT » (basanismos, 14:11 : « FUMÉE… siècles » — sens RENVOYÉ : destruction "
  "définitive — voir Limites). « DÈS MAINTENANT » (aparti, 14:13 : 1914+ !). « NUÉE "
  "BLANCHE » (nephelè leukè, 14:14 !). « COURONNE » (stephanos : 1914 — voir I002 !). "
  "« MÛRE » (exèranthè : DESSÉCHÉE !). « RAISINS mûrs » (èkmasan, 14:18 !). « PRESSOIR » "
  "(lènos, 14:19-20 !). « HORS de la ville » (14:20 !). « MORS » (chalinos : ~1,5 m !). "
  "« 1 600 STADES » (~300 km : « longueur Palestine » !). Joël 3:13 (P428 : « FAUCILLE… "
  "pressoir PLEIN… cuves REGORGENT » — « méchanceté GRANDE » !). Ésaïe 63:1-6 (sans P : "
  "« foulé SEUL… vêtements ROUGES » !). Mt 13:39 (« moisson = FIN… ANGES » — C8, voir "
  "H004 !)."
 ),
 explication=(
  "« Aionios » (ÉTERNEL — voir H004 !). « Hôra » (HEURE : 14:7 !). « Phobeô » "
  "(CRAIGNEZ !). « Ktizô » (CRÉÉ : mer, sources !). « Thymos » (CAPITEUX : fureur !). "
  "« Akratou » (SANS MÉLANGE : pur !). « Basanismos » (TOURMENT : renvoyé !). "
  "« Kapnos » (FUMÉE : 14:11 !). « Anapausis » (REPOS : « PAS » !). « Hupomonè » "
  "(ENDURANCE — voir H010 !). « Entolè » (COMMANDEMENTS !). « Pistis » (FOI !). "
  "« Makarios » (HEUREUX : 2e !). « Aparti » (DÈS MAINTENANT !). « Akoloutheô » "
  "(SUIVENT : œuvres !). « Nephelè » (NUÉE : blanche !). « Stephanos » (COURONNE : "
  "1914 !). « Drepanon » (FAUCILLE : affilée !). « Pempsom » (LANCE !). « Exèranthè » "
  "(DESSÉCHÉE : mûre !). « Trugaô » (VENDANGE !). « Staphylè » (RAISINS !). « Lènos » "
  "(PRESSOIR : grand !). « Chalinos » (MORS : ~1,5 m !). « Stadion » (STADE : ~185 m !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « NOTRE ÉPOQUE » (temps de la fin !). "
  "« ANGES SEULS capables » (ampleur de la tâche !). « 5e/6e anges » (vendange : "
  "14:17-18 !). « Vigne… JAMAIS racine » (définitif — « fruit MORTEL » ôté !). "
  "« Moisson = Harmaguédon » (« CARNAGE… faucille affilée » — CITÉ !). "
  "« Rassemblement » (adorateurs : lieu de FAVEUR — voir G007 !). « Cuve » (la colère : "
  "grandeur + sang !)."
 ),
 accomplissement=[
  ("Joël (AT)", "Faucille : « méchanceté GRANDE » (3:13)"),
  ("Ésaïe 63 (AT)", "Pressoir : « foulé SEUL » (sans P)"),
  ("33 de n. è.", "Mt 13:39 : « moisson = FIN » (C8)"),
  ("1914 + de n. è.", "« DÈS MAINTENANT » : heureux, reposent"),
  ("En cours", "« Mûre » : desséchée (exèranthè)"),
  ("« 1 600 » (à venir)", "Pressoir : sang, mors (voir I009)"),
 ],
 hist=(
  "Pressoir antique (foulé aux PIEDS !). Stade (~185 m : 1 600 ≈ 296 km !). Mors "
  "(~1,5 m : profondeur du sang !). « Ville » (Jérusalem : HORS !). Joël (sauterelles → "
  "faucille : P423-P428 !)."
 ),
 geo=(
  "« 1 600 » (Palestine NORD-SUD : ~300 km !). « Hors ville » (exclusion : 14:20). "
  "« Cuves » (Joël : REGORGENT !). « Mer, sources » (14:7 : Créateur !)."
 ),
 sci=(
  "1 600 × 185 m ≈ 296 km : CALCUL (Palestine !). « Mors » (~1,5 m : PROFONDEUR !). "
  "1 600 = 40 × 40 : CONSTAT arithmétique (pas d'interprétation — voir Limites). "
  "4 × 4 × 10 × 10 : CONSTAT (voir Limites). Exèranthè : DESSÉCHÉE (botanique !)."
 ),
 limites=(
  "« Tourment » (14:11) : sens renvoyé aux publications (destruction définitive). "
  "Ésaïe 63 : mention sans P. 1 600 : constats arithmétiques — PAS d'interprétation "
  "numérologique. Mt 13:39 sans entrée (C8 — voir H004)."
 ),
 tl=[("Joël", "Faucille : 3:13"), ("Is 63", "Pressoir : SEUL"), ("33", "Mt 13 : FIN"), ("1914 +", "« MAINTENANT »"),
     ("En cours", "« Mûre »"), ("À venir", "« 1 600 »")],
 src=[("L'écrasement de la vigne (époque, anges, cuve, 1966)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1966485"),
      ("Har-Maguédon, guerre d'un Dieu d'amour (moisson, 1600, 1985)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1985080"),
      ("Révélation 14 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/14"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I008_moisson.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I009", titre="Les bols et Harmaguédon — dernières, Euphrate, grenouilles, lieu",
 ref="Révélation 15:1-8 ; 16:1-21 ; Exode 7-10 ; Joël 3:2 ; Habaquq 2:3 ; Jérémie 25:33",
 statut="À venir (rassemblement ; « c'est fait » : à venir)",
 cat="I", syst="Système types · 96",
 reg="Registre : Révélation — P887 (15:1), P888 (15:2-4), P889 (15:5-8), P890 (16:1-2), P891 (16:3), P892 (16:4-7), P893 (16:8-9), P894 (16:10-11), P895 (16:12), P896 (16:13-16), P897 (16:17-21)",
 texte=[
  "« 7 DERNIÈRES plaies : la FUREUR MENÉE À TERME. » (Ré 15:1 — eschatai ! "
  "etelesthè !)",
  "« MER de verre + FEU — cantique de MOÏSE et de l'AGNEAU : JUSTES, VRAIES. » "
  "(15:2-4 — Ex 15 !)",
  "« Temple : FUMÉE — NUL ne pouvait ENTRER. » (15:8 — Ex 40 ! 1R 8 ! Is 6 !)",
  "« VERSEZ : ulcère (marque) — MER sang de MORT — FLEUVES sang. » (16:1-4 — "
  "phialè ! helkos !)",
  "« Tu es JUSTE, SAINT — sang des saints : sang À BOIRE — DIGNES — OUI. » "
  "(16:5-7 — dikaios ! axioi ! nai !)",
  "« SOLEIL brûle — TRÔNE ténèbres — langue mordue — PAS REPENTIS. » (16:8-11 — "
  "9:20-21 !)",
  "« EUPHRATE ASSÉCHÉ : rois de l'ORIENT — Cyrus ! » (16:12 — anatolè ! voir J001 !)",
  "« 3 bouches : GRENOUILLES — DÉMONS, SIGNES — rois du monde ENTIER rassemblés. » "
  "(16:13-14 — batrachoi ! Ex 8 !)",
  "« VOLEUR — HEUREUX qui veille : VÊTEMENTS, pas HONTE. » (16:15 — 3e makarios ! "
  "voir H001 !)",
  "« HAPAX : Har-Maguédon — en HÉBREU. » (16:16 — 1× dans la Bible !)",
  "« C'EST FAIT — SÉISME JAMAIS — Babylone COUPE — îles, montagnes — GRÊLE TALENT. » "
  "(16:17-21 — gegonen ! ~34 kg !)",
 ],
 contexte=(
  "« DERNIÈRES » (eschatai, 15:1 !). « TERMÉE » (etelesthè : ACHEVÉE !). « VERRE + FEU » "
  "(15:2 : Ex 24:10 ! Éz 1:22 !). « Moïse + Agneau » (15:3 : Ex 15 !). « FUMÉE » (15:8 : "
  "Ex 40:35 ! 1R 8:11 ! Is 6:4 !). « 7 BOLS » (phialè : COUPES ! — contre trompettes : "
  "TOTAL, pas tiers — APPEL puis JUGEMENT !). « JUSTE » (dikaios, 16:5 : « qui ES » !). "
  "« DIGNES » (axioi, 16:6 !). « OUI » (nai, 16:7 : l'AUTEL répond !). « Pas repentis » "
  "(16:9, 11 — 9:20-21 : voir I003 !). « EUPHRATE » (16:12 : Cyrus — voir J001 ! — « rois "
  "ORIENT » : anatolè — LEVER du soleil !). « GRENOUILLES » (batrachoi : Ex 8:6 ! — « 3 "
  "BOUCHES » : dragon, bête, FAUX PROPHÈTE !). « Démons » (daimonia, 16:14 : « PAROLES "
  "inspirées » !). « VOLEUR » (16:15 — voir H001 ! — « VÊTEMENTS » : himation — « HONTE » : "
  "aschèmosynè !). « Har-Maguédon » (HAPAX : 1× ! — « en HÉBREU » !). « C'EST FAIT » "
  "(gegonen, 16:17 — 21:6 : voir G005 !). « SÉISME JAMAIS » (16:18 !). « Babylone COUPE » "
  "(16:19 — voir I007 !). « TALENT » (~34 kg, 16:21 !). HAR-MAGUÉDON : « Har » (MONTAGNE !) "
  "+ « Meguiddo » (« RASSEMBLEMENT de troupes » !). « Tell 20 m » (PAS de montagne — "
  "mesure !). « Lieu » = TOPOS (CONDITION, situation !). « PAS nucléaire » (définition !). "
  "« PAS Moyen-Orient seul » (UNIVERSELLE — Jr 25:33 ! « TOUTE » !). « Rois… serviteurs » "
  "(représentants terrestres !). « Armées CIEL » (19:14 — voir I010 !). « Temps FIXÉ » "
  "(Ha 2:3 : « pas en RETARD » — sans P !). « Ruine… RUINENT » (11:18 — voir I003 !). "
  "Meguiddo : Débora (Jg 5:19 : « rois CANAAN… Taanak » !). Guidéon (Jg 7 : « 300… épée "
  "de JÉHOVAH » !). Josias (2R 23:29 — C8, voir J002 ! Néko !). Via Maris (ROUTE !). "
  "« 6e-7e bols » (rassemblent : 16:12 + 16:17-21 !)."
 ),
 explication=(
  "« Eschatai » (DERNIÈRES : 15:1 !). « Thymos » (FUREUR !). « Etelesthè » (ACHEVÉE !). "
  "« Hyalinè » (VERRE : 15:2 !). « Pyr » (FEU : mêlé !). « Ôdè » (CANTIQUE : Moïse !). "
  "« Dikaiai » (JUSTES : voies !). « Kapnos » (FUMÉE : 15:8 !). « Phialè » (BOLS : "
  "coupes !). « Ekcheô » (VERSEZ !). « Helkos » (ULCÈRE : 16:2 !). « Haima » (SANG : "
  "mer, fleuves !). « Nekros » (« de MORT » : 16:3 !). « Dikaios » (JUSTE : 16:5 !). "
  "« Hosios » (SAINT : 16:5 !). « Axioi » (DIGNES : 16:6 !). « Nai » (OUI : 16:7 !). "
  "« Kaumatizô » (BRÛLE : 16:8 !). « Skotos » (TÉNÈBRES : 16:10 !). « Xèrainô » "
  "(ASSÉCHÉ : 16:12 !). « Anatolè » (ORIENT : lever !). « Batrachoi » (GRENOUILLES : "
  "coassantes !). « Sèmeia » (SIGNES : démons !). « Himation » (VÊTEMENTS : 16:15 !). "
  "« Har » (MONTAGNE !). « Topos » (LIEU-condition !). « Gegonen » (C'EST FAIT !). "
  "« Seismos » (SÉISME : jamais !). « Talanton » (TALENT : ~34 kg !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « DERNIÈRES » (fureur à son terme !). "
  "TOTAL (contre tiers : trompettes = APPEL, bols = JUGEMENT !). « JUSTE » (vindication : "
  "16:5-7 !). « Cyrus » (Euphrate : TYPE — voir J001 !). « Grenouilles » (Ex 8 : "
  "propagande coassante — 3 bouches !). « Voleur » (voir H001 !). « HAPAX » (1× dans "
  "toute la Bible !). « PAS lieu » (condition mondiale !). « PAS nucléaire » "
  "(définition !). « Guerre de JÉHOVAH » (pas humaine — armées invisibles !). « Temps "
  "fixé » (Ha 2:3 : pas en retard !). « Paix ENSUITE » (voir G009 !)."
 ),
 accomplissement=[
  ("Exode (AT)", "Plaies : ulcère, sang, ténèbres, grêle (types)"),
  ("Cyrus (539)", "Euphrate asséché : TYPE (voir J001)"),
  ("Meguiddo (AT)", "Débora, Guidéon : TYPES décisifs"),
  ("~96 de n. è.", "Vision : les 7 bols"),
  ("1919 + de n. è.", "Bols : APPLICATION renvoyée aux publications"),
  ("« C'EST FAIT » (à venir)", "7e bol : séisme, grêle, Babylone"),
 ],
 hist=(
  "Ex 7-10 (ulcère, sang, ténèbres, grêle : 4 plaies reprises !). Ex 8:6 (grenouilles "
  "d'Égypte !). Cyrus (539 : Euphrate — voir J001). Débora (~1200 ? Jg 5 : Taanak !). "
  "Guidéon (Jg 7 : 300 !). Tell 20 m (archéologie : PAS de montagne !). Ha 2:3 (temps "
  "fixé — sans P)."
 ),
 geo=(
  "Euphrate (le GRAND fleuve : 16:12 !). Meguiddo (plaine de YIZRÉEL !). Via Maris "
  "(ROUTE des armées !). « Îles… montagnes » (16:20 : relief ôté !). « TOUTE terre » "
  "(universelle : 16:14 !)."
 ),
 sci=(
  "Talent (~34 kg : GRÊLON — 16:21 !). Tell 20 m : MESURE (pas de montagne !). HAPAX : "
  "1× — statistique (16:16 !). Topos : lieu = CONDITION (grec). Eschatai : DERNIÈRES "
  "(fin de série !)."
 ),
 limites=(
  "Bols : APPLICATION (proclamations ?) renvoyée aux publications. 2 Rois 23:29 "
  "sans entrée (C8 — voir J002). « Montagne » : pas de montagne — signalé. Habaquq 2:3 : "
  "mention sans P."
 ),
 tl=[("Exode", "Plaies : types"), ("539", "Cyrus : Euphrate"), ("Meguiddo", "Débora : type"), ("96", "Vision : 7"),
     ("1919 +", "Application : renvoi"), ("À venir", "« C'EST FAIT »")],
 src=[("Harmaguédon : un nouveau départ (lieu, universelle, temps, 2005)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2005881"),
      ("Har-Maguédôn — Insight (topos, futur, bols, voleur)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001884"),
      ("Har-Maguédon — définition (pas nucléaire, tell, Da 2:44)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101989210"),
      ("Révélation 16 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/16")],
 img="images/prophe_I009_bols.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="I010", titre="Le Roi guerrier — Alléluia, noces, ciel ouvert, lac",
 ref="Révélation 19:1-21 ; 20:1-6 ; Psaume 2:9 ; Ézéchiel 39:17-20 ; Ésaïe 63:1-6",
 statut="À venir (« ouvert » ; 1000 : voir F017)",
 cat="I", syst="Système 1914 (I002) · F017",
 reg="Registre : Révélation — P917 (19:1-2), P918 (19:6-8), P919 (19:9), P920 (19:10) ; 19:11-21 sans entrée (C8) ; ch. 20 : voir F017",
 texte=[
  "« ALLÉLUIA : SALUT, gloire — Babylone JUGÉE, sang VENGÉ. » (Ré 19:1-2 — voir "
  "G009 ! I007 !)",
  "« ALLÉLUIA : le Seigneur… RÈGNE — NOCES de l'Agneau — ÉPOUSE PRÊTE — LIN FIN. » "
  "(19:6-8 — gamos ! bussinos ! — 144 000, voir G006 !)",
  "« HEUREUX les INVITÉS au repas des noces. » (19:9 — 4e makarios ! — invités : "
  "renvoyés !)",
  "« ADORE DIEU : conserviteur — TÉMOIGNAGE de Jésus = ESPRIT de la prophétie. » "
  "(19:10 — sundoulos !)",
  "« Ciel OUVERT : BLANC — FIDÈLE et VÉRIDIQUE — yeux FLAMME — DIADEMES — NOM que nul "
  "— SANG — PAROLE de Dieu. » (19:11-13 — C8 ! logos !)",
  "« ARMÉES du ciel : BLANC, LIN — ÉPÉE de la bouche — FER — PRESSOIR foulé LUI-MÊME "
  "— ROI des rois. » (19:14-16 — C8 ! rhomphaia ! Ps 2:9 !)",
  "« SOUPER de Dieu : OISEAUX — CHAIR de rois… libres… esclaves. » (19:17-18 — C8 ! "
  "deipnon ! Éz 39 !)",
  "« Bête + ROIS + armées : GUERRE contre le cavalier — bête + FAUX PROPHÈTE : VIVANTS "
  "dans le LAC DE FEU — autres : ÉPÉE — oiseaux RASSASIÉS. » (19:19-21 — C8 !)",
 ],
 contexte=(
  "« ALLÉLUIA » (19:1, 3, 4, 6 : 4× — voir G009 !). « NOCES » (gamos, 19:7 ! — "
  "« ÉPOUSE » : gunè — les 144 000 : voir G006 ! — « LIN FIN » : bussinos — « ACTES "
  "JUSTES », 19:8 !). « HEUREUX » (19:9 : 4e makarios — « INVITÉS » : renvoyés, voir "
  "Limites). « ADORE DIEU » (19:10 : « CONSERVITEUR » — sundoulos ! — « TÉMOIGNAGE "
  "Jésus = ESPRIT PROPHÉTIE » !). « Ciel OUVERT » (19:11 — C8 !). « BLANC » (voir I002 : "
  "MÊME cavalier — « achève » !). « FIDÈLE… VÉRIDIQUE » (6:2 → 19:11 !). « FLAMME » "
  "(1:14 — voir I001 !). « DIADEMES » (diadèmata : PLURIEL — contre 1 COURONNE, 6:2 — "
  "constat, voir Limites). « NOM… NUL » (19:12 — C8 !). « SANG » (19:13 — C8 ! — Is 63, "
  "voir I008 !). « PAROLE » (logos : Jn 1:1 — voir I002 !). « ARMÉES » (strateumata, "
  "19:14 — « BLANC… LIN » !). « ÉPÉE » (rhomphaia : 1:16 — voir I001 !). « FER » (Ps 2:9 "
  "— 12:5 : voir I004 !). « PRESSOIR » (19:15 — voir I008 ! — « FOULE LUI-MÊME » !). "
  "« ROI… SEIGNEUR » (19:16 : « CUISSE » — renvoyée, voir Limites). « SOUPER » (deipnon, "
  "19:17 — « OISEAUX » — Éz 39:17-20, sans P !). « CHAIR » (19:18 : « rois… chefs… "
  "LIBRES… esclaves » !). « Bête… ROIS… GUERRE » (19:19 : « contre… armée » !). « Bête… "
  "FAUX PROPHÈTE » (19:20 : « VIVANTS… LAC DE FEU » — « SOUFRE » !). « ÉPÉE… RASSASIÉS » "
  "(19:21 !). Ch. 20 (voir F017 : ABÎME ! 1 000 ! RÈGNE ! 2e mort ! — voir G004 : "
  "résurrection !)."
 ),
 explication=(
  "« Hallèlou-YAH » (LOUEZ Yah — 4× !). « Gamos » (NOCES : 19:7 !). « Gunè » (ÉPOUSE : "
  "prête !). « Bussinos » (LIN FIN : actes justes !). « Makarios » (HEUREUX : 4e !). "
  "« Sundoulos » (CONSERVITEUR : 19:10 !). « Pneuma » (ESPRIT : de la prophétie !). "
  "« Èneôgmenon » (OUVERT : ciel !). « Leukos » (BLANC : justice !). « Pistos » "
  "(FIDÈLE !). « Alèthinos » (VÉRIDIQUE !). « Phlox » (FLAMME : yeux !). « Diadèmata » "
  "(DIADEMES : royautés !). « Onoma » (NOM : inconnu !). « Haima » (SANG : trempé !). "
  "« Logos » (PAROLE : Jn 1:1 !). « Strateumata » (ARMÉES : célestes !). « Rhomphaia » "
  "(ÉPÉE : longue !). « Sidèra » (FER : sceptre !). « Lènos » (PRESSOIR : foulé !). "
  "« Basileus » (ROI : des rois !). « Mèros » (CUISSE : inscription !). « Deipnon » "
  "(SOUPER : oiseaux !). « Sarx » (CHAIR : mangée !). « Limnè » (LAC : de feu !). "
  "« Theion » (SOUFRE !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « ALLÉLUIA » (Babylone jugée : voir G009, "
  "I007 !). « NOCES » (144 000-Épouse : voir G006 !). « ÉPOUSE PRÊTE » (19:7 !). "
  "« Invités » : renvoyés (voir Limites). « ADORE DIEU » (anges : conserviteurs !). "
  "« BLANC » (voir I002 : le MÊME — « achève sa victoire » !). « DIADEMES » (constat : "
  "1 → n !). « PAROLE » (Jn 1:1 !). « PRESSOIR » (voir I008 : foulé LUI-MÊME !). "
  "« SOUPER » (Éz 39 : Gog !). « LAC » (destruction — « 2e MORT », 20:14 : voir F017 !). "
  "Ch. 20 (voir F017 : millénium ! — voir G004 : résurrection !)."
 ),
 accomplissement=[
  ("1914 de n. è.", "Blanc : couronne (voir I002)"),
  ("Babylone (à venir)", "Jugée : voir I007 (phase 1)"),
  ("« ALLÉLUIA » (à venir)", "19:1-6 : salut, règne"),
  ("« NOCES » (à venir)", "19:7-9 : Épouse prête, invités"),
  ("« OUVERT » (à venir)", "19:11 : le Roi sort"),
  ("« LAC » (à venir)", "19:20 : bête + faux prophète"),
  ("1 000 (à venir)", "Ch. 20 : voir F017"),
 ],
 hist=(
  "Noces (coutume : CONTRAT, repas !). Souper (Éz 39 : Gog — sans P !). Lac (soufre : "
  "Sodome, Gn 19 !). Cuisse (inscription : COUTUME ? — renvoyée, voir Limites). "
  "« 2e mort » (20:14 : voir F017 !)."
 ),
 geo=(
  "« Ciel OUVERT » (19:11 : sortie !). « Zénith » (19:17 : soleil — oiseaux !). « Lac » "
  "(topographie FINALE : 19:20 !). « 1 000 » (terre : voir F017 !)."
 ),
 sci=(
  "« ALLÉLUIA ×4 » : COMPTE (19:1-6 !). « Couronne → diadèmes » (1 → n : CONSTAT — "
  "voir Limites). Limnè : LAC (2e mort !). « 1 000 » (voir F017 : ans solaires !). "
  "4e makarios (19:9 : liste I001 !)."
 ),
 limites=(
  "Révélation 19:11-21 sans entrée (C8). Invités (19:9) : identification renvoyée. "
  "Cuisse (19:16) : coutume renvoyée. Couronne/diadèmes (6:2/19:12) : constat, non "
  "expliqué. Ch. 20 : voir F017 (millénium, 2e mort)."
 ),
 tl=[("1914", "Blanc (I002)"), ("Babylone", "Jugée (I007)"), ("À venir", "« ALLÉLUIA »"), ("À venir", "« NOCES »"),
     ("À venir", "« OUVERT »"), ("À venir", "« LAC »"), ("1 000", "Voir F017")],
 src=[("Harmaguédon : un nouveau départ (19:14, Roi des rois, 2005)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2005881"),
      ("Révélation 19 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/19"),
      ("Révélation 20 — Bible d'étude, notes (abîme, 1000, voir F017)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/20"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_I010_guerrier.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J001", titre="Cyrus nommé — berger, oint, et le Grand Cyrus",
 ref="Ésaïe 44:24-28 ; 45:1-7, 13 ; 46:10-11 ; 48:14-15 ; Esdras 1:1-4 ; Romains 4:17",
 statut="Accomplie (539-537 ; Grand Cyrus : 1919)",
 cat="J", syst="Système 732/607/539/537",
 reg="Registre : Ésaïe — P160 (44:24-28), P161 (45:1-7), P163 (46:8-11), P165 (48:14-15) ; Esdras — P105 (1:1-4) ; Daniel — P374 (5:5-28), P375 (5:23-24)",
 texte=[
  "« ABÎME : ÉVAPORE-toi — je DESSÉCHERAI tes fleuves. » (Is 44:27 — tsula : "
  "l'Euphrate !)",
  "« Je dis de CYRUS : mon BERGER — TOUTE ma volonté — Jérusalem REBÂTIE, temple "
  "FONDÉ. » (44:28 — Koresh ! ro'i ! — ~732, pas encore détruite !)",
  "« À mon OINT, à Cyrus : MAIN DROITE — nations, CEINTURE des rois — PORTES pas "
  "fermées. » (45:1 — mashiah ! — païen OINT !)",
  "« J'aplanirai — portes d'AIRAIN, verrous de FER — TRÉSORS des ténèbres. » "
  "(45:2-3 — nehoshèt ! barzèl !)",
  "« Je t'ai appelé par ton NOM — SANS me connaître. » (45:4 — 2× ! yada !)",
  "« SUSCITÉ dans la justice — ma VILLE — mes captifs — SANS rançon. » (45:13 — "
  "hinnam : GRATUIT !)",
  "« Mon DESSEIN subsistera — OISEAU DE PROIE de l'EST. » (46:10-11 — atsati ! "
  "ayit !)",
 ],
 contexte=(
  "Ésaïe, ~732 (Juda : Achaz, Ézéchias ! — « 2 SIÈCLES avant » ! — « siècle et demi "
  "avant le POUVOIR » !). « Jérusalem DEBOUT » (chute : 607 — pas encore !). « Temple "
  "DEBOUT » (fondé : Salomon — « FONDÉ » : à reposer !). « Cyrus PAS NÉ » (« désolation "
  "AVANT naissance » !). « BERGER » (ro'i : titre ROYAL — 2S 5:2 ! Ps 78:71 !). « OINT » "
  "(mashiah, 45:1 : seul non-Israélite oint !). « Rm 4:17 » (« APPELLE… CE QUI N'EST "
  "PAS » — Insight CITE !). « Libre arbitre » (w24 : « pas porté ATTEINTE » — RENVOYÉ, "
  "voir Limites). « Grand Cyrus » (Jésus, 1919 : renvoi nominal !). « Édit NON annulé » "
  "(« ne pouvait PERMETTRE » — Esd 6 : Darius !). « Jéhovah… m'a CHARGÉ » (Esd 1:2, "
  "P105 !)."
 ),
 explication=(
  "« KORESH » (NOMMÉ : 44:28 !). « Ro'i » (BERGER : guide, nourrit !). « Hèphèts » "
  "(VOLONTÉ : plaisir !). « Tibbaneh » (REBÂTIE !). « Tiwwasèd » (FONDÉ : fondations !). "
  "« Tsula » (ABÎME : 44:27 !). « Mashiah » (OINT : 45:1 !). « Hèhèzaqti » (TENUE : main "
  "droite !). « Ceinture » (DÉSARMER les rois !). « Portes » (« pas FERMÉES » !). "
  "« Yashar » (APLANIR : 45:2 !). « Nehoshèt » (AIRAIN !). « Barzèl » (FER !). "
  "« Trésors » (« TÉNÈBRES » : 45:3 !). « Qara » (APPELÉ : par nom !). « Yada » (CONNAÎTRE : "
  "« sans » !). « Hinnam » (SANS rançon : GRATUIT !). « Atsati » (DESSEIN : 46:10 !). "
  "« Ayit » (OISEAU DE PROIE : 46:11 !). « Mizrah » (EST : Perse !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « 2 SIÈCLES » (732 → 539 !). « Berger » "
  "(malgré païen : mission !). « Oint » (consacré à la tâche !). « Rm 4:17 » (appelle ce "
  "qui n'est pas !). « Libre arbitre » (w24 : renvoi !). « Grand Cyrus » (Jésus, 1919 : "
  "renvoi nominal — délivrance de Babylone la Grande : voir I007 !). « Édit non annulé » "
  "(Esd 6 : Darius confirme !). « CHARGÉ » (Esd 1:2 : Cyrus RECONNAÎT !)."
 ),
 accomplissement=[
  ("~732 av. n. è.", "Ésaïe : le NOM (Jérusalem debout)"),
  ("607 av. n. è.", "Chute : Jérusalem détruite"),
  ("539 av. n. è.", "11/12 oct : NUIT — gué, portes, banquet (Da 5)"),
  ("538 av. n. è.", "Décret : « CHARGÉ » (Esd 1:1-4)"),
  ("537 av. n. è.", "Retour : 42 360 (voir B002)"),
  ("515 av. n. è.", "Temple : achevé (voir F015)"),
  ("1919 de n. è.", "Grand Cyrus : Jésus délivre (renvoi)"),
 ],
 hist=(
  "539 (Nabonide, Balthasar : banquet — Da 5, P374-375 !). Hérodote (gué, banquet !). "
  "Xénophon (Cyropédie !). Cylindre (1879 : « Marduk… Cyrus » — politique religieuse !). "
  "1QIsa (rouleau : TEXTE avant — antériorité prouvée !). Décret (Esd 1:1-4, P105 !). "
  "42 360 (Esd 2:64 : dénombrement — « SANS rançon » !). Lydie (547 : Crésus — « nations » "
  "!)."
 ),
 geo=(
  "Euphrate (le GUÉ : 44:27 !). Babylone (les PORTES : « airain » !). « EST » (Perse : "
  "Anshan !). Jérusalem (REBÂTIE : 44:28 !). « Nations » (Lydie 547, Babylone 539 !)."
 ),
 sci=(
  "732 − 539 ≈ 193 ans : « 2 SIÈCLES » ! « 11/12 oct » (539 : nuit datée !). 1QIsa "
  "(IIe s. av. : copie — l'ORIGINAL : VIIIe s. — antériorité !). Cylindre (1879 : "
  "corroboration profane !). 42 360 (Esd 2:64 : CHIFFRE !)."
 ),
 limites=(
  "Libre arbitre : mécanisme renvoyé à w24 (prescience sans contrainte). « Grand Cyrus » : "
  "renvoi nominal. 2 Chroniques 36:22-23 : P104 = 20-21 (22-23 : couvert par P105). "
  "« Agradatès » (Strabon) : tradition profane NON retenue."
 ),
 tl=[("732", "NOM : Cyrus"), ("607", "Chute"), ("539", "NUIT : 11/12 oct"), ("538", "Décret : CHARGÉ"),
     ("537", "Retour : 42 360"), ("515", "Temple"), ("1919", "Grand Cyrus")],
 src=[("Cyrus — Insight (siècle et demi, berger, Rm 4:17)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001102"),
      ("Prophétie écrite deux siècles à l'avance (Euphrate, Esd 1, 2020)", "https://wol.jw.org/fr/wol/d/r30/lp-f/202026082"),
      ("Ésaïe 45 — Bible d'étude, notes (oint, portes, nom)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/45"),
      ("Ésaïe 44 — Bible d'étude, notes (Berger, rebâtie, fondé)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/44")],
 img="images/prophe_J001_cyrus.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J002", titre="Josias nommé — l'autel accusé, la sépulture épargnée",
 ref="1 Rois 12:26-33 ; 13:1-6, 24 ; 2 Rois 22:1 ; 23:15-18, 29 ; 2 Chroniques 34:3",
 statut="Accomplie (~930 → 622 : 300 ans)",
 cat="J", syst="Système 930/722/640/609",
 reg="Registre : 1 Rois — P077 (13:2-5) ; 2 Rois 23 sans entrée (C8)",
 texte=[
  "« Un homme de Dieu arriva de JUDA à BÉTHEL — Jéroboam à l'autel, ENCENS. » "
  "(1R 13:1 — ANONYME ! roi-prêtre !)",
  "« AUTEL, AUTEL : un FILS à la maison de DAVID — son NOM : JOSIAS — IMMOLERA les "
  "prêtres — OSSEMENTS brûlés. » (13:2 — Yoshiyyah : « Jéhovah SOUTIENT » !)",
  "« SIGNE : l'autel se FENDRA, la GRAISSE se répandra. » (13:3 — mophèt !)",
  "« La MAIN du roi… SÉCHÉE — l'autel se FENDIT — la main GUÉRIE. » (13:4-6 — "
  "tiyabash !)",
  "« Béthel : autel DÉMOLI, BRÛLÉ, POUSSIÈRE — OSSEMENTS des sépulcres BRÛLÉS. » "
  "(2R 23:15-16 — C8 !)",
  "« QUELLE stèle ? — l'homme de Dieu… — la SÉPULTURE ÉPARGNÉE. » (23:17-18 — C8 ! "
  "respect !)",
 ],
 contexte=(
  "SCHISME, ~930 (Jéroboam : 1R 12 ! — « VEAUX » : Dan + Béthel ! — « FÊTE », 12:32 ! — "
  "« prêtres… PEUPLE », 12:31 !). « Homme de Dieu » (ANONYME — « de JUDA » !). "
  "« Jéroboam… ENCENS » (roi-PRÊTRE !). « BÉTHEL » (beth-el : « maison de Dieu » — "
  "« BETH-AVEN », Os 4:15 : « maison de MAL » !). « Veau… ASSYRIE » (Os 10:5-6 : emporté "
  "! — « autel TOUJOURS LÀ » : debout 300 ans !). « 18e ANNÉE » (purge « jusqu'aux villes "
  "de SAMARIE » — absolu non repris, voir Limites). « 8 ANS… 31 ANS » (640-609 : 2R 22:1 "
  "— « Yedida » !). « LIVRE » (622 : 2R 22:8 — « TROUVÉ » ! — « pas de son VIVANT », "
  "22:20 !). « Meguiddo » (609 : 2R 23:29 — C8 ! Néko — voir I009 !). « LION » (13:24 : "
  "arièh — « DÉSOBÉI » — NON développé, voir Limites)."
 ),
 explication=(
  "« Mizbèah, mizbèah » (AUTEL, AUTEL : l'OBJET accusé !). « Hinneh » (VOICI !). "
  "« Bèn… David » (FILS… DAVID !). « YOSHIYYAH » (Jéhovah SOUTIENT !). « Zabah » "
  "(IMMOLERA : sacrifiera !). « Atsamot » (OSSEMENTS !). « Mophèt » (SIGNE : 13:3 !). "
  "« Yiqqara » (FENDU !). « Dèshèn » (GRAISSE : répandue !). « Yad » (MAIN : 13:4 !). "
  "« Tiyabash » (SÉCHÉE : paralysée !). « Arièh » (LION : 13:24 !). « Nathats » "
  "(DÉMOLI : 23:15 !). « Saraph » (BRÛLÉ !). « Aphar » (POUSSIÈRE !). « Tsiyyun » (STÈLE : "
  "23:17 !). « Malat » (ÉPARGNÉE : 23:18 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « 300 ANS » (« prophétie VIEILLE de 300 ans » "
  "! — « 300 ans PLUS TÔT » ! — « PLUS de 300 ans » !). « S'est RÉALISÉE ENTIÈREMENT » "
  "(1R 13 + 2R 23 + Am 3:14 !). « L'a BEL ET BIEN fait » (fendu l'autel !). « Courage… "
  "FOI » (combat contre le faux culte !). « Humilité » (faveur !). « ÉPARGNA » (23:18 : "
  "respect du prophète !). « Os… prêtres de BAAL » (23:4-20 !)."
 ),
 accomplissement=[
  ("~930 av. n. è.", "Béthel : le NOM (schisme, veaux)"),
  ("930-722 av. n. è.", "Royaume Nord : l'autel debout"),
  ("722 av. n. è.", "Samarie : chute (Assyrie)"),
  ("640 av. n. è.", "Josias : 8 ans (31 ans)"),
  ("628 av. n. è.", "12e année : réforme (2Ch 34:3)"),
  ("622 av. n. è.", "18e année : LIVRE + Béthel (os, poussière)"),
  ("609 av. n. è.", "Meguiddo : mort (Néko — voir I009)"),
 ],
 hist=(
  "930 (schisme : Jéroboam !). 722 (Samarie : Assyrie !). 640-609 (31 ans : 2R 22:1 !). "
  "628 (12e année : 2Ch 34:3 !). 622 (18e année : LIVRE + purge !). « Veau emporté » "
  "(Os 10 : Assyrie !). « Autel toujours là » (300 ans DEBOUT !). Néko (609 : Meguiddo !)."
 ),
 geo=(
  "Béthel (FRONTIÈRE — ~12 km N de Jérusalem !). Dan (veau NORD !). Samarie (villes : "
  "purge !). « Sépulcres… MONTAGNE » (23:16 !). Meguiddo (mort — voir I009 !)."
 ),
 sci=(
  "930 − 622 ≈ 308 ans : « 300 » ! « PLUS de 300 » (trois publications !). "
  "« 350-360 » (comptes NON retenus — profanes, voir Limites). « Nom + acte + lieu » : "
  "TROIS précisions ! « Signe IMMÉDIAT » (autel fendu : VÉRIFICATION !)."
 ),
 limites=(
  "2 Rois 23 sans entrée (C8). « 642 » (absolu Insight) : NON repris — « 18e année » "
  "seule. « 350-360 » : comptes profanes non retenus. Lion (13:24) : épisode non "
  "développé. Amos 3:14 : cité par Insight, sans P."
 ),
 tl=[("930", "NOM : Josias"), ("722", "Samarie"), ("640", "8 ans"), ("628", "12e : réforme"),
     ("622", "18e : BÉTHEL !"), ("609", "Meguiddo")],
 src=[("Il a ramené le peuple à Jéhovah (300 ans, ossements, courage)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102025936"),
      ("Béthel — Insight (veau emporté, autel là, 18e année)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000682"),
      ("1 Rois 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/11/13"),
      ("2 Rois 23 — Bible d'étude, notes (Béthel, os, sépulture)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/23")],
 img="images/prophe_J002_josias.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J003", titre="Bethléhem Éphrata — petite, et les origines éternelles",
 ref="Michée 5:1-3 ; Matthieu 2:1-6 ; Luc 2:1-7, 11 ; Jean 7:42 ; 1 Samuel 16:1 ; Genèse 35:19",
 statut="Accomplie (~750 → 2 av. n. è. : 700 ans)",
 cat="J", syst="Système 750/2 · David",
 reg="Registre : Michée — P457 (5:2), P585 (5:2), P589 (5:2) ; Mt 2, Lc 2, Jn 7:42 sans entrée (C8)",
 texte=[
  "« SIÈGE… VERGE sur la JOUE du JUGE d'Israël. » (Mi 5:1 — tsur ! shophet ! — "
  "humilié !)",
  "« Bethléhem EPHRATA — PETITE entre les MILLIERS — de toi SORTIRA le DOMINATEUR — "
  "POUR MOI — ORIGINES d'ANCIENNETÉ, jours ÉTERNELS. » (5:2 — tsa'ir ! moshel ! miqedem ! "
  "olam !)",
  "« Il les LIVRERA jusqu'à ce qu'ENFANTE celle qui doit enfanter — le RESTE "
  "REVIENDRA. » (5:3 — yoledèt ! shear ! — Is 7:14 !)",
  "« Hérode… MAGES d'Orient… scribes : OÙ le Christ ? — Bethléhem — PAS LA MOINDRE — "
  "CONDUCTEUR qui PAÎTRA. » (Mt 2:1-6 — C8 ! hègoumenos ! poimanei !)",
  "« RECENSEMENT d'Auguste — Quirinius — MONTA de Nazareth : ville de DAVID — "
  "CRÈCHE. » (Lc 2:1-7 — C8 ! apographè ! phatnè !)",
  "« L'ÉCRITURE dit : de la descendance de DAVID, de Bethléhem. » (Jn 7:42 — C8 ! "
  "la foule SAIT !)",
 ],
 contexte=(
  "Michée, ~750 (Moresheth ! — contemporain d'Ésaïe ! — « 700 ANS avant » !). « SIÈGE » "
  "(5:1 : tsur — Sancherib, 701 !). « JUGE… JOUE » (5:1 : shophet — HUMILIÉ !). « 2 "
  "BETHLÉHEM » (Zabulon : Jos 19:15 ! — EPHRATA PRÉCISE !). « EPHRATA » (ephrathah : "
  "« FÉCONDITÉ » ! — Gn 35:16-19 : RACHEL ! — « Ephrath… Bethléhem » !). « PETITE » "
  "(tsa'ir ! — « MILLIERS » : alphè — CLANS !). « POUR MOI » (li : pour DIEU !). "
  "« ORIGINES » (motsaot : SORTIES ! — « ANCIENNETÉ » : miqedem ! — « ÉTERNELS » : mime "
  "olam — « temps INDÉFINIS » ! — Jn 1:1 ! 17:5 ! Col 1:15 ! — « au ciel » : renvoi "
  "nominal !). « ENFANTERA » (5:3 : yoledèt — Is 7:14 ! — « RESTE » : shear !). Hérode "
  "(Mt 2 : « GRAND », 37-4 ! — « TROUBLÉ » !). « MAGES » (magoi, 2:1 — « ORIENT » !). "
  "« Scribes » (2:4 : « OÙ… CHRIST » !). « PAS LA MOINDRE » (2:6 : INVERSION ! — "
  "« CONDUCTEUR » : hègoumenos ! — « PAÎTRA » : poimanei — BERGER !). « RECENSEMENT » "
  "(apographè, Lc 2:1 — « AUGUSTE » ! — « Quirinius », 2:2 : « PREMIER » — RENVOYÉE, voir "
  "Limites). « MONTA » (2:4 : anabainô — Nazareth → Bethléhem : ~150 km !). « Ville de "
  "DAVID » (2:4, 2:11 !). « CRÈCHE » (phatnè, 2:7 !). « Foule CONNAÎT » (Jn 7:42 : "
  "« l'Écriture DIT » !). David (1S 16:1 ! 17:12 : « ÉPHRATIEN » — « 8e fils » !). Ruth "
  "(Moab : « CHAMPS… Boaz » — Mt 1:5 : « Obed… Jessé » !). « Maison du PAIN » (beth-lehem "
  "— « pain de VIE », Jn 6:35 : NON fait — voir Limites)."
 ),
 explication=(
  "« Tsur » (SIÈGE : 5:1 !). « Shophet » (JUGE : frappé !). « Beth-lehem » (MAISON du "
  "PAIN !). « Ephrathah » (FÉCONDITÉ : précise !). « Tsa'ir » (PETITE !). « Alphè » "
  "(MILLIERS : clans !). « Yatsa » (SORTIRA !). « Moshel » (DOMINATEUR !). « Li » (POUR "
  "MOI : Dieu !). « Motsaot » (ORIGINES : sorties !). « Miqedem » (ANCIENNETÉ !). "
  "« Olam » (INDÉFINIS : éternels !). « Shear » (RESTE : 5:3 !). « Magoi » (MAGES !). "
  "« Hègoumenos » (CONDUCTEUR : 2:6 !). « Poimainô » (PAÎTRA : berger !). « Apographè » "
  "(RECENSEMENT : enregistrement !). « Anabainô » (MONTA : ~150 km !). « Phatnè » "
  "(CRÈCHE !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « 700 ANS » (750 → 2 !). « LAQUELLE » "
  "(Éphrata : celle de DAVID !). « PETITE » (contraste — « pas la moindre » : "
  "INVERSION !). « ORIGINES » (ciel avant : renvoi nominal — Jn 17:5 !). « Scribes "
  "SAVAIENT » (Mt 2:5 : réponse immédiate !). « Foule SAVAIT » (Jn 7:42 !). "
  "« Recensement » (Dieu MEUT Auguste : « TOUTE » la terre !). « Quirinius » : question "
  "renvoyée (voir Limites). « Pain » (beth-lehem / Jn 6:35 : NON fait — voir Limites)."
 ),
 accomplissement=[
  ("Rachel (Gn 35)", "Ephrath : « Bethléhem » (tombeau)"),
  ("Ruth (Moab)", "Champs : Boaz — Obed, Jessé (Mt 1:5)"),
  ("~1070 av. n. è.", "David : oint, 8e fils (1S 16)"),
  ("~750 av. n. è.", "Michée : le NOM (petite, origines)"),
  ("2 av. n. è.", "Recensement : montée, crèche (Lc 2)"),
  ("Hérode (Mt 2)", "Scribes : « Bethléhem » — pas la moindre"),
  ("~30 de n. è.", "Foule : « l'Écriture dit » (Jn 7:42)"),
 ],
 hist=(
  "~750 (Michée : Moresheth !). 37-4 (Hérode le Grand !). Auguste (recensement : « toute » "
  "!). Quirinius (Lc 2:2 : « premier » — RENVOYÉE !). David (~1070 : onction, 1S 16 !). "
  "Mt 1:5 (Ruth → Obed → Jessé !). Jos 19:15 (Bethléhem de Zabulon !)."
 ),
 geo=(
  "« 9 km » (SUD de Jérusalem !). « EPHRATA » (district : précise !). « Nazareth → "
  "Bethléhem » (~150 km : MONTA !). « Champs » (Ruth ! bergers ! Lc 2:8 !). « 2 "
  "Bethléhem » (Zabulon : Jos 19:15 !)."
 ),
 sci=(
  "750 − 2 ≈ 748 ans : « 700 » ! « 9 km » : DISTANCE (Jérusalem !). « ~150 km » : MONTÉE "
  "(Nazareth !). Olam : INDÉFINI (temps !). Apographè : ENREGISTREMENT (recensement !). "
  "Alphè : CLAN, millier (tribu !)."
 ),
 limites=(
  "Matthieu 2, Luc 2, Jean 7:42 sans entrée (C8). Quirinius (Lc 2:2) : question "
  "renvoyée aux publications (dates profanes). « Pain de vie » (Jn 6:35) : "
  "rapprochement NON fait par les publications — pas de concordisme. 1S 16, Ruth, "
  "Gn 35 : cross-refs sans P."
 ),
 tl=[("Rachel", "Ephrath"), ("Ruth", "Boaz : Obed"), ("1070", "David : oint"), ("750", "NOM : Bethléhem"),
     ("2 av.", "Crèche : montée"), ("Hérode", "Scribes : sait"), ("30", "Foule : sait")],
 src=[("Michée 5 — Bible d'étude, notes (Éphrata, origines, reste)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/33/5"),
      ("Matthieu 2 — Bible d'étude, notes (Hérode, scribes, Bethléhem)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/2"),
      ("Luc 2 — Bible d'étude, notes (recensement, montée, crèche)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/2"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_J003_bethlehem.jpg",
))
