#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAGUE 8 — Le cahier de l'auditeur.

Ecrit : preuves/CAHIER_AUDITEUR.html

Trois parties :
  A. 8 fiches de dates a trous (exercice) + corrigé detachable
  B. 13 fiches d'ecoute reliees (une par collection)
  C. 8 cartes d'objection recto/verso (85 x 55 mm), impression recto-verso

Regles : aucune date pour l'avenir · un seul systeme chronologique ·
         liens jw.org / wol.jw.org seulement · aucune ressource distante.
"""

import os, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# A. LES HUIT FICHES A TROUS
# ---------------------------------------------------------------------------
TROUS = [
 dict(n=1, date="607 av. n. è.", theme="Jérusalem dévastée — le début des 70 ans",
      ref="Jérémie 25:11, 12 · Jérémie 29:10 · 2 Chroniques 36:21 · Daniel 9:2",
      q=[("Les exilés sont de retour à Jérusalem à l’automne", "537"),
         ("Jérémie annonce une désolation de", "70 ans"),
         ("Opération : automne 537 − 70 ans = automne", "607"),
         ("Jérusalem tombe le 9 Tammouz ; le 10 Ab, Nébuzaradan détruit la ville — 2 Rois", "25:8, 9"),
         ("La majorité des historiens profanes retient", "587")],
      cor="Jérusalem est prise, le temple brûlé, les murailles abattues. Le pays reste désolé "
          "soixante-dix ans parce que, contrairement aux Assyriens, le roi de Babylone "
          "n’installe personne pour remplacer les Juifs."),
 dict(n=2, date="539 av. n. è.", theme="Babylone tombe — le fleuve et les portes",
      ref="Isaïe 44:27, 28 · Isaïe 45:1, 2 · Jérémie 50:38 · Daniel 5",
      q=[("La Chronique de Nabonide situe la chute de Babylone le 16", "Tashritu"),
         ("Soit, dans notre calendrier", "11/12 octobre"),
         ("Le roi perse nommé par son nom plus d’un siècle à l’avance", "Cyrus"),
         ("Cette date est la seule que", "toutes les chronologies admettent"),
         ("Le document profane : la Chronique de Nabonide et le", "cylindre de Cyrus")],
      cor="La ville est prise la nuit où Belshatsar fait servir le vin dans les coupes du temple. "
          "Le détournement de l’Euphrate correspond au texte d’Isaïe et de Jérémie sur le "
          "fleuve mis à sec."),
 dict(n=3, date="537 av. n. è.", theme="Le retour d’exil — la fin des 70 ans",
      ref="Jérémie 29:10 · 2 Chroniques 36:22, 23 · Esdras 1:1-4 · Esdras 3:1",
      q=[("D’après la tablette « Strassmaier, Cyrus n° 11 », la 1ʳᵉ année de Cyrus va "
          "du 17/18 mars 538 au 4/5 mars", "537"),
         ("Le décret est donc publié à la fin de l’hiver ou au début du printemps", "537"),
         ("Les exilés arrivent à Jérusalem juste avant le", "7ᵉ mois (Tishri)"),
         ("L’autel est relevé ; les fondations du temple sont posées l’année suivante", "536"),
         ("La désolation prend fin parce que le pays est de nouveau", "occupé")],
      cor="Ce n’est pas la signature du décret qui met fin aux soixante-dix ans, mais le retour "
          "effectif : le pays doit être de nouveau habité."),
 dict(n=4, date="455 av. n. è.", theme="L’ordre de rebâtir — le départ des 70 semaines",
      ref="Daniel 9:24, 25 · Néhémie 2:1-8 · Néhémie 6:15",
      q=[("Néhémie obtient l’ordre de rebâtir la", "20ᵉ année d’Artaxerxès Iᵉʳ"),
         ("Néhémie exerce la charge de", "échanson du roi"),
         ("Le règne d’Artaxerxès commence en", "474"),
         ("7 semaines + 62 semaines = 69 semaines =", "483 ans"),
         ("455 + 483 =", "29 de notre ère"),
         ("La muraille est achevée après", "52 jours de travail")],
      cor="La parole sort de Suse, mais elle ne prend effet qu’à Jérusalem : le même principe "
          "avait déjà valu pour le décret de Cyrus."),
 dict(n=5, date="29 de n. è.", theme="Le Messie paraît — au bout des 69 semaines",
      ref="Daniel 9:25 · Luc 3:1, 21-23 · Actes 10:38",
      q=[("69 semaines d’années =", "483 ans"),
         ("Luc date le début du ministère de Jean de la", "15ᵉ année de Tibère César"),
         ("Tibère règne à partir du 17 août", "14 de notre ère"),
         ("Référence du repère profane : Luc", "3:1"),
         ("Jésus est alors âgé d’environ", "30 ans")],
      cor="Jésus vient se faire baptiser dans le Jourdain et reçoit l’onction : il devient le "
          "Christ, Messie le Conducteur. Le grand temple spirituel commence à fonctionner."),
 dict(n=6, date="33 de n. è.", theme="Le Messie retranché — à la moitié de la semaine",
      ref="Daniel 9:24-27 · Matthieu 26:2 · Jean 19:14",
      q=[("La 70ᵉ semaine commence à l’automne", "29"),
         ("« La moitié de la semaine » =", "3 ans et demi"),
         ("automne 29 + 3 ans ½ = printemps", "33"),
         ("Jésus meurt le", "14 Nisan"),
         ("D’autres années parfois proposées", "30 et 31")],
      cor="Jésus meurt un vendredi, le 14 Nisan, jour de la Pâque. Le chiffre de trois ans et "
          "demi pour le ministère correspond aux quatre Pâques de l’Évangile de Jean."),
 dict(n=7, date="36 de n. è.", theme="La 70ᵉ semaine s’achève — la faveur s’ouvre aux nations",
      ref="Daniel 9:24, 27 · Actes 10:1-48 · Actes 11:1-18",
      q=[("70 semaines d’années =", "490 ans"),
         ("455 + 490 =", "36 de notre ère"),
         ("Le premier non-Juif incirconcis reçoit l’esprit saint", "Corneille"),
         ("Référence", "Actes 10"),
         ("Pierre rend compte à Jérusalem, et les opposants « se turent » — Actes", "11:18")],
      cor="Un officier romain craignant Dieu reçoit l’esprit saint avant même d’être baptisé. "
          "La Bibliothèque en ligne écrit : « il semble bien que Corneille n’a été introduit "
          "qu’en automne de l’an 36 » — la date est déduite, non révélée."),
 dict(n=8, date="1914 de n. è.", theme="Les sept temps s’achèvent",
      ref="Daniel 4:16, 23-25 · Luc 21:24 · Ézéchiel 21:26, 27 · Révélation 12:6, 14",
      q=[("7 temps = 7 × 360 =", "2 520 jours"),
         ("Règle d’interprétation : « Un jour pour une ______ » — Ézéchiel 4:6", "année"),
         ("Contrôle interne : 3 temps et demi =", "1 260 jours"),
         ("Point de départ : octobre", "607"),
         ("606 + 1 +", "1 913"),
         ("1914 marque un ______, jamais une fin", "début")],
      cor="Les temps fixés des nations s’achèvent. C’est le commencement de la conclusion du "
          "système de choses. Aucune date n’est fixée pour l’avenir : « Quant à ce jour-là et "
          "à cette heure-là, personne ne les connaît » (Matthieu 24:36)."),
]

# ---------------------------------------------------------------------------
# B. LES TREIZE FICHES D'ECOUTE
# ---------------------------------------------------------------------------
ECOUTE = [
 (1,  "Par où commencer", 6, "6 min 10", "SITE_LOCAL.html — onglet Accueil",
  "Quelle est la seule règle du jeu que je dois énoncer avant d’ouvrir le dossier ?"),
 (2,  "Les douze preuves", 9, "11 min 57", "22_GRAND_DOSSIER.md",
  "Laquelle des douze preuves se résume le mieux en une phrase ?"),
 (3,  "Les huit objections", 6, "6 min 05", "22_GRAND_DOSSIER.md — annexe",
  "Quelle objection m’a le plus résisté, et pourquoi ?"),
 (4,  "Babylone et Cyrus", 7, "6 min 53", "LIVRE_1_ENQUETE.html",
  "Quel détail matériel (le fleuve, les portes) me paraît le plus difficile à expliquer "
  "autrement que par la prophétie ?"),
 (5,  "Tyr, l’Égypte et les nations", 7, "8 min 11", "videos/SCRIPTS_VIDEOS.html — V3",
  "Pourquoi « racler la poussière » est-il un détail décisif ?"),
 (6,  "Les dates", 8, "8 min 12", "visuels/FRISES_CHRONOLOGIQUES.html",
  "Saurais-je refaire la chaîne sans regarder ?"),
 (7,  "Le Messie", 9, "15 min 14", "LIVRE_3_DETAIL.html — parties 7 et 8",
  "Pourquoi ne faut-il pas donner de total ?"),
 (8,  "Le signe des derniers jours", 8, "12 min 18", "SITE_LOCAL.html — onglet Signe",
  "Quelle phrase dois-je dire pour ne laisser croire à aucune date ?"),
 (9,  "Le livre de la Révélation", 8, "16 min 19", "LIVRE_3_DETAIL.html — parties 11 et 12",
  "Quel chapitre ai-je le plus envie de relire dans la Bible elle-même ?"),
 (10, "Le monde nouveau", 7, "9 min 05", "videos/SCRIPTS_VIDEOS.html — L1",
  "Par quoi la Bible finit-elle, au juste ?"),
 (11, "Comment le texte est arrivé jusqu’à nous", 7, "7 min 30", "23_REGISTRE_PROPHETIES_7.md",
  "Comment répondre en une phrase à « le texte a été recopié mille fois » ?"),
 (12, "Présenter le dossier à quelqu’un", 8, "6 min 35", "visuels/COFFRET.html",
  "Ai-je un fichier prêt à remettre cette semaine ?"),
 (13, "Les huit dates", 8, "2 min 52", "FICHES_DATES.html",
  "Quelle ligne de calcul est la plus fragile ?"),
]

# ---------------------------------------------------------------------------
# C. LES HUIT CARTES D'OBJECTION
# ---------------------------------------------------------------------------
OBJ = [
 dict(n=1, court="Écrites après coup",
      obj="« Les prophéties ont été écrites après coup. »",
      rep="C’est précisément l’argument des critiques contre Daniel 11. La question se tranche "
          "sur les dates, pas sur les faits : les manuscrits de la mer Morte, dont 4Q114 pour "
          "Daniel, attestent l’ancienneté des copies.",
      src=[("Daniel (livre de) — authenticité et historicité",
            "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001118"),
           ("La Bible a survécu aux tentatives de falsification",
            "https://wol.jw.org/fr/wol/d/r30/lp-f/2016247")]),
 dict(n=2, court="Poésie vague",
      obj="« Trop de prophéties ressemblent à de la poésie. »",
      rep="On ne retient que les énoncés datables et vérifiables : un nom, une durée, un lieu, "
          "une méthode. Ce qui n’est pas datable ne sert pas d’argument.",
      src=[("La Bible et l’Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
           ("Bibliothèque en ligne", "https://wol.jw.org/fr/wol/h/r30/lp-f")]),
 dict(n=3, court="On fait dire au texte",
      obj="« N’importe qui peut faire dire n’importe quoi à un texte. »",
      rep="Chaque fiche donne la référence, la teneur, l’accomplissement, la source extérieure "
          "et sa limite. Le lecteur vérifie ; il ne croit pas sur parole.",
      src=[("La Bible et l’Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
           ("Questions bibliques", "https://www.jw.org/fr/la-bible-et-vous/questions-bibliques/")]),
 dict(n=4, court="Dates invérifiables",
      obj="« Les dates de la Bible sont invérifiables. »",
      rep="Un seul système chronologique par document. Quand la chronologie profane diffère, "
          "elle est signalée — par exemple Ninive : 632 ou 612 selon le système retenu.",
      src=[("Chronologie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010959"),
           ("Quand l’ancienne Jérusalem a-t-elle été détruite ? (2)",
            "https://wol.jw.org/fr/wol/d/r30/lp-f/2011810")]),
 dict(n=5, court="1914 fixé après coup",
      obj="« Vous avez fixé 1914 après coup. »",
      rep="Le calcul est montré pas à pas : Daniel 4 ; Révélation 12:6, 14 ; Ézéchiel 4:6 ; "
          "Nombres 14:34. Libre à chacun d’examiner la méthode et de la contester.",
      src=[("“ La scène de ce monde est en train de changer ”",
            "https://wol.jw.org/fr/wol/d/r30/lp-f/2004084"),
           ("Le mystère du grand arbre est élucidé",
            "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999025")]),
 dict(n=6, court="Interprétation de la Révélation",
      obj="« Vous interprétez la Révélation à votre façon. »",
      rep="On donne la lecture de l’organisation et sa source, sans polémique : les prophéties "
          "accomplies sont vérifiables, les autres sont annoncées comme telles.",
      src=[("Bibliothèque en ligne", "https://wol.jw.org/fr/wol/h/r30/lp-f"),
           ("Questions bibliques", "https://www.jw.org/fr/la-bible-et-vous/questions-bibliques/")]),
 dict(n=7, court="Et si vous vous trompez ?",
      obj="« Et si vous vous trompez ? »",
      rep="C’est pourquoi le dossier ne date pas la fin et ne donne aucun total dogmatique. "
          "Une démonstration qui ne peut pas être réfutée n’est pas une démonstration.",
      src=[("La Bible et l’Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
           ("Cours biblique particulier",
            "https://www.jw.org/fr/la-bible-et-vous/cours-biblique-particulier/")]),
 dict(n=8, court="Ces images sont fausses",
      obj="« Ces images sont fausses. »",
      rep="Toutes les images générées sont légendées « Illustration. » et ne sont jamais "
          "présentées comme des documents : ni photographie d’un site réel, ni reproduction "
          "d’un artefact.",
      src=[("jw.org — accueil", "https://www.jw.org/fr/"),
           ("Bibliothèque en ligne", "https://wol.jw.org/fr/wol/h/r30/lp-f")]),
]

# Pour aller plus loin (recherche de cette vague)
PLUS = [
 ("La Bible se contredit-elle ? — divergences apparentes, rédacteurs indépendants, "
  "l’exemple de Matthieu 8:5 et Luc 7:3", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101989037"),
 ("La Bible se contredit-elle vraiment ? — l’affaire Galilée : « on a fait dire à la Bible »",
  "https://wol.jw.org/fr/wol/d/r30/lp-f/1981722"),
 ("Que révèle la chronologie de la Bible sur l’année 1914 ?",
  "https://wol.jw.org/fr/wol/d/r30/lp-f/502014148"),
]

# ---------------------------------------------------------------------------
# STYLE
# ---------------------------------------------------------------------------
CSS = """
:root{--bleu:#0B2545;--or:#E9C46A;--creme:#F7F4EC;--gris:#5b6472;}
*{box-sizing:border-box;}
body{margin:0;background:#cfcabd;color:#1b2430;
 font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.45;}
.pg{width:210mm;min-height:297mm;margin:0 auto 12mm;background:var(--creme);
 padding:14mm 15mm;page-break-after:always;}
.garde{background:var(--bleu);color:#fff;padding:58px 46px;min-height:297mm;}
.kicker{color:var(--or);text-transform:uppercase;letter-spacing:3px;font-size:12px;
 font-weight:700;margin-bottom:14px;}
.garde h1{font-size:40px;margin:0 0 12px;letter-spacing:.5px;line-height:1.1;}
.garde .sous{font-size:16px;color:#c9d3e4;max-width:600px;}
.garde .bloc{margin-top:36px;border-left:3px solid var(--or);padding-left:16px;}
.garde .bloc h3{color:#fff;font-size:15px;margin:0 0 6px;border:none;padding:0;
 text-transform:none;letter-spacing:0;}
.garde .bloc p{color:#c9d3e4;font-size:13px;margin:0;}
.garde .blocs{display:flex;flex-direction:column;gap:22px;margin-top:30px;}
.garde .chiffres{display:flex;gap:30px;margin-top:38px;flex-wrap:wrap;}
.garde .chiffres div{border-left:3px solid var(--or);padding-left:13px;}
.garde .chiffres b{display:block;font-size:27px;color:#fff;}
.garde .chiffres span{font-size:11px;color:#aab6cc;text-transform:uppercase;letter-spacing:1px;}
h1.t{font-size:27px;color:var(--bleu);margin:0 0 4px;}
.st{color:var(--gris);font-size:13px;margin-bottom:16px;}
h3{font-size:12px;text-transform:uppercase;letter-spacing:1.6px;color:var(--bleu);
 margin:16px 0 8px;border-left:4px solid var(--or);padding-left:8px;}
p{font-size:12.5px;margin:0 0 9px;}
.trou{border:1px solid #d8d2c4;border-radius:5px;background:#fff;padding:11px 13px;
 margin-bottom:9px;break-inside:avoid;}
.trou .hd{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:2px solid var(--or);padding-bottom:5px;margin-bottom:8px;}
.trou .hd b{font-size:15px;color:var(--bleu);}
.trou .hd .dt{font-size:19px;font-weight:800;color:var(--bleu);}
.trou .ref{font-family:Consolas,monospace;font-size:10.5px;color:var(--gris);
 margin-bottom:8px;}
.q{display:flex;gap:8px;font-size:12.5px;margin-bottom:7px;align-items:flex-start;}
.q .n{color:var(--or);font-weight:800;min-width:16px;}
.q .t{flex:1;}
.q .b{display:inline-block;min-width:120px;border-bottom:1.5px solid #0B2545;
 margin-left:5px;}
.ec{border:1px solid #d8d2c4;border-left:5px solid var(--bleu);background:#fff;
 padding:10px 12px;margin-bottom:10px;break-inside:avoid;}
.ec .hd{display:flex;justify-content:space-between;align-items:baseline;}
.ec .hd b{font-size:13.5px;color:var(--bleu);}
.ec .hd .m{font-size:11px;color:var(--gris);}
.ec .sup{font-family:Consolas,monospace;font-size:10.5px;color:var(--gris);margin:3px 0 6px;}
.ec .list{columns:2;column-gap:14px;font-size:11.5px;}
.ec .qv{font-size:11.5px;font-style:italic;color:#5b6472;margin-top:6px;}
.case{display:inline-block;width:12px;height:12px;border:1.5px solid var(--bleu);
 margin-right:6px;vertical-align:-2px;}
.lig{border-bottom:1px solid #cfc7b6;height:20px;margin-top:4px;}
.cartes{display:grid;grid-template-columns:1fr 1fr;gap:8mm;}
.carte{width:85mm;height:55mm;border:2px solid var(--bleu);border-radius:6px;background:#fff;
 padding:6mm 7mm;display:flex;flex-direction:column;justify-content:space-between;
 break-inside:avoid;overflow:hidden;}
.carte.verso{background:var(--bleu);border-color:var(--or);color:#fff;}
.carte .num{font-size:9px;letter-spacing:2px;font-weight:700;text-transform:uppercase;}
.carte.r .num{color:var(--or);}
.carte.v .num{color:var(--or);}
.carte .obj{font-size:14px;font-weight:700;color:var(--bleu);line-height:1.25;}
.carte .titreC{font-size:10px;color:var(--gris);text-transform:uppercase;letter-spacing:1px;}
.carte.v .rep{font-size:10.5px;color:#e8edf6;line-height:1.32;}
.carte.v .src{font-size:8px;color:#aab6cc;font-family:Consolas,monospace;line-height:1.25;
 word-break:break-all;}
table{border-collapse:collapse;width:100%;font-size:11.5px;}
th,td{border:1px solid #d8d2c4;padding:4px 7px;text-align:left;vertical-align:top;}
th{background:var(--bleu);color:#fff;font-size:10px;text-transform:uppercase;letter-spacing:.4px;}
td.r{text-align:center;font-weight:800;color:var(--bleu);white-space:nowrap;}
tr:nth-child(even) td{background:#fbf9f4;}
.cadre{background:#fff8e8;border:1px solid var(--or);border-left:5px solid var(--or);
 padding:10px 12px;font-size:12px;margin:10px 0;}
.cadre.b{background:#fff;border-color:#dcd6c6;border-left-color:var(--bleu);}
.src2{font-size:11px;}
.src2 a{color:#1a4a8a;display:block;margin-bottom:4px;word-break:break-all;}
ol,ul{margin:0 0 10px;padding-left:20px;}
li{font-size:12.5px;margin-bottom:5px;}
.pied{margin-top:auto;padding-top:8px;border-top:1px solid #d8d2c4;font-size:9.5px;
 color:var(--gris);display:flex;justify-content:space-between;}
.flexcol{display:flex;flex-direction:column;min-height:100%;}
@media print{
 body{background:#fff;}
 .pg,.garde{page-break-after:always;margin:0;}
 .carte{page-break-inside:avoid;}
 @page{size:A4;margin:0;}
}
"""

def e(s):
    return html.escape(str(s))

H = [f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CAHIER DE L'AUDITEUR — projet PREUVES</title>
<style>{CSS}</style></head><body>

<div class="garde">
<div class="kicker">Bibliothèque privée · projet PREUVES · vague 8</div>
<h1>CAHIER<br>DE L'AUDITEUR</h1>
<div class="sous">Ce cahier ne contient aucune démonstration. Il contient des cases vides.
On ne retient que ce qu'on a écrit soi-même : c'est la seule règle de ce carnet, et elle vaut
pour tout le dossier.</div>
<div class="chiffres">
<div><b>3</b><span>parties</span></div>
<div><b>8</b><span>fiches à trous</span></div>
<div><b>13</b><span>fiches d'écoute</span></div>
<div><b>8</b><span>cartes d'objection</span></div>
</div>
<div class="blocs">
<div class="bloc"><h3>Partie A — Les huit fiches à trous</h3>
<p>Huit dates, des blancs à remplir, un corrigé détachable à la fin. On remplit sans regarder,
puis on vérifie. Ce qui reste blanc est ce qu'il reste à apprendre.</p></div>
<div class="bloc"><h3>Partie B — Les treize fiches d'écoute</h3>
<p>Une fiche par collection : on coche au fur et à mesure, on répond à une seule question,
on note une seule phrase. Treize demi-pages reliées en un carnet.</p></div>
<div class="bloc"><h3>Partie C — Les huit cartes d'objection</h3>
<p>Format poche, 85 × 55 mm. Recto : l'objection, telle qu'elle est formulée. Verso : la réponse
en trois lignes et le lien. On imprime recto-verso, on découpe, on garde quatre cartes sur soi.</p></div>
</div>
<p style="margin-top:34px;font-size:11px;color:#8f9cb5">
Usage strictement privé. Aucun contenu protégé n'est reproduit. Liens exclusivement vers
www.jw.org et wol.jw.org. Aucune date pour l'avenir.</p>
</div>

<div class="pg"><div class="flexcol">
<h1 class="t">Mode d'emploi</h1>
<div class="st">Trois parties, trois usages. On peut n'en utiliser qu'une.</div>

<h3>La règle des vingt-quatre heures</h3>
<p>La courbe de l'oubli est impitoyable : sans réactivation, la moitié de ce qui vient d'être
entendu disparaît avant le lendemain. Ce cahier est construit autour de cette contrainte —
chaque partie demande une réactivation <b>dans les vingt-quatre heures</b>, jamais après.</p>

<h3>Partie A — comment remplir les fiches à trous</h3>
<ol>
<li>Lire la référence biblique dans la Bible, avant toute chose. Le cahier ne remplace pas le texte.</li>
<li>Remplir les blancs <b>sans consulter</b> les fiches de dates. Se tromper est utile : un blanc
faux se corrige, un blanc lu s'oublie.</li>
<li>Ne passer à la fiche suivante qu'après avoir vérifié la précédente sur le corrigé (dernière page).</li>
<li>Écrire la correction <b>en entier</b> à côté du blanc faux. Une correction lue ne corrige rien.</li>
</ol>

<h3>Partie B — comment tenir les fiches d'écoute</h3>
<ol>
<li>Cocher la piste aussitôt après l'écoute, pas à la fin de la collection.</li>
<li>Répondre à la question posée en bas de fiche. Une phrase. Pas plus.</li>
<li>Noter le support ouvert en même temps, si ce n'était pas celui indiqué.</li>
<li>Relire sa phrase le lendemain. C'est la réactivation des vingt-quatre heures.</li>
</ol>

<h3>Partie C — comment porter les cartes</h3>
<ol>
<li>Imprimer la page recto, retourner la feuille, imprimer la page verso. Vérifier sur une
feuille brouillon avant d'imprimer le beau papier.</li>
<li>Découper au massicot ou aux ciseaux, en suivant le cadre.</li>
<li>Ne garder sur soi que <b>quatre cartes</b> : celles des objections que l'on rencontre
réellement. Une carte jamais sortie de la poche ne sert à rien.</li>
<li>Au verso, le lien est écrit en clair : on le recopie, on ne le récite pas de mémoire.</li>
</ol>

<div class="cadre"><b>Ce que ce cahier ne fait pas.</b> Il ne prouve rien, il ne convainc
personne, il ne remplace aucune lecture de la Bible. Il sert à une seule chose : transformer une
écoute en souvenir. Tout le reste appartient à la conversation, qui est toujours une affaire
de personne à personne.</div>

<div class="pied"><span>Cahier de l'auditeur · projet PREUVES</span>
<span>{datetime.date.today().isoformat()} · vague 8</span></div>
</div></div>
"""]

# ---------------------------------------------------------------------------
# PARTIE A
# ---------------------------------------------------------------------------
H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Partie A — Les huit fiches à trous</h1>
<div class="st">Remplir sans consulter. Vérifier ensuite sur le corrigé, à la fin du cahier.</div>
""")
for f in TROUS:
    H.append('<div class="trou">')
    H.append(f'<div class="hd"><div><b>Fiche {f["n"]} / 8</b> — {e(f["theme"])}</div>'
             f'<div class="dt">{e(f["date"])}</div></div>')
    H.append(f'<div class="ref">{e(f["ref"])}</div>')
    for i, (q, r) in enumerate(f["q"], 1):
        H.append(f'<div class="q"><span class="n">{i}.</span><span class="t">{e(q)} '
                 f'<span class="b">&nbsp;</span></span></div>')
    H.append('<div class="q" style="margin-top:9px"><span class="n">▸</span>'
             '<span class="t"><b>Accomplissement, en une phrase :</b></span></div>')
    H.append('<div class="lig"></div><div class="lig"></div>')
    H.append("</div>")
H.append('<div class="pied"><span>Partie A — fiches à trous</span><span>1 page</span></div>')
H.append("</div></div>")

# ---------------------------------------------------------------------------
# PARTIE B
# ---------------------------------------------------------------------------
H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Partie B — Les treize fiches d'écoute</h1>
<div class="st">Une fiche par collection. Cocher la piste aussitôt après l'écoute, puis répondre
à la question du bas. Une phrase suffit.</div>
""")
for n, titre, np, duree, support, quest in ECOUTE:
    H.append('<div class="ec">')
    H.append(f'<div class="hd"><b>C{n:02d} — {e(titre)}</b>'
             f'<span class="m">{np} pistes · {e(duree)}</span></div>')
    H.append(f'<div class="sup">{e(support)}</div>')
    H.append('<div class="list">')
    for k in range(1, np + 1):
        H.append(f'<span class="case"></span> {k}&nbsp;&nbsp;')
    H.append("</div>")
    H.append(f'<div class="qv"><b>Question.</b> {e(quest)}</div>')
    H.append('<div class="lig"></div>')
    H.append("</div>")
H.append('<div class="pied"><span>Partie B — fiches d\'écoute</span><span>1 page</span></div>')
H.append("</div></div>")

# ---------------------------------------------------------------------------
# PARTIE C — recto
# ---------------------------------------------------------------------------
H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Partie C — Les huit cartes d'objection (recto)</h1>
<div class="st">Imprimer cette page, retourner la feuille, imprimer la page suivante.
Découper au cadre. Format poche : 85 × 55 mm.</div>
<div class="cartes">""")
for o in OBJ:
    H.append(f'<div class="carte r"><div><div class="num">Objection {o["n"]}/8 · recto</div>'
             f'<div class="obj">{e(o["obj"])}</div></div>'
             f'<div class="titreC">{e(o["court"])}</div></div>')
H.append("""</div>
<div class="cadre" style="margin-top:12px"><b>Conseil d'impression.</b> Faire un essai sur papier
brouillon pour vérifier le sens du recto-verso avant d'imprimer le beau papier. Les cartes se
découpent ensuite au massicot. On n'en garde que quatre sur soi.</div>
<div class="pied"><span>Partie C — recto</span><span>1 page</span></div>
</div></div>""")

H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Partie C — Les huit cartes d'objection (verso)</h1>
<div class="st">La réponse en trois lignes, puis le lien officiel écrit en clair.</div>
<div class="cartes">""")
for o in OBJ:
    srcs = "<br>".join(e(u) for _, u in o["src"])
    H.append(f'<div class="carte v"><div><div class="num">Objection {o["n"]}/8 · verso</div>'
             f'<div class="rep">{e(o["rep"])}</div></div>'
             f'<div class="src">{srcs}</div></div>')
H.append("""</div>
<div class="pied"><span>Partie C — verso</span><span>1 page</span></div>
</div></div>""")

# ---------------------------------------------------------------------------
# CORRIGE
# ---------------------------------------------------------------------------
H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Corrigé des huit fiches à trous</h1>
<div class="st">À détacher et à ranger séparément, ou à photocopier pour un tiers.
Page volontairement placée à la fin : on ne la consulte qu'après avoir rempli.</div>
<div class="cadre b"><b>Comment utiliser ce corrigé.</b> Ne pas surligner la bonne réponse sans
avoir réécrit la phrase entière à côté du blanc faux. Une correction recopiée de la main reste ;
une correction lue ne laisse aucune trace.</div>""")
for f in TROUS:
    H.append(f'<h3>Fiche {f["n"]} — {e(f["date"])} · {e(f["theme"])}</h3>')
    H.append('<table><thead><tr><th style="width:34px">#</th><th>Blanc</th>'
             '<th style="width:34%">Réponse</th></tr></thead><tbody>')
    for i, (q, r) in enumerate(f["q"], 1):
        H.append(f'<tr><td class="r">{i}</td><td>{e(q)}…</td><td><b>{e(r)}</b></td></tr>')
    H.append("</tbody></table>")
    H.append(f'<p style="font-size:11.5px;color:#5b6472"><b>Pour aller plus loin.</b> {e(f["cor"])}</p>')
H.append('<div class="pied"><span>Corrigé — à détacher</span><span>1 page</span></div>')
H.append("</div></div>")

# ---------------------------------------------------------------------------
# SOURCES
# ---------------------------------------------------------------------------
H.append("""<div class="pg"><div class="flexcol">
<h1 class="t">Sources et rappels</h1>
<div class="st">Ce qui a servi à construire ce cahier, et ce qui reste à vérifier par soi-même.</div>

<h3>Pour aller plus loin — objections voisines</h3>
<div class="src2">""")
for t, u in PLUS:
    H.append(f'<a href="{u}">{e(t)}<br>{e(u)}</a>')
H.append("""</div>

<h3>Les trois précautions, une dernière fois</h3>
<div class="cadre"><b>1. Un seul système chronologique par document.</b> 607 pour la désolation,
539 pour la chute de Babylone (date neutre), 537 pour le retour, 455 pour l'ordre de rebâtir,
29 pour l'onction, 33 pour la mort, 36 pour la fin de la faveur spéciale, 1914 pour la fin des
sept temps. On ne mélange pas les systèmes.</div>
<div class="cadre"><b>2. Aucune date pour l'avenir.</b> Ce qui n'est pas accompli reste sans
date. 1914 marque le début de la conclusion du système de choses, jamais une échéance.</div>
<div class="cadre"><b>3. Aucun total dogmatique.</b> La Bibliothèque en ligne écrit qu'il est
préférable de ne pas se montrer trop affirmatif quant au nombre exact des prophéties
messianiques. On vérifie, on ne compte pas.</div>

<h3>Règles de transmission</h3>
<table><thead><tr><th style="width:24%">Règle</th><th>Application</th></tr></thead><tbody>
<tr><td><b>Un à un</b></td><td>De personne à personne. Jamais de diffusion publique, jamais
d'envoi groupé.</td></tr>
<tr><td><b>Un fichier à la fois</b></td><td>On remet ce qui est demandé. Le dossier entier cesse
d'être lu dès qu'il est complet.</td></tr>
<tr><td><b>Liens officiels seulement</b></td><td>www.jw.org et wol.jw.org. Aucun extrait de
publication n'est recopié, hébergé ni republié.</td></tr>
<tr><td><b>Aucune collecte</b></td><td>Aucune donnée personnelle n'est demandée ni stockée.</td></tr>
<tr><td><b>Aucune date</b></td><td>Ce qui n'est pas accompli n'est jamais daté.</td></tr>
</tbody></table>

<p style="margin-top:16px;font-size:11.5px;color:#5b6472">Généré le """
          f"{datetime.date.today().isoformat()}"
          """ · vague 8 · projet PREUVES. Sources : Bibliothèque en ligne Watchtower
(wol.jw.org) et www.jw.org. Aucun contenu protégé n'est reproduit : les références bibliques
sont citées, les publications ne sont pas recopiées.</p>
<div class="pied"><span>Sources et rappels</span><span>1 page</span></div>
</div></div>
</body></html>""")

out = os.path.join(ROOT, "CAHIER_AUDITEUR.html")
open(out, "w", encoding="utf-8").write("\n".join(H))

print("Fiches à trous :", len(TROUS), "| blancs :", sum(len(f["q"]) for f in TROUS))
print("Fiches d'écoute :", len(ECOUTE))
print("Cartes d'objection :", len(OBJ))
print("CAHIER_AUDITEUR.html :", os.path.getsize(out) // 1024, "Ko")
