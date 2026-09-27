#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE D (1re partie) — LE MESSIE : PROCES, MORT, RESURRECTION
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="D",
    nom="Le Messie : procès, mort, résurrection (1re partie)",
    vague="5",
    intro=(
        "Neuf fiches pour la semaine décisive : le prix du Berger (trente pièces), "
        "le Psaume 22 crié à Golgotha, le Serviteur souffrant d'Ésaïe 53, l'agneau "
        "aux os intacts et le côté percé, la trahison de l'ami, le silence et les "
        "sévices du procès, la pierre rejetée devenue faîtière, la résurrection du "
        "troisième jour, et la droite de Dieu. Trois remarques de méthode valent "
        "pour toute la catégorie : stauros est rendu « poteau de supplice » selon "
        "son sens premier (voir l'article cité) ; le lieu exact de Golgotha et du "
        "tombeau n'est tranché dans aucune fiche ; et le linceul de Turin, daté du "
        "XIVe siècle par le carbone 14, n'entre dans aucun dossier. La 2e partie "
        "(vague 6) traitera le vinaigre (Ps 69:21), le berger frappé (Za 13:7) et "
        "le serpent d'airain (Nb 21)."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D001", titre="Les trente pièces — le prix d'un esclave",
 ref="Zacharie 11:12-13 ; Matthieu 26:14-16 ; 27:3-10 ; Exode 21:32 ; Jérémie 18-19 ; 32",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Zacharie — P507 (11:12-13), P614 (11:12), P615 (11:13)",
 texte=[
  "« Ils pesèrent mon salaire : trente pièces d'argent. Et Jéhovah me dit : "
  "Jette-le au trésor — le prix magnifique auquel j'ai été estimé à leurs yeux ! » "
  "(Za 11:12-13)",
  "« Que voulez-vous me donner, et je vous le livrerai ? Et ils lui comptèrent "
  "trente pièces d'argent. » (Mt 26:15)",
  "« Ils prirent les trente pièces d'argent, le prix de celui qui avait été mis "
  "à prix, et ils les donnèrent pour le champ du potier. » (Mt 27:9-10)",
  "« Si le bœuf frappe un esclave, on paiera trente sicles d'argent à son "
  "maître. » (Ex 21:32)",
 ],
 contexte=(
  "Zacharie 11 met en scène le Berger rejeté : deux bâtons, Faveur et Union, puis "
  "le salaire dérisoire et le bâton brisé — vers 520-518. Cinq siècles et demi "
  "plus tard, Judas Iscariote négocie avec les grands prêtres : le prix convenu "
  "tombe sans marchandage, comme un tarif connu. Après la condamnation, le "
  "remords : Judas rapporte l'argent dans le temple, le jette, et se pend "
  "(Mt 27:3-5). Les prêtres, qui refusent de mettre un « prix du sang » au trésor, "
  "achètent le champ d'un potier pour la sépulture des étrangers."
 ),
 explication=(
  "Trente sicles, c'est le tarif légal d'un esclave encorné (Ex 21:32) : le Berger "
  "d'Israël est estimé au prix d'un esclave — « le prix magnifique », dit Dieu "
  "avec ironie. « Jette-le au potier » ou « au trésor » : les deux lectures du "
  "verset 13 existent selon les manuscrits et versions ; elles convergent dans "
  "l'accomplissement — jetées dans le temple, les pièces achètent le champ du "
  "potier. Matthieu 27:9 attribue la citation à « Jérémie » alors que les trente "
  "pièces sont de Zacharie : il tisse en une seule formule Zacharie 11 (le prix), "
  "Jérémie 18-19 (le potier, Topheth) et Jérémie 32 (l'achat d'un champ) — "
  "combinaison signalée comme telle, voir Limites."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que le prophète Zacharie, établi "
  "berger par Jéhovah, préfigurait le Berger véritable : estimé trente pièces, "
  "comme un esclave. Les publications relèvent que ce sont les prêtres qui, "
  "ramassant l'argent jeté, « agissent à la place » de Judas pour l'achat — "
  "« ils les ont données pour le champ du potier ». Le champ, payé du prix du "
  "sang et affecté aux étrangers, devient Hakeldama, le « champ du sang » "
  "(Mt 27:8 ; Ac 1:19) : le toponyme araméen garde la facture."
 ),
 accomplissement=[
  ("520-518 av. n. è.", "Zacharie 11 : le Berger estimé trente pièces, bâton brisé"),
  ("33 de n. è., avant Pâque", "Judas négocie : trente pièces comptées sans débat (Mt 26:14-16)"),
  ("33 de n. è., 14 Nisan", "Arrestation à Gethsémani ; condamnation ; remords de Judas"),
  ("33 de n. è.", "L'argent jeté dans le temple ; pendaison de Judas (Mt 27:3-5)"),
  ("33 de n. è.", "Achat du champ du potier : Hakeldama, sépulture des étrangers"),
 ],
 hist=(
  "Exode 21:32 fournit le tarif : trente sicles pour un esclave — le salaire de "
  "Zacharie égale exactement le prix légal d'un homme acheté. Les trente "
  "« pièces d'argent » (arguria) sont vraisemblablement des sicles tyriens, la "
  "monnaie d'argent du tribut du Temple. Jérémie 18-19 situe le potier et Topheth "
  "dans la vallée de Hinnom : le champ acheté est dans le quartier des ateliers "
  "et du Topheth — la topographie de Jérémie recouvre celle de Matthieu. "
  "Hakeldama, nom araméen cité par les Actes, est le reçu toponymique de "
  "l'affaire."
 ),
 geo=(
  "Trois lieux tiennent l'affaire : le temple, où l'argent est jeté (Mt 27:5, "
  "jusque dans le naos) ; la vallée de Hinnom, au sud, quartier des potiers et "
  "de Topheth (Jr 19), où se trouve le champ ; et le champ lui-même, affecté aux "
  "étrangers — un cimetière d'immigrés et de pèlerins morts loin de chez eux, "
  "payé du prix du sang. Le Hakeldama traditionnel, sur le versant sud de "
  "Hinnom, garde le nom depuis l'Antiquité."
 ),
 sci=(
  "La métrologie confirme le tarif : le sicle judéen pèse environ 11,4 grammes — "
  "trente sicles représentent quelque 340 grammes d'argent, et les poids inscrits "
  "découverts en Juda attestent le système. La numismatique identifie le sicle "
  "de Tyr, à la chouette et au bonnet, comme la monnaie du tribut du Temple au "
  "Ier siècle : les pièces les plus probables du marché. Les fours de potiers "
  "antiques sont attestés autour de Jérusalem, et la céramique du Second Temple "
  "est l'artefact le plus daté des fouilles."
 ),
 limites=(
  "« Au potier » ou « au trésor » (Za 11:13) : la fiche donne les deux lectures "
  "et montre leur convergence, sans trancher la leçon primitive. « Jérémie » en "
  "Matthieu 27:9 pour un texte mêlant Zacharie et Jérémie : la fiche donne "
  "l'explication de la citation combinée et signale la difficulté au lieu de "
  "l'effacer. La mort de Judas est rapportée en deux récits complémentaires "
  "(pendaison, Mt 27:5 ; chute, Ac 1:18) : leur harmonisation reste une "
  "reconstruction. Le Hakeldama actuel est une tradition toponymique, pas une "
  "fouille probante."
 ),
 tl=[("520-518", "Zacharie 11"), ("33, av. Pâque", "Le marché"), ("14 Nisan", "Gethsémani"),
     ("14 Nisan", "L'argent jeté"), ("33", "Hakeldama")],
 src=[("Les conséquences du rejet du Berger (Za 11, Mt 27)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101972028"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Zacharie 11 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/11"),
      ("Matthieu 27 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/27")],
 img="images/prophe_D001_pieces.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D002", titre="Le Psaume 22 — crié à Golgotha",
 ref="Psaume 22 ; Matthieu 27:35-46 ; Marc 15:24-34 ; Luc 23:34-35 ; Jean 19:23-24",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P529 (22:1), P530 (22:6-8), P531 (22:14-16), P532 (22:17-18), P533 (22:22-31), P630-P634",
 texte=[
  "« Mon Dieu, mon Dieu, pourquoi m'as-tu abandonné ? » (Ps 22:1 ; Mt 27:46)",
  "« Tous ceux qui me voient se moquent de moi ; ils ricanent, ils hochent la "
  "tête : Qu'il s'en remette à Jéhovah, qu'il le délivre ! » (Ps 22:7-8 ; Mt 27:43)",
  "« Je suis comme de l'eau qu'on verse ; tous mes os se disloquent ; mon cœur "
  "est comme de la cire ; ma force est desséchée comme un tesson. » (Ps 22:14-15)",
  "« Ils ont percé mes mains et mes pieds. Ils se partagent mes vêtements et "
  "tirent au sort ma robe. » (Ps 22:16, 18 ; Jn 19:23-24)",
 ],
 contexte=(
  "David, vers le Xe siècle, compose une lamentation individuelle qui déborde son "
  "cas : aucun épisode de sa vie ne montre des mains percées ni des vêtements "
  "tirés au sort. Mille ans plus tard, à Golgotha, de la 3e heure (mise au poteau, "
  "Mc 15:25) à la 9e (la mort), chaque membre du psaume se joue : les moqueries "
  "des passants et des chefs, les ténèbres de midi à 15 heures, le cri en araméen, "
  "les soldats et la tunique. Jésus prie par le psautier jusque dans l'agonie."
 ),
 explication=(
  "Le cri n'est pas un désespoir : c'est la citation du verset 1, et le psaume "
  "s'achève en louange et en postérité (22:22-31, cité en Hé 2:12) — prier le "
  "début, c'est convoquer la fin. L'ironie de Matthieu 27:43 est parfaite : les "
  "chefs, citant le verset 8 (« qu'il le délivre, puisqu'il l'aime »), prouvent "
  "sans le savoir qu'ils jouent le psaume. « Ils ont percé » : l'hébreu massorétique "
  "porte « comme un lion » (kari), mais les Septante (IIe siècle avant notre ère) "
  "traduisent « ils ont percé », et le manuscrit du désert de Juda 5/6Hev "
  "(Nahal Hever, Ier siècle) porte karu, « ils ont percé » — témoin matériel "
  "pré-chrétien. La tunique sans couture, tissée d'une pièce, explique le sort : "
  "on ne déchire pas un vêtement de prix."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que David prophétisait la Passion "
  "au détail, mille ans d'avance et avant l'existence du supplice romain : le cri, "
  "les moqueries mot pour mot, la dislocation de la suspension, la soif, le "
  "percement, le partage. Stauros, le poteau de supplice, est un pieu vertical "
  "auquel on clouait les condamnés — mains et probablement pieds (Jn 20:25-27 ; "
  "Lc 24:39 ; Ps 22:16). La fin du psaume — « j'annoncerai ton nom à mes frères », "
  "les nations se tournant vers Jéhovah — accomplit la résurrection et la "
  "congrégation (voir D008, D009)."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "David compose le Psaume 22 : le juste percé et partagé"),
  ("IIe s. av. n. è.", "Les Septante : « ils ont percé » — lecture juive pré-chrétienne"),
  ("Ier s. de n. è.", "5/6Hev (Nahal Hever) : karu, « ils ont percé » — preuve matérielle"),
  ("33 de n. è., 14 Nisan", "3e-9e heure : moqueries, ténèbres, cri, mort ; la tunique tirée au sort"),
  ("33+ de n. è.", "Hébreux 2:12 reprend Ps 22:22 : la louange après l'agonie"),
 ],
 hist=(
  "Le dossier textuel est antérieur au christianisme : Septante du IIe siècle "
  "avant notre ère et manuscrit de Nahal Hever du Ier siècle s'accordent sur "
  "« ils ont percé ». Le supplice romain — mise au poteau, clous, exposition, "
  "partage des dépouilles par l'escouade — est documenté par les sources latines "
  "et l'archéologie. La tunique sans couture (chitôn araphos, Jn 19:23) est un "
  "tissage d'une pièce, vêtement de prix qu'on ne déchire pas : l'avarice des "
  "soldats accomplit le verset 18. Les chefs citant le verset 8 fournissent "
  "l'aveu adverse."
 ),
 geo=(
  "Golgotha, « lieu du crâne » en araméen : hors les murs, près d'une route "
  "(les passants injurient, Mt 27:39), visible (les connaissances « regardent », "
  "Lc 23:49), proche d'un jardin avec un tombeau neuf (Jn 19:41-42). Le Prétoire "
  "(Gabbatha) et le chemin de Simon de Cyrène complètent la carte. Deux "
  "traditions se disputent le lieu — Saint-Sépulcre intra-muros actuel, Jardin "
  "de la Tombe au nord : cette fiche ne tranche pas (voir Limites), et n'en a "
  "pas besoin."
 ),
 sci=(
  "L'ostéologie a tranché la réalité du supplice : en 1968 à Giv'at ha-Mivtar "
  "(Jérusalem), le talon d'un supplicié du Ier siècle (Yehohanan) a été retrouvé "
  "transpercé par un clou de 18 cm, tibias fracturés — clous et crurifragium "
  "attestés ensemble. La médecine de la suspension éclaire le verset 14-15 : "
  "asphyxie progressive, soif extrême (« langue collée »), dislocations. Le "
  "textile antique confirme les tuniques tissées d'une pièce. Chaque image du "
  "psaume a son correspondant matériel."
 ),
 limites=(
  "« Comme un lion / ils ont percé » (22:16) : la fiche donne les témoins des "
  "deux lectures — massorétique « comme un lion » contre Septante et 5/6Hev "
  "« ils ont percé » — au lieu d'en cacher une. Le cri n'est pas un désespoir : "
  "le psaume cité s'achève en louange (Hé 2:12). Golgotha exact non tranché "
  "(deux traditions). Poteau (stauros, pieu vertical) selon la Traduction du "
  "monde nouveau, avec l'article cité en source."
 ),
 tl=[("Xe s.", "Psaume 22"), ("IIe s. av.", "Septante : percé"), ("Ier s.", "5/6Hev : karu"),
     ("14 Nisan 33", "Golgotha, 3e-9e h"), ("33+", "Hé 2:12 : louange")],
 src=[("Mise au poteau — Étude perspicace (stauros, Ps 22:16)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012110"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Psaume 22 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/22"),
      ("Jean 19 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/19")],
 img="images/prophe_D002_psaume22.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D003", titre="Ésaïe 53 — le Serviteur souffrant",
 ref="Ésaïe 52:13-53:12 ; Actes 8:26-39 ; 1 Pierre 2:21-25 ; Matthieu 27:57-60 ; Jean 19:38-42",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Ésaïe — P170 (52:13-15), P171 (53:1-12), P618 (53:7), P624 (53:3) ; P603 traité en C013",
 texte=[
  "« Méprisé et abandonné des hommes, homme de douleurs, habitué à la souffrance ; "
  "nous l'avons méprisé, nous n'avons fait aucun cas de lui. » (Is 53:3)",
  "« Il était transpercé pour nos transgressions, écrasé pour nos fautes ; le "
  "châtiment qui nous donne la paix est tombé sur lui. » (Is 53:5)",
  "« Comme un agneau mené à l'abattoir, comme une brebis muette devant ses "
  "tondeurs, il n'a pas ouvert la bouche. » (Is 53:7)",
  "« On a mis sa sépulture avec les méchants, et avec le riche dans sa mort, "
  "bien qu'il n'ait pas commis de violence. » (Is 53:9)",
  "« Il verra une postérité, il prolongera ses jours ; par sa connaissance, mon "
  "serviteur justifiera beaucoup d'hommes. » (Is 53:10-11)",
 ],
 contexte=(
  "Quatrième chant du Serviteur (VIIIe siècle, même rouleau 1QIsa que C013). "
  "Peu après 33, sur la route déserte de Gaza, un haut fonctionnaire éthiopien — "
  "l'eunuque de la reine Candace — lit Ésaïe 53:7-8 dans son char et pose LA "
  "question : « De qui le prophète dit-il cela ? De lui-même, ou de quelqu'un "
  "d'autre ? » (Ac 8:34). Philippe, « commençant par ce passage, lui annonça la "
  "bonne nouvelle de Jésus » (Ac 8:35). Pierre, de son côté, tisse 1 Pierre 2 "
  "avec le chant entier."
 ),
 explication=(
  "Le chant est bâti en cinq strophes : triomphe annoncé (52:13-15 — « élevé », "
  "mais « défiguré »), rejet (53:1-3), substitution (53:4-6, voir C013), procès "
  "et mort (53:7-9), vindication (53:10-12). « Transpercé » (53:5) rejoint le "
  "Psaume 22:16 et Zacharie 12:10 : trois textes, un percement. Le verset 9 pose "
  "une énigme résolue en vingt-quatre heures : avec les méchants (Golgotha, entre "
  "deux malfaiteurs, Lc 23:32-33) ET avec le riche (le tombeau neuf de Joseph "
  "d'Arimathée). Les versets 10-11 annoncent la résurrection sans la nommer : "
  "« retranché » (53:8) puis « il verra… il prolongera ses jours » — la mort "
  "n'est pas la fin (voir D008)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah, avec Actes 8:35, est que le Serviteur "
  "souffrant, c'est Jésus : méprisé (53:3), muet au procès (53:7, voir D006), "
  "compté avec les transgresseurs (53:12), enseveli chez un riche (53:9) — "
  "Joseph d'Arimathée accomplissant la prophétie « sans s'en rendre compte ». "
  "Le Targum Jonathan, paraphrase juive (Ier-IIe siècle), entendait déjà « mon "
  "serviteur, le Messie » (cf. C012). « Il a porté les péchés de beaucoup » "
  "(53:12) fonde la rançon (Mt 20:28 ; 1Tm 2:6) : le Serviteur meurt à la place."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 52:13-53:12 : le Serviteur souffrant et vindicatif"),
  ("IIe s. av. n. è.", "1QIsa et les Septante : le chant est verrouillé avant Jésus"),
  ("33 de n. è., 14 Nisan", "Procès (53:8), silence (53:7), Golgotha entre malfaiteurs (53:9a, 53:12)"),
  ("33 de n. è., 14 Nisan", "Le tombeau neuf du riche Joseph (53:9b) — l'énigme résolue"),
  ("33 de n. è., 16 Nisan+", "« Il verra… il prolongera » (53:10-11) : la résurrection (voir D008)"),
 ],
 hist=(
  "Le grand rouleau 1QIsa (IIe siècle avant notre ère) contient le chant entier, "
  "sans rupture avec les chapitres 40-66 (voir B004) : deux cents ans minimum "
  "avant Golgotha. « Candace », le titre des reines de Méroé (Éthiopie antique), "
  "est attesté par les sources gréco-romaines : le fonctionnaire des Actes a un "
  "cadre réel. Joseph d'Arimathée, « membre éminent du Conseil » (Mc 15:43), "
  "fournit l'aveu adverse : c'est un notable du Sanhédrin qui offre le tombeau "
  "et les aromates — myrrhe et aloès, une centaine de livres (Jn 19:39), un "
  "ensevelissement de roi."
 ),
 geo=(
  "La route de Gaza (Ac 8:26, « désertique ») : c'est sur la piste du sud que "
  "l'eunuque lit et comprend — l'exégèse en char. Golgotha et le jardin (Jn 19:41) "
  "sont distants de quelques pas : les deux moitiés du verset 9 tiennent dans un "
  "périmètre. Arimathée, patrie de Joseph, est probablement Ramathaïm — "
  "identification incertaine (voir Limites). Le tombeau « neuf, taillé dans le "
  "roc, où personne n'avait encore été mis » (Mt 27:60 ; Lc 23:53) suppose un "
  "jardin privé de riche."
 ),
 sci=(
  "La datation de 1QIsa (paléographie et carbone 14, IIe siècle avant notre ère) "
  "place le chant deux siècles avant le christianisme : l'antériorité est "
  "physique. Les tombeaux rupestres du Ier siècle autour de Jérusalem — chambres à "
  "banquettes, enfeus (kokhim), pierre roulée (golel) — correspondent au tombeau "
  "de Matthieu 27:60 au détail architectural. Les aromates (une centaine de "
  "livres romaines, soit plus de trente kilos) supposent un ensevelissement "
  "massif, incompatible avec un corps volé à la hâte (voir D008)."
 ),
 limites=(
  "« Avec le riche » (53:9) : l'hébreu porte un singulier, accompli en Joseph — "
  "la fiche le dit simplement, sans surtraduire. « Il a plu à Jéhovah de "
  "l'écraser » (53:10) : mystère de la volonté divine, cité et non disséqué. "
  "Arimathée n'est pas localisée avec certitude. Le tombeau exact n'est pas "
  "tranché (Saint-Sépulcre ou Jardin de la Tombe, cf. D002). Le verset 4 a été "
  "traité en C013 (guérisons) : deux applications, un Serviteur — sans confusion."
 ),
 tl=[("VIIIe s.", "Ésaïe 53"), ("IIe s. av.", "1QIsa verrouille"), ("14 Nisan 33", "Golgotha + tombeau"),
     ("16 Nisan 33", "« Il verra »"), ("33+", "L'eunuque comprend")],
 src=[("La sépulture avec les méchants et avec les riches (Is 53:9)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/1200027501/36/2"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 53 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/53"),
      ("Actes 8 — Bible d'étude, notes (l'eunuque)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/8")],
 img="images/prophe_D003_serviteur.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D004", titre="L'agneau intact — aucun os brisé, le côté percé",
 ref="Exode 12:46 ; Nombres 9:12 ; Psaume 34:20 ; Zacharie 12:10 ; Jean 19:31-37 ; 1 Corinthiens 5:7",
 statut="Accomplie",
 cat="D", syst="Système 1513/33",
 reg="Registre : Exode — P629 (12:46) ; Psaumes — P536, P636 (34:20) ; Zacharie — P509, P638 (12:10)",
 texte=[
  "« On ne brisera aucun de ses os. » (Ex 12:46 — l'agneau pascal ; Nb 9:12)",
  "« Il garde tous ses os ; aucun d'eux n'est brisé. » (Ps 34:20 — le juste délivré)",
  "« Venus à Jésus, et le voyant déjà mort, ils ne lui brisèrent pas les jambes ; "
  "mais un des soldats lui perça le côté avec une lance, et aussitôt il sortit "
  "du sang et de l'eau. » (Jn 19:33-34)",
  "« Ils regarderont vers moi, celui qu'ils ont transpercé. » (Za 12:10 ; Jn 19:37)",
 ],
 contexte=(
  "Vendredi 14 Nisan, veille d'un « grand sabbat » (Jn 19:31 — le 15 Nisan pascal). "
  "La Loi ordonne de décrocher les pendus avant la nuit (Dt 21:22-23) : les Juifs "
  "demandent le crurifragium — les jambes brisées pour hâter la mort. Pendant ce "
  "temps, dans le Temple, on égorge les agneaux du soir, « entre les deux soirs » "
  "(Ex 12:6), l'après-midi du 14. Deux scènes, une ville, un après-midi : les "
  "agneaux au Temple, l'Agneau à Golgotha. Paul bouclera : « Christ, notre Pâque, "
  "a été sacrifié » (1Co 5:7)."
 ),
 explication=(
  "Jean 19:36-37 est le seul passage qui cite deux accomplissements en deux "
  "versets : les jambes épargnées (Ex 12:46 + Ps 34:20 — l'agneau ET le juste) et "
  "le côté percé (Za 12:10, « transpercé », daqaru). Le crurifragium romain, "
  "fracture des tibias à la masse, accélérait l'asphyxie : les deux malfaiteurs "
  "le subissent, Jésus, déjà mort, y échappe — l'ennemi lui-même préserve "
  "l'oracle. « Sang et eau » : le témoin oculaire insiste (Jn 19:35) — mort "
  "réelle, constatée par la lance, contre toute thèse d'évanouissement. Le "
  "Psaume 34, chanté par David délivré chez Akish (1S 21), promet au juste des os "
  "gardés : le Juste les garde jusque dans la mort."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus meurt le 14 Nisan, à "
  "l'heure de l'agneau (la 9e heure, 15 heures) : l'agneau sans défaut, aux os "
  "intacts, mangé le soir même dans les maisons, préfigurait le sacrifice parfait. "
  "Le coup de lance, loin d'être un détail macabre, est une preuve : la mort est "
  "constatée par l'exécutant romain, et « celui qui l'a vu en a rendu témoignage » "
  "(Jn 19:35). Zacharie 12:10 (« ils regarderont vers celui qu'ils ont transpercé ») "
  "s'accomplit à Golgotha — et gardera une portée que la Révélation reprendra "
  "(Ré 1:7), hors du cadre daté de cette fiche."
 ),
 accomplissement=[
  ("1513 av. n. è.", "Exode 12:46 : l'agneau aux os intacts, mangé le soir du 14 Nisan"),
  ("Xe s. av. n. è.", "Psaume 34:20 : le juste aux os gardés (David chez Akish)"),
  ("VIe s. av. n. è.", "Zacharie 12:10 : le Transpercé vers qui l'on regardera"),
  ("33 de n. è., 14 Nisan, 15 h", "Mort à la 9e heure ; jambes des deux autres brisées, les siennes non"),
  ("33 de n. è., 14 Nisan", "Le coup de lance : sang et eau ; décrochement avant le sabbat"),
 ],
 hist=(
  "Deutéronome 21:22-23 explique la demande juive : un pendu ne passe pas la nuit "
  "sur le bois — la hâte est légale, pas humaine. Le crurifragium est attesté "
  "archéologiquement : le supplicié de Giv'at ha-Mivtar (1968, voir D002) a les "
  "tibias fracturés — la procédure épargnée à Jésus. La Mishna (Pesahim 5, "
  "codifiée au IIe siècle) décrit l'égorgement pascal de l'après-midi au Temple : "
  "le cadre liturgique de l'heure. La lancea est l'arme réglementaire du "
  "légionnaire : le constat est militaire."
 ),
 geo=(
  "Le Temple et Golgotha, même après-midi : les agneaux égorgés dans les parvis, "
  "l'Agneau expirant hors les murs — la ville contient les deux autels. Le sang "
  "sur les linteaux (Ex 12) répond au sang et à l'eau du côté (Jn 19). Le jardin "
  "tout proche (Jn 19:41) permet l'ensevelissement rapide avant le sabbat : "
  "la proximité des lieux fait partie de l'accomplissement."
 ),
 sci=(
  "L'ostéologie (Yehohanan, 1968 : clou + tibias brisés) atteste ensemble les "
  "clous et le crurifragium du Ier siècle — exactement les deux gestes de Jean "
  "19:32-34, l'un subi par les deux autres, l'autre épargné à Jésus. La médecine "
  "propose des hypothèses pour « sang et eau » (épanchement péricardique ou "
  "pleural) : hypothèses, pas diagnostic — le texte insiste sur le témoignage, "
  "non sur le mécanisme (voir Limites). La Pâque est lunaire : le 14 Nisan tombe "
  "à la pleine lune de printemps — le calendrier fait partie du signe."
 ),
 limites=(
  "« Sang et eau » : hypothèses médicales citées comme telles, jamais comme "
  "diagnostic — Jean insiste sur le témoin, pas sur la lésion. Le quantième "
  "grégorien du 14 Nisan 33 n'est pas tranché ici (vendredi certain par les "
  "Évangiles : veille du sabbat). Zacharie 12:10 est traité pour Golgotha ; sa "
  "reprise en Révélation 1:7 (« tout œil le verra ») appartient à l'avenir non "
  "daté. La Mishna, postérieure (IIe siècle), est citée comme droit juif, pas "
  "comme compte rendu."
 ),
 tl=[("1513", "Ex 12:46 : l'agneau"), ("Xe s.", "Ps 34:20 : le juste"), ("VIe s.", "Za 12:10"),
     ("14 Nisan 33, 15 h", "Mort, os intacts"), ("14 Nisan 33", "La lance : sang et eau")],
 src=[("Psaume 34 — Bible d'étude (v. 20 : les os gardés)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/34"),
      ("Zacharie 12 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/12"),
      ("Jean 19 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/19"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_D004_agneau.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D005", titre="La trahison de l'ami — le talon levé, le baiser",
 ref="Psaume 41:9 ; Psaume 55:12-14 ; Jean 13:18-27 ; Matthieu 26:47-50 ; Psaume 109:8 ; Actes 1:15-26",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P539, P613 (41:9), P551, P617 (109:8) ; Évangiles — P704 (Mt 26:21-25)",
 texte=[
  "« L'homme avec qui j'étais en paix, en qui j'avais confiance, qui mangeait "
  "mon pain, a levé contre moi son talon. » (Ps 41:9 ; Jn 13:18)",
  "« Ce n'est pas un ennemi qui m'outrage — je le supporterais ; c'est toi, mon "
  "égal, mon guide, mon intime, avec qui j'avais de doux entretiens. » (Ps 55:12-14)",
  "« Celui que je baiserai, c'est lui : saisissez-le. » (Mt 26:48)",
  "« Qu'un autre prenne sa charge de surveillance. » (Ps 109:8 ; Ac 1:20 — Matthias)",
 ],
 contexte=(
  "David trahi par son conseiller intime Ahithophel, passé à Absalom (2S 15-17) "
  "puis pendu après l'échec du complot (2S 17:23) : trahison et pendaison, déjà. "
  "Mille ans plus tard, à la Cène, Jésus trempe le morceau — geste d'honneur de "
  "l'hôte — et l'offre à Judas (Jn 13:26) : dernier appel. À Gethsémani, dans la "
  "nuit, le baiser convenu désigne l'homme aux torches (Jn 18:3). Après Pâque, "
  "Pierre applique le Psaume 109 : la charge apostolique ne restera pas vacante — "
  "Matthias est adjoint aux onze (Ac 1:26), avant la Pentecôte."
 ),
 explication=(
  "« Lever le talon », c'est la ruade : comme le cheval qui rue contre la main "
  "qui le nourrit — l'image dit l'absurdité morale du geste. « Manger mon pain » "
  "dit la commensalité, alliance d'hospitalité : trahir son hôte est le pire des "
  "crimes d'honneur. Le baiser (phileô, baiser d'affection) détourné en signe "
  "d'arrestation : « C'est par un baiser que tu livres le Fils de l'homme ? » "
  "(Lc 22:48). Et Jésus appelle Judas « ami » (hetairos, compagnon, Mt 26:50) "
  "jusque dans la trahison. Le Psaume 109, imprécation contre le traître de "
  "David, fournit le verset 8 : la fonction survit au fonctionnaire indigne."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est qu'Ahithophel — le conseiller dont "
  "l'avis « était comme une parole de Dieu » (2S 16:23), passé à l'ennemi puis "
  "pendu — préfigurait Judas : intime, traître, pendu. Jésus sait « dès le "
  "commencement » (Jn 6:64) et nomme le diable (Jn 6:70) ; le morceau trempé est "
  "le dernier appel avant la nuit (Jn 13:30 : « il faisait nuit »). La charge "
  "reprise par Matthias (tiré au sort entre deux candidats, Ac 1:23-26) restaure "
  "le collège à douze pour la Pentecôte : la trahison ne laisse pas de chaise vide."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Ahithophel trahit David puis se pend (2S 15-17) ; Ps 41, 55, 109"),
  ("33 de n. è., 14 Nisan au soir", "La Cène : le morceau trempé offert à Judas (Jn 13:26) ; « il faisait nuit »"),
  ("33 de n. è., nuit", "Gethsémani : le baiser convenu, l'arrestation (Mt 26:47-50)"),
  ("33 de n. è.", "Pendaison de Judas (Mt 27:5 ; cf. D001 pour les deux récits)"),
  ("33 de n. è., avant Pentecôte", "Ps 109:8 appliqué : Matthias adjoint (Ac 1:20-26)"),
 ],
 hist=(
  "Ahithophel est documenté par le récit de 2 Samuel 15-17 : l'homme de Guilo, "
  "conseiller de David, beau-père d'Éliam (et donc grand-père de Bethsabée selon "
  "les généalogies croisées) — l'intime absolu. Le baiser comme signe nocturne "
  "s'explique : Gethsémani la nuit, torches et lanternes (Jn 18:3), visages "
  "pareils — il faut désigner. Jean 12:6 documente le mobile crapuleux : Judas "
  "tenait la bourse et « prenait ce qu'on y mettait ». Matthias, tiré au sort "
  "entre Joseph Barsabbas et lui, restaure les douze trônes promis (Mt 19:28)."
 ),
 geo=(
  "La chambre haute de Jérusalem (la Cène), le torrent du Cédron franchi de nuit "
  "(Jn 18:1), Gethsémani — « pressoir à huile » — au pied du mont des Oliviers : "
  "la trahison descend du cénacle au jardin. Le Temple, où l'argent est jeté "
  "(voir D001), et Hakeldama ferment la boucle. Lieux resserrés : tout se joue "
  "entre le Cédron et Hinnom, en une nuit et un matin."
 ),
 sci=(
  "Gethsémani garde son pressoir rupestre et sa grotte antiques, et huit oliviers "
  "monumentaux — mais leurs datations renvoient au Moyen Âge (époque des "
  "croisades), pas au Ier siècle : la fiche le dit (voir Limites). Le toponyme "
  "(pressoir à huile) confirme la fonction agricole du lieu au temps de Jésus. "
  "« Judas » (Yehudah) est l'un des noms les plus courants des ossuaires "
  "judéens : le traître porte le nom de tous — le banal du mal."
 ),
 limites=(
  "Le mobile de Judas est donné à deux niveaux — cupidité (Jn 12:6) et Satan "
  "(Jn 13:27 ; Lc 22:3) : la fiche ne psychologise pas au-delà des textes. La "
  "mort de Judas : deux récits complémentaires (voir D001), harmonisation non "
  "tranchée. Le Psaume 109 est un psaume d'imprécation : seul le verset 8, appliqué "
  "par Pierre, est traité ici. Les oliviers actuels de Gethsémani ne remontent "
  "pas au Ier siècle (datations médiévales)."
 ),
 tl=[("Xe s.", "Ahithophel : Ps 41"), ("14 Nisan au soir", "Le morceau"), ("Nuit", "Le baiser"),
     ("14 Nisan", "Pendaison"), ("Av. Pentecôte", "Matthias : Ps 109:8")],
 src=[("Dieu délivre l'homme plein d'égards (Ps 41, Ahithophel)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1979408"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Psaume 41 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/41"),
      ("Psaume 109 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/109")],
 img="images/prophe_D005_trahison.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D006", titre="Le silence et les sévices — l'agneau devant ses juges",
 ref="Ésaïe 53:7 ; Ésaïe 50:4-6 ; Michée 5:1 ; Psaume 38:13-14 ; Matthieu 26:57-68 ; 27:11-31",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Ésaïe — P618 (53:7), P623 (50:6) ; Michée 5:1 — contexte P457-P459",
 texte=[
  "« Comme un agneau mené à l'abattoir, il n'a pas ouvert la bouche. » (Is 53:7)",
  "« J'ai livré mon dos à ceux qui frappent, mes joues à ceux qui arrachent la "
  "barbe ; je n'ai pas caché mon visage aux outrages et aux crachats. » (Is 50:6)",
  "« On frappe avec le bâton sur la joue le juge d'Israël. » (Mi 5:1)",
  "« Jésus gardait le silence. » (Mt 26:63, devant Caïphe ; 27:12-14, devant Pilate)",
  "« Pilate s'en étonna fort. » (Mc 15:5 — l'aveu adverse du juge païen)",
 ],
 contexte=(
  "La nuit du 14 Nisan : Anne, puis Caïphe — faux témoins cherchés (Mt 26:59-61, "
  "« je puis détruire le temple »), silence, puis la réponse qui condamne "
  "(« tu l'as dit », Mt 26:64) et les crachats. Le matin : Pilate — silence sur "
  "« tous les chefs d'accusation » (Mt 27:12-14) ; Hérode — « il ne lui répondit "
  "rien » (Lc 23:9) ; retour chez Pilate — flagellation, couronne d'épines, "
  "manteau, « Voici l'homme » (Jn 19:5). Entre les audiences : gifles, voile, "
  "« prophétise ! » (Mc 14:65)."
 ),
 explication=(
  "Le silence n'est pas un aveu : Jésus parle quand il faut — « tu l'as dit » "
  "(Mt 26:64), « c'est pour cela que je suis né, et que je suis roi » "
  "(Jn 18:37), « tu n'aurais aucun pouvoir si… » (Jn 19:11) — et se tait devant "
  "l'iniquité. « Comme l'agneau » : le sacrifice pascal ne se défend pas (lien "
  "D004). Ésaïe 50:4-6 montre l'envers : le Serviteur à « l'oreille ouverte chaque "
  "matin », instruit, offrant son dos — obéissance active, pas passivité. "
  "Michée 5:1 frappe « le juge d'Israël » à la joue : le même chapitre annonce "
  "Bethléhem (5:2, voir C001) — le chapitre tient le berceau et la gifle."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que le silence devant Anne, Caïphe, "
  "Pilate et Hérode accomplit Ésaïe 53:7 à la lettre, et les sévices Ésaïe 50:6 "
  "et Michée 5:1 au détail : crachats (Mt 26:67), gifles (Jn 18:22), flagellation "
  "(Mt 27:26), couronnement d'épines. Pilate « étonné » (Mc 15:5) et sa femme "
  "avertie en rêve (Mt 27:19) fournissent l'aveu adverse : le juge païen proclame "
  "trois fois l'innocence (Jn 18:38 ; 19:4, 6) — et livre l'innocent. Le Psaume "
  "38:13-14 (David sourd-muet devant les pièges) donne le type davidique."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 50:6, 53:7 et Michée 5:1 : le Serviteur frappé et muet"),
  ("33 de n. è., nuit du 14", "Anne puis Caïphe : faux témoins, silence, « tu l'as dit », crachats"),
  ("33 de n. è., matin", "Pilate : silence total ; Hérode : aucune réponse (Lc 23:9)"),
  ("33 de n. è.", "Flagellation, couronne d'épines, « Voici l'homme » (Jn 19:1-5)"),
  ("33 de n. è.", "Triple proclamation d'innocence — et livraison (Jn 18:38-19:16)"),
 ],
 hist=(
  "Le procès viole le droit juif lui-même : selon les règles codifiées ensuite "
  "dans la Mishna (Sanhédrin), un procès capital ne se juge ni de nuit ni un jour "
  "de fête — celui-ci cumule les deux, avec des faux témoins « qui ne "
  "s'accordaient pas » (Mc 14:56-59). La flagellation au flagrum plombé est un "
  "supplice romain documenté, souvent mortel par lui-même. La parodie d'intronisation "
  "(couronne tressée, manteau écarlate, roseau-sceptre, « salut, roi ! ») improvise "
  "un sacre grotesque : les soldats couronnent sans le savoir (voir D007)."
 ),
 geo=(
  "Palais d'Anne et de Caïphe (quartier aristocratique, tradition du mont Sion), "
  "Prétoire romain — forteresse Antonia ou palais d'Hérode : les deux "
  "localisations sont défendues, la fiche ne tranche pas —, Gabbatha « le pavé » "
  "(Jn 19:13, dallage du jugement), palais d'Hérode Antipas : la nuit et le matin "
  "promènent l'Agneau muet d'un tribunal à l'autre, à travers la ville haute. "
  "Gethsémani, où il a été pris priant, n'est qu'à un kilomètre."
 ),
 sci=(
  "La médecine explique la suite : la flagellation romaine (lanières plombées, "
  "hémorragies, choc) laisse le condamné exsangue — Simon de Cyrène devra porter "
  "le poteau (Mc 15:21). L'épigraphie a livré les deux juges : l'ossuaire de "
  "Caïphe (1990, voir C005) et la pierre de Pilate, préfet de Judée (1961, voir "
  "C005) — le Sanhédrin et Rome ont leurs noms dans la pierre. Les dallages "
  "hérodiens et romains de Jérusalem illustrent le décor, sans le localiser "
  "sûrement."
 ),
 limites=(
  "L'arrachage de la barbe (Is 50:6b) n'est pas détaillé par les Évangiles : "
  "accompli dans l'ensemble des sévices ou non documenté au détail — la fiche "
  "le signale au lieu de l'affirmer. Prétoire (Antonia ou palais d'Hérode) et "
  "Gabbatha : identifications débattues, non tranchées. La Mishna est postérieure "
  "(IIe siècle) : citée comme droit juif, pas comme procès-verbal. L'espèce "
  "botanique des « épines » n'est pas spéculée."
 ),
 tl=[("VIIIe s.", "Is 50, 53, Mi 5"), ("Nuit du 14", "Anne, Caïphe"), ("Matin", "Pilate, Hérode"),
     ("Matin", "Flagellation, épines"), ("14 Nisan", "Livré quoique innocent")],
 src=[("La sépulture du Serviteur (Is 53, silence compris)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/1200027501/36/2"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 50 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/50"),
      ("Matthieu 26 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/26")],
 img="images/prophe_D006_silence.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D007", titre="La pierre rejetée — devenue tête de l'angle",
 ref="Psaume 118:22-23 ; Ésaïe 28:16 ; Matthieu 21:42-44 ; Actes 4:8-12 ; Éphésiens 2:19-22 ; 1 Pierre 2:4-8",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P556, P607 (118:22-23) ; Ésaïe — P600 (28:16) ; NT — P777 (1P 2), P992 (Mc 12)",
 texte=[
  "« La pierre que les bâtisseurs ont rejetée est devenue la principale pierre "
  "d'angle. Cela est venu de Jéhovah ; c'est une chose prodigieuse à nos yeux. » "
  "(Ps 118:22-23)",
  "« Voici que je pose en Sion une pierre, une pierre éprouvée, précieuse, "
  "angulaire, d'un fondement sûr ; celui qui croit ne fuira pas. » (Is 28:16)",
  "« N'avez-vous jamais lu dans les Écritures : La pierre qu'ont rejetée les "
  "bâtisseurs est devenue la principale pierre d'angle ? » (Mt 21:42, aux chefs, "
  "après les vignerons homicides)",
  "« Il n'y a de salut en aucun autre. » (Ac 4:12, Pierre aux juges du Sanhédrin)",
 ],
 contexte=(
  "Le Psaume 118 appartient au Hallel pascal (Ps 113-118) — le même psaume que "
  "« Hosanna » (voir C006), chanté par Jésus et les Douze à la Cène avant de "
  "sortir (Mt 26:30) : Jésus chante sa propre prophétie. Ésaïe 28 l'adresse aux "
  "dirigeants « moqueurs » de Jérusalem, alliés « avec la mort » (28:15). Dans la "
  "semaine pascale, au Temple, après la parabole des vignerons homicides — « ils "
  "comprirent que c'était d'eux qu'il parlait » (Mt 21:45) — Jésus retourne la "
  "pierre contre les bâtisseurs. Après la Pentecôte, Pierre la leur jette de "
  "nouveau : devant Anne, Caïphe et les mêmes noms qu'au procès (Ac 4:5-6)."
 ),
 explication=(
  "Rosh pinnah, « tête de l'angle » : la pierre faîtière qui coiffe et chaine les "
  "deux murs — la plus en vue de l'édifice, comme le Christ du temple spirituel. "
  "« Bâtisseurs » : au sens figuré les chefs ; au sens littéral, ceux qui "
  "bâtissent le Temple d'Hérode sous les yeux de Jésus — les constructeurs du "
  "sanctuaire rejettent la pierre du sanctuaire. Double effet : fondement sûr "
  "pour qui croit (Is 28:16), pierre d'achoppement pour qui refuse (Is 8:14, "
  "cité en 1P 2:8) — et Mt 21:44 ajoute : qui tombe dessus s'y brise. « Cela est "
  "venu de Jéhovah » : le retournement est divin, pas humain."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que le rejet (procès, Golgotha) "
  "puis l'exaltation (résurrection, droite — voir D008, D009) accomplissent le "
  "Psaume 118 et Ésaïe 28 à la lettre : la pierre méprisée par les experts est "
  "remise par Dieu au faîte. La congrégation, « temple spirituel », est bâtie "
  "dessus : fondés sur les apôtres et prophètes, « Jésus Christ lui-même étant "
  "la principale pierre angulaire » (Ép 2:20), les chrétiens en sont les « pierres "
  "vivantes » (1P 2:5). « Aucun autre nom » (Ac 4:12) : Pierre proclame aux juges "
  "mêmes l'exclusivité du salut — courage et doctrine d'une phrase."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Psaume 118:22 : la pierre rejetée puis exaltée (chantée à chaque Pâque)"),
  ("VIIIe s. av. n. è.", "Ésaïe 28:16 : la pierre éprouvée posée en Sion"),
  ("33 de n. è., semaine pascale", "Les vignerons homicides puis « n'avez-vous jamais lu ? » (Mt 21:33-44)"),
  ("33 de n. è., 14-16 Nisan", "Rejet (Golgotha) puis remise au faîte (résurrection, droite)"),
  ("33 de n. è., après Pentecôte", "Pierre devant le Sanhédrin : Ac 4:8-12 ; puis Éphésiens, 1 Pierre"),
 ],
 hist=(
  "Le Hallel (Ps 113-118) se chantait à la Pâque : Matthieu 26:30 (« après avoir "
  "chanté ») place le Psaume 118 sur les lèvres de Jésus quelques heures avant "
  "Gethsémani. La parabole des vignerons (Mt 21:33-41) vise nommément les chefs — "
  "le verset 45 le confirme : ils comprennent. Actes 4:5-6 nomme le tribunal : "
  "Anne, Caïphe, Jean, Alexandre — les juges du procès entendant l'acte "
  "d'accusation retourné. Ésaïe 28:15 (« alliance avec la mort ») nomme le parti "
  "adverse : les dirigeants moqueurs."
 ),
 geo=(
  "Le Temple d'Hérode, chantier colossal en cours (achevé vers 63-64, voir B008), "
  "est le décor : « les bâtisseurs » au sens propre taillent et posent pendant "
  "que les Bâtisseurs au sens figuré rejettent. « En Sion » (Is 28:16) : la pierre "
  "est posée à Jérusalem — Pentecôte au Cénacle, Pierre au portique de Salomon "
  "(Ac 3:11 ; 5:12). La pierre de Jérusalem (meleke), blanche et massive, fait "
  "les angles à bossage encore visibles au Mur occidental."
 ),
 sci=(
  "L'architecture explique la métaphore : la pierre d'angle chaine deux murs et "
  "reçoit les charges — la rejeter, c'est fragiliser l'édifice ; la faîtière "
  "couronne l'angle et se voit de partout. La géologie locale (calcaire meleke, "
  "tendre à la taille, durcissant à l'air) explique les blocs monumentaux du "
  "Temple hérodien, aux joints vifs sans mortier. Les angles à bossage du Mur "
  "occidental montrent l'appareil que Jésus avait sous les yeux en parlant."
 ),
 limites=(
  "« Tête de l'angle » : faîtière de couronnement (lecture de l'Étude perspicace) "
  "ou pierre angulaire de fondation (Éphésiens 2:20, « fondés ») — la fiche donne "
  "les deux lectures, complémentaires. Les vignerons homicides sont une parabole "
  "(fiction d'enseignement, cf. C011), pas un fait divers. « Aucun autre nom » "
  "est cité comme compréhension des Témoins de Jéhovah, sans débat interreligieux "
  "(règle 7). Aucune date pour l'avenir."
 ),
 tl=[("Xe s.", "Ps 118:22"), ("VIIIe s.", "Is 28:16"), ("33, sem. pascale", "« N'avez-vous lu ? »"),
     ("14-16 Nisan", "Rejet puis faîte"), ("33+", "Ac 4 : aux juges")],
 src=[("Pierre de l'angle — Étude perspicace (rosh pinnah)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011025"),
      ("Pierre angulaire — la tête de l'angle (Ac 4, Mt 21)", "https://wol.jw.org/fr/wol/d/r30/lp-f/202018439"),
      ("Psaume 118 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/118"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_D007_pierre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D008", titre="La résurrection — le troisième jour, selon les Écritures",
 ref="Psaume 16:8-11 ; Actes 2:22-32 ; 13:34-37 ; Matthieu 12:39-40 ; Jonas 1:17-2:10 ; 1 Corinthiens 15:3-8",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P527, P642 (16:8-11) ; Jonas — P450, P644 (Mt 12:39-40)",
 texte=[
  "« Tu n'abandonneras pas mon âme au Shéol ; tu ne permettras pas que ton fidèle "
  "voie la fosse. » (Ps 16:10)",
  "« David est mort, il a été enterré, et son tombeau est parmi nous jusqu'à ce "
  "jour. C'est donc du Christ qu'il a parlé. » (Ac 2:29-31, Pierre à la Pentecôte)",
  "« De même que Jonas fut trois jours et trois nuits dans le ventre du grand "
  "poisson, de même le Fils de l'homme sera trois jours et trois nuits dans le "
  "cœur de la terre. » (Mt 12:40)",
  "« Il a été relevé le troisième jour, selon les Écritures. » (1Co 15:4 — "
  "« Écritures » au pluriel)",
 ],
 contexte=(
  "Psaume 16 : David (miktam de confiance). Jonas : le prophète englouti (~VIIIe "
  "siècle, Ninive — voir F009), priant « du ventre du Shéol » (Jon 2:2). Jésus, "
  "aux pharisiens qui demandent un signe : « génération méchante et adultère » — "
  "pas d'autre signe que Jonas (Mt 12:39). Le 14 Nisan : mort ; le 15 : sabbat "
  "au tombeau ; le 16 Nisan, « le premier jour de la semaine, de grand matin » "
  "(Lc 24:1) : relevé. Quarante jours d'apparitions (Ac 1:3, « preuves certaines »), "
  "puis Pierre à la Pentecôte."
 ),
 explication=(
  "« Fosse » (shachath, texte hébreu) ou « corruption » (diaphthora, Septante "
  "suivie par Pierre) : les deux lectures convergent — pas d'abandon définitif, "
  "pas de décomposition. L'argument de Pierre est imparable devant Jérusalem : "
  "le tombeau de David est connu et occupé (Ac 2:29) — David parle donc d'un "
  "autre. « Trois jours et trois nuits » est un idiome juif (partie de jour = "
  "jour) : vendredi après-midi + sabbat + dimanche matin = « le troisième jour » "
  "(cf. Est 4:16 puis 5:1, « le troisième jour »). « Selon les Écritures » "
  "(pluriel) : Psaume 16, Jonas, Ésaïe 53:10-11 (« il verra… il prolongera ») — "
  "le dossier, pas un verset."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah établit quatre preuves : mort réelle "
  "(la lance, Jn 19:34-35), tombeau retrouvé vide (neuf, proche, localisé — "
  "Jn 19:41-42), apparitions multiples (jardin, Emmaüs, chambre haute, Tibériade, "
  "montagne, plus de 500 à la fois — 1Co 15:6), transformation des témoins "
  "(Thomas le sceptique convaincu par les plaies, Jn 20:24-29). « La plupart "
  "vivent encore » (1Co 15:6, vers 55) : l'apologétique est vérifiable du vivant "
  "des témoins. Relevé le 16 Nisan, Jésus est « prémices » (1Co 15:20, 23) : "
  "garantie pour tous (voir la catégorie G)."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Psaume 16:10 : le fidèle ne verra pas la fosse"),
  ("VIIIe s. av. n. è.", "Jonas : trois jours dans le Shéol du poisson (Jon 1:17-2:10)"),
  ("33 de n. è., 14-16 Nisan", "Mort (14), sabbat au tombeau (15), relevé le premier jour (16)"),
  ("33 de n. è., 40 jours", "Apparitions : Marie, Emmaüs, les Douze, Thomas, Tibériade, les 500+"),
  ("33 de n. è., Pentecôte", "Pierre : Ac 2:22-32 — « ce Jésus, Dieu l'a ressuscité »"),
 ],
 hist=(
  "Le tombeau vide est admis par l'adversaire : les chefs inventent le vol par "
  "les disciples endormis (Mt 28:11-15) — admettant le vide en l'expliquant. "
  "1 Corinthiens 15:3-8 (vers 55) nomme les témoins par groupes, dont « plus de "
  "cinq cents frères à la fois, dont la plupart vivent encore » : falsifiable. "
  "Thomas exige les plaies et les touche (Jn 20:24-29) : le sceptique interne "
  "convaincu. Tacite (Annales 15:44) atteste la mort sous Pilate — cité pour la "
  "mort uniquement (voir Limites)."
 ),
 geo=(
  "Le jardin et le tombeau neuf (Jn 19:41) : proximité de Golgotha, emplacement "
  "connu — le vide est vérifiable sur place. Emmaüs (Lc 24:13, une soixantaine de "
  "stades, ~11 km) : localisation débattue (Nicopolis, Qubeibeh, Motza…), non "
  "tranchée. La Galilée (montagne, Mt 28:16 ; Tibériade, Jn 21) et la chambre "
  "haute de Jérusalem : les apparitions couvrent le pays. Le tombeau exact "
  "(Saint-Sépulcre ou Jardin) n'est pas tranché (cf. D002)."
 ),
 sci=(
  "L'ensevelissement (myrrhe et aloès, plus de trente kilos, Jn 19:39 ; pierre "
  "roulée, golel) est incompatible avec un corps volé à la hâte par des pêcheurs "
  "effrayés. La mort réelle est médicalement constatée (lance, sang et eau — "
  "voir D004) : pas d'évanouissement. Et l'honnêteté du dossier exige "
  "l'exclusion : le linceul de Turin, daté du XIVe siècle par le carbone 14 "
  "(1988, trois laboratoires), n'entre pas dans ce dossier — ni pour, ni contre."
 ),
 limites=(
  "Le Testimonium flavianum (Josèphe) est partiellement interpolé : non utilisé. "
  "Tacite atteste la mort, pas la résurrection : cité dans cette limite. Le "
  "linceul de Turin (XIVe siècle au carbone 14) est exclu. Emmaüs et le tombeau "
  "exact : non tranchés. Le corps ressuscité — corps spirituel manifesté en corps "
  "de chair selon les publications (voir source Résurrection) — est cité comme "
  "compréhension, non disséqué. Osée 6:2 (« le troisième jour ») parle d'Israël, "
  "pas du Messie : non rattaché ici."
 ),
 tl=[("Xe s.", "Ps 16:10"), ("VIIIe s.", "Jonas : 3 jours"), ("14-16 Nisan 33", "Mort, sabbat, relevé"),
     ("40 jours", "Apparitions, 500+"), ("Pentecôte", "Pierre : Ac 2")],
 src=[("La résurrection de Jésus : 4 raisons d'être sûrs", "https://wol.jw.org/fr/wol/d/r30/lp-f/402014842"),
      ("Réellement, le Seigneur a été relevé ! (4 preuves)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2001201"),
      ("Psaume 16 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/16"),
      ("Actes 2 — Bible d'étude, notes (Pierre)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/2")],
 img="images/prophe_D008_resurrection.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D009", titre="À la droite de Dieu — assis, jusqu'à…",
 ref="Psaume 110:1-4 ; Actes 2:33-36 ; Psaume 68:18 ; Éphésiens 4:8-11 ; Actes 1:9-11 ; Marc 16:19",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P552, P608 (110:1), P542, P645 (68:18) ; NT — P747 (Ép 4:8-11)",
 texte=[
  "« Jéhovah a déclaré à mon Seigneur : Assieds-toi à ma droite, jusqu'à ce que "
  "je place tes ennemis comme un escabeau sous tes pieds. » (Ps 110:1)",
  "« David n'est pas monté aux cieux ; mais il dit : Jéhovah a dit à mon Seigneur : "
  "Assieds-toi à ma droite. » (Ac 2:34-35, Pierre — même argument qu'en D008)",
  "« Tu es monté en haut, tu as emmené des captifs ; tu as pris des dons parmi "
  "les hommes. » (Ps 68:18 — repris en Ép 4:8 : « il a donné des dons »)",
  "« Il fut élevé pendant qu'ils regardaient, et une nuée le déroba à leurs "
  "yeux. » (Ac 1:9, le 40e jour, mont des Oliviers)",
 ],
 contexte=(
  "Psaume 110 : David — le psaume le plus cité du Nouveau Testament. Jésus s'en "
  "sert pour clouer les pharisiens : « Si David l'appelle Seigneur, comment "
  "est-il son fils ? » (Mt 22:41-46) — silence adverse. Psaume 68 : cantique de "
  "l'arche montant à Sion (2S 6), avec captifs et butin redistribué (2S 6:19). "
  "Le 40e jour après le 16 Nisan, à Béthanie sur les Oliviers (Lc 24:50) : "
  "bénédiction, nuée, deux hommes en blanc — « il viendra de la même manière » "
  "(Ac 1:11). Dix jours plus tard : la Pentecôte, l'esprit répandu — preuve "
  "visible de l'intronisation invisible (Ac 2:33)."
 ),
 explication=(
  "« Jéhovah à mon Seigneur » : deux Seigneurs — YHWH et l'Adoni davidique, "
  "soumis à son propre descendant : la préexistence en un verset (cf. C001, "
  "« origines anciennes »). « Jusqu'à » : session d'attente — le règne médian "
  "avant la soumission des ennemis (1Co 15:25 ; Hé 10:13). Paul retourne le "
  "Psaume 68:18 : « pris des dons » devient « donné des dons » (Ép 4:8) — le "
  "vainqueur antique distribuait le butin (cf. 2S 6:19) : les dons, ce sont des "
  "hommes — apôtres, prophètes, évangélistes, bergers et enseignants (Ép 4:11). "
  "« De la même manière » (Ac 1:11) : modalité (nuée, ciel), pas date."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est qu'exalté le 40e jour, Jésus "
  "« s'assit à la droite de Dieu » (Mc 16:19) : « Dieu l'a fait Seigneur et "
  "Christ » (Ac 2:36). Il avait reçu « tout pouvoir » sur la montagne galiléenne "
  "(Mt 28:18) ; de la droite, il répand l'esprit à la Pentecôte — la foule "
  "entend la preuve de ce qu'elle ne voit pas. Le verset 4 (« prêtre pour "
  "toujours à la manière de Melchisédech ») fonde le dossier sacerdotal de "
  "l'épître aux Hébreux (Hé 5-7) : cité, non développé ici. Le verset 2 (« va au "
  "milieu de tes ennemis ») et 1914 : renvoi B009, non développé."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Psaumes 110 et 68 : le Seigneur assis, le vainqueur montant"),
  ("33 de n. è., 16 Nisan", "Relevé ; « tout pouvoir m'a été donné » (Mt 28:18)"),
  ("33 de n. è., 40e jour", "Ascension depuis les Oliviers : nuée, bénédiction (Ac 1:9-12)"),
  ("33 de n. è., 50e jour", "Pentecôte (6 Sivan) : l'esprit répandu, preuve de l'intronisation"),
  ("33 de n. è.", "Pierre : « Dieu l'a fait Seigneur et Christ » (Ac 2:36)"),
 ],
 hist=(
  "Matthieu 22:41-46 garde l'aveu adverse : devant « si David l'appelle Seigneur… », "
  "les pharisiens se taisent — incapables de répondre, ils valident la question. "
  "2 Samuel 6 (l'arche montant à Sion, danses, sacrifices, distributions) donne "
  "le contexte du Psaume 68 : Paul n'allégorise pas, il suit le cortège. Actes 1:3 "
  "(« preuves certaines » pendant quarante jours) encadre l'ascension de garanties. "
  "La Pentecôte (Ac 2) est l'événement public : trois mille baptisés — "
  "l'intronisation a son attestation de foule."
 ),
 geo=(
  "Le mont des Oliviers, versant de Béthanie (Lc 24:50 ; Ac 1:12, « le chemin "
  "d'un sabbat » de Jérusalem) : même mont que l'entrée (C006) et l'agonie — "
  "la boucle se ferme où la semaine s'était ouverte. « Hors de Sion » (Ps 110:2) : "
  "le sceptre part de Jérusalem — la Pentecôte au Cénacle en est le premier "
  "mouvement. La nuée (Ac 1:9) est la nuée théophanique — Sinaï, transfiguration : "
  "Dieu voyage en nuée."
 ),
 sci=(
  "Le calendrier fait partie du dossier : 16 Nisan (relevé) + 40 jours "
  "(apparitions) + 10 jours = 50e jour, Pentecôte, 6 Sivan — fête du don de la "
  "Loi devenue fête du don de l'esprit. La distance « chemin d'un sabbat » "
  "(Ac 1:12, ~1 km) correspond aux Oliviers proches. Aucun phénomène céleste daté "
  "n'est revendiqué pour l'ascension : la fiche ne spécule sur aucune astronomie — "
  "la nuée est théophanique, pas météorologique."
 ),
 limites=(
  "« Il viendra de la même manière » (Ac 1:11) : modalité, jamais date (C9). "
  "Psaume 110:2 et 1914 : renvoyés à B009 (Jérusalem foulée), non développés — "
  "cette fiche traite l'exaltation de 33. Psaume 110:4 (Melchisédech) : dossier "
  "de l'épître aux Hébreux, cité et non développé. Le point exact de l'ascension "
  "sur les Oliviers n'est pas marqué : l'église de l'Ascension est une tradition, "
  "signalée comme telle. Personne n'a vu l'arrivée : crue sur la parole et la "
  "Pentecôte."
 ),
 tl=[("Xe s.", "Ps 110 + 68"), ("16 Nisan 33", "« Tout pouvoir »"), ("40e jour", "Ascension"),
     ("50e jour", "Pentecôte : preuve"), ("33", "« Seigneur et Christ »")],
 src=[("Psaume 110 — Bible d'étude, notes (assis à ma droite)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/110"),
      ("Actes 1 — Bible d'étude, notes (l'ascension)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/1"),
      ("Éphésiens 4 — Bible d'étude, notes (il a donné des dons)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/49/4"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_D009_droite.jpg",
))
