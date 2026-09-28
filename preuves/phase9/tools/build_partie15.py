#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 9 — Intégration des priorités A de l'audit dans le registre.

Lit   : propositions_audit.py (226 propositions de l'audit du 27/09/2026,
        numérotées P1001-P1226 dans AUDIT_COMPLETUDE_REGISTRE.md)
Écrit : ../../24_REGISTRE_PROPHETIES_8.md  (PARTIE 15 : entrées définitives,
        priorité A, entrées similaires fusionnées, numérotation P1001 → suite)
        ../../25_PROPOSITIONS_B_C_EN_ATTENTE.md (priorités B et C non intégrées)
        correspondance_audit_registre.tsv (n° audit → n° registre définitif)

Règle : la numérotation définitive est continue et suit l'ordre canonique.
Les numéros de l'audit (« n° audit ») ne sont plus employés que pour la
traçabilité.
Usage : python3 build_partie15.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import propositions_audit as pa  # noqa: E402

PREUVES = os.path.dirname(os.path.dirname(HERE))
OUT_REG = os.path.join(PREUVES, "24_REGISTRE_PROPHETIES_8.md")
OUT_ATT = os.path.join(PREUVES, "25_PROPOSITIONS_B_C_EN_ATTENTE.md")
OUT_TSV = os.path.join(HERE, "correspondance_audit_registre.tsv")

# ---------------------------------------------------------------------------
# FUSIONS : n° audit conservé → n° audit absorbés + texte fusionné.
# Une fusion réunit des propositions qui annoncent le même événement
# (parallèles, type et antitype, oracle et citation apostolique).
# ---------------------------------------------------------------------------
FUSIONS = {
    1013: dict(absorbe=[1015],
               ref="Exode 3:18-22 ; 7:3-5",
               teneur="Pharaon ne laissera pas partir le peuple ; Jéhovah multipliera ses signes et frappera l'Égypte « par de grands jugements » ; l'Égypte saura qu'il est Jéhovah ; Israël sortira les mains pleines (dépouillement des Égyptiens)",
               acc="Exode 5:2 ; 7:14–12:36 ; 12:35, 36 ; 14:4, 18",
               statut="Accomplie"),
    1014: dict(absorbe=[1018],
               ref="Exode 4:21-23 ; 11:4-8",
               teneur="Pharaon endurcira son cœur ; « je tuerai ton fils premier-né » ; « vers minuit » tout premier-né d'Égypte mourra, grand cri dans le pays, les serviteurs de Pharaon supplieront Israël de partir",
               acc="Exode 12:29-33",
               statut="Accomplie"),
    1016: dict(absorbe=[1017],
               ref="Exode 7:17 ; 8:2, 21-23 ; 9:3, 4, 18 ; 10:4 ; 11:7",
               teneur="Six plaies annoncées la veille : sang, grenouilles, taons, peste, grêle, sauterelles ; distinction annoncée entre l'Égypte et Israël : Goshèn épargné",
               acc="Exode 7:20 ; 8:6, 24 ; 9:6, 7, 23, 26 ; 10:13, 23 ; 12:13",
               statut="Accomplie"),
    1030: dict(absorbe=[1186],
               ref="Nombres 21:8, 9 ; Jean 3:14, 15 ; 8:28 ; 12:32-34",
               teneur="Le serpent de cuivre : « quiconque le regardera vivra » ; « comme Moïse a élevé le serpent dans le désert, il faut que le Fils de l'homme soit élevé » ; « quand vous aurez élevé le Fils de l'homme, alors vous saurez que c'est moi »",
               acc="Nombres 21:9 ; Jean 19:17, 18 ; Actes 2:36, 37",
               statut="Accomplie"),
    1119: dict(absorbe=[1213],
               ref="Isaïe 45:22-25 ; Philippiens 2:9-11",
               teneur="« Tournez-vous vers moi et soyez sauvés, vous toutes les extrémités de la terre » ; « devant moi tout genou pliera, toute langue jurera » ; nom au-dessus de tout nom : « qu'au nom de Jésus fléchisse tout genou… et que toute langue reconnaisse ouvertement que Jésus Christ est Seigneur »",
               acc="Romains 14:11 (P731) ; Révélation 5:13",
               statut="En cours / À venir"),
    1120: dict(absorbe=[1127],
               ref="Isaïe 48:20-22 ; 52:11, 12",
               teneur="« Sortez de Babylone ! Fuyez de Chaldée ! » ; ils n'ont pas eu soif dans les déserts ; « sortez de là, ne touchez rien d'impur » ; « vous ne sortirez pas dans la précipitation » : Jéhovah devant et derrière ; « pas de paix pour les méchants »",
               acc="537 av. n. è. ; 2 Corinthiens 6:17 ; Révélation 18:4",
               statut="Accomplie (1er accomplissement)"),
    1162: dict(absorbe=[1208],
               ref="Matthieu 19:28 ; Luc 22:28-30 ; 1 Corinthiens 6:2, 3",
               teneur="« Lors de la recréation… vous siégerez sur douze trônes pour juger les douze tribus d'Israël » ; « je fais avec vous une alliance pour un royaume » ; « les saints jugeront le monde » ; « nous jugerons des anges »",
               acc="Révélation 20:4-6 ; Jude 6",
               statut="En cours / À venir"),
    1198: dict(absorbe=[1218],
               ref="Actes 1:11 ; Hébreux 9:27, 28",
               teneur="« Ce Jésus… viendra de la même manière que vous l'avez vu s'en aller au ciel » ; « le Christ… apparaîtra une seconde fois, en dehors du péché, à ceux qui l'attendent ardemment pour leur salut »",
               acc="Depuis 1914 ; Matthieu 24:3, 30 ; Révélation 1:7",
               statut="En cours / À venir"),
    1200: dict(absorbe=[1216],
               ref="Actes 10:42 ; 17:31 ; 2 Timothée 4:1 ; 1 Pierre 4:5",
               teneur="« Il a fixé un jour où il va juger la terre habitée avec justice par un homme qu'il a désigné », garantie donnée : sa résurrection ; Christ Jésus « va juger les vivants et les morts », lors de sa manifestation et de son royaume",
               acc="À venir ; Jean 5:22-29 ; Révélation 20:11-13",
               statut="À venir"),
}

