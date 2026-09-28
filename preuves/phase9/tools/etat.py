#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 9 — Machine à états (fichier etat.json) et tableau de bord.

Usage :
  python3 etat.py init                    # construit la file d'attente depuis le registre
  python3 etat.py set GE1001 REDACTION    # change l'état d'une fiche (contrôle des transitions)
  python3 etat.py vague P9-1 GE1001 GE1002 ... --page FICHES9_GENESE_1.html --cat GE9
  python3 etat.py media GE1001 --img images/prophe_GE1001_eden.jpg --mp3 audio/fiche_GE1001_eden.mp3
  python3 etat.py stats                   # compteurs
  python3 etat.py md                      # régénère ../ETATS_PHASE9.md
  python3 etat.py next [n]                # prochaines fiches à planifier (ordre canonique)

États : A_PLANIFIER → RECHERCHE → REDACTION → CONTROLE → MEDIAS → PUBLIE
        (RENVOI : entrée qui répète une entrée P001-P519 déjà dotée d'une fiche phase 8 ;
         elle reçoit une fiche courte de renvoi, mêmes états.)
"""
import json
import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PH9 = os.path.dirname(HERE)
PREUVES = os.path.dirname(PH9)
ETAT = os.path.join(PH9, "etat.json")
MD = os.path.join(PH9, "ETATS_PHASE9.md")

ETATS = ["A_PLANIFIER", "RECHERCHE", "REDACTION", "CONTROLE", "MEDIAS", "PUBLIE"]

REG_FILES = ["16_REGISTRE_PROPHETIES.md", "17_REGISTRE_PROPHETIES_2.md",
             "18_REGISTRE_PROPHETIES_3.md", "19_REGISTRE_PROPHETIES_4.md",
             "20_REGISTRE_PROPHETIES_5.md", "21_REGISTRE_PROPHETIES_6.md",
             "23_REGISTRE_PROPHETIES_7.md", "24_REGISTRE_PROPHETIES_8.md"]

BOOKS = ["Genèse", "Exode", "Lévitique", "Nombres", "Deutéronome", "Josué", "Juges", "Ruth",
         "1 Samuel", "2 Samuel", "1 Rois", "2 Rois", "1 Chroniques", "2 Chroniques", "Esdras",
         "Néhémie", "Esther", "Job", "Psaume", "Proverbes", "Ecclésiaste", "Cantique", "Isaïe",
         "Jérémie", "Lamentations", "Ézéchiel", "Daniel", "Osée", "Joël", "Amos", "Abdias",
         "Jonas", "Michée", "Nahum", "Habacuc", "Sophonie", "Aggée", "Zacharie", "Malachie",
         "Matthieu", "Marc", "Luc", "Jean", "Actes", "Romains", "1 Corinthiens", "2 Corinthiens",
         "Galates", "Éphésiens", "Philippiens", "Colossiens", "1 Thessaloniciens",
         "2 Thessaloniciens", "1 Timothée", "2 Timothée", "Tite", "Philémon", "Hébreux",
         "Jacques", "1 Pierre", "2 Pierre", "1 Jean", "2 Jean", "3 Jean", "Jude", "Révélation"]
SERIE = {"Genèse": "GE", "Exode": "EX", "Lévitique": "LV", "Nombres": "NB", "Deutéronome": "DT",
         "Josué": "JS", "Juges": "JG", "Ruth": "RT", "1 Samuel": "SM", "2 Samuel": "SM",
         "1 Rois": "RO", "2 Rois": "RO", "1 Chroniques": "CH", "2 Chroniques": "CH", "Esdras": "ED",
         "Néhémie": "NE", "Esther": "ES", "Job": "JB", "Psaume": "PS", "Proverbes": "PR",
         "Ecclésiaste": "EC", "Cantique": "CT", "Isaïe": "IS", "Jérémie": "JR", "Lamentations": "LM",
         "Ézéchiel": "EZ", "Daniel": "DN", "Osée": "OS", "Joël": "JL", "Amos": "AM", "Abdias": "AB",
         "Jonas": "JO", "Michée": "MI", "Nahum": "NA", "Habacuc": "HA", "Sophonie": "SO",
         "Aggée": "AG", "Zacharie": "ZA", "Malachie": "ML", "Matthieu": "MT", "Marc": "MC",
         "Luc": "LC", "Jean": "JN", "Actes": "AC", "Romains": "RM", "1 Corinthiens": "CO",
         "2 Corinthiens": "CO", "Galates": "GA", "Éphésiens": "EP", "Philippiens": "PH",
         "Colossiens": "CL", "1 Thessaloniciens": "TH", "2 Thessaloniciens": "TH",
         "1 Timothée": "TM", "2 Timothée": "TM", "Tite": "TT", "Philémon": "PM", "Hébreux": "HE",
         "Jacques": "JC", "1 Pierre": "PI", "2 Pierre": "PI", "1 Jean": "JA", "2 Jean": "JA",
         "3 Jean": "JA", "Jude": "JU", "Révélation": "RV"}
BOOK_RE = re.compile(r"^((?:[123] )?[A-Za-zÀ-ÿ'’\. ]+?)\s+\d")
NORM = {"Psaumes": "Psaume", "Cantique des cantiques": "Cantique", "Ézékiel": "Ézéchiel",
        "Apocalypse": "Révélation", "Ecclesiaste": "Ecclésiaste"}


def first_book(ref):
    m = BOOK_RE.match(ref)
    b = m.group(1).strip() if m else "?"
    return NORM.get(b, b)


def lire_registre():
    rows = {}
    for fn in REG_FILES:
        p = os.path.join(PREUVES, fn)
        if not os.path.isfile(p):
            continue
        for line in open(p, encoding="utf-8"):
            if not line.startswith("| P"):
                continue
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) < 5 or not re.match(r"^P\d+$", c[0]):
                continue
            rows[int(c[0][1:])] = dict(ref=c[1], teneur=c[2], acc=c[3], statut=c[4], fichier=fn)
    return rows


def charger():
    return json.load(open(ETAT, encoding="utf-8")) if os.path.isfile(ETAT) else None


def sauver(d):
    d["maj"] = datetime.date.today().isoformat()
    json.dump(d, open(ETAT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def cmd_init():
    rows = lire_registre()
    dups = {}
    dp = os.path.join(HERE, "doublons_versets.json")
    if os.path.isfile(dp):
        dups = {int(k[1:]): [int(x[1:]) for x in v]
                for k, v in json.load(open(dp, encoding="utf-8")).items()}
    fiches = {}
    for n in sorted(rows):
        if n < 520:
            continue  # couvert par la phase 8 (FICHES8_*)
        r = rows[n]
        book = first_book(r["ref"])
        serie = SERIE.get(book, "XX")
        code = f"{serie}{n}"
        typ, cible = "complete", None
        d = dups.get(n, [])
        low = [x for x in d if x < 520]
        if low:
            typ, cible = "renvoi", sorted(low)
        elif d and min(d) < n:
            typ, cible = "commune", [min(d)]
        fiches[code] = dict(P=n, ref=r["ref"], teneur=r["teneur"], statut=r["statut"],
                            livre=book, serie=serie, type=typ, cible=cible,
                            etat="A_PLANIFIER", vague=None, page=None, cat=None,
                            img=None, mp3=None, historique=[])
    d = dict(phase=9, cree=datetime.date.today().isoformat(), fiches=fiches, vagues={})
    sauver(d)
    print(f"file d'attente : {len(fiches)} fiches (P520–P{max(rows)})")


def ordre(f):
    b = f["livre"]
    return (BOOKS.index(b) if b in BOOKS else 99, f["P"])


def cmd_set(code, etat, note=""):
    d = charger()
    f = d["fiches"][code]
    if etat not in ETATS:
        raise SystemExit(f"état inconnu : {etat}")
    i0, i1 = ETATS.index(f["etat"]), ETATS.index(etat)
    if i1 > i0 + 1:
        raise SystemExit(f"{code} : transition interdite {f['etat']} → {etat} (une étape à la fois)")
    f["historique"].append([datetime.date.today().isoformat(), f["etat"], etat, note])
    f["etat"] = etat
    sauver(d)
    print(code, "→", etat)


def cmd_vague(nom, codes, page, cat):
    d = charger()
    d["vagues"][nom] = dict(fiches=codes, page=page, cat=cat,
                            date=datetime.date.today().isoformat())
    for c in codes:
        f = d["fiches"][c]
        f["vague"], f["page"], f["cat"] = nom, page, cat
    sauver(d)
    print("vague", nom, ":", len(codes), "fiches →", page)


def cmd_media(code, img=None, mp3=None):
    d = charger()
    f = d["fiches"][code]
    if img:
        f["img"] = img
    if mp3:
        f["mp3"] = mp3
    sauver(d)


def stats(d):
    fs = d["fiches"].values()
    par_etat = {e: sum(1 for f in fs if f["etat"] == e) for e in ETATS}
    par_type = {t: sum(1 for f in fs if f["type"] == t) for t in ("complete", "commune", "renvoi")}
    imgs = sum(1 for f in fs if f["img"] and os.path.isfile(os.path.join(PREUVES, f["img"])))
    mp3s = sum(1 for f in fs if f["mp3"] and os.path.isfile(os.path.join(PREUVES, f["mp3"])))
    return par_etat, par_type, imgs, mp3s


def cmd_stats():
    d = charger()
    pe, pt, imgs, mp3s = stats(d)
    tot = len(d["fiches"])
    print(f"fiches phase 9 : {tot} · PUBLIE {pe['PUBLIE']} · reste {tot - pe['PUBLIE']}")
    print("par état :", pe)
    print("par type :", pt)
    print(f"médias présents : {imgs} JPG · {mp3s} MP3")


def cmd_next(n=10):
    d = charger()
    fs = sorted((f for f in d["fiches"].values() if f["etat"] == "A_PLANIFIER" and not f["vague"]),
                key=ordre)
    for f in fs[:n]:
        print(f"{next(k for k, v in d['fiches'].items() if v is f):8} P{f['P']:<5} {f['livre']:14} {f['ref']}")


def cmd_md():
    d = charger()
    pe, pt, imgs, mp3s = stats(d)
    tot = len(d["fiches"])
    L = []
    L.append("# PHASE 9 — Machine à états (fiches manquantes P520 → P1120)")
    L.append("")
    L.append(f"*Généré par `phase9/tools/etat.py md` le {datetime.date.today().isoformat()} à partir de `phase9/etat.json` (source de vérité de l'avancement).*")
    L.append("")
    L.append("## 1. Graphe des états (par fiche)")
    L.append("```")
    L.append("A_PLANIFIER → RECHERCHE → REDACTION → CONTROLE → MEDIAS → PUBLIE")
    L.append("     ↑____________|___________|__________| (retour d'une étape si un contrôle échoue)")
    L.append("```")
    L.append("- **A_PLANIFIER** : entrée du registre inscrite dans la file d'attente, code de fiche réservé (`<SÉRIE><P>`), type fixé (complète · commune · renvoi).")
    L.append("- **RECHERCHE** : sources officielles (wol.jw.org / jw.org) et web (forums, vidéos, réseaux) collectées ; identifiants de documents notés dans la data.")
    L.append("- **REDACTION** : `phase9/data/p9_<vague>.py` écrit (11 blocs + texte + accomplissement + chronologie + sources).")
    L.append("- **CONTROLE** : `build_p9.py` passe (C4 liens officiels seuls · C5 limites non vides · C6 aucun bloc vide · C7 ≥ 2 sources officielles) ; statut = statut du registre.")
    L.append("- **MEDIAS** : illustration JPG (`images/prophe_<CODE>_<slug>.jpg`) et piste MP3 française (`audio/fiche_<CODE>_<slug>.mp3`) générées, appariées par le résolveur et présentes sur la page.")
    L.append("- **PUBLIE** : page `FICHES9_*.html` construite avec ses médias, présentée, compteurs à jour.")
    L.append("")
    L.append("Transitions : une étape à la fois (`etat.py set` refuse les sauts). Tout retour en arrière est journalisé dans `historique`.")
    L.append("")
    L.append("## 2. Compteurs globaux")
    L.append("")
    L.append("| Indicateur | Valeur |")
    L.append("|---|---|")
    L.append(f"| Fiches de la file d'attente (P520–P{max(f['P'] for f in d['fiches'].values())}) | **{tot}** |")
    L.append(f"| Fiches PUBLIE | **{pe['PUBLIE']}** |")
    L.append(f"| Reste à produire | **{tot - pe['PUBLIE']}** |")
    L.append(f"| Par état | " + " · ".join(f"{k} {v}" for k, v in pe.items()) + " |")
    L.append(f"| Par type | complète {pt['complete']} · commune {pt['commune']} · renvoi {pt['renvoi']} |")
    L.append(f"| Médias phase 9 présents dans le dépôt de travail | {imgs} JPG · {mp3s} MP3 |")
    L.append(f"| Pages produites | {len(d['vagues'])} |")
    L.append("")
    L.append("## 3. Vagues")
    L.append("")
    for nom, v in d["vagues"].items():
        L.append(f"### {nom} — {v['cat']} · `{v['page']}` · {v['date']}")
        L.append("")
        L.append("| Fiche | P | Référence | Type | État | JPG | MP3 |")
        L.append("|---|---|---|---|---|---|---|")
        for c in v["fiches"]:
            f = d["fiches"][c]
            L.append(f"| {c} | P{f['P']} | {f['ref']} | {f['type']}"
                     f"{' → ' + ', '.join('P%d' % x for x in f['cible']) if f['cible'] else ''} | "
                     f"{f['etat']} | {'✓' if f['img'] else '—'} | {'✓' if f['mp3'] else '—'} |")
        L.append("")
    L.append("## 4. File d'attente par livre (ordre canonique)")
    L.append("")
    L.append("| Livre | Série | Fiches | Publiées | Numéros |")
    L.append("|---|---|---|---|---|")
    par_livre = {}
    for f in d["fiches"].values():
        par_livre.setdefault(f["livre"], []).append(f)
    for b in sorted(par_livre, key=lambda x: BOOKS.index(x) if x in BOOKS else 99):
        fs = sorted(par_livre[b], key=lambda f: f["P"])
        pub = sum(1 for f in fs if f["etat"] == "PUBLIE")
        nums = ", ".join(f"P{f['P']}" for f in fs) if len(fs) <= 12 else f"P{fs[0]['P']} … P{fs[-1]['P']} ({len(fs)})"
        L.append(f"| {b} | {SERIE.get(b, '??')} | {len(fs)} | {pub} | {nums} |")
    L.append("")
    L.append("## 5. Règle de priorité de la file")
    L.append("")
    L.append("1. Ordre canonique des livres, puis numéro P croissant à l'intérieur d'un livre ; les entrées de la partie 15 (P1001–P1120) sont insérées dans le livre auquel elles appartiennent.")
    L.append("2. Une vague = une page = 6 à 10 fiches d'un même livre (ou de livres voisins), ≤ 10 JPG et ≤ 10 MP3 par réponse.")
    L.append("3. Les entrées de type *renvoi* reçoivent une fiche courte (identification, texte, ce que la relecture messianique ajoute, lien vers la fiche phase 8) ; les entrées *communes* sont traitées sur la fiche de la plus petite entrée du groupe.")
    L.append("")
    open(MD, "w", encoding="utf-8").write("\n".join(L))
    print("écrit", MD)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(0)
    c = a[0]
    if c == "init":
        cmd_init()
    elif c == "set":
        cmd_set(a[1], a[2], " ".join(a[3:]))
    elif c == "vague":
        nom = a[1]
        codes = [x for x in a[2:] if not x.startswith("--") and x != a[a.index("--page") + 1] and x != a[a.index("--cat") + 1]]
        page = a[a.index("--page") + 1]
        cat = a[a.index("--cat") + 1]
        cmd_vague(nom, codes, page, cat)
    elif c == "media":
        img = a[a.index("--img") + 1] if "--img" in a else None
        mp3 = a[a.index("--mp3") + 1] if "--mp3" in a else None
        cmd_media(a[1], img, mp3)
    elif c == "stats":
        cmd_stats()
    elif c == "next":
        cmd_next(int(a[1]) if len(a) > 1 else 10)
    elif c == "md":
        cmd_md()
    else:
        print(__doc__)
