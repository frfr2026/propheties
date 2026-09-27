#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE R — RELIQUATS ET COMPLEMENTS (vague 16)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="R",
    nom="Reliquats et compléments",
    vague="16",
    intro=(
        "Seizième vague : les reliquats — ces grandes prophéties restées hors des douze "
        "catégories. R001 : Joseph — les gerbes prosternées, les trois jours de prison, "
        "les sept vaches, la descente en Égypte. R002 : les clauses de l'alliance — "
        "malédictions du Lévitique, dispersion et retour du Deutéronome, cantique-témoin, "
        "adieux de Josué, prière de Néhémie. R003 : les promesses d'Isaïe et de Michée — "
        "socs de charrue, Prince de paix, faune réconciliée, pierre éprouvée, serviteur "
        "lumière, et Douma dans la nuit. R004 : les sept lettres aux congrégations. R005 : "
        "le trône, les vingt-quatre anciens, le rouleau et l'Agneau. R006 : l'aller et le "
        "retour — Osée renvoie en Égypte, Zacharie en ramène. Mêmes dix blocs, mêmes règles."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R001", titre="Joseph — les gerbes, les trois jours, les sept vaches",
 ref="Genèse 37:5-11 ; Genèse 40:8-23 ; Genèse 41:25-57 ; Genèse 46:1-7",
 statut="Accomplie (P021, P022, P023, P025)",
 cat="R", syst="Système patriarches (XVIIe s. — repères)",
 reg="Registre : Genèse — P021 (37:5-11 : rêves, prosternation), P022 (40:8-19 : échanson/panetier), P023 (41:25-32 : sept + sept), P025 (46:3-4 : descente, yeux fermés) ; rappel J005 (Gn 49, Shilo)",
 texte=[
  "« Vos GERBES se prosternaient devant ma gerbe. » (37:7 — P021 : le premier rêve !)",
  "« Le SOLEIL, la LUNE et ONZE ÉTOILES se prosternaient. » (37:9 — le second !)",
  "« Les TROIS sarments : TROIS JOURS… Pharaon te RÉTABLIRA. » (40:12-13 — P022 !)",
  "« Les TROIS corbeilles : TROIS JOURS… les oiseaux mangeront. » (40:18-19 — P022 !)",
  "« Les SEPT vaches grasses… SEPT années. Les SEPT maigres… SEPT années. » (41:26-27 — P023 !)",
  "« Le rêve RÉPÉTÉ DEUX FOIS : la chose est ARRÊTÉE. » (41:32 — P023 : ×2 = certain !)",
  "« N'aie pas PEUR de descendre… Joseph te FERMERA LES YEUX. » (46:3-4 — P025 !)",
 ],
 contexte=(
  "Joseph, 17 ans, préféré de Jacob, raconte deux rêves : ses frères « le haïrent encore "
  "plus », son père « le réprimande » (voir 2008728). Vendu 20 sicles (37:28 — C8), "
  "esclave de Potiphar, prisonnier calomnié, il interprète en prison (échanson, panetier — "
  "P022), puis devant Pharaon : les deux rêves « ont une seule et même signification » "
  "(voir 1101978076). Il a 30 ans passés quand il devient « le personnage le plus important "
  "d'Égypte après Pharaon » (voir 1101978076) ; il voyage dans tout le pays, emmagasine, "
  "épouse Asnath, père de Manassé et Éphraïm (voir it-1 « Joseph », 1200002515). Puis la "
  "famine « bien au-delà des frontières » amène les dix frères, qui « se prosternent » "
  "(voir 1200002515 : « réalisant partiellement les deux rêves »). Enfin Jacob descend, "
  "rassuré : « Joseph te fermera les yeux » (46:4 — P025)."
 ),
 explication=(
  "Gerbes (37:7) : onze gerbes des champs — les frères moissonneurs courbés ; astres (37:9) : "
  "soleil + lune + onze étoiles — père + mère + frères : toute la maison, ciel et terre. "
  "« Partiellement » (voir 1200002515) : les frères d'abord (42:6 — P021), Benjamin ensuite "
  "(43:26 — P021), Juda et tous enfin (44:14 ; 50:18 — P021) — l'accomplissement en quatre "
  "prosternations. Trois jours (40:12-19 — P022) : même chiffre, destins inverses — "
  "l'anniversaire de Pharaon (40:20 — P022) tranche. Sept + sept (41:26-27 — P023) : vaches "
  "(bétail) + épis (grain) — les deux nourritures, un seul calendrier. Rêve ×2 (41:32 — "
  "P023) : la répétition = l'arrêt — comme « tombée ×2 » (voir L010). « Fermera les yeux » "
  "(46:4 — P025) : le geste du fils à la mort du père (49:33 — P025) — la descente "
  "promet le retour des yeux, pas du corps."
 ),
 interpretation=(
  "« C'est Dieu qui l'avait envoyé en Égypte, non sans raison » (voir 1101978076) : « Dieu "
  "m'a envoyé devant vous pour préserver la vie » (45:5-8 — C8). L'échanson rétabli, le "
  "panetier pendu (40:20-22 — P022) : la prison valide le prisonnier — deux ans plus tard "
  "(41:1 — C8), l'échanson « se souvint enfin » (voir 1101978076). Abondance (41:47-54 — "
  "P023) : greniers « comme le sable de la mer » (41:49 — C8) ; famine : « tout pays venait » "
  "(41:57 — C8). Le cinquième (41:34 — C8 : impôt de 20 % pendant les grasses) : "
  "l'économie du salut. 20 sicles (37:28 — C8) : prix courant d'un esclave — l'élu vendu "
  "au tarif. 70 âmes descendent (contexte 46:27) ; une multitude remontera (voir L009 : "
  "Ex 12)."
 ),
 hist=(
  "Pharaon non nommé : Moyen Empire (Sésostris ? Hyksos ? — voir les limites : NON TRANCHÉ). "
  "Vizir sémitique : les peintures de Béni-Hassan montrent des pasteurs sémites en Égypte "
  "(repère) ; un « intendant des greniers » asiatique n'étonne pas l'égyptologie. Prix : "
  "~20 sicles l'esclave jeune à l'époque (tablettes de Nuzi, fourchette 20-30 — repère). "
  "Famine de sept ans : la stèle de Séhel (découverte 1889, texte ptolémaïque TARDIF "
  "attribuant 7 ans de famine à Djéser, IIIe dynastie — repère EXTERNE, sans lien : "
  "parallèle discuté, NON versé comme preuve — voir les limites). Le cinquième : fiscalité "
  "palatiale (Égypte : greniers d'État — voir it-Égypte, L009)."
 ),
 geo=(
  "Hébron (maison) → Sichem → Dothan (la citerne — 37:24, C8) : la descente du rêveur. "
  "Caravane ismaélite/madianite (37:25-28 — C8) : la route Galaad-Égypte (baume, myrrhe !). "
  "Égypte : le delta des greniers, le Nil des vaches (41:2 — C8 : « du Nil montaient » — "
  "les vaches du fleuve !). Goshen (contexte 46:28) : le pâturage des 70. Retour : « mes os "
  "remonteront » (50:25 — C8) — Moïse les prendra (Ex 13:19 — C8)."
 ),
 sci=(
  "Agronomie : 7 grasses + 7 maigres — cycles du Nil (crues hautes/basses — voir L009 : "
  "nilomètres) ; stockage « comme le sable » (41:49 — C8) : silos d'État, grain sur pied "
  "compté. Économie : impôt du cinquième (41:34 — C8) — 20 % prélevés, 100 % sauvés ; "
  "monétisation progressive (argent → bétail → terres → personnes, 47:14-21 — C8) : "
  "l'étatisation par la famine. Démographie : 70 → multitude en quatre générations "
  "(Ex 1:7 — C8 : « pullulèrent »). Onirologie : le récit ne théorise PAS les rêves — pas "
  "de clé générale (voir les limites) : Dieu parle, Joseph transmet, Pharaon décide."
 ),
 limites=(
  "Pharaon : NON NOMMÉ — Hyksos ? Sésostris II/III ? — non tranché (système des patriarches "
  "seul, XVIIe s. repère). Séhel : stèle TARDIVE (époque ptolémaïque), roi Djéser (IIIe dyn.) — "
  "parallèle, PAS preuve ; aucun lien externe (règle : jw.org/wol uniquement). Les rêves : "
  "aucune onirologie tirée — Joseph dit « Dieu » (41:16 — C8), point. C8 : 37:24-28, 41:1, "
  "41:16, 41:34, 41:49, 41:57, 45:5-8, 46:27-28, 47:14-21, 50:25 ; Ex 1:7, 13:19 — aucun P "
  "(vérifié : P021-P025 seuls en Gn 37-46 ; P024 = Gn 49, voir J005)."
 ),
 accomplissement=[("17 ans", "Gerbes + astres (37:7-9)"), ("20 sicles (C8)", "Dothan → Égypte"), ("3 jours", "Échanson/panetier (40:20-22)"),
     ("7 + 7", "Greniers, puis famine (41:47-54)"), ("4 prosternations", "42:6 → 50:18"), ("Descente", "Yeux fermés (46:4 → 49:33)")],
 tl=[("17 ans", "Gerbes + astres (37:7-9)"), ("20 sicles (C8)", "Dothan → Égypte"), ("3 jours", "Échanson/panetier (40:20-22)"),
     ("7 + 7", "Greniers, puis famine (41:47-54)"), ("4 prosternations", "42:6 → 50:18"), ("Descente", "Yeux fermés (46:4 → 49:33)")],
 src=[("Joseph — Étude perspicace (rasé, 7 ans, frères prosternés)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002515"),
      ("Les rêves de Pharaon (un seul sens, intendant)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101978076"),
      ("Genèse 37 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/37"),
      ("Genèse 41 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/41")],
 img="images/prophe_R001_joseph.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R002", titre="Les clauses de l'alliance — sept fois, puis le retour",
 ref="Lévitique 26:14-45 ; Deutéronome 4:25-31 ; 30:1-10 ; 31:16-21 ; 32:15-43 ; Josué 23:14-16 ; Néhémie 1:8, 9",
 statut="Accomplie (P048, P050, P056, P063, P067, P106) / Accomplie+À venir (P062, P064)",
 cat="R", syst="Système alliances (Sinaï → Moab → Sichem → Suse)",
 reg="Registre : Lévitique/Deutéronome/Josué/Néhémie — P048 (Lv 26:14-39 : malédictions), P050 (Lv 26:40-45 : confession, retour), P056 (Dt 4:25-31 : dispersion, retour), P062 (Dt 30:1-10 : rassemblés, cœur circoncis), P063 (Dt 31:16-21 : apostasie, cantique-témoin), P064 (Dt 32:15-43 : cantique, vengeance), P067 (Jos 23:14-16 : pas une parole tombée), P106 (Né 1:8-9 : rassemblés vers le lieu) ; rappel K008 (Lv 26:34-35, sabbats — versets disjoints)",
 texte=[
  "« Je vous punirai SEPT FOIS pour vos péchés. » (Lv 26:18 — P048 : ×4 dans le chapitre !)",
  "« Votre CIEL comme du FER, votre terre comme du BRONZE. » (26:19 — ciel fermé !)",
  "« Vos villes en RUINE… vos sanctuaires DÉSERTS. » (26:31 — ruine !)",
  "« Je vous DISPERSERAI… l'épée DÉGAINÉE derrière vous. » (26:33 — dispersion !)",
  "« Ils CONFESSERONT… leur cœur INCIRCONCIS s'humiliera. » (26:40-41 — P050 : l'aveu !)",
  "« Je me souviendrai de mon alliance avec JACOB… ISAAC… ABRAHAM. » (26:42 — remontée !)",
  "« Tu CHERCHERAS Jéhovah… tu REVIENDRAS. » (Dt 4:29-30 — P056 : chercher-revenir !)",
  "« Il te RAMÈNERA… il CIRCONCIRA ton cœur. » (Dt 30:3, 6 — P062 : cœur opéré !)",
  "« Ce CANTIQUE servira de TÉMOIN. » (Dt 31:19 — P063 : le chant-témoin !)",
  "« Jeshurun est devenu GRAS… et il a REGIMBÉ. » (Dt 32:15 — P064 : le gras rebelle !)",
  "« Ils ont sacrifié à des DÉMONS. » (32:17 — shedim !)",
  "« À MOI la vengeance. » (32:35 — cité Rm 12:19 ; Hé 10:30 !)",
  "« RÉJOUISSEZ-VOUS, nations, avec son peuple. » (32:43 — cité Rm 15:10 !)",
  "« PAS UNE PAROLE n'est tombée. » (Jos 23:14 — P067 : le bilan !)",
  "« Je vous RASSEMBLERAI… du BOUT DES CIEUX. » (Né 1:9 — P106 : le retour !)",
 ],
 contexte=(
  "Quatre lieux, un contrat. Sinaï (Lv 26) : le traité — bénédictions (26:3-13), sanctions "
  "graduées (26:14-39 — P048), restauration (26:40-45 — P050) ; « Bénédictions en cas "
  "d'obéissance ; malédictions en cas de désobéissance (26:1-46) » (voir ad « Lévitique », "
  "1200012675). Moab (Dt 4, 30, 31-32) : Moïse mourant — dispersion annoncée (4:25-31 — "
  "P056), retour promis (30:1-10 — P062), apostasie prévue (31:16-21 — P063), cantique "
  "déposé comme témoin (32 — P064). Sichem (Jos 23) : Josué mourant — bilan (« pas une "
  "parole tombée », 23:14 — P067) et avertissement (23:15-16 — P067). Suse (Né 1) : Néhémie "
  "PRIE Moïse — il cite Dt 30:4/4:27 : « du bout des cieux, je rassemblerai » (1:8-9 — "
  "P106). K008 a traité Lv 26:34-35, 43 (sabbats) : versets disjoints, pas de doublon."
 ),
 explication=(
  "« Sept fois » (26:18, 21, 24, 28 — P048) : la gradation ×4 — avertir, frapper, briser, "
  "disperser : chaque refus monte d'un degré. « Ciel de fer » (26:19 — P048) : sécheresse "
  "contractuelle. « Cœur incirconcis » (26:40-41 — P050) : l'orgueil comme prépuce — il "
  "« s'humiliera », alors Dieu « se souviendra » — dans l'ordre INVERSÉ : Jacob, Isaac, "
  "Abraham (26:42 — P050) : on remonte aux sources. « Bout des cieux » (Dt 30:4 ; Né 1:9 — "
  "P062, P106) : la diaspora totale — même là, la main ramasse. « Cœur circoncis » (30:6 — "
  "P062) : Dieu opère ce qu'il exige (voir Jr 31:31-34 — P062, rappel G002). Cantique-témoin "
  "(31:19, 21 — P063) : un chant qu'« on n'oubliera pas » — la mémoire chantée contre "
  "l'amnésie. Jeshurun (32:15 — P064 : « droit » — nom d'honneur devenu ironie) : gras → "
  "regimbé → abandonné. « Démons » (shedim, 32:17 — P064) : les dieux païens démasqués. "
  "« Vigne de Sodome » (32:32 — P064) : la corruption en cépage. « À moi » (32:35 — P064) : "
  "la vengeance confisquée aux hommes (Rm 12:19 ; Hé 10:30 — P064). « Nations avec son "
  "peuple » (32:43 — P064) : Rm 15:10 — les nations invitées à la joie."
 ),
 interpretation=(
  "Exécutions (registre) : P048 → 2R 17 (Samarie — voir L001) + 2R 25 (Jérusalem — voir B) + "
  "Lm 4:9-10 (la famine du siège — citée avec retenue). P050 → Esd 1:1-4 (Cyrus — voir J001) ; "
  "« je ne les rejetterai pas » (26:44 — P050). P056 → 2R 17:6, 25:21 + Né 1:8-9. P062 → Né "
  "1:8-9 + Jr 31 (nouvelle alliance — voir G002) ; la part finale (« cœur circoncis » plein) : "
  "À venir (registre) — aucune date. P063 → Jg 2:11-19 ; 3:5-7 (le cycle : apostasie, "
  "oppression, cri, juge). P064 → Rm 12:19, 15:10 ; Hé 10:30 (cités) + Ré 19:2 (À venir — "
  "voir I010) ; les malédictions « s'exécuteront à Har-Maguédôn » (voir 1951408 — avenir, "
  "aucune date). P067 → Jg 2:11-15 + 2R 17:7-23. P106 → Né 7:6 (recensés) + 8:1-18 (la Loi "
  "lue — Esdras !) : le retour CÉLÉBRÉ par la lecture."
 ),
 hist=(
  "740 (Samarie — voir L001), 607/587 (Jérusalem — voir B002) : les deux dispersions. "
  "Lm 4:9-10 (P048) : « heureux les morts par l'épée » — le siège dans l'horreur (3e personne, "
  "retenue). Cyrus (Esd 1 — voir J001) : 70 ans, le retour. 42 360 + serviteurs (Esd 2:64-65 — "
  "C8) : le retour CHIFFRÉ. Artaxerxés, XXe année (Né 1-2 — C8, Ve s. repère) : Néhémie "
  "gouverneur. Esdras lit (Né 8 — P106) : de l'aube à midi, le peuple DEBOUT — la "
  "restauration par la lecture. Juges (P063/P067) : ~300 ans de cycles (repère interne)."
 ),
 geo=(
  "Sinaï (Lv 26) : le contrat au désert. Moab (Dt) : face à Jéricho — Moïse voit sans entrer. "
  "Sichem (Jos 23) : entre Ébal et Garizim — les monts de la malédiction et de la "
  "bénédiction (Dt 27 — C8). Suse (Né 1) : Perse — la prière à 1 500 km. « Bout des cieux » "
  "(30:4 ; Né 1:9) : Halah, Babylone — et au-delà. Retour : les routes de l'est (Esd 8 — "
  "C8 : l'Ahavah !) vers Jérusalem — le lieu choisi (Né 1:9 — P106)."
 ),
 sci=(
  "Épidémiologie (26:25 — P048 : « peste au milieu de vous ») : le siège comme bouillon de "
  "culture. Agronomie (26:19-20 — P048 : ciel de fer, terre de bronze, force « en vain ») : "
  "sécheresse + épuisement — le rendement zéro. Démographie : 42 360 (Esd 2:64 — C8) + "
  "7 337 serviteurs + 200 chantres (2:65-67 — C8) : recensement du retour. Mnémonique "
  "(31:19-21 — P063) : le chant-témoin — un cantique s'oublie moins qu'une tablette : "
  "pédagogie orale. Juridique : structure suzerain-vassal (traités du Proche-Orient ancien : "
  "bénédictions/malédictions — repère) — Lv 26 en traité royal."
 ),
 limites=(
  "« Sept fois » (Lv 26) : PUNITIF, pas chronologique — aucun lien avec les « sept temps » "
  "(Dn 4 — voir F) : deux « sept », deux sens. Lm 4:9-10 : citée comme accomplissement du "
  "registre, avec retenue (3e personne). Har-Maguédôn (voir 1951408) + Ré 19:2 (P064) + cœur "
  "circoncis (P062) : parts À venir — AUCUNE date. K008 (Lv 26:34-35, 43) : même chapitre, "
  "versets disjoints — pas de doublon. C8 : Esd 2:64-67 ; 8 ; Né 2 ; Dt 27 — aucun P (vérifié)."
 ),
 accomplissement=[("Sinaï", "7 fois gradués (Lv 26:18-28)"), ("Moab", "Dispersion + retour (Dt 4 ; 30)"), ("Cantique", "Témoin déposé (Dt 31:19)"),
     ("Sichem", "Pas une parole tombée (Jos 23:14)"), ("Suse", "Bout des cieux (Né 1:9)"), ("Jérusalem", "La Loi lue (Né 8)")],
 tl=[("Sinaï", "7 fois gradués (Lv 26:18-28)"), ("Moab", "Dispersion + retour (Dt 4 ; 30)"), ("Cantique", "Témoin déposé (Dt 31:19)"),
     ("Sichem", "Pas une parole tombée (Jos 23:14)"), ("Suse", "Bout des cieux (Né 1:9)"), ("Jérusalem", "La Loi lue (Né 8)")],
 src=[("Lévitique (Livre du) — Auxiliaire (26:1-46, Moïse)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012675"),
      ("Questions de lecteurs (Lv 26/Deut, Har-Maguédôn, 1951)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1951408"),
      ("Lévitique 26 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/3/26"),
      ("Deutéronome 30 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/5/30"),
      ("Deutéronome 32 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/5/32")],
 img="images/prophe_R002_alliance.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R003", titre="Les promesses — socs, Prince, faune, pierre, serviteur, Douma",
 ref="Ésaïe 2:2-4 ; Michée 4:1-5 ; Ésaïe 9:3-7 ; 11:6-10 ; 28:14-22 ; 49:1-7 ; 21:11, 12 ; Actes 13:46, 47",
 statut="Accomplie (P145, P166, P578, P715, P136) / En cours (P108, P455) / Mixte (P120) / À venir (P124)",
 cat="R", syst="Système promesses (Sion → nations → création)",
 reg="Registre : Ésaïe/Michée/Actes — P108 (Is 2:2-4 : socs), P455 (Mi 4:1-5 : vigne et figuier), P120 (Is 9:3-7 : Prince de paix), P578 (Is 9:6-7 : trône affermi), P124 (Is 11:6-10 : faune, rameau), P145 (Is 28:14-22 : pierre éprouvée), P166 (Is 49:1-7 : lumière des nations), P715 (Ac 13:46-47 : vers les nations), P136 (Is 21:11-12 : Douma) ; rappels P556/P607 (d1), P777 (d1), P158/P612 (c2), J010 (Madian)",
 texte=[
  "« La MONTAGNE… au-dessus… TOUTES LES NATIONS en foule. » (Is 2:2 — P108 !)",
  "« Ils forgeront leurs ÉPÉES en SOCS… n'apprendront plus la GUERRE. » (2:4 — les socs !)",
  "« Chacun sous sa VIGNE et son FIGUIER, NUL ne les effraiera. » (Mi 4:4 — P455 !)",
  "« Le peuple dans les TÉNÈBRES a vu une GRANDE LUMIÈRE. » (Is 9:2 — P120 : la lumière !)",
  "« Comme au jour de MADIAN. » (9:4 — Gédéon, voir J010 !)",
  "« CONSEILLER MERVEILLEUX, DIEU FORT, PÈRE ÉTERNEL, PRINCE DE PAIX. » (9:6 — 4 titres !)",
  "« PAS DE FIN… sur le TRÔNE de David… le ZÈLE fera cela. » (9:7 — garanti !)",
  "« Le LOUP avec l'AGNEAU… le LÉOPARD avec le CHEVREAU. » (Is 11:6 — P124 !)",
  "« L'enfant sur le trou du COBRA. » (11:8 — l'enfant et le cobra !)",
  "« La terre REMPLIE de la connaissance… comme les EAUX couvrent la mer. » (11:9)",
  "« Une PIERRE ÉPROUVÉE… FONDEMENT. » (Is 28:16 — P145 : la pierre !)",
  "« Pas suffisant… je t'ai donné comme LUMIÈRE DES NATIONS. » (Is 49:6 — P166 !)",
  "« Nous nous TOURNONS vers les nations. » (Ac 13:46 — P715 : le tournant !)",
  "« GARDE, où en est la nuit ?… Le MATIN arrive, et la NUIT aussi. » (Is 21:11-12 — P136 !)",
 ],
 contexte=(
  "Neuf textes, une espérance. Is 2/Mi 4 : le MÊME oracle chez deux contemporains (Ésaïe à "
  "Jérusalem, Michée à Morésheth — voir L001) — Michée ajoute le v.4 (vigne/figuier) et le "
  "v.5 (« nous marcherons au nom de Jéhovah » — P455). Is 9 : la Galilée « traitée avec "
  "mépris » (9:1 — P120) puis honorée — Zabulon, Nephtali, « Galilée des nations ». Is 11 : "
  "le rameau de Jessé (contexte) et sa création réconciliée. Is 28 : les « vantards de "
  "Jérusalem » (voir si-1 « Isaïe », 1101990084) réfugiés dans le mensonge. Is 49 : le "
  "serviteur — « Sion consolée » (49:1—59:21 ; voir 1101990084). Ac 13 : Antioche de Pisidie — "
  "Paul se tourne. Is 21:11-12 : Douma crie depuis Séïr (voir L010 pour le chapitre)."
 ),
 explication=(
  "Montagne (2:2) : « montagne SYMBOLIQUE de Jéhovah » (voir 1101972015) — le culte élevé "
  "au-dessus des « montagnes » (royaumes). Socs (2:4) : forge INVERSE — l'ONU expose la "
  "statue (un homme forgeant une épée en soc, offerte par l'URSS — voir 1976800) : « ce "
  "n'est pas grâce à des efforts humains » (voir 1976800). Vigne/figuier (Mi 4:4 — P455) : "
  "la polyculture de paix — « nul ne les effraiera ». Madian (9:4 — P120/P578) : Gédéon, "
  "300 hommes (voir J010) — la victoire sans armée, modèle du Prince. Bottes au feu (9:5 — "
  "P120) : l'équipement militaire brûlé — démobilisation totale. Quatre titres (9:6 — "
  "P120/P578, texte vérifié) : conseiller, fort, père, prince — le gouvernement-personne. "
  "Zèle (9:7) : « c'est le zèle qui fera cela » (texte vérifié) — la garantie, pas l'homme. "
  "Faune (11:6-8 — P124) : 3 tableaux — prédateurs/proies, bétail/enfant conducteur, "
  "nourrisson/cobra : la peur abolie aux trois âges. Connaissance-mer (11:9 — P124) : "
  "l'océan comme mesure. Racine de Jessé (11:10 — P124) : « les nations chercheront » — "
  "l'étendard. Pierre (28:16 — P145) : « précieuse et éprouvée » (voir 1101990084) — posée "
  "pendant que les vantards signent « une alliance avec la Mort » (28:15 — P145). Cordeau "
  "(28:17 — P145) : le droit comme instrument. Serviteur (49:3, 6 — P166, texte vérifié) : "
  "« mon serviteur, ô Israël » PUIS « pas suffisant… lumière des nations » — "
  "l'élargissement : « son ministère terrestre s'est limité aux fils d'Israël » mais "
  "« appliqué à ses disciples » (voir 2007042, avec Ac 13:46-47 — P715). Douma (21:11 — "
  "P136 : « silence, nom prophétique d'Édom » — note vérifiée) : « matin ET nuit » (21:12) — "
  "salut et jugement ensemble ; « revenez ! » — l'appel dans la nuit."
 ),
 interpretation=(
  "Is 2/Mi 4 (En cours) : « depuis 1935 » (voir 1101972015 : article « La grande multitude ») "
  "— la grande foule « a accompli FIGURÉMENT » : socs forgés, guerre désapprise ; le final : "
  "aucune date. Is 9 : « commencé à se réaliser dans la seconde moitié de l'an 2 » (voir "
  "1101986072) — naissance (Lc 1:32-33 — P120/P578 ; Mt 1 — P578) ; alliance davidique (2S 7 — "
  "voir 1101986072 ; « dès maintenant et pour toujours », 9:7 — texte vérifié) ; plénitude : "
  "À venir (P120) — aucune date. Is 11 (À venir — P124) : AUCUNE date (voir les limites). "
  "Is 28 : posée (1P 2:6 — P777, voir D), rejetée (Ps 118:22 — P556/P607, voir D), fondement "
  "(Ép 2:20 — P145). Is 49 : Siméon (Lc 2:32 — P166 : « lumière des nations » AU TEMPLE), "
  "Antioche (Ac 13:46-48 — P715 : Juifs d'abord, nations ensuite ; « tous ceux qui étaient "
  "disposés » crurent — 13:48, P715), Rome (Ac 28:28 — P715 : « aux nations… elles "
  "écouteront ») ; aujourd'hui : « oints secondés par une grande foule » (voir 2007042). "
  "Douma : « région d'Édom ; Abdias » (P136 — voir L003)."
 ),
 hist=(
  "An 2 (seconde moitié — voir 1101986072) : naissance du Prince (voir J003 : Bethléhem). "
  "Siméon au temple (Lc 2 — P166). ~47 (Ier s. repère) : Antioche de Pisidie (Ac 13 — P715) "
  "— le tournant. ~59-61 (repère) : Rome (Ac 28 — P715). 1935 : « La grande multitude » "
  "(voir 1101972015) — l'afflux figuratif. XXe s. : statue de l'ONU (Vuchetich, URSS — voir "
  "1976800) : « jusqu'à présent elles n'ont pas converti » — la paix manquée des hommes. "
  "Gédéon (voir J010) : le jour de Madian, précédent du Prince."
 ),
 geo=(
  "Sion/Jérusalem (2:3 — P108) : la loi SORT — capitale de la parole. Galilée (9:1 — P120 : "
  "Zabulon, Nephtali, « chemin de la mer », Jourdain) : le mépris devenu honneur — Jésus "
  "Galiléen (voir C). Madian (9:4) : le torrent de Qishon (voir J010). Antioche (Pisidie — "
  "P715) → Rome (P715) : 2 500 km de lumière. « Extrémité de la terre » (Ac 13:47 — P715 ; "
  "voir 2007042). Douma (21:11 — P136) : nord de l'Arabie (repère) ; Séïr (21:11 — voir L003). "
  "Nations (11:10 ; 49:6 — P124, P166) : la géographie universelle."
 ),
 sci=(
  "Métallurgie (2:4 — P108/P455) : épées → socs, lances → serpes — la forge inverse : "
  "l'acier de guerre en acier de paix. Zoologie (11:6-8 — P124) : loup, agneau, léopard, "
  "chevreau, veau, lion, cobra — 7 espèces ; « le lion mangera de la paille » (11:7 — "
  "P124) : le régime aboli. Architecture (28:16 — P145 ; Ps 118:22 — P556) : pierre d'angle / "
  "tête de l'angle — la clé qui tient les deux murs. Optique spirituelle (9:2 ; 49:6 — "
  "P120, P166) : ténèbres → grande lumière — pas de physique (voir les limites). "
  "Agronomie (Mi 4:4 — P455) : vigne + figuier — polyculture, autarcie, paix."
 ),
 limites=(
  "Is 2/Mi 4 : 1er accomplissement FIGURÉ (voir 1101972015) — le final : AUCUNE date. Is 11 "
  "(P124, À venir) : faune littérale ou tableau ? — le texte dit, le temps montrera : NON "
  "TRANCHÉ, aucune date. Is 9:6 (« Dieu fort ») : titre du Prince — PAS de débat trinitaire "
  "(règle 7 : dogmatique interdite). Is 9:2-5 (P120) + 9:6-7 (P578) : deux P, un texte — même "
  "fiche, pas de doublon. Lumière (9:2 ; 49:6) : spirituelle — aucune physique tirée. Douma : "
  "oasis et/ou Édom symbolique (note + registre) — les deux versés."
 ),
 accomplissement=[("Ténèbres", "Galilée méprisée (9:1)"), ("Lumière", "Prince né (9:6, an 2)"), ("Pierre", "Posée, rejetée (28:16 → Ps 118)"),
     ("Tournant", "Vers les nations (Ac 13:46)"), ("1935", "L'afflux figuré (Is 2)"), ("Faune", "Loup + agneau (11:6, À venir)")],
 tl=[("Ténèbres", "Galilée méprisée (9:1)"), ("Lumière", "Prince né (9:6, an 2)"), ("Pierre", "Posée, rejetée (28:16 → Ps 118)"),
     ("Tournant", "Vers les nations (Ac 13:46)"), ("1935", "L'afflux figuré (Is 2)"), ("Faune", "Loup + agneau (11:6, À venir)")],
 src=[("Isaïe — Toute Écriture n°23 (pierre, serviteur, Sion)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990084"),
      ("Choses désirables (Is 2:2-4, 1935, socs figurés)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101972015"),
      ("Prince de paix face à Har-Maguédôn (David, an 2)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101986072"),
      ("Points marquants d'Isaïe II (49:6, disciples, extrémité)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007042"),
      ("Ésaïe 2 — Bible d'étude, texte vérifié", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/2"),
      ("Michée 4 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/33/4")],
 img="images/prophe_R003_promesses.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R004", titre="Les sept lettres — premier amour, porte ouverte, tièdes vomis",
 ref="Révélation 2:1—3:22",
 statut="1er accomplissement + En cours (P798-P812)",
 cat="R", syst="Système lettres (Ier s. → depuis 1914)",
 reg="Registre : Révélation — P798 (2:1-7 Éphèse), P799 (2:8-11 Smyrne), P800 (2:12-17 Pergame), P801 (2:18-29 Thyatire), P802 (3:1-6 Sardes), P803 (3:7-13 Philadelphie), P804 (3:14-22 Laodicée), P805 (2:5 repens-toi), P806 (2:10 couronne), P807 (2:23 reins et cœurs), P808 (3:2-3 fortifie), P809 (3:10 heure de l'épreuve), P810 (3:11 je viens vite), P811 (3:16 tiède vomi), P812 (3:19-21 discipline, porte) ; rappels I001-I010 (Ré 6+) ; Jr 17:10 (C8)",
 texte=[
  "« Tu as ABANDONNÉ ton PREMIER AMOUR… sinon j'ôterai ton PORTE-LAMPE. » (2:4-5 — P798/P805 !)",
  "« Au vainqueur : l'ARBRE DE VIE, dans le PARADIS. » (2:7 — le paradis !)",
  "« Tribulation pendant DIX JOURS… la COURONNE DE VIE. » (2:9-10 — P799/P806 !)",
  "« Là où est le TRÔNE DE SATAN… l'enseignement de BALAAM. » (2:13-14 — P800 !)",
  "« La MANNE CACHÉE… une PIERRE BLANCHE, un NOM NOUVEAU. » (2:17 — le nom !)",
  "« Tu tolères JEZABEL… je scrute les REINS ET LES CŒURS. » (2:20, 23 — P801/P807 !)",
  "« Tu as la réputation d'être VIVANT, mais tu es MORT. » (3:1 — P802 : morte-vivante !)",
  "« Ton nom ne sera pas EFFACÉ du LIVRE DE VIE. » (3:5 — le livre !)",
  "« Une PORTE OUVERTE… l'HEURE DE L'ÉPREUVE… JE VIENS VITE. » (3:8, 10, 11 — P803/P809/P810 !)",
  "« Une COLONNE dans le temple… la NOUVELLE JÉRUSALEM. » (3:12 — la colonne !)",
  "« Tu es TIÈDE… je vais te VOMIR. » (3:15-16 — P804/P811 : tiède !)",
  "« Riche… MISÉRABLE, aveugle et NU. » (3:17 — le bilan !)",
  "« Voici que je me tiens à la PORTE et je FRAPPE. » (3:19-20 — P812 : on frappe !)",
 ],
 contexte=(
  "Patmos (~96 — repère), « au jour du Seigneur » (1:10 — voir si-1 « Révélation », "
  "1101990127) : écrire « aux sept congrégations » d'Asie (1:11 — P798-P804) — Éphèse, "
  "Smyrne, Pergame, Thyatire, Sardes, Philadelphie, Laodicée. « Les sept étoiles : les anges "
  "des sept congrégations ; les sept porte-lampes : sept congrégations » (1:20 — voir "
  "1101990127). Sept = « perfection ou plénitude spirituelle » (voir 1101969037) : les sept "
  "lettres visent le Ier siècle ET « la condition des oints depuis 1914 » (registre P798). "
  "Chaque lettre : « je connais » + diagnostic + « au vainqueur ». Révélation 6+ : voir I."
 ),
 explication=(
  "Premier amour (2:4 — P798) : labeur sans flamme — « repens-toi, œuvres d'autrefois » (2:5 — "
  "P805), sinon porte-lampe ôté (2:5) : la congrégation éteinte. Dix jours (2:10 — P799/P806) : "
  "tribulation LIMITÉE — « fidèle jusqu'à la mort » = couronne. Trône de Satan (2:13 — P800) : "
  "Pergame, capitale du culte impérial (repère) — le trône païen face au trône. Balaam (2:14 — "
  "P800 : Nb 22-24, voir J006/J007) : la doctrine du piège — idolâtrie + immoralité. Pierre "
  "blanche (2:17 — P800) : bulletin d'acquittement (tribunaux antiques — repère) + nom nouveau "
  "(connu de Dieu seul). Jézabel (2:20 — P801, nom symbolique — C8 : 1R 16-21) : la corruptrice "
  "tolérée. Reins et cœurs (2:23 — P807, avec Jr 17:10 — C8) : le scrutin divin. Morte-vivante "
  "(3:1 — P802) : réputation vs réalité — « fortifie ce qui reste » (3:2 — P808 ; 1919 : "
  "affermissement — P808). Porte ouverte (3:8 — P803) : l'activité que nul ne ferme. Heure de "
  "l'épreuve (3:10 — P809) : gardé PENDANT — protection, pas exemption (grande tribulation — "
  "P809). « Je viens vite » (3:11 — P810) : tenir ferme — final À venir. Colonne (3:12 — P803) : "
  "stabilité + trois noms (Dieu, Nouvelle Jérusalem, nom nouveau). Tiède (3:15-16 — P804/P811) : "
  "ni bouillante ni froide — les eaux de Laodicée (voir géo) : vomi. Riche-misérable (3:17 — "
  "P804 : « pauvres, aveugles et nus » — voir 1101990127) : le bilan du banquier. Or/collyre/ "
  "blanc (3:18 — P804) : against la banque, la médecine, la laine (voir science). Porte (3:20 — "
  "P812) : Christ DEHORS qui frappe — la congrégation sans Christ dedans."
 ),
 interpretation=(
  "1er accomplissement : les sept du Ier siècle (registre P798-P804). Depuis 1914 : appel à "
  "la repentance (P805), fidélité jusqu'à la mort (P806), scrutin (P807), affermissement 1919 "
  "(P808 : « affermissement de l'œuvre »), protection à l'heure (P809), « tiens ferme » "
  "(P810), jugement sur la chrétienté tiède (P811 : « jugement sur la chrétienté » — "
  "registre, voir les limites), discipline des aimés (P812). Au vainqueur, sept couronnes : "
  "paradis (2:7), pas de seconde mort (2:11 — P799), manne + nom (2:17), nations + étoile "
  "(2:26-28 — P801), blanc + livre (3:5), colonne + noms (3:12), trône partagé (3:21 — P812). "
  "« Commencement de la création de Dieu » (3:14 — P804, voir 1101990127) : cité, non débattu "
  "(règle 7)."
 ),
 hist=(
  "Éphèse : Artémis, théâtre (repères) — Paul y écrivit (Ép 1 — voir 1101969037). Smyrne : "
  "fidèle sous les persécutions (Polycarpe, ~155, tradition — repère hedged). Pergame : "
  "capitale d'Asie, autel de Zeus, culte impérial (repères). Thyatire : corporations "
  "(Lydie la marchande de pourpre, Ac 16:14 — C8). Sardes : Crésus, or du Pactole (repère) — "
  "« vivante » de son passé. Philadelphie : ville frontalière, séismes (repère) — la porte "
  "tient. Laodicée : séisme 60, relevée SANS aide impériale (Tacite — repère) : « riche » "
  "(3:17) — banque, médecine (collyre), laine noire (repères). 1919 : affermissement (P808)."
 ),
 geo=(
  "Le circuit postal : Éphèse → Smyrne (N) → Pergame (N) → Thyatire (SE) → Sardes (S) → "
  "Philadelphie (SE) → Laodicée (S) — ~500 km en boucle (repère) : l'ordre des lettres = "
  "l'ordre de la route ! Patmos : l'île de l'exil (à l'ouest). Laodicée : vallée du Lycus — "
  "Hiérapolis (eaux CHAUDES) + Colosses (eaux FROIDES) voisines : Laodicée reçoit du TIÈDE "
  "par aqueduc (repère) — 3:15-16 en hydrologie ! Philadelphie (« amour fraternel ») : "
  "la porte de la Phrygie."
 ),
 sci=(
  "Hydrologie (3:15-16 — P804/P811) : aqueduc calcaire de Laodicée — l'eau arrive tiède et "
  "chargée : à vomir — littéralement. Médecine (3:18 — P804 : « collyre ») : école de "
  "médecine de Laodicée (collyre phrygien — repère) — Christ prescrit SON collyre. Textile "
  "(3:18 : « vêtements blancs ») : Laodicée = laine NOIRE célèbre (repère) — le blanc offert "
  "contre le noir vendu. Métallurgie (3:18 : « or épuré par le feu ») : ville de BANQUE "
  "(repère) — l'or du ciel contre l'or du coffre. Numérique : 7 lettres, 7 sceaux, 7 "
  "trompettes — totalité (voir 1101969037). Juridique : pierre blanche (2:17) = acquittement "
  "(repère)."
 ),
 limites=(
  "Dix jours (2:10) : durée BRÈVE et limitée — aucun calcul. Trône de Satan (2:13) : culte "
  "impérial de Pergame (repère proposé, hedged) — le texte ne détaille pas. « Commencement "
  "de la création » (3:14) : CITÉ (voir 1101990127), non débattu — règle 7 (dogmatique "
  "interdite). P811 (chrétienté) : formule DU REGISTRE (« jugement sur la chrétienté ») — "
  "preuve versée, pas d'attaque (règle 7). « Je viens vite » (P810) : final À venir — AUCUNE "
  "date. Ré 6+ : voir I (I001-I010). C8 : Ac 16:14, 19 ; 1R 16-21 (Jézabel) ; Jr 17:10 — "
  "aucun P (vérifié)."
 ),
 accomplissement=[("Patmos (~96)", "Jour du Seigneur (1:10)"), ("Circuit", "7 villes en boucle"), ("Ier s.", "7 lettres lues"),
     ("1914+", "Oints éprouvés (P805-P812)"), ("1919", "Affermissement (P808)"), ("Heure", "Gardés pendant (3:10)")],
 tl=[("Patmos (~96)", "Jour du Seigneur (1:10)"), ("Circuit", "7 villes en boucle"), ("Ier s.", "7 lettres lues"),
     ("1914+", "Oints éprouvés (P805-P812)"), ("1919", "Affermissement (P808)"), ("Heure", "Gardés pendant (3:10)")],
 src=[("Révélation — Toute Écriture n°66 (7 messages, porte-lampes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990127"),
      ("144 000 marqués du sceau (7 = totalité, 7 porte-lampes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101969037"),
      ("Révélation 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/2"),
      ("Révélation 3 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/3")],
 img="images/prophe_R004_eglises.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R005", titre="Le trône et l'Agneau — vingt-quatre anciens, sept sceaux",
 ref="Révélation 4:1—5:14",
 statut="Accomplie (P816, P817) / En cours (P813, P814, P815, P818) / À venir (P819)",
 cat="R", syst="Système trône (33 → 1914 → soumission)",
 reg="Registre : Révélation — P813 (4:1 : monte ici), P814 (4:4 : 24 anciens), P815 (4:6-8 : 4 créatures, saint), P816 (4:11 : tu es digne, création), P817 (5:2-5 : qui est digne, Lion), P818 (5:9-10 : achetés, royaume et prêtres), P819 (5:13 : toute créature loue) ; rappels J005 (Gn 49:9-10), I (sceaux) ; Ré 4:2-3, 5:11-12 (C8)",
 texte=[
  "« MONTE ICI : je te montrerai les choses qui doivent ARRIVER. » (4:1 — P813 : monte !)",
  "« VINGT-QUATRE anciens… VÊTEMENTS BLANCS… COURONNES D'OR. » (4:4 — P814 !)",
  "« Une MER DE VERRE… QUATRE créatures PLEINES D'YEUX. » (4:6 — P815 : la mer !)",
  "« SAINT, SAINT, SAINT est Jéhovah… jour et nuit. » (4:8 — P815 : ×3 !)",
  "« TU ES DIGNE… car tu as CRÉÉ toutes choses. » (4:11 — P816 : le créateur !)",
  "« QUI EST DIGNE d'ouvrir le rouleau ?… Et je PLEURAIS beaucoup. » (5:2, 4 — P817 : qui ?)",
  "« NE PLEURE PLUS… Le LION de Juda… a VAINCU. » (5:5 — le Lion !)",
  "« Un AGNEAU comme TUÉ… SEPT cornes, SEPT yeux. » (5:6 — l'Agneau !)",
  "« HARPE… BOLS D'OR… les PRIÈRES des saints. » (5:8 — l'encens !)",
  "« Tu as ACHETÉ… ROYAUME et PRÊTRES. » (5:9-10 — P818 : achetés !)",
  "« TOUTE créature… a LOUÉ l'Agneau. » (5:13 — P819 : toutes !)",
 ],
 contexte=(
  "Porte ouverte DANS LE CIEL (4:1 — P813) : Jean monte — « les choses qui doivent arriver » "
  "depuis 1914 (« visions du jour du Seigneur » — P813). Salle du trône : Celui qui siège "
  "(4:2 — C8 : jaspe, sardoine, arc-en-ciel émeraude — 4:3, C8), 24 trônes (4:4 — P814), mer "
  "de verre (4:6 — P815), 4 créatures (4:6-8 — P815 : lion, taureau, homme, aigle — 4:7, "
  "P815). Puis le ROULEAU : « écrit en dedans et sur le revers, scellé de sept sceaux » "
  "(5:1 — C8, texte vérifié) — cuir, parchemin ou papyrus (voir it-1 « Rouleau », "
  "1200003862) ; « personne ni dans le ciel, ni sur la terre, ni sous la terre » (5:3 — "
  "P817, texte vérifié). Les sceaux (ch.6+) : voir I."
 ),
 explication=(
  "« Monte ici » (4:1 — P813) : changement de scène — de la terre (ch.2-3, voir R004) au "
  "ciel. 24 (4:4 — P814) : 12 + 12 — la plénitude du peuple (tribus + apôtres) ; « rôle "
  "attribué aux 144 000 dans l'administration céleste » (P814) ; blanc (pureté) + or "
  "(royauté). Mer de verre (4:6 — P815) : le chaos aplani — transparence, stabilité. "
  "4 créatures (4:7 — P815) : lion (courage), taureau (force), homme (intelligence), aigle "
  "(perspicacité) — les 4 faces du pouvoir (voir Éz 1 — C8) ; « pleines d'yeux » (4:6, 8 — "
  "P815) : vigilance totale. « Saint ×3 » (4:8 — P815 ; Is 6:3 — C8) : la sainteté au "
  "superlatif — « jour et nuit », sans relâche. « Tu as créé » (4:11 — P816) : le motif de "
  "la gloire — la création (voir K003). Pleurs (5:4 — P817, texte vérifié : « je pleurais "
  "beaucoup ») : l'enjeu — sans ouvreur, pas d'avenir. Lion PUIS Agneau (5:5-6 — P817) : "
  "« ne pleure plus » — le vainqueur EST la victime : « la racine de David » (5:5 — P817 ; "
  "Gn 49:9-10 — P817, voir J005). 7 cornes/yeux (5:6 — P817, texte vérifié) : « les sept "
  "esprits envoyés par toute la terre » — pouvoir et vision pléniers. Harpes + encens (5:8 — "
  "P817, texte vérifié) : musique + « prières des saints » — le culte répond. « Acheté » "
  "(5:9 — P818 : agorazô — du marché !) : « toute tribu, langue, peuple, nation » — "
  "« royaume et prêtres » (5:10 — P818 ; « 144 000 rachetés ; depuis 33 et actuellement » — "
  "P818 ; voir 1101969037). Myriades (5:11-12 — C8 : « des myriades de myriades ») : "
  "l'acclamation chiffrée. Toutes (5:13 — P819) : cieux + terre + sous-terre + mer — 4 zones, "
  "zéro exception (Ph 2:10 — C8)."
 ),
 interpretation=(
  "« Jésus reçoit le droit d'ouvrir le rouleau : 1914 » (P817) : le Lion prend (5:7 — P817, "
  "texte vérifié : « il s'avança et prit »). Depuis 1914 : visions (P813), louange céleste "
  "(P815), anciens en fonction (P814). Depuis 33 : le rachat en cours (P818 : « depuis 33 de "
  "n. è. et actuellement » — Pentecôte, voir R003/P108) — 144 000 « royaume et prêtres » "
  "(voir 1101969037). Le rouleau ouvert plus tard (ch.10 — voir it-Rouleau : doux puis amer ; "
  "Éz 2-3 — C8 : « chants funèbres ») : comprendre coûte. Soumission universelle (P819, À venir "
  "— « lors de la soumission universelle ») : AUCUNE date. Création (4:11 — P816, Accomplie) : "
  "« tu as créé » — le passé fonde l'avenir (voir K : science)."
 ),
 hist=(
  "33 (Pentecôte — P818 : « depuis 33 » ; Ac 2 — voir R003) : le rachat commence. 1914 : le "
  "droit de régner reçu (P817 ; voir E/F — non rediscuté). « Actuellement » (P818) : le "
  "rassemblement continue. Patmos ~96 (repère) : la vision écrite (voir R004). Rouleaux "
  "antiques : cuir, parchemin, papyrus (voir 1200003862) — le livre avant le livre. Sceaux "
  "(7) : cachets d'argile/cire (repère) — inviolabilité graduée. Harpes du temple "
  "(repère) : kinnôr — voir L005 (Tyr) et L010 (Ps 137)."
 ),
 geo=(
  "Le ciel : salle du trône — cosmographie de la vision (trône central, 24 autour, 4 "
  "milieu, myriades dehors — 3 cercles !). Patmos → ciel (4:1 — P813) : la montée. « Toute "
  "tribu, langue, peuple, nation » (5:9 — P818) : les 4 cercles de l'humanité. « Cieux, "
  "terre, sous-terre, mer » (5:13 — P819) : les 4 zones du cosmos — sous la terre : le "
  "séjour des morts (voir L010 : la Tombe). Nouvelle Jérusalem (voir R004, 3:12 — P803) : "
  "la ville du rouleau ouvert (voir I)."
 ),
 sci=(
  "Codicologie (voir 1200003862) : rouleau écrit « en dedans et sur le revers » (5:1 — C8, "
  "texte vérifié) — saturation : plus de place, tout est dit ; 7 sceaux — fermeture "
  "progressive. Gemmologie (4:3 — C8) : jaspe (translucide), sardoine (rouge), émeraude "
  "(arc-en-ciel) — le trône en pierres. Optique (4:3 — C8 : arc-en-ciel ; 4:5 — C8 : "
  "« éclairs, voix, tonnerres ») : la théophanie en lumière et son. Zoologie symbolique "
  "(4:7 — P815) : 4 animaux-cardinaux. Acoustique (5:11-12 — C8 : myriades « d'une voix "
  "forte ») : le chœur chiffré. Arithmétique : 7 (plénitude), 24 (12+12), 4 (universalité)."
 ),
 limites=(
  "Is 6:3 (« saint ×3 », séraphins) : C8 — aucun P (vérifié). 4:2-3 (gemmes, arc-en-ciel), "
  "4:5 (éclairs), 5:1 (rouleau), 5:11-12 (myriades) : C8 — décrits, non sur-interprétés. Éz 1 "
  "(4 créatures) : C8 — parallèle signalé, non développé. P819 (soumission) : À venir — "
  "AUCUNE date. 1914/33 : registre (voir E/F) — non rediscutés. Sceaux (ch.6+) : voir I "
  "(I001-I004, I008)."
 ),
 accomplissement=[("Patmos (~96)", "Porte ouverte (4:1)"), ("Trône", "24 + 4 + mer (4:4-8)"), ("Digne", "Créateur (4:11)"),
     ("Pleurs", "Personne (5:3-4)"), ("1914", "Lion prend (5:5-7)"), ("Toutes", "Louange universelle (5:13, À venir)")],
 tl=[("Patmos (~96)", "Porte ouverte (4:1)"), ("Trône", "24 + 4 + mer (4:4-8)"), ("Digne", "Créateur (4:11)"),
     ("Pleurs", "Personne (5:3-4)"), ("1914", "Lion prend (5:5-7)"), ("Toutes", "Louange universelle (5:13, À venir)")],
 src=[("Rouleau — Étude perspicace (7 sceaux, doux-amer, Ézéchiel)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003862"),
      ("144 000 marqués du sceau (royaume et prêtres, réutilisé)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101969037"),
      ("Révélation 4 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/4"),
      ("Révélation 5 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/5")],
 img="images/prophe_R005_trone.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="R006", titre="L'aller et le retour — Osée renvoie, Zacharie ramène",
 ref="Osée 8:1-14 ; Osée 9:3 (C8) ; Zacharie 10:1-12",
 statut="Accomplie (P417) / 1er accomplissement (P505)",
 cat="R", syst="Système allers-retours (Égypte ↔ Assyrie)",
 reg="Registre : Osée/Zacharie — P417 (Os 8:1-14 : retour en Égypte, Assyrie), P505 (Za 10:1-12 : pluie, rassemblés d'Égypte et d'Assyrie) ; rappels J002 (Béthel), L001 (2R 17:6), L009 (Nil) ; Os 9:3, 2R 15, Dt 11:14 (C8)",
 texte=[
  "« Un AIGLE sur la maison de Jéhovah ! » (Os 8:1 — P417 : le vautour !)",
  "« Israël a REJETÉ le bien… l'ennemi le POURSUIVRA. » (8:3 — rejeté !)",
  "« Des ROIS SANS MOI… des princes À MON INSU. » (8:4 — sans moi !)",
  "« Ton VEAU, Samarie… en PIÈCES ! » (8:5-6 — le veau !)",
  "« Ils ont semé du VENT… moissonneront la TEMPÊTE. » (8:7 — vent-tempête !)",
  "« Éphraïm… ÂNON SAUVAGE, solitaire. » (8:9 — l'onagre !)",
  "« Ils RETOURNERONT EN ÉGYPTE. » (8:13 — P417 : l'aller !)",
  "« Éphraïm retournera en Égypte… en ASSYRIE, l'IMPUR. » (Os 9:3 — C8 : double !)",
  "« DEMANDEZ la pluie… les NUÉES D'ORAGE. » (Za 10:1 — P505 : la pluie !)",
  "« De lui la PIERRE D'ANGLE… le CLOU… l'ARC. » (10:4 — 3 titres !)",
  "« Je les SIFFLERAI… je les RACHÈTERAI. » (10:8 — le sifflet !)",
  "« Je les ai SEMÉS parmi les peuples… ils REVIENDRONT. » (10:9 — semis !)",
  "« D'ÉGYPTE… d'ASSYRIE… PAS DE PLACE. » (10:10 — le retour !)",
  "« La MER avec détresse… le NIL à sec… le SCEPTRE ôté. » (10:11 — nouvel Exode !)",
 ],
 contexte=(
  "Osée (~750, Jéroboam II — contemporain d'Isaïe, Amos, Michée) : marié à Gomer "
  "(« épouse de fornication » — voir it-1 « Osée », 1200012037), père de Jizréel, Lo-Ruhamah "
  "(« pas de miséricorde »), Lo-Ammi (« pas mon peuple » — voir 1200012037) — sa famille "
  "EST le sermon. Ch.8 : le procès — veau (voir 1200012037 : « culte des Baals et du veau »), "
  "rois illégitimes, alliances païennes. Zacharie (~520, Darius II — après l'exil, second "
  "temple en chantier — voir B005) : ch.10 — la pluie demandée, les bergers jugés (10:3 — "
  "P505), le rassemblement chanté (10:8-12 — texte vérifié). Deux sens, mêmes pays : Osée "
  "RENVOIE en Égypte (8:13), Zacharie EN RAMÈNE (10:10) — l'aller et le retour."
 ),
 explication=(
  "Aigle (8:1 — P417 : vautour/aigle fondant) : l'Assyrie fond sur la maison. « Sans moi » "
  "(8:4 — P417) : Zacharie, Shallum, Menahem, Péqah… (2R 15 — C8 : 4 assassinats en 15 ans) — "
  "des rois que Dieu n'a pas oints. Veau (8:5-6 — P417) : Béthel (voir J002) — « en pièces » : "
  "le veau débité. Vent-tempête (8:7 — P417) : le proverbe climatique — semailles vaines, "
  "moisson violente. Ânon (8:9 — P417 : onagre, « solitaire ») : Éphraïm paie ses amants "
  "(Assyrie + Égypte — 12:1, C8) au lieu d'être payé. Autels multipliés (8:11 — P417) : "
  "« pour pécher » — plus d'autels, plus de péché. Loi étrangère (8:12 — P417) : « regardée "
  "comme chose étrange » — la Loi devenue exotique. Pluie (Za 10:1 — P505 : « au temps de la "
  "pluie de l'arrière-saison », nuées d'orage — voir 1101972027) : demander à Jéhovah, pas "
  "aux théraphim (10:2 — P505 : idoles domestiques menteuses, devins, songes vains). Pierre/"
  "clou/arc (10:4 — P505) : de Juda — fondement, stabilité, guerre : le chef complet. Sifflet "
  "(10:8 — P505, texte vérifié : « je les sifflerai et les rassemblerai ») : le berger "
  "siffle — « pas d'obstacle insurmontable » (voir 1101972027). Semis (10:9 — P505) : « je "
  "les ai semés » — la dispersion SEMÉE (elle lèvera !) ; « ils se souviendront… reprendront "
  "vie… reviendront ». Pas de place (10:10 — P505, texte vérifié : Galaad + Liban PLEINS) : "
  "le retour déborde. Mer/Nil (10:11 — P505, texte vérifié) : « passer la mer avec détresse… "
  "Nil desséché… orgueil abaissé… sceptre ôté » — nouvel Exode (voir 1101972027 : « comme la "
  "mer Rouge » ; L009 pour le Nil)."
 ),
 interpretation=(
  "Os 8:13 → 2R 17:6 (P417 — voir L001 : Halah, Habor, Mèdes) ; Os 9:3 (C8, texte vérifié : "
  "« retournera en Égypte… en Assyrie, l'impur ») : le double exil — Égypte (fuite) + "
  "Assyrie (déportation) ; « rassemblerai la captivité » (formule du registre P417 — voir "
  "les limites). Za 10 (1er accomplissement — P505 : 10:6-10) : le retour de l'exil "
  "(Esd 1 — voir J001 ; B005) — Galaad et Liban repeuplés ; obstacles : mer, vagues, Nil, "
  "orgueil, sceptre (10:11 — voir 1101972027 : Dieu « abattrait les vagues ») ; « supérieurs "
  "en Jéhovah » (10:12 — P505). Chiasme : Égypte jugée (Os 8) → Égypte vidée (Za 10) ; "
  "Assyrie bourreau (Os 8) → Assyrie abaissée (Za 10:11)."
 ),
 hist=(
  "Coups d'État (2R 15 — C8 : Zacharie 6 mois, Shallum 1 mois, Menahem tributaire, Péqah, "
  "Osée) : « des rois sans moi » (8:4) en actes. Téglath-Phalazar (2R 15:29 — voir A010/L001), "
  "Salmanasar/Sargon (2R 17 — voir L001) : l'aigle (8:1) fond. Osée/Égypte (2R 17:4 — C8 : "
  "Sô) : l'ânon paie (8:9). Retour (Esd 1-2 — voir J001/B005 ; Né — voir R002) : « pas de "
  "place » (10:10) — 42 360 (voir R002). Pluies : premières (oct-nov) et dernières (mars-avr) "
  "(Dt 11:14 — C8) — 10:1 demande les dernières."
 ),
 geo=(
  "Samarie (8:5-6 — P417 : le veau — voir J002/L001). Égypte (8:13 ; 9:3 — aller ; 10:10-11 — "
  "retour + Nil à sec !). Assyrie (9:3 ; 10:10-11 — déportation ; orgueil abaissé). Galaad "
  "(est du Jourdain) + Liban (nord) — 10:10 : l'extension du retour — PLEINS. Mer (10:11 — "
  "« avec détresse » : la Rouge ? — voir 1101972027). Routes : Galaad-Égypte (caravanes — "
  "voir R001 !), Assyrie-Samarie (déportation — voir L001)."
 ),
 sci=(
  "Ornithologie (8:1 — P417) : aigle/vautour — le charognard fondant : l'Assyrie en "
  "prédateur. Agronomie (8:7 — P417 : vent → tempête ; 10:9 — P505 : dispersion-semis ; "
  "10:1 — P505 : pluie d'arrière-saison) : 3 proverbes climatiques. Zoologie (8:9 — P417 : "
  "onagre solitaire) : l'âne sauvage indomptable — Éphraïm. Hydrologie (10:11 — P505 : Nil "
  "« profondeurs desséchées ») : voir L009 — le fleuve à sec, deuxième fois. Démographie "
  "(10:10 — P505 : « pas de place ») : le retour-surpopulation. Toreutique (8:4 — P417 : "
  "« de leur argent et de leur or ils se sont fait des idoles ») : le métal précieux en "
  "veau."
 ),
 limites=(
  "Os 9:3 : C8 (hors P417, ch.8 seul) — texte vérifié, versé comme C8. 2R 15 (coups d'État), "
  "2R 17:4 (Sô), Dt 11:14 (pluies), Os 12:1 (huile en Égypte) : C8 — aucun P (vérifié). "
  "« Rassemblerai la captivité » (P417) : formule DU REGISTRE — le verset-source (Os 6:11 ?) "
  "non développé : registre = vérité (règle 13). Za 10 : « 1er accomplissement » (P505) — la "
  "suite : avenir, AUCUNE date. it-Osée (Gomer, ch.1-3) : contexte DU LIVRE — le P417 est au "
  "ch.8 : signalé, pas confondu."
 ),
 accomplissement=[("Gomer", "Famille-sermon (Os 1-3, contexte)"), ("Veau", "Béthel en pièces (8:5-6)"), ("Vent", "Tempête (8:7 → 2R 17:6)"),
     ("Aller", "En Égypte ! (8:13)"), ("Pluie", "Demandez ! (Za 10:1)"), ("Retour", "Pas de place (10:10)")],
 tl=[("Gomer", "Famille-sermon (Os 1-3, contexte)"), ("Veau", "Béthel en pièces (8:5-6)"), ("Vent", "Tempête (8:7 → 2R 17:6)"),
     ("Aller", "En Égypte ! (8:13)"), ("Pluie", "Demandez ! (Za 10:1)"), ("Retour", "Pas de place (10:10)")],
 src=[("Osée (Livre d') — Étude perspicace (Gomer, veau, Baals)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012037"),
      ("Obstacles surmontés (Za 10:8-12, mer, Nil)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101972027"),
      ("Osée 8 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/28/8"),
      ("Zacharie 10 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/10")],
 img="images/prophe_R006_allerretour.jpg",
))