# Date de rédaction retenue par section (tableau des livres, nwt).
REDACTION = {
    "Genèse": "Moïse, 1513 av. n. è.",
    "Exode": "Moïse, 1512 av. n. è.",
    "Nombres": "Moïse, 1473 av. n. è.",
    "Deutéronome": "Moïse, 1473 av. n. è.",
    "Josué": "Josué, vers 1450 av. n. è.",
    "Juges": "Samuel, vers 1100 av. n. è.",
    "1 Samuel": "Samuel, Gad, Nathân, vers 1078 av. n. è.",
    "2 Samuel": "Gad, Nathân, vers 1040 av. n. è.",
    "1 Rois": "Jérémie, 580 av. n. è.",
    "2 Rois": "Jérémie, 580 av. n. è.",
    "2 Chroniques": "Esdras, vers 460 av. n. è.",
    "Psaumes": "David et d'autres, achevés vers 460 av. n. è.",
    "Isaïe": "Isaïe, après 732 av. n. è.",
    "Daniel": "Daniel, vers 536 av. n. è.",
    "Osée, Michée, Zacharie": "Osée, après 745 · Michée, avant 717 · Zacharie, 518 av. n. è.",
    "Évangiles": "Matthieu, vers 41 · Marc, vers 60-65 · Luc, vers 56-58 · Jean, vers 98 de n. è.",
    "Actes": "Luc, vers 61 de n. è.",
    "Épîtres": "Romains, vers 56 · 1 Corinthiens, vers 55 · Hébreux, vers 61 · 2 Pierre, vers 64 · 1 Jean, vers 98 de n. è.",
}

