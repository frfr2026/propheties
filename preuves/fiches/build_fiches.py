#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE 7 — Generateur des fiches descriptives de propheties (v2, 2026-09-25).

Lit    : fiches/data/cat_<x>.py   (donnees source de verite)
Ecrit  : FICHES_<CODE>_<NOM>.html (autonome : CSS inline, medias locaux)

Nouveautes v2 : illustration embarquee par fiche, lecteur audio par fiche,
page de garde avec couverture, sommaire en cartes, navigation fixe,
feuille de style partagee (theme.py), mise en page ecran + impression A4.

Grille de validation C1-C12 appliquee avant ecriture :
C5 bloc 'limites' vide -> echec
C6 un des dix blocs vide -> echec
C7 moins de 2 sources wol/jw.org -> echec
C4 lien externe hors jw.org / wol.jw.org -> echec
"""

import os
import sys
import datetime
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "fiches")
sys.path.insert(0, HERE)

from theme import (THEME_CSS, LEGENDE_IMG, OFFICIAL, e, build_audio_index,
                   audio_pour_fiche, intros_pour_module, couverture_pour_module,
                   load_durations, duree_txt, lettres_fiche)

BLOCS = [
    ("contexte", "3 · Contexte"),
    ("explication", "4 · Explication du texte"),
    ("interpretation", "5 · Interprétation"),
    ("hist", "7 · Preuves historiques"),
    ("geo", "8 · Preuves géographiques"),
    ("sci", "9 · Preuves scientifiques et archéologiques"),
    ("limites", "10 · Ce que cette fiche ne dit pas"),
]


def svg_tl(steps, w=780, h=112):
    """Chronologie SVG inline : ligne, pastilles, etiquettes alternees."""
    n = len(steps)
    if n < 2:
        return ""
    pad = 60
    step = (w - 2 * pad) / (n - 1)
    y = 56
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Chronologie">']
    out.append(f'<line x1="{pad-24}" y1="{y}" x2="{w-pad+24}" y2="{y}" '
               f'stroke="#1a4a8a" stroke-width="3" stroke-linecap="round"/>')
    for i, (date, ev) in enumerate(steps):
        x = pad + i * step
        ext = (i in (0, n - 1))
        col = "#E9C46A" if ext else "#1a4a8a"
        r = 8 if ext else 6
        out.append(f'<circle cx="{x:.1f}" cy="{y}" r="{r}" fill="{col}" '
                   f'stroke="#0B2545" stroke-width="1.6"/>')
        up = (i % 2 == 0)
        ty = y - 18 if up else y + 30
        out.append(f'<text x="{x:.1f}" y="{ty}" text-anchor="middle" '
                   f'font-size="12.5" font-weight="700" fill="#0B2545">'
                   f'{e(ev)}</text>')
        out.append(f'<text x="{x:.1f}" y="{ty+14}" text-anchor="middle" '
                   f'font-size="10.5" fill="#5b6472">{e(date)}</text>')
    out.append("</svg>")
    return "\n".join(out)


def validate(fiches, cat):
    """Grille C4-C7. Leve une exception au premier echec."""
    errs = []
    for f in fiches:
        n = f["n"]
        for key, label in BLOCS:
            if not str(f.get(key, "")).strip():
                errs.append(f"{n} : bloc vide → {label}")
        if not f.get("texte"):
            errs.append(f"{n} : aucun verset cité")
        if not f.get("accomplissement"):
            errs.append(f"{n} : aucune étape d'accomplissement")
        if not f.get("tl"):
            errs.append(f"{n} : chronologie vide")
        off = 0
        for _, u in f.get("src", []):
            host = re.sub(r"^https?://", "", u).split("/")[0]
            if host in OFFICIAL:
                off += 1
            else:
                errs.append(f"{n} : lien non officiel → {u}")
        if off < 2:
            errs.append(f"{n} : seulement {off} source(s) officielle(s) (minimum 2)")
    if errs:
        raise SystemExit("VALIDATION ÉCHOUÉE\n" + "\n".join("  · " + x for x in errs))
    return True


def player_html(titre, mp3, durees):
    """Lecteur audio + repli imprimable."""
    if not mp3:
        return ""
    d = durees.get(mp3[:-4]) if mp3.endswith(".mp3") else None
    dt = f" · {duree_txt(d)}" if d else ""
    return (f'<div class="player fiche"><div class="t">🎧 {e(titre)}{dt}</div>'
            f'<audio controls preload="none" src="audio/{mp3}"></audio>'
            f'<div class="print-audio">🔊 Piste audio : audio/{e(mp3)}{dt} '
            f'(ouvrir le fichier dans le dossier pour l\u2019écouter).</div></div>')


def build(cat, fiches, fichier):
    validate(fiches, cat)
    idx, intros = build_audio_index()
    durees = load_durations()
    couv = couverture_pour_module(cat.get("code", ""), fiches)
    intro_mp3 = intros_pour_module(fiches, intros)

    mod_lettres = set(re.findall(r"[A-Z]", cat.get("code", "")))
    for f in fiches:
        mod_lettres |= lettres_fiche(f.get("n"))
    aud_map = {}
    sans_audio, sans_image, flous = [], [], []
    for f in fiches:
        mp3, flou = audio_pour_fiche(f, idx, mod_lettres)
        aud_map[f["n"]] = mp3
        if flou:
            flous.append(f"{f['n']}→{mp3}")
        if not mp3:
            sans_audio.append(f["n"])
        img = f.get("img", "")
        if not img or not os.path.isfile(os.path.join(ROOT, img)):
            sans_image.append(f["n"])

    H = []
    H.append(f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FICHES {e(cat['code'])} — {e(cat['nom'])}</title>
<style>{THEME_CSS}</style></head><body>
<div class="prog" id="prog"></div>
<a class="haut" href="#haut">↑ Haut</a>

<header class="hero" id="haut">
<img class="fond" src="{e(couv)}" alt="">
<div class="voile"></div>
<div class="contenu">
<div class="kicker">Bibliothèque privée · projet PREUVES · phase 7</div>
<h1>FICHES {e(cat['code'])}</h1>
<h2>{e(cat['nom'])}</h2>
<p class="intro">{e(cat['intro'])}</p>
<div class="chiffres">
<div><b>{len(fiches)}</b><span>fiches</span></div>
<div><b>10</b><span>blocs par fiche</span></div>
<div><b>{sum(len(f['src']) for f in fiches)}</b><span>sources</span></div>
<div><b>{len(fiches) - len(sans_audio)}</b><span>pistes audio</span></div>
<div><b>0</b><span>date pour l'avenir</span></div>
</div>""")
    for mp3 in intro_mp3:
        d = durees.get(mp3[:-4])
        dt = f" · {duree_txt(d)}" if d else ""
        H.append(f'<div class="player"><div class="t">🎧 Introduction audio{dt}</div>'
                 f'<audio controls preload="none" src="audio/{mp3}"></audio>'
                 f'<div class="print-audio">🔊 Piste : audio/{e(mp3)}.</div></div>')
    H.append("""</div></header>

<nav class="nav" aria-label="Fiches"><div class="bar">
<a class="accueil" href="#haut">⌂ Sommaire</a>
<a href="SITE_LOCAL.html">REPÈRES · accueil</a>""")
    for f in fiches:
        H.append(f'<a href="#{f["n"]}">{f["n"]}</a>')
    H.append('<a href="#chronos">Chronologies</a><a href="#rappels">Rappels</a>')
    H.append("</div></nav>\n\n<div class=\"wrap\">")

    # ---- SOMMAIRE EN CARTES
    H.append("""<h1 class="t">Les fiches de cette catégorie</h1>
<div class="st">Chaque carte ouvre la fiche complète : illustration, texte,
preuves, chronologie, sources et piste audio.</div>
<div class="grille">""")
    for f in fiches:
        mp3 = aud_map.get(f["n"])
        d = durees.get(mp3[:-4]) if mp3 else None
        meta = f'{e(f["statut"])}' + (f" · 🎧 {duree_txt(d)}" if d else "")
        H.append(f"""<div class="carte">
<a class="img" href="#{f["n"]}"><img src="{e(f['img'])}" alt="" loading="lazy"></a>
<div class="txt"><div class="num">FICHE {f["n"]}</div>
<h3><a href="#{f["n"]}">{e(f["titre"])}</a></h3>
<div class="meta">{meta}</div></div></div>""")
    H.append("</div>")

    # ---- MODE D'EMPLOI
    H.append("""<h1 class="t">Mode d'emploi de la catégorie</h1>
<div class="st">Dix blocs par fiche, toujours dans le même ordre. Le dixième
n'est jamais vide.</div>
<div class="cadre"><b>Comment lire une fiche.</b> On commence par le contexte :
sans lui, l'explication n'a pas de sol. On passe ensuite à l'exégèse — le
vocabulaire, le genre littéraire, la structure — avant toute interprétation.
L'interprétation donnée est <b>celle des Témoins de Jéhovah, avec sa source</b> ;
elle n'est jamais présentée comme la seule lecture possible. Viennent alors les
preuves, classées en trois registres distincts : historique (les documents),
géographique (le site), scientifique (la fouille, la datation, la mesure). On
termine toujours par les limites.</div>
<div class="grille2">
<div class="cadre"><b>Les trois registres de preuve.</b><br>
<b>Historique</b> — une tablette, une chronique, un auteur profane.<br>
<b>Géographique</b> — le relief, l'eau, la route : ce qui rendait le lieu
habitable, et ce qui l'a vidé.<br>
<b>Scientifique</b> — l'archéologie, l'épigraphie, la datation, parfois la
géologie ou l'hydrologie.</div>
<div class="cadre"><b>Les trois règles de la phase.</b><br>
1. <b>Un seul système chronologique par fiche.</b> Quand la chronologie profane
diffère, l'écart est signalé, jamais escamoté.<br>
2. <b>Aucune date pour l'avenir.</b><br>
3. <b>Aucun total dogmatique.</b> Une fiche vaut par sa précision, pas par son
nombre.</div>
</div>
<div class="attn"><b>Avertissement général.</b> Plusieurs de ces oracles annoncent
qu'un lieu « ne sera plus habité ». Certains de ces lieux sont aujourd'hui des
villes peuplées — Saïda, Amman, Gaza, Mossoul. Ces fiches le disent et le
situent : l'oracle vise un peuple, une cité antique ou un système politique, non
l'usage immémorial d'un site. Un dossier qui cacherait ces écarts perdrait le
seul avantage qu'il a : la vérifiabilité.</div>""")

    # ---- FICHES
    for f in fiches:
        mp3 = aud_map.get(f["n"])
        H.append(f'<article class="fiche" id="{f["n"]}">')
        H.append(f'<div class="visuel"><img src="{e(f["img"])}" alt="" '
                 f'loading="lazy"><div class="legende">{e(LEGENDE_IMG)}</div></div>')
        H.append('<div class="hd">')
        H.append(f'<div class="num">FICHE {f["n"]} · CATÉGORIE {e(cat["code"])}</div>')
        H.append(f'<h3>{e(f["titre"])}</h3>')
        H.append(f'<div class="ref">{e(f["ref"])}</div></div><div class="bd">')

        H.append('<div class="badges">')
        H.append(f'<span class="badge or">{e(f["statut"])}</span>')
        H.append(f'<span class="badge">{e(f["syst"])}</span>')
        H.append(f'<span class="badge">{len(f["src"])} sources</span>')
        if mp3:
            H.append('<span class="badge">🎧 version audio</span>')
        H.append("</div>")
        H.append(player_html(f"Écouter la fiche {f['n']}", mp3, durees))

        H.append("<h4>1 · Identification</h4>")
        H.append("<table><tbody>")
        H.append(f'<tr><td class="d">Référence</td><td>{e(f["ref"])}</td></tr>')
        H.append(f'<tr><td class="d">Statut</td><td>{e(f["statut"])}</td></tr>')
        H.append(f'<tr><td class="d">Chronologie</td><td>{e(f["syst"])}</td></tr>')
        H.append(f'<tr><td class="d">Registre</td><td>{e(f["reg"])}</td></tr>')
        H.append("</tbody></table>")

        H.append('<h4>2 · Le texte</h4><div class="txt"><ul>')
        for t in f["texte"]:
            H.append(f"<li>{e(t)}</li>")
        H.append("</ul></div>")

        for key, label in BLOCS:
            H.append(f"<h4>{label}</h4>")
            H.append(f"<p>{e(f[key])}</p>")
            if key == "interpretation":
                H.append("<h4>6 · L’accomplissement</h4>")
                H.append("<table><thead><tr><th>Quand</th>"
                         "<th>Événement</th></tr></thead><tbody>")
                for d_, ev in f["accomplissement"]:
                    H.append(f'<tr><td class="d">{e(d_)}</td><td>{e(ev)}</td></tr>')
                H.append("</tbody></table>")

        H.append("<h4>Chronologie</h4>")
        H.append(svg_tl(f["tl"]))
        H.append('<h4>Sources</h4><div class="src">')
        for t, u in f["src"]:
            H.append(f'<a href="{u}">{e(t)}<br>{e(u)}</a>')
        H.append("</div>")
        H.append("</div>")
        H.append(f'<div class="bd" style="padding-top:0"><div class="pied">'
                 f'<span>Fiche {f["n"]} — {e(f["titre"])}</span>'
                 f'<span>Catégorie {e(cat["code"])}</span></div></div>')
        H.append("</article>")

    # ---- CHRONOLOGIES DE CATEGORIE
    H.append(f"""<h1 class="t" id="chronos" style="scroll-margin-top:64px">
Chronologie de la catégorie {e(cat['code'])}</h1>
<div class="st">Toutes les fiches sur une seule ligne. Chaque ville a son propre
axe : les comparer revient à les confondre.</div>""")
    for f in fiches:
        H.append(f'<h4>{f["n"]} — {e(f["titre"])}</h4>')
        H.append(svg_tl(f["tl"]))
    H.append("""<div class="attn"><b>Remarque de méthode.</b> Ces chronologies ne
sont pas sur la même échelle et ne doivent pas être additionnées. Chaque fiche a
son propre axe : la comparaison n'a de sens qu'à l'intérieur d'une même
fiche.</div>""")

    # ---- RAPPELS
    H.append(f"""<h1 class="t" id="rappels" style="scroll-margin-top:64px">
Rappels et transmission</h1>
<div class="st">Ce qui vaut pour toute la phase 7.</div>
<table><thead><tr><th style="width:23%">Règle</th><th>Application</th></tr></thead>
<tbody>
<tr><td><b>Un seul système</b></td><td>607 · 539 · 537 · 455 · 29 · 33 · 36 ·
1914. Les dates neutres (701, 604, 539, 332, 105) sont signalées comme telles.
Un seul système par fiche.</td></tr>
<tr><td><b>Aucune date</b></td><td>Ce qui n'est pas accompli reste sans date.</td></tr>
<tr><td><b>Aucun total</b></td><td>La Bibliothèque en ligne écrit qu'il est
préférable de ne pas se montrer trop affirmatif quant au nombre exact des
prophéties messianiques.</td></tr>
<tr><td><b>Un à un</b></td><td>De personne à personne. Jamais de diffusion
publique, jamais d'envoi groupé.</td></tr>
<tr><td><b>Liens officiels</b></td><td>www.jw.org et wol.jw.org uniquement. Aucun
extrait de publication n'est recopié, hébergé ni republié.</td></tr>
<tr><td><b>Aucune collecte</b></td><td>Aucune donnée personnelle n'est demandée
ni stockée.</td></tr>
</tbody></table>
</div>
<footer class="site"><div class="in">
Généré le {datetime.date.today().isoformat()} · phase 7, vague
{cat.get("vague", "1")} · projet PREUVES. Sources : Bibliothèque en ligne
Watchtower (wol.jw.org) et www.jw.org. Aucun contenu protégé n'est reproduit :
les références bibliques sont citées par phrases courtes.<br>
Usage strictement privé. Liens exclusivement vers www.jw.org et wol.jw.org.
Aucune date pour l'avenir.
</div></footer>
""" + """<script>
(function(){var p=document.getElementById('prog');
addEventListener('scroll',function(){var h=document.documentElement;
var x=h.scrollTop/(h.scrollHeight-h.clientHeight)*100;p.style.width=x+'%';},
{passive:true});})();
</script>
</body></html>""")

    out = os.path.join(ROOT, fichier)
    open(out, "w", encoding="utf-8").write("\n".join(H))
    return out, sans_audio, sans_image, flous


if __name__ == "__main__":
    import importlib
    mod = sys.argv[1] if len(sys.argv) > 1 else "cat_a"
    out = sys.argv[2] if len(sys.argv) > 2 else "FICHES_A_NATIONS.html"
    m = importlib.import_module("data." + mod)
    p, sa, si, fl = build(m.CAT, m.FICHES, out)
    print("validation OK — 10 blocs, sources officielles, liens conformes")
    print("catégorie :", m.CAT["code"], "—", m.CAT["nom"])
    print("fiches :", len(m.FICHES))
    print("sources :", sum(len(f["src"]) for f in m.FICHES))
    print("écrit :", p, os.path.getsize(p) // 1024, "Ko")
    if sa:
        print("SANS AUDIO :", ", ".join(sa))
    if si:
        print("SANS IMAGE :", ", ".join(si))
    if fl:
        print("FLOU :", " · ".join(fl))
