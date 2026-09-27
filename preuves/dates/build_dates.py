#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAGUE 7 — Les fiches de dates.

Ecrit : preuves/FICHES_DATES.html   (8 fiches A4 detachable + garde + chaine complete)

Regles de fabrication :
  - une date par fiche, un seul systeme chronologique par document ;
  - le calcul est ecrit ligne par ligne, jamais sous-entendu ;
  - chaque fiche porte une limite honnete : ce qu'elle ne dit pas ;
  - aucune date pour l'avenir ;
  - sources : wol.jw.org / www.jw.org uniquement ;
  - aucune ressource distante, tout est inline.
"""

import os, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# LES HUIT FICHES
# ---------------------------------------------------------------------------
F = []

F.append(dict(
 n=1, date="607", ere="avant notre ère", sys="Système biblique",
 titre="Jérusalem dévastée — le début des 70 ans",
 prop_ref="Jérémie 25:11, 12 · Jérémie 29:10 · 2 Chroniques 36:21 · Daniel 9:2",
 prop_txt="« Tout ce pays deviendra une ruine, un désert, et ces nations seront asservies au "
          "roi de Babylone pendant soixante-dix ans. » — la désolation durera « jusqu'à "
          "l'accomplissement de soixante et dix ans ».",
 calcul=[("Point d'arrivée", "Le décret de Cyrus a pris effet et les exilés sont de retour "
          "à Jérusalem avant le 7ᵉ mois (Tishri) — Esdras 3:1", "automne 537"),
         ("Durée annoncée", "soixante-dix ans, pris au sens littéral par Daniel lui-même "
          "(« le nombre des années », Daniel 9:2)", "70 ans"),
         ("Soustraction", "automne 537 − 70 ans", "automne 607"),
         ("Confirmation biblique", "Jérusalem tombe le 9 Tammouz ; le 10 Ab, Nébuzaradan entre "
          "et détruit la ville et le temple — 2 Rois 25:8, 9", "607")],
 accom_ref="2 Rois 25:1-26 · 2 Chroniques 36:17-21 · Jérémie 52",
 accom_txt="La ville est prise, le temple brûlé, les murailles abattues, le roi emmené à Babylone. "
           "Le pays reste désolé soixante-dix ans : contrairement aux Assyriens, le roi de Babylone "
           "n'installe pas d'autres peuples pour remplacer les Juifs.",
 doc="<b>VAT 4956.</b> Cette tablette astronomique babylonienne est le document profane le plus "
     "discuté du dossier. Lue en plaçant la 37ᵉ année de Nabuchodonosor II en 588, elle renvoie "
     "sa 18ᵉ année à 607 — l'année de la destruction selon la chronologie biblique. "
     "<b>Josèphe</b> écrit de son côté : « la Judée, Jérusalem et le Temple demeurèrent déserts "
     "durant soixante-dix ans » (<i>Histoire ancienne des Juifs</i>, livre X, chap. XI, § 9).",
 limite="La majorité des historiens profanes retient 587. La date de 607 repose sur le témoignage "
        "unanime de Jérémie, de Zacharie, de Daniel et du rédacteur des Chroniques : soixante-dix "
        "ans littéraux. L'autre lecture de la tablette VAT 4956 (37ᵉ année en 568) donne 587. "
        "Cette fiche suit le système biblique.",
 src=[("Quand l’ancienne Jérusalem a-t-elle été détruite ? (1 et 2)",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
      ("Quand l’ancienne Jérusalem a-t-elle été détruite ? (2)",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/2011810"),
      ("Quand Jérusalem a-t-elle été dévastée par Babylone ?",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/101972329"),
      ("Jérusalem (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012382")],
 img="images/date_01_607.jpg"))

F.append(dict(
 n=2, date="539", ere="avant notre ère", sys="Date neutre",
 titre="Babylone tombe — le fleuve et les portes",
 prop_ref="Isaïe 44:27, 28 · Isaïe 45:1, 2 · Jérémie 50:38 · Jérémie 51:36, 37 · Daniel 5",
 prop_txt="Cyrus est nommé par son nom plus d'un siècle à l'avance. Devant lui, « les fleuves "
          "seront mis à sec », « les portes ne seront pas fermées », et Babylone « ne sera plus "
          "habitée ».",
 calcul=[("Date profane", "La Chronique de Nabonide situe l'entrée des troupes de Gubaru à "
          "Babylone le 16 Tashritu", "11/12 octobre 539"),
         ("Accord général", "Cette date est admise par toutes les chronologies, profanes "
          "comme bibliques : aucune école ne la conteste", "539"),
         ("Conséquence", "Le décret de libération n'est pas encore publié : il faut d'abord "
          "que le pouvoir perse s'installe", "voir fiche 3")],
 accom_ref="Daniel 5:1-31 · Esdras 1:1, 2 · 2 Chroniques 36:22, 23",
 accom_txt="La nuit où Belshatsar fait servir le vin dans les coupes du temple, une main écrit "
           "sur la muraille : MENÉ MENÉ TEQEL OUPHARSÎN. Daniel lit le jugement. La ville est "
           "prise dans la nuit ; le roi est tué.",
 doc="<b>Le cylindre de Cyrus</b> et <b>la Chronique de Nabonide</b> conservent le récit perse et "
     "babylonien de la prise de la ville. Le détournement de l'Euphrate et l'entrée par le lit du "
     "fleuve correspondent au texte d'Isaïe et de Jérémie sur le fleuve mis à sec.",
 limite="Cette date est neutre : elle n'engage aucun système chronologique et ne préjuge en rien "
        "de 607. Elle sert de pivot commun entre l'histoire profane et le récit biblique.",
 src=[("Quand Jérusalem a-t-elle été dévastée par Babylone ?",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/101972329"),
      ("Une date pivot de l’Histoire — 537", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
      ("La Bible et l’Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/date_02_539.jpg"))

F.append(dict(
 n=3, date="537", ere="avant notre ère", sys="Système biblique",
 titre="Le retour d'exil — la fin des 70 ans",
 prop_ref="Jérémie 29:10 · 2 Chroniques 36:22, 23 · Esdras 1:1-4 · Esdras 3:1",
 prop_txt="« Quand soixante-dix ans seront révolus à Babylone, je vous visiterai et j'accomplirai "
          "ma bonne parole à votre égard, en vous ramenant vers ce lieu-ci. »",
 calcul=[("1ʳᵉ année de Cyrus", "D'après la tablette « Strassmaier, Cyrus n° 11 », elle va du "
          "17/18 mars 538 au 4/5 mars 537", "538-537"),
         ("Date du décret", "Publié avant le 5/6 mars 537, donc à la fin de l'hiver ou au début "
          "du printemps 537 — Esdras 1:1", "début 537"),
         ("Arrivée à Jérusalem", "Les exilés arrivent juste avant le 7ᵉ mois (Tishri), "
          "Esdras 2:70 ; 3:1", "automne 537"),
         ("Fin des 70 ans", "Tishri 537 − Tishri 607", "70 ans accomplis")],
 accom_ref="Esdras 1:1-3:6 · 2 Chroniques 36:22, 23",
 accom_txt="L'autel est relevé à son emplacement au 7ᵉ mois de 537, malgré la crainte des peuples "
           "voisins ; les fondations du second temple sont posées l'année suivante. La désolation "
           "de soixante-dix ans prend fin parce que le pays est de nouveau occupé, non parce "
           "qu'un décret est signé.",
 doc="<b>La tablette « Strassmaier, Cyrus n° 11 »</b> fixe le cadre de la première année de Cyrus. "
     "L'histoire profane admet, pour l'essentiel, le retour des exilés en 537.",
 limite="La date exacte du décret est déduite de la tablette cunéiforme ; seul le retour effectif "
        "à Jérusalem est daté par le texte biblique. C'est l'arrivée, et non la signature, qui met "
        "fin aux soixante-dix ans.",
 src=[("Une date pivot de l’Histoire — 537", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
      ("Quand l’ancienne Jérusalem a-t-elle été détruite ? (1)",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
      ("Temple (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200014259")],
 img="images/date_03_537.jpg"))

F.append(dict(
 n=4, date="455", ere="avant notre ère", sys="Système biblique",
 titre="L'ordre de rebâtir — le départ des 70 semaines",
 prop_ref="Daniel 9:24, 25 · Néhémie 2:1-8",
 prop_txt="« Depuis la sortie de la parole de rétablir et de rebâtir Jérusalem jusqu'à Messie le "
          "Conducteur, il y aura sept semaines, et soixante-deux semaines. »",
 calcul=[("Avènement d'Artaxerxès Iᵉʳ", "Thémistocle arrive en Asie en 473 alors "
          "qu'Artaxerxès « régnait depuis peu » → le règne commence en 474", "474"),
         ("20ᵉ année du règne", "474 − 19", "455"),
         ("Nisan 455", "Néhémie, échanson, obtient du roi l'autorisation de rebâtir "
          "— Néhémie 2:1-8", "Nisan 455"),
         ("Prise d'effet", "L'ordre entre en vigueur au retour de Néhémie à Jérusalem, "
          "vers le 3/4 Ab (26/27-27/28 juillet)", "455"),
         ("Contrôle interne", "La muraille est achevée le 25 Élul (17 septembre) après "
          "52 jours de travail — Néhémie 6:15", "52 jours"),
         ("Durée annoncée", "7 semaines + 62 semaines = 69 semaines = 69 × 7", "483 ans"),
         ("Résultat", "455 avant notre ère + 483 ans", "29 de notre ère")],
 accom_ref="Néhémie 2:9-18 · Néhémie 6:15 · Esdras 7",
 accom_txt="La parole sort de Suse, mais elle ne prend effet qu'à Jérusalem : le même principe "
           "avait déjà valu pour le décret de Cyrus, qui mit fin aux soixante-dix ans lorsqu'il "
           "fut appliqué, non lorsqu'il fut signé.",
 doc="<b>Le règne d'Artaxerxès Iᵉʳ.</b> L'ouvrage <i>Christologie des Alten Testaments</i> "
     "(Hengstenberg) retient 474 pour le début du règne et conclut : « La vingtième année "
     "d'Artaxerxès est l'année 455 avant Christ. » La vingtième année va de Tishri 456 à "
     "Tishri 455 selon le comput de Néhémie.",
 limite="Certains ouvrages retiennent 445 pour la 20ᵉ année d'Artaxerxès. La Bibliothèque en "
        "ligne expose les raisons du choix de 455 dans les articles chronologiques cités ci-dessous. "
        "On ne mélange pas les deux systèmes dans un même document.",
 src=[("Soixante-dix semaines", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013825"),
      ("Le moment de la venue du Messie est révélé", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999030"),
      ("Un moyen infaillible de reconnaître le Messie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965762"),
      ("Chronologie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010959")],
 img="images/date_04_455.jpg"))

F.append(dict(
 n=5, date="29", ere="de notre ère", sys="Système biblique",
 titre="Le Messie paraît — au bout des 69 semaines",
 prop_ref="Daniel 9:25 · Luc 3:1, 21-23 · Actes 10:38",
 prop_txt="« Messie le Conducteur » apparaîtra au terme de soixante-neuf semaines d'années, "
          "soit 483 ans après la sortie de la parole.",
 calcul=[("Point de départ", "La parole de rebâtir Jérusalem entre en vigueur", "455 av. n. è."),
         ("Durée annoncée", "7 + 62 = 69 semaines d'années = 69 × 7", "483 ans"),
         ("Addition", "455 avant notre ère + 483 ans", "29 de notre ère"),
         ("Repère profane", "La 15ᵉ année de Tibère César — Tibère règne à partir "
          "du 17 août 14 de notre ère", "15ᵉ année = 29"),
         ("Ordre interne", "Jean commence à prêcher en 29 ; six mois plus tard il baptise Jésus",
          "automne 29")],
 accom_ref="Luc 3:1-3, 21-23 · Marc 1:9-11 · Jean 1:29-34",
 accom_txt="Jésus, âgé d'environ trente ans, vient se faire baptiser dans le Jourdain. Il est oint "
           "d'esprit saint : il devient le Christ, l'Oint, Messie le Conducteur. Le grand temple "
           "spirituel de Dieu commence à fonctionner.",
 doc="<b>Luc 3:1-3</b> date le début du ministère de Jean de la quinzième année de Tibère César, "
     "un repère profane solide puisque la mort d'Auguste (17 août 14) est elle-même datée par "
     "l'histoire romaine.",
 limite="La Bible ne donne ni le jour ni l'heure du baptême ; elle donne une année, et Luc la "
        "double d'un repère profane. « Environ trente ans » (Luc 3:23) reste une approximation "
        "assumée, pas une précision.",
 src=[("Le grand temple spirituel de Jéhovah", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996483"),
      ("Chronologie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010959"),
      ("Le moment de la venue du Messie est révélé", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999030")],
 img="images/date_05_29.jpg"))

F.append(dict(
 n=6, date="33", ere="de notre ère", sys="Système biblique",
 titre="Le Messie retranché — à la moitié de la semaine",
 prop_ref="Daniel 9:24-27 · Matthieu 26:2 · Jean 1:29 · Hébreux 10:5-10",
 prop_txt="« À la moitié de la semaine, il fera cesser sacrifice et offrande » ; le Messie est "
          "« retranché », et la prophétie annonce « une propitiation pour la faute » et "
          "« la justice pour des temps indéfinis ».",
 calcul=[("70ᵉ semaine", "Elle commence à l'automne 29, avec le baptême et l'onction de Jésus",
          "automne 29"),
         ("Moitié annoncée", "« la moitié de la semaine » = 3 ans et demi", "3 ans ½"),
         ("Addition", "automne 29 + 3 ans et demi", "printemps 33"),
         ("Repère évangélique", "La mort de Jésus a lieu le 14 Nisan, jour de la Pâque — "
          "Matthieu 26:2 ; Jean 19:14", "14 Nisan 33")],
 accom_ref="Matthieu 27:32-56 · Marc 15:21-41 · Luc 23:26-49 · Jean 19:16-37",
 accom_txt="Jésus meurt un vendredi, le 14 Nisan. Le même jour, à la même heure, l'agneau pascal "
           "est immolé au temple. Il présente à son Père la valeur de son sacrifice humain : "
           "la réalité céleste préfigurée par le Très-Saint est désormais établie.",
 doc="<b>Les quatre Évangiles</b> concordent sur la séquence : dernier repas le 14 Nisan au soir, "
     "procès la nuit, crucifixion le vendredi, tombeau vide le premier jour de la semaine. "
     "Le chiffre de 3 ans et demi pour le ministère correspond aux quatre Pâques mentionnées "
     "dans l'Évangile de Jean.",
 limite="D'autres propositions existent pour l'année de la mort de Jésus (30, 31). Cette fiche "
        "suit le système chronologique unique du dossier, fondé sur les soixante-dix semaines : "
        "455 + 486 ans et demi = printemps 33. On ne mélange pas les systèmes.",
 src=[("Soixante-dix semaines", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013825"),
      ("Chronologie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010959"),
      ("Le grand temple spirituel de Jéhovah", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996483")],
 img="images/date_06_33.jpg"))

F.append(dict(
 n=7, date="36", ere="de notre ère", sys="Système biblique",
 titre="La 70ᵉ semaine s'achève — la faveur s'ouvre aux nations",
 prop_ref="Daniel 9:24, 27 · Actes 10:1-48 · Actes 11:1-18",
 prop_txt="Soixante-dix semaines ont été « déterminées » sur le peuple de Daniel. La "
          "soixante-dixième s'achève 490 ans après le départ.",
 calcul=[("Point de départ", "La parole de rebâtir Jérusalem entre en vigueur", "455 av. n. è."),
         ("Durée annoncée", "70 semaines d'années = 70 × 7", "490 ans"),
         ("Addition", "455 avant notre ère + 490 ans", "36 de notre ère"),
         ("Repère biblique", "Corneille, premier non-Juif incirconcis, est introduit dans la "
          "congrégation — Actes 10", "automne 36"),
         ("Contrôle", "Pierre rend compte de l'événement à Jérusalem et les opposants "
          "« se turent et glorifièrent Dieu » — Actes 11:18", "Actes 11")],
 accom_ref="Actes 10:1-48 · Actes 11:1-18 · Actes 15:7-9",
 accom_txt="Un officier romain, craignant Dieu sans être prosélyte, reçoit l'esprit saint avant "
           "même d'être baptisé. La période de faveur spéciale accordée à la nation juive "
           "s'achève : la bonne nouvelle s'ouvre désormais aux gens des nations.",
 doc="<b>Le livre des Actes</b> situe la conversion de Corneille après la mort d'Étienne et la "
     "dispersion, et avant le séjour de Paul à Antioche : la séquence interne du récit cadre "
     "avec l'automne 36.",
 limite="La Bibliothèque en ligne elle-même écrit : « il semble bien que Corneille n'a été "
        "introduit dans la congrégation chrétienne qu'en automne de l'an 36 ». La date est "
        "déduite, non révélée. Le texte donne l'événement, le calcul situe l'année.",
 src=[("Soixante-dix semaines", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013825"),
      ("Chronologie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010959"),
      ("Bibliothèque en ligne", "https://wol.jw.org/fr/wol/h/r30/lp-f")],
 img="images/date_07_36.jpg"))

F.append(dict(
 n=8, date="1914", ere="de notre ère", sys="Système biblique",
 titre="Les sept temps s'achèvent — Jérusalem cesse d'être foulée",
 prop_ref="Daniel 4:16, 23-25 · Luc 21:24 · Ézéchiel 21:26, 27 · Révélation 11:2, 3 ; 12:6, 14",
 prop_txt="Sept temps passeront sur la domination exercée depuis Jérusalem, « jusqu'à ce que tu "
          "saches que le Très-Haut est Chef dans le royaume des humains ». Jésus reprend la "
          "formule : « Jérusalem sera foulée aux pieds par les nations jusqu'à ce que les "
          "temps fixés des nations soient accomplis. »",
 calcul=[("Durée symbolique", "7 temps = 7 × 360 jours prophétiques", "2 520 jours"),
         ("Règle d'interprétation", "« Un jour pour une année » — Ézéchiel 4:6 ; "
          "Nombres 14:34", "2 520 ans"),
         ("Contrôle interne", "3 temps et demi = 1 260 jours (Révélation 12:6, 14) ; "
          "le double = 2 520", "cohérent"),
         ("Point de départ", "Jérusalem dévastée, le trône de la royauté de Jéhovah cesse : "
          "octobre 607", "15 Tishri 607"),
         ("Premier segment", "d'octobre 607 à octobre de l'an 1 avant notre ère", "606 ans"),
         ("Deuxième segment", "d'octobre de l'an 1 avant notre ère à octobre de l'an 1 "
          "(il n'y a pas d'année zéro)", "1 an"),
         ("Troisième segment", "d'octobre de l'an 1 de notre ère à octobre 1914", "1 913 ans"),
         ("Total", "606 + 1 + 1 913", "2 520 ans → octobre 1914")],
 accom_ref="Luc 21:24 · Daniel 4:17 · Révélation 12:7-12",
 accom_txt="Les temps fixés des nations s'achèvent. Jésus Christ reçoit la domination ; "
           "les nations sont désormais « au milieu de ses ennemis ». C'est le commencement de la "
           "conclusion du système de choses : guerres, famines, pestes, et la prédication "
           "mondiale annoncée en Matthieu 24:14.",
 doc="<b>Le calcul n'est pas une invention du XXᵉ siècle :</b> il est fondé sur trois textes "
     "bibliques qui se croisent (Daniel 4, Ézéchiel 4:6, Luc 21:24) et sur la date de 607 "
     "établie par les soixante-dix ans. Le point de départ et la règle viennent tous deux "
     "de la Bible, pas de l'histoire profane.",
 limite="1914 marque le <b>début</b> de la conclusion du système de choses, <b>pas une date de "
        "fin</b>. Aucune date n'est fixée pour l'avenir. Ce dossier ne calcule rien au-delà : "
        "« Quant à ce jour-là et à cette heure-là, personne ne les connaît » (Matthieu 24:36).",
 src=[("“ La scène de ce monde est en train de changer ”",
       "https://wol.jw.org/fr/wol/d/r30/lp-f/2004084"),
      ("Le Roi règne !", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101981014"),
      ("Le mystère du grand arbre est élucidé", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999025"),
      ("La chronologie biblique désigne notre époque", "https://wol.jw.org/fr/wol/d/r30/lp-f/1974200")],
 img="images/date_08_1914.jpg"))

# ---------------------------------------------------------------------------
# LA CHAÎNE
# ---------------------------------------------------------------------------
CHAINE = [
 ("607 av. n. è.", "Jérusalem dévastée — début des 70 ans", "départ"),
 ("→ 70 ans", "désolation littérale (Jérémie 25:11)", "écart"),
 ("537 av. n. è.", "retour d'exil — fin des 70 ans", "date"),
 ("→ 82 ans", "reconstruction interdite, puis reprise", "écart"),
 ("455 av. n. è.", "ordre de rebâtir — départ des 70 semaines", "départ"),
 ("→ 483 ans", "69 semaines d'années (Daniel 9:25)", "écart"),
 ("29 de n. è.", "le Messie paraît, oint à son baptême", "date"),
 ("→ 3 ans ½", "« la moitié de la semaine » (Daniel 9:27)", "écart"),
 ("33 de n. è.", "le Messie retranché, 14 Nisan", "date"),
 ("→ 3 ans ½", "fin de la 70ᵉ semaine", "écart"),
 ("36 de n. è.", "Corneille — la faveur s'ouvre aux nations", "date"),
 ("→ 1 878 ans", "aucun calcul prophétique ne couvre cet intervalle", "écart"),
 ("1914 de n. è.", "fin des sept temps (2 520 ans depuis 607)", "date"),
]

# ---------------------------------------------------------------------------
# STYLE — A4 imprimable
# ---------------------------------------------------------------------------
CSS = """
:root{--bleu:#0B2545;--or:#E9C46A;--creme:#F7F4EC;--gris:#5b6472;}
*{box-sizing:border-box;}
body{margin:0;background:#cfcabd;color:#1b2430;
 font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.45;}
.garde{background:var(--bleu);color:#fff;padding:60px 46px;}
.garde .kicker{color:var(--or);text-transform:uppercase;letter-spacing:3px;
 font-size:12px;font-weight:700;margin-bottom:14px;}
.garde h1{font-size:38px;margin:0 0 10px;letter-spacing:.5px;}
.garde .sous{font-size:16px;color:#c9d3e4;max-width:640px;}
.garde .chiffres{display:flex;gap:26px;margin-top:34px;flex-wrap:wrap;}
.garde .chiffres div{border-left:3px solid var(--or);padding-left:13px;}
.garde .chiffres b{display:block;font-size:26px;color:#fff;}
.garde .chiffres span{font-size:12px;color:#aab6cc;text-transform:uppercase;letter-spacing:1px;}
.fiche{width:210mm;min-height:297mm;margin:0 auto 12mm;background:var(--creme);
 padding:14mm 15mm;page-break-after:always;position:relative;}
.hd{border-bottom:3px solid var(--bleu);padding-bottom:8px;margin-bottom:12px;
 display:flex;justify-content:space-between;align-items:flex-end;}
.hd .g{font-size:11px;letter-spacing:2.4px;font-weight:700;color:var(--or);
 text-transform:uppercase;}
.hd .n{font-size:11px;color:var(--gris);font-weight:700;}
.dateligne{display:flex;align-items:baseline;gap:14px;margin:0 0 4px;}
.dateligne .n0{font-size:64px;font-weight:800;color:var(--bleu);line-height:.9;
 letter-spacing:-2px;}
.dateligne .ere{font-size:15px;color:var(--gris);font-weight:600;}
.dateligne .sys{margin-left:auto;font-size:10.5px;background:var(--bleu);color:#fff;
 padding:3px 9px;border-radius:12px;letter-spacing:.6px;}
.dateligne .sys.neutre{background:#7a5b12;}
h2.titre{font-size:17px;color:var(--bleu);margin:6px 0 14px;}
h3{font-size:12px;text-transform:uppercase;letter-spacing:1.6px;color:var(--bleu);
 margin:14px 0 6px;border-left:4px solid var(--or);padding-left:8px;}
table{border-collapse:collapse;width:100%;font-size:12px;margin-bottom:4px;}
th,td{border:1px solid #d8d2c4;padding:5px 7px;text-align:left;vertical-align:top;}
th{background:var(--bleu);color:#fff;font-size:10.5px;text-transform:uppercase;
 letter-spacing:.4px;}
td.r{text-align:right;font-weight:700;color:var(--bleu);white-space:nowrap;}
tr:nth-child(even) td{background:#fbf9f4;}
p{margin:0 0 8px;font-size:12.5px;}
.ref{font-family:Consolas,monospace;font-size:11px;color:var(--gris);}
.cadre{background:#fff;border:1px solid #dcd6c6;border-left:5px solid var(--bleu);
 padding:9px 11px;margin:8px 0;}
.cadre.attention{background:#fff8e8;border-color:var(--or);border-left-color:var(--or);}
.cadre b{color:var(--bleu);}
.src{font-size:11px;columns:2;column-gap:16px;}
.src a{color:#1a4a8a;word-break:break-all;display:block;margin-bottom:3px;}
.notes{margin-top:auto;padding-top:10px;}
.notes .l{border-bottom:1px solid #cfc7b6;height:20px;}
.imgref{font-family:Consolas,monospace;font-size:10.5px;color:var(--gris);}
.pied{border-top:1px solid #d8d2c4;margin-top:10px;padding-top:6px;font-size:10px;
 color:var(--gris);display:flex;justify-content:space-between;}
.chainetable td{padding:7px 9px;}
.chainetable tr.ecart td{background:#eef1f6;color:var(--gris);font-style:italic;font-size:11.5px;}
.chainetable tr.depart td.n0{background:#fdf6e3;font-weight:800;}
.ch-doc{max-width:210mm;margin:0 auto 12mm;background:var(--creme);padding:14mm 15mm;
 page-break-after:always;}
.ch-doc h1{font-size:26px;color:var(--bleu);margin:0 0 4px;}
.ch-doc .soustitre{color:var(--gris);font-size:13px;margin-bottom:16px;}
.avert{background:#0B2545;color:#fff;padding:12px 15px;border-radius:4px;font-size:12.5px;
 margin:14px 0;}
.avert b{color:var(--or);}
ol{margin:0;padding-left:20px;}
li{font-size:12.5px;margin-bottom:6px;}
@media print{
 body{background:#fff;}
 .fiche,.ch-doc{page-break-after:always;margin:0;}
 .garde{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
 @page{size:A4;margin:0;}
}
"""

def esc(s):
    return html.escape(str(s))

H = [f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FICHES DE DATES — projet PREUVES</title>
<style>{CSS}</style></head><body>

<div class="garde">
<div class="kicker">Bibliothèque privée · projet PREUVES · vague 7</div>
<h1>FICHES DE DATES</h1>
<div class="sous">Huit dates, huit fiches détachables au format A4. Chacune donne la prophétie,
le calcul écrit ligne par ligne, l'accomplissement, le document profane qui l'appuie, la source
et — toujours — la limite de ce qu'elle permet d'affirmer.</div>
<div class="chiffres">
<div><b>8</b><span>fiches A4</span></div>
<div><b>28</b><span>lignes de calcul</span></div>
<div><b>1</b><span>chaîne complète</span></div>
<div><b>0</b><span>date pour l'avenir</span></div>
</div>
</div>

<div class="ch-doc">
<h1>Comment se servir de ces fiches</h1>
<div class="soustitre">Une fiche à la fois. Un système chronologique à la fois. Aucune date pour l'avenir.</div>

<h3>La règle des trois lectures</h3>
<ol>
<li><b>Lire la prophétie.</b> On ne commente pas : on lit le texte et sa référence. C'est le
point de départ de tout le dossier.</li>
<li><b>Suivre le calcul.</b> Chaque ligne est une opération, avec son résultat à droite. Si une
ligne ne se défend pas, la fiche entière tombe — c'est fait exprès : le lecteur peut vérifier
au lieu de croire.</li>
<li><b>Lire la limite avant la conclusion.</b> Toute fiche se termine par ce qu'elle ne dit pas.
C'est ce qui la rend crédible.</li>
</ol>

<h3>Les trois précautions</h3>
<div class="avert"><b>1. Un seul système par document.</b> Le dossier retient 607 pour la
désolation de Jérusalem, 537 pour le retour, 455 pour l'ordre de rebâtir, 29 pour l'onction du
Messie, 33 pour sa mort, 36 pour la fin de la faveur spéciale, et 1914 pour la fin des sept
temps. La date de 539 est la seule admise par toutes les chronologies : elle sert de pivot,
jamais d'argument. On ne mélange pas deux systèmes dans une même page.</div>
<div class="avert"><b>2. Aucune date pour l'avenir.</b> Ce qui n'est pas accompli reste sans
date. 1914 marque le début de la conclusion du système de choses. Il ne sert à calculer aucune
échéance : « Quant à ce jour-là et à cette heure-là, personne ne les connaît » (Matthieu 24:36).</div>
<div class="avert"><b>3. Aucun total dogmatique.</b> La Bibliothèque en ligne écrit qu'il est
préférable de ne pas se montrer trop affirmatif quant au nombre exact des prophéties
messianiques. Huit dates valent mieux que mille : on vérifie, on ne compte pas.</div>

<h3>Présenter une fiche en quatre-vingt-dix secondes</h3>
<ol>
<li>Poser la fiche à plat, sans la commenter : <i>« Voici un texte écrit d'avance, et voici ce
qui s'est passé. »</i></li>
<li>Poser le doigt sur la ligne de calcul et laisser l'autre lire.</li>
<li>Nommer le document profane : la tablette, l'inscription, la chronique.</li>
<li>Dire la limite soi-même, avant qu'elle ne soit objectée. C'est le geste qui emporte
la confiance.</li>
<li>Finir sur un lien officiel : <a href="https://www.jw.org/fr/">www.jw.org</a> ou
<a href="https://wol.jw.org/fr/wol/h/r30/lp-f">wol.jw.org</a>.</li>
</ol>
<p style="margin-top:14px;font-size:11.5px;color:#5b6472"><b>Illustrations.</b> Chaque fiche
renvoie à une image du dossier <span class="ref">images/</span>. Aucune de ces images n'est un
document : ni photographie d'un site réel, ni reproduction d'un artefact. Ce sont des
illustrations d'ambiance, toujours légendées comme telles.</p>
</div>

<div class="ch-doc">
<h1>La chaîne complète</h1>
<div class="soustitre">Les huit dates dans l'ordre, avec les écarts. Un seul fil relie le tout :
455 → 29 → 33 → 36 d'un côté (les soixante-dix semaines), et 607 → 1914 de l'autre
(les sept temps). Les deux fils ne se mélangent pas.</div>
<table class="chainetable"><thead><tr><th style="width:150px">Repère</th>
<th>Événement</th><th style="width:112px">Nature</th></tr></thead><tbody>"""]

for rep, ev, nat in CHAINE:
    cls = {"écart": "ecart", "départ": "depart"}.get(nat, "")
    H.append(f'<tr class="{cls}"><td class="n0">{esc(rep)}</td><td>{esc(ev)}</td>'
             f'<td style="font-size:11px;color:#5b6472">{esc(nat)}</td></tr>')

H.append("""</tbody></table>
<div class="cadre attention" style="margin-top:16px"><b>À remarquer.</b> Entre 36 et 1914,
aucun calcul prophétique ne couvre l'intervalle : le dossier ne comble pas les vides. Entre
607 et 1914 en revanche, le fil est continu : ce sont les sept temps, soit 2 520 ans. Les deux
chaînes sont indépendantes ; les confondre est l'erreur la plus fréquente dans les présentations
trop rapides.</div>
<div class="cadre"><b>Contrôle d'honnêteté.</b> Sur les huit dates, une seule (539) est admise
par toutes les chronologies. Deux (607 et 455) sont contestées par une partie des historiens
profanes. Trois (537, 29, 36) sont déduites de documents datés. Deux (33, 1914) découlent
d'un calcul biblique interne. Le dire vaut mieux que le cacher.</div>
</div>""")

for f in F:
    H.append('<div class="fiche">')
    H.append(f'<div class="hd"><div><div class="g">Fiche de date n° {f["n"]} / 8</div>'
             f'<div class="n">PROJET PREUVES · vague 7</div></div>'
             f'<div class="n">Système : {esc(f["sys"])}</div></div>')
    neutre = " neutre" if f["sys"] == "Date neutre" else ""
    H.append(f'<div class="dateligne"><div class="n0">{esc(f["date"])}</div>'
             f'<div class="ere">{esc(f["ere"])}</div>'
             f'<div class="sys{neutre}">{esc(f["sys"].upper())}</div></div>')
    H.append(f'<h2 class="titre">{esc(f["titre"])}</h2>')

    H.append('<h3>1 · La prophétie</h3>')
    H.append(f'<div class="ref">{esc(f["prop_ref"])}</div>')
    H.append(f'<p style="margin-top:5px">{esc(f["prop_txt"])}</p>')

    H.append('<h3>2 · Le calcul</h3>')
    H.append('<table><thead><tr><th>Étape</th><th>Opération</th>'
             '<th style="width:118px">Résultat</th></tr></thead><tbody>')
    for et, op, res in f["calcul"]:
        H.append(f"<tr><td><b>{esc(et)}</b></td><td>{esc(op)}</td><td class='r'>{esc(res)}</td></tr>")
    H.append("</tbody></table>")

    H.append('<h3>3 · L’accomplissement</h3>')
    H.append(f'<div class="ref">{esc(f["accom_ref"])}</div>')
    H.append(f'<p style="margin-top:5px">{esc(f["accom_txt"])}</p>')

    H.append('<h3>4 · Le document</h3>')
    H.append(f'<div class="cadre">{f["doc"]}</div>')

    H.append('<h3>5 · Ce que cette fiche ne dit pas</h3>')
    H.append(f'<div class="cadre attention">{f["limite"]}</div>')

    H.append('<h3>6 · Sources</h3><div class="src">')
    for t, u in f["src"]:
        H.append(f'<a href="{u}">{esc(t)}<br>{esc(u)}</a>')
    H.append("</div>")

    H.append('<div class="notes">')
    H.append('<h3 style="border-left-color:#d8d2c4;color:#5b6472">Notes manuscrites</h3>')
    for _ in range(4):
        H.append('<div class="l"></div>')
    H.append("</div>")
    H.append(f'<div class="pied"><span>Illustration : <span class="imgref">{esc(f["img"])}</span>'
             f' — illustration d’ambiance, jamais un document.</span>'
             f'<span>Fiche {f["n"]}/8 · {esc(f["date"])} {esc(f["ere"])}</span></div>')
    H.append("</div>")

H.append(f"""
<div class="ch-doc">
<h1>Rappel final — transmission</h1>
<div class="soustitre">Ce carnet est un ensemble de fichiers privés. Il ne devient ni un site,
ni une chaîne, ni un compte.</div>
<table><thead><tr><th style="width:24%">Règle</th><th>Application</th></tr></thead><tbody>
<tr><td><b>Un à un</b></td><td>Transmission de personne à personne. Jamais de diffusion publique,
jamais d'envoi groupé.</td></tr>
<tr><td><b>Une fiche à la fois</b></td><td>On remet la fiche demandée. Le carnet entier cesse
d'être lu dès qu'il est complet.</td></tr>
<tr><td><b>Liens officiels seulement</b></td><td>Tout renvoi passe par www.jw.org ou wol.jw.org.
Aucun extrait de publication n'est recopié, hébergé ni republié.</td></tr>
<tr><td><b>Aucune collecte</b></td><td>Aucune donnée personnelle n'est demandée ni stockée.</td></tr>
<tr><td><b>Aucune date</b></td><td>Ce qui n'est pas accompli n'est jamais daté.</td></tr>
</tbody></table>
<p style="margin-top:18px;font-size:11.5px;color:#5b6472">
Généré le {datetime.date.today().isoformat()} · vague 7 · projet PREUVES.
Sources : Bibliothèque en ligne Watchtower (wol.jw.org) et www.jw.org.
Aucun contenu protégé n'est reproduit : les références bibliques sont citées, les publications
ne sont pas recopiées.</p>
</div>
</body></html>""")

out = os.path.join(ROOT, "FICHES_DATES.html")
open(out, "w", encoding="utf-8").write("\n".join(H))

print("Fiches :", len(F))
print("Lignes de calcul :", sum(len(f["calcul"]) for f in F))
print("Sources :", sum(len(f["src"]) for f in F))
print("FICHES_DATES.html :", os.path.getsize(out) // 1024, "Ko")