SECTION_TITRES = {
    "Genèse": "Genèse — Éden, Déluge, Sodome",
    "Exode": "Exode — la sortie d'Égypte annoncée",
    "Nombres": "Nombres — le désert",
    "Deutéronome": "Deutéronome — le lieu du nom, la conquête",
    "Josué": "Josué — le Jourdain, Jéricho",
    "Juges": "Juges — Débora, Gédéon, Yotham",
    "1 Samuel": "1 Samuel — Anne, le droit du roi, Saül",
    "2 Samuel": "2 Samuel — David",
    "1 Rois": "1 Rois — Salomon, Élie",
    "2 Rois": "2 Rois — Élisée, Jonas, Ézéchias",
    "2 Chroniques": "2 Chroniques — la lettre d'Élie",
    "Psaumes": "Psaumes — compléments messianiques et du Royaume",
    "Isaïe": "Isaïe — compléments (chapitres 1-66)",
    "Daniel": "Daniel — complément",
    "Osée, Michée, Zacharie": "Osée, Michée, Zacharie — compléments",
    "Évangiles": "Évangiles — Jésus et les annonces de sa naissance",
    "Actes": "Actes — les apôtres",
    "Épîtres": "Épîtres — Paul, Pierre, Jean",
}


def statut_norm(s):
    return s.replace(" ; ", " / ")


def integrer():
    """Retourne (entrees_definitives, en_attente, correspondance)."""
    absorbes = {}
    for keep, fu in FUSIONS.items():
        for a in fu["absorbe"]:
            absorbes[a] = keep
    finals, attente, corr = [], [], []
    num = 1000
    for i, x in enumerate(pa.P):
        na = 1001 + i  # numéro d'audit
        if na in absorbes:
            corr.append((na, f"fusionné → voir n° audit {absorbes[na]}", x["ref"]))
            continue
        if x["prio"] != "A":
            attente.append((na, x))
            corr.append((na, f"en attente ({x['prio']})", x["ref"]))
            continue
        num += 1
        row = dict(x)
        if na in FUSIONS:
            row.update({k: v for k, v in FUSIONS[na].items() if k != "absorbe"})
            row["fusion"] = FUSIONS[na]["absorbe"]
        row["statut"] = statut_norm(row["statut"])
        row["P"] = num
        row["audit"] = na
        finals.append(row)
        corr.append((na, f"P{num}", row["ref"]))
    return finals, attente, corr


def ecrire_registre(finals):
    L = []
    L.append("# REGISTRE GÉNÉRAL DES PROPHÉTIES BIBLIQUES ET DE LEURS ACCOMPLISSEMENTS — COMPLÉMENTS DE L'AUDIT")
    L.append(f"### Inventaire exhaustif — partie 15 : compléments issus de l'audit de complétude (priorité A) — P1001 à P{finals[-1]['P']}")
    L.append("*Même méthode que les parties 1 à 14 : référence, teneur, accomplissement, statut. Aucun commentaire. Les entrées similaires (parallèles, type et antitype, oracle et citation apostolique) ont été fusionnées en une seule ligne. Les propositions de priorité B et C restent hors registre (fichier 25) jusqu'à validation.*")
    L.append("")
    L.append("Règles du registre (rappel) :")
    L.append("1. Aucun commentaire : référence, teneur, accomplissement, statut.")
    L.append("2. Teneurs et accomplissements conformes à la compréhension des Témoins de Jéhovah (jw.org, wol.jw.org).")
    L.append("3. Statuts : Accomplie · Accomplie (1er accomplissement) · En cours · À venir (combinaisons séparées par « / »).")
    L.append("4. Un seul système chronologique (607 / 539 / 537 / 455 / 29 / 33 / 70 / 1914) ; aucune date pour l'avenir.")
    L.append("5. Aucun total de prophéties présenté comme une certitude (wol 2011607).")
    L.append("6. Numérotation continue : suite de P1000 (fichier 23). Les numéros sont définitifs et ne seront jamais réattribués.")
    L.append("7. Traçabilité : `phase9/tools/correspondance_audit_registre.tsv` donne, pour chaque numéro provisoire de l'audit (AUDIT_COMPLETUDE_REGISTRE.md), le numéro définitif ou le motif de non-intégration.")
    L.append("")
    L.append("---")
    L.append("---")
    L.append("")
    L.append("# PARTIE 15 — COMPLÉMENTS DE L'AUDIT DE COMPLÉTUDE (PRIORITÉ A)")
    L.append(f"**{len(finals)} entrées · ordre canonique · {sum(1 for f in finals if f.get('fusion'))} lignes issues d'une fusion**")
    L.append("")
    cur = None
    for f in finals:
        if f["sec"] != cur:
            cur = f["sec"]
            L.append(f"## {SECTION_TITRES.get(cur, cur)}")
            L.append(f"**Rédaction : {REDACTION.get(cur, '')}**")
            L.append("")
            L.append("| N° | Prophétie (référence) | Teneur | Accomplissement (référence) | Statut |")
            L.append("|---|---|---|---|---|")
        L.append(f"| P{f['P']} | {f['ref']} | {f['teneur']} | {f['acc']} | {f['statut']} |")
        # ligne vide après chaque section : gérée au changement de section
        nxt = finals[finals.index(f) + 1]["sec"] if finals.index(f) + 1 < len(finals) else None
        if nxt != cur:
            L.append("")
    L.append("---")
    L.append("")
    L.append("## Récapitulatif de la partie 15")
    L.append("")
    L.append("| Section | Entrées | Numéros |")
    L.append("|---|---|---|")
    secs = []
    for f in finals:
        if not secs or secs[-1][0] != f["sec"]:
            secs.append([f["sec"], 0, f["P"], f["P"]])
        secs[-1][1] += 1
        secs[-1][3] = f["P"]
    for s, n, a, b in secs:
        L.append(f"| {s} | {n} | P{a}–P{b} |" if a != b else f"| {s} | {n} | P{a} |")
    L.append(f"| **Total** | **{len(finals)}** | **P1001–P{finals[-1]['P']}** |")
    L.append("")
    L.append("Fusions opérées (n° audit conservé ← n° audit absorbés) : " + " · ".join(
        f"{k} ← {', '.join(str(a) for a in v['absorbe'])}" for k, v in FUSIONS.items()) + ".")
    L.append("")
    open(OUT_REG, "w", encoding="utf-8").write("\n".join(L))


