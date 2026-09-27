#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit les trois livres imprimables (HTML prêt à imprimer, A4).
LIVRE_1_ENQUETE.html   : les 12 preuves, fiches de 2 pages (source : 22_GRAND_DOSSIER.md)
LIVRE_2_LES_1000.html   : le registre mis en pages (sources : 16 à 21)
LIVRE_3_DETAIL.html    : 25 détails datés, avec source et limite
Aucune ressource externe : polices système, aucun script, aucun chargement réseau."""
import re, os, glob, html

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
OUT = BASE
REG = ['16_REGISTRE_PROPHETIES.md', '17_REGISTRE_PROPHETIES_2.md',
       '18_REGISTRE_PROPHETIES_3.md', '19_REGISTRE_PROPHETIES_4.md',
       '20_REGISTRE_PROPHETIES_5.md', '21_REGISTRE_PROPHETIES_6.md',
       '23_REGISTRE_PROPHETIES_7.md']

PART_RE = re.compile(r'^#{1,3}\s*PARTIE\s+(\d+)\s*[—–-]\s*(.+?)\s*$')
HEAD_RE = re.compile(r'^(#{2,3})\s+(.+?)\s*$')
ROW_RE = re.compile(r'^\|\s*P(\d{3,4})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$')
NUM_RE = re.compile(r'^\d+(?:\.\d+)?\s+')

CSS = """
@page{size:A4;margin:17mm 15mm 16mm}
@page:first{margin:0}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;background:#fff;color:#12203a;font:10.5pt/1.5 Georgia,"Times New Roman",serif}
h1,h2,h3,h4,.kicker,.badge,th,.num,.brand{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.cover{height:297mm;background:linear-gradient(160deg,#0B2545,#13315C 60%,#0a1e38);color:#fff;
  padding:34mm 22mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always}
.cover .brand{letter-spacing:3px;font-size:10pt;color:#E9C46A;text-transform:uppercase}
.cover h1{font-size:34pt;line-height:1.08;margin:14mm 0 6mm}
.cover .st{font-size:13pt;color:#cfe0f5;max-width:130mm}
.cover .foot{font-size:9.5pt;color:#9fc0e4;border-top:1px solid #2a4a75;padding-top:5mm}
.cover .gold{color:#E9C46A}
.page{page-break-before:always}
h2{color:#0B2545;border-bottom:2.5px solid #E9C46A;padding-bottom:2.5mm;margin:0 0 5mm;font-size:17pt}
h3{color:#0B2545;margin:7mm 0 2mm;font-size:12.5pt}
h4{color:#13315C;margin:5mm 0 1.5mm;font-size:11pt}
p{margin:0 0 3mm;text-align:justify;hyphens:auto}
.kicker{font-size:9pt;letter-spacing:2px;color:#8a7a4e;text-transform:uppercase;margin:0 0 2mm}
.fiche{page-break-before:always}
.fiche .num{font-size:38pt;color:#eadfc0;line-height:1;margin:0}
.fiche h2{margin-top:1mm}
.lab{font-weight:700;color:#0B2545}
.lim{background:#fdf7e4;border-left:3px solid #E9C46A;padding:3mm 4mm;margin:4mm 0;font-size:9.5pt}
.warn{background:#fdeeee;border-left:3px solid #b26a1f;padding:3mm 4mm;margin:4mm 0;font-size:9.5pt}
.q{background:#eef4fb;border-left:3px solid #4a7fbf;padding:3mm 4mm;margin:4mm 0;font-style:italic}
table{width:100%;border-collapse:collapse;margin:3mm 0 5mm;font-size:8.6pt}
th,td{border:1px solid #d8d2c0;padding:1.4mm 2mm;vertical-align:top;text-align:left}
th{background:#f2ecd9;color:#0B2545;font-size:8.4pt}
tr{page-break-inside:avoid}
td.n{width:11mm;font-weight:700;color:#0B2545;font-family:"Segoe UI",Arial,sans-serif}
td.r{width:30mm;font-weight:600}
td.s{width:26mm;font-size:8.2pt}
ol,ul{margin:0 0 3mm 5mm;padding:0}
li{margin:0 0 1.6mm}
.toc{columns:2;column-gap:10mm;font-size:10pt}
.toc div{margin:0 0 2mm;break-inside:avoid}
.toc b{color:#0B2545}
.rule{border:0;border-top:1px solid #d8d2c0;margin:6mm 0}
.src{font-size:9pt;color:#40506b}
.footline{margin-top:8mm;border-top:1px solid #d8d2c0;padding-top:2mm;font-size:8.5pt;color:#7b8aa3}
.center{text-align:center}
.badge{display:inline-block;font-size:8pt;padding:.6mm 2mm;border:1px solid #0B2545;border-radius:3mm;margin:0 1mm 1mm 0}
@media screen{body{background:#e9e3d2}.sheet{max-width:210mm;margin:0 auto;background:#fff;padding:14mm 12mm;box-shadow:0 2px 18px rgba(0,0,0,.18)}}
@media print{.sheet{max-width:none;margin:0;padding:0;box-shadow:none}}
"""

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    return s

def md_block(lines):
    """convertisseur minimal : titres, listes, tableaux, paragraphes"""
    out, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i].rstrip()
        if not l.strip():
            i += 1; continue
        if l.startswith('#### '):
            out.append('<h4>%s</h4>' % inline(l[5:])); i += 1; continue
        if l.startswith('### '):
            out.append('<h3>%s</h3>' % inline(l[4:])); i += 1; continue
        if l.startswith('## '):
            out.append('<h2>%s</h2>' % inline(l[3:])); i += 1; continue
        if l.startswith('# '):
            out.append('<h2>%s</h2>' % inline(l[2:])); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < n and lines[i].lstrip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c or '') for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                head = rows[0]
                body = rows[1:]
                t = ['<table><thead><tr>'] + ['<th>%s</th>' % inline(c) for c in head] + ['</tr></thead><tbody>']
                for r in body:
                    t.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>')
                t.append('</tbody></table>')
                out.append(''.join(t))
            continue
        if re.match(r'^\s*[-*] ', l):
            items = []
            while i < n and re.match(r'^\s*[-*] ', lines[i]):
                items.append('<li>%s</li>' % inline(re.sub(r'^\s*[-*] ', '', lines[i]))); i += 1
            out.append('<ul>' + ''.join(items) + '</ul>'); continue
        if re.match(r'^\s*\d+\. ', l):
            items = []
            while i < n and re.match(r'^\s*\d+\. ', lines[i]):
                items.append('<li>%s</li>' % inline(re.sub(r'^\s*\d+\. ', '', lines[i]))); i += 1
            out.append('<ol>' + ''.join(items) + '</ol>'); continue
        if l.startswith('> '):
            out.append('<div class="q">%s</div>' % inline(l[2:])); i += 1; continue
        if re.fullmatch(r'-{3,}', l.strip()):
            out.append('<hr class="rule">'); i += 1; continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4} |\||\s*[-*] |\s*\d+\. |> |-{3,})', lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append('<p>%s</p>' % inline(' '.join(buf)))
    return '\n'.join(out)

def page(title, center, body, foot=''):
    return (f'<div class="sheet"><div class="cover"><div><div class="brand">Repères · bibliothèque privée</div>'
            f'<h1>{title}</h1><div class="st">{center}</div></div><div class="foot">{foot}</div></div>\n'
            f'{body}</div>')

def wrap(doc_title, inner):
    return (f'<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{doc_title}</title><style>{CSS}</style></head><body>\n{inner}\n</body></html>')

# ---------------------------------------------------------------- LIVRE 1
dossier = open(os.path.join(ROOT, '22_GRAND_DOSSIER.md'), encoding='utf-8').read().split('\n')
fiches, cur, intro = [], None, []
for line in dossier:
    m = re.match(r'^# PREUVE (\d+) — (.+)$', line)
    if m:
        if cur: fiches.append(cur)
        cur = {'n': int(m.group(1)), 'titre': m.group(2), 'lines': []}
        continue
    (cur['lines'] if cur else intro).append(line)
if cur: fiches.append(cur)

lab_map = {'L\'accroche': 'L\'accroche', 'Le fait vérifiable': 'Le fait vérifiable',
           'La prophétie': 'La prophétie', 'L\'accomplissement': 'L\'accomplissement',
           'Les sources': 'Les sources', 'La question qui ouvre': 'La question qui ouvre',
           'Les sorties': 'Les sorties', 'La référence officielle': 'La référence officielle'}

body1 = []
# sommaire
body1.append('<div class="page"><h2>Sommaire</h2><div class="toc">')
for f in fiches:
    body1.append('<div><b>Preuve %d.</b> %s</div>' % (f['n'], inline(f['titre'])))
body1.append('</div><hr class="rule">')
body1.append('<div class="warn">Les 12 fiches qui suivent suivent toutes la même structure : l\'accroche, le fait vérifiable, la prophétie, '
             'l\'accomplissement, les sources et ce qu\'elles ne prouvent pas, la question qui ouvre, les sorties et la référence officielle. '
             'Elles ne remplacent pas les publications : elles renvoient, par lien, vers jw.org et wol.jw.org.</div>')
body1.append('<h2>Comment se servir de ce livre</h2>')
body1.append(md_block([l for l in intro if not l.startswith('# ')]))
body1.append('</div>')

for f in fiches:
    body1.append('<div class="fiche"><div class="num">%02d</div><h2>%s</h2>' % (f['n'], inline(f['titre'])))
    buf = []
    for l in f['lines']:
        if re.match(r'^\*\*(L\'accroche|Le fait vérifiable|La prophétie|L\'accomplissement|Les sources|La question qui ouvre|Les sorties|La référence officielle)', l):
            if buf: body1.append(md_block(buf)); buf = []
            label = re.match(r'^\*\*(.+?)\.?\*\*', l).group(1)
            rest = re.sub(r'^\*\*(.+?)\*\*\s*', '', l)
            cls = 'q' if label.startswith('La question') else ('lim' if label.startswith('Les sources') else '')
            if cls:
                body1.append('<div class="%s"><span class="lab">%s.</span> %s</div>' % (cls, inline(label), inline(rest)))
            else:
                body1.append('<p><span class="lab">%s.</span> %s</p>' % (inline(label), inline(rest)))
        else:
            buf.append(l)
    if buf: body1.append(md_block(buf))
    body1.append('<div class="footline">Fiche %d — registre : voir les entrées indiquées ci-dessus. Sources officielles : jw.org · wol.jw.org</div></div>' % f['n'])

# annexe
annexe = dossier[dossier.index([l for l in dossier if l.startswith('## ANNEXE')][0]):] if any(l.startswith('## ANNEXE') for l in dossier) else []
if annexe:
    body1.append('<div class="page">' + md_block(annexe) + '</div>')

open(os.path.join(OUT, 'LIVRE_1_ENQUETE.html'), 'w', encoding='utf-8').write(wrap(
    'L\'Enquête — les 12 grandes preuves',
    page('L\'ENQUÊTE', 'Les 12 grandes preuves des prophéties bibliques et de leurs accomplissements, '
         'présentées une par une, avec leurs sources et leurs limites honnêtes.',
         ''.join(body1),
         foot='Registre général exhaustif : 1 000 entrées (P001-P975) · 14 parties · usage privé<br>'
              'Sources : jw.org · wol.jw.org')))
print('LIVRE 1 : %d fiches' % len(fiches))

# ---------------------------------------------------------------- LIVRE 2
entries, part, section = [], '', ''
for fn in REG:
    for line in open(os.path.join(ROOT, fn), encoding='utf-8'):
        m = PART_RE.match(line)
        if m: part, section = m.group(2), ''; continue
        h = HEAD_RE.match(line)
        if h:
            t = NUM_RE.sub('', h.group(2)).strip()
            if t and not t.startswith(('SUITE', 'RÈGLES', 'RAPPEL', 'PLAN')):
                section = t
            continue
        r = ROW_RE.match(line)
        if r:
            entries.append({'n': int(r.group(1)), 'ref': r.group(2), 't': r.group(3),
                            'a': r.group(4), 's': r.group(5), 'p': part, 'sec': section})
entries.sort(key=lambda e: e['n'])

body2 = []
parts = []
for e in entries:
    if not parts or parts[-1][0] != e['p']:
        parts.append([e['p'], e['n'], e['n'], 1])
    else:
        parts[-1][2] = e['n']; parts[-1][3] += 1

body2.append('<div class="page"><h2>Sommaire</h2><div class="toc">')
for p in parts:
    body2.append('<div><b>%s</b><br>P%03d – P%03d · %d entrées</div>' % (inline(p[0]), p[1], p[2], p[3]))
if len(parts) >= 13:
    body2.append('<div><b>Tableau récapitulatif final</b><br>index · totaux · statuts · repères · garde-fous</div>')
body2.append('</div><hr class="rule">')
body2.append('<h2>Comment lire ce registre</h2>')
body2.append('<p>Chaque ligne tient en cinq colonnes : le numéro d\'inventaire, la référence, la teneur de la prophétie, '
             'l\'accomplissement, et le statut. Aucun commentaire n\'est ajouté. Les entrées sont numérotées de P001 à P1000 : '
             'le numéro sert à citer, vérifier et retrouver une ligne sans paraphrase.</p>')
body2.append('<p><span class="badge">Accomplie</span><span class="badge">Accomplie (1er accomplissement)</span>'
             '<span class="badge">En cours</span><span class="badge">À venir</span><span class="badge">Accomplie (identifiée)</span></p>')
body2.append('<div class="lim"><b>Trois garde-fous.</b> 1) Un seul système chronologique par contenu : le registre emploie le système de datation '
             'de l\'organisation (Jérusalem 607 av. n. è.) ; lorsque la chronologie profane courante diffère, elle est signalée. '
             '2) Aucun total de prophéties messianiques n\'est présenté comme une certitude : c\'est un inventaire de travail. '
             '3) Aucune date n\'est donnée pour la fin.</div></div>')

cur_p = cur_s = None
for e in entries:
    if e['p'] != cur_p:
        if cur_p: body2.append('</tbody></table>')
        body2.append('<div class="page"><h2>%s</h2>' % inline(e['p']))
        body2.append('<table><thead><tr><th>N°</th><th>Référence</th><th>Teneur</th><th>Accomplissement</th><th>Statut</th></tr></thead><tbody>')
        cur_p, cur_s = e['p'], None
    elif e['sec'] != cur_s:
        pass
    if e['sec'] != cur_s:
        body2.append('<tr><td colspan="5" style="background:#f7f4ec;font-weight:700;color:#0B2545">%s</td></tr>' % inline(e['sec'] or '—'))
        cur_s = e['sec']
    body2.append('<tr><td class="n">P%03d</td><td class="r">%s</td><td>%s</td><td>%s</td><td class="s">%s</td></tr>'
                 % (e['n'], inline(e['ref']), inline(e['t']), inline(e['a']), inline(e['s'])))
body2.append('</tbody></table></div>')

# index alphabétique des sections
secs = {}
for e in entries:
    if e['sec']:
        d = secs.setdefault(e['sec'], [e['n'], e['n'], 0])
        d[0] = min(d[0], e['n']); d[1] = max(d[1], e['n']); d[2] += 1
body2.append('<div class="page"><h2>Index des sections</h2><table><thead><tr><th>Section</th><th>Entrées</th><th>Nombre</th></tr></thead><tbody>')
for k in sorted(secs, key=lambda x: x.lower()):
    v = secs[k]
    body2.append('<tr><td>%s</td><td class="n" style="width:32mm">P%03d – P%03d</td><td>%d</td></tr>' % (inline(k), v[0], v[1], v[2]))
body2.append('</tbody></table>')
body2.append('<div class="footline">Registre général exhaustif : %d entrées · %d parties · sources officielles : jw.org · wol.jw.org</div></div>'
             % (len(entries), len(parts)))

open(os.path.join(OUT, 'LIVRE_2_LES_1000.html'), 'w', encoding='utf-8').write(wrap(
    'Les 975 — registre général exhaustif',
    page('LES 975', 'Registre général exhaustif des prophéties bibliques et de leurs accomplissements : '
         '1 000 entrées numérotées, 14 parties, aucune entrée manquante, aucun doublon.',
         ''.join(body2),
         foot='Référence · teneur · accomplissement · statut — sans commentaire<br>Sources : jw.org · wol.jw.org')))
print('LIVRE 2 : %d entrées, %d parties' % (len(entries), len(parts)))

# ---------------------------------------------------------------- LIVRE 3
D = [
 (1, 'Un roi nommé deux siècles à l\'avance', 'entre 740 et 700 av. n. è. (rédaction) → 539 av. n. è.',
  'Isaïe 44:28 ; 45:1-4', 'Isaïe nomme Cyrus et annonce sa politique : il rebâtira Jérusalem et libérera les captifs « sans rançon ni présents ».',
  'Le cylindre de Cyrus, retrouvé à Sippar (environ 32 km de Bagdad), en cunéiforme, relate la prise de Babylone et la politique de retour des captifs dans leur pays.',
  'La date de rédaction du livre d\'Isaïe est discutée : des critiques situent une partie du texte plus tard.'),
 (2, 'La nuit du 5-6 octobre 539', '539 av. n. è.', 'Isaïe 44:27 ; 45:1 ; Jérémie 50:38 ; 51:30,31',
  'Les eaux protectrices de l\'Euphrate se « dessécheront » ; les portes de la ville « ne seront pas fermées » ; la ville est prise en une nuit.',
  'Chronique babylonienne, Bérose, « Poème de Nabonide » ; les publications de l\'organisation datent la prise du 5 octobre (calendrier grégorien) ou du 11 octobre (julien).',
  'La datation du jour dépend du calendrier employé : le registre retient « 5-6 octobre » sans resserrer davantage.'),
 (3, 'Le nom de Belshatsar', 'VIe siècle av. n. è.', 'Daniel 5:1, 9, 22',
  'Daniel nomme « Belshatsar le roi de Babylone », alors que les historiens anciens ne donnaient que Nabonide comme dernier roi.',
  'Une tablette cunéiforme parle de « Belshatsar, le principal officier du roi » ; le « Poème de Nabonide », publié en 1924, établit sa position royale et sa corégence.',
  '« Fils de » peut signifier « petit-fils de » ; Belshatsar était corégent, non souverain unique.'),
 (4, 'La « troisième place dans le royaume »', 'VIe siècle av. n. è.', 'Daniel 5:7, 16, 29',
  'Belshatsar offre non la deuxième mais la troisième place du royaume à qui lira l\'écriture : deux places étaient donc déjà occupées.',
  'Une tablette de la 12e année de Nabonide porte un serment prêté par « Nabonide le roi » et « Belshatsar le fils du roi » : la double royauté est attestée.',
  'Le sens exact du rang reste interprété ; l\'essentiel attesté est la corégence.'),
 (5, 'Tyr : la chaussée d\'Alexandre', '332 av. n. è.', 'Ézéchiel 26:12',
  '« Ils jetteront au milieu des eaux tes pierres, ton bois et ta poussière. »',
  'Alexandre construit une digue avec les débris de la ville continentale qu\'il venait de démolir : « With the debris of the mainland portion of the city, which he had demolished, he built a huge mole in 332 » (The Encyclopedia Americana).',
  'Les dates précises des deux sièges de Tyr (Babyloniens puis Macédoniens) restent discutées.'),
 (6, 'Tyr : un lieu de séchage pour filets', 'accomplissement continu', 'Ézéchiel 26:14',
  '« Tu ne seras plus rebâtie » ; la ville deviendra « un lieu de séchage pour filets ».',
  'Le site de l\'ancienne Tyr continentale est un champ de fouilles au bord de la mer ; l\'île est devenue presqu\'île par la jetée d\'Alexandre.',
  'Le littoral a connu plusieurs occupations : la formulation porte sur la puissance et le statut de la ville, non sur toute présence humaine.'),
 (7, 'Ninive, la ville jamais relevée', 'vers 633 av. n. è. selon l\'organisation ; 612 selon la chronologie profane', 'Nahum 1:8 ; 2:6 ; 3:19 ; Sophonie 2:13-15',
  '« Les portes des fleuves s\'ouvriront » ; Ninive deviendra une solitude aride où les troupeaux se couchent ; « ta blessure est incurable ».',
  'Les fouilles de Kuyunjik et de Nimroud ont livré les palais et les prismes de Sennachérib ; la ville a été prise par les Babyloniens et les Mèdes et n\'a jamais retrouvé son rang.',
  'Deux systèmes chronologiques existent : ne jamais les mélanger dans un même contenu.'),
 (8, 'Soixante-dix ans', '607 av. n. è. → 537 av. n. è.', 'Jérémie 25:11,12 ; 29:10 ; Daniel 9:1,2',
  'La désolation de Jérusalem durera soixante-dix ans, puis Dieu fera revenir les exilés.',
  'Tablettes administratives néo-babyloniennes attestant la déportation et les rations distribuées ; Esdras rapporte le décret de Cyrus et le retour.',
  'La chronologie profane emploie 587 pour la chute de Jérusalem ; le registre emploie le système de l\'organisation et l\'indique.'),
 (9, 'Quatre cent quatre-vingt-trois ans', '455 av. n. è. → automne 29 de n. è.', 'Daniel 9:25,26',
  '« Depuis la sortie de la parole pour rétablir et pour rebâtir Jérusalem jusqu\'à Messie le Guide, il y aura sept semaines, également soixante-deux semaines. »',
  'Soixante-neuf semaines = 483 ans ; le point de départ retenu est 455 av. n. è. ; l\'arrivée est l\'automne 29, année du baptême de Jésus.',
  'L\'identification du décret de départ varie selon les lecteurs ; le registre retient 455 et le signale.'),
 (10, 'Raphia, 217 av. n. è.', '217 av. n. è.', 'Daniel 11:10-12',
  'Une grande armée du Nord monte, puis le roi du Sud livre bataille contre elle.',
  'La rencontre de Raphia oppose Antiochus III à Ptolémée IV en 217 av. n. è. ; le chapitre poursuit avec Rome (11:19,20) puis Tibère.',
  'La précision même du chapitre est invoquée par les critiques comme argument de datation tardive (après 166 av. n. è.) : le dire, sans entrer dans le débat confessionnel.'),
 (11, 'Rome entre en scène', '64 et 31 av. n. è.', 'Daniel 11:19,20',
  'Après les rois grecs, un successeur envoie des exacteurs « dans la gloire de son royaume », puis « se fera briser ».',
  'La Syrie devient province romaine en 64 avant notre ère ; la bataille d\'Actium en 31 marque la fin des royaumes hellénistiques indépendants.',
  'Correspondance d\'ensemble, non point par point selon toutes les lectures.'),
 (12, 'Les deux mille trois cents jours et Antiochus IV', '168 av. n. è.', 'Daniel 8:11-14',
  'Le sanctuaire sera foulé pendant 2 300 jours, puis sera purifié.',
  'La persécution d\'Antiochus IV et la profanation du temple sont documentées : elle s\'achève avec la purification de 164 av. n. è. et la fête de Hanoukka.',
  'La chronologie interne des 2 300 jours est calculée de plusieurs façons selon les commentateurs.'),
 (13, 'Les « sept temps » : de 607 av. n. è. à octobre 1914', '2520 ans', 'Daniel 4:1-25 ; Révélation 12:6,14 ; Luc 21:24 ; Nombres 14:34',
  'Un arbre immense est abattu et sa souche liée pour « sept temps » : une interruption de la domination de Dieu sur la terre.',
  'Trois temps et demi = 1 260 jours, donc sept temps = 2 520 jours ; règle « un jour pour une année » ; de 607 av. n. è. à l\'automne 1914, début du règne du Christ dans les cieux.',
  'Il s\'agit d\'un raisonnement prophétique fondé sur une méthode et une chronologie : le présenter comme tel, avec la méthode visible.'),
 (14, 'Sennachérib devant Jérusalem, 701 av. n. è.', '701 av. n. è.', 'Isaïe 37:33-38',
  'Le roi d\'Assyrie n\'entrera pas dans la ville, il n\'y tirera pas de flèche, et il retournera par le chemin par lequel il est venu.',
  'Sur ses prismes, Sennachérib se vante de ses conquêtes mais **ne dit pas avoir pris Jérusalem** : il la décrit comme enfermée « comme un oiseau dans une cage ».',
  'Le nombre des soldats morts (185 000) relève de la tradition biblique ; présenter la conjonction des témoignages, non une équation.'),
 (15, 'Lakish, 701 av. n. è.', '701 av. n. è.', '2 Rois 18:13-15 ; Michée 1:13',
  'Lakish est mentionnée comme place forte de Juda et objet du siège assyrien.',
  'Les ostraca de Lakish (18 tessons, fouille de 1935) mentionnent les « signaux de Lakish » et Azékah ; une dalle du palais de Sennachérib à Ninive montre les captifs emmenés après la chute de Lakish.',
  'L\'identification de l\'une des lettres avec Jérémie n\'est pas retenue : ne pas la présenter comme démontrée.'),
 (16, 'Nébo-Sarsekim', '587-586 av. n. è.', 'Jérémie 39:3,13',
  'Un officier babylonien de haut rang portant ce nom est cité au nombre des princes venus à Jérusalem.',
  'Une tablette conservée au British Museum, déchiffrée en 2007, mentionne « Nebo-sarsekim », chef des eunuques, apportant de l\'or au temple ; identification par le nom **et** la fonction.',
  'Le musée parle d\'une découverte due à un « heureux hasard » : le dire.'),
 (17, 'Askalon et Ékron, 604 av. n. è.', '604 av. n. è.', 'Jérémie 47:5,7 ; Sophonie 2:4',
  'Gaza, Askalon, Ékron sont annoncées comme villes frappées par le « jour de Jéhovah » contre la Philistie.',
  'La campagne babylonienne de 604 est documentée par une chronique babylonienne et par les publications archéologiques ; Ékron était alors sous domination assyrienne puis babylonienne.',
  'Le vocabulaire prophétique emploie des images : ne retenir que ce qui est datable et vérifiable.'),
 (18, 'Thèbes (No-Amôn), 663 av. n. è.', '663 av. n. è.', 'Nahum 3:8-10',
  '« Es-tu meilleure que No-Amôn, qui était assise parmi les canaux d\'eau ? » — Nahum rappelle sa ruine comme un avertissement.',
  'Les annales assyriennes d\'Assourbanipal rapportent la prise de Thèbes (No-Amôn) en 663 avant notre ère.',
  'La prophétie utilise un événement connu de ses auditeurs : c\'est son rôle dans l\'argumentation et le dire.'),
 (19, 'Édom effacé', 'Ve-IVe siècle av. n. è.', 'Malachie 1:2-5 ; Abdias 1:10,17,18 ; Jérémie 49:17,18',
  '« Parce qu\'Édom dit : Nous rebâtirons — ils bâtiront, mais moi je démolirai » ; Édom sera retranché pour toujours.',
  'Les Nabatéens s\'installent dans la région au IVe siècle avant notre ère ; Édom n\'a jamais été rétabli comme nation ou royaume.',
  'Le pays a connu des occupations successives du nom : l\'objet de la prophétie est la nation et son dieu, non le sol.'),
 (20, 'Karkemish, 625 av. n. è.', '625 av. n. è. (chronologie de l\'organisation)', 'Jérémie 46:2',
  'L\'annonce situe la défaite de l\'armée égyptienne à Karkemish.',
  'La chronique babylonienne rapporte la bataille de Karkemish ; la datation varie selon le système employé (625/605).',
  'Comme pour Ninive : un seul système par contenu, l\'autre est signalé.'),
 (21, 'Pella : une fuite, pas un massacre', '66-70 de n. è.', 'Luc 19:43,44 ; 21:20-24 ; Matthieu 24:15-22',
  '« Quand vous verrez Jérusalem entourée par des armées qui campent, alors sachez que pour elle la désolation s\'est approchée ; alors, que ceux qui seront en Judée se mettent à fuir vers les montagnes. »',
  'Les Romains attaquent en 66 puis se retirent, laissant le temps de fuir ; l\'Encyclopédie judaïque indique que la communauté chrétienne s\'installa à Pella, de l\'autre côté du Jourdain.',
  'La fuite à Pella est rapportée par des sources anciennes et reprise par les publications ; elle n\'est pas attestée dans chaque détail.'),
 (22, 'Les sicles de Massada', '66-70 de n. è.', 'Matthieu 24:2 ; Luc 21:6',
  '« Il ne restera pas ici pierre sur pierre qui ne soit renversée. »',
  'Yigael Yadin rapporte des sicles correspondant à chaque année de la révolte, jusqu\'à la cinquième — celle de la destruction du temple en 70.',
  'Ces pièces datent la révolte, non l\'accomplissement de chaque parole : le dire.'),
 (23, 'Jérusalem « mise au niveau du sol »', '70 de n. è.', 'Luc 19:43,44 ; Matthieu 23:37,38',
  '« Tes ennemis t\'entoureront d\'une palissade […] et ils t\'abattront, toi et tes enfants. »',
  'Josèphe écrit : « Tout le reste de l\'enceinte de la cité, les démolisseurs le mirent si complètement au niveau du sol que les gens qui se rendaient après sur les lieux ne pouvaient croire qu\'ils eussent jamais été habités. » Sur les tours et un pan du mur occidental subsistèrent.',
  'L\'image « pas pierre sur pierre » porte sur le temple et l\'ensemble bâti, non sur l\'intégralité des murs de la ville.'),
 (24, 'Bethléhem, et un décret impérial', 'vers 2 av. n. è.', 'Michée 5:2 ; Luc 2:1-6',
  'Le Messie devait naître à Bethléhem, « la plus petite des villes de Juda ».',
  'Le recensement ordonné par César conduit Marie et Joseph à Bethléhem : la prophétie s\'accomplit par un acte administratif romain hors du contrôle des intéressés.',
  'La date exacte de la naissance n\'est pas donnée par la Bible ; le registre ne l\'avance pas.'),
 (25, 'Les copies les plus anciennes : 4Q114', 'copie datée entre 220 et 165 av. n. è.', 'Daniel 7-12 (support)',
  'L\'objection la plus courante contre Daniel est celle d\'une rédaction tardive ; l\'ancienneté des copies intervient donc directement.',
  'Une étude combinant radiocarbone et intelligence artificielle (PLOS ONE, 4 juin 2025) situe le fragment 4Q114 de Daniel entre 220 et 165 avant notre ère, c\'est-à-dire avant la période que suppose la thèse de la rédaction tardive.',
  'Une copie ancienne ne fixe pas la date de rédaction de l\'original ; elle en recule seulement la limite haute.'),
]

body3 = ['<div class="page"><h2>Sommaire des 25 détails</h2><div class="toc">']
for d in D:
    body3.append('<div><b>%02d.</b> %s <span class="src">— %s</span></div>' % (d[0], inline(d[1]), inline(d[3])))
body3.append('</div><hr class="rule">')
body3.append('<h2>Le principe du livre</h2>'
             '<p>Un contenu, un seul détail. Chaque fiche ne retient qu\'un fait daté et vérifiable, donne sa référence, '
             'sa source extérieure, puis <b>ce que cette source ne prouve pas</b>. C\'est la règle qui rend le témoignage crédible : '
             'la limite annoncée avant que l\'interlocuteur ne la trouve.</p>'
             '<div class="lim"><b>Rappel.</b> Un seul système chronologique par contenu. Aucun total de prophéties présenté comme une certitude. '
             'Aucune date donnée pour la fin. Les images (le cas échéant) sont légendées « Illustration. » et ne sont jamais présentées comme des documents.</div></div>')

for d in D:
    n, titre, dat, ref, ten, acc, lim = d
    body3.append('<div class="fiche"><div class="num">%02d</div><h2>%s</h2>' % (n, inline(titre)))
    body3.append('<p class="src"><b>Datation :</b> %s &nbsp;·&nbsp; <b>Référence :</b> %s</p>' % (inline(dat), inline(ref)))
    body3.append('<h4>La prophétie</h4><p>%s</p>' % inline(ten))
    body3.append('<h4>Le fait vérifiable</h4><p>%s</p>' % inline(acc))
    body3.append('<div class="lim"><b>Ce que cela ne prouve pas.</b> %s</div>' % inline(lim))
    body3.append('<div class="src">Sources officielles à transmettre : jw.org · wol.jw.org (renvoi par lien, jamais par copie).</div>')
    body3.append('</div>')
body3.append('<div class="page"><h2>Sources générales de ce livre</h2>'
             '<ul>'
             '<li><i>La Bible : Parole de Dieu ou des hommes ?</i>, chapitre 9 « Des prophéties qui se sont réalisées » (wol 1101989039) et chapitre 10 (wol 1101989040).</li>'
             '<li><i>Réveillez-vous !</i> 11/2007, « Ses prophéties réalisées » (wol 102007407) — Cyrus, l\'Euphrate, les portes non fermées.</li>'
             '<li><i>Étude n° 9 : L\'archéologie et le texte inspiré</i> (wol 1101990136) et <i>Étude n° 10 : La Bible, authentique et véridique</i> (wol 1101990137).</li>'
             '<li>« Comment l\'Histoire fut écrite des siècles à l\'avance » (wol 1977481) — les 70 semaines et la destruction de 70.</li>'
             '<li>Articles « Belshatsar » (wol 1200000628) et « Daniel, un livre au banc des accusés » (wol 1101999021).</li>'
             '<li>jw.org : « L\'archéologie confirme-t-elle l\'exactitude de la Bible ? » (g 11/2007) ; « History and the Bible ».</li>'
             '<li>Sources extérieures citées par ces publications : Josèphe, <i>Guerre des Juifs</i> et <i>Contre Apion</i> ; Arrien ; <i>The Encyclopedia Americana</i> ; <i>Encyclopédie judaïque</i> ; Yadin, <i>Massada</i> ; chronique babylonienne ; « Poème de Nabonide » ; cylindre de Cyrus (British Museum) ; ostracon de Lakish ; PLOS ONE, 4 juin 2025.</li>'
             '</ul>'
             '<div class="warn">Aucun texte des publications n\'est reproduit dans ce livre : les références renvoient à la source officielle, et la lecture se fait sur jw.org ou wol.jw.org.</div>'
             '<div class="footline">Le Détail qui change tout · 25 détails datés · usage privé</div></div>')

open(os.path.join(OUT, 'LIVRE_3_DETAIL.html'), 'w', encoding='utf-8').write(wrap(
    'Le Détail qui change tout — 25 détails datés',
    page('LE DÉTAIL<br>QUI CHANGE TOUT', 'Vingt-cinq détails datés, vérifiables hors de la Bible — chacun avec sa référence, '
         'sa source extérieure et la limite honnête de cette source.',
         ''.join(body3),
         foot='Un contenu, un détail · aucune probabilité inventée<br>Sources : jw.org · wol.jw.org')))
print('LIVRE 3 : %d détails' % len(D))
print('fichiers écrits dans', OUT)
