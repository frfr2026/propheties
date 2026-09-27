#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vague 4 — VISUELS
Génère, sans aucune ressource externe :
  1. FRISES_CHRONOLOGIQUES.html  — 12 frises (planche graphique + planche de détails tirée du registre)
                                   + annexe « couverture canonique » (66 livres → 1 000 entrées)
  2. DECOUVRIR_PAS_A_PAS.html    — 24 cartes à 3 volets
  3. COFFRET.html                — jaquette, dos de classeur (8), couverture CD, étiquettes, colophon
  4. CARTES_QR.html              — 8 cartes de visite avec QR (liens jw.org / wol.jw.org uniquement)
  5. qr/*.png                    — les QR codes, réutilisables
Sources : 16 à 21 + 23_REGISTRE_PROPHETIES_7.md (registre, 1 000 entrées).
"""
import re, os, base64, io, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
PREUVES = os.path.dirname(ROOT)
OUT = ROOT

FILES = ['16_REGISTRE_PROPHETIES.md', '17_REGISTRE_PROPHETIES_2.md',
         '18_REGISTRE_PROPHETIES_3.md', '19_REGISTRE_PROPHETIES_4.md',
         '20_REGISTRE_PROPHETIES_5.md', '21_REGISTRE_PROPHETIES_6.md',
         '23_REGISTRE_PROPHETIES_7.md']
PART_RE = re.compile(r'^#{1,3}\s*PARTIE\s+(\d+)\s*[—–-]\s*(.+?)\s*$')
ROW_RE = re.compile(r'^\|\s*P(\d{3,4})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$')

LIB_RE = re.compile(r'^LIB[_ ]?\d+\s*$')

# ---------------------------------------------------------------- 1. REGISTRE
entries, parts = [], []
for f in FILES:
    p = os.path.join(PREUVES, f)
    if not os.path.exists(p):
        print('  (absent)', f); continue
    cur_part, cur_sec = '', ''
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        m = PART_RE.match(line)
        if m:
            cur_part = m.group(2).strip(); cur_sec = ''
            if not parts or parts[-1] != cur_part:
                parts.append(cur_part)
            continue
        if line.startswith('## '):
            cur_sec = line[3:].strip(); continue
        r = ROW_RE.match(line)
        if r:
            entries.append({'n': int(r.group(1)), 'ref': html.unescape(r.group(2)),
                            'teneur': html.unescape(r.group(3)), 'accompl': html.unescape(r.group(4)),
                            'statut': html.unescape(r.group(5)), 'part': cur_part, 'sec': cur_sec})
entries.sort(key=lambda e: e['n'])
P = {e['n']: e for e in entries}

def find(key):
    """Retrouve une entrée du registre par sa référence (exacte, préfixe, ou contenu)."""
    for e in entries:
        if e['ref'] == key: return e
    for e in entries:
        if e['ref'].startswith(key): return e
    for e in entries:
        if key in e['ref']: return e
    return None

def esc(t): return html.escape(str(t), quote=False)

def wrap(t, n):
    out, line = [], ''
    for w in t.split():
        if len(line) + len(w) + 1 > n: out.append(line); line = w
        else: line = (line + ' ' + w).strip()
    if line: out.append(line)
    return out

# ---------------------------------------------------------------- 2. FRISES
# (clé de référence dans le registre, datation, libellé court)
FRISES = [
 ("FRISE 1", "DE LA PROMESSE AUX ANCÊTRES", "vers 1657 av. n. è. et avant",
  "La promesse d'Éden, puis les promesses faites aux ancêtres — chacune datée, chacune vérifiable dans le texte.",
  [("Genèse 3:15", "à Éden", "Une postérité écrasera la tête du serpent"),
   ("Genèse 9:25-27", "après le déluge", "Canaan asservi ; Sem béni ; Japhet élargi"),
   ("Genèse 12:2, 3", "1943 av. n. è.", "Grande nation, nom grand, bénédiction pour toutes les familles"),
   ("Genèse 13:14-17", "1943 av. n. è.", "La terre donnée à sa postérité, pour toujours"),
   ("Genèse 15:13-14", "1933 av. n. è.", "400 ans de servitude, puis la sortie avec de grands biens"),
   ("Genèse 15:16", "1933 av. n. è.", "Retour à la quatrième génération"),
   ("Genèse 17:19-21", "1919 av. n. è.", "Isaac héritier de l'alliance ; Ismaël béni et multiplié"),
   ("Genèse 18:10, 14", "1918 av. n. è.", "Sara enfantera au temps fixé, l'année suivante"),
   ("Genèse 25:23", "1858 av. n. è.", "L'aîné servira le plus jeune"),
   ("Genèse 27:27-29", "avant 1728", "Nations et peuples serviront Jacob"),
   ("Genèse 46:3, 4", "1728 av. n. è.", "Jacob descendra en Égypte ; Dieu l'en fera remonter"),
   ("Genèse 48:19", "vers 1711", "Éphraïm deviendra une multitude de nations"),
   ("Genèse 49:8-12", "1711 av. n. è.", "Le sceptre ne s'éloignera pas de Juda"),
   ("Genèse 49:22-26", "1711 av. n. è.", "Bénédiction de Joseph : le rocher d'Israël le bénira"),
   ("Genèse 50:24, 25", "1657 av. n. è.", "Dieu vous fera remonter ; emportez mes ossements")]),

 ("FRISE 2", "DE L'ÉGYPTE À LA TERRE PROMISE", "1513 – 1473 av. n. è.",
  "La sortie d'Égypte annoncée à Abram, puis les promesses du désert et de la conquête.",
  [("Exode 3:12", "1513 av. n. è.", "Vous servirez Dieu sur cette montagne : le signe est donné"),
   ("Exode 6:2-8", "1513 av. n. è.", "Je vous ferai sortir ; je vous prendrai pour mon peuple"),
   ("Exode 9:16", "1513 av. n. è.", "Pour annoncer mon nom par toute la terre"),
   ("Exode 12:12, 13", "1513 av. n. è.", "Je passerai sur l'Égypte ; le sang sera un signe"),
   ("Exode 14:4", "1513 av. n. è.", "Pharaon poursuivra ; je me glorifierai contre lui"),
   ("Exode 19:5, 6", "1513 av. n. è.", "Royaume de prêtres, nation sainte"),
   ("Nombres 14:26-35", "1513 av. n. è.", "Quarante ans dans le désert, puis l'entrée dans le pays"),
   ("Nombres 24:17-19", "1473 av. n. è.", "Une étoile sortira de Jacob"),
   ("Deutéronome 18:15-19", "1473 av. n. è.", "Un prophète comme Moïse : écoutez-le"),
   ("Deutéronome 28:15-68", "1473 av. n. è.", "Les malédictions de l'infidélité : la dispersion"),
   ("Deutéronome 30:1-10", "1473 av. n. è.", "Après la dispersion, le rassemblement"),
   ("Deutéronome 31:16-21", "1473 av. n. è.", "Le cantique témoin contre un peuple infidèle"),
   ("Josué 6:26", "vers 1473", "Maudit l'homme qui rebâtira Jéricho"),
   ("Josué 23:14-16", "vers 1450", "Aucune promesse n'est restée sans effet — mais l'infidélité coûtera")]),

 ("FRISE 3", "LES JUGES ET LA ROYAUTÉ", "vers 1450 – 997 av. n. è.",
  "Du temps des juges à la division du royaume : un nom annoncé trois siècles à l'avance.",
  [("Juges 1:1, 2", "vers 1450", "Juda montera ; le pays est livré en sa main"),
   ("Juges 2:1-3", "vers 1450", "Les nations ne seront pas dépossédées : elles seront un piège"),
   ("Juges 6:14-16", "vers 1160", "Gédéon délivrera Israël de Madian"),
   ("Juges 13:3-5", "vers 1140", "Un fils naziréen sauvera Israël des Philistins"),
   ("1 Samuel 2:27-36", "vers 1110", "La maison d'Éli jugée ; un prêtre fidèle se lèvera"),
   ("1 Samuel 3:11-14", "vers 1110", "Le jugement ne sera pas effacé"),
   ("1 Samuel 13:13, 14", "1117 av. n. è.", "La royauté ne subsistera pas : un homme selon le cœur de Dieu"),
   ("1 Samuel 15:28", "1117 av. n. è.", "Le royaume est donné à un autre, meilleur que toi"),
   ("2 Samuel 7:8-16", "règne de David", "Ton trône sera affermi pour des temps indéfinis"),
   ("2 Samuel 12:10-12", "règne de David", "L'épée ne s'éloignera pas de ta maison"),
   ("1 Rois 9:3-9", "vers 1027", "Le temple et le pays : condition d'obéissance, sinon l'exil"),
   ("1 Rois 11:29-39", "997 av. n. è.", "Ahija annonce la division : dix tribus arrachées"),
   ("1 Rois 13:2-5", "997 av. n. è.", "Josias est nommé trois siècles avant sa naissance"),
   ("1 Rois 14:6-16", "997 av. n. è.", "Israël arraché à cause de Jéroboam"),
   ("1 Rois 17:1", "règne d'Achab", "La sécheresse annoncée par Élie"),
   ("2 Rois 8:10-13", "vers 890", "Hazaël, roi de Syrie, fera du mal à Israël"),
   ("2 Rois 19:32-34", "732 av. n. è.", "Le roi d'Assyrie n'entrera pas dans cette ville"),
   ("2 Rois 20:5, 6", "732 av. n. è.", "Quinze années ajoutées ; la ville délivrée"),
   ("2 Rois 20:16-18", "732 av. n. è.", "Tout sera emporté à Babylone : les fils deviendront serviteurs")]),

 ("FRISE 4", "LES PROPHÈTES DU VIIIe SIÈCLE", "vers 844 – 732 av. n. è.",
  "Ninive, Samarie, Damas, l'Assyrie : deux siècles de prophéties datées, ville par ville.",
  [("Jonas 3:4", "vers 844 av. n. è.", "Ninive sera renversée dans quarante jours"),
   ("Amos 2:6-16", "vers 804 av. n. è.", "Israël vendu pour de l'argent : je vous opprimerai"),
   ("Amos 4:1-13", "vers 804 av. n. è.", "Prépare-toi à rencontrer ton Dieu, ô Israël"),
   ("Amos 5:1-27", "vers 804 av. n. è.", "Vous irez en exil au-delà de Damas"),
   ("Amos 7:10-17", "vers 804 av. n. è.", "Amos : le pays sera exilé ; ta femme sera une prostituée dans la ville"),
   ("Amos 8:1-10", "vers 804 av. n. è.", "La fin est venue : je ne passerai plus devant mon peuple"),
   ("Amos 9:1-15", "vers 804 av. n. è.", "Captifs, mais je relèverai la hutte de David"),
   ("Osée 1:4, 5", "vers 745 av. n. è.", "Je briserai l'arc d'Israël dans la vallée de Yizréel"),
   ("Osée 1:9-11", "vers 745 av. n. è.", "Vous n'êtes pas mon peuple ; puis ils seront appelés fils du Dieu vivant"),
   ("Osée 8:1-14", "vers 740 av. n. è.", "Ils rentreront en Égypte : les forteresses dévorées"),
   ("Osée 9:1-17", "vers 740 av. n. è.", "Éphraïm retournera en Égypte ; vagabonds parmi les nations"),
   ("Osée 10:1-15", "vers 740 av. n. è.", "Le roi de Samarie sera emporté comme l'écume sur l'eau"),
   ("Osée 14:1-9", "vers 740 av. n. è.", "Revenez : je guérirai leur infidélité"),
   ("Isaïe 7:8", "vers 736 av. n. è.", "Dans soixante-cinq ans Éphraïm sera brisé"),
   ("Isaïe 7:14", "vers 735 av. n. è.", "La jeune femme concevra et enfantera un fils"),
   ("Isaïe 8:1-4", "vers 734 av. n. è.", "Avant que l'enfant sache dire mon père : butin de Damas et de Samarie"),
   ("Isaïe 10:5-19", "après 740", "L'Assyrie, bâton de ma colère, sera à son tour brisée"),
   ("Michée 1:10-16", "vers 716 av. n. è.", "Samarie dévastée ; l'héritage mesuré au cordeau"),
   ("Michée 3:1-12", "vers 716 av. n. è.", "Sion sera labourée comme un champ"),
   ("Michée 5:2", "vers 716 av. n. è.", "De Bethléem sortira celui qui doit être chef en Israël")]),

 ("FRISE 5", "AVANT LA CHUTE DE JÉRUSALEM", "vers 732 – 607 av. n. è.",
  "Israël tombé, l'Assyrie brisée, Babylone nommée : les autres nations sont nommées et datées une à une.",
  [("Isaïe 13:1-22", "vers 732 av. n. è.", "Babylone, la beauté des royaumes, comme Sodome"),
   ("Isaïe 14:4-23", "vers 732 av. n. è.", "Tu seras un rejeton odieux : ton pays, ton peuple"),
   ("Isaïe 19:1-17", "vers 716 av. n. è.", "L'Égypte livrée à un maître dur"),
   ("Isaïe 21:1-10", "vers 700 av. n. è.", "Babylone est tombée, tombée !"),
   ("Isaïe 22:1-25", "vers 700 av. n. è.", "Jérusalem : la brèche de la ville de David est fréquente"),
   ("Isaïe 23:1-18", "vers 700 av. n. è.", "Tyr : votre forteresse démolie, jamais relevée comme avant"),
   ("Isaïe 37:6, 7, 33-35", "732 av. n. è.", "Sennachérib rentrera dans son pays par l'épée"),
   ("Isaïe 38:1-8", "732 av. n. è.", "Quinze années de plus ; la ville délivrée de sa main"),
   ("Isaïe 39:5-7", "732 av. n. è.", "Tout ce qui est dans ta maison ira à Babylone"),
   ("Isaïe 40:1-11", "vers 732 av. n. è.", "Une voix crie dans le désert : préparez le chemin"),
   ("Isaïe 43:5-7", "vers 732 av. n. è.", "Je ferai revenir ta descendance du pays du levant et du couchant"),
   ("Isaïe 44:24-28", "vers 732 av. n. è.", "Cyrus : mon berger accomplira tout mon plaisir"),
   ("Isaïe 45:1-7", "vers 732 av. n. è.", "Le nom, la fonction et la politique du libérateur"),
   ("Isaïe 46:1, 2", "vers 732 av. n. è.", "Bel plie, Nébo s'incline : les dieux de Babylone emportés"),
   ("Isaïe 47:1-15", "vers 732 av. n. è.", "Descends t'asseoir dans la poussière, vierge, fille de Babylone"),
   ("Isaïe 53:1-12", "vers 732 av. n. è.", "Le Serviteur : méprisé, transpercé, mis au nombre des transgresseurs"),
   ("Sophonie 2:4-7", "vers 648 av. n. è.", "Gaza, Askalon, Ékron, Ashdod : la côte abandonnée"),
   ("Sophonie 2:12-15", "vers 648 av. n. è.", "Ninive : la ville dévastée, sans habitant"),
   ("Nahum 2:1-10", "vers 632 av. n. è.", "Les portes du fleuve s'ouvrent ; le palais est ébranlé"),
   ("Nahum 3:1-7", "vers 632 av. n. è.", "Malheur à la ville de sang : je relèverai tes jupes sur ton visage"),
   ("Habacuc 1:5-11", "vers 628 av. n. è.", "Je suscite les Chaldéens, nation amère et impétueuse"),
   ("Habacuc 2:1-4", "vers 628 av. n. è.", "La vision attend son temps fixé : elle ne mentira pas"),
   ("Joël 2:1-11", "vers 640 av. n. è.", "Jour de ténèbres : un peuple nombreux et fort monte sur le pays"),
   ("Joël 3:9-17", "vers 640 av. n. è.", "Que les nations montent dans la vallée de Yehoshaphat")]),

 ("FRISE 6", "JÉRÉMIE, TÉMOIN DE LA CHUTE", "vers 647 – 580 av. n. è.",
  "Quarante ans d'avertissements datés, la nuit de Babylone, puis la promesse d'un retour fixé à soixante-dix ans.",
  [("Jérémie 1:13-16", "vers 647 av. n. è.", "Le chaudron incliné : le mal vient du nord"),
   ("Jérémie 4:5-8", "vers 647 av. n. è.", "Je fais venir le malheur du nord : la lionne est partie"),
   ("Jérémie 6:1-5", "vers 647 av. n. è.", "Le mal se penche du nord sur Jérusalem"),
   ("Jérémie 6:22-26", "vers 647 av. n. è.", "Un peuple vient du pays du nord : l'angoisse te saisira"),
   ("Jérémie 7:30-34", "vers 647 av. n. è.", "Ils ont bâti les hauts lieux de Topheth"),
   ("Jérémie 13:18, 19", "vers 619 av. n. è.", "Votre splendeur descendra : les villes du sud fermées"),
   ("Jérémie 20:1-6", "vers 617 av. n. è.", "Pashhur : captivité à Babylone, toi et ta maison"),
   ("Jérémie 21:1-10", "vers 609 av. n. è.", "Je livre cette ville en la main du roi de Babylone"),
   ("Jérémie 22:24-30", "vers 609 av. n. è.", "Yekonia : je t'arracherai, comme une bague"),
   ("Jérémie 24:1-10", "vers 609 av. n. è.", "Deux corbeilles de figues : les exilés, la cible"),
   ("Jérémie 25:1-11", "vers 605 av. n. è.", "Soixante-dix ans de service du roi de Babylone"),
   ("Jérémie 25:12-14", "vers 605 av. n. è.", "Quand les soixante-dix ans seront accomplis, je le punirai"),
   ("Jérémie 27:1-11", "vers 617 av. n. è.", "Mettez votre cou dans le joug du roi de Babylone"),
   ("Jérémie 28:1-17", "vers 617 av. n. è.", "Hanania mourra ; les vases iront à Babylone"),
   ("Jérémie 29:1-14", "vers 617 av. n. è.", "Soixante-dix ans : autant de temps que j'ai de pensées de paix"),
   ("Jérémie 32:6-15", "vers 607 av. n. è.", "Achète le champ d'Anathoth : on achètera encore dans ce pays"),
   ("Jérémie 34:1-7", "vers 607 av. n. è.", "Tu mourras en paix ; Jérusalem prise par le roi de Babylone"),
   ("Jérémie 36:1-3, 27-32", "vers 605 av. n. è.", "Le rouleau brûlé par Yoaqim est réécrit, avec davantage"),
   ("Jérémie 39:15-18", "vers 607 av. n. è.", "Ébed-Mélek ne sera pas livré : sa vie sera un butin"),
   ("Jérémie 43:8-13", "vers 607 av. n. è.", "Nabuchodonosor dressera son trône sur les pierres de Tahpanhès"),
   ("Jérémie 50:1-3", "vers 605 av. n. è.", "Une nation vient du nord qui fera de Babylone une désolation"),
   ("Jérémie 51:59-64", "vers 605 av. n. è.", "Babylone s'enfoncera et ne se relèvera pas"),
   ("Lamentations 2:15-17", "607 av. n. è.", "Il a exécuté sa parole, comme il l'avait décidé"),
   ("Lamentations 4:21, 22", "607 av. n. è.", "Édom : la coupe passera aussi vers toi")]),

 ("FRISE 7", "ÉZÉCHIEL, PROPHÈTE DE L'EXIL", "613 – 591 av. n. è.",
  "Des prophéties datées au jour près, rédigées à des centaines de kilomètres de Jérusalem.",
  [("Ézéchiel 4:1-8", "613 av. n. è.", "Le siège de Jérusalem figuré sur une brique : 390 puis 40 jours"),
   ("Ézéchiel 4:9-17", "613 av. n. è.", "Ration de famine : dix-huit pâtisseries d'orge par jour"),
   ("Ézéchiel 5:1-17", "612 av. n. è.", "Le rasoir : un tiers par l'épée, un tiers dans le feu"),
   ("Ézéchiel 7:1-27", "612 av. n. è.", "La fin est venue sur les quatre extrémités du pays"),
   ("Ézéchiel 8:1-18", "612 av. n. è.", "Les abominations dans le temple ; la gloire se retire"),
   ("Ézéchiel 11:16-21", "vers 612 av. n. è.", "Je vous rassemblerai : je mettrai en vous un cœur nouveau"),
   ("Ézéchiel 12:1-16", "611 av. n. è.", "Le bagage de l'exilé : la figure du départ de Sédécias"),
   ("Ézéchiel 17:1-24", "vers 611 av. n. è.", "Les deux grands aigles ; le cèdre tendre planté sur la montagne"),
   ("Ézéchiel 19:1-14", "vers 611 av. n. è.", "Les lionceaux de la mère lionne emmenés en Égypte et à Babylone"),
   ("Ézéchiel 21:1-32", "vers 611 av. n. è.", "L'épée du roi de Babylone : il tire au sort Jérusalem"),
   ("Ézéchiel 22:1-31", "vers 611 av. n. è.", "La ville de sang meurtrie dans ses propres murailles"),
   ("Ézéchiel 24:1-14", "589 av. n. è.", "Le chaudron : le mois même où le siège commence"),
   ("Ézéchiel 24:15-27", "589 av. n. è.", "La mort de sa femme : un signe pour les exilés"),
   ("Ézéchiel 26:1-6", "588 av. n. è.", "Tyr : je rassemblerai ses pierres, son bois, sa poussière"),
   ("Ézéchiel 26:12-14", "588 av. n. è.", "Un lieu pour étendre les filets : rasée comme le sommet d'un rocher"),
   ("Ézéchiel 29:1-16", "588 av. n. è.", "L'Égypte dévastée quarante ans, dispersée parmi les nations"),
   ("Ézéchiel 33:21-29", "607 av. n. è.", "Le rescapé annonce la prise de la ville : prophétie datée à l'octobre"),
   ("Ézéchiel 37:1-14", "593 av. n. è.", "Les ossements desséchés : je vous ramènerai dans votre pays"),
   ("Ézéchiel 38:1-23", "vers 591 av. n. è.", "Gog de Magog : l'assaut final contre le peuple rassemblé"),
   ("Ézéchiel 40:1-48:35", "593 av. n. è.", "Le temple et la ville : « Jéhovah est là »")]),

 ("FRISE 8", "DANIEL ET LES EMPIRES", "618 – 536 av. n. è.",
  "Quatre empires nommés par un seul mot de métal, puis deux cent trente années de querelles nommées par leur lieu.",
  [("Daniel 1:1-7", "618 av. n. è.", "La première déportation : des jeunes gens formés à Babylone"),
   ("Daniel 1:17-21", "617 av. n. è.", "Daniel resta jusqu'à la première année de Cyrus"),
   ("Daniel 2:1-43", "vers 603 av. n. è.", "La statue : or, argent, airain, fer, fer et argile"),
   ("Daniel 2:34, 35, 44, 45", "vers 603 av. n. è.", "La pierre qui brise la statue et devient une montagne"),
   ("Daniel 4:10-27", "vers 606 av. n. è.", "Le grand arbre : abattu, un bandeau de fer, sept temps"),
   ("Daniel 4:31, 32", "vers 606 av. n. è.", "Nabuchodonosor déchu, les cheveux comme les plumes de l'aigle"),
   ("Daniel 5:5-28", "5 octobre 539 av. n. è.", "La main sur le mur : mené, pesé, divisé"),
   ("Daniel 5:23, 24", "5 octobre 539 av. n. è.", "Le roi a exalté les dieux d'argent et d'or : sa fin est là"),
   ("Daniel 6:24", "vers 537 av. n. è.", "Les accusateurs jetés dans la fosse aux lions"),
   ("Daniel 7:1-7", "vers 553 av. n. è.", "Quatre bêtes : lionne, ours, léopard, bête à dix cornes"),
   ("Daniel 7:8, 24-26", "vers 553 av. n. è.", "La petite corne qui dompte trois cornes et parle contre le Très-Haut"),
   ("Daniel 7:9-14", "vers 553 av. n. è.", "Le Fils de l'homme reçoit domination, gloire et royaume"),
   ("Daniel 8:1-8, 20, 21", "vers 551 av. n. è.", "Le bélier médo-perse et le bouc grec aux quatre cornes"),
   ("Daniel 8:9-14, 23-25", "vers 551 av. n. è.", "La corne insolente ; deux mille trois cents soirs et matins"),
   ("Daniel 9:24-27", "539 av. n. è.", "Les soixante-dix semaines : soixante-deux puis une semaine"),
   ("Daniel 10:12-14", "537 av. n. è.", "Le prince du royaume de Perse ; Michel, votre prince"),
   ("Daniel 11:2", "537 av. n. è.", "Trois rois de Perse, puis un quatrième riche de tout"),
   ("Daniel 11:3", "537 av. n. è.", "Un roi vaillant : le bouc d'Alexandre"),
   ("Daniel 11:5", "537 av. n. è.", "Le roi du midi et un prince du nord"),
   ("Daniel 11:10-13", "537 av. n. è.", "Les armées montées et descendues : Antiochus III"),
   ("Daniel 11:11, 12", "217 av. n. è.", "La bataille de Raphia : le roi du midi frappe"),
   ("Daniel 11:21-24", "vers 175 av. n. è.", "Le méprisé : Antiochus IV, dans la paix, s'empare du royaume"),
   ("Daniel 11:31-35", "vers 167 av. n. è.", "La chose immonde qui cause la désolation ; les sages purifiés"),
   ("Daniel 12:1", "temps de la fin", "Michel se lèvera : un temps de détresse tel qu'il n'en fut pas"),
   ("Daniel 12:2, 3", "temps de la fin", "Beaucoup se réveilleront : les uns pour la vie, les autres pour l'opprobre"),
   ("Daniel 12:4, 9", "temps de la fin", "La vraie connaissance deviendra abondante ; le livre scellé"),
   ("Daniel 12:7, 11, 12", "1 260 · 1 290 · 1 335 jours", "Trois durées annoncées et datées dans les publications")]),

 ("FRISE 9", "LE RETOUR ET LA RECONSTRUCTION", "537 – 455 av. n. è.",
  "Le décret de Cyrus, l'autel relevé, le temple rebâti, la muraille et la semaine des soixante-dix semaines.",
  [("2 Chroniques 36:20-21", "607 – 537 av. n. è.", "Le pays a payé ses sabbats jusqu'à la restauration de soixante-dix ans"),
   ("Esdras 1:1-4", "537 av. n. è.", "Le décret de Cyrus : que le peuple remonte"),
   ("Néhémie 1:8, 9", "vers 456 av. n. è.", "Je vous rassemblerai malgré l'exil lointain"),
   ("Aggée 1:2-11", "520 av. n. è.", "La maison est en ruine ; c'est pourquoi je retiens la rosée"),
   ("Aggée 1:12-15", "520 av. n. è.", "Zorobabel et Josué raniment le peuple"),
   ("Aggée 2:1-9", "520 av. n. è.", "La gloire de cette maison sera plus grande que la première"),
   ("Aggée 2:20-23", "520 av. n. è.", "Zorobabel, mon serviteur : je te ferai comme un sceau"),
   ("Zacharie 1:7-17", "519 av. n. è.", "Les soixante-dix ans : ma colère est tombée ; je reviens à Jérusalem"),
   ("Zacharie 2:1-13", "519 av. n. è.", "Le cordeau à mesurer : Jérusalem habitée comme les villes sans muraille"),
   ("Zacharie 3:1-10", "519 av. n. è.", "Le grand prêtre Josué : le turban purifié, le Germe"),
   ("Zacharie 4:1-14", "519 av. n. è.", "Le chandelier et les deux oints : ce n'est pas par la force"),
   ("Zacharie 6:9-15", "519 av. n. è.", "Le Germe bâtira le temple et siégera sur le trône"),
   ("Zacharie 8:1-17", "518 av. n. è.", "Les places de la ville seront remplies de garçons et de filles"),
   ("Zacharie 8:18-23", "518 av. n. è.", "Dix hommes de toutes les langues saisiront le pan de la robe d'un Juif"),
   ("Zacharie 9:9", "vers 518 av. n. è.", "Ton roi vient, humble et monté sur un âne"),
   ("Zacharie 11:12, 13", "vers 518 av. n. è.", "Trente pièces d'argent jetées dans la maison de Jéhovah"),
   ("Zacharie 12:10-14", "vers 518 av. n. è.", "Ils regarderont vers celui qu'ils ont transpercé"),
   ("Zacharie 13:1-9", "vers 518 av. n. è.", "Une source pour le péché ; le berger frappé, les brebis dispersées"),
   ("Zacharie 14:1-21", "vers 518 av. n. è.", "Le jour de Jéhovah : ses pieds sur le mont des Oliviers"),
   ("Malachie 1:2-5", "vers 460 av. n. è.", "J'ai aimé Jacob ; Édom foulé hors des frontières"),
   ("Malachie 3:1-6", "vers 460 av. n. è.", "J'envoie mon messager : il préparera le chemin"),
   ("Malachie 4:1-6", "vers 460 av. n. è.", "Le jour qui brûle comme un four ; Élie avant ce jour")]),

 ("FRISE 10", "LES PSAUMES ET LES ÉCRITS : LA TRAME MESSIANIQUE", "vers 1070 – 460 av. n. è.",
  "Des siècles de chant, et des détails qui se recoupent : les mains, les pieds, les vêtements, les os.",
  [("Psaume 2:1-6", "vers 1040", "Les rois de la terre se rassemblent contre Jéhovah et contre son oint"),
   ("Psaume 2:7", "vers 1040", "Tu es mon fils : aujourd'hui je suis devenu ton père"),
   ("Psaume 8:4-8", "vers 1040", "Tout est mis sous ses pieds : brebis, bœufs, bêtes des champs"),
   ("Psaume 16:8-11", "vers 1040", "Tu ne permettras pas que ton fidèle voie la fosse"),
   ("Psaume 22:1", "vers 1040", "Mon Dieu, pourquoi m'as-tu abandonné ?"),
   ("Psaume 22:6-8", "vers 1040", "Il s'est confié à Jéhovah : que Jéhovah le délivre"),
   ("Psaume 22:14-16", "vers 1040", "Mes os se sont disjoints ; ma force s'est desséchée comme un tesson"),
   ("Psaume 22:17, 18", "vers 1040", "Ils se partagent mes vêtements ; ils tirent au sort ma tunique"),
   ("Psaume 34:20", "vers 1040", "Aucun de ses os ne sera brisé"),
   ("Psaume 35:11-19", "vers 1040", "Des témoins violents se lèvent : ils me rendent le mal pour le bien"),
   ("Psaume 40:6-8", "vers 1040", "Tu m'as creusé des oreilles : voici, je viens"),
   ("Psaume 41:9", "vers 1040", "Celui qui mangeait mon pain a levé le talon contre moi"),
   ("Psaume 55:12-14", "vers 1040", "Ce n'est pas un ennemi qui m'outrage, mais toi, mon compagnon"),
   ("Psaume 68:18", "vers 1040", "Tu es monté en haut : tu as emmené des captifs"),
   ("Psaume 69:4", "vers 1040", "Ils me haïssent sans cause"),
   ("Psaume 69:9", "vers 1040", "Le zèle de ta maison me dévore"),
   ("Psaume 69:21", "vers 1040", "Dans ma soif, ils m'ont donné du vinaigre"),
   ("Psaume 69:22-28", "vers 1040", "Que leur table devienne un piège ; que leur camp soit dévasté"),
   ("Psaume 78:2", "vers 1040", "J'ouvrirai ma bouche par des proverbes, je dirai les énigmes des temps anciens"),
   ("Psaume 89:3, 4, 35-37", "vers 1040", "Sa descendance durera pour toujours comme le soleil"),
   ("Psaume 109:8", "vers 1040", "Qu'un autre prenne sa charge"),
   ("Psaume 110:1", "vers 1040", "Assieds-toi à ma droite, jusqu'à ce que je fasse de tes ennemis ton marchepied"),
   ("Psaume 110:4", "vers 1040", "Tu es prêtre pour toujours à la manière de Melkisédec"),
   ("Psaume 118:22, 23", "vers 1040", "La pierre que les bâtisseurs ont rejetée est devenue la tête de l'angle"),
   ("Psaume 132:11", "vers 1040", "Du fruit de tes entrailles je mettrai sur ton trône"),
   ("Job 14:13-15", "vers 1473", "Tu appelleras et je te répondrai : tu désireras l'œuvre de tes mains"),
   ("Proverbes 30:4", "vers 717", "Qui est monté au ciel et en est descendu ? Quel est son nom et le nom de son fils ?"),
   ("Cantique des Cantiques 3:11 ; 6:9 ; 8:6, 7", "vers 1020", "L'amour est aussi dur que la mort : ses flammes sont un feu")]),

 ("FRISE 11", "LE CHRIST : DE LA NAISSANCE AU RÈGNE", "2 av. n. è. – 33 de n. è.",
  "Naissance, ministère, procès, mort et résurrection : la partie la plus dense du registre, en trois ans et demi.",
  [("Isaïe 7:14", "vers 2 av. n. è.", "La jeune femme enfantera : on l'appellera Emmanuel"),
   ("Michée 5:2", "vers 2 av. n. è.", "Toi, Bethléem : de toi sortira celui qui doit être chef"),
   ("Jérémie 31:15-17", "vers 2 av. n. è.", "Rachel pleure ses fils ; ils reviendront du pays de l'ennemi"),
   ("Osée 11:1", "vers 2 av. n. è.", "D'Égypte j'ai appelé mon fils"),
   ("Isaïe 9:1, 2", "vers 2 av. n. è.", "Le peuple qui marchait dans les ténèbres a vu une grande lumière"),
   ("Malachie 3:1", "29 de n. è.", "J'envoie mon messager : il préparera le chemin devant moi"),
   ("Isaïe 40:1-11", "29 de n. è.", "Une voix crie dans le désert : préparez le chemin de Jéhovah"),
   ("Isaïe 61:1-3", "29 de n. è.", "L'esprit de Jéhovah est sur moi : il m'a oint pour annoncer la bonne nouvelle"),
   ("Isaïe 42:1-4", "29 de n. è.", "Voici mon serviteur : il ne brisera pas le roseau froissé"),
   ("Isaïe 35:5,6", "30 de n. è.", "Les yeux des aveugles s'ouvriront, les oreilles des sourds s'ouvriront"),
   ("Isaïe 53:4", "30 de n. è.", "Il a porté nos maladies : les démons sortent à sa parole"),
   ("Zacharie 9:9", "33 de n. è.", "Ton roi vient, humble, monté sur un âne"),
   ("Daniel 9:24-27", "33 de n. è.", "La moitié de la dernière semaine : le Messie retranché"),
   ("Psaume 41:9", "33 de n. è.", "Celui qui mangeait mon pain a levé le talon contre moi"),
   ("Psaume 22:17, 18", "33 de n. è.", "Ils se partagent mes vêtements"),
   ("Psaume 34:20", "33 de n. è.", "Aucun de ses os ne sera brisé"),
   ("Exode 12:46", "33 de n. è.", "Aucun os de l'agneau pascal ne sera brisé"),
   ("Isaïe 53:9", "33 de n. è.", "Son tombeau est assigné avec les méchants, mais il est avec le riche"),
   ("Isaïe 53:12", "33 de n. è.", "Il a été mis au nombre des transgresseurs : il a intercédé"),
   ("Psaume 16:8-11", "33 de n. è.", "Tu ne permettras pas que ton fidèle voie la fosse"),
   ("Psaume 110:1", "33 de n. è.", "Assieds-toi à ma droite : ennemis pour marchepied"),
   ("Daniel 7:13,14", "33 de n. è.", "Le Fils de l'homme reçoit domination et royaume indéfinis")]),

 ("FRISE 12", "DEPUIS 1914 : CE QUI EST EN COURS, CE QUI VIENT", "1914 – aujourd'hui",
  "Les prophéties que le registre tient pour en cours : le signe composite, la prédication, et ce qui reste à venir.",
  [("Daniel 4:31, 32", "octobre 1914", "Les sept temps : de 607 av. n. è. à 1914 — le calcul publié, étape par étape"),
   ("Luc 21:24", "1914 – aujourd'hui", "Jérusalem foulée par les nations jusqu'à ce que les temps soient accomplis"),
   ("Matthieu 24:6,7", "1914 – aujourd'hui", "Guerre et rumeurs de guerre : nation contre nation"),
   ("Matthieu 24:7", "1914 – aujourd'hui", "Disettes et tremblements de terre en divers lieux"),
   ("Matthieu 24:12", "1914 – aujourd'hui", "L'accroissement de l'illégalité et le refroidissement de l'amour"),
   ("Matthieu 24:14", "1914 – aujourd'hui", "Cette bonne nouvelle du Royaume prêchée dans toute la terre habitée"),
   ("Matthieu 24:21,22", "à venir", "Une grande tribulation telle qu'il n'en est pas survenue"),
   ("Matthieu 24:45-47", "en cours", "L'esclave fidèle établi sur tous ses biens"),
   ("Matthieu 25:31-33", "en cours", "La séparation des brebis et des chèvres"),
   ("Luc 21:31", "en cours", "Quand vous verrez ces choses, sachez que le Royaume est proche"),
   ("Actes 1:8", "33 – aujourd'hui", "Témoins jusqu'à la partie la plus lointaine de la terre"),
   ("2 Timothée 3:1-5", "1914 – aujourd'hui", "Les derniers jours : vingt traits de caractère"),
   ("Révélation 12:7-9", "après 1914", "La guerre dans le ciel : le dragon précipité"),
   ("Révélation 12:10-12", "après 1914", "Malheur à la terre : le diable sait qu'il a peu de temps"),
   ("Révélation 13:16,17", "en cours", "La marque de la bête sauvage : acheter et vendre"),
   ("Révélation 17:12-14", "en cours / à venir", "Dix rois livrent leur puissance à la bête : ils font la guerre à l'Agneau"),
   ("Révélation 18:6-8", "à venir", "Babylone la Grande : en un seul jour ses fléaux"),
   ("Révélation 19:11", "à venir", "Le cavalier au cheval blanc et son armée céleste"),
   ("Révélation 20:1-3", "à venir", "Le dragon lié pour mille ans"),
   ("Révélation 20:4", "à venir", "Ceux qui viennent à la vie et règnent avec le Christ mille ans"),
   ("Révélation 21:3", "à venir", "La tente de Dieu avec les humains : il habitera avec eux"),
   ("Révélation 21:4", "à venir", "Il essuiera toute larme : ni mort, ni deuil, ni cri, ni douleur"),
   ("Révélation 22:1,2", "à venir", "Le fleuve d'eau de vie et les arbres pour la guérison des nations")]),
]

# ---------------------------------------------------------------- 3. ANNEXE CANONIQUE
BOOKS = ["Genèse","Exode","Lévitique","Nombres","Deutéronome","Josué","Juges","Ruth","1 Samuel","2 Samuel",
 "1 Rois","2 Rois","1 Chroniques","2 Chroniques","Esdras","Néhémie","Esther","Job","Psaume","Proverbes",
 "Ecclésiaste","Cantique des Cantiques","Isaïe","Jérémie","Lamentations","Ézéchiel","Daniel","Osée","Joël",
 "Amos","Abdias","Jonas","Michée","Nahum","Habacuc","Sophonie","Aggée","Zacharie","Malachie","Matthieu",
 "Marc","Luc","Jean","Actes","Romains","1 Corinthiens","2 Corinthiens","Galates","Éphésiens","Philippiens",
 "Colossiens","1 Thessaloniciens","2 Thessaloniciens","1 Timothée","2 Timothée","Tite","Philémon","Hébreux",
 "Jacques","1 Pierre","2 Pierre","1 Jean","2 Jean","3 Jean","Jude","Révélation"]
NO_PROPH = {"Esther", "Philémon", "2 Jean", "3 Jean"}

def book_of(ref):
    best = None
    for b in BOOKS:
        if ref.startswith(b) and (best is None or len(b) > len(best)): best = b
    return best

cover = {b: [] for b in BOOKS}
for e in entries:
    b = book_of(e['ref'])
    if b: cover[b].append(e)
distinct = {}
for b in BOOKS:
    distinct[b] = len(set((e['ref'], e['teneur']) for e in cover[b]))

# ---------------------------------------------------------------- 4. QR
QR_URLS = [
 ("Accueil officiel", "https://www.jw.org/fr/"),
 ("Bibliothèque en ligne", "https://wol.jw.org/fr/wol/h/r30/lp-f"),
 ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
 ("La Bible et la science", "https://www.jw.org/fr/la-bible-et-vous/science/"),
 ("Cours biblique", "https://www.jw.org/fr/la-bible-et-vous/cours-biblique-particulier/"),
 ("Demandez une visite", "https://www.jw.org/fr/temoins-de-jehovah/demandez-une-visite/"),
 ("Bible d'étude", "https://www.jw.org/fr/biblioth%C3%A8que/bible/bible-d-etude/"),
 ("Questions bibliques", "https://www.jw.org/fr/la-bible-et-vous/questions-bibliques/"),
]
qr_data = {}
try:
    import qrcode
    os.makedirs(os.path.join(OUT, 'qr'), exist_ok=True)
    for label, url in QR_URLS:
        img = qrcode.make(url)
        buf = io.BytesIO(); img.save(buf, format='PNG')
        raw = buf.getvalue()
        fn = re.sub(r'[^a-z0-9]+', '_', label.lower()).strip('_') + '.png'
        open(os.path.join(OUT, 'qr', fn), 'wb').write(raw)
        qr_data[label] = 'data:image/png;base64,' + base64.b64encode(raw).decode()
    print('QR :', len(qr_data), 'codes écrits dans visuels/qr/')
except Exception as ex:
    print('QR indisponible :', ex)

# ---------------------------------------------------------------- 5. CSS
CSS = """
@page { size: A4 portrait; margin: 14mm 12mm; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: Georgia, "Times New Roman", serif; color: #16324F; background: #fff; font-size: 10pt; line-height: 1.45; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
h1 { font-size: 21pt; color: #0B2545; margin: 0 0 2mm; letter-spacing: .3px; }
h2 { font-size: 14pt; color: #0B2545; margin: 0 0 2mm; border-bottom: 1.6pt solid #E9C46A; padding-bottom: 1.2mm; }
h3 { font-size: 11pt; color: #0B2545; margin: 4mm 0 1.5mm; }
.sub { color: #4A5A6A; font-size: 9pt; margin: 0 0 3mm; }
.hdr { border-top: 3pt solid #0B2545; padding-top: 3mm; margin-bottom: 4mm; }
.small { font-size: 8pt; color: #4A5A6A; }
table { width: 100%; border-collapse: collapse; font-size: 7.4pt; }
th { background: #0B2545; color: #fff; text-align: left; padding: 1.4mm; font-weight: 700; }
td { border-bottom: .4pt solid #D8D2C4; padding: 1.3mm; vertical-align: top; }
tr { page-break-inside: avoid; }
.n { white-space: nowrap; font-family: "Courier New", monospace; font-size: 7pt; color: #0B2545; }
.lab { color: #0B2545; font-weight: 700; }
.q { background: #F7F4EC; border-left: 2.4pt solid #E9C46A; padding: 2.4mm; margin-top: 3mm; font-size: 9pt; }
.q b { color: #0B2545; }
.lim { background: #F7F4EC; border: .5pt solid #D8D2C4; padding: 2.2mm; margin-top: 2.4mm; font-size: 8.4pt; }
.rule { border: 0; border-top: .6pt solid #D8D2C4; margin: 4mm 0; }
.tag { display: inline-block; border: .6pt solid #0B2545; border-radius: 6px; padding: .4mm 1.6mm; font-size: 7.2pt; margin: 0 1.2mm 1.2mm 0; }
.tag.on { background: #0B2545; color: #fff; }
.frise svg { width: 100%; height: auto; }
.card { border: .7pt solid #0B2545; border-radius: 2mm; padding: 3mm; margin-bottom: 4mm; page-break-inside: avoid; }
.card .num { font-size: 8pt; color: #E9C46A; font-weight: 700; letter-spacing: 1px; }
.card h3 { margin: .8mm 0 2mm; }
.volet { margin: 0 0 1.6mm; font-size: 8.6pt; }
.volet .l { display: block; font-size: 7pt; text-transform: uppercase; letter-spacing: .8px; color: #4A5A6A; }
.foot { font-size: 7.4pt; color: #4A5A6A; border-top: .5pt solid #D8D2C4; margin-top: 2mm; padding-top: 1.4mm; }
.slab { border: 1pt solid #0B2545; border-radius: 2mm; overflow: hidden; }
.slab .top { background: #0B2545; color: #fff; padding: 4mm; }
.slab .top .t { font-size: 20pt; letter-spacing: 2px; font-weight: 700; }
.slab .top .s { color: #E9C46A; font-size: 9pt; letter-spacing: 1px; }
.slab .body { padding: 4mm; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }
.spine { border: .7pt solid #0B2545; border-radius: 1.5mm; padding: 2.6mm; margin-bottom: 2.4mm; }
.spine .k { font-size: 7pt; color: #E9C46A; font-weight: 700; }
.spine .t { font-size: 9.4pt; font-weight: 700; color: #0B2545; }
.cd { border: 1.2pt solid #0B2545; border-radius: 3mm; padding: 6mm; text-align: center; }
.cd .t { font-size: 24pt; letter-spacing: 3px; color: #0B2545; font-weight: 700; }
.cd .s { color: #4A5A6A; font-size: 9pt; }
.vcard { border: .8pt dashed #0B2545; border-radius: 2mm; padding: 3mm; display: grid; grid-template-columns: 26mm 1fr; gap: 3mm; align-items: center; }
.vcard img { width: 26mm; height: 26mm; }
.vcard .u { font-family: "Courier New", monospace; font-size: 7pt; word-break: break-all; color: #0B2545; }
.pagebreak { page-break-after: always; }
@media print { body { font-size: 9.6pt; } }
"""

def head(title, style=CSS):
    return ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            '<title>%s</title><style>%s</style></head><body>' % (esc(title), style))

# ---------------------------------------------------------------- 6. FRISES : écriture
def svg_timeline(items):
    n = len(items)
    step = min(8.4, (235.0 - 10) / max(n, 1))   # hauteur adaptée : la planche tient sur une page
    h = n * step + 10
    out = ['<svg viewBox="0 0 180 %d" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, serif">' % h]
    out.append('<rect x="0" y="0" width="180" height="%d" fill="#fff"/>' % h)
    out.append('<line x1="90" y1="4" x2="90" y2="%d" stroke="#0B2545" stroke-width="0.6"/>' % (h - 6))
    out.append('<line x1="90" y1="4" x2="90" y2="%d" stroke="#E9C46A" stroke-width="1.6" stroke-dasharray="1 2.6"/>' % (h - 6))
    for i, (key, date, label) in enumerate(items):
        y = 8 + i * step
        left = (i % 2 == 0)
        out.append('<circle cx="90" cy="%.1f" r="1.5" fill="#0B2545"/>' % y)
        out.append('<circle cx="90" cy="%.1f" r="2.7" fill="none" stroke="#E9C46A" stroke-width="0.5"/>' % y)
        if left:
            out.append('<line x1="86" y1="%.1f" x2="90" y2="%.1f" stroke="#D8D2C4" stroke-width="0.4"/>' % (y, y))
            out.append('<text x="85" y="%.1f" text-anchor="end" font-size="5.4" fill="#0B2545" font-weight="bold">%s</text>' % (y - 0.6, esc(date)))
            out.append('<text x="85" y="%.1f" text-anchor="end" font-size="4.6" fill="#3A4A5A">%s</text>' % (y + 3.2, esc(label)))
        else:
            out.append('<line x1="90" y1="%.1f" x2="94" y2="%.1f" stroke="#D8D2C4" stroke-width="0.4"/>' % (y, y))
            out.append('<text x="95" y="%.1f" font-size="5.4" fill="#0B2545" font-weight="bold">%s</text>' % (y - 0.6, esc(date)))
            out.append('<text x="95" y="%.1f" font-size="4.6" fill="#3A4A5A">%s</text>' % (y + 3.2, esc(label)))
    out.append('</svg>')
    return ''.join(out)

def frise_pages():
    pages = [head("Frises chronologiques — 12 planches")]
    pages.append('<div class="page"><div class="hdr"><h1>FRISES CHRONOLOGIQUES</h1>'
                 '<div class="sub">Douze planches · chaque frise : une planche graphique, puis une planche de détails tirés du registre '
                 '(référence · teneur · accomplissement · statut). Datation selon le système des publications de l\'organisation ; '
                 'lorsque la chronologie profane diffère, la divergence est signalée là où elle existe.</div></div>'
                 '<table><thead><tr><th>Frise</th><th>Titre</th><th>Période</th><th>Repères</th></tr></thead><tbody>')
    for code, titre, periode, _res, items in FRISES:
        pages.append('<tr><td class="n">%s</td><td><b>%s</b></td><td>%s</td><td class="n">%d</td></tr>'
                     % (esc(code), esc(titre), esc(periode), len(items)))
    tot = sum(len(f[4]) for f in FRISES)
    pages.append('</tbody></table><div class="q"><b>%d repères datés</b> répartis en %d planches, chacun renvoyant à une entrée numérotée du registre '
                 '(1 000 entrées · 14 parties). Utilisation : montrer la planche, lire la date, ouvrir la référence.</div>'
                 '<div class="lim"><b>Ce que ces frises ne sont pas.</b> Elles ne remplacent aucune publication : elles citent des références '
                 'bibliques et des repères historiques déjà présents dans le registre. Les divergences de datation entre les systèmes '
                 '(Babylone 607/587 ; Ninive 632/612) sont signalées au cas par cas, jamais mélangées.</div>'
                 '<div class="foot">Liens officiels : jw.org · wol.jw.org — aucune ressource externe n\'est chargée par ce fichier.</div></div>'
                 % (tot, len(FRISES)))
    for code, titre, periode, res, items in FRISES:
        pages.append('<div class="page frise"><div class="hdr"><h2>%s — %s</h2>'
                     '<div class="sub">%s · %s</div></div>%s'
                     '<div class="foot">Repères chronologiques — la planche de détails suit.</div></div>'
                     % (esc(code), esc(titre), esc(periode), esc(res), svg_timeline(items)))
        rows = []
        for key, date, label in items:
            e = find(key)
            if e is None:
                rows.append('<tr><td class="n">—</td><td class="n">%s</td><td class="n">%s</td><td>%s</td><td></td><td></td></tr>'
                            % (esc(date), esc(key), esc(label)))
                continue
            rows.append('<tr><td class="n">P%03d</td><td class="n">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
                        % (e['n'], esc(e['ref']), esc(e['teneur']), esc(e['accompl']), esc(e['statut'])))
        pages.append('<div class="page"><div class="hdr"><h2>%s — détails</h2><div class="sub">%s repères · référence · teneur · accomplissement · statut</div></div>'
                     '<table><thead><tr><th style="width:11mm">N°</th><th style="width:10mm">Date</th><th style="width:30mm">Référence</th>'
                     '<th>Teneur</th><th style="width:42mm">Accomplissement</th><th style="width:24mm">Statut</th></tr></thead><tbody>%s</tbody></table></div>'
                     % (esc(code), len(items), ''.join(rows)))
    # Annexe : couverture canonique
    pages.append('<div class="page"><div class="hdr"><h2>Annexe — couverture canonique</h2>'
                 '<div class="sub">Les soixante-six livres et le nombre d\'entrées du registre qui citent chacun d\'eux.</div></div>'
                 '<table><thead><tr><th>Livre</th><th>Entrées</th><th>Dont entrées distinctes</th><th>Livre</th><th>Entrées</th><th>Dont entrées distinctes</th></tr></thead><tbody>')
    half = 33
    for i in range(half):
        a, b = BOOKS[i], BOOKS[i + half]
        cells = []
        for bk in (a, b):
            c, d = len(cover[bk]), distinct[bk]
            note = ' <i>(aucune prophétie)</i>' if bk in NO_PROPH else ''
            cells.append('<td>%s%s</td><td class="n">%d</td><td class="n">%d</td>' % (esc(bk), note, c, d))
        pages.append('<tr>%s</tr>' % ''.join(cells))
    pages.append('</tbody></table>'
                 '<div class="q"><b>%d livres sur 66</b> comportent au moins une entrée · <b>%d entrées</b> au total · '
                 'quatre livres ne comportent aucune prophétie annoncée (Esther, Philémon, 2 Jean, 3 Jean).</div>'
                 '<div class="lim"><b>Lecture.</b> La colonne « entrées » compte les lignes du registre qui citent le livre, y compris les '
                 'renvois du tableau consolidé des prophéties messianiques ; la colonne suivante ne compte qu\'une seule fois une même '
                 'référence avec la même teneur. Aucun total dogmatique n\'est avancé sur le nombre des prophéties messianiques.</div>'
                 '<div class="foot">Registre : 1 000 entrées · 14 parties · généré par visuels/build_visuels.py</div></div>'
                 % (sum(1 for b in BOOKS if cover[b]), len(entries)))
    return ''.join(pages) + '</body></html>'

# ---------------------------------------------------------------- 7. CARTES À 3 VOLETS
VOLETS = ["Contexte", "Repère chronologique", "Référence biblique", "Ce que l'on peut vérifier",
          "Le détail qui marque", "Ce que cela ne prouve pas", "Une question pour ouvrir", "Un lien officiel"]
CARDS = [
 ("La première promesse", "Genèse 3:15", "Une postérité écrasera la tête du serpent", "promesse d'Éden", "Toute la Bible est écrite comme une réponse à cette ligne."),
 ("Le déluge annoncé", "Genèse 6:3", "Cent vingt ans, puis le déluge", "avant le déluge", "Un délai annoncé : le temps de construire."),
 ("Sodome et Gomorrhe", "Genèse 18:20-33", "Le jugement est annoncé, puis différé pour dix justes", "vers 1913 av. n. è.", "Une négociation verset par verset avant l'exécution."),
 ("Isaac annoncé par son nom et son année", "Genèse 17:19-21", "Le nom de l'enfant est donné avant sa conception", "1918 av. n. è.", "Trois visiteurs, un nom, une année."),
 ("Quatre cents ans annoncés", "Genèse 15:13-14", "Servitude, puis sortie avec de grands biens", "1933 av. n. è.", "La durée est annoncée quatre siècles avant la sortie."),
 ("Le prophète comme Moïse", "Deutéronome 18:15-19", "Un prophète s'élèvera ; écoutez-le", "1473 av. n. è.", "La lignée mène à un seul : Pierre cite le texte."),
 ("Josias, nommé trois siècles avant", "1 Rois 13:2-5", "Un roi de Juda, nommé, brûlera les ossements sur l'autel", "997 av. n. è.", "Le nom est écrit avant la naissance ; le roi agira exactement ainsi."),
 ("Ninive et les quarante jours", "Jonas 3:4", "Dans quarante jours, Ninive sera renversée", "vers 844 av. n. è.", "La ville s'est repentie : le délai annoncé explique le sursis."),
 ("Samarie, la tête bandée", "Osée 1:4, 5", "L'arc d'Israël brisé dans la vallée", "vers 745 av. n. è.", "Le royaume du nord tombe en 740."),
 ("L'Assyrie, bâton puis brisure", "Isaïe 10:5-19", "L'outil de la colère est à son tour brisé", "après 740 av. n. è.", "Deux temps dans une seule prophétie : l'usage, puis la chute."),
 ("Bethléem nommée", "Michée 5:2", "De toi sortira celui qui doit être chef en Israël", "vers 716 av. n. è.", "Le lieu est nommé sept siècles avant la naissance."),
 ("Bel plie, Nébo s'incline", "Isaïe 46:1, 2", "Les dieux de Babylone emportés sur des bêtes", "vers 732 av. n. è.", "Les idoles transportées : l'exact contraire d'un dieu qui porte son peuple."),
 ("Tyr, la poussière jetée à l'eau", "Ézéchiel 26:12", "Les pierres, le bois et la poussière jetés au milieu des eaux", "588 av. n. è.", "Le détail est inhabituel : les pierres d'une ville jetées à la mer."),
 ("Le chaudron de Jérusalem", "Ézéchiel 24:1-14", "Le chaudron rouillé, le siège, le mois précis", "589 av. n. è.", "La vision est datée du jour même du début du siège."),
 ("La main sur le mur", "Daniel 5:5-28", "Mené, pesé, divisé", "5 octobre 539 av. n. è.", "Trois mots écrits la nuit même de la chute."),
 ("Le nom de Belshatsar", "Daniel 5:1, 2", "Un roi de Babylone nommé dans le récit", "539 av. n. è.", "Longtemps contesté, attesté depuis par des textes cunéiformes."),
 ("La statue aux quatre métaux", "Daniel 2:36-43", "Un enchaînement de dominations mondiales", "vers 603 av. n. è.", "Quatre métaux, quatre empires, puis une pierre."),
 ("Raphia, 217 av. n. è.", "Daniel 11:11, 12", "Le roi du midi frappe à son tour", "217 av. n. è.", "Le lieu de la bataille se laisse identifier dans le texte."),
 ("Les soixante-dix semaines", "Daniel 9:24-27", "Soixante-deux semaines, puis une semaine partagée", "539 av. n. è.", "Un décret daté, un compte d'années, et un point d'arrivée."),
 ("Le décret de Cyrus", "Isaïe 44:28", "Un roi perse nommé deux siècles avant sa naissance", "vers 732 av. n. è.", "Le cylindre d'argile décrit la politique annoncée."),
 ("Zorobabel, comme un sceau", "Aggée 2:20-23", "L'élu, porté comme un sceau", "520 av. n. è.", "Un retour qui réinstalle une lignée royale."),
 ("La pierre rejetée", "Psaume 118:22, 23", "La pierre rejetée devient la tête de l'angle", "vers 1040 av. n. è.", "Cité par Pierre et par Paul, appliqué au Christ."),
 ("Le cavalier et le signe composite", "Matthieu 24:6-14", "Guerres, famines, séismes, prédication mondiale", "depuis 1914", "Ce n'est pas un élément isolé, mais leur simultanéité."),
 ("Ce qui vient", "Révélation 21:3, 4", "Dieu habitera avec les humains ; toute larme essuyée", "à venir", "Trois fois « à venir » dans le registre, jamais daté."),
]
OFFICIAL_LINK = "jw.org/fr · wol.jw.org/fr"

def cards_pages():
    pages = [head("Découvrir pas à pas — 24 cartes")]
    pages.append('<div class="page"><div class="hdr"><h1>DÉCOUVRIR PAS À PAS</h1>'
                 '<div class="sub">24 cartes · chacune en trois volets, choisis de façon fixe : lisible en trois minutes, imprimable à découper.</div></div>'
                 '<table><thead><tr><th>N°</th><th>Thème</th><th>Référence</th><th>Repère</th></tr></thead><tbody>')
    for i, (theme, ref, teneur, repere, note) in enumerate(CARDS, 1):
        pages.append('<tr><td class="n">%02d</td><td><b>%s</b></td><td class="n">%s</td><td>%s</td></tr>'
                     % (i, esc(theme), esc(ref), esc(repere)))
    pages.append('</tbody></table><div class="q"><b>Mode d\'emploi.</b> Prendre une carte, lire à voix haute le volet 1 et le volet 2, '
                 'puis laisser la personne lire la référence. Le volet « ce que cela ne prouve pas » se lit aussi : c\'est lui qui établit la confiance.</div></div>')
    for block in range(6):  # 6 pages de 4 cartes
        pages.append('<div class="page">')
        for i in range(block * 4, min(block * 4 + 4, len(CARDS))):
            theme, ref, teneur, repere, note = CARDS[i]
            e = find(ref)
            volets = [VOLETS[(i + k) % len(VOLETS)] for k in range(3)]
            contenu = {
                "Contexte": note,
                "Repère chronologique": repere,
                "Référence biblique": ref + (" · registre : P%03d" % e['n'] if e else ""),
                "Ce que l'on peut vérifier": (e['accompl'] if e else teneur),
                "Le détail qui marque": teneur,
                "Ce que cela ne prouve pas": "Un récit atteste une donnée ; il ne prouve pas à lui seul la date de rédaction du livre qui l'annonce, ni une interprétation. Le registre ne date jamais l'avenir.",
                "Une question pour ouvrir": "Si ce détail était vérifiable ailleurs que dans la Bible, qu'est-ce que cela changerait pour vous ?",
                "Un lien officiel": OFFICIAL_LINK,
            }
            pages.append('<div class="card"><div class="num">CARTE %02d — %s</div><h3>%s</h3>' % (i + 1, esc(repere).upper(), esc(theme)))
            for v in volets:
                pages.append('<div class="volet"><span class="l">%s</span>%s</div>' % (esc(v), esc(contenu[v])))
            pages.append('<div class="foot">Référence : %s · texte intégral de la ligne dans le registre (P%03d)%s</div></div>'
                         % (esc(ref), e['n'] if e else 0, ' — absente du registre' if e is None else ''))
        pages.append('</div>')
    return ''.join(pages) + '</body></html>'

# ---------------------------------------------------------------- 8. COFFRET
CLASSEURS = [
 ("1", "Pentateuque", "65 entrées · P001-P065", "Genèse à Deutéronome : la promesse, l'Égypte, la conquête"),
 ("2", "Livres historiques", "41 entrées · P066-P106", "Josué, Juges, Samuel, Rois, Chroniques, Esdras, Néhémie"),
 ("3", "Isaïe", "74 entrées · P107-P180", "Assyrie, Babylone, Cyrus, le Serviteur"),
 ("4", "Jérémie et Lamentations", "116 entrées · P181-P300", "Les soixante-dix ans, la chute, la promesse du retour"),
 ("5", "Ézéchiel et Daniel", "113 entrées · P301-P407", "Les visions datées, les empires, les soixante-dix semaines"),
 ("6", "Les Douze", "112 entrées · P408-P519", "Osée à Malachie : Samarie, Ninive, Édom, le jour de Jéhovah"),
 ("7", "Psaumes et écrits", "83 entrées · P520-P602", "La trame messianique : les mains, les pieds, les vêtements, les os"),
 ("8", "Le Christ et les apôtres", "222 entrées · P603-P824", "Le signe composite, la résurrection, l'assemblée, les lettres"),
 ("9", "Révélation", "176 entrées · P825-P1000", "Les sept messages, les sceaux, les trompettes, les bêtes, la Nouvelle Jérusalem"),
]
CHAPITRES_CD = [
 "1. Comment se servir des dix planches", "2. Dix secondes : l'accroche", "3. La date avant l'argument",
 "4. Un système chronologique à la fois", "5. Les huit objections et leur réponse brève",
 "6. Les cinq règles de présentation", "7. La recherche par mot dans le site local",
 "8. L'audio : écouter avant de parler", "9. Le déroulé d'une conversation de quinze minutes",
 "10. Vers jw.org : les six liens officiels",
]

def media_counts():
    import glob as _g
    img = len(_g.glob(os.path.join(PREUVES, 'images', '*.jpg'))) + len(_g.glob(os.path.join(PREUVES, 'images', '*.png')))
    aud = len(_g.glob(os.path.join(PREUVES, 'audio', '*.mp3')))
    return img, aud

def coffret_pages():
    IMG_N, AUD_N = media_counts()
    p = [head("Coffret — PREUVES")]
    p.append('<div class="page"><div class="slab"><div class="top"><div class="s">BIBLIOTHÈQUE PRIVÉE · USAGE PERSONNEL</div>'
             '<div class="t">PREUVES</div><div class="s">PROPHÉTIES BIBLIQUES &amp; ACCOMPLISSEMENTS</div></div><div class="body">'
             '<div class="grid2"><div><h3>Ce que contient le coffret</h3><table><tbody>'
             '<tr><td>Registre numéroté</td><td class="n">1 000 entrées</td></tr>'
             '<tr><td>Parties</td><td class="n">14 + récapitulatif</td></tr>'
             '<tr><td>Livres imprimables</td><td class="n">3</td></tr>'
             '<tr><td>Site local autonome</td><td class="n">1 fichier</td></tr>'
             '<tr><td>Grandes preuves</td><td class="n">12 fiches</td></tr>'
             '<tr><td>Détails datés</td><td class="n">25</td></tr>'
             '<tr><td>Frises chronologiques</td><td class="n">12 planches</td></tr>'
             '<tr><td>Cartes à volets</td><td class="n">24</td></tr>'
             '<tr><td>Images (JPG)</td><td class="n">' + str(IMG_N) + '</td></tr>'
             '<tr><td>Audio (MP3, français)</td><td class="n">' + str(AUD_N) + '</td></tr>'
             '</tbody></table></div><div><h3>Trois règles</h3>'
             '<p class="small">1. Tout aboutit à un lien officiel : jw.org ou wol.jw.org. '
             '2. Aucun contenu protégé n\'est recopié : on cite des références. '
             '3. Une conversation à la fois, jamais d\'envoi de masse, jamais de site personnel.</p>'
             '<div class="foot">Fichiers sources : registre 16-21 et 23 · Grand Dossier 22 · SITE_LOCAL.html · livres/ · visuels/</div></div></div>'
             '</div></div><hr class="rule">')
    if qr_data:
        p.append('<h2>Accès immédiat</h2><div class="grid2">')
        for label, url in QR_URLS:
            p.append('<div class="vcard"><img src="%s" alt="QR %s"><div><b>%s</b><div class="u">%s</div></div></div>'
                     % (qr_data[label], esc(label), esc(label), esc(url)))
        p.append('</div>')
    p.append('<div class="lim"><b>Ce que ce coffret n\'est pas.</b> Ni un site, ni une chaîne, ni un compte : un ensemble de fichiers '
             'à usage strictement personnel et privé, à imprimer ou à transmettre un par un, avec des liens vers les sites officiels.</div></div>')

    p.append('<div class="page"><div class="hdr"><h1>DOS DE CLASSEUR</h1><div class="sub">Neuf étiquettes à découper, à coller sur les dos de classeurs. '
             'Chaque titre renvoie à des entrées numérotées, jamais à une paraphrase.</div></div>')
    for k, titre, compte, sous in CLASSEURS:
        p.append('<div class="spine"><span class="k">CLASSEUR %s</span><div class="t">%s</div>'
                 '<div class="small">%s</div><div class="small">%s</div></div>' % (esc(k), esc(titre), esc(compte), esc(sous)))
    p.append('<div class="foot">Impression : A4, sans mise à l\'échelle, marges par défaut. Découper sur le trait.</div></div>')

    p.append('<div class="page"><div class="hdr"><h1>COUVERTURE DU DISQUE</h1><div class="sub">Pour un disque ou une clé remis en main propre : dix pistes audio en français.</div></div>')
    p.append('<div class="cd"><div class="t">PREUVES</div><div class="s">DIX PISTES · DÉMONSTRATION EN FRANÇAIS</div></div>')
    p.append('<h3>Pistes</h3><table><tbody>')
    for c in CHAPITRES_CD:
        p.append('<tr><td>%s</td></tr>' % esc(c))
    p.append('</tbody></table><div class="lim"><b>Rappel.</b> Aucun extrait de publication n\'est enregistré : ces pistes sont des scripts '
             'originaux qui citent des références bibliques et renvoient aux sites officiels.</div>'
             '<div class="foot">Durée indicative : 10 à 14 minutes au total · voix unique, français.</div></div>')

    p.append('<div class="page"><div class="hdr"><h1>ÉTIQUETTES</h1><div class="sub">Vingt-quatre étiquettes : thème · référence · numéro de registre. À découper et coller sur les pochettes.</div></div>'
             '<table><thead><tr><th>Thème</th><th>Référence</th><th>N°</th><th>Thème</th><th>Référence</th><th>N°</th></tr></thead><tbody>')
    for i in range(12):
        a, b = CARDS[i], CARDS[i + 12]
        cells = []
        for theme, ref, *_ in (a, b):
            e = find(ref)
            cells.append('<td>%s</td><td class="n">%s</td><td class="n">%s</td>'
                         % (esc(theme), esc(ref), ('P%03d' % e['n']) if e else '—'))
        p.append('<tr>%s</tr>' % ''.join(cells))
    p.append('</tbody></table><div class="foot">Coffret PREUVES — généré par visuels/build_visuels.py · usage privé</div></div>')
    return ''.join(p) + '</body></html>'

# ---------------------------------------------------------------- 9. CARTES QR
def qr_pages():
    p = [head("Cartes de visite — QR officiels")]
    p.append('<div class="page"><div class="hdr"><h1>CARTES DE VISITE — QR</h1>'
             '<div class="sub">Huit cartes à découper. Chaque QR pointe vers un site officiel : jw.org ou wol.jw.org. Aucun autre domaine.</div></div>')
    p.append('<div class="grid2">')
    for i, (label, url) in enumerate(QR_URLS):
        src = qr_data.get(label, '')
        p.append('<div class="card vcard"><div>%s</div><div><b>Carte %d — %s</b><div class="u">%s</div>'
                 '<div class="small">Scannez, lisez, vérifiez. Aucune inscription, aucune collecte de données.</div></div></div>'
                 % (('<img src="%s" alt="QR" style="width:26mm;height:26mm">' % src) if src else '<div class="small">QR non généré</div>',
                    i + 1, esc(label), esc(url)))
    p.append('</div><div class="lim"><b>Règle d\'usage.</b> Ces cartes se remettent en main propre, une par une. Aucune campagne, aucune '
             'distribution en masse, aucun dépôt sur un espace public. Le contenu ne remplace pas une publication : il mène à elle.</div>'
             '<div class="foot">Cartes QR — visuels/CARTES_QR.html</div></div>')
    return ''.join(p) + '</body></html>'

# ---------------------------------------------------------------- 10. ÉCRITURE
def write(name, content):
    path = os.path.join(OUT, name)
    open(path, 'w', encoding='utf-8').write(content)
    return path, len(content.encode('utf-8'))

tot_items = sum(len(f[4]) for f in FRISES)
missing = [(code, key) for code, _t, _p, _r, items in FRISES for key, _d, _l in items if find(key) is None]

rep = []
rep.append(write('FRISES_CHRONOLOGIQUES.html', frise_pages()))
rep.append(write('DECOUVRIR_PAS_A_PAS.html', cards_pages()))
rep.append(write('COFFRET.html', coffret_pages()))
rep.append(write('CARTES_QR.html', qr_pages()))

print('registre : %d entrées · %d parties' % (len(entries), len(parts)))
print('frises : %d planches · %d repères · non indexés : %d' % (len(FRISES), tot_items, len(missing)))
for code, key in missing: print('   manquant :', code, '→', key)
print('couverture canonique : %d livres avec entrées / 66' % sum(1 for b in BOOKS if cover[b]))
for name, size in rep: print('écrit : %s (%.0f Ko)' % (name, size / 1024))
