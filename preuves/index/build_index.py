#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INDEX GÉNÉRAL — construit mécaniquement sur le registre (1 000 entrées).
Sept index, aucun commentaire :
  1. par livre (66 livres)
  2. par statut exact
  3. par partie (14 + récapitulatif)
  4. repérages automatiques par mot-clé : personnes · lieux · mesures de temps · mentions du futur
  5. index continu P001 → P1000 (référence seule)
Sortie : preuves/INDEX_GENERAL.html (aucune ressource externe, aucun script)
"""
import re, os, html

PREUVES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'INDEX_GENERAL.html')

FILES = ['16_REGISTRE_PROPHETIES.md', '17_REGISTRE_PROPHETIES_2.md',
         '18_REGISTRE_PROPHETIES_3.md', '19_REGISTRE_PROPHETIES_4.md',
         '20_REGISTRE_PROPHETIES_5.md', '21_REGISTRE_PROPHETIES_6.md',
         '23_REGISTRE_PROPHETIES_7.md']
PART_RE = re.compile(r'^#{1,3}\s*PARTIE\s+(\d+)\s*[—–-]\s*(.+?)\s*$')
ROW_RE = re.compile(r"^\|\s*P(\d{3,4})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")

entries, parts = [], []
for f in FILES:
    p = os.path.join(PREUVES, f)
    if not os.path.exists(p): continue
    cur_part, cur_sec = '', ''
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        m = PART_RE.match(line)
        if m:
            cur_part = m.group(2).strip(); cur_sec = ''
            if not parts or parts[-1] != cur_part: parts.append(cur_part)
            continue
        if line.startswith('## '):
            cur_sec = line[3:].strip(); continue
        r = ROW_RE.match(line)
        if r:
            entries.append({'n': int(r.group(1)), 'ref': html.unescape(r.group(2)), 'teneur': html.unescape(r.group(3)),
                            'accompl': html.unescape(r.group(4)), 'statut': html.unescape(r.group(5)),
                            'part': cur_part, 'sec': cur_sec})
entries.sort(key=lambda e: e['n'])
TOTAL = len(entries)

def esc(t): return html.escape(str(t), quote=False)

def ranges(nums):
    nums = sorted(set(nums)); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
        out.append('P%03d' % nums[i] if i == j else 'P%03d–P%03d' % (nums[i], nums[j]))
        i = j + 1
    return ', '.join(out)

BOOKS = ["Genèse","Exode","Lévitique","Nombres","Deutéronome","Josué","Juges","Ruth","1 Samuel","2 Samuel",
 "1 Rois","2 Rois","1 Chroniques","2 Chroniques","Esdras","Néhémie","Esther","Job","Psaume","Proverbes",
 "Ecclésiaste","Cantique des Cantiques","Isaïe","Jérémie","Lamentations","Ézéchiel","Daniel","Osée","Joël",
 "Amos","Abdias","Jonas","Michée","Nahum","Habacuc","Sophonie","Aggée","Zacharie","Malachie","Matthieu",
 "Marc","Luc","Jean","Actes","Romains","1 Corinthiens","2 Corinthiens","Galates","Éphésiens","Philippiens",
 "Colossiens","1 Thessaloniciens","2 Thessaloniciens","1 Timothée","2 Timothée","Tite","Philémon","Hébreux",
 "Jacques","1 Pierre","2 Pierre","1 Jean","2 Jean","3 Jean","Jude","Révélation"]

def book_of(ref):
    best = None
    for b in BOOKS:
        if ref.startswith(b) and (best is None or len(b) > len(best)): best = b
    return best

PERSONNES = ["Cyrus","Darius","Josias","Belshatsar","Nabuchodonosor","Nébucadnetsar","Alexandre","Antiochus","Sédécias",
 "Pierre","Paul","Jean le Baptiseur","Élie","Élisée","Gédéon","Samson","Moïse","Abraham","Jacob","Isaac","Joseph",
 "Éphraïm","Éli","Samuel","Saül","David","Salomon","Jéroboam","Achab","Ézéchias","Sennachérib","Hazaël","Hanania",
 "Pashhur","Michel","Gog","Magog","Melkisédec","Zorobabel","Aggée","Ébed-Mélek","Yekonia","Josué","Ismaïl","Ismaël",
 "Ésaü","Laban","Agar","Éliakim","Joaqim"]
LIEUX = ["Jérusalem","Babylone","Tyr","Ninive","Samarie","Égypte","Assyrie","Édom","Moab","Ammon","Damas","Gaza",
 "Askalon","Ékron","Ashdod","Lakish","Bethléem","Raphia","Sion","Jéricho","Pella","Madian","Canaan","Sinaï",
 "Euphrate","Jourdain","Tahpanhès","Anathoth","Topheth","Massada","Galaad","Sodome","Gomorrhe","Béthel","Élam","Suse"]
MESURES = ["année","ans","jours","semaines","semaine","temps fixés","mille ans","heures","mois"]
FUTUR = ["à venir", "en cours"]

def grep(words, field='all'):
    res = {}
    for w in words:
        hits = []
        for e in entries:
            hay = e['ref'] + ' ' + e['teneur'] + ' ' + e['accompl']
            if re.search(r'\b' + re.escape(w), hay, re.I): hits.append(e['n'])
        if hits: res[w] = hits
    return res

by_book = {b: [] for b in BOOKS}
for e in entries:
    b = book_of(e['ref'])
    if b: by_book[b].append(e['n'])
by_statut = {}
for e in entries: by_statut.setdefault(e['statut'], []).append(e['n'])
by_part = {}
for e in entries: by_part.setdefault(e['part'], []).append(e['n'])

CSS = """
@page { size: A4 portrait; margin: 14mm 12mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, "Times New Roman", serif; color: #16324F; background: #fff; font-size: 9.6pt; line-height: 1.4; margin: 0; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
h1 { font-size: 20pt; color: #0B2545; margin: 0 0 2mm; }
h2 { font-size: 13pt; color: #0B2545; margin: 0 0 2mm; border-bottom: 1.6pt solid #E9C46A; padding-bottom: 1.1mm; }
h3 { font-size: 10.5pt; color: #0B2545; margin: 3.5mm 0 1.4mm; }
.sub { color: #4A5A6A; font-size: 8.6pt; margin: 0 0 3mm; }
.hdr { border-top: 3pt solid #0B2545; padding-top: 3mm; margin-bottom: 4mm; }
table { width: 100%; border-collapse: collapse; font-size: 7.6pt; }
th { background: #0B2545; color: #fff; text-align: left; padding: 1.3mm; }
td { border-bottom: .4pt solid #D8D2C4; padding: 1.1mm; vertical-align: top; }
.n { font-family: "Courier New", monospace; font-size: 7pt; color: #0B2545; }
.nums { font-family: "Courier New", monospace; font-size: 6.9pt; color: #23405C; word-spacing: .4mm; }
.q { background: #F7F4EC; border-left: 2.4pt solid #E9C46A; padding: 2.4mm; margin-top: 3mm; font-size: 9pt; }
.lim { background: #F7F4EC; border: .5pt solid #D8D2C4; padding: 2.2mm; margin-top: 2.4mm; font-size: 8.2pt; }
.foot { font-size: 7.2pt; color: #4A5A6A; border-top: .5pt solid #D8D2C4; margin-top: 2mm; padding-top: 1.2mm; }
.cont { column-count: 4; column-gap: 4mm; font-size: 6.9pt; font-family: "Courier New", monospace; }
.cont div { break-inside: avoid; }
"""

H = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Index général du registre</title><style>%s</style></head><body>' % CSS]

# ---- page 1
H.append('<div class="page"><div class="hdr"><h1>INDEX GÉNÉRAL DU REGISTRE</h1>'
         '<div class="sub">Construit mécaniquement sur le registre : <b>%d entrées</b> (P001–P%03d) · %d parties · aucun commentaire ajouté.</div></div>'
         % (TOTAL, entries[-1]['n'], len(by_part)))
H.append('<table><thead><tr><th style="width:9mm">Index</th><th>Objet</th><th style="width:60mm">Ce qu\'il donne</th></tr></thead><tbody>')
rows = [
 ('1', 'Par livre', '66 lignes : le livre, le nombre d\'entrées qui le citent, la plage de numéros'),
 ('2', 'Par statut exact', 'chaque formulation de statut, son compte et la liste des numéros'),
 ('3', 'Par partie', 'les 14 parties et le tableau récapitulatif, avec comptes et plages'),
 ('4', 'Repérages par mot-clé', 'personnes nommées · lieux · mesures de temps · mentions du futur'),
 ('5', 'Index continu', 'les %d numéros avec leur seule référence biblique, pour vérification ligne à ligne' % TOTAL),
]
for a, b, c in rows:
    H.append('<tr><td class="n">%s</td><td><b>%s</b></td><td>%s</td></tr>' % (a, esc(b), esc(c)))
H.append('</tbody></table>')
H.append('<div class="q"><b>Mode d\'emploi.</b> Ces index ne sont pas une interprétation : ils recopient et classent ce qui figure déjà '
         'dans les tableaux du registre. Pour citer une ligne, on cite son numéro : « entrée P%03d, %s ». Pour vérifier un total, '
         'on additionne l\'index 3 : les comptes doivent égaler %d.</div>' % (entries[0]['n'], esc(entries[0]['ref']), TOTAL))
H.append('<div class="lim"><b>Avertissements repris du registre.</b> Aucun total dogmatique sur le nombre des prophéties messianiques. '
         'Un seul système chronologique par contenu : celui des publications de l\'organisation (désolation de Juda 607 av. n. è. ; retour 537 ; '
         'chute de Ninive 632 ; Jérusalem 607 ; désolation 70 de n. è.), la divergence profane étant signalée là où elle existe. '
         'Aucune date pour l\'avenir. Aucune reproduction de contenu protégé.</div>')
H.append('<div class="foot">Index général — généré par index/build_index.py · registre : fichiers 16 à 21 et 23</div></div>')

# ---- index 1 : par livre
H.append('<div class="page"><div class="hdr"><h2>Index 1 — par livre</h2>'
         '<div class="sub">Nombre d\'entrées du registre qui citent chaque livre ; plage des numéros.</div></div>')
H.append('<table><thead><tr><th>Livre</th><th style="width:14mm">Entrées</th><th>Numéros</th>'
         '<th style="width:14mm">Entrées</th><th>Numéros</th></tr></thead><tbody>')
for i in range(33):
    row = []
    for b in (BOOKS[i], BOOKS[i + 33]):
        nn = by_book[b]
        row.append('<td>%s</td><td class="n">%d</td><td class="n">%s</td>'
                   % (esc(b), len(nn), ranges(nn) if nn else '— (aucune entrée)'))
    H.append('<tr>%s</tr>' % ''.join(row))
H.append('</tbody></table><div class="q"><b>%d livres sur 66</b> comportent au moins une entrée. '
         'Sans entrée : %s.</div>'
         % (sum(1 for b in BOOKS if by_book[b]), esc(', '.join(b for b in BOOKS if not by_book[b]))))
H.append('<div class="foot">Index 1 — la colonne « entrées » compte les lignes du registre, y compris les renvois du tableau consolidé des prophéties messianiques.</div></div>')

# ---- index 2 : par statut
H.append('<div class="page"><div class="hdr"><h2>Index 2 — par statut exact</h2>'
         '<div class="sub">%d formulations distinctes telles qu\'elles figurent dans la colonne « statut ».</div></div>' % len(by_statut))
H.append('<table><thead><tr><th>Statut</th><th style="width:14mm">Nb</th><th>Numéros</th></tr></thead><tbody>')
for st, nn in sorted(by_statut.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    H.append('<tr><td>%s</td><td class="n">%d</td><td class="nums">%s</td></tr>' % (esc(st), len(nn), ranges(nn)))
H.append('</tbody></table><div class="foot">Total : %d entrées · aucune entrée sans statut.</div></div>' % TOTAL)

# ---- index 3 : par partie
H.append('<div class="page"><div class="hdr"><h2>Index 3 — par partie</h2>'
         '<div class="sub">Comptes à additionner pour vérifier le total général.</div></div>')
H.append('<table><thead><tr><th style="width:9mm">N°</th><th>Partie (intitulé du registre)</th><th style="width:16mm">Entrées</th><th>Numéros</th></tr></thead><tbody>')
for i, (p, nn) in enumerate(by_part.items(), 1):
    H.append('<tr><td class="n">%d</td><td>%s</td><td class="n">%d</td><td class="nums">%s</td></tr>' % (i, esc(p), len(nn), ranges(nn)))
H.append('<tr><td class="n"></td><td><b>TOTAL</b></td><td class="n"><b>%d</b></td><td class="n">P%03d – P%03d</td></tr>'
         % (TOTAL, entries[0]['n'], entries[-1]['n']))
H.append('</tbody></table><div class="foot">Le tableau récapitulatif final du registre (totaux par corpus, statuts, repères, garde-fous) figure dans le fichier 21.</div></div>')

# ---- index 4 : repérages
H.append('<div class="page"><div class="hdr"><h2>Index 4 — repérages automatiques par mot-clé</h2>'
         '<div class="sub">Recherche littérale dans les colonnes référence, teneur et accomplissement. Liste des mots employés ; à vérifier ligne par ligne.</div></div>')
for titre, words in (('Personnes nommées', PERSONNES), ('Villes, pays, régions', LIEUX), ('Mesures de temps', MESURES)):
    res = grep(words)
    H.append('<h3>%s — %d termes repérés sur %d essayés</h3>' % (esc(titre), len(res), len(words)))
    H.append('<table><thead><tr><th style="width:34mm">Terme</th><th style="width:14mm">Nb</th><th>Numéros</th></tr></thead><tbody>')
    for w, nn in sorted(res.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        H.append('<tr><td>%s</td><td class="n">%d</td><td class="nums">%s</td></tr>' % (esc(w), len(nn), ranges(nn)))
    H.append('</tbody></table>')
H.append('<h3>Mentions du futur dans la colonne statut</h3><table><thead><tr><th style="width:34mm">Mention</th><th style="width:14mm">Nb</th><th>Numéros</th></tr></thead><tbody>')
for w in FUTUR:
    nn = [e['n'] for e in entries if w in e['statut'].lower()]
    H.append('<tr><td>%s</td><td class="n">%d</td><td class="nums">%s</td></tr>' % (esc(w), len(nn), ranges(nn)))
H.append('</tbody></table>')
H.append('<div class="lim"><b>Nature de ce repérage.</b> Il s\'agit d\'une recherche de chaînes de caractères : un même mot peut désigner '
         'un lieu ou une personne différente selon le contexte (par exemple « Josué » le successeur de Moïse et « Josué » le grand prêtre ; '
         '« Éphraïm » la tribu et le territoire). Les numéros sont donnés à titre de repérage, jamais de comptage doctrinal. '
         'Les termes retenus sont ceux qui apparaissent effectivement dans le registre ; une liste plus longue n\'ajouterait que du bruit.</div>')
H.append('<div class="foot">Index 4 — repérage automatique · aucune interprétation · à vérifier ligne par ligne</div></div>')

# ---- index 5 : continu
H.append('<div class="page"><div class="hdr"><h2>Index 5 — les %d numéros et leur référence</h2>'
         '<div class="sub">Liste continue, référence seule : sert à vérifier qu\'aucun numéro ne manque et à retrouver une ligne par sa référence.</div></div>' % TOTAL)
H.append('<div class="cont">')
for e in entries:
    H.append('<div><span class="n">P%03d</span> %s</div>' % (e['n'], esc(e['ref'])))
H.append('</div><div class="foot">P001 → P%03d sans interruption · %d lignes · généré le jour de la construction du fichier</div></div>'
         % (entries[-1]['n'], TOTAL))

H.append('</body></html>')

path = os.path.abspath(OUT)
open(path, 'w', encoding='utf-8').write(''.join(H))
print('INDEX_GENERAL.html : %d entrées · %d livres · %d statuts · %d parties · %.0f Ko'
      % (TOTAL, sum(1 for b in BOOKS if by_book[b]), len(by_statut), len(by_part), os.path.getsize(path) / 1024))
print('   écrit :', path)
