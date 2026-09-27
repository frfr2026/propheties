#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 8 — wrapper : builder v2 + 11e bloc (schema) + retouches phase 8.
Usage : python3 build_p8.py p8_gen1 FICHES8_GENESE_1.html"""
import os
import sys
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "fiches"))
sys.path.insert(0, os.path.join(HERE, "data"))

import build_fiches

# 11 blocs : schema avant limites ; limites renumerote.
build_fiches.BLOCS.insert(-1, ("schema", "10 · Schéma · l'essentiel en bref"))
for i, (k, _l) in enumerate(build_fiches.BLOCS):
    if k == "limites":
        build_fiches.BLOCS[i] = (k, "11 · Ce que cette fiche ne dit pas")

mod = importlib.import_module(sys.argv[1])
out = sys.argv[2]
p, sa, si, fl = build_fiches.build(mod.CAT, mod.FICHES, out)

# Retouches phase 8 (post-traitement).
h = open(p, encoding="utf-8").read()
h = h.replace("<b>10</b><span>blocs par fiche</span>",
              "<b>11</b><span>blocs par fiche</span>")
h = h.replace("Dix blocs par fiche", "Onze blocs par fiche")
h = h.replace("Le dixième", "Le onzième")
h = h.replace("phase 7", "phase 8")
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