def ecrire_attente(attente):
    L = []
    L.append("# PROPOSITIONS D'AJOUT AU REGISTRE — PRIORITÉS B ET C EN ATTENTE DE VALIDATION")
    L.append("### Issues de l'audit de complétude du 27 septembre 2026 — non intégrées au registre")
    L.append("*Ces lignes ne font pas partie du registre. Le « n° audit » renvoie à AUDIT_COMPLETUDE_REGISTRE.md ; un numéro définitif (suite de la partie 15) ne sera attribué qu'à l'intégration. B = prophétie réelle mais mineure ou complément d'une entrée existante ; C = cas limite (typologie, assertion, promesse conditionnelle) à trancher.*")
    L.append("")
    cur = None
    for na, x in attente:
        if x["sec"] != cur:
            if cur is not None:
                L.append("")
            cur = x["sec"]
            L.append(f"## {cur}")
            L.append("")
            L.append("| N° audit | Priorité | Prophétie (référence) | Teneur | Accomplissement (référence) | Statut proposé | Justification / source |")
            L.append("|---|---|---|---|---|---|---|")
        L.append(f"| {na} | {x['prio']} | {x['ref']} | {x['teneur']} | {x['acc']} | {statut_norm(x['statut'])} | {x['src']} |")
    L.append("")
    nb = len(attente)
    nB = sum(1 for _, x in attente if x["prio"] == "B")
    nC = nb - nB
    L.append(f"**Total en attente : {nb} propositions ({nB} B · {nC} C).** Les propositions B absorbées par une fusion (Exode 7:3-5 ; 8:22, 23 ; 9:4 ; 11:7) figurent déjà dans la partie 15.")
    L.append("")
    open(OUT_ATT, "w", encoding="utf-8").write("\n".join(L))


def ecrire_corr(corr):
    with open(OUT_TSV, "w", encoding="utf-8") as fh:
        fh.write("n_audit\tresultat\treference\n")
        for na, r, ref in corr:
            fh.write(f"{na}\t{r}\t{ref}\n")


if __name__ == "__main__":
    finals, attente, corr = integrer()
    ecrire_registre(finals)
    ecrire_attente(attente)
    ecrire_corr(corr)
    print(f"partie 15 : {len(finals)} entrées (P1001–P{finals[-1]['P']}), "
          f"{len(FUSIONS)} fusions ; en attente : {len(attente)} ; écrit :")
    print(" ", OUT_REG)
    print(" ", OUT_ATT)
    print(" ", OUT_TSV)
