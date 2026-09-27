#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit SITE_LOCAL.html : bibliothèque privée hors ligne.
Lit les 6 fichiers du registre (16 à 21), en extrait les 1 000 entrées,
puis génère une page HTML autonome (aucune ressource externe)."""
import re, json, os, glob, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)          # .../preuves

sys.path.insert(0, os.path.join(ROOT, 'fiches'))
from theme import THEME_CSS
SITE_CSS = '\n/* ---------- site REPERES (V2_THEME) ---------- */\n.wrap{max-width:1120px;}\nbody{font-size:16px;}\nheader.hero-site{position:relative;color:#fff;overflow:hidden;\n background:linear-gradient(135deg,#0B2545,#12345f 60%,#1a4a8a);}\nheader.hero-site img.fond{position:absolute;inset:0;width:100%;height:100%;\n object-fit:cover;opacity:.35;}\nheader.hero-site .voile{position:absolute;inset:0;\n background:linear-gradient(180deg,rgba(11,37,69,.2),rgba(11,37,69,.88));}\nheader.hero-site .contenu{position:relative;max-width:1120px;margin:0 auto;\n padding:38px 20px 28px;}\nheader.hero-site h1{font-size:clamp(22px,3.6vw,32px);margin:0 0 8px;\n line-height:1.15;}\nheader.hero-site .sub{color:#dbe4f2;font-size:14px;}\nnav{background:#0a1e38;position:sticky;top:0;z-index:20;\n border-bottom:3px solid var(--jw-or);}\nnav .wrap{display:flex;gap:6px;flex-wrap:wrap;padding-top:8px;\n padding-bottom:8px;}\nnav button{background:rgba(255,255,255,.10);border:0;color:#fff;\n padding:7px 15px;font:inherit;font-size:13px;font-weight:600;cursor:pointer;\n border-radius:18px;}\nnav button:hover{background:var(--jw-or);color:#0B2545;}\nnav button.on{background:var(--jw-or);color:#0B2545;}\nmain.wrap{padding-top:10px;}\nsection{display:none;}\nsection.on{display:block;animation:fondu .3s ease;}\n@keyframes fondu{from{opacity:0;transform:translateY(6px);}to{opacity:1;}}\nh2{color:var(--jw-bleu-fonce);border-bottom:3px solid var(--jw-or);\n padding-bottom:8px;margin-top:34px;font-size:clamp(20px,3vw,26px);}\nh3{color:var(--jw-bleu-fonce);}\n.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));\n gap:12px;margin:18px 0;}\n.stat{background:#fff;border:1px solid var(--bord);border-left:5px solid\n var(--jw-or);border-radius:10px;padding:12px 14px;\n box-shadow:var(--ombre-legere);}\n.stat b{display:block;font-size:26px;color:var(--jw-bleu-fonce);}\n.stat span{font-size:13px;color:var(--gris);}\n.tools{display:flex;gap:10px;flex-wrap:wrap;align-items:center;background:#fff;\n border:1px solid var(--bord);border-radius:12px;padding:12px;margin:14px 0;\n box-shadow:var(--ombre-legere);}\ninput[type=search],select{font:inherit;padding:9px 11px;\n border:1px solid #c9c2ae;border-radius:8px;background:#fff;min-width:170px;}\ninput[type=search]{flex:1 1 300px;}\n.count{font-size:14px;color:var(--gris);}\n.e{background:#fff;border:1px solid var(--bord);border-radius:12px;\n padding:12px 14px;margin:9px 0;display:grid;grid-template-columns:64px 1fr;\n gap:12px;box-shadow:var(--ombre-legere);}\n.e .num{font-weight:700;color:var(--jw-bleu-fonce);background:#f2ecd9;\n border-radius:8px;text-align:center;padding:6px 2px;height:fit-content;\n font-size:14px;}\n.e .ref{font-weight:700;color:var(--jw-bleu-fonce);}\n.e .t{margin:3px 0;}\n.e .a{font-size:14px;color:#40506b;}\n.e .meta{margin-top:7px;font-size:12px;color:#7b8aa3;display:flex;gap:8px;\n flex-wrap:wrap;align-items:center;}\n.badge{font-size:11px;padding:2px 9px;border-radius:11px;color:#fff;\n white-space:nowrap;}\n.s1{background:#2e7d5b;}.s6{background:#2b6f8f;}.s7{background:#8e8b7a;}\n.s2{background:#4a7fbf;}.s3{background:#b26a1f;}.s4{background:#8a3b3b;}\n.s5{background:#4a3b8a;}\n.part{background:#fff;border:1px solid var(--bord);border-radius:12px;\n padding:12px 14px;cursor:pointer;text-align:left;font:inherit;\n box-shadow:var(--ombre-legere);transition:transform .2s ease;}\n.part:hover{border-color:var(--jw-or);transform:translateY(-3px);}\n.part b{display:block;color:var(--jw-bleu-fonce);}\n.part span{font-size:13px;color:var(--gris);}\n.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));\n gap:12px;}\n.preuve{background:#fff;border:1px solid var(--bord);border-radius:12px;\n padding:14px;position:relative;box-shadow:var(--ombre-legere);}\n.preuve .pn{position:absolute;top:8px;right:12px;font-size:28px;font-weight:800;\n color:#eadfc0;}\n.preuve h3{margin:0 0 6px;padding-right:34px;font-size:17px;}\n.preuve p{margin:6px 0;font-size:14px;}\n.pl{font-size:13px;color:var(--gris);}\n.lnk{background:none;border:0;color:var(--jw-bleu);text-decoration:underline;\n cursor:pointer;font:inherit;padding:0;}\n.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));\n gap:12px;}\n.gal figure{margin:0;background:#fff;border:1px solid var(--bord);\n border-radius:12px;overflow:hidden;box-shadow:var(--ombre-legere);\n transition:transform .2s ease;}\n.gal figure:hover{transform:translateY(-4px);}\n.gal img{width:100%;height:150px;object-fit:cover;display:block;\n background:#e9e3d2;}\n.gal figcaption{font-size:11px;padding:6px 9px;color:var(--gris);}\n#audList{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));\n gap:10px;}\nli.aud{list-style:none;background:#fff;border:1px solid var(--bord);\n border-radius:12px;padding:10px 12px;margin:0;font-size:13px;\n box-shadow:var(--ombre-legere);}\nli.aud .audt{font-weight:700;color:var(--jw-bleu-fonce);margin-bottom:4px;\n font-size:12.5px;}\naudio{width:100%;height:36px;margin:4px 0 0;}\nul.clean{list-style:none;padding:0;}\nul.rules{list-style:none;padding:0;}\nul.rules li{background:#fff;border-left:5px solid var(--jw-or);border-radius:8px;\n padding:10px 14px;margin:9px 0;box-shadow:var(--ombre-legere);}\nul.rules strong{display:block;color:var(--jw-bleu-fonce);}\nul.rules span{font-size:14px;color:#40506b;}\n.more{margin:14px 0;padding:10px 20px;border:0;background:var(--jw-bleu-fonce);\n color:#fff;border-radius:22px;cursor:pointer;font:inherit;font-weight:600;}\n.more:hover{background:var(--jw-bleu);}\n.note{background:#fdf7e4;border:1px solid #e8d9a8;border-radius:10px;\n padding:12px 14px;font-size:14px;}\n.warn{background:#fdeeee;border:1px solid #e6c4c4;border-radius:10px;\n padding:12px 14px;font-size:14px;}\nfooter{background:var(--jw-bleu-fonce);color:#cfe0f5;padding:22px 0;\n font-size:13px;margin-top:30px;}\nfooter .wrap{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;}\n@media print{nav,.tools,.more,footer,audio{display:none;}body{background:#fff;}\n .e{break-inside:avoid;}}\n'
CSS_FULL = THEME_CSS + SITE_CSS
try:
    DUREES = json.load(open(os.path.join(ROOT, 'collections', 'durations.json'), encoding='utf-8'))
except (OSError, ValueError):
    DUREES = {}

FILES = ['16_REGISTRE_PROPHETIES.md', '17_REGISTRE_PROPHETIES_2.md',
         '18_REGISTRE_PROPHETIES_3.md', '19_REGISTRE_PROPHETIES_4.md',
         '20_REGISTRE_PROPHETIES_5.md', '21_REGISTRE_PROPHETIES_6.md',
         '23_REGISTRE_PROPHETIES_7.md']

PART_RE = re.compile(r'^#{1,3}\s*PARTIE\s+(\d+)\s*[—–-]\s*(.+?)\s*$')
HEAD_RE = re.compile(r'^(#{2,3})\s+(.+?)\s*$')
ROW_RE = re.compile(r'^\|\s*P(\d{3,4})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$')
NUM_RE = re.compile(r'^\d+(?:\.\d+)?\s+')

entries = []
for fn in FILES:
    n = 0
    part, section = '', ''
    for line in open(os.path.join(ROOT, fn), encoding='utf-8'):
        m = PART_RE.match(line)
        if m:
            part = m.group(2)
            section = ''
            continue
        h = HEAD_RE.match(line)
        if h:
            t = NUM_RE.sub('', h.group(2)).strip()
            if t and not t.startswith(('SUITE', 'RÈGLES', 'RAPPEL', 'PLAN', 'Récapitulatif')):
                section = t
            continue
        r = ROW_RE.match(line)
        if r:
            n += 1
            entries.append({'n': int(r.group(1)), 'ref': r.group(2), 'teneur': r.group(3),
                            'accompl': r.group(4), 'statut': r.group(5),
                            'part': part, 'section': section})

def groupe(st):
    t = st.lower()
    if 'identifiée' in t: return 'Accomplie (identifiée)'
    if '1er accomplissement' in t and ('à venir' in t or 'en cours' in t): return '1er accomplissement + suite'
    if '1er accomplissement' in t: return 'Accomplie (1er accomplissement)'
    if t.startswith('accomplie') and ('à venir' in t or 'en cours' in t): return 'Accomplie + suite à venir'
    if t.startswith('en cours'): return 'En cours'
    if t.startswith('à venir'): return 'À venir'
    return 'Accomplie'

for e in entries:
    e['groupe'] = groupe(e['statut'])
entries.sort(key=lambda e: e['n'])
nums = [e['n'] for e in entries]

def collect(kind):
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, kind, '*'))):
        b = os.path.basename(p)
        if b.lower().endswith(('.jpg', '.jpeg', '.png', '.mp3')):
            out.append(kind + '/' + b)
    return out

images = [p for p in collect('images') if not p.lower().endswith('.mp3')]
audios = collect('audio') + [p for p in collect('images') if p.lower().endswith('.mp3')]

parts = []
for e in entries:
    if not parts or parts[-1]['nom'] != e['part']:
        parts.append({'nom': e['part'], 'de': e['n'], 'a': e['n'], 'n': 1})
    else:
        parts[-1]['a'] = e['n']; parts[-1]['n'] += 1

parts.append({'nom': 'TABLEAU RÉCAPITULATIF FINAL', 'de': 0, 'a': 0, 'n': 0})

def tally(key):
    d = {}
    for e in entries:
        d[e[key]] = d.get(e[key], 0) + 1
    return dict(sorted(d.items(), key=lambda kv: -kv[1]))

DATA = {
    'entries': entries,
    'parts': parts,
    'statuts': tally('statut'),
    'groupes': tally('groupe'),
    'sections': tally('section'),
    'images': images,
    'audios': audios,
    'durees': DUREES,
    'min': min(nums), 'max': max(nums), 'total': len(entries),
}

PREUVES = [
    (1, 'Un roi nommé deux siècles à l\'avance', 'Isaïe 44:28 ; 45:1 — le cylindre de Cyrus atteste le nom et la politique de retour des captifs.', 'P155-P162'),
    (2, 'Babylone prise en une seule nuit', 'Jérémie 50:38 ; 51:36 — eaux taries ; 539 av. n. è., 5-6 octobre.', 'P238-P245'),
    (3, 'Tyr : trois détails qui se complètent', 'Ézéchiel 26:3-5, 12, 14 — siège de 13 ans (Josèphe), puis la chaussée d\'Alexandre.', 'P335-P344'),
    (4, 'Ninive, la ville jamais relevée', 'Nahum 2:6 ; Sophonie 2:13-15 — chute « v. 633 » (organisation) / 612 (profane).', 'P447-P450 ; P463-P469 ; P479-P482'),
    (5, 'Soixante-dix ans, comptés par un païen', 'Jérémie 25:11,12 — 607 → 537 ; tablettes administratives à l\'appui.', 'P221 ; P222 ; P385'),
    (6, 'Les soixante-dix semaines', 'Daniel 9:25 — 455 → automne 29 de n. è. ; puis 33, puis 70.', 'P385 ; P639-P641'),
    (7, 'Daniel 11 : une guerre nommée par son lieu', 'Daniel 11:10-12 — Raphia, 217 av. n. è. ; objection de datation tardive mentionnée.', 'P387-P402'),
    (8, 'Les « sept temps » : de 607 av. n. è. à 1914', 'Daniel 4 ; Révélation 12:6,14 — 2 520 ans ; règle jour-année (Nombres 14:34).', 'P370-P371 ; P690'),
    (9, 'Le signe composite et la prédication mondiale', 'Matthieu 24:4-14 — douze marques simultanées ; plus de 1 090 langues.', 'P647-P666'),
    (10, 'Jérusalem 66-70 : une fuite, pas un massacre', 'Luc 21:20-24 — retrait romain en 66, fuite vers Pella, destruction en 70.', 'P679-P690'),
    (11, 'Ésaïe 53 : douze détails sur le Serviteur', 'Isaïe 53:3-12 — trois détails hors de portée du condamné.', 'P624-P627 ; P629-P638 ; P643'),
    (12, 'Ce qui est en cours et ce qui vient', 'Révélation 6 ; 11 ; 13 ; 16-21 — 1914, 1920, 1919 ; puis Har-Maguédôn et le millénium.', 'P820-P836 ; P852-P856 ; P874 ; P898-P1000'),
]

LINKS = [
    ('La Bible et vous — commencer à lire', 'https://www.jw.org/fr/la-bible-et-vous/'),
    ('La Bible et la science', 'https://www.jw.org/fr/la-bible-et-vous/science/'),
    ('La Bible et l\'Histoire', 'https://www.jw.org/fr/la-bible-et-vous/histoire/'),
    ('Demandez une visite', 'https://www.jw.org/fr/temoins-de-jehovah/demandez-une-visite/'),
    ('Bibliothèque en ligne (wol)', 'https://wol.jw.org/fr/wol/h/r30/lp-f'),
    ('Rechercher dans les publications', 'https://wol.jw.org/fr/wol/s/r30/lp-f'),
]

RULES = [
    ('Un contact à la fois', 'Jamais d\'envoi de masse, jamais de contact à froid, jamais vers un autre pays.'),
    ('On ne copie pas, on renvoie', 'Aucun contenu de l\'organisation n\'est reproduit : on transmet un lien vers jw.org ou wol.jw.org.'),
    ('Aucun dogme dans les contenus d\'entrée', 'On présente des faits vérifiables et des critères ; la personne conclut elle-même.'),
    ('On énonce les limites, pas seulement les preuves', 'Ce qui est solide, ce qui est un raisonnement, ce qui relève de la compréhension.'),
    ('Tout aboutit au dispositif officiel', 'jw.org, wol.jw.org, ou le formulaire « Demandez une visite ». Jamais un site personnel.'),
]

data_json = json.dumps(DATA, ensure_ascii=False, separators=(',', ':'))
assert '</script' not in data_json.lower()

preuves_html = '\n'.join(
    f'<article class="preuve" id="p{p[0]}"><div class="pn">{p[0]:02d}</div><h3>{p[1]}</h3>'
    f'<p>{p[2]}</p><p class="pl">Registre : <button class="lnk" data-pref="{p[3]}">{p[3]}</button></p></article>'
    for p in PREUVES)

links_html = '\n'.join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in LINKS)
rules_html = '\n'.join(f'<li><strong>{t}</strong><span>{d}</span></li>' for t, d in RULES)

FICHES_PAGES = [
 ("FICHES_A_NATIONS.html", "A", "Contre les nations", "prophe_A_couverture.jpg", 9),
 ("FICHES_B_JERUSALEM.html", "B", "Jérusalem et Juda", "prophe_B_couverture.jpg", 9),
 ("FICHES_C_MESSIE_1.html", "A–C", "Fin des nations · Messie (1)", "prophe_AC_couverture.jpg", 9),
 ("FICHES_C_MESSIE_2.html", "C", "Le Messie (2)", "prophe_C2_couverture.jpg", 9),
 ("FICHES_D_PASSION_1.html", "D", "Passion (1)", "prophe_D_couverture.jpg", 9),
 ("FICHES_E_EMPIRES_1.html", "D–E", "Passion (2) · Empires (1)", "prophe_DE_couverture.jpg", 9),
 ("FICHES_F_CHRONO_1.html", "E–F", "Empires (2) · Chronologies", "prophe_EF_couverture.jpg", 9),
 ("FICHES_G_RESTAURATION_1.html", "F–G", "Chronologies (2) · Restauration", "prophe_FG_couverture.jpg", 9),
 ("FICHES_H_SIGNE_1.html", "G–H", "Restauration (2) · Le signe", "prophe_GH_couverture.jpg", 9),
 ("FICHES_I_REVELATION_1.html", "H–I", "Le signe (2) · Révélation", "prophe_HI_couverture.jpg", 9),
 ("FICHES_J_NOMMES_1.html", "I–J", "Révélation (2) · Nommés (1)", "prophe_IJ_couverture.jpg", 9),
 ("FICHES_J_NOMMES_2.html", "J", "Nommés d’avance (2)", "prophe_J2_couverture.jpg", 8),
 ("FICHES_K_SCIENCE_1.html", "J–K", "Nommés (3) · Science (1)", "prophe_JK_couverture.jpg", 7),
 ("FICHES_L_GEO_1.html", "K–L", "Science (2) · Géographie (1)", "prophe_KL_couverture.jpg", 9),
 ("FICHES_L_GEO_2.html", "L", "Géographie (2)", "prophe_L2_couverture.jpg", 3),
 ("FICHES_R_RELIQUATS.html", "R", "Reliquats", "prophe_R_couverture.jpg", 6),
 ("FICHES_S_PSAUMES.html", "S", "Psaumes", "prophe_S_couverture.jpg", 6),
 ("FICHES_T_JEREMIE_1.html", "T", "Jérémie (1) : le jugement", "prophe_T_couverture.jpg", 6),
 ("FICHES_T_JEREMIE_2.html", "T", "Jérémie (2) : la restauration", "prophe_T_couverture.jpg", 6),
]
fiches_html = "\n".join(
    '<div class="carte"><a class="img" href="%s">'
    '<img loading="lazy" src="images/%s" alt=""></a>'
    '<div class="txt"><div class="num">DOSSIER %s</div>'
    '<h3><a href="%s">%s</a></h3>'
    '<div class="meta">%d fiches · illustré · audio</div></div></div>'
    % (fn, cov, code, fn, nom, nb) for fn, code, nom, cov, nb in FICHES_PAGES)

HTML = r'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>REPÈRES — Bibliothèque privée des prophéties bibliques et de leurs accomplissements</title>
<style>
__CSS__
</style>
</head>
<body>
<header class="hero-site"><img class="fond" src="images/site_bibliotheque_perso.jpg" alt=""><div class="voile"></div><div class="contenu">
<div class="kicker">Bibliothèque privée · hors ligne</div>
<h1>REPÈRES — Prophéties bibliques et accomplissements</h1>
<div class="sub">Registre exhaustif : <b id="hTotal">1000</b> entrées · 14 parties · 19 dossiers de fiches · usage strictement personnel et privé</div>
</div></header>
<nav><div class="wrap">
<button data-tab="accueil" class="on">Accueil</button>
<button data-tab="registre">Les 1 000 entrées</button>
<button data-tab="parties">Les 14 parties</button>
<button data-tab="preuves">Les 12 preuves</button>
<button data-tab="medias">Médias</button>
<button data-tab="liens">Liens officiels</button>
<button data-tab="regles">Règles d'usage</button>
</div></nav>
<main class="wrap">

<section id="accueil" class="on">
<h2>Ce que contient cette bibliothèque</h2>
<p>Ce dossier rassemble un <b>registre exhaustif et sans commentaire</b> des prophéties bibliques et de leurs accomplissements : chaque ligne donne quatre éléments — la référence, la teneur, l'accomplissement, le statut. Les entrées sont numérotées de <b>P001</b> à <b>P1000</b>, classées par corpus biblique, et réparties en <b>14 parties</b>, avec un tableau récapitulatif final.</p>
<div class="stats">
<div class="stat"><b id="sTotal">1000</b><span>entrées vérifiées</span></div>
<div class="stat"><b id="sParts">14</b><span>parties</span></div>
<div class="stat"><b id="sImg">49</b><span>illustrations</span></div>
<div class="stat"><b id="sAud">68</b><span>audios français</span></div>
</div>
<h2>Comment lire le registre</h2>
<p>Les quatre statuts employés : <span class="badge s1">Accomplie</span> <span class="badge s2">Accomplie (1er accomplissement)</span> <span class="badge s3">En cours</span> <span class="badge s4">À venir</span> — plus, lorsque l'identification est établie, <span class="badge s5">Accomplie (identifiée)</span>.</p>
<div class="note">Ce contenu suit la compréhension des Témoins de Jéhovah et renvoie, pour toute vérification, aux publications officielles sur <b>jw.org</b> et <b>wol.jw.org</b>. Aucun texte de ces publications n'est reproduit ici : les liens sont fournis, la lecture se fait à la source.</div>
<h2>Trois règles de lecture</h2>
<ul class="rules">
<li><strong>Un seul système chronologique par contenu</strong><span>Le registre emploie le système de datation de l'organisation (Jérusalem 607 av. n. è.). Quand la chronologie profane courante diffère, elle est signalée — par exemple Ninive : « v. 633 » / 612.</span></li>
<li><strong>Aucun total présenté comme une certitude</strong><span>Le nombre des prophéties messianiques n'est jamais donné comme un chiffre dogmatique : c'est un inventaire de travail.</span></li>
<li><strong>Aucune date de la fin</strong><span>Le registre décrit des signes et des accomplissements ; il ne fixe aucune date pour l'issue finale.</span></li>
</ul>
<h2>Les 19 dossiers de fiches</h2>
<p>150 fiches illustrées et lues en français : chaque dossier s’ouvre dans son fichier, à partager seul, en privé.</p>
<div class="grille">
__FICHES__
</div>
<h2>Par où commencer</h2>
<ul class="clean">
<li>→ <button class="lnk" data-goto="preuves">Les 12 preuves</button> : les dossiers prêts à présenter, avec leurs limites honnêtes.</li>
<li>→ <button class="lnk" data-goto="registre">Les 1 000 entrées</button> : la recherche par mot, par partie, par statut.</li>
<li>→ <button class="lnk" data-goto="liens">Liens officiels</button> : les seules destinations à transmettre, en privé.</li>
</ul>
</section>

<section id="registre">
<h2>Le registre — 1 000 entrées</h2>
<div class="tools">
<input type="search" id="q" placeholder="Rechercher : Cyrus, Tyr, 539, Michée 5:2, résurrection…">
<select id="fGrp"><option value="">Toutes les familles de statut</option></select>
<select id="fPart"><option value="">Toutes les parties</option></select>
<select id="fStat"><option value="">Tous les statuts</option></select>
<select id="fSect"><option value="">Toutes les sections</option></select>
<button class="lnk" id="reset">réinitialiser</button>
</div>
<div class="count" id="count"></div>
<div id="list"></div>
<button class="more" id="more">Afficher 50 entrées de plus</button>
</section>

<section id="parties">
<h2>Les 14 parties du registre</h2>
<p>Cliquez sur une partie pour ouvrir ses entrées dans la recherche.</p>
<div class="grid" id="partsGrid"></div>
</section>

<section id="preuves">
<h2>Les 12 grandes preuves</h2>
<p>Chaque preuve comporte : l'accroche, le fait vérifiable, la prophétie, l'accomplissement, les sources et leurs limites, la question qui ouvre, et les formats de sortie. Le détail complet figure dans le fichier <b>22_GRAND_DOSSIER.md</b>.</p>
<div class="grid">
__PREUVES__
</div>
</section>

<section id="medias">
<h2>Illustrations</h2>
<div class="note">Toutes les images sont des <b>illustrations</b> générées : elles ne sont jamais présentées comme des documents historiques. Elles s'affichent lorsque la bibliothèque est ouverte localement, depuis son dossier.</div>
<div class="gal" id="gal"></div>
<h2>Audios en français</h2>
<p>Lecture du registre et du Grand Dossier : <b id="sAud2">169</b> pistes, dans le dossier <b>audio/</b>.</p>
<ul class="clean" id="audList"></ul>
</section>

<section id="liens">
<h2>Liens officiels — les seules destinations à transmettre</h2>
<div class="warn">Règle absolue : aucun site, blog, groupe ou page personnelle. On transmet un lien officiel, en privé, à une personne à la fois.</div>
<ul class="clean">
__LINKS__
</ul>
<p style="font-size:13px;color:#5a6b85">Ces liens ouvrent les sites officiels des Témoins de Jéhovah. Aucun contenu de ces sites n'est recopié dans cette bibliothèque.</p>
</section>

<section id="regles">
<h2>Règles d'usage de cette bibliothèque</h2>
<ul class="rules">
__RULES__
</ul>
<h2>Le périmètre</h2>
<ul class="clean">
<li>Bibliothèque <b>privée, locale</b> : les fichiers restent sur l'appareil.</li>
<li>Partage <b>fichier par fichier</b>, à une personne à la fois.</li>
<li>Aucune collecte ni stockage de données personnelles.</li>
<li>Aucune reproduction de contenu protégé : les références renvoient aux publications officielles.</li>
<li>Une IA n'est jamais présentée comme un humain ; aucun bot ne prêche ni n'enseigne à la place d'un proclamateur.</li>
</ul>
</section>

</main>
<footer><div class="wrap">
<div>REPÈRES — registre exhaustif des prophéties et de leurs accomplissements · <b id="fTotal">1000</b> entrées · contenu privé</div>
<div>Destinations : jw.org · wol.jw.org</div>
</div></footer>

<script id="data" type="application/json">__DATA__</script>
<!--APP_JS_START-->
<script>
(function(){
  "use strict";
  var D = JSON.parse(document.getElementById('data').textContent);
  var E = D.entries, shown = 50, filtered = E;

  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function cls(g){
    if(/identifiée/i.test(g)) return 's5';
    if(/1er accomplissement/i.test(g)) return 's2';
    if(/^En cours/i.test(g)) return 's3';
    if(/^À venir/i.test(g)) return 's4';
    if(/suite/i.test(g)) return 's6';
    return 's1';
  }
  function byId(id){ return document.getElementById(id); }
  function opt(sel, vals){
    var s = byId(sel);
    vals.forEach(function(v){
      var o = document.createElement('option');
      o.value = v; o.textContent = v + ' (' + D.statuts[v] + ')';
      if(sel === 'fPart'){ var pp = D.parts.filter(function(p){return p.nom===v;})[0]||{n:''}; o.textContent = v.split(' — ')[0] + ' — ' + pp.n + ' entrées'; }
      if(sel === 'fSect'){ o.textContent = v + ' (' + D.sections[v] + ')'; }
      s.appendChild(o);
    });
  }

  function row(e){
    return '<article class="e"><div class="num">P' + String(e.n).padStart(3,'0') + '</div><div>' +
      '<div class="ref">' + esc(e.ref) + '</div>' +
      '<div class="t">' + esc(e.teneur) + '</div>' +
      '<div class="a"><b>Accomplissement :</b> ' + esc(e.accompl) + '</div>' +
      '<div class="meta"><span class="badge ' + cls(e.groupe) + '">' + esc(e.statut) + '</span>'
      + '<span class="badge s7">' + esc(e.groupe) + '</span>' +
      '<span>' + esc(e.part) + (e.section ? ' · ' + esc(e.section) : '') + '</span></div>' +
      '</div></article>';
  }

  function render(){
    var q = byId('q').value.trim().toLowerCase();
    var p = byId('fPart').value, st = byId('fStat').value, se = byId('fSect').value, g = byId('fGrp').value;
    filtered = E.filter(function(e){
      if(g && e.groupe !== g) return false;
      if(p && e.part !== p) return false;
      if(st && e.statut !== st) return false;
      if(se && e.section !== se) return false;
      if(q){
        var hay = (e.ref + ' ' + e.teneur + ' ' + e.accompl + ' P' + e.n).toLowerCase();
        if(hay.indexOf(q) === -1) return false;
      }
      return true;
    });
    var slice = filtered.slice(0, shown);
    byId('list').innerHTML = slice.map(row).join('') || '<p class="note">Aucune entrée ne correspond à cette recherche.</p>';
    byId('count').textContent = filtered.length + ' entrée(s) affichée(s) sur ' + E.length +
      (filtered.length ? ' — de P' + String(filtered[0].n).padStart(3,'0') + ' à P' + String(filtered[filtered.length-1].n).padStart(3,'0') : '');
    byId('more').style.display = shown < filtered.length ? '' : 'none';
  }

  ['q','fGrp','fPart','fStat','fSect'].forEach(function(id){
    byId(id).addEventListener('input', function(){ shown = 50; render(); });
    byId(id).addEventListener('change', function(){ shown = 50; render(); });
  });
  byId('more').addEventListener('click', function(){ shown += 50; render(); });
  byId('reset').addEventListener('click', function(){
    byId('q').value = ''; byId('fGrp').value = ''; byId('fPart').value = ''; byId('fStat').value = ''; byId('fSect').value = '';
    shown = 50; render();
  });

  function tab(name){
    Array.prototype.forEach.call(document.querySelectorAll('section'), function(s){ s.classList.toggle('on', s.id === name); });
    Array.prototype.forEach.call(document.querySelectorAll('nav button'), function(b){ b.classList.toggle('on', b.dataset.tab === name); });
    window.scrollTo(0, 0);
  }
  Array.prototype.forEach.call(document.querySelectorAll('nav button'), function(b){
    b.addEventListener('click', function(){ tab(b.dataset.tab); });
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-goto]'), function(b){
    b.addEventListener('click', function(){ tab(b.dataset.goto); });
  });
  Array.prototype.forEach.call(document.querySelectorAll('[data-pref]'), function(b){
    b.addEventListener('click', function(){
      tab('registre');
      var r = b.dataset.pref.match(/P(\d{3,4})/);
      if(r){ var n = parseInt(r[1],10); var idx = E.findIndex(function(e){return e.n === n;}); shown = Math.max(50, idx + 1); }
      byId('q').value = ''; byId('fGrp').value = ''; byId('fPart').value = ''; byId('fStat').value = ''; byId('fSect').value = '';
      render();
    });
  });

  var pg = byId('partsGrid');
  D.parts.forEach(function(p, i){
    var b = document.createElement('button');
    b.className = 'part';
    b.innerHTML = '<b>' + esc(p.nom) + '</b><span>' + (p.n ? 'P' + String(p.de).padStart(3,'0') + ' – P' + String(p.a).padStart(3,'0') + ' · ' + p.n + ' entrées' : 'index · totaux · statuts · repères · garde-fous') + '</span>';
    b.addEventListener('click', function(){
      if(!p.n){ tab('regles'); return; }
      byId('fPart').value = p.nom; shown = 50; tab('registre'); render();
    });
    pg.appendChild(b);
  });

  var gal = byId('gal');
  D.images.forEach(function(src){
    var f = document.createElement('figure');
    f.innerHTML = '<img loading="lazy" src="' + esc(src) + '" alt=""><figcaption>Illustration. ' + esc(src.replace('images/','')) + '</figcaption>';
    gal.appendChild(f);
  });

  var al = byId('audList');
  D.audios.forEach(function(src){
    var li = document.createElement('li');
    li.className = 'aud';
    var base = src.replace('audio/','').replace('.mp3','');
    var dur = (D.durees && D.durees[base]) || null;
    var joli = base.replace(/^fiche_/,'').replace(/_/g,' ');
    var mm = dur ? ' · ' + Math.floor(dur/60) + ':' + ('0'+Math.round(dur%60)).slice(-2) : '';
    li.innerHTML = '<div class="audt">' + esc(joli) + esc(mm) + '</div><audio controls preload="none" src="' + esc(src) + '"></audio>';
    al.appendChild(li);
  });

  opt('fGrp', Object.keys(D.groupes).sort(function(a,b){ return D.groupes[b]-D.groupes[a]; }));
  opt('fStat', Object.keys(D.statuts).sort(function(a,b){ return D.statuts[b]-D.statuts[a] || (a<b?-1:1); }));
  opt('fPart', D.parts.map(function(p){ return p.nom; }));
  var ss = Object.keys(D.sections).filter(function(k){ return D.sections[k] >= 2; }).sort();
  opt('fSect', ss);

  byId('sTotal').textContent = D.total;
  byId('hTotal').textContent = D.total;
  byId('fTotal').textContent = D.total;
  byId('sParts').textContent = D.parts.length;
  byId('sImg').textContent = D.images.length;
  byId('sAud').textContent = D.audios.length;
  byId('sAud2').textContent = D.audios.length;
  render();
})();
</script>
<!--APP_JS_END-->
</body>
</html>
'''

HTML = (HTML.replace('__CSS__', CSS_FULL).replace('__DATA__', data_json)
            .replace('__PREUVES__', preuves_html)
            .replace('__LINKS__', links_html)
            .replace('__RULES__', rules_html).replace('__FICHES__', fiches_html))

out = os.path.join(ROOT, 'SITE_LOCAL.html')
open(out, 'w', encoding='utf-8').write(HTML)

print('entrées :', len(entries), '| P%03d-P%03d' % (min(nums), max(nums)))
print('parties :', len(parts), '| images :', len(images), '| audios :', len(audios))
print('statuts :', DATA['statuts'])
print('écrit :', out, '%.0f Ko' % (len(HTML) / 1024))
