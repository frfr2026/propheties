#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE C (2e partie) — LE MESSIE : LE MINISTERE
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="C",
    nom="Le Messie : le ministère (2e partie)",
    vague="4",
    intro=(
        "Après le lieu, la mère et le précurseur (1re partie), voici le ministère : "
        "neuf fiches qui suivent Jésus de Nazareth à Jérusalem. L'entrée triomphale "
        "sur un ânon, la lecture d'Ésaïe 61 à la synagogue, la lumière levée sur la "
        "Galilée, le Prophète annoncé par Moïse, les miracles qui répondent à Jean, "
        "les paraboles promises par Asaph, le Serviteur doux d'Ésaïe 42, les maladies "
        "portées d'Ésaïe 53:4, et le surnom de Nazaréen. Deux précisions de périmètre : "
        "Ésaïe 53 n'entre ici que par son verset 4, celui que Matthieu applique aux "
        "guérisons — le reste du chant appartient à la catégorie D ; et la pierre "
        "angulaire, rejetée puis exaltée, attendra elle aussi la catégorie D, avec le "
        "procès, la mort et la résurrection."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C006", titre="L'entrée triomphale — ton roi vient à toi, humble",
 ref="Zacharie 9:9-10 ; Matthieu 21:1-11 ; Marc 11:1-11 ; Luc 19:28-44 ; Jean 12:12-19",
 statut="Accomplie",
 cat="C", syst="Système 33",
 reg="Registre : Zacharie — P503 (9:9) ; contexte : P502 (9:1-8)",
 texte=[
  "« Sois très joyeuse, fille de Sion ! Pousse des cris de triomphe, fille de "
  "Jérusalem ! Ton roi vient à toi : il est juste et victorieux, humble, monté "
  "sur un âne, sur un ânon, le petit d'une ânesse. » (Za 9:9)",
  "« Je retrancherai le char d'Éphraïm et le cheval de Jérusalem ; il annoncera "
  "la paix aux nations. » (Za 9:10)",
  "« Hosanna au Fils de David ! Béni soit celui qui vient au nom de Jéhovah ! » "
  "(Mt 21:9, reprenant Ps 118:25-26)",
 ],
 contexte=(
  "Zacharie prophétise vers 520-518, après le retour d'exil : son chapitre 9 "
  "s'ouvre sur le jugement des voisins — Hadrac, Damas, Tyr, la Philistie — puis "
  "basculle vers Sion et son roi. Cinq siècles et demi plus tard, à quelques jours "
  "de la Pâque de 33, Jésus monte de Béthanie et Bethphagé, sur le versant oriental "
  "du mont des Oliviers. Les pèlerins affluent déjà à Jérusalem pour la fête ; la "
  "foule qui descend avec lui grossit à chaque pas, et l'acclamation éclate."
 ),
 explication=(
  "Le verset 10 donne la clé du verset 9 : le cheval et le char retranchés, c'est "
  "la guerre abolie — le roi promis ne monte pas un destrier mais un âne, monture "
  "de paix et, en Israël, monture des chefs (Jg 10:4 ; 1R 1:33, Salomon intronisé "
  "sur la mule de David). « Humble » traduit un mot qui dit aussi l'affliction : "
  "le roi vient en doux, non en conquérant. Matthieu précise l'ânesse et son ânon ; "
  "Marc et Luc ajoutent que l'ânon n'avait encore porté personne — un animal neuf "
  "pour un usage sacré, comme les vaches de l'arche (1S 6:7). « Hosanna » n'est pas "
  "un cri de joie : c'est le verset 25 du Psaume 118, « sauve donc ! », détourné "
  "de la liturgie vers Jésus."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus s'est présenté ce jour-là "
  "comme le Roi promis, pacifique et légitime : l'ânon trouvé comme annoncé, les "
  "vêtements étendus comme pour Jéhu (2R 9:13, rite d'intronisation), le Psaume 118 "
  "clamé par la foule. Les publications précisent le détail de Matthieu 21:7 : "
  "les disciples mirent leurs vêtements sur l'ânon, et c'est sur ces vêtements "
  "que Jésus s'assit — non sur deux animaux à la fois. Le même jour, Jésus pleure "
  "sur la ville (Lc 19:41-44) : le Roi présenté est aussi le Juge annoncé."
 ),
 accomplissement=[
  ("520-518 av. n. è.", "Zacharie 9:9 nomme le roi humble cinq siècles et demi d'avance"),
  ("33 de n. è., avant Pâque", "L'ânesse et l'ânon trouvés à Bethphagé, comme Jésus l'avait dit"),
  ("33 de n. è.", "Descente du mont des Oliviers : vêtements, rameaux, Psaume 118 acclamé"),
  ("33 de n. è.", "« Si eux se taisent, les pierres crieront » (Lc 19:40) ; pleurs sur Jérusalem"),
  ("33 de n. è.", "Entrée dans le temple, regard sur toutes choses, retour à Béthanie (Mc 11:11)"),
 ],
 hist=(
  "Le dossier est liturgique et royal. Le Psaume 118 appartient au Hallel, chanté "
  "à la Pâque : la foule détourne vers Jésus l'antienne du pèlerinage. 2 Rois 9:13 "
  "fournit le précédent des vêtements étendus sous les pas du roi proclamé. "
  "1 Rois 1:33 montre Salomon intronisé sur la mule de David : la monture pacifique "
  "du sacre. Josèphe, de son côté, décrit les foules immenses de la Pâque — "
  "Jérusalem déborde de pèlerins, et c'est devant eux que l'acclamation éclate. "
  "Jean 12:16 ajoute la note d'honnêteté : les disciples eux-mêmes ne comprirent "
  "qu'après la glorification."
 ),
 geo=(
  "L'itinéraire est une descente : Bethphagé et Béthanie sur le versant oriental, "
  "la route qui contourne le mont des Oliviers, la vallée du Cédron en contrebas, "
  "puis la remontée vers le Temple. C'est au tournant où la ville apparaît que "
  "Jésus pleure (Lc 19:41) : la topographie commande la dramaturgie. Le mont des "
  "Oliviers fait face au Temple, à moins d'un kilomètre à vol d'oiseau : le Roi "
  "vient à Sion par la route orientale, celle des pèlerins de Jéricho et de "
  "Béthanie."
 ),
 sci=(
  "La topographie du mont des Oliviers et le tracé de la route antique, jalonnée "
  "de tombeaux du Ier siècle, correspondent au récit des quatre Évangiles. "
  "L'archéologie funéraire de Béthanie (tombeaux à kokhim du Second Temple) confirme "
  "l'occupation du village au temps de Marthe, Marie et Lazare. La zoologie "
  "historique éclaire le choix de la monture : l'âne blanc des chefs israélites "
  "(Jg 5:10) n'a rien d'une bête de somme quelconque — c'est la monture du pouvoir "
  "en temps de paix, opposée au cheval de guerre du verset 10."
 ),
 limites=(
  "Marc, Luc et Jean ne mentionnent que l'ânon : Matthieu complète, il ne "
  "contredit pas — la question des lecteurs citée en source tranche le détail de "
  "Matthieu 21:7. La foule qui acclame ne comprend pas ce qu'elle chante "
  "(Jn 12:16) : l'accomplissement constaté n'implique pas l'adhésion lucide. "
  "Cette fiche ne fixe pas le jour exact de l'entrée dans la semaine pascale. "
  "Les pleurs sur Jérusalem (Lc 19:41-44) annoncent 70 : voir B007."
 ),
 tl=[("520-518", "Zacharie 9:9"), ("33, av. Pâque", "L'ânon trouvé"), ("33", "L'entrée"),
     ("33", "Pleurs sur la ville"), ("33", "Le temple, puis Béthanie")],
 src=[("Sur quel animal Jésus fit-il son entrée ? — QR", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965567"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Zacharie 9 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/9"),
      ("Matthieu 21 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/21")],
 img="images/prophe_C006_entree.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C007", titre="Ésaïe 61 à Nazareth — aujourd'hui, cette parole",
 ref="Ésaïe 61:1-3 ; Luc 4:16-30 ; Matthieu 11:5",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Ésaïe — P177 (61:1-3), P596 (61:1-2), P605 (61:1)",
 texte=[
  "« L'esprit du Souverain Seigneur Jéhovah est sur moi, car Jéhovah m'a oint "
  "pour annoncer la bonne nouvelle aux humbles ; il m'a envoyé pour panser ceux "
  "qui ont le cœur brisé, proclamer la libération aux captifs, l'ouverture des "
  "yeux aux prisonniers, pour proclamer l'année de bienveillance de Jéhovah. » "
  "(Is 61:1-2a)",
  "« Et le jour de vengeance de notre Dieu. » (Is 61:2b — le membre de phrase que "
  "Jésus ne lit pas)",
  "« Aujourd'hui, cette parole que vous venez d'entendre est accomplie. » (Lc 4:21)",
 ],
 contexte=(
  "Un sabbat, à Nazareth, « où il avait été élevé », Jésus entre dans la synagogue "
  "« comme il en avait l'habitude » et se lève pour lire. On lui remet le rouleau "
  "d'Ésaïe ; il le déroule, trouve le passage, lit, roule le livre, s'assied — "
  "la position du maître qui enseigne — et prononce une seule phrase de commentaire. "
  "C'est le manifeste du ministère galiléen, dans les premiers mois qui suivent le "
  "baptême de 29. Tous les yeux sont fixés sur lui."
 ),
 explication=(
  "La lecture est un acte exégétique : Jésus lit 61:1 jusqu'au milieu du verset 2 "
  "et s'arrête avant « le jour de vengeance ». La coupure est le message : la "
  "première venue ouvre « l'année » — la longue période de faveur — et réserve la "
  "vengeance. Luc, écrivant en grec, cite selon les Septante : « l'année favorable "
  "de Jéhovah ». « Oint » (mashach), c'est le mot même de Messie et de Christ : "
  "en lisant, Jésus se désigne. La mission listée est spirituelle avant d'être "
  "sociale : cœurs brisés, captifs du péché, aveugles de l'ignorance, écrasés "
  "relevés."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus, oint d'esprit saint à "
  "son baptême de 29, s'est appliqué à lui-même la prophétie et a ouvert « l'année "
  "de bienveillance » — toute la période pendant laquelle Dieu montre sa faveur à "
  "ceux qui se tournent vers lui. Les publications soulignent que l'accomplissement "
  "d'Ésaïe 61 est d'abord spirituel : le bonheur matériel n'est pas la chose "
  "primordiale. Et elles notent le paradoxe final : admiré (« tous lui rendaient "
  "témoignage »), Jésus est rejeté dans l'heure — « médecin, guéris-toi toi-même » "
  "— et conduit au précipice. L'Oint proclamé chez lui, puis chassé de chez lui."
 ),
 accomplissement=[
  ("VIIIe-VIIe s. av. n. è.", "Ésaïe 61 : le manifeste de l'Oint (même rouleau que B004)"),
  ("IIe s. av. n. è.", "Les Septante : « l'année favorable » — le texte que Luc citera"),
  ("29 de n. è., automne", "Baptême : l'onction d'esprit qui fait l'Oint"),
  ("30 de n. è. env.", "Lecture à Nazareth : « aujourd'hui, cette parole est accomplie »"),
  ("30 de n. è. env.", "Rejet et précipice évité ; départ pour Capharnaüm (voir C008)"),
 ],
 hist=(
  "La note d'étude sur Luc 4:17 donne la mesure du rouleau : le grand rouleau "
  "d'Ésaïe de la mer Morte assemble 17 feuilles cousues, 7,3 mètres de long, "
  "54 colonnes — celui de Nazareth avait peut-être une longueur semblable. "
  "Dérouler jusqu'au chapitre 61 prenait du temps : le silence de la synagogue "
  "fait partie de la scène. L'inscription de Théodotos, à Jérusalem (Ier siècle), "
  "atteste une synagogue bâtie « pour la lecture de la Loi » : le cadre liturgique "
  "du récit est épigraphiquement confirmé."
 ),
 geo=(
  "Nazareth : un bourg de Basse-Galilée, dans une cuvette à l'écart des grandes "
  "routes (voir C014). La synagogue — le lieu de lecture, d'enseignement et de "
  "jugement local — en est le cœur. Le « sourcil de la montagne » où l'on veut "
  "précipiter Jésus (Lc 4:29) est montré traditionnellement au mont du Précipice, "
  "à deux kilomètres au sud : tradition, pas fouille (voir Limites). De Nazareth "
  "rejetante, Jésus descend à Capharnaüm, au bord du lac : trente kilomètres vers "
  "le nord-est, et un changement de monde."
 ),
 sci=(
  "Le texte lu est doublement verrouillé : le rouleau 1QIsa-a (IIe siècle avant "
  "notre ère) contient Ésaïe 61 dans un hébreu antérieur au christianisme, et la "
  "Septante en donne le grec que Luc reprend. L'archéologie de Nazareth (maisons à "
  "cour, citernes, pressoirs et silos du Ier siècle) confirme un bourg juif rural "
  "et pieux — le décor exact du récit. Sous la synagogue blanche de Capharnaüm "
  "(IVe siècle), les fouilles ont dégagé des murs en basalte du Ier siècle : la "
  "pierre des synagogues où Jésus enseigna."
 ),
 limites=(
  "L'emplacement exact de la synagogue de Nazareth n'est pas localisé, et le mont "
  "du Précipice est une identification traditionnelle. L'année de la lecture "
  "(vers 30) est approximative : Luc la place au début du ministère galiléen sans "
  "la dater au mois près. Le « jour de vengeance » non lu renvoie à un avenir que "
  "cette fiche ne date pas. Le rejet de Nazareth montre, comme en C006, que "
  "l'accomplissement constaté ne force pas l'adhésion."
 ),
 tl=[("VIIIe-VIIe s.", "Ésaïe 61"), ("IIe s.", "Septante"), ("29", "Onction au baptême"),
     ("30 env.", "Lecture à Nazareth"), ("30 env.", "Rejet, puis Capharnaüm")],
 src=[("Il est encore temps de profiter de l'année de bienveillance", "https://wol.jw.org/fr/wol/d/r30/lp-f/1970805"),
      ("Luc 4 — Bible d'étude (le rouleau de 7,3 m)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/4"),
      ("Luc 4:16-21 et Ésaïe 61:1-2 cités", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965082"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_C007_nazareth.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C008", titre="La Galilée des nations — une grande lumière",
 ref="Ésaïe 9:1-2 ; Matthieu 4:12-17, 23-25 ; Luc 4:31",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Ésaïe — P119 (9:1-2), P597 (9:1-2)",
 texte=[
  "« Le peuple qui marchait dans les ténèbres a vu une grande lumière ; sur ceux "
  "qui habitaient le pays de l'ombre de la mort, une lumière a brillé. » (Is 9:2)",
  "« Pays de Zabulon et pays de Nephtali, route de la mer, au-delà du Jourdain, "
  "Galilée des nations ! » (Is 9:1 ; Mt 4:15)",
  "« Il quitta Nazareth et s'installa à Capharnaüm, au bord de la mer, dans le "
  "territoire de Zabulon et de Nephtali. » (Mt 4:13)",
 ],
 contexte=(
  "Le paradoxe est voulu par Ésaïe : le nord — Zabulon et Nephtali — a été la "
  "première proie de Tiglath-Piléser III (2R 15:29, voir A010 : « le pays de "
  "Nephtali » emmené en Assyrie) ; il sera le premier éclairé. Huit siècles plus "
  "tard, quand Jésus apprend l'arrestation de Jean, il se retire en Galilée, "
  "quitte Nazareth qui l'a rejeté (voir C007) et s'installe à Capharnaüm. Matthieu "
  "cite l'oracle au moment exact du déménagement : la lumière a une adresse."
 ),
 explication=(
  "« Galilée des nations » (littéralement « cercle des nations ») dit la mixité : "
  "dès Salomon, vingt villes galiléennes ont été cédées à Hiram de Tyr (1R 9:11), "
  "et la « route de la mer » (la Via Maris, Damas-Côte-Égypte) brasse les peuples. "
  "Les « ténèbres », au sens premier, ce sont les armées assyriennes ; au sens "
  "plénier, l'obscurité spirituelle où « l'ombre de la mort » règne. La « grande "
  "lumière », c'est l'enseignement et les œuvres (Mt 4:23 : enseigner, prêcher, "
  "guérir — le triptyque du ministère). Capharnaüm, « au bord de la mer » et "
  "« au-delà du Jourdain » vu de Jérusalem, coche chaque membre de l'oracle."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Capharnaüm est devenue « sa "
  "ville » (Mt 9:1) et le quartier général de la lumière : c'est là que Jésus "
  "appelle les quatre premiers disciples, puis Matthieu au bureau des impôts, "
  "choisit les douze sur une montagne proche — tous Galiléens sauf peut-être "
  "Judas — et accomplit l'essentiel de ses œuvres de puissance. Les foules qui "
  "affluent « de Galilée, de la Décapole, de Jérusalem, de Judée et d'au-delà du "
  "Jourdain » (Mt 4:25) dessinent la carte de la lumière : Juifs et nations mêlés, "
  "comme le nom l'annonçait."
 ),
 accomplissement=[
  ("733 av. n. è. env.", "Tiglath-Piléser III ravage Nephtali (2R 15:29) : les ténèbres"),
  ("VIIIe s. av. n. è.", "Ésaïe 9:1-2 promet la grande lumière aux mêmes territoires"),
  ("30 de n. è. env.", "Arrestation de Jean ; Jésus s'installe à Capharnaüm (Mt 4:12-13)"),
  ("30-32 de n. è.", "Le ministère galiléen : Mt 4:23-25, les foules des cinq régions"),
  ("31 de n. è. env.", "Les douze choisis près de Capharnaüm, Galiléens pour la plupart"),
 ],
 hist=(
  "2 Rois 15:29 nomme les victimes : « tout le pays de Nephtali » — les mêmes "
  "noms que l'oracle, huit siècles avant Matthieu. 1 Rois 9:11 explique la mixité : "
  "Salomon paie Hiram en villes galiléennes. Le bureau des impôts de Capharnaüm "
  "(Mt 9:9) suppose un poste-frontière : la ville est à la limite de la Galilée "
  "d'Antipas et de la Gaulanitide de Philippe, sur la route de Damas — le "
  "« cercle des nations » en acte. L'économie du lac (pêche, salaisons, batellerie) "
  "explique que quatre pêcheurs deviennent « pêcheurs d'hommes »."
 ),
 geo=(
  "Le lac de Galilée — 21 kilomètres sur 12, à 212 mètres au-dessous de la mer, "
  "eau douce et poissonneuse — est le centre du monde de la fiche. Capharnaüm "
  "(Tell Hum, probablement) occupe la rive nord, en Nephtali, près de la frontière "
  "de Zabulon : les deux tribus de l'oracle. La Via Maris passe à proximité ; la "
  "Décapole hellénistique borde la rive orientale. La Galilée, à son maximum une "
  "centaine de kilomètres sur cinquante, embrasse Aser, Issacar, Nephtali et "
  "Zabulon : toute la carte tient dans un week-end de marche."
 ),
 sci=(
  "Les fouilles de Capharnaüm ont livré la synagogue de basalte du Ier siècle "
  "sous la blanche du IVe, et la « maison de Pierre » devenue lieu de culte très "
  "tôt (graffiti, puis église octogonale). La « barque de Galilée », coque de pêche "
  "du Ier siècle découverte en 1986 dans la vase et datée par le carbone 14 et la "
  "céramique associée, montre l'embarcation-type des disciples. Les poids de filets, "
  "hameçons et salaisons retrouvés autour du lac confirment l'économie de la pêche "
  "décrite par les Évangiles."
 ),
 limites=(
  "L'identification Capharnaüm = Tell Hum est quasi certaine (toponymie arabe "
  "Kefar Nahum, tradition, distance) mais sans inscription nominative : aucun "
  "« Capharnaüm » gravé n'a été trouvé. La « maison de Pierre » est un lieu vénéré "
  "très tôt, pas une adresse certifiée. La barque de 1986 est une barque du temps "
  "de Jésus, pas la barque de Jésus. Les chiffres de population de la Galilée "
  "chez Josèphe sont manifestement exagérés et ne sont pas repris ici."
 ),
 tl=[("733", "Ténèbres assyriennes"), ("VIIIe s.", "Ésaïe 9"), ("30 env.", "Capharnaüm"),
     ("30-32", "Lumière : foules"), ("31 env.", "Les douze")],
 src=[("Matthieu 4 — le texte (Capharnaüm, la lumière)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001061144"),
      ("Galilée — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011560"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 9 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/9")],
 img="images/prophe_C008_galilee.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C009", titre="Le prophète comme Moïse — écoutez-le",
 ref="Deutéronome 18:15-19 ; Actes 3:22-23 ; Jean 1:45 ; 6:14 ; 7:40 ; Matthieu 17:5",
 statut="Accomplie",
 cat="C", syst="Système 1473/29",
 reg="Registre : Deutéronome — P058 (18:15-19)",
 texte=[
  "« Jéhovah ton Dieu te suscitera d'entre tes frères un prophète comme moi : "
  "vous l'écouterez. » (Dt 18:15)",
  "« Je mettrai mes paroles dans sa bouche, et il leur dira tout ce que je lui "
  "ordonnerai. » (Dt 18:18)",
  "« Celui-ci est mon Fils bien-aimé : écoutez-le. » (Mt 17:5, la voix sur la "
  "montagne, reprenant Dt 18:15)",
  "« Toute âme qui n'écoutera pas ce Prophète sera exterminée du milieu du "
  "peuple. » (Ac 3:23, Pierre citant Moïse)",
 ],
 contexte=(
  "Moïse parle dans les plaines de Moab, en 1473, à la veille de l'entrée en "
  "Canaan. Le peuple, qui avait supplié à Horeb de ne plus entendre directement "
  "la voix de Dieu (Dt 18:16), reçoit un médiateur pour toujours : après Moïse, "
  "un prophète « comme » lui. Quinze siècles plus tard, Philippe dit à Nathanaël : "
  "« Nous avons trouvé celui dont Moïse a écrit » (Jn 1:45) ; la foule rassasiée "
  "s'écrie : « C'est vraiment le Prophète » (Jn 6:14) ; et Pierre, à la Pentecôte, "
  "applique l'oracle à Jésus ressuscité."
 ),
 explication=(
  "« Comme moi » : médiateur d'une alliance, législateur, libérateur, faiseur de "
  "signes — le parallèle est de fonction, pas de biographie. « D'entre tes frères » : "
  "Israélite, pas devin étranger — l'oracle suit immédiatement l'interdit de la "
  "divination (Dt 18:9-14) : à la magie païenne, Dieu oppose la parole mise « dans "
  "sa bouche ». Le critère du vrai prophète suit (18:22) : ce qu'il dit arrive. "
  "« Écoutez-le » devient la formule de la transfiguration (Mt 17:5) : Dieu lui-même "
  "renvoie à Moïse. Et Jean-Baptiste, interrogé, nie être « le Prophète » "
  "(Jn 1:21) : l'attente distinguait le Christ, Élie et le Prophète — trois "
  "figures, dont Jésus remplit deux."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus est « le Grand Moïse » : "
  "prophète (il prédit la ruine du temple, les guerres, la fin), médiateur (de la "
  "nouvelle alliance, comme Moïse de la Loi), libérateur (d'un salut éternel, "
  "comme Moïse d'un salut hors d'Égypte). Les publications relèvent que Jésus "
  "lui-même a attesté le Deutéronome en le citant trois fois contre Satan "
  "(Mt 4). Pierre applique la sanction de l'oracle — « exterminée du milieu du "
  "peuple » — à la génération qui refuse d'écouter : voir B007 pour 70."
 ),
 accomplissement=[
  ("1473 av. n. è.", "Moïse annonce le Prophète dans les plaines de Moab"),
  ("Ier s. av. n. è.", "4QTestimonia : Qumrân cite Dt 18:18-19 dans une anthologie messianique"),
  ("29 de n. è.", "Baptême ; Philippe : « celui dont Moïse a écrit » (Jn 1:45)"),
  ("32 de n. è. env.", "Transfiguration : « écoutez-le » (Mt 17:5) ; les pains : « le Prophète » (Jn 6:14)"),
  ("33 de n. è.", "Pierre à la Pentecôte applique Dt 18 à Jésus (Ac 3:22-23)"),
 ],
 hist=(
  "L'attente est attestée avant Jésus. Le manuscrit 4QTestimonia, de Qumrân "
  "(Ier siècle avant notre ère), aligne Deutéronome 18:18-19 avec Nombres 24:17 "
  "et Deutéronome 33 : un florilège messianique qui prouve que l'oracle était lu "
  "comme messianique avant le christianisme. Les Samaritains attendaient le Taheb, "
  "le prophète-restaurateur fondé sur ce même texte — la Samaritaine du puits "
  "s'en fait l'écho (Jn 4:25 : « je sais que le Messie vient »). Jésus cite le "
  "Deutéronome contre le Tentateur : le Prophète authentifie le livre qui "
  "l'annonce."
 ),
 geo=(
  "L'oracle naît face à Canaan, dans les plaines de Moab, au pied du Nebo où Moïse "
  "va mourir sans entrer : le Prophète promis entrera, lui, et fera entrer. Il "
  "renvoie à Horeb, « le jour de l'assemblée » (Dt 18:16) : le Sinaï de la peur "
  "devient la promesse d'une parole audible. Quinze siècles plus tard, la "
  "formule résonne sur une « haute montagne » de Galilée (Mt 17:1) puis au Temple "
  "de Jérusalem (Ac 3:11, le portique de Salomon) : du désert à la ville sainte, "
  "la boucle est bouclée."
 ),
 sci=(
  "La critique textuelle confirme la stabilité de l'oracle : texte massorétique, "
  "Pentateuque samaritain, Septante et manuscrits de Qumrân convergent sur "
  "Deutéronome 18:15-19, sans variante qui en affaiblisse la portée. 4QTestimonia "
  "fournit la preuve matérielle de la lecture messianique pré-chrétienne : le "
  "texte était souligné avant d'être accompli. La datation interne du Deutéronome "
  "(« un peu plus de deux mois », plaines de Moab) appartient au système "
  "chronologique de la fiche."
 ),
 limites=(
  "« Le Prophète » avec majuscule est le titre que la foule donne (Jn 6:14 ; 7:40), "
  "pas un titre que Jésus revendique : il se dit « fils de l'homme » et laisse "
  "les œuvres parler. Jean-Baptiste nie être le Prophète (Jn 1:21) : l'attente du "
  "Ier siècle distinguait des figures que les Évangiles répartissent autrement. "
  "La date de 1473 appartient à la chronologie biblique (système de la fiche), "
  "non aux chronologies profanes. La sanction d'Actes 3:23 ne date aucun événement "
  "à venir."
 ),
 tl=[("1473", "Moïse annonce"), ("Ier s. av.", "4QTestimonia"), ("29", "« Celui de Moïse »"),
     ("32 env.", "« Écoutez-le »"), ("33", "Pierre applique")],
 src=[("Reconnaissons Jésus comme le Grand Moïse", "https://wol.jw.org/fr/wol/d/r30/lp-f/2009283"),
      ("Deutéronome (livre du) — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011134"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Deutéronome 18 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/5/18")],
 img="images/prophe_C009_moise.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C010", titre="Les miracles — la réponse à Jean en prison",
 ref="Ésaïe 35:5-6 ; Matthieu 11:2-6 ; Luc 7:18-23 ; Matthieu 15:30-31",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Ésaïe — P152 (35:1-10), P604 (35:5-6)",
 texte=[
  "« Alors les yeux des aveugles s'ouvriront, et les oreilles des sourds se "
  "déboucheront ; alors le boiteux sautera comme le cerf, et la langue du muet "
  "criera de joie. » (Is 35:5-6)",
  "« Les aveugles voient, les boiteux marchent, les lépreux sont purifiés, les "
  "sourds entendent, les morts sont relevés, et la bonne nouvelle est annoncée "
  "aux pauvres. » (Mt 11:5, réponse de Jésus aux envoyés de Jean)",
  "« Heureux celui pour qui je ne serai pas une occasion de trébucher ! » (Mt 11:6)",
 ],
 contexte=(
  "Jean est en prison à Machéronte (voir C005) quand il envoie deux disciples "
  "poser la question : « Es-tu celui qui vient, ou devons-nous en attendre un "
  "autre ? » Jésus ne répond ni oui ni non : il montre. « Allez rapporter à Jean "
  "ce que vous entendez et voyez » — puis la liste. Ésaïe 35, au sens premier, "
  "chante le retour de l'exil par une « route sainte » (35:8) ; Jésus en prélève "
  "les versets 5-6 comme pièces d'identité du Messie. Juste avant, il a relevé le "
  "fils de la veuve de Naïn (Lc 7:11-17) : les envoyés ont peut-être vu un mort "
  "relevé."
 ),
 explication=(
  "« Celui qui vient » (ho erchomenos), c'est le Psaume 118:26 — Jean demande si "
  "Jésus est le Béni-qui-vient. La réponse cite Ésaïe 35 en y ajoutant deux "
  "membres : les lépreux purifiés et les morts relevés — au-delà même de l'oracle. "
  "Chaque membre renvoie à des faits datés du ministère : l'aveugle-né (Jn 9), "
  "le sourd-muet de la Décapole (Mc 7:31-37, « Effata »), les boiteux de la montagne "
  "(Mt 15:30-31), les dix lépreux (Lc 17), le fils de Naïn, la fille de Jaïrus. "
  "Le dernier membre — « la bonne nouvelle aux pauvres » — est Ésaïe 61:1 (voir "
  "C007) : les deux manifestes se rejoignent dans une seule phrase."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus a prouvé par ses œuvres, "
  "et non par un titre revendiqué, qu'il était le Messie : les guérisons "
  "accomplissent Ésaïe 35 et Ésaïe 61 à la lettre — « complètement guéris », "
  "« aussitôt », devant témoins. L'avertissement final vaut pour tous, y compris "
  "dans l'épreuve : la foi tient même en prison. Et les publications voient dans "
  "ces guérisons le modèle du Royaume à venir — un monde sans hôpitaux ni "
  "pharmacies — dont cette fiche ne date pas l'avènement."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 35 : la route sainte et les sens rouverts"),
  ("30-32 de n. è.", "Naïn, Capharnaüm, la Décapole : morts relevés, aveugles, sourds, boiteux"),
  ("32 de n. è. env.", "De Machéronte, Jean envoie demander : « Es-tu celui qui vient ? »"),
  ("32 de n. è. env.", "La réponse par les faits : Matthieu 11:4-6"),
  ("33 de n. è.", "Lazare, relevé après quatre jours : le sceau (Jn 11)"),
 ],
 hist=(
  "Le contraste avec la médecine antique fait partie du dossier : à Épidaure, on "
  "incubait des rêves ; chez Hippocrate, on prescrivait des régimes ; Jésus "
  "guérit « aussitôt » et « complètement », y compris l'aveugle de naissance "
  "(Jn 9:1 — incurable avéré) et le lépreux exclu (Mc 1:40-44, avec renvoi au "
  "prêtre selon Lévitique 14). La piscine de Siloé, où l'aveugle-né va se laver "
  "(Jn 9:7), a été dégagée en 2004-2005 : un grand bassin à marches du Ier siècle "
  "avant notre ère, exactement au lieu dit par la tradition."
 ),
 geo=(
  "La carte des miracles est celle du ministère : Naïn en Galilée du sud (le fils "
  "de la veuve), Capharnaüm (la belle-mère, le paralytique, le serviteur du "
  "centurion), la Décapole païenne (le sourd-muet — et les foules qui glorifient "
  "« le Dieu d'Israël », Mt 15:31), Siloé à Jérusalem (l'aveugle-né), Béthanie "
  "(Lazare). Chaque lieu ajoute une pièce : ville juive, territoire païen, "
  "capitale, village ami — la lumière ne connaît pas de frontière."
 ),
 sci=(
  "Les fouilles de Siloé (2004-2005) ont confirmé le décor de Jean 9 : escaliers "
  "monumentaux, eau vive du tunnel d'Ézéchias (voir B006). Le vocabulaire médical "
  "de Luc — médecin (Col 4:14) — affleure dans les récits (« forte fièvre », "
  "Lc 4:38) : les diagnostics sont posés par un professionnel antique. La "
  "« lèpre » biblique (Lévitique 13-14) est une catégorie rituelle large, "
  "constatée par le prêtre : elle recouvre des affections diverses, pas "
  "nécessairement la maladie de Hansen moderne — la fiche ne fait pas de "
  "diagnostic rétrospectif."
 ),
 limites=(
  "Les miracles ne convertissent pas mécaniquement : les villes témoins refusent "
  "(Mt 11:20-24), et « malgré tant de miracles, ils ne croyaient pas » (Jn 12:37). "
  "Jean reçoit la réponse et sera pourtant exécuté : la preuve n'épargne pas "
  "l'épreuve. Ésaïe 35, au sens premier, chante le retour d'exil — la fiche le "
  "dit, et montre le second sens révélé par Jésus. La santé universelle du "
  "Royaume est promise sans date."
 ),
 tl=[("VIIIe s.", "Ésaïe 35"), ("30-32", "Miracles"), ("32 env.", "Question de Jean"),
     ("32 env.", "Réponse par les faits"), ("33", "Lazare")],
 src=[("Quels bienfaits l'Évangile peut-il vous procurer ? (Mt 11:5)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1992921"),
      ("La santé parfaite : les guérisons comme modèle", "https://wol.jw.org/fr/wol/d/r30/lp-f/101998483"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 35 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/35")],
 img="images/prophe_C010_miracles.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C011", titre="Les paraboles — j'ouvrirai ma bouche en illustrations",
 ref="Psaume 78:2 ; Matthieu 13:34-35 ; Marc 4:33-34 ; Ésaïe 6:9-10",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Psaumes — P548 (78:2), P601 (78:2)",
 texte=[
  "« J'ouvrirai ma bouche en paraboles ; je publierai des choses cachées depuis "
  "les temps anciens. » (Ps 78:2)",
  "« Jésus dit tout cela aux foules en paraboles, et sans parabole il ne leur "
  "parlait pas — afin que s'accomplisse ce qui avait été dit par le prophète. » "
  "(Mt 13:34-35)",
  "« C'est pourquoi je leur parle en paraboles : parce qu'en regardant ils "
  "regardent en vain, et qu'en entendant ils entendent en vain. » (Mt 13:13, "
  "citant Is 6:9-10)",
 ],
 contexte=(
  "Le Psaume 78 est d'Asaph — « Asaph le visionnaire » (2Ch 29:30), prophète et "
  "chantre de David : un psaume historique (l'Exode, le désert, David) ouvert par "
  "un verset qui déborde son auteur. Dix siècles plus tard, « ce jour-là » "
  "(Mt 13:1), Jésus sort s'asseoir au bord de la mer ; la foule est si grande "
  "qu'il monte dans une barque et enseigne du large : le semeur, l'ivraie, la "
  "moutarde, le levain, le trésor, la perle, le filet. Les disciples demandent : "
  "« Pourquoi leur parles-tu en paraboles ? »"
 ),
 explication=(
  "L'hébreu mashal (parabole, proverbe, énigme) devient le grec parabolê — "
  "« placer à côté » : rapprocher le ciel et la terre pour enseigner. Le verset "
  "de Matthieu 13:35 dit « depuis la fondation » (du monde) : les paraboles "
  "dévoilent des desseins voilés depuis l'origine. Double effet, expliqué par "
  "Jésus lui-même : révéler aux disciples (« il vous est donné de connaître », "
  "Mt 13:11) et voiler aux endurcis, selon Ésaïe 6 — les paraboles trient en "
  "enseignant. Asaph « prophète » : c'est le titre de l'auteur qui fait du verset "
  "une prophétie, pas seulement une préface."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus a accompli le Psaume 78:2 "
  "à la lettre : aux foules, il ne parlait qu'en illustrations — semeur (les "
  "cœurs), ivraie (les deux postérités), moutarde et levain (la croissance du "
  "Royaume), trésor et perle (le prix à payer), filet (le tri final). Les "
  "publications précisent le genre : les paraboles commencent par « un homme "
  "avait… » mais sortent de l'imagination inspirée — fictions d'enseignement, "
  "pas reportages. But premier : enseigner ; but second : décourager les "
  "superficiels, qui n'aiment pas creuser."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Asaph le visionnaire ouvre son psaume par le verset-prophétie"),
  ("31-32 de n. è.", "Le discours en paraboles : Mt 13, Mc 4, Lc 8 — la barque-chaire"),
  ("31-32 de n. è.", "Explications privées aux disciples : le voile se lève pour eux"),
  ("33 de n. è.", "Les paraboles du jugement : vignerons (Mt 21), noces (Mt 22), talents (Mt 25)"),
  ("33 de n. è.", "« Jamais homme n'a parlé comme cet homme » (Jn 7:46) : le constat des gardes"),
 ],
 hist=(
  "La parabole a une histoire avant Jésus : Nathan devant David (2S 12, la brebis "
  "du pauvre), Jotham devant Sichem (Jg 9, les arbres qui se choisissent un roi). "
  "Les rabbis maniaient le mashal ; Jésus s'en distingue par l'autorité — « mais "
  "moi, je vous dis » — qui stupéfie (Mt 7:28-29). Le cadre judiciaire confirme "
  "l'impact : les gardes envoyés pour l'arrêter reviennent bredouilles et "
  "témoignent malgré eux (Jn 7:32, 45-46) — un aveu adverse, comme les prêtres "
  "de Matthieu 2 (voir C001)."
 ),
 geo=(
  "Les paraboles sont le paysage galiléen transfiguré : le champ du semeur, "
  "l'ivraie des blés, la moutarde des bords du lac, le levain des cuisines, le "
  "trésor des labours, la perle des marchands, le filet des pêcheurs. La barque "
  "au large et la foule sur la plage (Mt 13:2) forment un amphithéâtre naturel : "
  "l'eau calme porte la voix. Synagogues, routes, puits, vignes — chaque décor "
  "devient une page."
 ),
 sci=(
  "L'acoustique lacustre est réelle : une voix portant sur l'eau calme atteint une "
  "foule massée en pente douce — la configuration de Mt 13:2 est un dispositif "
  "oratoire. La botanique confirme le décor : la moutarde noire (Brassica nigra), "
  "graine d'un millimètre, monte à trois mètres et abrite les oiseaux. "
  "L'agronomie explique le semeur : semailles à la volée avant le labour — la "
  "semence « le long du chemin » n'est pas une maladresse du paysan, c'est la "
  "méthode du temps."
 ),
 limites=(
  "« La plus petite de toutes les semences » est une expression proverbiale du "
  "Ier siècle, pas un traité de botanique : il existe des graines plus petites "
  "(orchidées), et la fiche le dit. Les paraboles sont des fictions inspirées, "
  "pas des faits divers : le trésor caché et la perle n'ont jamais été trouvés. "
  "« Sans parabole il ne leur parlait pas » vise les foules : aux disciples, en "
  "privé, « il expliquait tout » (Mc 4:34)."
 ),
 tl=[("Xe s.", "Asaph : Ps 78:2"), ("31-32", "Barque-chaire"), ("31-32", "Explications privées"),
     ("33", "Paraboles du jugement"), ("33", "« Jamais homme… »")],
 src=[("Illustrations (paraboles) — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012098"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Psaume 78 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/78"),
      ("Matthieu 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/13")],
 img="images/prophe_C011_paraboles.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C012", titre="Le Serviteur doux — le roseau froissé",
 ref="Ésaïe 42:1-4, 6-7 ; Matthieu 12:15-21 ; Matthieu 3:16-17 ; Marc 3:7-12",
 statut="Accomplie",
 cat="C", syst="Système 29/33/36",
 reg="Registre : Ésaïe — P158 (42:1-9), P598 (42:1-4), P612 (42:6-7)",
 texte=[
  "« Voici mon serviteur que je soutiens, mon élu en qui mon âme prend plaisir : "
  "j'ai mis mon esprit sur lui ; il fera connaître la justice aux nations. » "
  "(Is 42:1)",
  "« Il ne criera pas, il n'élèvera pas la voix, il ne la fera pas entendre dans "
  "la rue. Il ne brisera pas le roseau froissé, il n'éteindra pas la mèche qui "
  "fume. » (Is 42:2-3)",
  "« Celui-ci est mon Fils bien-aimé, en qui j'ai pris plaisir. » (Mt 3:17 — la "
  "voix du baptême, combinant Ps 2:7 et Is 42:1)",
 ],
 contexte=(
  "Premier des quatre « chants du Serviteur » (Ésaïe 42, 49, 50, 52-53). Matthieu "
  "le cite — sa plus longue citation d'Ésaïe — à un moment précis : après la "
  "guérison de l'homme à la main desséchée, un sabbat, les pharisiens complotent ; "
  "Jésus se retire, guérit tous les malades des foules, et « leur défend sévèrement "
  "de le faire connaître » (Mt 12:16). Le silence ordonné accomplit le silence "
  "annoncé : « il ne criera pas ». Serviteur puissant et doux — les deux à la fois."
 ),
 explication=(
  "Trois titres en un verset : serviteur (mission), élu (choix), bien-aimé "
  "(amour) — et la voix du baptême les reprend en y ajoutant « Fils » (Ps 2:7). "
  "« Il ne criera pas » : pas de démagogie, pas de zélotisme, pas de campagne — "
  "le contraire du tribun. Le roseau froissé (plante frêle des marais, une fois "
  "pliée bonne à jeter) et la mèche de lin qui fume (la lampe à huile au bord de "
  "s'éteindre) figurent les broyés : l'homme à la main desséchée, les foules "
  "éreintées, tous ceux dont la dernière étincelle vacille. « Jusqu'à ce qu'il "
  "fasse triompher la justice » : la douceur n'exclut pas le tri — elle en est "
  "le chemin."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus est ce Serviteur : oint "
  "d'esprit au baptême, il fait connaître la justice « aux nations » — et déjà "
  "les foules viennent de la Décapole, de Tyr et de Sidon (Mc 3:7-8 ; Mt 15). "
  "Il relève les humbles avec tendresse au lieu d'achever les vacillants : "
  "enfants bénis, péagers accueillis, malade de trente-huit ans relevé. Douceur "
  "qui n'est pas mollesse : aux broyeurs — scribes et pharisiens qui « écrasent » "
  "le peuple (Mt 23:4) — il oppose la fermeté. Les nations « espéreront en son "
  "nom » : Corneille, en 36, ouvre la porte (Ac 10)."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 42 : le premier chant du Serviteur"),
  ("29 de n. è., automne", "Baptême : l'esprit descend, la voix cite le Serviteur (Mt 3:16-17)"),
  ("30-32 de n. è.", "Retraits, guérisons, silence ordonné : « il ne criera pas » (Mt 12)"),
  ("33 de n. è.", "L'entrée humble (voir C006) ; le silence devant les juges (voir catégorie D)"),
  ("36 de n. è.", "Corneille : les nations entrent dans l'espérance (Ac 10)"),
 ],
 hist=(
  "La lecture messianique du Serviteur précède le christianisme : le Targum "
  "Jonathan, paraphrase araméenne des prophètes (Ier-IIe siècle), rend Ésaïe 52:13 "
  "par « voici que mon serviteur, le Messie, prospérera » — les synagogues "
  "entendaient le Serviteur comme Messie avant Jésus. Les foules mêlées de Marc "
  "3:7-8 (Galilée, Judée, Idumée, Transjordanie, Tyr, Sidon) montrent la justice "
  "« aux nations » en marche. Le « secret messianique » (silence ordonné) a sa "
  "logique : l'heure n'est pas venue, et le zèle politique guette."
 ),
 geo=(
  "Le Serviteur est annoncé à Jérusalem, oint au Jourdain, manifesté en Galilée, "
  "accueilli jusqu'en Phénicie païenne (la Cananéenne, Mt 15:21-28 — « même les "
  "petits chiens », et sa fille guérie). « Les îles » et « les côtes lointaines » "
  "d'Ésaïe 42:4, 10 dessinent l'horizon : la douceur du Serviteur n'a pas de "
  "frontière. Le Jourdain du baptême, les synagogues de Galilée, les maisons de "
  "Capharnaüm : la justice aux nations commence dans les bourgs."
 ),
 sci=(
  "La botanique confirme la métaphore : le roseau commun (Phragmites) des marais "
  "du Houlé et du Jourdain, une fois froissé, ne se redresse pas — le geste de ne "
  "pas l'achever est une délicatesse réelle. L'archéologie domestique montre "
  "l'objet de la seconde image : les lampes à huile du Ier siècle, avec leurs "
  "mèches de lin, sont les artefacts les plus courants des fouilles — chaque "
  "auditeur tenait la métaphore entre ses mains. La main « desséchée » (atrophie) "
  "guérie instantanément un sabbat (Mt 12:10-13) joint le dossier médical."
 ),
 limites=(
  "« Mon serviteur » désigne aussi, en Ésaïe, Israël collectif (Is 41:8 ; 44:1) "
  "et même Cyrus, « oint » pour une tâche politique (Is 45:1, voir B004) : la fiche "
  "distingue les serviteurs — le Serviteur individuel des chants n'est ni la "
  "nation ni le Perse. Le silence ordonné aux guéris est une pédagogie du temps, "
  "pas de la peur. L'année 36 (Corneille) appartient au système chronologique de "
  "la fiche. Le Serviteur souffrant (Is 52-53) attend la catégorie D."
 ),
 tl=[("VIIIe s.", "Ésaïe 42"), ("29", "Baptême : la voix"), ("30-32", "« Il ne crie pas »"),
     ("33", "Douceur jusqu'au bout"), ("36", "Corneille : les nations")],
 src=[("Il accomplit une prophétie d'Ésaïe (le Serviteur)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986609"),
      ("N'éteignez pas la mèche de lin qui fume !", "https://wol.jw.org/fr/wol/d/r30/lp-f/1995846"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 42 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/42")],
 img="images/prophe_C012_serviteur.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C013", titre="Il a porté nos maladies — les soirées de Capharnaüm",
 ref="Ésaïe 53:4 ; Matthieu 8:16-17 ; Marc 1:32-34 ; Luc 4:40-41 ; 1 Pierre 2:24",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Ésaïe — P603 (53:4) ; le reste du chant : catégorie D",
 texte=[
  "« Pourtant, ce sont nos maladies qu'il a portées, et nos douleurs dont il "
  "s'est chargé. » (Is 53:4a)",
  "« Le soir venu, on lui amena beaucoup de démoniaques ; il chassa les esprits "
  "par sa parole et guérit tous les malades — afin que s'accomplisse ce qui avait "
  "été dit par Ésaïe : Il a pris nos infirmités et porté nos maladies. » "
  "(Mt 8:16-17)",
  "« Toute la ville était rassemblée devant la porte. » (Mc 1:33)",
 ],
 contexte=(
  "Un soir de sabbat à Capharnaüm : le matin, Jésus a guéri un démoniaque à la "
  "synagogue puis la belle-mère de Pierre ; au coucher du soleil — la fin du "
  "sabbat, on peut de nouveau porter les malades — « toute la ville » afflue à "
  "la porte de la maison. Marc, Luc et Matthieu racontent la même soirée ; seul "
  "Matthieu la commente par Ésaïe 53:4. Le verset appartient au quatrième chant "
  "du Serviteur, celui du Serviteur souffrant : Matthieu en prélève le début "
  "pour les guérisons, avant la croix. Le reste du chant — versets 5 à 12 — "
  "attend la catégorie D."
 ),
 explication=(
  "« Porter » (deux verbes hébreux : porter, se charger) dit le fardeau assumé : "
  "le Serviteur ne guérit pas de loin, il s'en charge. « Maladies » et « douleurs » "
  "couvrent le corps et l'âme — holisme hébreu : la fièvre de la belle-mère et "
  "l'oppression des démoniaques relèvent du même verbe. « Par sa parole » : pas "
  "de rite, pas d'incantation — l'autorité nue. Deux applications, un Serviteur : "
  "Matthieu applique le verset 4 aux guérisons du ministère, Pierre l'appliquera "
  "à la croix (1P 2:24, « par ses meurtrissures vous avez été guéris »). La fiche "
  "tient les deux bouts sans les confondre."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que les guérisons de Jésus "
  "accomplissent Ésaïe 53:4 au sens propre : il « porte » les maladies en "
  "compatissant — « ému de pitié » devant le lépreux (Mc 1:41), en pleurs devant "
  "le tombeau de Lazare (Jn 11:35) : le Porteur pleure avec les porteurs. Les "
  "esprits chassés « par sa parole » montrent le Royaume envahissant le territoire "
  "de Satan (Mt 12:28). Et ces soirées de Capharnaüm sont des arrhes : la santé "
  "que le Royaume donnera à tous, Jésus la donne déjà à quelques-uns — sans date "
  "pour le « tous »."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 53:4 : le Serviteur porteur, dans le chant du Souffrant"),
  ("30 de n. è. env.", "Capharnaüm : la synagogue, la belle-mère, puis la soirée à la porte (Mc 1)"),
  ("30-32 de n. è.", "Les soirées de guérisons : Mt 8, Mc 1, Lc 4 — « tous » guéris"),
  ("33 de n. è.", "Lazare : le Porteur pleure, puis ordonne (Jn 11)"),
  ("33 de n. è.", "La croix : 1 Pierre 2:24 reprend le même verset (voir catégorie D)"),
 ],
 hist=(
  "Le contraste antique est total : à Épidaure, les malades dormaient dans le "
  "temple d'Asclépios en espérant un rêve ; Jésus guérit « tous » en une soirée, "
  "démons compris, « par sa parole ». Le lépreux guéri est renvoyé au prêtre "
  "« selon ce que Moïse a prescrit » (Mc 1:44, Lv 14) : la guérison réintègre dans "
  "la communauté et dans le culte. Luc, le médecin (Col 4:14), précise « une forte "
  "fièvre » (Lc 4:38) : le diagnostic d'un professionnel antique, guéri en un "
  "instant."
 ),
 geo=(
  "Tout se joue à Capharnaüm, « sa ville » (voir C008) : la synagogue le matin, "
  "la maison de Pierre le soir, la porte où « toute la ville » s'entasse. Le lac "
  "fournit la suite : juste après Matthieu 8:17, Jésus apaise la tempête — le "
  "Porteur des maladies commande aussi aux vents. Maison, porte, lac : la "
  "géographie d'une soirée qui contient le ministère entier."
 ),
 sci=(
  "Les « fortes fièvres » du bord du lac évoquent le paludisme des zones "
  "marécageuses (le Houlé) : endémie plausible, guérison instantanée. La « lèpre » "
  "de Lévitique 13-14 est une catégorie rituelle constatée par le prêtre, "
  "recouvrant des dermatoses diverses — pas nécessairement la maladie de Hansen : "
  "la fiche ne pose pas de diagnostic rétrospectif. L'architecture vérifie un "
  "détail : le paralytique descendu « à travers le toit » (Mc 2:4) suppose des "
  "toits de branchages et de terre — exactement ceux des maisons fouillées à "
  "Capharnaüm."
 ),
 limites=(
  "Ésaïe 53:4 a deux applications scripturaires — les guérisons (Mt 8:17) et la "
  "croix (1P 2:24) : cette fiche traite la première et renvoie la seconde, avec "
  "les versets 5 à 12, à la catégorie D. « Lèpre » n'est pas un diagnostic moderne. "
  "Les guérisons sont des signes pour quelques-uns, pas encore la santé pour "
  "tous : le « tous » définitif reste sans date. Les exorcismes sont rapportés "
  "comme des faits par les Évangiles ; la fiche ne les naturalise ni ne les "
  "psychologise."
 ),
 tl=[("VIIIe s.", "Ésaïe 53:4"), ("30 env.", "Soirée à la porte"), ("30-32", "« Tous » guéris"),
     ("33", "Lazare pleuré"), ("33", "La croix : 1P 2:24")],
 src=[("La santé parfaite : les guérisons comme modèle", "https://wol.jw.org/fr/wol/d/r30/lp-f/101998483"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 53 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/53"),
      ("Matthieu 8 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/8")],
 img="images/prophe_C013_maladies.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C014", titre="Le Nazaréen — il sera appelé de ce nom",
 ref="Matthieu 2:23 ; Ésaïe 11:1 ; Jérémie 23:5 ; 33:15 ; Zacharie 3:8 ; 6:12 ; Jean 1:46 ; 19:19",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Ésaïe 11:1 — P123 ; Mt 2:23 sans entrée dédiée (lacune signalée, C8) ; contexte Mt 2 : P590, P591",
 texte=[
  "« Il vint habiter dans une ville appelée Nazareth, afin que s'accomplisse ce "
  "que les prophètes avaient annoncé : Il sera appelé Nazaréen. » (Mt 2:23)",
  "« Un rameau sortira de la souche de Jessé, un rejeton [nétsèr] de ses racines "
  "portera du fruit. » (Is 11:1)",
  "« De Nazareth peut-il sortir quelque chose de bon ? » (Jn 1:46, Nathanaël)",
  "« Jésus le Nazaréen, le roi des Juifs. » (Jn 19:19, l'écriteau de Pilate)",
 ],
 contexte=(
  "Au retour d'Égypte (voir C003), Joseph apprend qu'Archélaüs règne sur la Judée "
  "— un cruel qui a fait tuer 3 000 Juifs dans le Temple — et, averti par Dieu, "
  "installe sa famille à Nazareth, en Galilée, hors de sa juridiction. Matthieu "
  "conclut : « afin que s'accomplisse… Il sera appelé Nazaréen ». L'énigme est "
  "célèbre : aucun verset de l'Ancien Testament ne contient cette formule. "
  "Matthieu cite « les prophètes » — au pluriel : il résume, il ne cite pas."
 ),
 explication=(
  "Trois pistes, données ici avec leur poids. (1) Le rejeton : l'hébreu nétsèr "
  "(Is 11:1) désigne le Messie-rejeton de Jessé ; Matthieu, parlant au pluriel, "
  "pensait peut-être aussi à la « pousse juste » de Jérémie (Jr 23:5 ; 33:15) et "
  "au « Germe » de Zacharie (Za 3:8 ; 6:12) — et Nazareth signifie probablement "
  "« ville-rejeton ». Paronomase : le Rejeton habite la ville-rejeton. (2) Le "
  "mépris : les Nazaréens étaient méprisés — « de Nazareth, rien de bon » "
  "(Jn 1:46) — et le Méprisé annoncé (Is 53:3) trouve son surnom de mépris. (3) Le "
  "surnom devenu titre : « Nazaréen » colle à Jésus (Mc 1:24, jusque dans la "
  "bouche des démons), à l'écriteau trilingue (Jn 19:19), puis aux disciples "
  "(Ac 24:5, « la secte des Nazaréens »)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah retient la première piste : l'allusion "
  "à Ésaïe 11:1 — le Messie-nétsèr, rejeton de Jessé — élargie aux « pousses » de "
  "Jérémie et de Zacharie, puisque Matthieu parle des prophètes au pluriel. "
  "Nazareth, « ville-rejeton », reçoit le Rejeton : la géographie accomplit le "
  "vocabulaire. Le surnom suit Jésus jusqu'au gibet, où Pilate l'affiche en "
  "hébreu, latin et grec — le mépris proclamé en trois langues — puis aux "
  "chrétiens eux-mêmes, « Nazaréens » aux yeux du monde."
 ),
 accomplissement=[
  ("VIIIe-VIe s. av. n. è.", "Is 11:1, Jr 23:5, Za 3:8 et 6:12 : le Rejeton, la Pousse, le Germe"),
  ("1 av. n. è. env.", "Installation à Nazareth : le Rejeton dans la ville-rejeton (Mt 2:23)"),
  ("29-32 de n. è.", "« Jésus le Nazaréen » : foules, démons (Mc 1:24), juges — le surnom colle"),
  ("33 de n. è.", "L'écriteau trilingue : le Nazaréen proclamé roi (Jn 19:19-20)"),
  ("36+ de n. è.", "« La secte des Nazaréens » : le surnom passe aux disciples (Ac 24:5)"),
 ],
 hist=(
  "L'obscurité de Nazareth est elle-même un document : le bourg n'est nommé ni "
  "dans l'Ancien Testament, ni chez Josèphe qui liste les villes galiléennes, ni "
  "dans les anciennes sources rabbiniques — le mépris de Nathanaël a une base "
  "administrative. Le nom est pourtant gravé : l'inscription de Césarée (IIIe "
  "siècle de notre ère), liste sacerdotale, mentionne la famille d'Happitses "
  "résidant à Nazareth. L'écriteau trilingue de Jean 19:20 correspond à la pratique "
  "romaine du titulus affichant le motif de la condamnation."
 ),
 geo=(
  "Nazareth : une cuvette de Basse-Galilée, à l'écart de la Via Maris — "
  "l'obscurité géographique fait le mépris. À six kilomètres, Sephoris, capitale "
  "d'Antipas en chantier : le charpentier grandit à une heure de marche d'une cour "
  "royale qui l'ignore — contexte, pas récit (voir Limites). Capharnaüm est à "
  "vingt-cinq kilomètres au nord-est, Jérusalem à une centaine au sud : le "
  "Nazaréen devra marcher pour être entendu."
 ),
 sci=(
  "Les fouilles de Nazareth (maisons à cour du Ier siècle, citernes, pressoirs, "
  "silos, kokhim) confirment un bourg juif rural et pieux — le décor du mépris "
  "comme celui de l'enfance. Une maison du Ier siècle à flanc de coteau, fouillée "
  "près de l'église, montre l'habitat-type : deux pièces, cour, citerne — "
  "l'ordinaire, pas le palais. L'inscription de Césarée (IIIe siècle) atteste le "
  "nom dans la pierre. Aucun rempart, aucun monument : l'archéologie confirme "
  "l'insignifiance — et c'est elle qui accomplit."
 ),
 limites=(
  "Aucun verset ne contient la formule exacte « il sera appelé Nazaréen » : la "
  "fiche ne prétend pas le contraire — c'est une synthèse des prophètes, au "
  "pluriel, pas une citation. Le lien nétsèr-Nazareth est une paronomase probable "
  "(« signifie probablement », dit la source), pas une étymologie certaine. La "
  "piste du mépris (Is 53:3, Jn 1:46) est une lecture complémentaire proposée par "
  "des commentateurs, pas une position tranchée ici. Sephoris est un contexte "
  "géographique, jamais un lieu évangélique."
 ),
 tl=[("VIIIe-VIe s.", "Le Rejeton promis"), ("1 env.", "Nazareth"), ("29-32", "« Le Nazaréen »"),
     ("33", "L'écriteau"), ("36+", "« Secte des Nazaréens »")],
 src=[("Notes d'étude sur Matthieu 2:23 (nétsèr, les prophètes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001070602"),
      ("Branche, germe, rejeton — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000811"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Matthieu 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/2")],
 img="images/prophe_C014_nazareen.jpg",
))
