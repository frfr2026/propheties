#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE J-K (vague de transition 13) — FIN DES NOMMES + LA BIBLE ET LA SCIENCE
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="J–K",
    nom="Fin des nommés d'avance · La Bible et la science (1re partie)",
    vague="13",
    intro=(
        "Cette vague de transition ferme la catégorie J et ouvre la catégorie K. "
        "Côté J, un dernier nommé restait : Gog du pays de Magog, la coalition "
        "qui attaquera le peuple de Dieu — Compréhension actualisée (2015), textes "
        "d'Ézéchiel 38 et 39, séquence sans date. Côté K, six premières fiches "
        "« Bible et science » : la postérité innombrable comme les étoiles et le "
        "sable, l'alliance du jour et de la nuit garantie par les lois du ciel, le "
        "dessein durable pour la terre, le Psaume 8 (lune, étoiles, sentiers des "
        "mers), Élie et Aggée maîtres de la pluie sous parole, et le cadran d'Achaz "
        "où l'ombre recule. Mêmes dix blocs, mêmes règles : un seul système "
        "chronologique par fiche, aucune date pour l'avenir, et des limites écrites "
        "noir sur blanc."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J012", titre="Gog de Magog — la coalition contre le vrai culte",
 ref="Ézéchiel 38:1-23 ; Ézéchiel 39:1-20 ; Révélation 20:7-10 (F017) ; Genèse 10:2 (C8)",
 statut="À venir (P360, P361)",
 cat="J", syst="Système séquence (Babylone → Gog → Royaume)",
 reg="Registre : Ézéchiel — P360 (38:1-23 : Gog attaque, jugement), P361 (39:1-20 : Gog tombe, oiseaux convoqués)",
 texte=[
  "« Fils d'homme, tourne ta face contre GOG du pays de MAGOG, chef suprême de MÉSHEK et TOUBAL. » "
  "(38:2 — le nommé !)",
  "« La Perse, l'Éthiopie et POUT avec eux… GOMER… TOGARMA, des parties reculées du NORD. » "
  "(38:5-6 — la coalition !)",
  "« Je mettrai des CROCS dans tes mâchoires, je te ferai sortir avec toute ton armée. » (38:4 — les crocs !)",
  "« Tu monteras contre mon peuple… comme une NUÉE pour couvrir le pays… dans les DERNIERS JOURS. » "
  "(38:9, 16 — la nuée !)",
  "« Mon pays » : un peuple RASSEMBLÉ des nations, habitant en SÉCURITÉ, avec du bétail et des biens. "
  "(38:8, 11-12 — la cible !)",
  "« Je le jugerai par la PESTE et le SANG… pluie torrentielle, GRÊLE, FEU et SOUFRE. » (38:22 — le jugement !)",
  "« Sur les MONTAGNES d'Israël tu tomberas… je te donnerai en pâture aux OISEAUX. » (39:4 — le festin !)",
  "« SEPT ANS, ils brûleront les armes… SEPT MOIS, on enterrera… la vallée de HAMON-GOG. » (39:9, 11-12)",
 ],
 contexte=(
  "Ézéchiel prophétise parmi les exilés de Babylone. Les chapitres 38 et 39 forment un "
  "diptyque : l'attaque (38) puis la chute (39). Le décor est planté avec soin : un "
  "peuple rassemblé des nations où il était dispersé, rétabli sur les « montagnes "
  "d'Israël » auparavant dévastées, vivant en sécurité, sans murailles (38:8, 11). "
  "C'est cette prospérité sans défense qui excite la convoitise : « Je monterai… pour "
  "piller et faire du butin » (38:11-12 — C8). Magog figure déjà dans la Table des "
  "nations comme fils de Japhet (Gn 10:2 — C8) ; Méshek et Toubal sont des peuples du "
  "nord connus des annales assyriennes (Moushki, Tabal — voir l'historique)."
 ),
 explication=(
  "Le point capital est l'identité de Gog, précisée en 2015 : Gog de Magog désigne non "
  "une créature spirituelle invisible, mais un ennemi humain visible — une coalition de "
  "nations qui combattra le vrai culte (voir 2015364, 1102017177). Deux indices du texte "
  "l'excluent du monde des esprits : Gog reçoit une sépulture — la vallée de Hamon-Gog "
  "(39:11) — et son armée sert de pâture aux oiseaux et aux bêtes (39:4, 17-20) : "
  "traitement d'une armée humaine. « Je mettrai des crocs dans tes mâchoires » (38:4) et "
  "« je te ferai venir contre mon pays » (38:16) ne signifient pas que Dieu force les "
  "nations à attaquer ses adorateurs — jamais il ne ferait venir le mal sur son peuple : "
  "poussées par Satan, les nations tenteront d'effacer le vrai culte, et Jéhovah "
  "retournera leur attaque en jugement (voir 1102017177 §18). « Mon pays » est le pays "
  "spirituel : le peuple de Dieu, répandu sur toute la terre — d'où la nécessité d'une "
  "coalition mondiale pour l'attaquer (voir 2015364)."
 ),
 interpretation=(
  "La séquence est claire : l'attaque de Gog suit la destruction de Babylone la Grande "
  "par les puissances politiques (voir I007) et s'inscrit dans la grande tribulation — "
  "une coalition de nations, appelée « Gog du pays de Magog », tentera de supprimer "
  "ceux qui pratiquent la vraie religion, mais Dieu les protégera (voir 502016178). "
  "Le jugement reprend tout l'arsenal des plaies : peste, sang, pluie torrentielle, "
  "grêle, feu et soufre (38:22), plus la panique — « l'épée de chacun contre son frère » "
  "(38:21 — C8). Le festin des oiseaux (39:17-20) a son jumeau en Révélation 19:17-18 "
  "(voir I010). Quant à « Gog et Magog » de Révélation 20:7-8, l'expression y est "
  "reprise pour la rébellion post-millénaire — autre événement, même nom (voir F017). "
  "Le refrain des deux chapitres — « ils sauront que je suis Jéhovah » (38:23 ; 39:6-7 — "
  "C8) — dit le but : la sanctification du nom."
 ),
 hist=(
  "Les noms de la coalition appartiennent à la géographie antique réelle : Magog, "
  "Méshek, Toubal, Gomer descendent de Japhet (Gn 10:2-3 — C8) ; les annales assyriennes "
  "connaissent les Moushki (Méshek) et le Tabal (Toubal) en Anatolie orientale ; Togarma "
  "correspond à la région arménienne. Perse, Éthiopie (Coush) et Pout complètent le tour "
  "d'horizon : nord, est, sud. « Parties reculées du nord » (38:15) : la direction "
  "d'où vinrent historiquement les envahisseurs d'Israël (Scythes, Babyloniens par le "
  "nord). Aucune nation moderne n'est nommée par les publications : la fiche ne nomme "
  "personne (voir les limites)."
 ),
 geo=(
  "Le « pays de Magog » au nord, les « montagnes d'Israël » au centre : l'attaque "
  "converge vers le pays du peuple rassemblé. La vallée de Hamon-Gog (« multitude de "
  "Gog », 39:11) — lieu de sépulture de sept mois (39:12-14 — C8) — et la ville de "
  "Hamona (« multitude », 39:16 — C8) marquent le pays du jugement. Les oiseaux sont "
  "convoqués « de partout » (39:17) : le festin est continental. Les armes brûlées sept "
  "ans (39:9-10 — arcs, flèches, lances) dispensent de ramasser du bois : le butin "
  "devient combustible."
 ),
 sci=(
  "Logistique : une armée coalisée « comme une nuée » (38:9) — effectifs innombrables, "
  "chevaux et cavaliers (38:4, 15), panoplie complète (boucliers, casques, épées, 38:4-5). "
  "Police des champs de bataille : sept mois d'inhumation par des équipes dédiées, avec "
  "baliseurs marquant les ossements (39:14-15 — C8) — procédure sanitaire avant la "
  "lettre. Météorologie du jugement : pluie torrentielle et grêle (38:22) — les mêmes "
  "armes qu'à Beth-Horôn (Jos 10:11 — C8) et à Harmaguédon (Ré 16:21 — voir I009). "
  "Écologie du festin : oiseaux et bêtes convoqués (39:17-20) — la chaîne alimentaire "
  "comme fossoyeur."
 ),
 limites=(
  "Aucune nation ou coalition moderne n'est identifiée ici : les publications ne nomment "
  "personne, et cette fiche ne spécule pas — les identifications datées du passé "
  "(voir 1981522, obsolète) ne sont pas reprises. Aucune date : « derniers jours » "
  "(38:16) et grande tribulation situent sans dater. Les chiffres — sept ans de feu "
  "(39:9), sept mois de sépulture (39:12) — sont le texte reçu, sans conversion. "
  "« Gog et Magog » de Révélation 20:8 est un autre événement sous le même nom (voir "
  "F017) : les deux dossiers ne sont pas mélangés."
 ),
 accomplissement=[("Exil", "Diptyque 38-39"), ("Rassemblé", "Peuple en sécurité"), ("Babylone", "Détruite (I007)"),
     ("Coalition", "Gog monte"), ("Jugement", "38:22 : grêle, feu"), ("Hamon-Gog", "7 mois de sépulture") ],
 tl=[("Exil", "Diptyque 38-39"), ("Rassemblé", "Peuple en sécurité"), ("Babylone", "Détruite (I007)"),
     ("Coalition", "Gog monte"), ("Jugement", "38:22 : grêle, feu"), ("Hamon-Gog", "7 mois de sépulture") ], src=[("Qui est Gog de Magog ? (Questions, 2015 — mise au point)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2015364"),
      ("« Je vais agir contre toi, ô Gog » (Culte pur, chap. 17)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102017177"),
      ("Qu'est-ce que la grande tribulation ? (séquence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/502016178"),
      ("Ézéchiel 38 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/38"),
      ("Ézéchiel 39 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/39")],
 img="images/prophe_J012_gog.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K001", titre="Innombrables — les étoiles, le sable, la poussière",
 ref="Genèse 15:4-6 ; Genèse 22:15-18 ; Genèse 26:2-5 ; Genèse 28:13-15",
 statut="Accomplie (P005, P013, P016, P019)",
 cat="K", syst="Système générations (Abraham → Moïse → Salomon → Christ)",
 reg="Registre : Genèse — P005 (15:4-6 : postérité comme les étoiles), P013 (22:15-18 : étoiles et sable, porte des ennemis), P016 (26:2-5 : à Isaac, comme les étoiles), P019 (28:13-15 : à Jacob, comme la poussière)",
 texte=[
  "« Regarde le ciel et COMPTE les étoiles, SI TU PEUX les compter. » (15:5 — le défi !)",
  "« Ainsi sera ta POSTÉRITÉ. » (15:5 — le transfert !)",
  "« Il CRUT en Jéhovah, qui le lui compta pour JUSTICE. » (15:6 — la foi comptée !)",
  "« Comme les ÉTOILES des cieux et comme le SABLE du bord de la mer. » (22:17 — ciel et mer !)",
  "« Ta postérité possédera la PORTE de ses ennemis. » (22:17 — la porte !)",
  "« Je multiplierai ta postérité comme les ÉTOILES » — à Isaac (26:4 — confirmé !)",
  "« Ta postérité sera comme la POUSSIÈRE de la terre » — à Jacob (28:14 — la terre !)",
 ],
 contexte=(
  "Quatre scènes, trois patriarches, une même promesse. Abram, sans enfant, s'inquiète "
  "pour son héritier (15:2-3 — C8) : Dieu le fait sortir sous les étoiles (15:5). Au "
  "Morija, après l'épreuve, le serment solennel avec les deux comparaisons (22:15-18). "
  "À Isaac, en famine, l'ordre de ne pas descendre en Égypte et la confirmation (26:2-5). "
  "À Jacob, en fuite à Béthel, l'échelle puis la poussière (28:12-14 — C8). Trois "
  "comparaisons — étoiles (le ciel), sable (la mer), poussière (la terre) : le cosmos "
  "entier recruté pour dire l'innombrable."
 ),
 explication=(
  "« Si tu peux » : le défi est loyal — à l'œil nu, on ne voit que quelques milliers "
  "d'étoiles, et pourtant la comparaison vise juste (voir le bloc science). Les trois "
  "images escaladent : les étoiles (multitude glorieuse), le sable (multitude foulée "
  "mais indestructible), la poussière (multitude répandue aux quatre vents — 28:14 dit "
  "l'expansion ouest, est, nord, sud). « Ainsi sera » (15:5) : la postérité égale le "
  "modèle. Et 15:6 pose le principe que Paul exploitera : la foi « comptée pour "
  "justice » (Rm 4:3 — C8 ; Ga 3:6 — C8). « La porte de ses ennemis » (22:17) ajoute la "
  "victoire au nombre : posséder la porte, c'est tenir la ville."
 ),
 interpretation=(
  "La postérité a trois étages. La nation : « les fils d'Israël pullulèrent… devinrent "
  "extrêmement forts » (Ex 1:7 — P005), et Moïse constate : « vous êtes aujourd'hui "
  "aussi nombreux que les étoiles » (Dt 1:10 — P005). Le Roi : Salomon règne sur un "
  "peuple « aussi nombreux que le sable » (1R 4:20 — P013), et « pas une parole n'est "
  "restée sans effet » (Jos 21:43-45 — P013). Le Christ : « à ta postérité » — « c'est-à-dire "
  "à Christ » (Ga 3:16 — P013) ; « si vous êtes à Christ, vous êtes la postérité "
  "d'Abraham » (Ga 3:29 — C8). Hébreux boucle : « d'un seul homme… comme les étoiles… "
  "comme le sable » (Hé 11:12 — P005). « Comme le sable » signifie indéfini, non chiffré "
  "(voir 1957529)."
 ),
 hist=(
  "De 70 âmes (Ex 1:5 — C8) à la nation : en quatre générations après Jacob, la "
  "postérité sort d'Égypte en peuple organisé (voir 1101963005). Les recensements du "
  "désert chiffrent : 603 550 hommes (Nb 1:46 — C8). L'apogée salomonienne constate la "
  "formule : « Juda et Israël étaient nombreux, aussi nombreux que le sable… ils "
  "mangeaient, buvaient et se réjouissaient » (1R 4:20 — P013). Isaac moissonne au "
  "centuple l'année de la promesse (Gn 26:12-14 — P016). Jacob revient à Sichem puis "
  "Béthel comme annoncé (33:18 ; 35:6-12 — P019)."
 ),
 geo=(
  "La nuit cananéenne : un ciel sans pollution lumineuse, où quelques milliers d'étoiles "
  "donnent l'illusion du tout — et pourtant le texte voit juste (voir science). Le bord "
  "de la mer : la Méditerranée, dont le sable fournit la seconde mesure. Le Morija : le "
  "lieu du serment (22:2 — C8). Béthel : l'échelle et la poussière (28:19 — C8). Sichem : "
  "le retour accompli (33:18 — P019)."
 ),
 sci=(
  "Astronomie : à l'œil nu, quelques milliers d'étoiles seulement sont visibles — et "
  "pourtant la Bible compare leur nombre aux milliards de grains de sable : « la Bible "
  "est exacte sur le plan scientifique » (voir 101988248). La revue Bible Review, citée "
  "par l'article, s'étonne de cette précision dans l'Antiquité et suggère qu'Abraham "
  "était peut-être astronome — sans preuve, et sans lentilles antiques connues ; la "
  "conclusion évitée est l'inspiration. Jérémie, sans télescope, affirme avec la même "
  "précision : « L'armée des cieux ne peut se compter, ni le sable de la mer se mesurer » "
  "(Jr 33:22 — P253, voir K002). L'astronomie moderne donne raison à la comparaison : "
  "des centaines de milliards d'étoiles par galaxie, des milliards de galaxies."
 ),
 limites=(
  "« Comme le sable » est une image d'indéfini, pas un chiffre : on ne convertit pas la "
  "promesse en démographie (voir 1957529 : 144 000 « comme le sable » au sens "
  "d'indéterminé). L'hypothèse « Abraham astronome » (Bible Review) est rapportée pour "
  "être réfutée avec l'article : aucune lentille antique, aucun télescope patriarcal. "
  "Les recensements (Nb 1:46) sont les chiffres du texte, non des statistiques "
  "contrôlées. La postérité spirituelle (Ga 3:29) n'est pas un comptage ethnique."
 ),
 accomplissement=[("Nuit", "« Compte, si tu peux »"), ("Morija", "Serment : étoiles + sable"), ("Gérar", "À Isaac (P016)"),
     ("Béthel", "Poussière (P019)"), ("Égypte→Canaan", "Nation (Ex 1:7 ; Dt 1:10)"), ("Salomon→Christ", "Sable (1R 4) ; Ga 3:16") ],
 tl=[("Nuit", "« Compte, si tu peux »"), ("Morija", "Serment : étoiles + sable"), ("Gérar", "À Isaac (P016)"),
     ("Béthel", "Poussière (P019)"), ("Égypte→Canaan", "Nation (Ex 1:7 ; Dt 1:10)"), ("Salomon→Christ", "Sable (1R 4) ; Ga 3:16") ], src=[("« Comme les étoiles des cieux » (exactitude scientifique, 1998)", "https://wol.jw.org/fr/wol/d/r30/lp-f/101988248"),
      ("Une nation nouvelle est délivrée (4e génération)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101963005"),
      ("Genèse 15 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/15"),
      ("Genèse 22 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/22")],
 img="images/prophe_K001_etoiles.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K002", titre="L'alliance du jour et de la nuit — les lois du ciel garantes",
 ref="Jérémie 33:17-22 ; Jérémie 31:35-37 ; Jérémie 33:25, 26",
 statut="Accomplie / À venir (P253) · Continu (P244)",
 cat="K", syst="Système cycles (jour/nuit, lune, saisons)",
 reg="Registre : Jérémie — P253 (33:17-22 : trône de David, alliance du jour et de la nuit), P244 (31:35-37 : ordonnances du ciel, nation préservée)",
 texte=[
  "« Pourrez-vous rompre mon alliance du JOUR et de la NUIT… ? NON ! » (33:20 — le défi !)",
  "« Alors pourrait être rompue mon alliance avec DAVID… » (33:21 — le transfert !)",
  "« L'armée des cieux ne peut se COMPTER, ni le sable se MESURER. » (33:22 — Jr compte comme Gn !)",
  "« Soleil le jour, LUNE et étoiles la nuit… qui AGITE la mer. » (31:35 — le moteur des marées !)",
  "« Si ces LOIS s'écartaient… Israël CESSERAIT d'être une nation. » (31:36 — la garantie !)",
  "« Si les CIEUX se mesuraient… je rejetterais Israël. » (31:37 — l'impossible garant !)",
 ],
 contexte=(
  "Jérémie est enfermé dans la cour de garde pendant le siège (33:1 — C8) ; Jérusalem va "
  "tomber, et l'on dit déjà : Jéhovah a abandonné (33:24 — C8). C'est à ce moment — "
  "ville cernée, prophète en prison — que Dieu répond par le cosmos : le jour et la "
  "nuit, le soleil, la lune, les étoiles, la mer agitée. L'argument est un a fortiori "
  "cosmique : ce que personne ne peut rompre (l'alternance) garantit ce que personne ne "
  "peut croire (la survie de David et d'Israël). Jérémie 31:35-37 (P244) et 33:20-26 "
  "(P253) sont les deux volets du même acte."
 ),
 explication=(
  "« Alliance » s'applique ici à une ordonnance formelle : une création de Dieu régie "
  "par ses lois, « telle que la succession immuable du jour et de la nuit » (voir it-1 "
  "« Alliance », 1200001054). Le jour et la nuit viennent « au moment prévu » (voir "
  "2019525) — mo'èd, le rendez-vous. « Lois » (ḥuqqôt, 31:36 ; 33:25) : des ordonnances "
  "gravées, pas des habitudes. « Qui agite la mer » (31:35) : la lune motrice des marées "
  "(voir science). « Mesurer les cieux » (31:37) : l'impossible par excellence — les "
  "distances stellaires défient toute mesure humaine, et c'est cette impossibilité qui "
  "garantit. Double objet garanti : le trône de David (33:21, alliance davidique — voir "
  "J008) et la nation (31:36)."
 ),
 interpretation=(
  "Trône : « David ne manquera jamais d'un homme sur son trône » (33:17) — accompli en "
  "Christ : « Jéhovah Dieu lui donnera le trône de David » (Lc 1:32-33 — P253 ; voir "
  "J008), « notre Seigneur est sorti de Juda » (Hé 7:14 — P253 ; voir J005). Nation : "
  "« Israël ne cessera pas d'être une nation » (31:36) — le registre retient la "
  "préservation historique du peuple, en continu (P244), avec Jr 33:25-26 en sceau. "
  "Chaque aurore est un argument : depuis Jérémie, le jour et la nuit ne sont jamais "
  "venus « hors leur temps » — la garantie tourne toujours, donc l'alliance tient "
  "toujours."
 ),
 hist=(
  "Constat : depuis le siège de Jérusalem (VIe s.), l'alternance jour/nuit n'a jamais "
  "manqué — des centaines de milliers d'aurores consécutives, la plus longue série "
  "d'accomplissements continus du registre. Calendrier : les cycles garantis servent à "
  "dater tout le reste — sabbats, fêtes, 70 semaines (voir F). Relève davidique : "
  "Zorobabel, de la lignée, gouverneur au retour (Ag 2:23 — C8 ; voir J008). Préservation "
  "nationale : exil, retour, persécutions — le peuple de l'alliance traverse (P244 : "
  "« préservation historique », continu)."
 ),
 geo=(
  "La cour de garde : une prison à ciel ouvert — Jérémie voit le soleil et la lune "
  "dont il parle. Juda : du même point, la mer à l'ouest (« qui agite la mer ») et le "
  "désert à l'est ; le soleil se lève sur le mont des Oliviers, se couche sur la mer. "
  "« En leur temps » : les rendez-vous (mo'adîm) rythment l'année judéenne — équinoxes, "
  "lune nouvelle, moissons. Le cosmos de Jérémie tient dans un regard : soleil, lune, "
  "étoiles, mer."
 ),
 sci=(
  "Rotation : l'alternance jour/nuit est la rotation terrestre — 24 h stables, la "
  "grande horloge garantie par alliance. Gravitation : « qui agite la mer » (31:35) — "
  "la lune motrice des marées, deux bourrelets quotidiens, prévisibles à la minute : "
  "les « lois » (ḥuqqôt) en action. Constantes : l'uniformité de la nature — postulat de "
  "toute science — est ici un décret : les lois « ne s'écarteront pas ». Immensité : "
  "« si les cieux se mesuraient » (31:37) — les distances en années-lumière, l'expansion "
  "cosmique : mesurées sans être épuisées. Innombrable : 33:22 rejoint Gn 15:5 (voir K001)."
 ),
 limites=(
  "« Alliance avec le jour » est une image d'alliance (ordonnance garantie), pas un "
  "contrat signé avec un astre. P244 « continu » est un constat (préservation "
  "historique selon le registre), pas une prédiction datée — et cette fiche ne fait "
  "aucune géopolitique. La mécanique (rotation, gravitation) décrit le comment des "
  "cycles, pas le pourquoi de la garantie : la science constate les lois, l'alliance "
  "les fonde. Le trône « pour toujours » s'accomplit en Christ (voir J008) : aucune "
  "date pour l'avenir."
 ),
 accomplissement=[("Siège", "Prison + cosmos"), ("Chaque aurore", "« Au moment prévu »"), ("Retour", "Zorobabel (C8)"),
     ("Nazareth", "Lc 1:32-33 (P253)"), ("Continu", "Nation préservée (P244)"), ("Toujours", "Lois non écartées") ],
 tl=[("Siège", "Prison + cosmos"), ("Chaque aurore", "« Au moment prévu »"), ("Retour", "Zorobabel (C8)"),
     ("Nazareth", "Lc 1:32-33 (P253)"), ("Continu", "Nation préservée (P244)"), ("Toujours", "Lois non écartées") ], src=[("Alliance — Étude perspicace (succession immuable, Jr 33:20)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001054"),
      ("La foi nous rend forts (Jr 33:20, 2019)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2019525"),
      ("Jérémie 33 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/33"),
      ("Jérémie 31 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/31")],
 img="images/prophe_K002_jour.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K003", titre="Remplissez la terre — le dessein durable du 6e jour",
 ref="Genèse 1:28 ; Révélation 21:3, 4 ; Psaume 37:29 ; Ésaïe 55:11",
 statut="À venir (P975)",
 cat="K", syst="Système dessein (Éden → Royaume → Tente)",
 reg="Registre : Genèse/Révélation — P975 (Gn 1:28 + Ré 21:3-4 : dessein originel mené à terme)",
 texte=[
  "« Soyez FÉCONDS, devenez NOMBREUX, REMPLISSEZ la terre et SOUMETTEZ-la. » (1:28 — le mandat !)",
  "« Dieu ne manque JAMAIS de réaliser ses desseins. » (Is 55:11 — le principe !)",
  "« Les justes POSSÉDERONT la terre, et sur elle ils résideront pour TOUJOURS. » (Ps 37:29)",
  "« La TENTE de Dieu est avec les humains… il ESSUIERA toute larme… la MORT ne sera plus. » "
  "(Ré 21:3-4 — P975 !)",
  "« La terre DEMEURE pour toujours. » (Ec 1:4 — C8)",
  "« Non créée pour RIEN, FORMÉE pour être HABITÉE. » (Is 45:18 — C8)",
 ],
 contexte=(
  "Sixième jour : l'homme et la femme viennent d'être créés à l'image de Dieu (1:27 — "
  "C8), et la première parole qu'ils entendent est une bénédiction-mandat (1:28). La "
  "Genèse les place ensuite dans un jardin bien irrigué, le jardin d'Éden, en parfaite "
  "santé, avec devant eux un avenir éternel (voir 102008164). La rébellion (ch. 3 — C8) "
  "ne fait pas abandonner le dessein : Dieu « ne manque jamais de réaliser ses desseins » "
  "(voir 1983124, avec Gn 1:28 et Is 55:11). Le mandat du commencement attend son point "
  "final : la tente de Dieu avec les humains (Ré 21:3-4 — P975 ; voir G005)."
 ),
 explication=(
  "Quatre verbes, un programme : être féconds (la vie), devenir nombreux (la famille), "
  "remplir la terre (mālē' — la plénitude ordonnée, pas l'entassement), la soumettre "
  "(kābaš — la gestion, pas le pillage : voir K004). « Toute la planète serait "
  "finalement un paradis rempli d'humains parfaits » (voir 102008164) : le jardin "
  "d'Éden était la maquette, la terre le chantier. Ésaïe 55:11 donne la physique du "
  "dessein : la parole sortie « ne reviendra pas sans résultat ». Le Psaume 37:29 en "
  "est le titre de propriété : « les justes posséderont la terre… pour toujours » "
  "(voir 1983124)."
 ),
 interpretation=(
  "Dessein originel, méthode adaptée : le Royaume messianique est l'instrument par "
  "lequel le mandat de 1:28 s'accomplira malgré la rébellion (voir G, I010). Deux "
  "témoins inattendus cités par les publications (voir 102008164) : le bibliste Henry "
  "Alford — un royaume « qui dominera cette terre », des sujets qui « hériteront la "
  "terre régénérée et bénie pour toujours » — et Isaac Newton : « la terre continuera "
  "d'être habitée par les mortels après le jour de jugement… pour l'éternité ». Point "
  "final : Révélation 21:3-4 (P975) — tente, présence, larmes essuyées, mort abolie "
  "(voir G005)."
 ),
 hist=(
  "Newton (1643-1727) : le père de la gravitation croyait au paradis terrestre éternel "
  "(voir 102008164) — la science moderne naît chez un lecteur de 1:28. Alford (XIXe s.) : "
  "le royaume terrestre dans un commentaire du Nouveau Testament (voir 102008164). "
  "1983 : « Vous pouvez vivre éternellement sur une terre qui deviendra un paradis » "
  "(voir 1983124) — le dessein prêché comme bonne nouvelle. Démographie : huit "
  "milliards d'humains (repère neutre) — le « remplissez » en cours, la « plénitude "
  "ordonnée » à venir."
 ),
 geo=(
  "Éden : le jardin-maquette, bien irrigué, avec ses quatre fleuves (2:10-14 — C8). « Toute "
  "la planète » (voir 102008164) : le chantier — du jardin au globe. « Paradis » "
  "(paradeisos) : le jardin clos des rois perses — le mot même dit l'extension : toute "
  "la terre en jardin royal. La tente (Ré 21:3) : le tabernacle étendu à la planète — "
  "Dieu campe avec les humains."
 ),
 sci=(
  "Viabilité : « formée pour être habitée » (Is 45:18 — C8) — la Terre est une planète "
  "habitable par décret : eau liquide, atmosphère, magnétosphère, lune stabilisatrice. "
  "Durabilité : « la terre demeure pour toujours » (Ec 1:4 — C8) — le support ne sera "
  "pas jeté. Hydrologie : jardin « bien irrigué » (voir 102008164) — le cycle de l'eau "
  "(voir K005) comme infrastructure du dessein. Gestion : « soumettez » (kābaš) — "
  "l'intendance des espèces et des milieux confiée au mandataire (voir K004 : domination "
  "= responsabilité)."
 ),
 limites=(
  "« Remplissez » ne fixe aucun chiffre de population : aucune démographie normative "
  "n'est tirée du mandat. « Soumettez » n'autorise aucun pillage : gestion, pas "
  "prédation (voir K004). Le paradis planétaire est À VENIR (P975) : aucune date, aucun "
  "scénario, aucun programme militant — la fiche décrit le dessein, elle ne milite pas. "
  "Newton et Alford sont cités comme témoins d'une lecture, pas comme autorités "
  "doctrinales."
 ),
 accomplissement=[("6e jour", "Mandat (1:28)"), ("Éden", "Maquette irriguée"), ("Chute", "Dessein maintenu (Is 55:11)"),
     ("Royaume", "« Hériteront » (Ps 37:29)"), ("Millénium", "Paradis (voir G)"), ("21:3-4", "La Tente (P975)") ],
 tl=[("6e jour", "Mandat (1:28)"), ("Éden", "Maquette irriguée"), ("Chute", "Dessein maintenu (Is 55:11)"),
     ("Royaume", "« Hériteront » (Ps 37:29)"), ("Millénium", "Paradis (voir G)"), ("21:3-4", "La Tente (P975)") ], src=[("La terre sera-t-elle un paradis ? (Gn 1:28, Newton)", "https://wol.jw.org/fr/wol/d/r30/lp-f/102008164"),
      ("Vivre éternellement sur une terre paradisiaque (1983)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1983124"),
      ("Genèse 1 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/1"),
      ("Révélation 21 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/21")],
 img="images/prophe_K003_terre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K004", titre="Psaume 8 — la lune, les étoiles et les sentiers des mers",
 ref="Psaume 8:1-9 ; Hébreux 2:6-9 ; 1 Corinthiens 15:27",
 statut="Accomplie (P526, P610)",
 cat="K", syst="Système échelles (ciel → terre → mer)",
 reg="Registre : Psaumes — P526 (Ps 8:4-8 : inférieur aux anges, tout sous ses pieds), P610 (Ps 8:5-8 : idem)",
 texte=[
  "« Quand je vois tes CIEUX… la LUNE et les ÉTOILES que tu as préparées… » (8:3 — le vertige !)",
  "« Qu'est-ce que le MORTEL pour que tu penses à lui ? » (8:4 — la question !)",
  "« Tu l'as fait de PEU inférieur aux anges. » (8:5 — le rang !)",
  "« Tu l'as COURONNÉ de gloire et de splendeur. » (8:5 — la couronne !)",
  "« Tu as mis TOUTES CHOSES sous ses pieds. » (8:6 — le tout !)",
  "« …tout ce qui parcourt les SENTIERS DES MERS. » (8:8 — les sentiers !)",
 ],
 contexte=(
  "Psaume de David, « sur la guitith » (suscription — instrument dont le sens exact est "
  "incertain, voir les limites). Le psaume est bâti en inclusio : le verset 1 et le "
  "verset 9 sont identiques — « Ô Jéhovah notre Seigneur, que ton nom est majestueux "
  "sur toute la terre ! » Tout tient entre ces deux acclamations : le ciel (v. 3), "
  "l'homme (v. 4-5), la charge (v. 6-8). David parle en berger : des nuits à garder les "
  "troupeaux sous les étoiles (1S 17:34-35 — C8 : le lion et l'ours), des jours à "
  "observer bétail, bêtes, oiseaux, poissons."
 ),
 explication=(
  "Le mouvement est un paradoxe : plus le ciel est grand (v. 3), plus la question est "
  "petite (v. 4 : « qu'est-ce que le mortel ? ») — et plus la réponse est haute (v. 5-8 : "
  "couronné, autorité, TOUT). « De peu inférieur » (mé'at) : un cran sous les anges, "
  "pas un gouffre. L'inventaire descend du proche au lointain : petit et gros bétail, "
  "animaux sauvages, oiseaux, poissons — « et tout ce qui parcourt les sentiers des "
  "mers » (8:8) : des ROUTES dans l'océan, que poissons et navires empruntent sans les "
  "voir. Les publications citent le psaume avec Hébreux 2:5-9 (voir 1101988024) et "
  "reproduisent l'inventaire complet (voir 1975726)."
 ),
 interpretation=(
  "Hébreux applique le psaume à Jésus : « nous voyons Jésus… couronné de gloire » "
  "(Hé 2:9 — P526, P610), avec la tension assumée : « actuellement, nous ne voyons pas "
  "encore que toutes choses lui soient soumises » (Hé 2:8 — C8) — accompli et à venir "
  "ensemble. Paul reprend la formule : « il a mis toutes choses sous ses pieds » — "
  "« sauf celui qui lui a soumis toutes choses » (1Co 15:27 — P526, P610). La domination "
  "d'Adam (Gn 1:28 — voir K003), perdue en Éden, est relevée en Christ : le couronnement "
  "du v. 5 trouve son titulaire définitif."
 ),
 hist=(
  "Matthew Fontaine Maury (1806-1873), officier de marine américain, « père de "
  "l'océanographie moderne » : cartes des vents et des courants, routes maritimes "
  "réduites de moitié — il déclarait avoir été guidé par « les sentiers des mers » du "
  "Psaume 8:8. Le Gulf Stream, cartographié dès le XVIIIe siècle, est le plus célèbre "
  "de ces sentiers. « Réveillez-vous ! » (1973) promet qu'on connaîtra bien mieux « tout "
  "ce qui parcourt les sentiers des mers » dans l'ordre nouveau (voir 101972683) : la "
  "science marine a un avenir au paradis."
 ),
 geo=(
  "Cieux de Judée : la lune et les étoiles du berger, sans pollution lumineuse. Les mers : "
  "la Méditerranée de David, puis tous les océans — les sentiers courent partout : Gulf "
  "Stream (Atlantique), Kuroshio (Pacifique), circumpolaire antarctique. « Sous ses "
  "pieds » (8:6) : du sol au plancher océanique — « le fond des mers » couvert comme par "
  "les eaux de la connaissance (Is 11:9 — C8). Le domaine de l'homme va du zénith aux "
  "abysses."
 ),
 sci=(
  "Astronomie : lune et étoiles « préparées » (kûn — établies, ordonnées) — le ciel-ouvrage "
  "(voir K002 : les lois). Océanographie : les courants marins sont des fleuves dans la "
  "mer — le Gulf Stream transporte une trentaine de millions de m³ d'eau par seconde ; "
  "gyres, upwellings, tapis roulant thermohalin : les « sentiers » existent, cartographiés. "
  "Zoologie marine : baleines, thons, tortues migrent le long des courants — « tout ce "
  "qui parcourt » (8:8) à la lettre. Aérologie : Maury cartographia aussi les vents — "
  "les sentiers du ciel, jumeaux de ceux des mers."
 ),
 limites=(
  "Maury « guidé par le verset » : témoignage rapporté du navigateur, pas démonstration "
  "— la fiche le cite comme fait historique, non comme preuve. « Sentiers » = courants "
  "(lecture reçue), sans exclure les routes de navigation qui les suivent. « Pas encore "
  "toutes choses » (Hé 2:8) : la tension accompli/à venir est assumée, pas résolue par "
  "une date. « Guitith » (suscription) : sens incertain (instrument ? pressoir ? Gath ?) — "
  "non tranché."
 ),
 accomplissement=[("Nuits de Juda", "Berger astronome"), ("Psaume", "Inclusio v.1 = v.9"), ("Ier s.", "Hé 2 : Jésus couronné"),
     ("1Co 15:27", "« Tout » sauf Dieu"), ("XIXe s.", "Maury : les sentiers"), ("À venir", "« Pas encore » (Hé 2:8)") ],
 tl=[("Nuits de Juda", "Berger astronome"), ("Psaume", "Inclusio v.1 = v.9"), ("Ier s.", "Hé 2 : Jésus couronné"),
     ("1Co 15:27", "« Tout » sauf Dieu"), ("XIXe s.", "Maury : les sentiers"), ("À venir", "« Pas encore » (Hé 2:8)") ], src=[("La fuite vers le refuge (Ps 8:3-8 cité, 1976)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1975726"),
      ("Qu'est-ce qu'un aquarium ? (sentiers, 1973)", "https://wol.jw.org/fr/wol/d/r30/lp-f/101972683"),
      ("Un message doux et amer (Ps 8 + Hé 2, re)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101988024"),
      ("Psaume 8 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/8")],
 img="images/prophe_K004_psaume8.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K005", titre="Le ciel sous parole — Élie ferme, Élie ouvre ; Aggée retient",
 ref="1 Rois 17:1 ; 1 Rois 18:1, 41-45 ; Jacques 5:17, 18 ; Aggée 1:2-11",
 statut="Accomplie (P080, P485)",
 cat="K", syst="Système saisons (3 ans 1/2 sans pluie)",
 reg="Registre : Rois/Aggée — P080 (1R 17:1 : ni rosée ni pluie, sinon par sa parole), P485 (Ag 1:2-11 : cieux retiennent la rosée)",
 texte=[
  "« Ni ROSÉE ni PLUIE ces années-ci, SINON PAR MA PAROLE. » (17:1 — le robinet !)",
  "« Va, montre-toi à Achab : je vais donner de la PLUIE. » (18:1 — 3e année !)",
  "« Voici un PETIT NUAGE comme la paume d'une main qui MONTE DE LA MER. » (18:44 — la paume !)",
  "« Le ciel se NOIRCIT de nuées et de vent : FORTE PLUIE. » (18:45 — le cycle bouclé !)",
  "« Il ne plut pas pendant TROIS ANS ET SIX MOIS… puis le ciel donna de la pluie. » (Jc 5:17-18)",
  "« Les CIEUX RETIENNENT la rosée, la terre retient ses PRODUITS. » (Ag 1:10 — le robinet, bis !)",
 ],
 contexte=(
  "Achab règne, Jézabel importe Baal — le dieu de l'orage sémitique, « chevaucheur des "
  "nuées » des tablettes d'Ougarit (XIVe s.) — et Jéhovah répond chez Baal, sur son "
  "terrain : le ciel (1R 16:31-33 — C8). Élie le Thischbite, Galaadite surgi de nulle "
  "part, jette 17:1 à la face du roi puis disparaît : Kerith (corbeaux, 17:6 — C8), "
  "Sarepta (farine et huile, 17:14-16 — C8). Troisième année : Carmel — 450 prophètes de "
  "Baal, feu du ciel (18:19-40 — C8), puis la paume. Cinq siècles plus tard, Aggée "
  "rejoue le robinet : le temple en ruines, les maisons lambrissées (1:4 — C8) — les "
  "cieux retiennent la rosée (1:10-11)."
 ),
 explication=(
  "« Sinon par ma parole » : la parole du prophète est le robinet du ciel — fermé en "
  "17:1, rouvert en 18:1 (« je vais donner »). Baal « chevaucheur des nuées » ne peut "
  "ni allumer (Carmel : pas de feu, 18:26-29 — C8) ni arroser : Jéhovah fait les deux le "
  "même jour (feu 18:38, pluie 18:45). « Trois ans et six mois » (Jc 5:17 — P080 ; Lc "
  "4:25 — C8) : la durée que 17:1 (« ces années-ci ») ne chiffrait pas. La séquence "
  "18:44-45 est un cycle de l'eau complet : mer → petit nuage → ciel noirci de vent → "
  "forte pluie. Aggée : même robinet, autre motif — rosée retenue, produits retenus, "
  "« bourse percée » (1:6 — C8) : sanction économique ciblée jusqu'à la reprise du "
  "chantier (Esd 5:1-2 — P485)."
 ),
 interpretation=(
  "Le cas d'Élie démontre « l'efficacité des prières chez un homme avec des sentiments "
  "semblables aux nôtres » (voir it-1 « Éliya », 1200001307, avec Jc 5:17) : il pria "
  "pour fermer, il pria pour ouvrir (Jc 5:17-18). L'Insight liste six miracles d'Élie : "
  "pluie empêchée, farine et huile, résurrection, feu du Carmel, pluie rendue, feu sur "
  "les capitaines (voir 1200001307). Aggée : les priorités commandent le climat — la "
  "maison de Dieu d'abord, et les cieux rouvrent (la reprise du chantier, Esd 5:1-2, "
  "suit l'oracle — P485). Deux époques, un seul ciel sous parole."
 ),
 hist=(
  "Achab dans les annales assyriennes : le monolithe de Kurkh (Salmanazar III, bataille "
  "de Qarqar, 853 — repère) nomme « Achab l'Israélite » et ses 2 000 chars — le roi de "
  "la sécheresse existe hors de la Bible. Baal « chevaucheur des nuées » (rkb 'rpt) : "
  "titre ougaritique (XIVe s.) — le rival désigné du Carmel. Sarepta (Sarafand, Liban) : "
  "ville phénicienne fouillée, entre Tyr et Sidon. Le ouadi de Kerith, à l'est du "
  "Jourdain en Gad (voir 1200001307), tarit (17:7 — C8) : la sécheresse frappe aussi le "
  "prophète."
 ),
 geo=(
  "Galaad : le pays d'Élie, à l'est du Jourdain. Kerith : le refuge qui tarit (17:7). "
  "Sarepta : la côte phénicienne — le prophète nourri en pays de Jézabel ! Le Carmel : "
  "le cap sur la mer d'où le serviteur voit monter la paume (18:43-44 — C8) — le nuage "
  "monte DE LA MER : le cycle commence sous ses yeux. Yizréel : Achab y court sous la "
  "pluie, Élie devant son char (18:45-46 — C8). Jérusalem post-exilique : le second "
  "robinet (Aggée)."
 ),
 sci=(
  "Cycle de l'eau en 18:44-45 : évaporation marine → « petit nuage » (convection) → "
  "« ciel noirci de nuées et de vent » (coalescence, front) → « forte pluie » — séquence "
  "météorologique exacte, observée depuis le Carmel face à la mer. Rosée : condensation "
  "nocturne, vitale dans l'été levantin sans pluie — 17:1 ferme les DEUX robinets (rosée "
  "d'été + pluies d'automne et de printemps, Jc 5:7 — C8). Sécheresse de 3 ans 1/2 : "
  "torrents à sec (Kerith, 17:7), nappes épuisées, bétail menacé (18:5 — C8). Économie : "
  "Ag 1:6 — semer beaucoup, rentrer peu ; « bourse percée » : l'inflation de la "
  "sécheresse."
 ),
 limites=(
  "« Ces années-ci » (17:1) ne chiffre pas : la durée (3 ans 1/2) vient de Luc et Jacques "
  "— la fiche ne fait pas dire à 17:1 ce qu'il ne dit pas. Le mécanisme de la fermeture "
  "(comment le ciel se ferme) n'est pas décrit : miracle constaté par ses effets, pas "
  "météorologie expliquée. Kerith exact : non identifié (plusieurs ouadis proposés à "
  "l'est du Jourdain). Le sceau dit « de Jézabel » n'est pas évoqué (authenticité "
  "débattue). Qarqar 853 : repère conventionnel, signalé comme tel."
 ),
 accomplissement=[("17:1", "Robinet fermé"), ("Kerith-Sarepta", "Nourri (17:6, 16)"), ("Carmel", "Feu (18:38)"),
     ("Paume", "Nuage de la mer (18:44)"), ("3 ans 1/2", "Pluie (18:45 ; Jc 5:17)"), ("Aggée", "Rosée → chantier (Esd 5)") ],
 tl=[("17:1", "Robinet fermé"), ("Kerith-Sarepta", "Nourri (17:6, 16)"), ("Carmel", "Feu (18:38)"),
     ("Paume", "Nuage de la mer (18:44)"), ("3 ans 1/2", "Pluie (18:45 ; Jc 5:17)"), ("Aggée", "Rosée → chantier (Esd 5)") ], src=[("Éliya — Étude perspicace (3 ans 1/2, 6 miracles)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001307"),
      ("Jacques 5 — Bible d'étude (3 ans 6 mois)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/59/5"),
      ("1 Rois 18 — Bible d'étude (Carmel, paume)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/11/18"),
      ("Aggée 1 — Bible d'étude (rosée retenue)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/37/1")],
 img="images/prophe_K005_elie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="K006", titre="Le cadran d'Achaz — l'ombre recule de dix marches",
 ref="Ésaïe 38:1-8 ; 2 Rois 20:5-11 ; 2 Chroniques 32:30 (C8)",
 statut="Accomplie (P154)",
 cat="K", syst="Système jours (3e jour) + ans (15 ans)",
 reg="Registre : Ésaïe — P154 (Is 38:1-8 : quinze années ajoutées, signe de l'ombre reculée)",
 texte=[
  "« Mets ORDRE à ta maison : tu vas MOURIR. » (38:1 — le diagnostic !)",
  "« Ézéchias… pleura ABONDAMMENT. » (38:3 — les larmes !)",
  "« J'AJOUTERAI à tes jours QUINZE ANNÉES. » (38:5 — les 15 ans !)",
  "« Je DÉLIVRERAI, toi et cette ville, de l'ASSYRIEN. » (38:6 — la ville avec !)",
  "« L'ombre AVANCERA-t-elle de dix degrés, ou RECULERA-t-elle ? » (2R 20:9 — le choix !)",
  "« C'est peu que l'ombre avance… plutôt qu'elle RECULE. » (2R 20:10 — l'impossible choisi !)",
  "« L'ombre RECULA de dix degrés sur le cadran d'Achaz. » (38:8 — le signe !)",
 ],
 contexte=(
  "Ézéchias est malade — un furoncle soigné au gâteau de figues (2R 20:7 — C8) — pendant "
  "que l'Assyrien menace (Sennachérib : voir A013). Ésaïe annonce la mort ; le roi se "
  "tourne vers le mur et plaide sa fidélité (38:2-3) ; Ésaïe, « pas encore sorti de la "
  "cour », est renvoyé avec le contre-ordre (2R 20:4-5 — C8). Triple don : guérison "
  "(« le troisième jour tu monteras », 2R 20:5), quinze années (38:5), ville délivrée "
  "(38:6). Le signe couvre les trois : le ciel signera le décret sur le cadran du "
  "palais — les « degrés d'Achaz », l'escalier monumental du père (voir 1200011961)."
 ),
 explication=(
  "Le choix offert est un test : avancer (sens naturel — « c'est peu de chose ») ou "
  "reculer (impossible). Ézéchias choisit l'impossible — et l'impossible arrive (38:8 ; "
  "2R 20:11 — P154). « Degrés » traduit ma'alôt — des MARCHES, pas des degrés d'angle : "
  "un escalier (ou un cadran à marches) dont l'ombre marquait l'heure ; l'ombre remonta "
  "de dix marches. Le signe est public (palais, plein jour) et vérifiable (chacun sait "
  "lire une ombre). « Le troisième jour » (2R 20:5, 8) : guérison datée — montée au "
  "Temple, culte restauré. Et trois ans après cet événement, Ézéchias eut un fils : "
  "Manassé (voir 1200011961) — sans les quinze ans, pas de Manassé ; sans Manassé, pas "
  "de Josias (Mt 1:10 — C8 ; voir J002, J011) !"
 ),
 interpretation=(
  "Le ciel garantit le décret : comme le jour et la nuit garantissent David (voir K002), "
  "l'ombre garantit Ézéchias — Dieu signe avec le soleil. La prière avec larmes (38:3, 5 : "
  "« j'ai entendu… j'ai vu tes larmes ») obtient le contre-ordre : le décret de mort "
  "n'est pas fatal. La ville est comprise dans le don (38:6) — Sennachérib brisera ses "
  "dents la nuit même de l'orgueil (voir A013). Et la lignée : les quinze ans portent "
  "Manassé, Amon, Josias — le cadran d'Achaz fait tic-tac jusqu'à Béthel (voir J002)."
 ),
 hist=(
  "Sennachérib assiège Jérusalem (prisme de Taylor : le roi « enfermé comme un oiseau » "
  "— voir A013) : le contexte assyrien de 38:6 est documenté. Le tunnel de Siloé, percé "
  "sous Ézéchias pour amener l'eau du Guihon intra-muros (2Ch 32:30 — C8), porte "
  "l'inscription commémorative des carriers — le chantier du siège, encore visitable. "
  "Une bulle « à Ézéchias, fils d'Achaz, roi de Juda » (Ophel, mise au jour 2015) "
  "atteste le roi du signe. Manassé règne 55 ans (2R 21:1 — C8) : les quinze ans "
  "fructifient au-delà."
 ),
 geo=(
  "Le palais : la cour, les degrés exposés au soleil — le signe a lieu à domicile, en "
  "plein jour. « Tu monteras à la maison de Jéhovah » (2R 20:5) : monter — la topographie "
  "de Jérusalem en un verbe (le Temple domine). Le Guihon et Siloé : l'eau du siège, le "
  "tunnel de 533 m (repère). Contre-champ assyrien : Lakish assiégée, Jérusalem épargnée "
  "(voir A013). Le cadran regarde le sud (soleil au zénith de Juda) — orientation "
  "exacte inconnue (voir les limites)."
 ),
 sci=(
  "Gnomonique : les cadrans solaires antiques (Égypte, Mésopotamie — obélisques, marches, "
  "murs gradués) lisaient l'heure aux ombres dès le IIe millénaire ; un escalier "
  "monumental fait un excellent cadran : chaque marche = une heure-marque. Philologie "
  "décisive : ma'alôt = « montées, marches » — PAS des degrés d'angle : aucune conversion "
  "en minutes n'est légitime (les « 40 minutes » de certains commentateurs supposent "
  "des degrés, ce que le mot ne dit pas — voir les limites). Optique : une ombre qui "
  "recule suppose lumière + relief modifiés — le texte constate l'effet, pas le "
  "mécanisme. Médecine : le gâteau de figues (2R 20:7) — cataplasme émollient d'usage "
  "courant au Proche-Orient ancien."
 ),
 limites=(
  "« Degrés » = marches (ma'alôt), pas degrés d'angle : AUCUNE durée (40 minutes ou "
  "autre) n'est calculée ici — les conversions supposent ce que le mot ne dit pas. Le "
  "mécanisme du recul n'est pas décrit : miracle constaté par son effet public, pas "
  "phénomène expliqué. La forme exacte du cadran d'Achaz (escalier ? degrés maçonnés ? "
  "l'Auxiliaire dit « escalier ») et son orientation restent inconnues. Les figues "
  "(2R 20:7) : soin rapporté, efficacité non évaluée — la guérison est attribuée à "
  "Jéhovah (38:5), pas au cataplasme."
 ),
 accomplissement=[("Lit", "« Tu vas mourir » (38:1)"), ("Mur", "Prière + larmes (38:2-3)"), ("Cour", "Ésaïe revient (2R 20:4-5)"),
     ("Degrés", "L'ombre recule (38:8)"), ("3e jour", "Montée au Temple (2R 20:5)"), ("+3 ans", "Manassé → Josias !") ],
 tl=[("Lit", "« Tu vas mourir » (38:1)"), ("Mur", "Prière + larmes (38:2-3)"), ("Cour", "Ésaïe revient (2R 20:4-5)"),
     ("Degrés", "L'ombre recule (38:8)"), ("3e jour", "Montée au Temple (2R 20:5)"), ("+3 ans", "Manassé → Josias !") ], src=[("Ézéchias — Auxiliaire (15 ans, escalier d'Achaz, Manassé)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011961"),
      ("Ésaïe 38 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/38"),
      ("2 Rois 20 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/20"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_K006_cadran.jpg",
))
