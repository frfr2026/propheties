#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 8 · vague P8-18 (mixte 4 livres) · CH+ED+NE+IS : P103-P108."""
# pylint: disable=invalid-name,line-too-long

CAT = dict(
    code="CH+ED+NE+IS",
    nom="Chroniques (2) + Esdras (1) + Néhémie (1) + Isaïe (1) — retours et restes",
    intro=("Oded fait renvoyer deux cent mille captifs ; la terre jouira de "
           "soixante-dix sabbats ; Cyrus décrète le retour et la maison se "
           "rebâtit ; les dispersés se rassemblent au lieu choisi ; Sion "
           "dévastée tient comme une hutte ; les nations affluent et les "
           "épées deviennent des socs."),
    vague="P8-18",
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="CH103", titre="« Renvoyez les captifs ! » : Oded arrête l'armée et 200 000 repartent",
    ref="2 Chroniques 28:9-11",
    statut="Accomplie",
    cat="CH", syst="Interception d'Oded (défaite → 120 000 → 200 000 → rencontre → renvoyez → soignés → Jéricho)",
    reg="Registre : 2 Chroniques — P103 (28:9-11 : 200 000 captifs de Juda renvoyés) ; accomplissement 2Ch 28:12-15",
    texte=[
        "« PÉQAH… 120 000… UN JOUR… ABANDONNÉ JÉHOVAH. » (28:6 — Jéhovah !)",
        "« ZIKRI… TUAI le FILS du ROI… CHEFS… MAISON. » (28:7 — maison !)",
        "« 200 000 FEMMES… FILS… FILLES… BUTIN… SAMARIE. » (28:8 — Samarie !)",
        "« ODED… PROPHÈTE… SORTIT à leur RENCONTRE. » (28:9 — rencontre !)",
        "« COLÈRE… LIVRÉS… TUÉS avec RAGE… jusqu'aux CIEUX. » (28:9 — cieux !)",
        "« VOULEZ ASSERVIR… FRÈRES… TORTS envers JÉHOVAH ? » (28:10 — Jéhovah !)",
        "« ÉCOUTEZ-MOI… RENVOYEZ… ARDENTE COLÈRE. » (28:11 — colère !)",
        "« 4 CHEFS ÉPHRAÏM… SE LEVÈRENT… S'OPPOSÈRENT. » (28:12 — opposèrent !)",
        "« N'AMENEZ PAS… AJOUTER… FAUTES… COLÈRE sur ISRAËL. » (28:13 — Israël !)",
        "« ARMÉE LAISSA… CAPTIFS + BUTIN… devant CHEFS. » (28:14 — chefs !)",
        "« VÊTIRENT… NOURRIRENT… OIGNIRENT… ÂNES… JÉRICHO. » (28:15 — Jéricho !)",
    ],
    contexte=(
        "Samarie, ~732? — ACHAZ IMPIE (28:1-4 : les PIRES (les JUDA (les ENFANTS (les FEU (les HAUTS LIEUX (les "
        "PARTOUT (les IDOLÂTRIES — les TOTALES (les JUGEMENTS (les MÉRITÉS (les COALITIONS (les PUNITIVES !). La "
        "GUERRE SYRO-ÉPHRAÏMITE (28:5-8 : PÉQAH (les NORD (les RETSIN (les DAMAS (les COALISÉS (les JUDA (les "
        "ÉCRASÉS (Is 7 ! (les CONTEXTES (les PROPHÉTIQUES (les IMMANUEL (les ANNONCÉS (les MÊMES (les GUERRES ! "
        ": les COALITIONS — les VOISINES (les CHÂTIMENTS (les INSTRUMENTAUX !). 120 000 UN JOUR (28:6 : les "
        "HÉCATOMBES (les VAILLANTS (les gibborim (les TOMBÉS (les NOMBRES (les ÉNORMES (les DÉSASTRES — les "
        "NATIONAUX (les DEUILS (les INCOMPTABLES !) + le FILS du ROI (28:7 : MAASÉYA (les TUÉS (les ZIKRI (les "
        "ÉPHRAÏMITES (les PALAIS (les DÉCAPITÉS (les DYNASTIES — les FRAPPÉES (les SUCCESSIONS (les MENACÉES !). "
        "ODED (28:9 : les PROPHÈTES (les SAMARIE (les NORD (les PARLENT (les NORD (les CONSCIENCES (les RÉVEILLÉES "
        "(les 1200003297 : « PROPHÈTE de SAMARIE durant… PÉQAH… et ACHAZ (762-env. 759) » (OFFICIEL ! (les DATES "
        "— les ANCRÉES (les RÈGNES (les CROISÉS !)."
    ),
    explication=(
        "« ODED… SORTIT (vayyetse') à leur RENCONTRE (liqratam) », 28:9 : yatsa' — SORTIR (les INTERCEPTIONS (les "
        "PROPHÉTIQUES (les ARMÉES (les VICTORIEUSES (les STOPPÉES (les PAROLES (les SEULES (les COURAGES — les "
        "SOLITAIRES (les PROPHÈTES (les BARRAGES !). « Dans sa COLÈRE (za'aph)… il les a LIVRÉS (netanam) », 28:9 : "
        "za'aph + natan — COLÈRE + LIVRER (les PERMISSIONS (les DIVINES (les JUDA (les PUNIS (les INSTRUMENTS (les "
        "NORD (les DISTINCTIONS — les CRUCIALES (les PERMETTRE (les APPROUVER (les DIFFÉRENTS !). « Vous les AVEZ TUÉS "
        "(haragtem) avec une RAGE ('aph)… jusqu'aux CIEUX (lashamayim) », 28:9 : aph — RAGE (les EXCÈS (les MEURTRES "
        "(les COLÈRES (les HUMAINES (les DÉMESURÉES (les CIEUX (les ATTEINTS (les HYPERBOLES — les JUDICIAIRES (les "
        "CRIS (les MONTÉS !). « Vous VOULEZ (omerim) ASSERVIR (likhbosh)… vos FRÈRES (achekhem) », 28:10 : kavash + "
        "ach — ASSERVIR + FRÈRES (les FRATERNITÉS (les SCHISMES (les DÉPASSÉS (les NORD (les SUD (les MÊMES (les SANGS "
        "(les ESCLAVAGES — les FRATRICIDES (les INTERDITS (les SCANDALES !). « N'Y A-T-IL PAS… des TORTS ('ashamot)… "
        "ENVERS JÉHOVAH ? », 28:10 : asham — TORT (les CULPABILITÉS (les PROPRES (les VAINQUEURS (les PECHEURS (les "
        "MIROIRS — les RETOURNÉS (les JUGES (les JUGÉS !). « ÉCOUTEZ-MOI (shema'uni)… RENVOYEZ (vehahashivu) », 28:11 : "
        "shama' + shuv — ÉCOUTER + RENVOYER (les IMPÉRATIFS (les PROPHÉTIQUES (les RESTITUTIONS (les ORDONNÉES (les "
        "OBÉISSANCES — les EXIGÉES (les COLÈRES (les ÉVITÉES !)."
    ),
    interpretation=(
        "PERMISE ≠ APPROUVÉE (les VICTOIRES (les AUTORISÉES (les EXCÈS (les CONDAMNÉS (les DIEUX (les PERMETTENT (les "
        "HOMMES (les RESPONSABLES (les THÉOLOGIES — les SUBTILES (les INSTRUMENTS (les COUPABLES (les JUGÉS !). "
        "FRÈRES MALGRÉ SCHISMES (les NORD (les SUD (les SÉPARÉS (les 200 ANS (les FRATERNITÉS (les DEMEURENT (les DIEUX "
        "(les VOIENT (les FAMILLES (les FRONTIÈRES — les HUMAINES (les SANGS (les DIVINS !). Les 4 CHEFS (28:12 : "
        "AZARIA + BARÉKIA + ÉZÉCHIAS + AMASA (les ÉPHRAÏMITES (les NOMMÉS (les MINORITÉS (les JUSTES (les ARMÉES (les "
        "ARRÊTÉES (les COURAGES — les COLLECTIFS (les QUATRE (les SUFFISENT !) + 1200003297 : « QUATRE CHEFS "
        "ÉPHRAÏMITES SOUTINRENT ODED, et les CAPTIFS furent SOIGNÉS et RAMENÉS » (OFFICIEL ! (les SOINS — les "
        "OFFICIELS (les RETOURS (les ORGANISÉS !). JÉRICHO SOIGNÉ (28:15 : les VÊTUS (les NOURRIS (les OINTS (les "
        "MONTÉS (les ÂNES (les FAIBLES (les PORTÉS (les RENVOIS — les ROYAUX (les ENNEMIS (les TRAITÉS (les FRÈRES !)."
    ),
    hist=(
        "PÉQAH (2R 15:25-31 : les USURPATEURS (les 20 ANS (les ASSASSINS (les PEQAHYA (les ALLIÉS (les RETSIN (les FINS "
        "(les OSÉE (les ASSASSINE (les TIGLATH (les CONTEXTES (les DYNASTIES — les VIOLENTES (les NORD (les "
        "AGONISANTES !). RETSIN DAMAS (28:5 : les SYRIENS (les COALISÉS (les CAPTIFS (les DAMAS (les PREMIERS (les "
        "RAZZIAS (les DOUBLES (les FRONTS (les JUDA (les ÉCRASÉS (les ÉTAUX — les RÉGIONAUX (les PRESSIONS (les "
        "MORTELLES !). TIGLATH-PILÉSER III (2R 16:7-9 : les ACHAZ (les APPELLENT (les ASSYRIE (les SECOURS (les "
        "TRIBUTS (les TRÉSORS (les VASSALITÉS (les CONSÉQUENCES — les GÉOPOLITIQUES (les PETITS (les ÉCRASÉS (les "
        "GRANDS (les APPELÉS !). JÉRICHO VILLE des PALMIERS (28:15 : 'ir-hattemarim — PALMIERS (les OASIS (les "
        "ACCUEILS (les CONVOIS (les HUMANITAIRES (les ANTIQUES (les SOINS — les MASSIFS (les LOGISTIQUES (les "
        "PRODIGIEUSES !)."
    ),
    geo=(
        "SAMARIE (28:8-9 : les DESTINATIONS (les CAPTIFS (les MARCHES (les FORCÉES (les RENCONTRES (les ODED (les "
        "PORTES (les VILLES (les INTERCEPTIONS — les GÉOGRAPHIQUES (les RETOURS (les AMORCÉS (les AVANT-ENTRÉES !). "
        "JUDA → SAMARIE (les ROUTES (les MONTAGNES (les ~80 KM (les FEMMES (les ENFANTS (les ÉPUISÉS (les COLONNES — "
        "les MISÉRABLES (les MARCHES (les DOULOUREUSES !). JÉRICHO (28:15 : les RENVOIS (les FRONTIÈRES (les SUD (les "
        "PALMIERS (les EAUX (les REPOS (les CONVOIS (les RÉCEPTIONNÉS (les FRATERNITÉS — les GÉOGRAPHIQUES (les "
        "RETOURS (les SOIGNÉS !). ÉPHRAÏM (28:12 : les 4 CHEFS (les TRIBUS (les DOMINANTES (les NORD (les VOIX (les "
        "AUTORISÉES (les OPPOSITIONS — les CRÉDIBLES (les INTÉRIEURES (les EFFICACES !)."
    ),
    sci=(
        "La DÉMOGRAPHIE (28:8 : les 200 000 (les FEMMES (les ENFANTS (les FAMILLES (les ENTIÈRES (les DÉPORTÉES (les "
        "PROPORTIONS (les CIVILES (les GUERRES — les TOTALES (les POPULATIONS (les CIBLÉES !). La LOGISTIQUE (28:15 : "
        "les NOURRIR (les 200 000 (les VÊTIR (les NUS (les DÉPOUILLÉS (les OINDRE (les BLESSÉS (les TRANSPORTER (les "
        "FAIBLES (les OPÉRATIONS — les COLOSSALES (les ORGANISATIONS (les IMPROVISÉES (les RÉUSSIES !). La MÉDECINE "
        "(les OINTS (les vayesusukhum (les HUILES (les PLAIES (les SOINS (les MASSIFS (les ONGUENTS (les QUANTITÉS (les "
        "PHARMACOPÉES — les URGENCES (les GUERRES (les HUMANITAIRES !). L'HIPPOLOGIE (les ÂNES (les chamorim (les "
        "MONTURES (les FAIBLES (les EXTÉNUÉS (les PORTÉS (les CONVOIS (les MIXTES (les MARCHEURS (les CAVALIERS (les "
        "SOLLICITUDES — les VÉTÉRINAIRES (les HUMAINES !)."
    ),
    schema=(
        "ODED EN 10 TEMPS : ACHAZ (les IMPIES !) → COALITION (« PÉQAH + RETSIN » : les ÉCRASÉS !) → 120 000 (« UN JOUR » "
        ": les HÉCATOMBES !) → FILS (« TUÉ… ZIKRI » : les DÉCAPITÉS !) → 200 000 (« FEMMES… BUTIN… SAMARIE » : les "
        "DÉPORTÉS !) → ODED (« SORTIT à leur RENCONTRE » : les INTERCEPTÉS !) → « RAGE… CIEUX » (les ACCUSÉS !) → « "
        "FRÈRES… TORTS ? » (les MIROIRS !) → « RENVOYEZ… COLÈRE » (les ORDONNÉS !) → 4 CHEFS (« S'OPPOSÈRENT » : les "
        "SOUTENUS !) → LAISSA (« CAPTIFS + BUTIN » : les RESTITUÉS !) → JÉRICHO (« VÊTUS… ÂNES » : les SOIGNÉS !). Un "
        "prophète arrête une armée — deux cent mille repartent soignés."
    ),
    limites=(
        "Les 200 000 (les CHIFFRES (les RONDS (les EXACTS (les TEXTES (les AFFIRMENT (les SCEPTIQUES (les DOUTENT (les "
        "FOIS — les SIMPLES (les GARDÉS (les DÉBATS (les NOTÉS !). Les 120 000 (28:6 : les UN JOUR (les BATAILLES (les "
        "RANGÉES (les MASSACRES (les NOMBRES (les ÉNORMES (les GUERRES (les ANTIQUES (les EXAGÈRENT (les SCRIBES (les "
        "COMPTENT (les VÉRITÉS — les PAST (les TRANCHÉES (les TEXTES (les PRÉSERVÉS !). Les 2 ODED (2Ch 15:1, 8 + 28:9 : "
        "les PÈRE (les AZARIA (les SAMARIE (les MÊMES ? (les DIFFÉRENTS (les SIÈCLES (les ÉCARTS : 1200003297 : « 1… "
        "PÈRE… 2… PROPHÈTE de SAMARIE » (OFFICIEL ! (les DEUX — les DISTINGUÉS (les OFFICIELLEMENT !). Les DATES "
        "(762-759 (les 1200003297 (les OFFICIELLES (les PÉQAH (les 20 ANS (les CHRONOLOGIES (les DÉBATTUES (les "
        "GUERRES (les SYRO-ÉPHRAÏMITES (les ~734-732 (les FOURCHETTES (les PRUDENTES !). Les 4 NOMS (28:12 : les "
        "AZARIA (les MULTIPLES (les HOMONYMES (les IDENTIFICATIONS (les IMPOSSIBLES (les GÉNÉALOGIES (les PARTIELLES "
        "(les MÉMOIRES — les NOMINALES (les HONORÉES !)."
    ),
    accomplissement=[(("28:5-8", "COALITION + 120 000 (JOUR !) + 200 000 (SAMARIE)")),
        ((("28:9-11"), "RENCONTRE + « RAGE » + « RENVOYEZ »")),
        ((("28:12-13"), "4 CHEFS (OPPOSÈRENT !)")),
        ((("28:14"), "LAISSA (CAPTIFS + BUTIN !)")),
        ((("28:15"), "SOIGNÉS + ÂNES + JÉRICHO (!)"))],
    tl=[((("28:6"), "120 000 (JOUR !)")),
        ((("28:8"), "200 000 (SAMARIE)")),
        ((("28:9"), "RENCONTRE (ODED)")),
        ((("28:11"), "« RENVOYEZ »")),
        ((("28:15"), "JÉRICHO (SOIGNÉS)"))],
    src=[("Oded — Étude (prophète de Samarie, 200 000 renvoyés, 2Ch 28)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003297"),
        ("2 Chroniques 28 — Bible d'étude (Oded, captifs, 28:9-15)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/28"),
        ("2 Chroniques 28 — Traduction du monde nouveau (Achaz, Éphraïm)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/14/28")],
    img="images/prophe_CH103_captifs.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="CH104", titre="« Jusqu'à ce que la terre ait joui de ses sabbats » : soixante-dix ans de repos forcé",
    ref="2 Chroniques 36:20-21",
    statut="Accomplie",
    cat="CH", syst="70 sabbats (messagers → moqués → plus remède → brûlée → déportés → sabbats → Cyrus → Daniel)",
    reg="Registre : 2 Chroniques — P104 (36:20-21 : 70 ans, terre accomplira ses sabbats) ; accomplissement Esd 1:1-4 ; Dn 9:2",
    texte=[
        "« MESSAGERS… SE MOQUAIENT… MÉPRISAIENT… COLÈRE. » (36:15-16 — colère !)",
        "« PLUS de REMÈDE. » (36:16 — remède !)",
        "« CHALDÉENS… JEUNE… VIEILLARD… PAS ÉPARGNÉ. » (36:17 — épargné !)",
        "« TOUT… EMPORTÉ… BABYLONE… TRÉSORS. » (36:18 — trésors !)",
        "« MAISON BRÛLÉE… MUR DÉMOLI… PALAIS FEU. » (36:19 — feu !)",
        "« DÉPORTÉS… SERVITEURS… jusqu'aux PERSES. » (36:20 — Perses !)",
        "« PAROLE JÉRÉMIE… JOUI SABBATS… REPOSA… DÉVASTÉ… 70 ANS. » (36:21 — ans !)",
        "« CYRUS… 1re ANNÉE… PAROLE JÉRÉMIE… MONTEZ ! » (Esd 1:1-3 — montez !)",
        "« DANIEL… DISCERNA par les LIVRES… 70 ANS. » (Dn 9:1-2 — livres !)",
    ],
    contexte=(
        "Jérusalem, 607 — les DERNIERS ROIS (36:1-14 : JOACHAZ (les 3 MOIS (les JOJAKIM (les 11 ANS (les BRÛLE (les "
        "ROULEAUX (Jr 36 ! (les JOJAKIN (les 3 MOIS (les DÉPORTÉS (les SÉDÉCIAS (les 11 ANS (les RÉVOLTÉS (les SERMENTS "
        "(les VIOLÉS (les SPIRALES — les FINALES (les AGONIES (les DYNASTIQUES !). Les MESSAGERS MÉPRISÉS (36:15-16 : "
        "« JÉHOVAH… ENVOYA… de BONNE HEURE… COMPASSION » (les MATINS (les RÉPÉTÉS (les PATIENCES (les DIVINES (les "
        "MOQUERIES (les HUMAINES (les MÉPRIS (les PROPHÈTES (les EXCÈS — les COMBLES (les MISÉRICORDES (les "
        "ÉPUISÉES !). JÉRÉMIE 25 (les ANNONCES (Jr 25:11-12 : « 70 ANS… SERVIRONT… BABYLONE » (les PROPHÉTIES (les "
        "PRÉCISES (les DURÉES (les CHIFFRÉES (les VÉRIFIABLES (les PAROLES — les DATÉES (les COMPTABLES !). LÉVITIQUE "
        "26 (les MENACES (Lv 26:34-35 : « la TERRE JOUIRA… PENDANT qu'elle sera DÉVASTÉE » (les SABBATS (les VOLÉS "
        "(les LOIS (les IGNORÉES (les 490 ANS ? (les 70 MANQUÉS (les DETTES — les FONCIÈRES (les EXIGÉES !). DANIEL "
        "VIEUX (Dn 9:1-2 : les 539 ? (les DARIUS (les MÈDE (les LIVRES (les LUS (les ANNÉES (les COMPTÉES (les PRIÈRES "
        "(les SUIVENT (les LECTEURS — les PROPHÉTIQUES (les BIBLES (les INTERPRÈTENT (les BIBLES !)."
    ),
    explication=(
        "« Ils SE MOQUAIENT (mal'ivim)… MÉPRISAIENT (vozim) », 36:16 : la'av + bazah — MOQUER + MÉPRISER (les "
        "RÉCEPTIONS (les MESSAGERS (les RISÉES (les DÉDAINS (les PAROLES (les DIVINES (les TRAITÉES (les PLAISANTERIES "
        "(les CRIMES — les VERBAUX (les MORTELS !). « Il n'y eut PLUS de REMÈDE ('ein marpe') », 36:16 : marpe' — "
        "REMÈDE (les MÉDECINES (les DIVINES (les INEFFICACES (les MALADIES (les INCURABLES (les JUGEMENTS (les "
        "DERNIERS (les RECOURS (les ÉCHECS — les TOTAUX (les GRÂCES (les TERMINÉES !). « Il NE les ÉPARGNA PAS (lo' "
        "chamal) », 36:17 : chamal — ÉPARGNER (les PITIÉS (les RETIRÉES (les JEUNES (les VIEUX (les VIERGES (les "
        "TOUS (les FRAPPÉS (les TOTALITÉS — les TERRIFIANTES (les JUGEMENTS (les SANS-EXCEPTIONS !). « Afin que S'ACCOMPLÎT "
        "(lemallot) la PAROLE… par JÉRÉMIE », 36:21 : malle' — ACCOMPLIR (les REMPLIR (les PAROLES (les VASES (les "
        "HISTOIRES (les CONTENUS (les PROPHÉTIES — les SOLDÉES (les COMPTABILITÉS (les DIVINES !). « Jusqu'à ce que "
        "la TERRE ('arets) eût JOUI (ratsah) de ses SABBATS (shabbtotekha) », 36:21 : ratsah — JOUIR (les AGRÉER (les "
        "TERRES (les PERSONNES (les DETTES (les PAYÉES (les REPOS (les FORCÉS (les CRÉANCES — les FONCIÈRES (les "
        "RECOUVRÉES !) + 1964886 : « une PÉRIODE ININTERROMPUE d'ANNÉES SABBATIQUES… pour COMPENSER toutes les ANNÉES "
        "SABBATIQUES… NON OBSERVÉES » (OFFICIEL ! (les COMPENSATIONS — les EXACTES (les SABBATS (les RENDUS !). « "
        "SOIXANTE-DIX (shav'im) ANS », 36:21 : shav'im — 70 (les NOMBRES (les PARFAITS (les 7 × 10 (les PLÉNITUDES (les "
        "DURÉES — les SYMBOLIQUES (les LITTÉRALES (les DEUX !)."
    ),
    interpretation=(
        "Les SABBATS VOLÉS RENDUS (les 490 ANS (les 70 MANQUÉS (les CALCULS (les PROPOSÉS (les DETTES (les EXIGÉES (les "
        "TERRES (les CRÉANCIÈRES (les JUSTICES — les COSMIQUES (les SOLS (les REMBOURSÉS !). « PLUS de REMÈDE » (les "
        "FINS (les MISÉRICORDES (les COLLECTIVES (les INDIVIDUS (les SAUVABLES (les NATIONS (les CONDAMNÉES (les "
        "DISTINCTIONS — les TERRIFIANTES (les GRÂCES (les ÉPUISABLES !). DANIEL LIT et COMPREND (Dn 9:2 : « je DISCERNAI "
        "(binoti) par les LIVRES (sepharim) » (les EXÉGÈSES (les PROPHÉTIQUES (les JÉRÉMIE (les LUS (les ANNÉES (les "
        "COMPTÉES (les PRIÈRES (les DÉCLENCHÉES (les MODÈLES — les ÉTERNELS (les LIRE (les COMPRENDRE (les PRIER !). "
        "607 → 537 (les 70 EXACTS (les CHRONOLOGIES (les OFFICIELLES (les PIVOTS (les VÉRIFIÉS (les PROPHÉTIES — les "
        "PONCTUELLES (les HISTOIRES (les CONFORMES !) + 1964886 : « La PÉRIODE… COMMENÇA… en 607… Quand PRIT FIN… En "
        "537 » (OFFICIEL ! (les DATES — les OFFICIELLES (les DÉBATS (les TRANCHÉS !). La TERRE PERSONNE (les VIDES (les "
        "HANTÉS (les PASSANTS (les DÉTOURNENT (les 1200012382 : « un VIDE dans l'HISTOIRE… jusqu'à CYRUS » (CONDER, "
        "OFFICIEL ! (les ARCHÉOLOGIES — les MUETTES (les SILENCES (les ÉLOQUENTS !)."
    ),
    hist=(
        "607 (les CHUTES (les SIÈGES (les 18 MOIS (les FAMINES (les BRÈCHES (les FUITES (les RIBLA (les YEUX (les "
        "CREVÉS (les DATES — les OFFICIELLES (les 1964886 (les TRANCHÉES !). 539 (les BABYLONE (les PRISES (les CYRUS "
        "(les NABONIDE (les BELSHATSAR (les NUITS (les MAINS (les ÉCRIVENT (Dn 5 ! (les EMPIRES — les TRANSFÉRÉS (les "
        "MÈDES-PERSES (les INTRONISÉS !). 537 (les RETOURS (les DÉCRETS (les TISRI (les AUTELS (les REBÂTIS (Esd 3 ! "
        "(les FIN (les DÉSOLATIONS (les REPEUPLEMENTS (les AMORCÉS !) + 1965684 : « 537… DATE où CYRUS… a PUBLIÉ son "
        "DÉCRET » (OFFICIEL ! (les PIVOTS — les HISTORIQUES (les PROPHÉTIQUES !). PAS de COLONIES (les CONTRASTES (les "
        "SAMARIE (les REPEUPLÉES (les JUDA (les VIDES (les POLITIQUES (les BABYLONIENNES (les DIVERSES (les PROPHÉTIES "
        "— les RESPECTÉES (les DÉSERTS (les PRÉSERVÉS !) + 1200012382 : « le ROI de BABYLONE N'INSTALLA PAS d'autres "
        "PEUPLES… le PAYS RESTA DÉSOLÉ pendant SOIXANTE-DIX ANS » (OFFICIEL ! (les VIDES — les VOULUS (les PROPHÉTISÉS !)."
    ),
    geo=(
        "BABYLONE (36:20 : les DÉPORTATIONS (les CONVOIS (les 900 KM (les EXILS (les FLEUVES (les PLEURS (Ps 137 ! (les "
        "DIASPORAS — les FORMÉES (les IDENTITÉS (les PRÉSERVÉES !). JUDA VIDE (36:21 : les DÉVASTÉE (les shamemah (les "
        "CHAMPS (les FRICHES (les VILLES (les RUINES (les ROUTES (les HERBES (les PAYSAGES — les POST-APOCALYPTIQUES "
        "(les SABBATS (les VISIBLES !). JÉRUSALEM RUINES (36:19 : les MURS (les DÉMOLIS (les PORTES (les FEU (les "
        "TEMPLE (les BRASIER (les MONTAGNE (les MAISON (les TAS (les DÉSALTATIONS — les TOTALES (les GLOIRES (les "
        "CENDRES !). Les PERSES (36:20 : « jusqu'au RÈGNE (malkhut) des PERSES » (les EMPIRES (les SUCCESSIONS (les "
        "HORIZONS (les DATÉS (les FINS (les EXILS (les ANNONCÉES (les GÉOPOLITIQUES — les PROPHÉTISÉES (les "
        "PRÉCISES !)."
    ),
    sci=(
        "L'AGRONOMIE (36:21 : les JACHÈRES (les 70 ANS (les SOLS (les REPOSÉS (les FERTILITÉS (les RESTAURÉES (les "
        "FRICHES (les FORÊTS (les REVENUES (les ÉCOLOGIES — les RÉGÉNÉRÉES (les SABBATS (les AGRONOMIQUES !). La "
        "DÉMOGRAPHIE (les VIDES (les TOTAUX (les EXILS (les MASSIFS (les PAUVRES (les RESTÉS (2R 25:12 ! (les VIGNERONS "
        "(les LABOUREURS (les RÉSIDUS (les MINIMES (les RECENSEMENTS — les EFFONDRÉS (les COURBES (les ZÉRO !). La "
        "CHRONOLOGIE (les 607 (les 537 (les 70 EXACTS (les ASTRONOMIES (les VAT 4956 (les DÉBATS (les ÉCLIPSES (les "
        "INTERPRÉTÉES (les DIVERSEMENT (les OFFICIELS (les 607 (les TRANCHÉS !). L'ARCHÉOLOGIE (les COUCHES (les "
        "DESTRUCTIONS (les CENDRES (les LAKISH (les ARAD (les OSTRACA (les SIÈGES (les BULLES (les BRÛLÉES (les "
        "FOUILLES — les CONFIRMANTES (les FEUX (les DATÉS (les RUINES (les PARLANTES !)."
    ),
    schema=(
        "70 ANS EN 10 TEMPS : ROIS (« JOJAKIM… SÉDÉCIAS » : les AGONISANTS !) → MESSAGERS (« ENVOYA… COMPASSION » : les "
        "PATIENTS !) → MOQUÉS (« SE MOQUAIENT… MÉPRISAIENT » : les EXCÉDÉS !) → « PLUS de REMÈDE » (les INCURABLES !) → "
        "CHALDÉENS (« PAS ÉPARGNÉ » : les TOTAUX !) → BRÛLÉE (« MAISON… MUR… PALAIS » : les INCENDIÉS !) → DÉPORTÉS (« "
        "SERVITEURS… PERSES » : les EXILÉS !) → « JOUI SABBATS… REPOSA » (les CRÉANCIERS !) → « 70 ANS » (les COMPTÉS !) "
        "→ CYRUS (« 1re ANNÉE… MONTEZ ! » (ED105 !) → DANIEL (« DISCERNA par les LIVRES » : les LECTEURS !). Plus de "
        "remède — la terre prendra ses sabbats de force, soixante-dix ans."
    ),
    limites=(
        "607 vs 587 (les SAVANTS (les MAJORITÉS (les 587 (les OFFICIELS (les 607 (les 1964886 (les TRANCHENT (les "
        "PREUVES (les ASTRONOMIQUES (les INTERPRÉTÉES (les DÉBATS (les OUVERTS (les FOIS (les OFFICIELLES (les "
        "ASSUMÉES !). Les 490 ANS (les CALCULS (les 70 × 7 (les SABBATS (les MANQUÉS (les DEPUIS (les QUAND (les "
        "ENTRÉE (les CANAAN ? (les SAÜL ? (les COMPTES (les PROPOSÉS (les INCERTAINS (les DETTES (les CERTAINES (les "
        "MONTANTS (les ESTIMÉS !). VAT 4956 (les TABLETTES (les ÉCLIPSES (les LUNAIRES (les DATATIONS (les "
        "NÉO-BABYLONIENNES (les LECTURES (les DIVERSES (les EXÉGÈTES (les ASTRONOMES (les DÉBATTENT (les CONCLUSIONS "
        "(les DIVERGENT (les PRUDENCES — les REQUISES (les PASSIONS (les ÉVITÉES !). Les PAUVRES RESTÉS (2R 25:12 : les "
        "VIDES (les TOTAUX ? (les RÉSIDUS (les VIGNERONS (les GUEDALIA (les ASSASSINÉ (les FUITES (les ÉGYPTE (Jr 43 ! "
        "(les DÉSALTATIONS — les COMPLÈTES (les APRÈS-GUEDALIA !). DANIEL DATES (Dn 9:1 : les DARIUS (les MÈDE (les "
        "IDENTITÉS (les DÉBATTUES (les CYAXARE ? (les GUBARU ? (les HISTORIENS (les CHERCHENT (les TEXTES (les AFFIRMENT "
        "(les PERSONNES (les MYSTÉRIEUSES !)."
    ),
    accomplissement=[(("36:15-16", "MESSAGERS (MOQUÉS) + « PLUS REMÈDE »")),
        ((("36:17-19"), "CHALDÉENS + BRÛLÉE (MUR !)")),
        ((("36:20-21"), "DÉPORTÉS + « SABBATS… 70 ANS »")),
        ((("Esd 1:1-4"), "CYRUS (MONTEZ ! ED105 !)")),
        ((("Dn 9:1-2"), "DANIEL (LIVRES !)"))],
    tl=[((("36:16"), "« PLUS REMÈDE »")),
        ((("36:19"), "BRÛLÉE (MUR !)")),
        ((("36:21"), "« 70 ANS » (SABBATS)")),
        ((("Esd 1:1"), "CYRUS (1re !)")),
        ((("Dn 9:2"), "LIVRES (DISCERNA)"))],
    src=[("Jérusalem — Étude (vide, 70 ans désolée, pas de colonies)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012382"),
        ("Jéhovah, Celui qui fait accomplir ses prophéties (70 sabbats, 607→537)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1964886"),
        ("2 Chroniques 36 — Bible d'étude (chute, sabbats, 36:15-21)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/36")],
    img="images/prophe_CH104_sabbats.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="ED105", titre="« Qu'il monte à Jérusalem ! » : Cyrus réveillé décrète le retour et la maison",
    ref="Esdras 1:1-4",
    statut="Accomplie",
    cat="ED", syst="Décret de Cyrus (1re année → réveillé → proclamation → Dieu ciel → montez → aidés → ustensiles)",
    reg="Registre : Esdras — P105 (1:1-4 : décret de Cyrus, reconstruction de la maison) ; accomplissement Esd 1:5-11 ; 6:3-15",
    texte=[
        "« 1re ANNÉE CYRUS… PAROLE JÉRÉMIE… RÉVEILLA ESPRIT. » (1:1 — esprit !)",
        "« PROCLAMATION… BOUCHE + ÉCRIT… TOUT ROYAUME. » (1:1 — royaume !)",
        "« DIEU du CIEL… DONNÉ ROYAUMES… CHARGÉ MAISON. » (1:2 — maison !)",
        "« QUI de son PEUPLE ?… QU'IL MONTE… BÂTISSE ! » (1:3 — bâtisse !)",
        "« AIDÉS… ARGENT OR BÉTAIL… VOLONTAIRES. » (1:4 — volontaires !)",
        "« ESPRITS RÉVEILLÉS… SE LEVÈRENT… BÂTIR. » (1:5 — levèrent !)",
        "« VOISINS AIDÈRENT… ARGENT OR… PRÉCIEUX. » (1:6 — précieux !)",
        "« USTENSILES RENDUS… SHESHBATSA… 5 400. » (1:7-11 — 400 !)",
        "« MÉMORANDUM… ECBATANE… RETROUVÉ… DARIUS. » (6:1-2 — retrouvé !)",
        "« MAISON REBÂTIE… DÉPENSES ROI… ACHEVÉE. » (6:3-15 — achevée !)",
    ],
    contexte=(
        "Babylone, 537 — CYRUS le PERSE (les 539 (les BABYLONE (les PRISES (les NUIT (les FLEUVES (les DÉTOURNÉS (les "
        "PORTES (les OUVERTES (les EMPIRES (les TRANSFÉRÉS (les ACHÉMÉNIDES (les FONDÉS (les POLITIQUES — les "
        "TOLÉRANTES (les PEUPLES (les RENVOYÉS (les DIEUX (les RESTAURÉS !). NOMMÉ 150 ANS AVANT (Is 44:28-45:1 : les "
        "KÔRESH (les CITÉS (les SIÈCLES (les AVANT (les NAISSANCES (les « OINT (mashiach) » (les PAÏENS (les OINTS (les "
        "PROPHÉTIES — les NOMINALES (les VERTIGINEUSES (les PREUVES (les MASSIVES ! : texte biblique cité, fiche Isaïe "
        "à venir). 70 ANS FINIS (Jr 25:12 + 29:10 : les COMPTES (les ÉCOULÉS (les DANIEL (les CALCULE (Dn 9:2 ! (les "
        "DÉCRETS (les PONCTUELS (les HORLOGES — les PROPHÉTIQUES (les SONNENT !). SHESHBATSA (1:8 : les PRINCES (les "
        "JUDA (les nesi'im (les ZOROBABEL ? (les MÊMES (les DIFFÉRENTS (les DÉBATS (les GOUVERNEURS (les PREMIERS (les "
        "RETOURS (les CONDUITS (les IDENTITÉS — les FLOUES (les RÔLES (les CLAIRS !)."
    ),
    explication=(
        "« JÉHOVAH RÉVEILLA ('ur) l'ESPRIT (ruach) de CYRUS », 1:1 : 'ur — RÉVEILLER (les SOMMEILS (les SPIRITUELS "
        "(les PAÏENS (les SECOUÉS (les DÉCISIONS (les INSPIRÉES (les SOUVERAINETÉS — les INTIMES (les CŒURS (les ROIS "
        "(les TOURNÉS (Pr 21:1 !). « Il FIT PASSER (ya'aver) une PROCLAMATION (qol)… par ÉCRIT (vemikhtav) », 1:1 : "
        "qol + mikhtav — VOIX + ÉCRIT (les HÉRAUTS (les CRIENT (les SCRIBES (les NOTENT (les DIFFUSIONS — les DOUBLES "
        "(les ORALES (les ARCHIVÉES (les PREUVES (les CONSERVÉES !). « Le DIEU du CIEL (elohé hashamayim)… M'A DONNÉ "
        "(natan) TOUS les ROYAUMES », 1:2 : natan — DONNER (les CONFESSIONS (les PAÏENNES (les SOURCES (les POUVOIRS "
        "(les RECONNUES (les THÉOLOGIES — les CYRUS (les ÉTONNANTES (les VRAIES (les PARTIELLES !). « Il M'A CHARGÉ "
        "(paqad)… de lui BÂTIR (livnot) une MAISON (bayit) », 1:2 : paqad — CHARGER (les MISSIONS (les DONNÉES (les "
        "PAÏENS (les MAÇONS (les TEMPLES (les VOCATIONS — les IMPROBABLES (les EXÉCUTÉES !). « QUI (mi)… de son PEUPLE "
        "(me'ammo) ?… QU'IL MONTE (ya'al) », 1:3 : 'alah — MONTER (les APPELS (les VOLONTAIRES (les MONTÉES (les "
        "JÉRUSALEM (les PÈLERINAGES (les RETOURS (les ASCENSIONS — les SPIRITUELLES (les GÉOGRAPHIQUES !). « Avec des "
        "DONS VOLONTAIRES (nedavah) », 1:4 : nedavah — VOLONTAIRE (les GÉNÉROSITÉS (les SPONTANÉES (les CŒURS (les "
        "LARGES (les FINANCEMENTS — les PARTICIPATIFS (les FOULES (les BÂTISSEUSES !)."
    ),
    interpretation=(
        "Dieu UTILISE les PAÏENS (les CYRUS (les NON-CROYANTS (les INSTRUMENTS (les OINTS (les MISSIONS (les ACCOMPLIES "
        "(les FOIS — les NON-REQUISES (les OBÉISSANCES (les OBTENUES !). « RÉVEILLA les ESPRITS » (1:5 : les PLURIELS "
        "(les CYRUS (les PEUPLES (les CHEFS (les PRÊTRES (les LÉVITES (les RÉVEILS — les COLLECTIFS (les DÉPARTS (les "
        "VOLONTAIRES (les 50 000 (les LEVÉS !). Les VOISINS AIDENT (1:6 : les EXODES (les RÉPÉTÉS (Ex 12:36 : « ils "
        "DÉPOUILLÈRENT » (les ÉGYPTIENS (les BABYLONIENS (les SPOLIÉS (les GÉNÉREUX (les SORTIES — les ENRICHIES (les "
        "OPPRESSEURS (les FINANCENT (les LIBÉRATIONS !). RO097 INVERSÉ (les « TOUT EMPORTÉ » (les RO097 ! (les « TOUT "
        "RENDU » (les 5 400 (les USTENSILES (les INVENTORIÉS (les RESTITUTIONS — les COMPTABLES (les BUTINS (les REMBOURSÉS "
        "!). ECBATANE (6:2 : les ARCHIVES (les RETROUVÉES (les MÉMORANDUMS (les CONSERVÉS (les DIEUX (les GARDENT (les "
        "REÇUS (les PROOFS — les ADMINISTRATIFS (les PROPHÉTIES (les CLASSÉES !)."
    ),
    hist=(
        "Le CYLINDRE de CYRUS (les POLITIQUES (les RETOURS (les PEUPLES (les DIEUX (les RESTAURÉS (les PROPAGANDES (les "
        "TOLÉRANTES (les JUIFS (les NON-NOMMÉS (les PRUDENCES — les REQUISES (les CONTEXTES (les CONFIRMÉS (les DÉTAILS "
        "(les BIBLIQUES (les UNIQUES ! : fond seul, jamais en sources). 539 PRISE (les HÉRODOTE (les XÉNOPHON (les "
        "FLEUVES (les DÉTOURNÉS (les FÊTES (les BELSHATSAR (les SURPRISES (les PORTES (les OUVERTES (les RÉCITS — les "
        "CROISÉS (les GRECS (les HÉBREUX (les CONCORDANTS !). 537 PIVOT (les TISRI (les RETOURS (les AUTELS (les "
        "REBÂTIS (Esd 3:1-3 ! (les CULTES (les RESTAURÉS (les AVANT-MURS (les PRIORITÉS — les SPIRITUELLES (les "
        "ADORATIONS (les PREMIÈRES !) + 1965684 : « 537… DATE… DÉCRET… CONFIRMATION de l'ACCOMPLISSEMENT de CERTAINES "
        "PROPHÉTIES » (OFFICIEL ! (les PIVOTS — les DOUBLES (les HISTORIQUES (les PROPHÉTIQUES !). ECBATANE (les 1 914 M "
        "(les ELVEND (les ÉTÉS (les FRAIS (les ARCHIVES (les ROYALES (les MÉMORANDUMS (les RETROUVÉS : 1200013366 : « "
        "C'est à ECBATANE que l'on RETROUVA… le MÉMORANDUM… (Esd 6:2-5) » (OFFICIEL ! (les ALTITUDES — les ARCHIVES "
        "(les FRAÎCHES (les CONSERVÉES !)."
    ),
    geo=(
        "BABYLONE → JÉRUSALEM (les 900 KM (les 4 MOIS (Esd 7:9 ! (les CARAVANES (les FAMILLES (les TRÉSORS (les ROUTES "
        "(les FERTILES (les CROISSANTS (les VOYAGES — les ÉPIQUES (les EXODES (les SECONDS !). ECBATANE (les HAMADAN (les "
        "MÈDES (les CAPITALES (les ÉTÉ (les 1 914 M (les ELVEND (les ARCHIVES (les PALAIS (les MÉMORANDUMS (les DORMENT "
        "(les DÉCOUVERTES — les ULTÉRIEURES (les DARIUS (les VÉRIFIE !) + 1200013366 : « PASARGADE… à environ 650 KM au "
        "SUD-EST d'ECBATANE » (OFFICIEL ! (les DISTANCES — les MESURÉES (les EMPIRES (les VASTES !). JÉRUSALEM RUINES "
        "(les RETOURS (les CHOCS (les DÉSALTATIONS (les RECONSTRUCTIONS (les AMORCÉES (les AUTELS (les PREMIERS (les "
        "FONDATIONS (les SECOND (les OPPOSITIONS (les SAMARITAINS (Esd 4 ! : les CHANTIERS — les CONTESTÉS (les "
        "INTERROMPUS (les REPRIS !). L'EMPIRE (les « TOUS les ROYAUMES » (les 1:2 (les PERSES (les MÈDES (les LYDIENS "
        "(les BABYLONIENS (les ÉTENDUES (les CONTINENTALES (les PROCLAMATIONS — les MONDIALES (les HÉRAUTS (les PARTOUT !)."
    ),
    sci=(
        "L'ARCHIVISTIQUE (6:1-2 : les RECHERCHES (les TRÉSORS (les ROULEAUX (les bet-siphraya (les MAISONS (les LIVRES "
        "(les CLASSEMENTS (les ANTIQUES (les RETROUVAILLES (les MIRACULEUSES (les BUREAUCRATIES — les EFFICACES (les "
        "MÉMOIRES (les IMPÉRIALES !). La MÉTALLURGIE (1:9-11 : les 5 400 (les COUPES (les OR (les ARGENT (les COUTEAUX "
        "(les INVENTAIRES (les DÉTAILLÉS (les COMPTES (les PRÉCIS (les RESTITUTIONS — les VÉRIFIABLES (les TRANSPARENCES "
        "(les TOTALES !). La LOGISTIQUE (2:64-65 : les 42 360 + 7 337 + 200 (les ~50 000 (les PERSONNES (les CHEVAUX "
        "(les MULETS (les CHAMEAUX (les ÂNES (les CONVOIS (les IMMENSES (les RAVITAILLEMENTS (les 4 MOIS (les "
        "ORGANISATIONS — les PRODIGIEUSES (les EXODES (les PLANIFIÉS !). La CLIMATOLOGIE (les ÉTÉS (les BABYLONIENS "
        "(les TORRIDES (les ECBATANE (les FRAÎCHEUR (les 1 914 M (les TRANSHUMANCES (les ROYALES (les CONFORTS — les "
        "ALTITUDINAUX (les DÉCRETS (les ESTIVAUX !)."
    ),
    schema=(
        "CYRUS EN 10 TEMPS : 70 ANS (les ÉCOULÉS (CH104 !) → 1re ANNÉE (« PAROLE JÉRÉMIE » : les PONCTUELS !) → RÉVEILLÉ "
        "(« ESPRIT de CYRUS » : les SECOUÉS !) → PROCLAMATION (« BOUCHE + ÉCRIT… TOUT ROYAUME » : les DIFFUSÉS !) → « "
        "DIEU du CIEL… DONNÉ » (les CONFESSÉS !) → « CHARGÉ… MAISON » (les MISSIONNÉS !) → « QUI… QU'IL MONTE » (les "
        "APPELÉS !) → « AIDÉS… VOLONTAIRES » (les FINANCÉS !) → ESPRITS (« RÉVEILLÉS… LEVÈRENT » : les MOBILISÉS !) → "
        "VOISINS (« AIDÈRENT… PRÉCIEUX » : les DÉPOUILLÉS !) → USTENSILES (« RENDUS… 5 400 » : les RESTITUÉS !) → "
        "ECBATANE (« MÉMORANDUM… RETROUVÉ » : les ARCHIVÉS !) → ACHEVÉE (6:15 : les TERMINÉES !). Réveillé, il proclame "
        "— cinquante mille montent, cinq mille quatre cents reviennent."
    ),
    limites=(
        "Le CYLINDRE (les JUIFS (les ABSENTS (les TEXTES (les GÉNÉRAUX (les POLITIQUES (les GLOBALES (les DÉCRETS (les "
        "SPÉCIFIQUES (les BIBLIQUES (les COMPLÉMENTS (les NON-CONTRADICTIONS (les PRUDENCES — les EXÉGÉTIQUES (les "
        "TRIOMPHALISMES (les ÉVITÉS : fond seul !). SHESHBATSA (1:8 : les ZOROBABEL (les MÊMES (les ONCLES (les "
        "DIFFÉRENTS (les TITRES (les NOMS (les BABYLONIENS (les HÉBREUX (les IDENTIFICATIONS (les DÉBATTUES (les RÔLES "
        "(les SUCCESSIFS (les PROPOSÉS !). Les 50 000 (2:64-65 : les CHIFFRES (les PRÉCIS (les FAMILLES (les LISTÉES "
        "(les EXACTITUDES (les SCRIBES (les COPIES (les VARIANTES (les NÉHÉMIE 7 (les PARALLÈLES (les DIFFÉRENCES (les "
        "MINEURES (les HARMONIES (les PROPOSÉES !). ORAL + ÉCRIT (1:1 : les DEUX (les FORMES (les HÉRAUTS (les ARCHIVES "
        "(les DIFFUSIONS (les COMPLÉMENTAIRES (les CONSERVATIONS (les INÉGALES (les ÉCRITS (les RETROUVÉS (les VOIX "
        "(les PERDUES !). Les DATES (les 537 (les 1965684 (les OFFICIELLES (les TISRI (les RETOURS (les HIVER-PRINTEMPS "
        "(les DÉCRETS (les SAISONS (les RECONSTITUÉES (les VRAISEMBLANCES (les FORTES !)."
    ),
    accomplissement=[(("1:1-2", "RÉVEILLÉ + « DIEU CIEL… CHARGÉ »")),
        ((("1:3-4"), "« MONTEZ ! » + « AIDÉS »")),
        ((("1:5-6"), "ESPRITS (LEVÈRENT !) + VOISINS")),
        ((("1:7-11"), "USTENSILES (5 400 !)")),
        ((("6:1-5"), "ECBATANE (RETROUVÉ !)")),
        ((("6:6-15"), "DARIUS + ACHEVÉE (!)"))],
    tl=[((("1:1"), "RÉVEILLÉ (CYRUS)")),
        ((("1:3"), "« MONTEZ ! » (MAISON)")),
        ((("1:11"), "5 400 (RENDUS !)")),
        ((("6:2"), "ECBATANE (ARCHIVES)")),
        ((("6:15"), "ACHEVÉE (DARIUS)"))],
    src=[("Une date pivot de l'Histoire (537, décret de Cyrus, retour)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
        ("Perse, Perses — Étude (décret 537, Ecbatane, mémorandum)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013366"),
        ("Esdras 1 — Bible d'étude (décret, retour, 1:1-11)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/15/1")],
    img="images/prophe_ED105_cyrus.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="NE106", titre="« De là-bas je vous rassemblerai » : Néhémie plaide Moïse pour les dispersés",
    ref="Néhémie 1:8, 9",
    statut="Accomplie",
    cat="NE", syst="Prière de Néhémie (Kislev → nouvelles → pleura → confession → Moïse → disperserai → rassemblerai)",
    reg="Registre : Néhémie — P106 (1:8, 9 : rassemblement des dispersés vers le lieu choisi) ; accomplissement Né 7:6 ; 8:1-18",
    texte=[
        "« KISLEV… 20e ANNÉE… SUSE… HANANI VINT. » (1:1-2 — vint !)",
        "« RESTE… AFFLICTION… MUR BRISÉE… PORTES FEU. » (1:3 — feu !)",
        "« ENTENDIT… PLEURA… JEÛNA… PRIA… JOURS. » (1:4 — jours !)",
        "« CONFESSION… NOUS AVONS AGI… PAS GARDÉ. » (1:6-7 — gardé !)",
        "« SOUVIENS-TOI… PAROLE MOÏSE… INFIDÈLES… DISPERSERAI. » (1:8 — disperserai !)",
        "« SI REVENEZ… BOUT des CIEUX… RASSEMBLERAI… LIEU CHOISI… NOM. » (1:9 — nom !)",
        "« SERVITEURS… RACHETÉS… PUISSANCE… MAIN FORTE. » (1:10 — forte !)",
        "« ÉCHANSON… ROI… SUCCÈS… FAVEUR. » (1:11 — faveur !)",
        "« RETOURS… JÉRUSALEM… JUDA… VILLES. » (7:6 — villes !)",
        "« ASSEMBLÉS… PLACE… LECTURE… COMPRIRENT… FÊTE. » (8:1-18 — fête !)",
    ],
    contexte=(
        "Suse, 445 — NÉHÉMIE ÉCHANSON (1:11 : les mashqeh — ÉCHANSONS (les GOÛTEURS (les POISONS (les CONFIANCES (les "
        "ABSOLUES (les PROXIMITÉS (les ROYALES (les INFLUENCES — les STRATÉGIQUES (les POSTES (les PROVIDENTIELS !). "
        "ARTAXERXÈS Ier (les 20e ANNÉE (les 445 (les LONGUE-MAIN (les EMPIRES (les APOGÉES (les AUTORISATIONS (les "
        "ACCORDÉES (2:1-8 ! (les LETTRES (les ESCORTES (les BOIS (les FORÊTS (les ROYALES (les FAVEURS — les INOUÏES "
        "(les PAÏENS (les FINANCENT (les MURS !). 13 ANS APRÈS ESDRAS (458 : les RETOURS (les VAGUES (les SUCCESSIVES "
        "(les TEMPLE (les REBÂTI (les 515 (les MURS (les RUINES (les VILLES (les OUVERTES (les DANGERS — les "
        "PERSISTANTS (les ŒUVRES (les INACHEVÉES !). HANANI (1:2 : les FRÈRES (les NOUVELLES (les FRAÎCHES (les JUDA "
        "(les TÉMOINS (les OCULAIRES (les RAPPORTS — les ALARMANTS (les AFFLICTIONS (les GRANDES (les HONTES (les "
        "REPROCHES !). MOÏSE CITÉ (1:8-9 : les Dt 30:1-4 (les Lv 26 (les Dt 28 (les LOIS (les CONNUES (les EXIL (les "
        "ÉTUDIÉES (les PRIÈRES (les NOURRIES (les ÉCRITURES — les PLAIDÉES (les PROMESSES (les RÉCLAMÉES !)."
    ),
    explication=(
        "« SOUVIENS-TOI (zekhor-na')… de la PAROLE (haddavar)… à MOÏSE », 1:8 : zakhar — SE SOUVENIR (les PLAIDOYERS "
        "(les SCRIPTURAIRES (les DIEUX (les RAPPELÉS (les PROMESSES (les EXIGÉES (les PRIÈRES — les BIBLIQUES (les "
        "EFFICACES (cf. RO096 : « SOUVIENS-TOI » ! : les VERBES — les EXAUCÉS !). « Si vous ÊTES INFIDÈLES (tim'alu)… "
        "je vous DISPERSERAI (aphits otkhem) », 1:8 : ma'al + puts — INFIDÉLITÉ + DISPERSER (les MENACES (les "
        "RÉALISÉES (les EXILS (les EXPLIQUÉS (les CAUSES (les RECONNUES (les CONFESSIONS — les LUCIDES (les JUGEMENTS "
        "(les MÉRITÉS !). « Si vous REVENEZ (tashuvu) à MOI… vous GARDEZ (shamartem) », 1:9 : shuv + shamar — REVENIR "
        "+ GARDER (les CONDITIONS (les DOUBLES (les RETOURS (les OBÉISSANCES (les REPENTIRS — les COMPLETS (les CŒURS "
        "(les CONDUITES !). « Quand vos DISPERSÉS (niddachekhem) seraient au BOUT (biqtse) des CIEUX (hashamayim) », "
        "1:9 : nadach + qatseh — DISPERSER + BOUT (les EXTRÉMITÉS (les COSMIQUES (les DIASPORAS (les TOTALES (les "
        "DISTANCES — les INSURMONTABLES (les HUMAINEMENT (les NÉGLIGEABLES (les DIVINEMENT !). « De LÀ-BAS (misham) je "
        "les RASSEMBLERAI (aqabtssem) », 1:9 : qabats — RASSEMBLER (les CONTRAIRES (les DISPERSER (les SYMÉTRIES (les "
        "COVENANTS (les DISPERSIONS (les RÉVERSIBLES (les EXILS — les TEMPORAIRES (les RETOURS (les GARANTIS !). « Au "
        "LIEU (hammaqom) que J'AI CHOISI (bacharti)… pour mon NOM (shemi) », 1:9 : bachar + shem — CHOISIR + NOM (les "
        "Dt 12 (les CENTRALISATIONS (les SION (les ÉLUES (les PRÉSENCES (les LOCALISÉES (les DESTINATIONS — les "
        "UNIQUE (les RETOURS (les ORIENTÉS !)."
    ),
    interpretation=(
        "PRIER avec la BIBLE (les MOÏSE (les CITÉS (les PROMESSES (les PLAIDÉES (les DIEUX (les PRIS (les MOTS (les "
        "MÉTHODES — les NÉHÉMIE (les MODÈLES (les PRIÈRES (les SCRIPTURAIRES !). DISPERSION/RASSEMBLEMENT (les "
        "SYMÉTRIES (les EXILS (les ENTRÉES (les SORTIES (les JUGEMENTS (les GRÂCES (les BALANCES — les COVENANTS (les "
        "MENACES (les TENUES (les PROMESSES (les TENUES !). « NOUS » SOLIDAIRE (1:6-7 : les CONFESSIONS (les "
        "COLLECTIVES (les NÉHÉMIE (les NÉS (les EXIL (les INNOCENTS ? (les COUPABLES (les AVEC (les SOLIDARITÉS — les "
        "NATIONALES (les HUMILITÉS (les PARTAGÉES !). ÉCHANSON PROVIDENTIEL (les POSTES (les STRATÉGIQUES (les "
        "ÉSTHER (les PRÉCÉDENTS (les COURS (les PAÏENNES (les INFILTRÉES (les PEUPLES — les SAUVÉS (les INTÉRIEURS !). "
        "8:1-18 JOYEUX (les RASSEMBLÉS (les PLACES (les LECTURES (les COMPRISES (les LARMES (les JOIES (les HUTTES (les "
        "FÊTÉES (les ACCOMPLISSEMENTS — les FESTIFS (les RETOURS (les CÉLÉBRÉS !)."
    ),
    hist=(
        "ARTAXERXÈS Ier (les 465-424 (les 20e ANNÉE (les 445 (les DÉCRETS (les MURS (les AUTORISÉS (les MISSIONS (les "
        "OFFICIELLES (les GOUVERNEURS (les NOMMÉS (les DATES — les ANCRÉES (les CHRONOLOGIES (les SÛRES !). SUSE (les "
        "PALAIS (les FOUILLES (les APADANAS (les CAPITALES (les HIVER (les ÉLAM (les ARCHÉOLOGIES — les SOMPTUEUSES "
        "(les DÉCORS (les RECONSTITUÉS (les LOUvre (les EXPOSÉS !). 52 JOURS (6:15 : les MURS (les REBÂTIS (les VITESSE "
        "(les RECORDS (les ENNEMIS (les DÉCOURAGÉS (les DIEUX (les RECONNUS (les CHANTIERS — les MIRACULEUX (les "
        "ORGANISATIONS (les NÉHÉMIE !). FÊTE HUTTES (8:14-17 : « DEPUIS… JOSUÉ » (les SIÈCLES (les INTERROMPUES (les "
        "REPRISES (les JOIES (les GRANDES (les CONTINUITÉS — les RESTAURÉES (les TRADITIONS (les RESSUSCITÉES !)."
    ),
    geo=(
        "SUSE (1:1 : les SHUSHAN (les ÉLAM (les 350 KM (les BABYLONE (les PALAIS (les HIVER (les ÉCHANSONS (les SERVENT "
        "(les DISTANCES — les EXILS (les CONFORTS (les NOSTALGIES !). JÉRUSALEM MURS (1:3 : les BRÈCHES (les 140 ANS "
        "(les RUINES (les PORTES (les BRÛLÉES (les VILLES (les OUVERTES (les VULNÉRABILITÉS — les HONTEUSES (les "
        "REPROCHES (les VOISINS !). « BOUT des CIEUX » (1:9 : les DIASPORAS (les EMPIRES (les PERSES (les VASTES (les "
        "INDE (les ÉTHIOPIE (Est 1:1 ! (les 127 PROVINCES (les DISPERSIONS — les MONDIALES (les RASSEMBLEMENTS (les "
        "MIRACULEUX !). Le LIEU CHOISI (1:9 : les SION (les TEMPLES (les NOMS (les RÉSIDENT (les DESTINATIONS (les "
        "UNIQUES (les PÈLERINAGES — les ORIENTÉS (les RETOURS (les FOCALISÉS !)."
    ),
    sci=(
        "L'ŒNOLOGIE (1:11 : les ÉCHANSONS (les GOÛTEURS (les VINS (les POISONS (les DÉTECTÉS (les CONFIANCES (les "
        "ABSOLUES (les VIES (les ROIS (les DÉPOSÉES (les FONCTIONS — les DÉLICATES (les GORGES (les BOUCLIERS !). La "
        "FINANCE (5:14-18 : les GOUVERNEURS (les SALAIRES (les REFUSÉS (les 12 ANS (les TABLES (les 150 (les NOURRIS "
        "(les FRAIS (les PROPRES (les INTÉGRITÉS — les FISCALES (les EXEMPLAIRES (les CORRUPTIONS (les REFUSÉES !). "
        "L'ACOUSTIQUE (8:1-8 : les PLACES (les PORTES (les EAUX (les LECTURES (les MATIN-MIDI (les FOULES (les "
        "ÉCOUTENT (les LÉVITES (les EXPLIQUENT (les TRADUISENT ? (les ARAMÉEN ? (les PÉDAGOGIES — les MASSIVES (les "
        "COMPRÉHENSIONS (les ASSURÉES !). L'URBANISME (les MURS (les PORTES (les TOURS (les BRECHES (les RELEVÉS (3 ! "
        "(les SECTIONS (les FAMILLES (les CHANTIERS (les PARCELLÉS (les GÉNIES — les CIVILS (les ANTIQUES (les "
        "EFFICACES !)."
    ),
    schema=(
        "NÉHÉMIE EN 11 TEMPS : KISLEV (« 20e ANNÉE… SUSE » : les DATÉS !) → HANANI (« VINT… JUDA » : les INFORMÉS !) → « "
        "AFFLICTION… MUR… FEU » (les ALARMÉS !) → PLEURA (« JEÛNA… PRIA… JOURS » : les AFFLIGÉS !) → CONFESSION (« NOUS "
        "AVONS AGI » : les SOLIDAIRES !) → « SOUVIENS-TOI… MOÏSE » (les PLAIDEURS !) → « INFIDÈLES… DISPERSERAI » (les "
        "MENACÉS !) → « REVENEZ… BOUT CIEUX » (les CONDITIONNÉS !) → « RASSEMBLERAI… LIEU… NOM » (les PROMIS !) → « "
        "RACHETÉS… PUISSANCE » (les RAPPELÉS !) → ÉCHANSON (« SUCCÈS… FAVEUR » : les POSITIONNÉS !) → MURS (52 JOURS !) → "
        "ASSEMBLÉE (« LECTURE… FÊTE » : les RASSEMBLÉS !). Le bout des cieux n'est pas trop loin — le lieu choisi les "
        "attend."
    ),
    limites=(
        "ARTAXERXÈS Ier (les CONSENSUS (les 445 (les II ? (les MINORITÉS (les 385 ? (les CHRONOLOGIES (les ESDRAS (les "
        "LIÉES (les DÉBATS (les SAVANTS (les DATES — les MAJORITAIRES (les ADOPTÉES !). « DEPUIS JOSUÉ » (8:17 : les "
        "LITTÉRAUX (les HUTTES (les JAMAIS (les SALOMON ? (les ESDRAS 3 ? (les SENS (les FERVEUR (les INÉGALÉE (les "
        "INTERPRÉTATIONS (les PROPOSÉES (les HYPERBOLES (les POSSIBLES !). Les LISTES (7:6-73 : les ESDRAS 2 (les "
        "PARALLÈLES (les DIFFÉRENCES (les CHIFFRES (les VARIANTES (les COPIES (les FAUTES (les HARMONIES (les PROPOSÉES "
        "(les TOTAUX (les CONCORDENT (les DÉTAILS (les DIVERGENT !). La PRIÈRE EXAUCÉE (2:1-8 : les 4 MOIS (les KISLEV → "
        "NISAN (les ATTENTES (les TRISTESSES (les REMARQUÉES (les DEMANDES (les ACCORDÉES (les DÉLAIS — les ÉPROUVÉS "
        "(les PATIENCES (les RÉCOMPENSÉES !). L'ARAMÉEN (8:8 : les TRADUISAIENT ? (les EXPLIQUAIENT (les LANGUES (les "
        "EXIL (les OUBLIÉES (les HÉBREUX (les COMPRIS (les DÉBATS (les LINGUISTES (les TARGUMS (les ORIGINES (les "
        "DISCUTÉES !)."
    ),
    accomplissement=[(("1:1-4", "KISLEV + NOUVELLES + PLEURA (JOURS !)")),
        ((("1:5-7"), "CONFESSION (« NOUS » !)")),
        ((("1:8-9"), "MOÏSE + « DISPERSERAI… RASSEMBLERAI »")),
        ((("1:10-11"), "RACHETÉS + ÉCHANSON (FAVEUR !)")),
        ((("7:6"), "RETOURS (VILLES !)")),
        ((("8:1-18"), "ASSEMBLÉE + LECTURE + FÊTE (!)"))],
    tl=[((("1:3"), "« MUR… FEU » (HONTE)")),
        ((("1:4"), "PLEURA (JEÛNA)")),
        ((("1:8"), "« DISPERSERAI » (MOÏSE)")),
        ((("1:9"), "« RASSEMBLERAI » (LIEU !)")),
        ((("8:1"), "ASSEMBLÉE (PLACE !)"))],
    src=[("Néhémie — Texte (rassemblement, lieu choisi, 1:8-10)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001061120"),
        ("Nehémia — Texte (retour, muraille, rassemblement)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001060019"),
        ("Néhémie 1 — Bible d'étude (prière, Moïse, 1:4-11)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/16/1")],
    img="images/prophe_NE106_rassembles.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="IS107", titre="« Comme une hutte dans une vigne » : le pays ravagé et Sion seule debout",
    ref="Isaïe 1:7-9",
    statut="Accomplie",
    cat="IS", syst="Réquisitoire d'Isaïe (vision → fils → plaies → désolation → feu → hutte → reste → Sodome)",
    reg="Registre : Isaïe — P107 (1:7-9 : pays ravagé, Sion comme abri de veilleur) ; accomplissement 2R 18:13-16 ; 25:8-11",
    texte=[
        "« VISION… ISAÏE… JUDA JÉRUSALEM… 4 ROIS. » (1:1 — rois !)",
        "« CIEUX ÉCOUTEZ… TERRE… FILS ÉLEVÉS… RÉVOLTÉS. » (1:2 — révoltés !)",
        "« BŒUF CONNAÎT… ÂNE… ISRAËL NE CONNAÎT PAS. » (1:3 — pas !)",
        "« PLAIES… MEURTRISSURES… PAS PANSEES… HUILE. » (1:6 — huile !)",
        "« PAYS DÉSOLATION… VILLES FEU… ÉTRANGERS DÉVORENT. » (1:7 — dévorent !)",
        "« FILLE SION RESTÉE… HUTTE VIGNE… ABRI CONCOMBRES. » (1:8 — concombres !)",
        "« Comme une VILLE ASSIÉGÉE. » (1:8 — assiégée !)",
        "« Si PAS LAISSÉ RESTE… SODOME… GOMORRHE. » (1:9 — Gomorrhe !)",
        "« SENNACHÉRIB… VILLES… TRIBUT… OR PORTES. » (2R 18:13-16 — portes !)",
        "« BRÛLA MAISON… MURS… DÉPORTA… PAUVRES. » (2R 25:8-11 — pauvres !)",
    ],
    contexte=(
        "Jérusalem, ~740-700 — ISAÏE fils d'AMOTS (1:1 : les « JÉHOVAH SAUVE » (les NOMS (les PROGRAMMES (les "
        "MINISTÈRES (les 60 ANS ? (les MARTYRS (les TRADITIONS (les SCIÉS (RO098 ! (les PROPHÈTES — les MAJEURS (les "
        "ÉVANGÉLISTES (les ANCIENS !). 4 ROIS (1:1 : OZIAS (les LÉPREUX (les YOTAM (les BONS (les ACHAZ (les IMPIES "
        "(les ÉZÉCHIAS (les PIEUX (les SIÈCLES (les TRAVERSÉS (les RÈGNES (les CONTRASTÉS (les FIDÉLITÉS — les "
        "CONSTANTES (les CONTEXTES (les VARIABLES !). « VISION (chazon) » (1:1 : les VOIR (les RECEVOIR (les "
        "RÉQUISITOIRES (les COVENANTS (les Dt 32 (les TÉMOINS (les CIEL-TERRE (les PROCÈS — les DIVINS (les "
        "PLAIDOYERS (les OUVERTS !). DOUBLE HORIZON (les 701 (les SENNACHÉRIB (les ASSYRIENS (les 607 (les "
        "NEBUCADNETSAR (les BABYLONIENS (les DEUX (les RAVAGES (les DEUX (les ACCOMPLIS (les PROPHÉTIES — les "
        "ÉTAGES (les PREMIERS (les SECONDS !)."
    ),
    explication=(
        "« Votre PAYS ('artsekhem) est une DÉSOLATION (shemamah) », 1:7 : shemamah — DÉSOLATION (les ÉTATS (les "
        "ACCOMPLIS (les PRÉSENTS (les PROPHÉTIQUES (les PARFAITS (les CERTITUDES (les GRAMMAIRES — les JUGEMENTS (les "
        "DÉJÀ-VUS !). « Vos VILLES ('arekhem) sont CONSUMÉES (seruphoth) par le FEU ('esh) », 1:7 : saraph — BRÛLER "
        "(les INCENDIES (les SYSTÉMATIQUES (les POLITIQUES (les TERRE-BRÛLÉE (les ENNEMIS (les PRATIQUENT (les "
        "DÉSASTRES — les URBAINS (les RUINES (les FUMANTES !). « Des ÉTRANGERS (zarim) DÉVORENT (okhelim)… SOUS vos "
        "YEUX (le'enekhem) », 1:7 : zar + akhal — ÉTRANGER + DÉVORER (les RÉCOLTES (les PILLÉES (les SPECTATEURS (les "
        "IMPUISSANTS (les HUMILIATIONS — les PUBLIQUES (les FRUITS (les VOLÉS (les REGARDS !). « La FILLE (bat) de SION "
        "(tsiyyon) est RESTÉE (notarah) », 1:8 : bat + yatar — FILLE + RESTER (les PERSONNIFICATIONS (les VILLES (les "
        "FEMMES (les SURVIVANTES (les SOLITUDES (les TENDRESSES — les TRAGIQUES (les CAPITALES (les VEUVES !). « Comme "
        "une HUTTE (sukkah) dans une VIGNE (kherem)… un ABRI (melunah) dans un CHAMP (miqshah) de CONCOMBRES », 1:8 : "
        "sukkah + melunah — HUTTE + ABRI (les CABANES (les SAISONNIÈRES (les GARDIENS (les RÉCOLTES (les FRAGILES (les "
        "TEMPORAIRES (les VULNÉRABILITÉS — les TOTALES (les SOUFFLES (les RENVERSENT !) + 2006882 : « JÉRUSALEM PARAÎTRA "
        "EXTRÊMEMENT VULNÉRABLE, aussi FRAGILE qu'une SIMPLE HUTTE… que l'on RENVERSE SANS PEINE » (OFFICIEL ! (les "
        "FRAGILITÉS — les OFFICIELLES (les HUTTES (les POUSSÉES !). « Si JÉHOVAH… ne nous avait LAISSÉ (hothir) un RESTE "
        "(sarid) », 1:9 : yatar + sarid — LAISSER + RESTE (les RÉSIDUS (les GRACIEUX (les SURVIVANTS (les THÉOLOGIES (les "
        "RESTES (les FONDÉES (les JUGEMENTS — les LIMITÉS (les MISÉRICORDES (les RÉSERVES !)."
    ),
    interpretation=(
        "DOUBLE HORIZON (les 701 (les PARTIELS (les JÉRUSALEM (les ÉPARGNÉES (les 607 (les TOTAUX (les BRÛLÉES (les "
        "PROPHÉTIES — les PROGRESSIVES (les PREMIERS (les GOÛTS (les SECONDS (les PLÉNITUDES !) + 2R 18:13-16 (les "
        "TRIBUTS (les RANÇONS (les 701 (les VÉRIFIÉS !) + 2R 25:8-11 (les INCENDIES (les DÉPORTATIONS (les 607 (les "
        "SOLDÉS !). La HUTTE (les VULNÉRABILITÉS (les JÉRUSALEM (les SEULES (les ENTOURÉES (les RAVAGÉES (les DEBOUT "
        "(les MIRACLES (les FRAGILES (les PRÉSERVÉES (les IMAGES — les AGRICOLES (les PARLANTES (les PAYSANS (les "
        "COMPRENNENT !). Le RESTE (les THÉOLOGIES (les FONDATRICES (les 10:20-22 (les REVIENDRA (les Rm 9:27 (les PAUL "
        "(les CITE (les ÉLUS (les PRÉSERVÉS (les JUGEMENTS (les TAMISENT (les GRÂCES — les FILTRANTES (les RÉSIDUS (les "
        "SAINTS !). SODOME LIMITE (les COMPARAISONS (les EXTRÊMES (les ANÉANTISSEMENTS (les ÉVITÉS (les PEU (les "
        "MÉRITES (les ZÉRO (les GRÂCES (les TOUT (les FRISSONS — les SALUTAIRES (les PRESQUE-SODOME (les SAUVÉS !)."
    ),
    hist=(
        "SENNACHÉRIB 701 (les 46 VILLES (les PRISMES (les LAKISH (les RELIEFS (les TRIBUTS (les 300 + 30 (les OR (les "
        "PORTES (les DÉPOUILLÉES (les RO094 ! RO095 ! (les CONTEXTES — les CONNUS (les DÉTAILS (les CROISÉS !). 607 (les "
        "NEBUZARADAN (les BRÛLE (les MAISON (les PALAIS (les MURS (les DÉMOLIT (les DÉPORTE (les PAUVRES (les LAISSE (les "
        "VIGNERONS (les FINS — les DOCUMENTÉES (les RO098 ! (les PLATS (les RETOURNÉS !). OZIAS → ÉZÉCHIAS (les ~740-700 "
        "(les 40 ANS (les MINISTÈRES (les LONGS (les TREMBLEMENTS (les Am 1:1 (les LÈPRES (les ROYALES (les CRISES — les "
        "SUCCESSIVES (les VOIX (les CONSTANTES !). TILGATH-PILNÉSER (les ACHAZ (les VASSAUX (les 2R 16 (les AUTELS (les "
        "DAMAS (les COPIÉS (les IDOLÂTRIES — les IMPORTÉES (les JUGEMENTS (les PRÉPARÉS !)."
    ),
    geo=(
        "JUDA RAVAGÉ (1:7 : les VILLES (les FORTES (les PRISES (les CAMPAGNES (les PILLÉES (les ROUTES (les COUPÉES (les "
        "TERRITOIRES — les OCCUPÉS (les ENNEMIS (les MAÎTRES !). JÉRUSALEM SEULE (1:8 : les HUTTES (les ENTOURÉES (les "
        "CHAMPS (les RAVAGÉS (les CAPITALES (les ASSIÉGÉES (les ÎLOTS — les MIRACULEUX (les MERS (les ENNEMIES !). "
        "VIGNES + CONCOMBRES (1:8 : les CULTURES (les SAISONNIÈRES (les CABANES (les GARDIENS (les RÉCOLTES (les "
        "PROTÉGÉES (les VOLEURS (les ANIMAUX (les AGRICULTURES — les IMAGÉES (les AUDITEURS (les RURAUX !). SODOME (1:9 : "
        "les MER MORTE (les SOUVENIRS (les SOUFRE (les FEU (les ANÉANTISSEMENTS (les TOTAUX (les COMPARAISONS — les "
        "TERRIFIANTES (les SORTS (les ÉVITÉS !)."
    ),
    sci=(
        "L'AGRONOMIE (1:8 : les SUKKOTH (les CABANES (les BRANCHAGES (les TEMPORAIRES (les DÉMONTABLES (les FRAGILES "
        "(les VENTS (les RENVERSENT (les ÉPHÉMÈRES — les SAISONNIERS (les ABANDONNÉS (les HIVERS !). La POLIORCÉTIQUE "
        "(les VILLES (les ASSIÉGÉES (les BLOCUS (les FAMINES (les SOIFS (les NÉGOCIATIONS (les CAPITULATIONS (les "
        "TECHNIQUES — les ASSYRIENNES (les BABYLONIENNES (les ÉPROUVÉES !). La PYROLOGIE (les VILLES (les FEU (les "
        "COUCHES (les CENDRES (les LAKISH (les NIVEAU III (les ARAD (les STRATES (les BRÛLÉES (les DATÉES (les "
        "FOUILLES — les IGNÉES (les TÉMOINS (les CARBONISÉS !). La SISMOLOGIE (les OZIAS (les TREMBLEMENTS (les Am 1:1 "
        "(les Za 14:5 (les MÉMOIRES (les SÉISMES (les REPÈRES (les CHRONOLOGIQUES (les GÉOLOGIES — les PROPHÉTIQUES (les "
        "TERRES (les TREMBLENT !)."
    ),
    schema=(
        "ISAÏE 1 EN 11 TEMPS : VISION (« 4 ROIS » : les ENCADRÉS !) → CIEUX (« ÉCOUTEZ… TERRE » : les ASSIGNÉS !) → FILS "
        "(« ÉLEVÉS… RÉVOLTÉS » : les INGRATS !) → BŒUF (« CONNAÎT… ISRAËL PAS » : les HUMILIÉS !) → PLAIES (« PAS PANSEES » "
        ": les INFECTÉS !) → DÉSOLATION (« PAYS… » : les RAVAGÉS !) → FEU (« VILLES… » : les INCENDIÉS !) → ÉTRANGERS (« "
        "DÉVORENT… YEUX » : les PILLÉS !) → HUTTE (« VIGNE… CONCOMBRES » : les FRAGILISÉS !) → ASSIÉGÉE (« VILLE… » : les "
        "ENCERCLÉS !) → RESTE (« Si PAS LAISSÉ… » : les PRÉSERVÉS !) → SODOME (« …GOMORRHE » : les ÉVITÉS !) → 701 (« "
        "TRIBUT… PORTES » : les RANÇONNÉS !) → 607 (« BRÛLA… DÉPORTA » : les SOLDÉS !). Ravagé comme Sodome — sauf une "
        "hutte, sauf un reste."
    ),
    limites=(
        "701 ou 607 (les EMPHASES (les DÉBATS (les PROLOGUES (les SYNTHÈSES (les MINISTÈRES (les ENTIERS (les RÉSUMÉS (les "
        "DEUX (les HORIZONS (les ASSUMÉS (les « ACCOMPLIE » (les REGISTRE (les TRANCHE !). La HUTTE (les SENS (les "
        "2006882 (les OFFICIELS (les VULNÉRABILITÉS (les JÉRUSALEM (les ASSIÉGÉES (les CONSENSUS (les LARGES (les IMAGES "
        "(les CLAIR (les DÉBATS (les MINIMES !). Le RESTE (les QUI (les QUAND (les 701 (les RESCAPÉS (les 607 (les "
        "DÉPORTÉS (les RETOURS (les 537 (les ÉTAGES (les MULTIPLES (les THÉOLOGIES (les PROGRESSIVES !). La DATE d'Is 1 "
        "(les PROLOGUES (les RÉDACTIONS (les TARDIVES (les SYNTHÈSES (les COMPOSITIONS (les DÉBATS (les CRITIQUES (les "
        "UNITÉS (les DÉFENDUES (les MESSAGES (les COHÉRENTS !). SODOME (les COMPARAISONS (les LIMITES (les JUDA (les "
        "PIRE ? (les ÉZÉCHIEL 16 (les DÉVELOPPE (les GRADATIONS (les PERVERSITÉS (les MESURES (les DÉPASSÉES !)."
    ),
    accomplissement=[(("1:1-6", "VISION + FILS + BŒUF + PLAIES")),
        ((("1:7"), "DÉSOLATION + FEU + DÉVORENT (YEUX !)")),
        ((("1:8"), "HUTTE (VIGNE !) + ASSIÉGÉE")),
        ((("1:9"), "RESTE (!) + SODOME")),
        ((("2R 18:13-16"), "701 (TRIBUT ! RO095 !)")),
        ((("2R 25:8-11"), "607 (BRÛLA ! RO098 !)"))],
    tl=[((("1:1"), "VISION (4 ROIS)")),
        ((("1:7"), "DÉSOLATION (FEU !)")),
        ((("1:8"), "HUTTE (VIGNE !)")),
        ((("1:9"), "RESTE (SODOME)")),
        ((("2R 25:9"), "607 (BRÛLA !)"))],
    src=[("Points marquants du livre d'Isaïe — I (hutte, vulnérable, 1:8-9)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2006882"),
        ("Isaïe 1 — Bible d'étude (réquisitoire, reste, 1:1-9)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/1"),
        ("Isaïe 1 — Traduction du monde nouveau (vision, Sion)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/23/1")],
    img="images/prophe_IS107_veilleur.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="IS108", titre="« Ils forgeront leurs épées en socs » : les nations affluent, la guerre désapprise",
    ref="Isaïe 2:2-4",
    statut="En cours",
    cat="IS", syst="Paix des nations (vue → finale → montagne → établie → affluent → montons → forgeront → plus guerre)",
    reg="Registre : Isaïe — P108 (2:2-4 : nations affluent, épées en socs) ; accomplissement Mi 4:1-3 ; Ac 2:1-11",
    texte=[
        "« CHOSE VUE… ISAÏE… JUDA JÉRUSALEM. » (2:1 — Jérusalem !)",
        "« PÉRIODE FINALE JOURS… MONTAGNE MAISON… ÉTABLIE. » (2:2 — établie !)",
        "« AU-DESSUS MONTS… ÉLEVÉE… NATIONS AFFLUENT. » (2:2 — affluent !)",
        "« VENEZ ! MONTONS… ENSEIGNERA CHEMINS… SENTIERS. » (2:3 — sentiers !)",
        "« LOI SORTIRA SION… PAROLE… JÉRUSALEM. » (2:3 — Jérusalem !)",
        "« JUGERA NATIONS… REMETTRA ORDRE… PEUPLES. » (2:4 — peuples !)",
        "« FORGERONT ÉPÉES SOCS… LANCES SERPES. » (2:4 — serpes !)",
        "« NATION NE LÈVERA ÉPÉE… PLUS APPRENDRONT GUERRE. » (2:4 — guerre !)",
        "« MICHÉE… MÊME ORACLE… CONFIRME… TÉMOIN. » (Mi 4:1-3 — témoin !)",
        "« PENTECÔTE… NATIONS… LANGUES… 3 000. » (Ac 2:1-11 — 000 !)",
        "« ONU… MUR… ÉPÉES SOCS… ORIGINE TUE. » (New York — York !)",
    ],
    contexte=(
        "Jérusalem, ~740 — « PÉRIODE FINALE des JOURS (acharit hayyamim) » (2:2 : les ESCHATOLOGIES (les HORIZONS (les "
        "LOINTAINS (les MESSIANIQUES (les TEMPS (les DERNIERS (les ÈRES — les NOUVELLES (les ROYAUMES (les VENUS !). "
        "La MONTAGNE (2:2 : les SION (les 740 M (les TEMPLES (les TRÔNES (les ÉLÉVATIONS (les EXALTATIONS (les "
        "SUPRÉMATIES (les SPIRITUELLES (les TOPOGRAPHIES — les THÉOLOGIQUES (les COLLINES (les DÉPASSÉES !). MICHÉE "
        "CONTEMPORAIN (Mi 4:1-3 : les MÊMES (les ORACLES (les MOT-À-MOT (les DOUBLES (les TÉMOINS (les Dt 19:15 (les QUI "
        "(les PREMIERS (les DÉBATS (les INSPIRATIONS — les COMMUNES (les ESPRITS (les MÊMES !). PENTECÔTE 33 (Ac 2:1-11 : "
        "les NATIONS (les 15 (les PARTHES (les MÈDES (les ÉLAMITES (les LANGUES (les ENTENDUES (les 3 000 (les BAPTISÉS "
        "(les AFFLUENCES — les AMORCÉES (les FLEUVES (les NAISSANTS !). L'ONU (les NEW YORK (les MURS (les ESPLANADES "
        "(les CITATIONS (les SANS-SOURCES (les IDÉAUX (les AFFICHÉS (les IMPUISSANCES (les CONSTATÉES : 1102000024 : « "
        "Ces PAROLES sont INSCRITES sur un MUR… Pendant des DÉCENNIES, l'ORIGINE… N'A PAS ÉTÉ INDIQUÉE » (OFFICIEL ! "
        "(les MURS — les MUETS (les SOURCES (les TUES !)."
    ),
    explication=(
        "« Dans la PÉRIODE FINALE (beacharit) des JOURS (hayyamim) », 2:2 : acharit — FINALE (les TEMPS (les "
        "DERNIERS (les ÈRES (les MESSIANIQUES (les CALENDRIERS (les PROPHÉTIQUES (les HORIZONS — les OUVERTS (les "
        "ACCOMPLISSEMENTS (les PROGRESSIFS !). « La MONTAGNE (har)… sera solidement ÉTABLIE (nakhon) », 2:2 : kun — "
        "ÉTABLIR (les STABILITÉS (les FERMES (les FONDEMENTS (les INÉBRANLABLES (les ROYAUMES — les FIXÉS (les "
        "TREMBLEMENTS (les EXCLUS !). « AU-DESSUS (bero'sh) du SOMMET des MONTAGNES », 2:2 : ro'sh — TÊTE (les "
        "SUPRÉMATIES (les HIÉRARCHIES (les CULTES (les CONCURRENTS (les DÉPASSÉS (les EXALTATIONS — les SUPRÊMES (les "
        "RIVAUX (les ABAISSÉS !). « Toutes les NATIONS (kol-haggoyim) VIENDRONT EN FOULE (venaharu) », 2:2 : nahar — "
        "COULER (les FLEUVES (les HUMAINS (les COURANTS (les IRRÉSISTIBLES (les PÈLERINAGES — les MASSIFS (les AFFLUENCES "
        "(les FLUVIALES !). « VENEZ (lekhu) ! MONTONS (vena'aleh)… Il nous ENSEIGNERA (veyorenu) », 2:3 : halakh + 'alah "
        "+ yarah — VENIR + MONTER + ENSEIGNER (les INVITATIONS (les MUTUELLES (les ASCENSIONS (les VOLONTAIRES (les "
        "INSTRUCTIONS (les SOLLICITÉES (les TORAH — les DÉSIRÉES (les NATIONS (les ÉLÈVES !). « Ils FORGERONT (vekhitettu) "
        "leurs ÉPÉES (charvotam) en SOCS (le'ittim) », 2:4 : khatat — FORGER (les MARTELER (les BATTRE (les RECYCLER (les "
        "GUERRES (les AGRICULTURES (les MORTS (les VIES (les RECONVERSIONS — les RADICALES (les ARSENAUX (les CHARRUES !). "
        "« Ils N'APPRENDRONT PLUS (lo' yilmadu 'od) la GUERRE (milchamah) », 2:4 : lamad — APPRENDRE (les "
        "DÉSAPPRENTISSAGES (les ÉCOLES (les GUERRE (les FERMÉES (les SCIENCES (les MILITAIRES (les OUBLIÉES (les PAIX — "
        "les STRUCTURELLES (les IGNORANCES (les HEUREUSES !)."
    ),
    interpretation=(
        "EN COURS ! (les PENTECÔTE (les DÉBUTS (les NATIONS (les AFFLUENT (les ÉGLISES (les MULTIPLIENT (les SIÈCLES (les "
        "ÉCOULENT (les FLEUVES (les GROSSISSENT (les ACCOMPLISSEMENTS — les PROGRESSIFS (les FINALS (les ATTENDUS !). "
        "L'ONU IMPUISSANTE (les MURS (les CITENT (les CANONS (les TONNENT (les IDÉAUX (les AFFICHÉS (les RÉALITÉS (les "
        "DÉMENTENT (les CONTRASTES — les TRAGIQUES (les PAROLES (les VOLÉES (les PAIX (les MANQUÉES !) + 1102000024 : « "
        "L'ENSEMBLE des NATIONS N'ATTEINDRONT JAMAIS ce BUT… HORS de leur PORTÉE » (OFFICIEL ! (les VERDICTS — les "
        "OFFICIELS (les ONU (les CONDAMNÉES (les ÉCHECS !). Le CULTE PUR (les SERVITEURS (les UNIS (les NATIONS (les "
        "RÉCONCILIÉES (les ÉPÉES (les FIGURÉES (les FORGÉES (les PAIX (les VÉCUES (les COMMUNAUTÉS — les TÉMOINS (les "
        "PROPHÉTIES (les INCARNÉES !) + 1102000024 : « Les PAROLES d'ISAÏE sont RÉALISÉES par des MEMBRES de NOMBREUSES "
        "NATIONS… UNIS dans le CULTE PUR » (OFFICIEL ! (les RÉALISATIONS — les PRÉSENTES (les VISIBLES (les VÉRIFIABLES "
        "!). MICHÉE TÉMOIN (les DEUX (les BOUCHES (les Dt 19:15 (les CONFIRMATIONS (les MUTUELLES (les ORACLES — les "
        "SCELLÉS (les DOUBLE (les AUTHENTIFIÉS !)."
    ),
    hist=(
        "PENTECÔTE 33 (Ac 2:9-11 : les 15 NATIONS (les PARTHES (les MÈDES (les ÉLAMITES (les MÉSOPOTAMIENS (les "
        "JUDEENS (les CAPPADOCIENS (les PONT (les ASIE (les PHRYGIE (les PAMPHYLIE (les ÉGYPTE (les LIBYE (les ROMAINS "
        "(les CRÉTOIS (les ARABES (les INVENTAIRES — les MONDIAUX (les EMPIRES (les REPRÉSENTÉS !). L'ONU 1945 (les "
        "SAN FRANCISCO (les CHARTE (les NEW YORK (les SIÈGES (les MURS (les ISAÏE (les ANONYMES (les GUERRES (les "
        "CONTINUENT (les 1948 (les 1950 (les 1967 (les INNOMBRABLES (les ÉCHECS — les PATENTS (les IDÉAUX (les TRAHIS "
        "!). MICHÉE ~730 (les MORESHETH (les CAMPAGNARDS (les CONTEMPORAINS (les ISAÏE (les URBAINS (les DEUX (les VOIX "
        "(les MÊMES (les ORACLES (les CONFIRMATIONS — les CROISÉES (les VILLES (les CHAMPS !). L'ÉGLISE PRIMITIVE (les "
        "PAIX (les NON-VIOLENCES (les MARTYRS (les NON-RÉSISTANTS (les 3 SIÈCLES (les TÉMOINS (les DÉSARMÉS (les "
        "PRATIQUES — les ISAÏENNES (les ÉPÉES (les RANGÉES !)."
    ),
    geo=(
        "La MONTAGNE SION (2:2 : les 740 M (les MORIJA (les TEMPLES (les ÉLÉVATIONS (les SYMBOLIQUES (les SUPRÉMATIES "
        "(les SPIRITUELLES (les COLLINES (les ENTOURÉES (les DÉPASSÉES (les TOPOGRAPHIES — les TRANSFIGURÉES (les "
        "GÉOGRAPHIES (les THÉOLOGIES !). Les NATIONS (2:2 : les goyim (les PAÏENS (les LOINTAINS (les AFFLUENT (les "
        "JÉRUSALEM (les CENTRES (les ATTRACTIONS (les MONDIALES (les PÔLES — les SPIRITUELS (les BOUSSOLES (les "
        "CONVERGENTES !). SION → MONDE (2:3 : « La LOI (torah) SORTIRA (tetse') de SION » (les SOURCES (les RAYONNENT "
        "(les ENSEIGNEMENTS (les DIFFUSENT (les MISSIONS — les CENTRIFUGES (les JÉRUSALEM (les ÉMETTRICES !). NEW YORK "
        "(les EAST RIVER (les MURS (les ESPLANADES (les TOURISTES (les PHOTOGRAPHIENT (les DIPLOMATES (les PASSENT (les "
        "IRONIES — les GÉOGRAPHIQUES (les PAIX (les GRAVÉES (les GUERRES (les VOTÉES !)."
    ),
    sci=(
        "La MÉTALLURGIE (2:4 : les ÉPÉES (les charavot (les BRONZE (les FER (les FORGES (les MARTÈLEMENTS (les SOCS (les "
        "'ittim (les CHARRUES (les LANCES (les chanitot (les SERPES (les mazmerot (les RECONVERSIONS (les TECHNIQUES (les "
        "FAISABLES (les VOLONTÉS — les MANQUANTES (les FOURS (les PRÊTS !). L'AGRONOMIE (les SOCS (les LABOURS (les "
        "SERRES (les MOISSONS (les OUTILS (les PAIX (les PRODUCTIFS (les INSTRUMENTS (les MORT (les DESTINÉS (les VIES "
        "(les SYMBOLES — les PUISSANTS (les ÉCONOMIES (les CONVERTIES !). La POLÉMOLOGIE (les GUERRES (les ÉTUDIÉES (les "
        "DÉSAPPRENDRE (les ACADÉMIES (les FERMÉES (les DOCTRINES (les OUBLIÉES (les BUDGETS (les MILITAIRES (les ZÉRO (les "
        "UTOPIES — les PROPHÉTIQUES (les GARANTIES (les DIVINES !). La SOCIOLOGIE (les PAIX (les VÉCUES (les COMMUNAUTÉS "
        "(les MULTINATIONALES (les RÉCONCILIÉES (les ENNEMIS (les FRÈRES (les EXPÉRIENCES — les CONCRÈTES (les CULTES "
        "(les PURS (les TÉMOINS !)."
    ),
    schema=(
        "SOCS EN 11 TEMPS : VUE (« ISAÏE… JUDA JÉRUSALEM » : les ENCADRÉS !) → FINALE (« PÉRIODE… JOURS » : les "
        "ESCHATOLOGIQUES !) → MONTAGNE (« MAISON… » : les DÉSIGNÉES !) → ÉTABLIE (« SOLIDEMENT » : les FIXÉES !) → "
        "AU-DESSUS (« SOMMET… MONTS » : les EXALTÉES !) → AFFLUENT (« NATIONS… FOULE » : les FLUVIALES !) → « VENEZ ! "
        "MONTONS » (les INVITÉES !) → « ENSEIGNERA… SENTIERS » (les INSTRUITES !) → « LOI… SION… PAROLE… JÉRUSALEM » (les "
        "RAYONNÉES !) → « JUGERA… ORDRE » (les ARBITRÉES !) → « FORGERONT… SOCS… SERPES » (les RECONVERTIES !) → « PLUS "
        "APPRENDRONT GUERRE » (les DÉSAPPRENEUSES !) → MICHÉE (« MÊME… TÉMOIN » : les CONFIRMÉES !) → PENTECÔTE (« NATIONS… "
        "3 000 » : les AMORCÉES !) → ONU (« MUR… YORK » : les AFFICHÉES !). Les fleuves montent — les forges recyclent, "
        "les écoles de guerre ferment."
    ),
    limites=(
        "MICHÉE/ISAÏE (les QUI (les PREMIERS (les EMPRUNTS (les MUTUELS (les SOURCES (les COMMUNES (les ESPRITS (les MÊMES "
        "(les AUTHENTICITÉS (les DOUBLES (les GARANTIES (les CANONS (les DÉBATS — les SAVANTS (les FOIS (les SIMPLES !). « "
        "FINALE » (les SENS (les ÈRES (les MESSIANIQUES (les DÉBUTS (les PENTECÔTE (les FINS (les RETOURS (les ÉTAPES (les "
        "MULTIPLES (les ESCHATOLOGIES (les PROGRESSIVES (les « EN COURS » (les REGISTRE (les TRANCHE !). L'ONU (les USAGES "
        "(les SÉCULIERS (les LÉGITIMES (les DÉTOURNÉS (les IRONIES (les COMMENTÉES (les 1102000024 (les OFFICIELS (les "
        "APPLICATIONS (les AUTORISÉES (les CRITIQUES (les LIBRES !). Les EFFECTIFS (les AFFLUENCES (les COMBIEN (les "
        "NATIONS (les TOUTES (les LITTÉRAUX (les REPRÉSENTANTS (les UNIVERSALISMES (les ESCHATOLOGIQUES (les PORTÉES (les "
        "DÉBATTUES (les DIRECTIONS (les CERTAINES !). La FINALE (les GUERRES (les CESSERONT (les QUAND (les RETOURS (les "
        "CHRIST (les MILLÉNAIRES (les DÉBATS (les ÉCOLES (les SCÉNARIOS (les DIVERS (les ESPOIRS (les COMMUNS !)."
    ),
    accomplissement=[(("2:1-2", "VUE + FINALE + ÉTABLIE (DESSUS !)")),
        ((("2:2-3"), "AFFLUENT (!) + « MONTONS » + LOI (SION !)")),
        ((("2:4"), "JUGERA + FORGERONT (SOCS !) + « PLUS GUERRE »")),
        ((("Mi 4:1-3"), "MICHÉE (TÉMOIN !)")),
        ((("Ac 2:1-11"), "PENTECÔTE (NATIONS !)"))],
    tl=[((("2:2"), "FINALE (ÉTABLIE)")),
        ((("2:2"), "AFFLUENT (NATIONS !)")),
        ((("2:4"), "SOCS (FORGERONT !)")),
        ((("Mi 4:1"), "MICHÉE (MÊME !)")),
        ((("Ac 2:1"), "PENTECÔTE (33 !)"))],
    src=[("L'élévation de la maison de Jéhovah (socs, ONU, culte pur, Is 2)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102000024"),
        ("Isaïe 2 — Traduction du monde nouveau (montagne, nations, paix)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/23/2"),
        ("Isaïe 2 — Bible d'étude (période finale, socs, 2:2-4)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/2")],
    img="images/prophe_IS108_socs.jpg",
))
