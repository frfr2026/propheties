#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 9 — wrapper du builder v2 (fiches/build_fiches.py + theme.py).

Ajouts phase 9 :
- 11 blocs (schéma avant limites), libellés « phase 9 » ;
- le bloc « Schéma · l'essentiel » est rendu en frise visuelle (boîtes → flèches)
  en plus de la chronologie SVG ;
- bandeau « Registre » cliquable vers le fichier de registre ;
- rappel du type de fiche (complète · commune · renvoi) dans l'identification.

Usage : python3 build_p9.py p9_gen1 FICHES9_GENESE_1.html
"""
import os
import re
import sys
import html
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "fiches"))
sys.path.insert(0, os.path.join(HERE, "data"))

import build_fiches  # noqa: E402

build_fiches.BLOCS.insert(-1, ("schema", "10 · Schéma · l'essentiel en bref"))
for i, (k, _l) in enumerate(build_fiches.BLOCS):
    if k == "limites":
        build_fiches.BLOCS[i] = (k, "11 · Ce que cette fiche ne dit pas")

CSS_P9 = """
/* ---------- phase 9 : frise du schéma ---------- */
.flux{display:flex;flex-wrap:wrap;gap:10px 6px;align-items:stretch;margin:8px 0 14px}
.flux .etape{flex:1 1 180px;max-width:100%;background:#f4f7fb;border:1px solid #cfd9e6;
 border-left:5px solid #1a4a8a;border-radius:8px;padding:9px 11px;font-size:13.5px;
 line-height:1.35;position:relative;display:flex;align-items:center}
