#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design system partage PROJET PREUVES (v2, 2026-09-25).

- THEME_CSS : feuille de style moderne commune a toutes les pages generees.
  Fichiers de sortie toujours autonomes (CSS inline) : partage fichier par fichier.
- Helpers medias : appariement fiche -> illustration + audio, durees, couvertures.

Sources de la demarche (recherche du 2026-09-25) :
- identite jw.org : bleu apaisant + blanc, sans-serif geometrique, cartes
  image + titre + description (page d'accueil jw.org ; logos-world, 1000logos) ;
- cartes CSS : grille auto-fill minmax(), radius, ombres douces, survol lift,
  clamp() (sliderrevolution, uicookies, tutorialspoint) ;
- ergonomie : lecture en F (essentiel en haut a gauche), hierarchie, espaces,
  sans-serif, texte aligne a gauche, pas de capitales courantes ni de
  justifie (choblab, webprospection, CNRS-LIRIS).
"""

import os
import re
import json
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # preuves/
AUD_DIR = os.path.join(ROOT, "audio")
IMG_DIR = os.path.join(ROOT, "images")
DUR_PATH = os.path.join(ROOT, "collections", "durations.json")

OFFICIAL = ("wol.jw.org", "www.jw.org", "jw.org", "tv.jw.org")

# ---------------------------------------------------------------------------
# FEUILLE DE STYLE
# ---------------------------------------------------------------------------
THEME_CSS = """
:root{
 --jw-bleu:#1a4a8a; --jw-bleu-fonce:#0B2545; --jw-bleu-clair:#e8eef7;
 --jw-or:#E9C46A; --jw-or-fonce:#7a5b12;
 --fond:#eef1f6; --carte:#ffffff; --creme:#faf8f2; --encre:#1b2430;
 --gris:#5b6472; --bord:#d8dee9; --ok:#2e7d32; --radius:14px;
 --ombre:0 2px 10px rgba(11,37,69,.10),0 10px 28px rgba(11,37,69,.08);
 --ombre-legere:0 1px 4px rgba(11,37,69,.10);
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{margin:0;background:var(--fond);color:var(--encre);
 font-family:"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
 line-height:1.6;font-size:15px;}
.wrap{max-width:1060px;margin:0 auto;padding:0 clamp(12px,3vw,28px) 40px;}
/* ---------- hero ---------- */
.hero{position:relative;color:#fff;overflow:hidden;
 background:linear-gradient(135deg,var(--jw-bleu-fonce),#12345f 60%,#1a4a8a);}
.hero img.fond{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
 opacity:.38;}
.hero .voile{position:absolute;inset:0;
 background:linear-gradient(180deg,rgba(11,37,69,.25),rgba(11,37,69,.82));}
.hero .contenu{position:relative;max-width:1060px;margin:0 auto;
 padding:clamp(28px,6vw,64px) clamp(12px,3vw,28px) clamp(22px,4vw,40px);}
.kicker{color:var(--jw-or);text-transform:uppercase;letter-spacing:3px;
 font-size:12px;font-weight:700;margin-bottom:10px;}
.hero h1{font-size:clamp(28px,5vw,46px);margin:0 0 6px;line-height:1.08;}
.hero h2{font-size:clamp(16px,2.6vw,22px);color:var(--jw-or);font-weight:600;
 margin:0 0 14px;}
.hero p.intro{color:#dbe4f2;font-size:15px;max-width:660px;margin:0 0 18px;}
.chiffres{display:flex;gap:clamp(14px,3vw,30px);flex-wrap:wrap;margin:6px 0 4px;}
.chiffres div{border-left:3px solid var(--jw-or);padding-left:12px;}
.chiffres b{display:block;font-size:clamp(20px,3vw,28px);}
.chiffres span{font-size:11px;color:#aab6cc;text-transform:uppercase;
 letter-spacing:1px;}
/* ---------- lecteur audio ---------- */
.player{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);
 backdrop-filter:blur(3px);border-radius:var(--radius);padding:10px 14px;
 margin-top:16px;max-width:640px;}
.player .t{font-size:12px;color:var(--jw-or);font-weight:700;
 text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
.player audio{width:100%;height:38px;display:block;}
.player.fiche{background:var(--jw-bleu-clair);border-color:#b9c9e2;}
.player.fiche .t{color:var(--jw-bleu);}
.print-audio{display:none;}
/* ---------- navigation ---------- */
.nav{position:sticky;top:0;z-index:50;background:rgba(11,37,69,.96);
 border-bottom:3px solid var(--jw-or);}
.nav .bar{max-width:1060px;margin:0 auto;padding:8px clamp(12px,3vw,28px);
 display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.nav a{color:#fff;text-decoration:none;font-size:12.5px;font-weight:600;
 padding:5px 11px;border-radius:20px;background:rgba(255,255,255,.10);
 white-space:nowrap;}
.nav a:hover{background:var(--jw-or);color:var(--jw-bleu-fonce);}
.nav a.accueil{background:var(--jw-or);color:var(--jw-bleu-fonce);}
/* ---------- cartes sommaire ---------- */
h1.t{font-size:clamp(22px,3.4vw,30px);color:var(--jw-bleu-fonce);
 margin:34px 0 4px;}
.st{color:var(--gris);font-size:14px;margin-bottom:16px;}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
 gap:18px;margin:16px 0 8px;}
.carte{background:var(--carte);border-radius:var(--radius);overflow:hidden;
 box-shadow:var(--ombre-legere);border:1px solid var(--bord);
 transition:transform .25s ease,box-shadow .25s ease;display:flex;
 flex-direction:column;}
.carte:hover{transform:translateY(-5px);box-shadow:var(--ombre);}
.carte a.img{display:block;aspect-ratio:16/9;overflow:hidden;background:#dfe5ee;}
.carte a.img img{width:100%;height:100%;object-fit:cover;display:block;}
.carte .txt{padding:14px 16px 16px;display:flex;flex-direction:column;gap:7px;
 flex:1;}
.carte .num{font-size:11px;font-weight:800;letter-spacing:2px;
 color:var(--jw-bleu);}
.carte h3{margin:0;font-size:17px;line-height:1.3;}
.carte h3 a{color:var(--jw-bleu-fonce);text-decoration:none;}
.carte h3 a:hover{color:var(--jw-bleu);}
.carte .meta{font-size:12px;color:var(--gris);margin-top:auto;}
/* ---------- fiche ---------- */
.fiche{background:var(--carte);border-radius:var(--radius);overflow:hidden;
 box-shadow:var(--ombre);border:1px solid var(--bord);margin:26px 0;
 scroll-margin-top:64px;}
.fiche .visuel{position:relative;aspect-ratio:21/9;max-height:340px;
 overflow:hidden;background:#dfe5ee;}
.fiche .visuel img{width:100%;height:100%;object-fit:cover;display:block;}
.fiche .visuel .legende{position:absolute;left:0;right:0;bottom:0;
 padding:22px 20px 8px;font-size:11px;color:#e8eef7;
 background:linear-gradient(180deg,transparent,rgba(11,37,69,.85));}
.fiche .hd{background:var(--jw-bleu-fonce);color:#fff;padding:16px 22px 14px;}
.fiche .hd .num{color:var(--jw-or);font-weight:800;font-size:11px;
 letter-spacing:2px;}
.fiche .hd h3{margin:4px 0 6px;font-size:clamp(20px,3vw,26px);line-height:1.2;}
.fiche .hd .ref{font-family:Consolas,"Courier New",monospace;font-size:12px;
 color:#b9c5d8;}
.fiche .bd{padding:18px clamp(14px,3vw,26px) 22px;}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px;}
.badge{background:var(--jw-bleu-clair);border:1px solid #b9c9e2;
 border-radius:20px;padding:3px 12px;font-size:12px;color:var(--jw-bleu);
 font-weight:600;}
.badge.or{background:#fdf6e3;border-color:var(--jw-or);color:var(--jw-or-fonce);}
.fiche h4{font-size:12.5px;text-transform:uppercase;letter-spacing:1.5px;
 color:var(--jw-bleu-fonce);margin:20px 0 8px;border-left:5px solid var(--jw-or);
 padding-left:9px;}
.fiche h4:first-of-type{margin-top:4px;}
.fiche p{margin:0 0 10px;font-size:14.5px;}
.txt{background:#f4f7fb;border-left:4px solid var(--jw-or);border-radius:0 10px
 10px 0;padding:10px 14px;margin:0 0 12px;}
.txt li{font-size:14px;margin-bottom:6px;font-style:italic;}
.attn{background:#fff8e8;border:1px solid var(--jw-or);border-left:5px solid
 var(--jw-or);border-radius:0 10px 10px 0;padding:11px 14px;font-size:13.5px;
 margin:12px 0;}
.attn b{color:var(--jw-or-fonce);}
.cadre{background:var(--creme);border:1px solid var(--bord);border-left:5px solid
 var(--jw-bleu);border-radius:0 10px 10px 0;padding:11px 14px;font-size:13.5px;
 margin:12px 0;}
.grille2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
table{border-collapse:collapse;width:100%;font-size:13px;margin:8px 0 12px;
 background:#fff;border-radius:10px;overflow:hidden;
 box-shadow:var(--ombre-legere);}
th,td{border:1px solid var(--bord);padding:6px 9px;text-align:left;
 vertical-align:top;}
th{background:var(--jw-bleu-fonce);color:#fff;font-size:11px;
 text-transform:uppercase;letter-spacing:.4px;}
td.d{white-space:nowrap;font-weight:700;color:var(--jw-bleu);}
tr:nth-child(even) td{background:#f7f9fc;}
.src{columns:2;column-gap:16px;font-size:12px;}
.src a{color:var(--jw-bleu);display:block;margin-bottom:5px;
 word-break:break-all;}
svg{max-width:100%;height:auto;}
ul.plain{list-style:none;padding-left:0;}
ul.plain li{font-size:14px;margin-bottom:7px;}
.pied{border-top:1px solid var(--bord);margin-top:14px;padding-top:8px;
 font-size:11.5px;color:var(--gris);display:flex;justify-content:space-between;
 flex-wrap:wrap;gap:6px;}
.haut{position:fixed;right:16px;bottom:16px;z-index:60;background:
 var(--jw-bleu-fonce);color:#fff;text-decoration:none;font-size:13px;
 font-weight:700;padding:9px 14px;border-radius:24px;
 box-shadow:var(--ombre);border:2px solid var(--jw-or);}
.prog{position:fixed;top:0;left:0;height:4px;background:var(--jw-or);width:0;
 z-index:70;}
footer.site{background:var(--jw-bleu-fonce);color:#aab6cc;font-size:12px;
 margin-top:30px;}
footer.site .in{max-width:1060px;margin:0 auto;
 padding:20px clamp(12px,3vw,28px);}
@media(max-width:640px){.grille2{grid-template-columns:1fr;}.src{columns:1;}
 .fiche .visuel{aspect-ratio:16/9;}}
@media print{
 body{background:#fff;font-size:12px;}
 .nav,.haut,.prog,.player audio{display:none !important;}
 .print-audio{display:block;font-size:11px;color:var(--gris);
  border:1px dashed #999;border-radius:8px;padding:5px 9px;margin-top:8px;}
 .hero img.fond{opacity:.18;}
 .hero{color:#000;background:#fff;border-bottom:3px solid var(--jw-bleu-fonce);}
 .hero .voile{display:none;}
 .hero h1,.hero h2,.hero p.intro,.chiffres b{color:#000 !important;}
 .kicker{color:var(--jw-or-fonce);}
 .chiffres span{color:#333;}
 .carte,.fiche{box-shadow:none;break-inside:avoid;}
 .fiche{border:1.5px solid #999;}
 .wrap{max-width:none;}
 @page{size:A4;margin:11mm;}
}
"""

# Légende standard des illustrations (jamais des documents).
LEGENDE_IMG = ("Illustration — image générée pour ce dossier privé : ni "
               "photographie d'un site réel, ni reproduction d'un artefact.")


def e(s):
    return html.escape(str(s), quote=False)


def norm(s):
    """Normalise pour comparaison : minuscules, alphanumerique seul."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_audio(fn):
    """fiche_A01_tyr.mp3 -> (num=1, core='tyr', intro=False, lettres='A').
    fiche_T2_07_abandon.mp3 -> (7, 'abandon', False, 'T').
    fiche_T2_intro.mp3 / fiche_JK_intro.mp3 -> (None, ..., True, lettres)."""
    m = re.match(r"^fiche_([A-Z]+)(\d*)(?:_(\d+))?_(.+)\.mp3$", fn)
    if not m:
        return None
    lettres, v, num2, core = m.group(1), m.group(2), m.group(3), m.group(4)
    if core.startswith("intro"):
        return {"num": None, "core": core, "intro": True,
                "lettres": lettres, "fn": fn}
    if num2 and len(v) == 1:
        # schema versionne : T2_07_abandon, C2_06_entree -> num = 2e groupe
        num = int(num2)
    elif num2:
        # theme commencant par des chiffres : B02_70_ans -> num 2, theme 70_ans
        num = int(v)
        core = num2 + "_" + core
    else:
        num = int(v) if v else None
    return {"num": num, "core": core, "intro": False,
            "lettres": lettres, "fn": fn}


def parse_img_core(img):
    """images/prophe_T007_abandon.jpg -> 'abandon'."""
    base = os.path.basename(img)
    base = re.sub(r"^prophe_", "", base)
    base = re.sub(r"^[A-Z]+\d+_", "", base)
    base = re.sub(r"\.(jpg|jpeg|png)$", "", base)
    return base


def parse_fiche_num(n):
    """'T007' -> 7 ; 'R002' -> 2."""
    m = re.search(r"(\d+)$", n or "")
    return int(m.group(1)) if m else None


def load_durations():
    try:
        return json.load(open(DUR_PATH, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def duree_txt(sec):
    if sec is None:
        return ""
    sec = int(round(sec))
    return f"{sec // 60}:{sec % 60:02d}"


def build_audio_index():
    """Retourne (par_num_core, intros) pour tout le dossier audio/."""
    idx, intros = {}, []
    if not os.path.isdir(AUD_DIR):
        return idx, intros
    for fn in sorted(os.listdir(AUD_DIR)):
        if not fn.endswith(".mp3"):
            continue
        p = parse_audio(fn)
        if not p:
            continue
        if p["intro"]:
            intros.append(p)
        else:
            idx.setdefault((p["num"], norm(p["core"])), []).append(p)
    return idx, intros


def lettres_fiche(n):
    m = re.match(r"^([A-Z]+)", n or "")
    return set(m.group(1)) if m else set()


def audio_pour_fiche(f, idx, mod_lettres=None):
    """Apparie une fiche a son MP3 : (1) numero + theme exacts, desambigue
    par les lettres du module ; (2) repli : numero + lettres de la fiche
    (variantes de theme : raphia/nordsud, bethlehem/bethleem...).
    Retourne (mp3, flou) ; mp3 est None si echec."""
    mod_lettres = mod_lettres or set()
    num = parse_fiche_num(f.get("n"))
    core = norm(parse_img_core(f.get("img", "")))
    cands = idx.get((num, core), [])
    if cands:
        filt = [c for c in cands if set(c["lettres"]) & mod_lettres]
        if len(filt) == 1:
            return filt[0]["fn"], False
        if len(filt) > 1:
            return None, False
        if len(cands) == 1:
            return cands[0]["fn"], False
        return None, False
    # repli : meme numero + lettres communes fiche/audio, unique
    lf = lettres_fiche(f.get("n"))
    if num is not None and lf:
        fuzzy = []
        for (n2, _c2), lst in idx.items():
            if n2 != num:
                continue
            for c in lst:
                if set(c["lettres"]) & lf:
                    fuzzy.append(c["fn"])
        fuzzy = list(dict.fromkeys(fuzzy))
        if len(fuzzy) == 1:
            return fuzzy[0], True
    return None, False


def intros_pour_module(fiches, intros):
    """Pistes d'intro dont les lettres recoupent celles des fiches."""
    lettres = set()
    for f in fiches:
        m = re.match(r"^([A-Z]+)", f.get("n", ""))
        if m:
            lettres.update(m.group(1))
    out = []
    for p in intros:
        if set(p["lettres"]) & lettres:
            out.append(p["fn"])
    # dédoublonne en gardant l'ordre
    out = list(dict.fromkeys(out))
    # exactitude d'abord : si des intros recouvrent EXACTEMENT les lettres du
    # module (ex. GE_intro pour GE), on ne garde qu'elles.
    if lettres:
        exact = [fn for fn in out
                 for p in intros if p["fn"] == fn and set(p["lettres"]) == lettres]
        if exact:
            return list(dict.fromkeys(exact))
    return out


def couverture_pour_module(code, fiches):
    """Image de couverture : prophe_*_couverture.jpg si elle matche le code,
    sinon l'image de la premiere fiche."""
    try:
        cands = [f for f in os.listdir(IMG_DIR) if "_couverture" in f]
    except OSError:
        cands = []
    key = (code or "").replace("–", "").replace("-", "")
    stems = {}
    for c in cands:
        stem = re.sub(r"^prophe_", "", c).replace("_couverture.jpg", "")
        stems.setdefault(stem, c)
    for want in (key, code, key + "2"):
        if want in stems:
            return "images/" + stems[want]
    for stem in sorted(stems):
        if stem.startswith(key) and len(stem) == len(key) + 1:
            return "images/" + stems[stem]
    if fiches:
        return fiches[0].get("img", "")
    return ""
