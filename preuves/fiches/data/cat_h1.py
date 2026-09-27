#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE G-H (vague de transition) — RESTAURATION (2e partie) + LE SIGNE
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="G–H",
    nom="Restauration et monde nouveau (2e partie) · Le signe et les derniers jours",
    vague="9",
    intro=(
        "Cette vague de transition ferme la catégorie G et ouvre la catégorie H. "
        "Côté restauration, quatre dernières fiches : les 144 000 (nombre littéral "
        "prouvé par le contraste, Dan absent et Lévi présent), la grande foule "
        "(innombrable, palmes des Huttes, applicable dès maintenant), le fleuve "
        "et les feuilles pour la guérison des nations (Ézéchiel 47 avec Révélation "
        "22, la boucle d'Éden), et Jéhovah qui devient Roi (Zacharie 14, les "
        "psaumes du Règne, le septième trompette et l'Alléluia). La catégorie G "
        "compte ainsi 9 fiches et est terminée. Côté signe, cinq premières fiches : "
        "le cadre des Oliviers (deux questions, le figuier, Noé, « personne ne "
        "sait » — avec l'état 1992 cité comme daté et l'actuel renvoyé, méthode "
        "E007), les guerres (1914, le roux, les douleurs), les famines, pestes et "
        "séismes (Luc seul pour les pestes, magnitude distinguée des victimes), "
        "la prédication mondiale (le seul signe joyeux, vérifiable : 212 pays en "
        "1990), et les traits des derniers jours (19 ou 20 selon le découpage — "
        "et « pas la preuve principale »). Périmètre : la grande tribulation et "
        "« paix et sécurité » appartiennent à la vague 10."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G006", titre="Les 144 000 — comptés, scellés, prémices",
 ref="Révélation 7:4-8 ; 14:1-5 ; Luc 12:32 ; Jean 10:16 ; Galates 6:16 ; Exode 19:5-6",
 statut="En cours (choix « à peu près achevé » : renvoi)",
 cat="G", syst="Système 33/36/1914",
 reg="Registre : Révélation — P832 (7:4-8), P878 (14:1-3), P879 (14:4-5) ; Jean — P701 (10:16) ; Exode — P045 (19:5-6) ; Lc 12:32, Ga 6:16, 2Co 11:2 sans entrée (C8)",
 texte=[
  "« J'entendis le nombre de ceux qui furent scellés : 144 000, de TOUTES les "
  "tribus des fils d'Israël — 12 000 de chaque. » (Ré 7:4-8)",
  "« L'Agneau debout sur le mont Sion, et avec lui 144 000 ayant son nom et le "
  "nom de son Père écrits sur leurs fronts. » (Ré 14:1 — Sion CÉLESTE : Hé 12:22)",
  "« Ils chantent un cantique NOUVEAU que PERSONNE ne pouvait apprendre. » "
  "(Ré 14:3 — expérience unique)",
  "« Vierges, suivant l'Agneau PARTOUT, achetés d'entre le genre humain comme "
  "PRÉMICES, sans mensonge. » (Ré 14:4-5)",
  "« N'aie pas peur, PETIT troupeau, car votre Père a APPROUVÉ de vous donner "
  "le Royaume. » (Lc 12:32 — mikron poimnion !)",
 ],
 contexte=(
  "Entre le 6e et le 7e sceau (7:1-3) : les vents RETENUS — « ne faites pas de mal… "
  "jusqu'à ce que nous ayons scellé » : le sursis permet le scellement. Sion "
  "céleste (Hébreux 12:22 — voir G002), pas Moriah. « Achetés » (agorazô : au "
  "MARCHÉ — prix payé : 1Co 6:20 !). Pentecôte 33 : les premiers scellés "
  "(voir F018) ; 36 : les nations entrent (voir C012). 1935 : la foule identifiée "
  "→ le choix des 144 000 « alors à peu près achevé » (détail renvoyé au livre "
  "Révélation, voir Limites)."
 ),
 explication=(
  "144 000 LITTÉRAL : le contraste 7:4 (nombré) contre 7:9 (innombrable) — « la "
  "force du contraste » : si 144 000 était symbolique-illimité, le contraste "
  "s'effondre. « Prémices » (14:4) : petite sélection — troisième rang après Jésus "
  "(1Co 15) et les disciples (Jc 1:18) — voir F018 ! 12 × 12 000 : douze (peuple "
  "de Dieu) × mille (multitude complète) — structure symbolique, total littéral. "
  "Dan ABSENT (idolâtrie de Juges 18 ? « serpent » de Genèse 49:17 ? — raison "
  "renvoyée, voir Limites) ; Lévi PRÉSENT — sans territoire dans l'Ancien "
  "Testament (Nb 18 : « Jéhovah = leur part ») : PREUVE que ce n'est pas l'Israël "
  "charnel ; Manassé nommé (Joseph couvre). « Scellés » (sphragizô : 2Co 1:21-22, "
  "Ép 1:13, 4:30 — le sceau, c'est l'esprit : acompte !). Nom sur les fronts "
  "(Père + Agneau — contre la marque de la bête, 13:16-17 : renvoi I). Cantique "
  "nouveau (14:3, cf. 5:9) : « nul ne pouvait » — chant d'expérience. « Vierges » "
  "(parthenoi : SPIRITUELLES — 2Co 11:2, « vierge pure » ! ; « femmes » : sens "
  "renvoyé à I). « Suivent PARTOUT » (hopou an : imitation totale). « Sans "
  "mensonge » (14:5 : So 3:13 — « reste… langue trompeuse » !). « Petit troupeau » : "
  "petit MAIS approuvé. « Royaume de PRÊTRES » (Ex 19:5-6, P045 ; 1P 2:9 : « nation "
  "sainte… royale » !). Nouvelle alliance LIMITÉE aux 144 000 — bienfaits au monde "
  "entier (voir G002)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : l'Israël SPIRITUEL (Ga 6:16, « Israël "
  "de Dieu » ; Jc 1:1, « douze tribus dispersées » ; Rm 2:28-29, 9:6 — voir G002). "
  "Nombre exact et limité — « petit » devant la foule (Lc 12:32 contre Ré 7:9). "
  "Appel : Pentecôte 33, nations dès 36, choix à travers les siècles, « à peu près "
  "achevé » en 1935 (remplacements ensuite — renvoi nominal). Ils règnent « sur "
  "la terre » (5:9-10 ; 20:6 — voir F017) : rois ET prêtres sous le Roi-Prêtre "
  "Melchisédek (Hé 7)."
 ),
 accomplissement=[
  ("Pentecôte 33", "Premiers scellés : 120, puis 3 000 (voir F018)"),
  ("36 de n. è.", "Corneille : les nations entrent (voir C012)"),
  ("Ier-XXe s.", "Le choix à travers les siècles (douze tribus spirituelles)"),
  ("1935 de n. è.", "Foule identifiée → choix « à peu près achevé » (renvoi)"),
  ("1914 + de n. è.", "Première résurrection « en cours » (voir F017, G004)"),
  ("Millénium", "Règne : rois et prêtres (voir F017)"),
 ],
 hist=(
  "Pentecôte (Juifs et prosélytes : les premiers). Dan (Juges 18 : idolâtrie "
  "tribale — observation, pas conclusion). Lévi (Nombres 18 : pas de part — "
  "« Jéhovah = leur part » — PRÉSENT ici : la preuve). 1935 (Washington : "
  "identification de la foule — renvoi nominal au livre Révélation). « Petit "
  "troupeau » (Lc 12:32 : « n'aie pas peur » — petitesse rassurée)."
 ),
 geo=(
  "Sion CÉLESTE (Hé 12:22 — pas Moriah : le ciel). Douze tribus : les NOMS sans "
  "les territoires — pas de carte. « D'entre le genre humain » (ek : extraits — "
  "de TOUTES nations, pas de Palestine). « Sur la terre » (5:10) : règne d'en "
  "haut sur le paradis (voir G003, G005)."
 ),
 sci=(
  "12 000 × 12 = 144 000 : exact. Contraste nombré/innombrable : logique — "
  "l'argument du Questions des lecteurs, cité. « Prémices » : agronomie — la "
  "première part, petite (voir F018). Sceau antique : propriété + authenticité "
  "(2Co 1:22 : « acompte »)."
 ),
 limites=(
  "Dan absent : raison renvoyée à la catégorie I. « Femmes » (14:4) : sens "
  "renvoyé à I. Marque de la bête (13:16-17) : renvoi I. 1935 : détail renvoyé "
  "au livre Révélation. Luc 12:32, Galates 6:16, 2 Corinthiens 11:2 sans entrée "
  "au registre (C8)."
 ),
 tl=[("33", "Premiers : Pentecôte"), ("36", "Nations : Corneille"), ("Siècles", "Choix"),
     ("1935", "« Achevé » (renvoi)"), ("1914 +", "1re : en cours"), ("Millénium", "Règne")],
 src=[("Les bienfaits de la nouvelle alliance (144 000, Sion, prémices)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1966123"),
      ("Une grande foule innombrable (outre les 144 000, Israël spirituel)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101988020"),
      ("Révélation 7 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/7"),
      ("Révélation 14 — Bible d'étude, notes (Sion, prémices)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/14")],
 img="images/prophe_G006_144000.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G007", titre="La grande foule — innombrable, en palmes, déjà lavée",
 ref="Révélation 7:9-17 ; Jean 10:16 ; Zacharie 8:23 ; Ésaïe 49:10 ; Lévitique 23:40",
 statut="En cours (identifiée 1935 : renvoi ; survie : à venir)",
 cat="G", syst="Système 33/1914 (1935 : renvoi)",
 reg="Registre : Révélation — P833 (7:9-10), P835 (7:14), P836 (7:15-17) ; Jean — P701 (10:16)",
 texte=[
  "« APRÈS ces choses : une grande foule que PERSONNE ne pouvait compter, de "
  "TOUTES nations, tribus, peuples et langues — robes blanches, palmes. » "
  "(Ré 7:9 — second groupe !)",
  "« Ils crient d'une voix forte : LE SALUT à notre Dieu et à l'Agneau ! » "
  "(7:10 — une seule voix)",
  "« Ceux-ci SORTENT de la grande tribulation ; ils ont BLANCHI leurs robes "
  "dans le SANG de l'Agneau. » (7:14 — ek : survivent ! blanc dans rouge !)",
  "« Ils servent jour et nuit dans son temple ; Celui sur le trône ÉTENDRA sur "
  "eux sa tente. » (7:15 — skenoo : voir G005 !)",
  "« Plus de faim, plus de soif, plus de soleil ; l'Agneau-BERGER les guidera "
  "aux sources ; Dieu essuiera leurs larmes. » (7:16-17 — Is 49:10 + 25:8 !)",
  "« J'ai d'AUTRES brebis : UN seul troupeau, UN seul berger. » (Jn 10:16 — "
  "allos : autres, pas différentes !)",
 ],
 contexte=(
  "APRÈS les 144 000 (7:9 : « après ces choses » — deuxième groupe !). Les vents "
  "retenus (7:1-3) : le SURSIS permet la foule — outre l'Israël spirituel. Un "
  "ancien EXPLIQUE (7:13-17 : « qui sont-ils ? d'où ? » — le dialogue !). Grande "
  "tribulation (Mt 24:21 — détail : vague 10) : Babylone la Grande D'ABORD, puis "
  "délivrance au paroxysme (reste + foule — Ré 7:1, 18:2). Et DÈS MAINTENANT : "
  "l'expression s'applique avant la tribulation (espérance terrestre, service "
  "actuel — avant l'attaque contre la fausse religion)."
 ),
 explication=(
  "« Personne ne pouvait » (ouk edunato : IMPOSSIBLE — contre 144 000 comptés : "
  "le contraste PROUVE les deux !). Quatre termes (nations/tribus/peuples/langues : "
  "TOTALITÉ — comme Ré 14:6, voir H004 !). « Blanchies DANS LE SANG » : paradoxe — "
  "le sang TACHE, ici il BLANCHIT : justes par la FOI au sacrifice. Palmes "
  "(phoinix : Jean 12:13 — accueil ROYAL des Rameaux ! + Lévitique 23:40 — HUTTES ! "
  "voir F018 : la foule des Huttes, saluant le Messie Roi !). Cri UNANIME (7:10 : "
  "« d'une voix forte » — une voix, toutes langues !). « SORTENT » (ek tès thlipseôs : "
  "SURVIVENT — pas ressuscitent !). Service (latreuo : SACRÉ — jour et nuit !). "
  "« Dans son temple » : détail renvoyé à I (naos ? cour ? — voir Limites). Tente "
  "ÉTENDUE (7:15 : skenoo — « tente AVEC », voir G005 !). 7:16 = Ésaïe 49:10 CITÉ "
  "(« ni faim ni soif… ni mirage » — le RETOUR d'exil, comme 537, voir B002 !). "
  "7:17 : l'Agneau-BERGER (paradoxe — Ps 23 : « eaux paisibles » !) + « essuiera » "
  "(Is 25:8 — voir G004, G005 !). « Autres brebis » (allos, pas heteros : autres, "
  "non différentes — « petit troupeau », Lc 12:32, C8, contre foule). Zacharie 8:23 "
  "(voir G002 : « dix hommes saisiront le pan » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : l'espérance TERRESTRE — foule "
  "internationale, nombre NON déterminé (« aucun homme ne peut le prédire »). "
  "Ils SURVIVENT (pas ressuscitent) : lavés DÉJÀ — « pratiquants du vrai culte » "
  "maintenant. « Applicable DÈS MAINTENANT » à l'espérance terrestre avant "
  "l'éclatement (attaque contre Babylone la Grande). Identifiée en 1935 (renvoi "
  "nominal au livre Révélation — comme G006). Séquence : Babylone d'abord, "
  "délivrance au paroxysme (reste des 144 000 + foule)."
 ),
 accomplissement=[
  ("33 + de n. è.", "Brebis rassemblées (« autres brebis », Jn 10:16)"),
  ("1935 de n. è.", "Identifiée (renvoi nominal au livre Révélation)"),
  ("Maintenant", "Lavées : service sacré, espérance terrestre"),
  ("Tribulation (à venir)", "Babylone attaquée (détail : vague 10)"),
  ("« SORTENT » (à venir)", "Survivent : délivrés au paroxysme"),
  ("Millénium", "Plus faim ni soif : sources (voir F017)"),
 ],
 hist=(
  "1935 (Washington — renvoi nominal). Rameaux (Jn 12:13 : palmes au ROI — même "
  "geste !). Huttes (Lv 23:40 : palmes — voir F018 : la fête de la cueillette !). "
  "Ésaïe 49:10 (retour d'exil : « ni faim ni soif » — comme 537, voir B002). "
  "« Tente » (tabernacle — voir G005 : Dieu campe avec nous)."
 ),
 geo=(
  "TOUTES nations (quatre termes — aucun pays exclu). « Devant le trône » : "
  "DEBOUT — position d'approuvés. « Temple » : lieu du service — détail à I. "
  "Sources d'eaux (7:17 : Psaume 23 — le Berger mène)."
 ),
 sci=(
  "Innombrable contre nombré : logique du contraste (voir G006). « Blanc dans "
  "rouge » : paradoxe — chimiquement le sang tache : miracle SYMBOLIQUE, dit. "
  "Quatre termes (ethnos/phylè/laos/glôssa) : totalité linguistique."
 ),
 limites=(
  "« Temple » (7:15, naos ? cour ?) : détail renvoyé à la catégorie I. 1935 : "
  "détail renvoyé au livre Révélation. Grande tribulation : détail à la vague 10. "
  "Luc 12:32 sans entrée (C8 — voir G006)."
 ),
 tl=[("33 +", "Brebis"), ("1935", "Identifiée (renvoi)"), ("Maintenant", "Lavées, service"),
     ("Tribulation", "Babylone (v10)"), ("« SORTENT »", "Survivent"), ("Millénium", "Sources")],
 src=[("Une grande foule innombrable (7:9-17, tribulation, tente)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101988020"),
      ("Qui est la grande foule ? (survivent, dès maintenant, 1995)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1995288"),
      ("Révélation 7 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/7"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_G007_foule.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G008", titre="Le fleuve et les feuilles — la boucle d'Éden",
 ref="Révélation 22:1-5 ; Ézéchiel 47:1-12 ; Zacharie 14:8 ; Genèse 2:10 ; 3:22-24 ; Psaume 1:3",
 statut="À venir (dès le début du millénium)",
 cat="G", syst="Système 593/96 · millénium (F017)",
 reg="Registre : Révélation — P959 (22:1-2), P960 (22:3-4), P961 (22:5) ; Ézéchiel — P366 (47:1-12) ; Zacharie — P511 (14:1-21)",
 texte=[
  "« Un fleuve d'eau de la vie, limpide comme du cristal, SORTANT du trône de "
  "Dieu et de l'Agneau, au milieu de la grande voie. » (Ré 22:1 — ekporeuomenon !)",
  "« Des deux côtés, des arbres de vie : 12 récoltes, chaque mois ; les feuilles "
  "POUR LA GUÉRISON des nations. » (22:2 — therapeia : notre THÉRAPIE !)",
  "« Plus AUCUNE malédiction ; ils verront son visage ; son nom sur leurs fronts ; "
  "plus de nuit ; ils RÉGNERONT à tout jamais. » (22:3-5)",
  "« Un torrent sortait de la maison : 1 000 coudées — chevilles ; 1 000 — genoux ; "
  "1 000 — taille ; 1 000 — INFRANCHISSABLE. » (Éz 47:1-5 — 593 av. n. è.)",
  "« Les eaux de la mer seront GUÉRIES ; TOUT vivra ; des pêcheurs d'En-Guédi à "
  "En-Églaïm ; fruits pour nourriture, feuilles pour GUÉRIR. » (Éz 47:8-12)",
  "« Des eaux vives sortiront de Jérusalem : moitié vers la mer ORIENTALE, moitié "
  "vers l'OCCIDENTALE — été et hiver. » (Za 14:8)",
 ],
 contexte=(
  "Ézéchiel, exilé en 593 : torrent de la « maison symbolique » — devant l'autel, "
  "vers la mer Salée (Morte). Jean, ~96 : APRÈS le millénium du chapitre 20 "
  "(voir F017) — chapitres 21-22 : L'APRÈS (voir G005). Le fleuve COMMENCE après "
  "Harmaguédon et la chute de Satan dans l'abîme — « au début du règne millénaire ». "
  "Éden : un fleuve SORTAIT (Gn 2:10) — puis chérubins et épée (3:24 : FERMÉ). "
  "Révélation 22 : LIBRE — la boucle."
 ),
 explication=(
  "« SORTANT » (du TRÔNE : source divine — comme Gn 2:10 !). « Cristal » : pureté. "
  "« Au milieu de la RUE » (plateia : GRANDE VOIE — fleuve EN VILLE !). « Bois de "
  "vie » (xylon, collectif — des deux côtés !). Douze récoltes (« chaque mois » : "
  "PAS de saison morte !). Feuilles THERAPEIA (« comme certaines plantes "
  "médicinales » — digitale, quinine, saule : RÉELLES !). « Plus de malédiction » "
  "(katathema : Genèse 3:17-19 LEVÉE !). « Verront son visage » (Mt 5:8, « cœur pur » "
  "— Exode 33:20 INVERSÉ : voir et VIVRE !). Nom sur les fronts (contre la marque — "
  "voir G006). « Plus de nuit » (Jéhovah = lumière : Is 60:19-20 !). « Régneront » "
  "(22:5 : pas subir — RÉGNER ; qui ? renvoyé à I, voir Limites). Ézéchiel 47 : "
  "mille coudées ×4 (~500 m ×4 ≈ 2 km — coudée ~50 cm) — le torrent GRANDIT "
  "(chevilles → infranchissable !). Mer MORTE guérie (« GUÉRIES… TOUT vivra » — "
  "la mer MORTE VIT !). Pêcheurs (En-Guédi → En-Églaïm : TOUTE la côte ouest — "
  "« comme la Grande Mer » !). Marais SALÉS (47:11 : « abandonnés au sel » — pas "
  "TOUT guéri : non expliqué ici, renvoyé, voir Limites). Arbres : fruits "
  "(nourriture) + feuilles (guérison) — 47:12 = Ré 22:2. Zacharie 14:8 : deux mers "
  "(Morte + Méditerranée !), deux saisons (« été ET hiver »). Genèse 3:24 → "
  "Ré 22 : FERMÉ → LIBRE — chérubins levés. Psaume 1:3 (« fruit en sa saison… "
  "pas flétri »)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : le fleuve coule DÈS le début du "
  "millénium (après Harmaguédon + abîme). Guérison RÉELLE — « réellement la "
  "guérison… santé complètement rétablie » : pas un symbole. TROIS dons : eau "
  "(vie), fruits (nourriture), feuilles (santé). Les nations guéries : « celles "
  "qui marchent à la lumière de la ville » (21:24). Progression millénaire "
  "(voir F017, G005 : effacement progressif)."
 ),
 accomplissement=[
  ("Éden", "Fleuve + arbre de vie (Gn 2:10)"),
  ("Chute", "FERMÉ : chérubins et épée (Gn 3:24)"),
  ("593 av. n. è.", "Ézéchiel 47 : le torrent (exil)"),
  ("~520 av. n. è.", "Zacharie 14:8 : les deux mers"),
  ("31 de n. è.", "« Fleuves d'eau vive » (Jn 7:38 — voir F018)"),
  ("~96 de n. è.", "Révélation 22 : la vision"),
  ("Millénium", "Le fleuve COULE (voir F017)"),
 ],
 hist=(
  "593 (Ézéchiel exilé — « maison symbolique »). Mer Morte (34 % de sel, dix fois "
  "l'océan — « morte » — VIVRA : dessalement miraculeux, dit). En-Guédi (oasis — "
  "David, 1S 24 !). Pêcheurs (« Grande Mer » = Méditerranée). Phytothérapie "
  "(digitale, quinine, saule-aspirine : feuilles qui guérissent — RÉEL)."
 ),
 geo=(
  "Temple → autel → EST → Arabah → mer Morte (Éz 47:1-8 : le trajet — 2 km "
  "mesurés, puis torrent). En-Guédi → En-Églaïm (47:10 : toute la côte ouest). "
  "Deux mers (Za 14:8 : Morte + Méditerranée). Genèse 2:10 (Pishon… Euphrate : "
  "quatre bras). « Rue » (plateia : fleuve URBAIN — en ville sainte)."
 ),
 sci=(
  "1 000 coudées ×4 (≈ 2 km, coudée ~50 cm : ordre). Mer Morte à 34 % : guérison = "
  "dessalement — miracle, dit. Douze récoltes : pas de saison (« été et hiver », "
  "Za 14:8). Therapeia : phytothérapie réelle (digitale, quinine, saule). « Tout "
  "vivra » : écologie restaurée."
 ),
 limites=(
  "Marais salés (47:11) : non expliqués ici — renvoyés. « Régneront » (22:5, qui ?) : "
  "renvoyé à la catégorie I. Mécanisme : miracle, dit. Coudée (~50 cm) : ordre "
  "de grandeur."
 ),
 tl=[("Éden", "Fleuve, arbre"), ("Chute", "FERMÉ"), ("593", "Éz 47 : torrent"), ("520", "Za 14 : 2 mers"),
     ("31", "Jn 7 : fleuves"), ("96", "Ré 22"), ("Millénium", "COULE")],
 src=[("Une véritable fontaine de vie éternelle (Ré 22, Éz 47, millénium)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1967764"),
      ("Invitation à boire l'eau de la vie (feuilles, nations, lumière)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101963031"),
      ("Révélation 22 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/22"),
      ("Ézéchiel 47 — Bible d'étude, notes (torrent, mer guérie)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/47")],
 img="images/prophe_G008_fleuve.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G009", titre="Jéhovah devient Roi — un seul nom sur toute la terre",
 ref="Zacharie 14 ; Psaumes 93, 96-99 ; Abdias 21 ; Révélation 11:15 ; 19:6 ; Matthieu 6:9-10",
 statut="En cours (1914 : céleste ; « un seul nom » : à venir)",
 cat="G", syst="Système 1914 · millénium (F017)",
 reg="Registre : Zacharie — P511 (14:1-21) ; Révélation — P856 (11:15-19), P918 (19:6-8) ; Abdias — P446 (21) ; Ps 96-99 sans entrée (C8)",
 texte=[
  "« Jéhovah DEVIENDRA roi sur toute la terre ; en ce jour-là, Jéhovah sera UN, "
  "et son nom UN. » (Za 14:9 — futur : INAUGURATION !)",
  "« Ses pieds se poseront sur le mont des Oliviers, qui se FENDRA — très grande "
  "vallée ; et Jéhovah mon Dieu viendra, TOUS les saints avec lui. » (14:4-5)",
  "« Jour UNIQUE : le SOIR, il y aura de la LUMIÈRE. » (14:7 — inversion !)",
  "« Plus d'ANATHÈME ; les nations survivantes MONTERONT chaque année à la fête "
  "des HUTTES — sinon, pas de pluie. » (14:11, 16-19 — voir F018 !)",
  "« Sur les clochettes des chevaux : SAINTETÉ ; plus de Cananéen dans la "
  "maison. » (14:20-21 — profane → sacré !)",
  "« DITES parmi les nations : Jéhovah EST DEVENU ROI ! » (Ps 96:10 ; 97:1 ; 99:1 "
  "— proclamation !)",
  "« Des SAUVEURS monteront sur Sion… et la royauté sera à Jéhovah. » "
  "(Ab 21 — DERNIER verset d'Abdias !)",
  "« Le royaume du monde EST DEVENU celui de notre Seigneur — septième trompette. » "
  "(Ré 11:15 — aoriste : ACCOMPLI !)",
  "« ALLÉLUIA ! Jéhovah… RÈGNE — comme voix d'eaux et de tonnerres. » (Ré 19:6 — "
  "hallelou-YAH !)",
 ],
 contexte=(
  "Zacharie (~520-518 — voir D011) : chapitre 14, FIN du livre — après les visions "
  "nocturnes (1-6). Psaumes du Règne (93, 96-99) : « est devenu roi » — proclamation "
  "aux nations. Abdias (contre ÉDOM — 21 versets : le 21e bascule à Jéhovah Roi !). "
  "Révélation : 7e trompette (11:15) + 19:6 (après Babylone jugée, 19:1-2). "
  "Matthieu 6:9-10 (« que ton nom soit SANCTIFIÉ… que ton règne vienne » — "
  "Éz 36:23 : « je sanctifierai mon GRAND nom » : le BUT — vindication !)."
 ),
 explication=(
  "« DEVIENDRA » (Za 14:9 : futur — pas « est » : INAUGURATION, voir 1914). "
  "« UN… UN » (echad : Dt 6:4, « Jéhovah UN » ! Ml 2:10, Ga 3:20 — + « son nom UN » : "
  "Is 42:8, « ma gloire à nul autre » ! 44:6). Ha'arets (Rbi8 : terre OU pays — "
  "les deux sens !). Pieds sur les Oliviers (14:4 : SYMBOLIQUE — détail renvoyé, "
  "voir Limites). Montagne FENDUE (est-ouest, « très grande vallée », moitiés "
  "nord/sud — fuite « comme au tremblement » d'Ozias, Am 1:1, 14:5 !). Saints AVEC "
  "(14:5 : armée céleste). « Le soir : lumière » (14:7, « jour UNIQUE » : astronomie "
  "inversée — miracle, dit). « Plus d'anathème » (cherem, 14:11 : plus de "
  "voué-à-destruction — Jérusalem SÛRE). Nations aux HUTTES (14:16-19 : SURVIVANTS, "
  "« d'année en année » — pèlerinage ÉTERNEL ; « pas de pluie » : sanction "
  "climatique ; Égypte punie, 14:18-19 — voir F018 !). Clochettes SAINTETÉ (14:20 : "
  "chevaux, marmites — TOUT saint ; « Cananéen » 14:21 : marchand ? — sens renvoyé). "
  "« EST DEVENU ROI » (Ps 96:10, 97:1, 99:1 — TMN « est devenu roi » ; hébreu "
  "yahweh malakh : versions PARTAGÉES — règne / deviendra / devint : signalée, voir "
  "Limites). « DITES parmi les nations » (96:10 : PROCLAMATION — voir H004 !). « Tous "
  "les dieux prosternés » (97:7 : CITÉ en Hé 1:6, « que tous les anges » !). "
  "Ob 21 (« SAUVEURS » pluriel — « jugeront Ésaü » — royauté à Jéhovah : FIN du livre !). "
  "« EST DEVENU » (Ré 11:15 : aoriste — ACCOMPLI — « aux siècles » !). « Alléluia » "
  "(19:6 : hallelou-YAH — « louez Yah » — + Ps 97:1 en renvoi ! — « voix d'eaux… "
  "tonnerres »)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1914 — inauguration CÉLESTE (« est "
  "devenu roi », voir B009). « Un seul nom » : fin des religions — un seul culte "
  "(millénium, voir F017). Huttes OBLIGATOIRES pour les nations (pluie = "
  "bénédiction). « Plus d'anathème » : sécurité éternelle. Alléluia (19:6) : la "
  "louange du Règne. Sanctification du nom (Mt 6:9, Éz 36:23) : le BUT de tout — "
  "vindication."
 ),
 accomplissement=[
  ("Xe s. av. n. è. ?", "Psaumes du Règne : « est devenu roi »"),
  ("IXe s. av. n. è. ?", "Abdias 21 : la royauté à Jéhovah"),
  ("~520 av. n. è.", "Zacharie 14 : pieds, eaux (voir G008), Roi, Huttes"),
  ("1914 de n. è.", "« Est devenu roi » : céleste (voir B009)"),
  ("Millénium", "« Un seul nom » (voir F017)"),
  ("Fin", "« Dieu tout en tous » (voir F017)"),
 ],
 hist=(
  "1914 (voir B009). Oliviers (Ac 1:12 : ascension — « reviendra DE LA MÊME MANIÈRE », "
  "1:11 — lien avec Za 14:4 : lecture signalée, voir Limites). Ozias (Am 1:1 : "
  "tremblement — précédent sismique cité par Za 14:5 !). Huttes (voir F018). "
  "Alléluia (Ps 104-106, 111-118, 146-150 : « louez Yah »). 7e trompette (Ré 11:15 : "
  "dernière — voir catégorie I)."
 ),
 geo=(
  "Oliviers (EST de Jérusalem — fendu EST-OUEST !). Vallée (nord/sud — fuite). "
  "Jérusalem (14:11 : « habitée en SÉCURITÉ »). Nations qui MONTENT (14:16 : "
  "« d'année en année » — pèlerinage éternel). Égypte (14:18 : punie — pas de pluie)."
 ),
 sci=(
  "« Fendue » : séisme (Ozias, Am 1:1 — précédent cité !). « Soir : lumière » : "
  "miracle, dit. « Pas de pluie » : sanction climatique (agronomie). Ha'arets : "
  "terre/pays — note Rbi8, les deux sens."
 ),
 limites=(
  "Pieds, vallée (14:4-5) : symbolique — détail renvoyé aux publications. « Est "
  "devenu roi » : versions partagées (règne/deviendra/devint) — signalée. Cananéen "
  "(14:21, marchand ?) : sens renvoyé. Lien Actes 1:11-12 : lecture signalée. "
  "Psaumes 96-99 sans entrée au registre (C8)."
 ),
 tl=[("Xe s. ?", "Ps : Roi"), ("IXe s. ?", "Ab 21"), ("520", "Za 14"), ("1914", "Céleste"),
     ("Millénium", "Un nom"), ("Fin", "Tout en tous")],
 src=[("Zacharie 14 — Bible d'étude, notes (Roi, Huttes, sainteté)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/14"),
      ("Psaume 96 — Bible d'étude, notes (est devenu roi)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/96"),
      ("Révélation 19 — Bible d'étude, notes (Alléluia, règne)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/19"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_G009_roi.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H001", titre="Le cadre des Oliviers — deux questions, Noé, personne ne sait",
 ref="Matthieu 24:1-3, 32-47 ; Marc 13:1-4 ; Luc 21:5-7, 20-24 ; 1 Thessaloniciens 5:2",
 statut="Accomplie (70) + en cours (« plus grand »)",
 cat="H", syst="Système 33/70/1914",
 reg="Registre : Matthieu — P679 (24:2), P647-P654 (24:4-8), P666 (24:32-34), P667 (24:36), P668 (24:37-39), P673 (24:45-47) ; Luc — P681 (21:20-21), P684 (21:22-24) ; Marc — P981 (13:1-2) ; 24:42 sans entrée (C8)",
 texte=[
  "« Il ne restera pas une pierre sur une pierre. » (Mt 24:2 — voir B008)",
  "« Dis-nous : QUAND cela arrivera-t-il, et QUEL sera le SIGNE de ta PRÉSENCE "
  "et de la FIN ? » (24:3 — DEUX questions : pote ? + ti to sèmeion ?)",
  "« Apprenez du figuier : branches tendres, feuilles — l'été est proche ; ainsi, "
  "quand vous verrez TOUTES ces choses… CETTE génération ne disparaîtra pas. » "
  "(24:32-34)",
  "« Ce jour-là et cette heure-là, PERSONNE ne les connaît — ni les anges, ni le "
  "FILS. » (24:36 + Mc 13:32 — Jésus s'exclut : anti-date absolu)",
  "« Comme aux jours de Noé : mangeaient, buvaient, mariaient — et ne se rendirent "
  "compte de RIEN. » (24:37-39 — vie NORMALE, soudaineté)",
  "« VEILLEZ, car vous ne savez pas QUEL JOUR. » (24:42 — grègoreite !)",
  "« Comme un VOLEUR » (24:43-44 ; 1Th 5:2 — soudaineté)",
  "« L'esclave FIDÈLE : nourriture au BON MOMENT — établi sur TOUS ses biens. » "
  "(24:45-47)",
 ],
 contexte=(
  "MARDI 11 Nisan 33 (trois jours avant — dernière semaine, voir D) : Temple admiré "
  "(« vois ces pierres », Mc 13:1 — Hérode, voir F015 !), sentence (24:2), puis les "
  "Oliviers — « assis… EN PRIVÉ » (24:3 : Pierre, Jacques, Jean, André — Mc 13:3 : "
  "QUATRE !). Deux questions : (a) QUAND le Temple ? (b) SIGNE de la PRÉSENCE "
  "(parousia : PRÉSENCE invisible, pas « retour » !) + FIN (synteleia : ACHÈVEMENT !) ? "
  "Jésus répond aux DEUX, entrelacées : 70 (Luc 21:20-24 : ENCERCLÉE, « fuyez » — "
  "voir B007 !) ET le « plus grand accomplissement » (fin MONDIALE : H002-H005, "
  "vague 10)."
 ),
 explication=(
  "« Pas une pierre » (lithos epi lithon — voir B008 : Titus !). Deux questions : "
  "QUAND (pote — Temple) + SIGNE (sèmeion — présence + fin) — « ta PRÉSENCE » "
  "(parousia : présence invisible — signe, pas spectacle !) + « FIN » (synteleia : "
  "achèvement !). Figuier (24:32 : « branches tendres » — parabole de SAISON — PAS "
  "Israël : contre les interprétations populaires, signalée, voir Limites). « CETTE "
  "génération » (hè genea hautè, 24:34) : 1992 — « cette génération ÂGÉE » (état DATÉ, "
  "cité !) — ACTUEL : renvoyé aux publications récentes (méthode E007 : « l'explication "
  "précisée au fil du temps — signalé, pas caché », voir Limites). « Ciel et terre "
  "passeront » (24:35 : symboliques — Ré 21:1, voir G005 — « mes paroles : JAMAIS »). "
  "« PERSONNE » (24:36 : oude… — NI anges NI FILS (Mc 13:32) : Jésus S'EXCLUT — "
  "anti-date ABSOLU !). Noé (24:37-39 : « mangeaient, buvaient, mariaient » — VIE "
  "NORMALE — « ne se rendirent compte » — 120 ans (Gn 6:3) + « prédicateur de "
  "justice » (2P 2:5) : avertis ET surpris !). « VEILLEZ » (grègoreite, 24:42 — C8 — "
  "« vous ne savez pas QUEL JOUR »). « Voleur » (24:43-44 : 1Th 5:2, P754 — soudaineté !). "
  "Esclave FIDÈLE (24:45-47 : « nourriture au BON MOMENT » — « TOUS ses biens » — "
  "identification 2013 renvoyée aux publications récentes, voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : DOUBLE accomplissement — 70 (Luc "
  "21:20-24 : encerclée, fuite aux montagnes — Pella, voir B007 ! — « cette "
  "génération » du Ier siècle : 33→70 = 37 ans !) + « plus grand » (1914+ : "
  "H002-H005). Parousia INVISIBLE : le signe, pas le spectacle. « Cette génération » : "
  "état 1992 cité comme DATÉ, actuel renvoyé (E007-style). « Personne ne sait » : "
  "Mc 13:32 (le FILS !) — aucune date, jamais. Noé : normalité + soudaineté — le "
  "modèle. Esclave : nourriture + 2013 renvoyé."
 ),
 accomplissement=[
  ("11 Nisan 33 (mardi)", "Le discours : Temple, Oliviers, quatre disciples"),
  ("66-70 de n. è.", "Encerclée, fuite (Pella), Temple (voir B007-B008) — 37 ans"),
  ("1914 + de n. è.", "« Plus grand » : le signe (H002-H005, voir B009)"),
  ("1992 de n. è.", "« Génération âgée » : état DATÉ, cité"),
  ("Fin (à venir)", "« Nul ne sait » (24:36) — sans date, jamais"),
 ],
 hist=(
  "11 Nisan 33 (mardi — voir D). Temple d'Hérode (voir F015 : « pierres »). 66 "
  "(Cestius se retire — la fenêtre ! voir B007) → 70 (Titus — voir B007-B008). "
  "Pella (fuite aux montagnes — voir B007). 1914 (voir B009). 1992 (w92 : « L'année "
  "qui a bouleversé », « génération âgée » — DATÉ). 2013 (esclave : précision — "
  "renvoyée)."
 ),
 geo=(
  "Temple → OLIVIERS (24:3 : face au Temple — le lieu de VUE). « En privé » "
  "(quatre : Mc 13:3). Jérusalem ENCERCLÉE (Lc 21:20 : « armées » — 66 + 70). "
  "« Fuyez aux MONTAGNES » (Lc 21:21 — Pella, voir B007)."
 ),
 sci=(
  "33→70 = 37 ans : UNE génération (Ier siècle). Parousia : linguistique — PRÉSENCE "
  "(pas « retour »). Synteleia : ACHÈVEMENT (pas « fin »). « Voleur » (1Th 5:2) : "
  "soudaineté — pas de date."
 ),
 limites=(
  "« Génération » : 1992 cité comme daté, actuel renvoyé aux publications récentes "
  "(méthode E007). Esclave (2013) : renvoyé. Figuier : PAS Israël — parabole "
  "saisonnière, signalée. Matthieu 24:42 sans entrée (C8) ; 24:3 : contexte (pas "
  "d'entrée isolée). Matthieu 24:21-22 : détail à la vague 10."
 ),
 tl=[("11 Nisan 33", "Discours : Oliviers"), ("66-70", "Encerclée, Temple (37 ans)"), ("1914 +", "« Plus grand »"),
     ("1992", "« Âgée » (daté)"), ("Fin", "« Nul ne sait »")],
 src=[("1914 : l'année qui a bouleversé le monde (affres, génération, 1992)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1992320"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Luc 21 — Bible d'étude, notes (encerclée, temps des nations)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/21"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H001_oliviers.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H002", titre="Nation contre nation — 1914, le roux, les douleurs",
 ref="Matthieu 24:6-8 ; Marc 13:7-8 ; Luc 21:9-10, 25-26 ; Révélation 6:3-4 ; Matthieu 24:22",
 statut="En cours (depuis 1914 ; « écourtés » : à venir)",
 cat="H", syst="Dates neutres (1914-1945) · 1914 (B009)",
 reg="Registre : Matthieu — P648 (24:6-7), P650 (24:7), P651 (24:7), P654 (24:8) ; Marc — P649 (13:8) ; Révélation — P821 (6:3-4) ; Luc — P663 (21:25-26)",
 texte=[
  "« Vous entendrez parler de GUERRES et de BRUITS de guerres : il FAUT que cela "
  "arrive — mais pas encore la FIN. » (Mt 24:6 — akoai : RUMEURS ! dei : il FAUT !)",
  "« Nation se dressera contre NATION, royaume contre ROYAUME. » (24:7 — ethnos + "
  "basileia : peuples ET empires !)",
  "« Tout cela : COMMENCEMENT des douleurs. » (24:8 — ôdin : ENFANTEMENT !)",
  "« Un cheval ROUX : ÔTER LA PAIX de la terre — qu'ils S'ÉGORGENT ; une GRANDE "
  "épée. » (Ré 6:4 — pyrros : FEU !)",
  "« Angoisse des nations, au bruit de la mer ; les hommes RENDANT L'ÂME de "
  "terreur. » (Lc 21:25-26 — apopsychô : MOURIR de peur !)",
  "« Si ces jours n'étaient ÉCOURTÉS, NULLE chair ne serait sauvée. » (24:22 — "
  "koloboo : AMPUTÉS !)",
 ],
 contexte=(
  "« Douleurs » (ôdin : ENFANTEMENT — gravité + fréquence + durée CROISSANTES : le "
  "modèle prédictif !). 1914 : la Grande Guerre (voir B009) — « guerre TOTALE… "
  "comme jamais » — DÉBUT des douleurs. « Monde de BARBARIE » (Elmer Davis, Two "
  "Minutes Till Midnight : méthodes « abandonnées… jusqu'en août 1914 » — 1914 = "
  "tournant !). DEUX guerres mondiales : « Grande » → « première MONDIALE » — les "
  "TITRES prouvent la nouveauté. « Pas UNE guerre : GRANDE ÉCHELLE + UNE GÉNÉRATION » "
  "— le signe, c'est l'ÉCHELLE."
 ),
 explication=(
  "« BRUITS » (akoai : rumeurs, menaces — pas que des guerres : des MENACES !). "
  "« Il FAUT » (dei : NÉCESSITÉ — comme Jn 3:14, voir D012 !). « Pas encore » "
  "(oupo : les guerres ≠ la fin — COMMENCEMENT !). Ethnos (NATIONS : peuples !) + "
  "basileia (ROYAUMES : empires !) — 1914 : les DEUX (peuples en guerre, 4 empires "
  "morts : allemand, austro-hongrois, russe, ottoman !). Roux (pyrros : FEU !). "
  "« ÔTER LA PAIX » (tèn eirènèn : LA paix — ARTICLE : la paix GÉNÉRALE !). "
  "« S'égorger » (sphaxousin : ÉGORGER — fratricide !). « GRANDE épée » (machaira "
  "megalè : pas un couteau !). Ôdin (enfantement : rapprochées + intensifiées — "
  "modèle !). Angoisse (synochè : PRESSION, Lc 21:25 !). « Mer et flots » (peuples : "
  "Is 17:12, voir E002 !). Apopsychô (MOURIR de peur, 21:26 !). « Écourtés » "
  "(koloboo : AMPUTÉS — « NULLE chair » (sarx : AUCUNE — extinction POSSIBLE : "
  "moyen NON précisé, voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1914 — DÉBUT des douleurs (« guerre "
  "TOTALE, comme jamais »). Les TITRES (« Grande », « mondiale ») prouvent la "
  "nouveauté dans les annales. « Monde de barbarie » (Davis : août 1914 = rupture "
  "de civilisation). Paix ÔTÉE (Ré 6:4 = Mt 24:7 : les deux ensemble !). « Bonne "
  "nouvelle » : les douleurs = Royaume PROCHE — « paix PERMANENTE » à venir. "
  "« Écourtés » (24:22) : Dieu AMPUTE — la chair SAUVÉE."
 ),
 accomplissement=[
  ("1914-1918", "Grande Guerre (~10 M) : DÉBUT des douleurs"),
  ("1939-1945", "Seconde (~50-60 M) : les douleurs continuent"),
  ("1945 +", "« Bruits » : guerre froide (voir E007 : OTAN)"),
  ("1947 +", "Horloge : « minutes avant minuit » (Bulletin — neutre)"),
  ("« Écourtés » (à venir)", "24:22 : Dieu ampute — sans date"),
 ],
 hist=(
  "Sarajevo (28 juin 1914 — août : engrenage !). ~10 M (WWI), ~50-60 M (WWII) : "
  "ORDRES — débattus (voir Limites). « TOTALE » : civils ciblés, blocus — nouveauté "
  "(civils : ~10 % → ~50 % + : ordres). Quatre empires morts (1914-1922 : allemand, "
  "austro-hongrois, russe, ottoman). Davis (Two Minutes Till Midnight : « barbarie »). "
  "Horloge (Bulletin, 1947 : « minuit » = catastrophe — neutre)."
 ),
 geo=(
  "« Nation contre nation » : MONDIALE — pas locale (1914 : Europe → monde). "
  "« Royaume contre royaume » : EMPIRES — quatre morts. « Mer » (Lc 21:25 : peuples). "
  "OTAN (voir E007 : le Sud)."
 ),
 sci=(
  "~10 M / ~50-60 M : ordres DÉBATTUS (voir Limites). « TOTALE » : part civile "
  "croissante (ordres). « Nulle chair » : extinction POSSIBLE (nucléaire : moyen "
  "NON précisé — dit). Ôdin : modèle prédictif (rapprochement + intensification)."
 ),
 limites=(
  "Morts : ordres de grandeur DÉBATTUS (historiens partagés). « Nulle chair » : "
  "moyen non précisé — dit. Matthieu 24:21 : détail à la vague 10. Seconde guerre : "
  "pas un « signe » séparé — les « bruits » continuent."
 ),
 tl=[("1914", "DÉBUT : douleurs"), ("1914-18", "~10 M"), ("1939-45", "~50-60 M"), ("1945 +", "Bruits : froide"),
     ("1947 +", "Horloge"), ("Avenir", "« Écourtés »")],
 src=[("Le temps de la fin (douleurs 1914, échelle, tableau 6 signes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1954881"),
      ("La folie de la guerre (Davis, barbarie, paix permanente)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1957760"),
      ("Révélation 6 — Bible d'étude, notes (roux, paix ôtée)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/6"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24")],
 img="images/prophe_H002_guerres.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H003", titre="Famines, pestes, séismes — Luc seul, deux courbes",
 ref="Matthieu 24:7 ; Luc 21:11 ; Révélation 6:5-8 ; Actes 24:5 ; Ézéchiel 14:21",
 statut="En cours (depuis 1914 ; « signes du ciel » : renvoi)",
 cat="H", syst="Dates neutres (1918-2010) · signe (1914+)",
 reg="Registre : Matthieu — P650 (24:7), P651 (24:7) ; Luc — P652 (21:11), P653 (21:11) ; Révélation — P822 (6:5-6), P823 (6:7-8)",
 texte=[
  "« Il y aura des famines et des tremblements de terre PAR ENDROITS. » "
  "(Mt 24:7 — kata topous : distribution !)",
  "« GRANDS tremblements de terre et, par endroits, famines et ÉPIDÉMIES ; choses "
  "EFFRAYANTES et GRANDS signes du ciel. » (Lc 21:11 — megas ! LUC SEUL pour pestes !)",
  "« Cheval NOIR, balance : un denier = UNE RATION de blé ; huile et vin : PAS "
  "TOUCHE. » (Ré 6:5-6 — journée = ration ; luxe intact : INÉGALITÉS !)",
  "« Cheval PÂLE-verdâtre : LA MORT, et l'hadès SUIT — pouvoir sur le QUART. » "
  "(Ré 6:8 — chloros ! tetarton !)",
  "« Par CET homme qui est une PLAIE. » (Ac 24:5 — loimos : Paul ! AUTRE occurrence !)",
 ],
 contexte=(
  "« PAR ENDROITS » (kata topous : pas partout — PARTOUT par endroits !). LUC SEUL "
  "mentionne les « pestes » (Mt/Mc : non — « les trois récits se COMPLÈTENT » : "
  "méthode !). « GRANDS » (megas, Lc 21:11 : séismes ET signes !). « Choses "
  "EFFRAYANTES » (phobêtron : HAPAX du Nouveau Testament — « ne figure qu'ICI » — "
  "phobeô : PEUR !). « Signes du ciel » (Lc 21:11 : renvoyé H suite/I, voir Limites). "
  "Tableau 1955 : disette, séismes « extraordinaires », épidémies (état daté — "
  "voir Limites pour la précision moderne)."
 ),
 explication=(
  "Limoi (famines : PLURIEL !). Seismos (séismes : notre « SISMIQUE » !). Megas "
  "(GRANDS : Lc 21:11 !). Loimos (« PESTES » litt. — « épidémies » : LUC SEUL — "
  "Mt/Mc sans : COMPLÉMENTARITÉ !). Ac 24:5 (SEULE autre occurrence : Paul = "
  "« plaie » — « agitateur » !). Phobêtron (HAPAX : sens par contexte — « terrifiants » "
  "!). « Signes du ciel » (ouranos : renvoyé). Noir (melas : balance — RATIONNEMENT !). "
  "« Denier = chénice » (journée, Mt 20:2 = RATION : survie ! « 3 chénices d'orge » : "
  "pauvres — orge !). « Huile et vin » (6:6 : LUXE intact — INÉGALITÉS !). Chloros "
  "(VERDÂTRE : chlorophylle — pâleur CADAVÉRIQUE !). « LA Mort » (thanatos "
  "PERSONNIFIÉE + hadès SUIT !). « QUART » (tetarton : 1/4 !). « Glaive + famine + "
  "mort + bêtes » (4 fléaux : Éz 14:21, « mes 4 châtiments » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : GRANDE ÉCHELLE — pas UN séisme : le "
  "TABLEAU (guerres + disette + séismes + épidémies + persécution + apostasie — "
  "voir le tableau 1955). Grippe 1918-1920 (20-50 M : « plus que la guerre » !). "
  "Famines XXe (Ukraine 1932-33, Chine 1959-61 : « dizaines de millions » — ORDRES, "
  "voir Limites). Séismes : HONNÊTETÉ — magnitude STABLE (catalogues USGS : ~15 M7+/an) "
  "contre VICTIMES croissantes (urbanisation) — DEUX courbes DISTINGUÉES : Tangshan "
  "1976 (~240 000), tsunami 2004 (~230 000), Haïti 2010 (100-200 000) — ordres. "
  "« Extraordinaires » (1955, daté) : précisé par la distinction moderne — signalé."
 ),
 accomplissement=[
  ("1914 +", "Blocus, disette (guerre)"),
  ("1918-1920", "Grippe : 20-50 M (« plus que la guerre »)"),
  ("1932-1933", "Ukraine (Holodomor : millions — ordres)"),
  ("1959-1961", "Chine (Grand Bond : dizaines de M — ordres)"),
  ("1976 / 2004 / 2010", "Tangshan, tsunami, Haïti (victimes : villes !)"),
  ("« Ciel » (renvoi)", "Signes : H suite / I"),
 ],
 hist=(
  "Grippe 1918-1920 (« espagnole » : 20-50 M — fourchette = INCERTITUDE avouée ; "
  "origine débattue — Kansas ? — voir Limites). Ukraine 1932-1933 (Holodomor : "
  "millions — politiques : chiffres débattus). Chine 1959-1961 (Grand Bond : "
  "dizaines de millions — débattus). Tangshan 1976 (nuit : ~240 000). Tsunami 2004 "
  "(9,1 : ~230 000). Haïti 2010 (7,0 : 100-200 000 — pauvreté = vulnérabilité). "
  "USGS (~15 M7+/an : STABLE — détection améliorée)."
 ),
 geo=(
  "« PAR ENDROITS » : distribution MONDIALE. Ukraine/Chine : GRENIERS — famines "
  "PARADOXALES. Ceinture de feu (Pacifique : séismes). Haïti (faille + pauvreté : "
  "victimes = VULNÉRABILITÉ, pas magnitude). « Ciel » (signes — renvoi)."
 ),
 sci=(
  "USGS (~15 M7+/an : stable — DÉTECTION, pas multiplication). Victimes = "
  "URBANISATION (1976/2004/2010 : VILLES !). Grippe 20-50 M : fourchette avouée. "
  "Famines : ordres DÉBATTUS (causes politiques). « Denier = ration » : économie "
  "antique (survie). Chloros : pâleur cadavérique."
 ),
 limites=(
  "Chiffres : ordres DÉBATTUS (famines politiques, grippe : fourchette). Grippe : "
  "origine débattue. Séismes : magnitude contre victimes DISTINGUÉES — pas de "
  "« courbe de séismes » ; « extraordinaires » (1955) précisé, signalé. « Signes "
  "du ciel » : renvoyé (H suite / I). Phobêtron (hapax) : sens par contexte."
 ),
 tl=[("1914 +", "Disette"), ("1918-20", "Grippe : 20-50 M"), ("1932-61", "Famines : ordres"),
     ("1976/04/10", "Séismes : villes"), ("Ciel", "Signes (renvoi)")],
 src=[("Luc 21 — Bible d'étude, notes (Luc seul : pestes, hapax, ciel)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/21"),
      ("Une catastrophe est imminente (signe : guerres, famines, pestes, angoisse)", "https://wol.jw.org/fr/wol/d/r30/lp-f/101987484"),
      ("Révélation 6 — Bible d'étude, notes (noir, pâle, quart)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/6"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H003_famines.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H004", titre="Prêchée à toutes les nations — le seul signe joyeux",
 ref="Matthieu 24:14 ; Marc 13:10 ; Matthieu 28:19-20 ; Actes 1:8 ; Révélation 14:6 ; Matthieu 9:35",
 statut="En cours (« ALORS viendra la fin »)",
 cat="H", syst="Système 33/1914 · chiffres courants (jw.org)",
 reg="Registre : Matthieu — P660 (24:14) ; Révélation — P880 (14:6-7) ; Actes — P700 (1:8) ; Mt 13:39 sans entrée (C8)",
 texte=[
  "« Cette bonne nouvelle du Royaume sera prêchée sur toute la TERRE HABITÉE, "
  "en TÉMOIGNAGE pour TOUTES les nations — et ALORS viendra la fin. » "
  "(Mt 24:14 — oikouménè ! martyrion ! tote !)",
  "« Il FAUT D'ABORD que la bonne nouvelle soit prêchée. » (Mc 13:10 — proton : "
  "AVANT !)",
  "« FAITES des disciples de TOUTES les nations… jusqu'à la fin. » (Mt 28:19-20 — "
  "mathèteusate : ENSEIGNEZ !)",
  "« Jusqu'à l'EXTRÉMITÉ de la terre. » (Ac 1:8 — eschatou tès gès : le BOUT !)",
  "« Un ange AU MILIEU DU CIEL : évangile ÉTERNEL à TOUTE nation, tribu, langue, "
  "peuple. » (Ré 14:6 — aionios ! 4 termes !)",
 ],
 contexte=(
  "« Caractéristique POSITIVE » : le SEUL signe JOYEUX — après guerres et disette "
  "(« malgré perspectives SOMBRES » : étonnement des disciples !). « Époque de la "
  "MOISSON » (Mt 13:39 : « la moisson = FIN » — moissonneurs = ANGES — C8, voir "
  "Limites). Ange VOLANT (Ré 14:6 : « au milieu du ciel » — VISIBLE partout !). "
  "1990 : 212 pays et îles (état daté, cité !) → AUJOURD'HUI : 240 pays/territoires "
  "(rapport annuel — voir Limites : année précisée, chiffres courants)."
 ),
 explication=(
  "Oikouménè (« terre HABITÉE » — pas gê : monde habité — PARTOUT où vivent !). "
  "Martyrion (TÉMOIGNAGE — PAS conversion : TÉMOIGNER, pas convertir !). « TOUTES "
  "les nations » (pasa ta ethnè : sans exception !). « ALORS » (tote : la prédication "
  "PRÉCÈDE — CONDITION !). « D'ABORD » (proton, Mc 13:10 : AVANT la fin !). "
  "« FAITES des disciples » (mathèteusate : ENSEIGNEZ — pas « convertissez » !). "
  "« Extrémité » (Ac 1:8 : Jérusalem → Judée → Samarie → BOUT : 4 cercles !). "
  "« ÉTERNEL » (aionios, Ré 14:6 : pas temporaire !). Quatre termes (nation/tribu/langue/"
  "peuple : TOTALITÉ — comme Ré 7:9, voir G007 !). « Moisson » (therismos, Mt 13:39 : "
  "« = FIN » — C8 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : 1914 — naissance du Royaume = BONNE "
  "nouvelle (contre la mauvaise : la guerre !). « Chacun peut VOIR » : VÉRIFIABLE — "
  "pas invisible : sortez et regardez ! 212 pays (1990, daté) → 240 AUJOURD'HUI "
  "(rapport annuel). 1 000+ langues (jw.org : « le plus traduit » — RECORD !). "
  "8 M+ proclamateurs (rapport annuel). « Positive » : JOIE dans le signe. Moisson : "
  "époque — anges + humains."
 ),
 accomplissement=[
  ("33 de n. è.", "Jérusalem (Ac 2 : 3 000)"),
  ("36 + de n. è.", "Nations (voir C012)"),
  ("Ier s.", "« Toute la création » (Col 1:23 — monde romain ? voir Limites)"),
  ("1914 + de n. è.", "« Plus grand » : mondiale"),
  ("1990 de n. è.", "212 pays et îles (daté, cité)"),
  ("Aujourd'hui", "240 pays/territoires, 8 M+, 1 000+ langues (courants)"),
  ("« ALORS » (à venir)", "La fin — après : pas de date"),
 ],
 hist=(
  "1990 (212 pays et îles — cité !). AUJOURD'HUI (240 : rapport annuel — année "
  "précisée, voir jw.org, voir Limites). jw.org (1 000+ langues : RECORD mondial — "
  "vérifiable). 8 M+ (rapport ANNUEL : audité). Col 1:23 (« toute création » : Ier "
  "siècle — monde ROMAIN ? — signalé). « Étonnement » (disciples : guerre ET "
  "prédication ?!)."
 ),
 geo=(
  "« Oikouménè » : HABITÉE — pas déserts : PARTOUT où vivent. « Extrémité » "
  "(Ac 1:8 : 4 cercles — Jérusalem → BOUT). 240 pays (îles INCLUSES — 1990 : « pays "
  "et îles »). 1 000+ langues : traduction TOTALE."
 ),
 sci=(
  "212 → 240 : CROISSANCE mesurable. 1 000+ langues : RECORD — vérifiable. 8 M+ : "
  "rapport annuel — audité. « Chacun peut voir » : FALSIFIABLE — sortez, regardez. "
  "Oikouménè : géographie antique (monde HABITÉ)."
 ),
 limites=(
  "Chiffres COURANTS : rapport annuel — année précisée, voir jw.org (pas figés "
  "ici). Col 1:23 (« toute création » : monde romain ? — signalé). Matthieu 13:39 "
  "sans entrée (C8). « Fin » (24:14 : APRÈS — pas de date)."
 ),
 tl=[("33", "Jérusalem"), ("36 +", "Nations"), ("Ier s.", "Col 1:23"), ("1914 +", "Mondiale"),
     ("1990", "212 (daté)"), ("Aujourd'hui", "240 !"), ("« ALORS »", "Fin")],
 src=[("Une bonne nouvelle pour tous (Ré 14:6, 212 pays, chacun peut voir)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1990000"),
      ("Matthieu 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/24"),
      ("Révélation 14 — Bible d'étude, notes (ange, évangile éternel)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/14"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H004_predication.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="H005", titre="Les traits des derniers jours — 19 ou 20, et pas la preuve",
 ref="2 Timothée 3:1-5, 13 ; 2 Pierre 3:3 ; Jacques 5:1-6 ; 1 Thessaloniciens 5:3 (renvoi v10)",
 statut="En cours (depuis 1914 : « principale »)",
 cat="H", syst="Système 65/1914",
 reg="Registre : 2 Timothée — P761 (3:1-5), P762 (3:12-13) ; Jacques — P773 (5:1-6), P774 (5:7-8), P775 (5:9) ; 1 Thessaloniciens — P754 (5:1-3)",
 texte=[
  "« SACHE : dans les derniers jours, des temps CRITIQUES, difficiles à supporter. » "
  "(2Tm 3:1 — ginôsko : IMPÉRATIF ! chalepoi : DANGEREUX — Mt 8:28 !)",
  "« Amants D'EUX-MÊMES, amants de l'ARGENT… amants des PLAISIRS PLUTÔT qu'amants "
  "de Dieu. » (3:2-4 — trois PHIL- : soi, argent, plaisirs !)",
  "« Ayant une FORME de piété mais en ayant RENIÉ la force — DÉTOURNE-TOI. » "
  "(3:5 — morphôsis : forme SANS force ! apotrephô : CONSIGNE !)",
  "« Les méchants et imposteurs progresseront vers le PIRE, égarant ET égarés. » "
  "(3:13 — progrès INVERSÉ !)",
  "« L'or rouillé » (Jc 5:3 — katioo : OXYMORE — l'or ne rouille pas !)",
  "« Quand ils diront : PAIX ET SÉCURITÉ — SOUDAINE destruction. » (1Th 5:3 — "
  "détail : vague 10 !)",
 ],
 contexte=(
  "Paul à Timothée (~65 : DERNIÈRE lettre — prison — « SACHE » !). « Derniers jours » "
  "(eschatos : comme Ac 2:17 (Joël — Pentecôte !), Hé 1:2, Jc 5:3, 2P 3:3 — DÈS le "
  "Ier siècle ? — « application PRINCIPALE à notre époque » : double temps !). "
  "« Conclusion » (synteleia — voir H001 !). « PAS la preuve PRINCIPALE » : Paul "
  "PRÉVIENT de ce qu'on ENDURERA — pas une preuve : MÉTHODE (honnêteté citée !). "
  "Presse DATÉE : Financial Times (« dieux » !), Bangkok Post (« amoralité » !), "
  "Boundless (« croisade » !) — TÉMOINS cités."
 ),
 explication=(
  "« SACHE » (ginôsko : Timothée DOIT savoir !). « Eschatos » (DERNIERS — Ac 2:17 ! "
  "Hé 1:2 !). « Chalepoi » (CRITIQUES — Mt 8:28 : démoniaques « DANGEREUX » — MÊME "
  "MOT !). « Difficiles à supporter » (dys- : DUR !). 19 OU 20 ? (1994 : 19 ! 2006 : "
  "20 ! — DÉCOUPAGE : « sans affection / sans esprit d'entente » : un ou deux ? — "
  "le compte VARIE : signalé, voir Limites). Liste : philautoi (1er : SOI !), "
  "philargyroi (ARGENT !), orgueilleux… philèdonoi (PLAISIRS !) — trois PHIL- "
  "encadrent ! « PLUTÔT qu'amants de Dieu » (3:4 : CONTRASTE !). « Ingrats » "
  "(acharistoi : Lc 17:17 — 9 lépreux !). « Sans affection » (astorgoi : Rm 1:31 !). "
  "« Calomniateurs » (diaboloi : « diables » !). « Traîtres » (prodotai : Judas, Lc "
  "6:16 !). « Gonflés » (tetyphômenoi : 1Tm 3:6, 6:4 !). « FORME » (morphôsis : Rm "
  "2:20 — forme SANS force !). « RENIÉ » (èrnèmenoi : PARFAIT — reniement ACCOMPLI !). "
  "« DÉTOURNE-TOI » (apotrephô : pas débat — ÉVITE !). « Vers le PIRE » (3:13 : "
  "prokoptousin epi to cheiron — « progresseront » vers le PIRE : progrès INVERSÉ !). "
  "« Égarant ET égarés » (planôntes kai planômenoi : actifs + passifs !). « Or ROUILLÉ » "
  "(Jc 5:3 : katioo — OXYMORE : l'or ne rouille pas — richesses POURRIES !). « Cris "
  "des moissonneurs » (Jc 5:4 : « aux OREILLES » — Sabaoth !). « Paix et sécurité » "
  "(1Th 5:3, P754 : « SOUDAINE » — « comme DOULEURS » (ôdin — voir H002 !) — "
  "« n'échapperont PAS » — DÉTAIL : vague 10 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : « PROFIL de la génération » (les traits "
  "caractérisent). Presse : FT (« insistent… deviennent des DIEUX » !), Bangkok "
  "(« amoralité » !), Boundless (« croisade » !) — témoins, pas preuves. « PAS la "
  "preuve principale » : PRÉVENIR d'endurer (pendant les derniers jours) — fruits "
  "MAUVAIS du monde autour (Mt 7:17 !). « Conclusion » : derniers jours = fin du "
  "système. « Vers le pire » (3:13) : en cours."
 ),
 accomplissement=[
  ("~65 de n. è.", "Lettre : « SACHE » (prison, dernière)"),
  ("Ier s.", "Début : « derniers jours » (Ac 2:17 !)"),
  ("1914 + de n. è.", "« Principale » : conclusion"),
  ("Presse (datée)", "FT, Bangkok, Boundless : TÉMOINS"),
  ("« PIRE » (en cours)", "3:13 : égarant et égarés"),
  ("« Paix et sécurité » (à venir)", "1Th 5:3 : vague 10"),
 ],
 hist=(
  "~65 (Paul prisonnier — dernière lettre). FT (« dieux » — Angleterre). Bangkok "
  "Post (« amoralité » — Thaïlande). Boundless (« croisade » — internet). Trois "
  "continents. Jacques 5 (riches : « or rouillé »). 2P 3:3 (moqueurs — voir G005)."
 ),
 geo=(
  "PARTOUT : traits UNIVERSELS — pas un pays. « Monde autour » (des chrétiens — "
  "partout). Presse : trois continents (Angleterre, Thaïlande, internet)."
 ),
 sci=(
  "19/20 : DÉCOUPAGE — le compte varie : signalé. Trois PHIL- : structure (soi / "
  "argent / plaisirs). Morphôsis : forme contre force — DISTINCTION. « PAS preuve » : "
  "méthode — PRÉVENIR (honnêteté citée). Indicateurs : ILLUSTRÉS — pas de courbe "
  "GLOBALE (voir Limites)."
 ),
 limites=(
  "19 ou 20 : selon le découpage — signalé. Pas de courbe de « décadence » globale : "
  "traits illustrés, indicateurs cités — pas de sociologie TOTALE. « Paix et "
  "sécurité » : détail à la vague 10. Presse : datée — TÉMOINS cités, pas preuves. "
  "Mt 8:28 (même mot chalepoi) : cross-ref."
 ),
 tl=[("65", "Lettre : SACHE"), ("Ier s.", "Début : Ac 2"), ("1914 +", "Principale !"),
     ("Presse", "Témoins (3 continents)"), ("En cours", "« PIRE »"), ("À venir", "« Paix » (v10)")],
 src=[("Vivons-nous les derniers jours ? (20 traits, presse, 2006)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2006681"),
      ("Un enseignement pour notre époque (19 traits, pas preuve, 1994)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1994283"),
      ("2 Timothée 3 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/55/3"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_H005_traits.jpg",
))