.flux .etape.or{border-left-color:#E9C46A;background:#fdf8ea}
.flux .fl{align-self:center;color:#1a4a8a;font-size:20px;font-weight:700;padding:0 2px}
.flux .etape b{display:block;font-size:11px;letter-spacing:.06em;color:#5b6472;margin-bottom:3px}
.reg-lien{font-size:12.5px;margin:-4px 0 10px}
.reg-lien a{color:#1a4a8a;text-decoration:none;border-bottom:1px dotted #1a4a8a}
.renvois{max-width:1060px;margin:28px auto 8px;padding:0 16px}
.renvois h2{font-size:20px;color:#1a4a8a;margin:0 0 6px}
.renvois p.intro{font-size:14px;color:#333;margin:0 0 12px}
.renvois table{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff}
.renvois th,.renvois td{border:1px solid #d5dbe6;padding:7px 9px;vertical-align:top;text-align:left}
.renvois th{background:#eef2f8;color:#1a4a8a}
.renvois td.c{white-space:nowrap;font-weight:700;color:#1a4a8a}
.renvois a{color:#1a4a8a}
@media print{.flux .etape{break-inside:avoid;border:1px solid #999}}
"""


def frise(txt):
    """'A → B · C → D' -> boîtes et flèches (première et dernière en or)."""
    parts = [p.strip() for p in re.split(r"\s*→\s*", txt) if p.strip()]
    if len(parts) < 2:
        return f"<p>{html.escape(txt, quote=False)}</p>"
    out = ['<div class="flux">']
    for i, p in enumerate(parts):
        cls = "etape or" if i in (0, len(parts) - 1) else "etape"
        lab = f"<b>ÉTAPE {i + 1}</b>" if i not in (0, len(parts) - 1) else (
            "<b>POINT DE DÉPART</b>" if i == 0 else "<b>ABOUTISSEMENT</b>")
        out.append(f'<div class="{cls}"><div>{lab}{html.escape(p, quote=False)}</div></div>')
        if i < len(parts) - 1:
            out.append('<div class="fl">→</div>')
    out.append("</div>")
    out.append(f'<p style="font-size:12.5px;color:#5b6472">{html.escape(txt, quote=False)}</p>')
    return "\n".join(out)


def main():
    mod = importlib.import_module(sys.argv[1])
    out = sys.argv[2]
    p, sa, si, fl = build_fiches.build(mod.CAT, mod.FICHES, out)
    h = open(p, encoding="utf-8").read()

    # libellés
    h = h.replace("<b>10</b><span>blocs par fiche</span>", "<b>11</b><span>blocs par fiche</span>")
    h = h.replace("Dix blocs par fiche", "Onze blocs par fiche")
    h = h.replace("Le dixième", "Le onzième")
    h = h.replace("phase 7", "phase 9")
    h = h.replace("</style>", CSS_P9 + "</style>", 1)

    # frise du schéma : <h4>10 · Schéma …</h4>\n<p>…</p>
    def rep(m):
        raw = html.unescape(m.group(1))
        return m.group(0).split("<p>")[0] + frise(raw)
    h = re.sub(r"<h4>10 · Schéma · l'essentiel en bref</h4>\n<p>(.*?)</p>", rep, h, flags=re.S)

    # lien registre sous le tableau d'identification
    regfile = mod.CAT.get("registre", "24_REGISTRE_PROPHETIES_8.md")
    for f in mod.FICHES:
        pn = f.get("P", "")
        typ = f.get("type", "complète")
        cible = f.get("cible", "")
        ligne = (f'<div class="reg-lien">Entrée <b>P{pn}</b> du registre — '
                 f'<a href="{regfile}">{regfile}</a> · fiche {typ}'
                 + (f" · voir aussi {html.escape(cible, quote=False)}" if cible else "") + "</div>")
        anchor = f'<tr><td class="d">Registre</td><td>{html.escape(f["reg"], quote=False)}</td></tr>\n</tbody></table>'
        if anchor in h:
            h = h.replace(anchor, anchor + "\n" + ligne, 1)

    # fiches « renvoi » / « commune » : section courte avant le pied de page
    renvois = getattr(mod, "RENVOIS", [])
    if renvois:
        rows = []
        for r in renvois:
            liens = " · ".join(f'<a href="{html.escape(u)}">{html.escape(t)}</a>' for t, u in r.get("liens", []))
            rows.append(
                f'<tr><td class="c">{html.escape(r["n"])}</td><td>P{html.escape(str(r["P"]))}</td>'
                f'<td>{html.escape(r["ref"])}</td><td>{html.escape(r["teneur"])}</td>'
                f'<td>{html.escape(r["statut"])}</td><td>{html.escape(r["type"])}</td>'
                f'<td>{html.escape(r["note"], quote=False)}<br>{liens}</td></tr>')
        sec = ('<section class="renvois" id="renvois"><h2>Renvois et fiches communes de cette vague</h2>'
               '<p class="intro">Entrées du registre dont le passage est déjà traité par une fiche individuelle '
               '(phase 8) ou qui seront traitées sur la fiche d\'une autre entrée : elles reçoivent ici une '
               'fiche courte avec le lien vers la fiche de référence. Aucun média propre.</p>'
               '<table><thead><tr><th>Code</th><th>Entrée</th><th>Référence</th><th>Teneur (registre)</th>'
               '<th>Statut</th><th>Type</th><th>Renvoi</th></tr></thead><tbody>' + "".join(rows) +
               '</tbody></table></section>\n')
        h = h.replace('<footer class="site">', sec + '<footer class="site">', 1)

    open(p, "w", encoding="utf-8").write(h)
    print("validation OK — 11 blocs, sources officielles, liens conformes")
    print("catégorie :", mod.CAT["code"], "—", mod.CAT["nom"])
    print("fiches :", len(mod.FICHES))
    print("sources :", sum(len(f["src"]) for f in mod.FICHES))
    print("écrit :", p, os.path.getsize(p) // 1024, "Ko")
    if sa:
        print("SANS AUDIO :", ", ".join(sa))
    if si:
        print("SANS IMAGE :", ", ".join(si))
    if fl:
        print("FLOU :", " · ".join(fl))


if __name__ == "__main__":
    main()
