#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE J (vague 12, suite) — PERSONNAGES ET LIEUX NOMMES D'AVANCE (2e partie)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="J",
    nom="Personnages et lieux nommés d'avance (2e partie)",
    vague="12",
    intro=(
        "Après Cyrus, Josias et Bethléhem (vague 11), la catégorie J continue : huit "
        "personnages ou maisons nommés d'avance. Isaac, dont le nom — « Rire » — est "
        "prononcé avant sa conception ; Shilo, le titre royal scellé sur le lit de mort "
        "de Jacob ; l'étoile de Jacob, vue par Balaam « pas maintenant, pas de près » ; "
        "Balaam lui-même, contraint de bénir et de nommer Amalek, les Kéniens, Assour, "
        "Éber et Kittim ; la maison de David, avec Salomon nommé avant sa naissance ; "
        "la maison d'Éli, jugée par un homme de Dieu anonyme ; Samson, naziréen dès le "
        "ventre ; et Josias, auquel la prophétesse Houlda promet le repos avant la "
        "tempête. Mêmes dix blocs, mêmes règles : un seul système chronologique par "
        "fiche, aucune date pour l'avenir, et des limites écrites noir sur blanc."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J004", titre="Isaac nommé — le Rire promis avant sa conception",
 ref="Genèse 17:19-21 ; Genèse 21:12 ; Genèse 18:9-15 (C8) ; Romains 9:7 ; Hébreux 11:18",
 statut="Accomplie (P010, P012)",
 cat="J", syst="Système âges bibliques (annonce → naissance)",
 reg="Registre : Genèse — P010 (17:19-21 : Isaac héritier, Ismaël béni), P012 (21:12 : postérité appelée par Isaac)",
 texte=[
  "« Sara, ta femme, va t'enfanter un fils. Tu le nommeras ISAAC. » "
  "(Gn 17:19 — le nom avant la conception !)",
  "« Je ferai de mon alliance avec lui une alliance PERPÉTUELLE pour ses descendants. » "
  "(17:19 — alliance, pas seulement naissance !)",
  "« Quant à Ismaël… il engendrera DOUZE PRINCES, et je ferai de lui une grande nation. » "
  "(17:20 — le cadet n'est pas oublié !)",
  "« Je ferai alliance avec Isaac, que Sara t'enfantera L'ANNÉE PROCHAINE, à cette époque. » "
  "(17:21 — délai d'un an, daté !)",
  "« C'est par le moyen d'ISAAC que je réaliserai mes promesses. » "
  "(21:12 — la postérité appelée par Isaac !)",
  "« Dieu m'a préparé du RIRE ; quiconque l'apprendra rira de moi. » "
  "(21:6 — Sara boucle le nom !)",
 ],
 contexte=(
  "Abraham a 99 ans quand Jéhovah lui apparaît (17:1) ; à la naissance, il en aura 100 "
  "et Sara 90 (17:17 — les chiffres de l'annonce sont ceux de l'accomplissement). Sara "
  "a cessé depuis longtemps d'avoir ses règles (18:11). Ismaël, le fils d'Agar, a 13 ans "
  "et vient d'être circoncis (17:25). La scène se joue sous les chênes de Mamré, près "
  "d'Hébron : alliance de la circoncision, changement des noms — Abram devient Abraham "
  "(« père d'une multitude »), Saraï devient Sara — puis trois visiteurs annoncent "
  "« au temps fixé, l'année prochaine » (18:10, 14 — C8). Sara rit dans la tente ; "
  "l'ange la reprend : « Y a-t-il rien de trop extraordinaire pour Jéhovah ? » (18:14)."
 ),
 explication=(
  "« Isaac » (Yitsḥaq) signifie « Rire » : le nom est un programme en trois actes — "
  "Abraham rit (17:17), Sara rit (18:12), puis Sara rit de joie (21:6). Le « temps fixé » "
  "(mo'èd, 18:14 ; 21:2) verrouille le délai : un an, ni plus ni moins. L'alliance est "
  "« perpétuelle » (17:19) et nominative : elle passe par Isaac, non par Ismaël — non "
  "que le cadet soit maudit : il reçoit sa propre promesse chiffrée, douze princes et "
  "une grande nation (17:20). Genèse 21:12 tranche le conflit des deux fils après le "
  "sevrage : la postérité de l'alliance « sera appelée » par Isaac — formule reprise "
  "telle quelle par Paul (Rm 9:7) et l'épître aux Hébreux (11:18)."
 ),
 interpretation=(
  "Isaac est le maillon essentiel de la lignée menant à Christ (1Ch 1:28, 34 ; Mt 1:1, 2 ; "
  "Lc 3:34). Paul en fait la charte de la promesse contre la chair : « c'est par Isaac "
  "qu'une postérité te sera appelée » (Rm 9:7), « nous sommes enfants de la promesse, "
  "comme Isaac » (Ga 4:28 — C8). Hébreux 11:18 rappelle que les promesses avaient été "
  "dites « en Isaac » — avant de raconter l'épreuve du Morija, où Abraham raisonna que "
  "Dieu pouvait relever son fils (Hé 11:19 — C8). Ismaël, béni et multiplié, reçoit "
  "l'accomplissement terrestre de 17:20 sans recevoir l'alliance : deux promesses, deux "
  "destinées, un seul texte."
  "« Au temps fixé » l'année suivante, Sara enfante (21:1-7 — P010) ; Abraham nomme "
  "l'enfant Isaac (21:3) et le circoncit le huitième jour (21:4). Ismaël, de son côté, "
  "engendre les douze princes nommés un par un en Genèse 25:12-16 — liste reprise à "
  "l'identique en 1 Chroniques 1:29-31, double attestation généalogique. « C'est par "
  "Isaac » : la lignée de l'alliance passe par Jacob, Juda, David, jusqu'à Christ — "
  "les généalogies de Matthieu 1 et Luc 3 en font foi."
 ),
 accomplissement=[
  ("Annonce (100/90 ans)", "Le nom Isaac avant la conception"),
  ("+1 an", "Naissance « au temps fixé » (21:1-7)"),
  ("8e jour", "Circoncision (21:4)"),
  ("Sevrage", "21:12 : postérité par Isaac"),
  ("Ismaël", "12 princes (25:12-16 // 1Ch 1)"),
  ("Ier s.", "Rm 9:7 ; Hé 11:18 citent 21:12"),
 ],
 hist=(
  "Double attestation interne : la liste des douze princes ismaélites (25:13-15) est "
  "recopiée en 1 Chroniques 1:29-31, à des siècles d'intervalle rédactionnel. Réception "
  "au Ier siècle : Paul (Rm 9:7 ; Ga 4:28) et Hébreux 11:18 citent Genèse 21:12 comme une "
  "charte connue et admise. Les tribus arabes issues d'Ismaël (Nabayoth, Qédar — voir "
  "A011) occupent durablement le nord de l'Arabie et le désert syrien. Les récits "
  "patriarcaux (puits, alliances, dots, sépulcre de Makpéla) décrivent un monde "
  "semi-nomade cohérent du IIe millénaire, sans anachronisme d'empire."
 ),
 geo=(
  "Mamré-Hébron : les chênes où l'annonce est faite (18:1) ; Beer-Schéba : le puits où "
  "Abraham plante un tamaris et « invoque le nom de Jéhovah » après la naissance "
  "(21:31-33 — C8) ; le Négueb et le désert de Parân, où Ismaël devient archer (21:20-21 — "
  "C8). Hébron reste la ville d'Abraham : c'est là qu'il enterre Sara (ch. 23 — C8) et "
  "qu'il sera lui-même recueilli (25:9 — C8)."
 ),
 sci=(
  "Physiologie : Genèse 18:11 note que Sara « avait cessé d'avoir ses règles » — "
  "constat de ménopause en vocabulaire exact, qui fonde le rire puis le miracle. "
  "Onomastique : Yitsḥaq est un inaccompli (« il rit / on rira ») — nom-phrase, comme "
  "Yishma'èl (« Dieu entend ») ; Saraï (« ma princesse ») devient Sara (« princesse », "
  "sans suffixe : princesse de nations, 17:16). Paronomase triple : le rire d'Abraham "
  "(surprise), de Sara (doute), puis de Sara (joie) — le récit joue du même verbe "
  "tsāḥaq aux trois actes."
 ),
 limites=(
  "Les cent ans d'Abraham et les quatre-vingt-dix ans de Sara sont les âges de "
  "l'accomplissement, l'annonce ayant lieu à 99 ans (17:1, 24) — le récit ne se "
  "contredit pas, il date deux moments. L'identification précise des douze tribus "
  "ismaélites à des groupes arabes postérieurs n'est pas détaillée ici. Cette fiche ne "
  "fait pas d'Isaac un « type » systématique au-delà de ce que dit Galates 4. Le Morija "
  "(ch. 22) appartient à une autre prophétie du registre."
 ),
 tl=[("99 ans", "Annonce à Mamré"), ("+1 an", "« Au temps fixé »"), ("8e jour", "Circoncision"),
     ("Sevrage", "21:12 : « par Isaac »"), ("12 princes", "Ismaël multiplié"), ("Ier s.", "Paul cite 21:12")],
 src=[("Isaac — Étude perspicace (nom, rire, alliance)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002203"),
      ("Abraham et Sara obéissent à Dieu (récit)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/202025246/11/0"),
      ("Genèse 17 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/17"),
      ("Genèse 21 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/21")],
 img="images/prophe_J004_isaac.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J005", titre="Shilo — le sceptre de Juda jusqu'au Légitime",
 ref="Genèse 49:8-12 ; Genèse 49:10 ; 1 Chroniques 5:2 ; Hébreux 7:14 ; Révélation 5:5",
 statut="Accomplie (P029, P572)",
 cat="J", syst="Système lignée (Juda → David → Jésus)",
 reg="Registre : Genèse — P029 (49:8-12 : sceptre, législateur, Shilo), P572 (49:10 : le sceptre ne s'écartera pas)",
 texte=[
  "« Juda, tes frères te loueront… les fils de ton père se prosterneront devant toi. » "
  "(49:8 — la primauté change de mains !)",
  "« LIONCEAU… il s'est couché comme un LION : qui le fera lever ? » "
  "(49:9 — le lion de Juda !)",
  "« Le SCEPTRE ne s'écartera pas de Juda… jusqu'à ce que vienne SHILO. » "
  "(49:10 — le titre scellé !)",
  "« Et à lui appartiendra l'OBÉISSANCE DES PEUPLES. » (49:10 — tous les peuples !)",
  "« Il attache son ânon à la VIGNE… il lave son vêtement dans le VIN. » "
  "(49:11 — l'abondance du règne !)",
 ],
 contexte=(
  "Jacob, mourant en Égypte, convoque ses douze fils : « Rassemblez-vous, que je vous "
  "annonce ce qui arrivera dans la suite des jours » (49:1 — C8). Il commence par "
  "disqualifier les trois aînés : Ruben (l'inceste, 49:3-4), Siméon et Lévi (la violence "
  "de Sichem, 49:5-7). La primauté royale échoit donc au quatrième, Juda — « car Juda "
  "devint supérieur parmi ses frères, et de lui sortit le guide » (1Ch 5:2 — P029). "
  "L'oracle de Juda (49:8-12) est le plus long des douze : louange, lion, sceptre, "
  "Shilo, vigne et vin."
 ),
 explication=(
  "« Shilo » est le nom-titre du souverain à venir : « celui à qui il est », c'est-à-dire "
  "celui à qui appartiennent légitimement le sceptre (la souveraineté) et le bâton de "
  "commandement (le pouvoir de commander). Le « jusqu'à » borne la durée : le sceptre "
  "reste à Juda jusqu'à la venue du Légitime — après quoi, c'est lui qui règne, et non "
  "plus seulement sur Israël mais sur « les peuples ». Le lionceau devenu lion (49:9) "
  "dit la montée en puissance ; la vigne et le vin en surabondance (49:11-12 — on attache "
  "un âne à un cep précieux, on lave un vêtement dans du vin !) disent la prospérité "
  "du règne."
 ),
 interpretation=(
  "Le vrai nom de celui qui est devenu le Shilo promis est Jésus (voir 1962482) : par "
  "sa mère Marie, il possède le droit naturel à la royauté davidique ; par son père "
  "nourricier Joseph, le droit légal au sceptre. « Notre Seigneur est sorti de Juda » "
  "(Hé 7:14 — P029) ; il est « le lion de la tribu de Juda » (Ré 5:5 — P029). L'autorité "
  "de Christ a été accrue conformément à ce que Jacob avait prophétisé (voir 2002725 §8 "
  "— et F017 pour l'intronisation). L'obéissance « des peuples » dépasse Israël : c'est "
  "le programme du Royaume messianique (voir G007)."
  "Juda domine : à chaque recensement du désert, Juda est la tribu la plus nombreuse, "
  "et c'est elle qui marche en tête (Nb 2:3-9 — C8) ; après l'entrée en Canaan, « Juda "
  "montera le premier » (Jg 1:1-2 — C8). David, de Bethléhem de Juda, reçoit la dynastie "
  "(2S 7:12-16 — P029, et J008). Jésus naît de la tribu de Juda (Mt 1:1-3 — C8 ; Hé 7:14), "
  "est acclamé « Fils de David », puis intronisé Roi (voir F017) : le Légitime est venu, "
  "l'obéissance des peuples est en marche (voir I008, G007)."
 ),
 accomplissement=[
  ("Égypte", "Oracle sur le lit de Jacob"),
  ("Désert", "Juda marche en tête (Nb 2)"),
  ("Juges", "« Juda montera » (Jg 1:1-2)"),
  ("Bethléhem", "David, puis Jésus (Hé 7:14)"),
  ("Ré 5:5", "Le lion de la tribu de Juda"),
  ("F017", "Autorité accrue du Légitime"),
 ],
 hist=(
  "Prééminence durable : après le schisme consécutif à la mort de Salomon, Benjamin "
  "reste fidèle à Juda — car le Shilo promis devait sortir de Juda (voir 1962482 §61). "
  "La généalogie royale (Mt 1:1-17 — C8) fait le pont documentaire entre Juda et Jésus en "
  "trois fois quatorze générations. Attestation extra-biblique de la dynastie : la stèle "
  "araméenne de Tel Dan (IXe s., découverte 1993) mentionne la « maison de David » ; la "
  "stèle moabite de Mésha (~840) est lue par plusieurs épigraphistes avec la même formule."
 ),
 geo=(
  "Goshen (Égypte) : le lit de mort d'où part l'oracle ; Hébron : première capitale de "
  "David, en Juda (2S 2:1-4 — C8) ; Bethléhem de Juda : ville de David et du Christ "
  "(voir J003) ; Jérusalem : le trône ; le territoire de Juda (Jos 15 — C8), vignoble "
  "par excellence — la vallée d'Eshcol et ses grappes portées à deux (Nb 13:23 — C8) "
  "illustrent la vigne de 49:11."
 ),
 sci=(
  "Philologie : « Shilo » (šîlōh) se lit comme la contraction de « celui à qui [cela "
  "appartient] » — titre juridique, pas prénom. « Sceptre » (šēbeṭ) désigne aussi la "
  "tribu : le bâton fait le corps. « Obéissance » (49:10) traduit un terme rarissime, "
  "quasi-hapax, qui souligne le caractère unique de cette soumission. Viticulture : "
  "attacher une bête à un cep et laver au vin sont des images d'inversion — le précieux "
  "devient ordinaire — procédé poétique de la surabondance ; les pressoirs taillés dans "
  "le roc parsèment toujours les collines de Judée."
 ),
 limites=(
  "Le sens exact de « Shilo » est débattu chez les exégètes (lieu de Silo ? « le "
  "pacifique » ?) : cette fiche suit les publications — titre du Messie à qui appartient "
  "la souveraineté (2002725). La continuité précise du sceptre pendant l'exil et l'époque "
  "hasmonéenne n'est pas tranchée ici : Zorobabel, de la lignée davidique, est gouverneur "
  "au retour (Ag 2:23 — C8). Les versets 11-12 (vigne, vin, yeux, dents) sont lus au premier "
  "degré — prospérité du règne — sans allégorie forcée."
 ),
 tl=[("Lit de Jacob", "Oracle en Égypte"), ("Désert", "Juda en tête"), ("Juges", "« Juda montera »"),
     ("David", "Dynastie (J008)"), ("Bethléhem", "Le Légitime"), ("1914+", "Autorité accrue (F017)")],
 src=[("La fin approchant, cultivons l'obéissance (Shilo, 2002)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2002725"),
      ("Ils régneront avec le lion de Juda (droit naturel et légal)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1962482"),
      ("Genèse 49 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/1/49"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_J005_shilo.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J006", titre="L'étoile de Jacob — vue « pas maintenant, pas de près »",
 ref="Nombres 24:17-19 ; Nombres 24:17 ; 2 Samuel 8:2, 14 ; Matthieu 2:1, 2 ; Révélation 22:16",
 statut="Accomplie / À venir (P053, P573)",
 cat="J", syst="Système double horizon (David → Christ)",
 reg="Registre : Nombres — P053 (24:17-19 : étoile et sceptre), P573 (24:17 : étoile de Jacob)",
 texte=[
  "« Je le vois, NON MAINTENANT ; je le contemple, PAS DE PRÈS. » "
  "(24:17 — double distance !)",
  "« Une ÉTOILE sortira de Jacob, un SCEPTRE s'élèvera d'Israël. » (24:17 — astre et roi !)",
  "« Il brisera le FRONT de Moab, le crâne de tous les GUERRIERS VIOLENTS. » (24:17)",
  "« ÉDOM sera une possession, SÉIR une possession… Israël fera des exploits. » (24:18)",
  "« Celui qui sort de Jacob DOMINERA ; il fera périr les rescapés des villes. » (24:19)",
 ],
 contexte=(
  "Plaines de Moab, face à Jéricho : Balaq a fait venir Balaam de Péthor pour maudire, "
  "et trois fois Balaam a béni. Furieux, Balaq le congédie : « Fuis dans ton lieu ! » "
  "(24:10-11 — C8). Avant de partir, Balaam annonce « ce que ce peuple fera à ton peuple "
  "dans la suite des temps » (24:14 — C8) : quatrième oracle, le seul qui commence par "
  "une double clause de distance — ni maintenant, ni de près. L'horizon n'est plus le "
  "camp sous ses yeux, mais un roi à venir."
 ),
 explication=(
  "Dans la Bible, une « étoile » symbolise un prince glorieux : les rois de Jérusalem, "
  "assis sur le « trône de Jéhovah », furent comme des « étoiles de Dieu » (voir 1949762). "
  "Ici, l'étoile et le sceptre désignent ensemble un souverain issu de Jacob. Le premier "
  "accomplissement a lieu lorsque David devient roi, puis asservit les Moabites et les "
  "Édomites (voir it-2 « Nombres », 1200003279) — plus de 400 ans après Balaam (voir it-2 "
  "« Moab », 1200003097). Mais l'oracle vise plus loin : avant de partir, « le prophète "
  "de Pethor annonça que l'étoile messianique viendrait par la semence de Jacob » (voir "
  "it-1 « Balaq », 1200000546)."
 ),
 interpretation=(
  "Double horizon assumé : David d'abord, Christ définitivement. Moab (le front brisé) "
  "et Édom-Séir (la possession) sont les ennemis héréditaires d'Israël, écrasés par "
  "David (2S 8:2, 14 — P053) ; le Psaume 2, cité à l'accomplissement de P053, étend le "
  "programme au Roi oint brisant les nations — horizon messianique. Jésus lui-même "
  "revendique le titre : « Je suis… l'étoile brillante du matin » (Ré 22:16 — P053, "
  "P573). Des mages d'Orient — comme Balaam l'Oriental ! — verront « son étoile » et "
  "monteront à Jérusalem chercher le roi des Juifs (Mt 2:1, 2 — P573)."
  "David : Moab mesuré au cordeau et asservi au tribut, Édom couvert de garnisons "
  "(2S 8:2, 14 — P053), plus de quatre siècles après l'oracle. Bethléhem : l'astre vu en "
  "Orient conduit des mages au « roi des Juifs » (Mt 2:1, 2 — P573). Patmos : le Christ "
  "glorifié se nomme « l'étoile brillante du matin » (Ré 22:16 — P053, P573). Reste "
  "l'horizon du Psaume 2 — le bris définitif — qui appartient à l'avenir (voir I010) : "
  "le registre dit « Accomplie / À venir »."
 ),
 accomplissement=[
  ("Moab", "4e oracle : « pas maintenant »"),
  ("+400 ans", "David : Moab, Édom (2S 8:2, 14)"),
  ("Bethléhem", "« Son étoile » (Mt 2:1-2)"),
  ("Patmos", "« L'étoile du matin » (Ré 22:16)"),
  ("Ps 2", "Horizon : bris des nations"),
  ("I010", "Bris définitif (à venir)"),
 ],
 hist=(
  "Moab et Édom sont des royaumes historiques : la stèle de Mésha (~840, Louvre) "
  "raconte en moabite la révolte de Moab contre la maison d'Omri ; les annales "
  "assyriennes et les inscriptions égyptiennes nomment Édom-Séir. David, le premier "
  "accomplissement, est attesté hors de la Bible : stèle araméenne de Tel Dan (IXe s., "
  "« maison de David », 1993). Les mages (Mt 2) sont des savants orientaux — milieu "
  "babylonien où Daniel avait jadis dirigé les sages (Dn 2:48 — C8) et d'où pouvait "
  "venir, sept siècles plus tard, une attente nourrie de Nombres 24."
 ),
 geo=(
  "Le Pisga et les plaines de Moab : le point de vue de l'oracle, face à Jéricho ; "
  "l'Arnon : le fleuve-frontière de Moab, que l'étoile « brise » ; la montagne de Séir : "
  "le massif d'Édom au sud de la mer Morte, promis en « possession » ; la vallée du Sel, "
  "où David bat Édom (2S 8:13 — C8) ; Bethléhem : le second point de chute de l'étoile, "
  "sous les yeux des mages."
 ),
 sci=(
  "Philologie : le texte porte « le front de Moab » et, selon le TM, « tous les "
  "guerriers violents » — l'hébreu sous-jacent (« fils de Shéth ») est de lecture "
  "discutée, et la note de la Bible d'étude le signale. Astronomie : cette fiche ne "
  "propose AUCUNE identification de l'astre de Matthieu 2 (conjonction, comète, supernova) "
  "— voir les limites. Symbolique comparée : l'astre royal est un emblème courant dans "
  "l'Antiquité (étendards, monnaies, sceaux) ; la Bible l'emploie pour les princes "
  "glorieux (voir 1949762)."
 ),
 limites=(
  "L'origine de l'astre vu par les mages (Matthieu 2) n'est pas tranchée ici — voir les "
  "publications. Aucune explication astronomique naturaliste n'est proposée ni reprise. "
  "Le « bris » définitif d'Édom-Séir au sens du Psaume 2 appartient à l'horizon "
  "messianique final (voir I010) : aucune date. La lecture « fils de Shéth » de 24:17 "
  "reste discutée ; la fiche suit le TM et sa note."
 ),
 tl=[("Plaines de Moab", "4e oracle"), ("+400 ans", "David asservit"), ("Bethléhem", "« Son étoile » (Mt 2)"),
     ("Patmos", "« L'étoile du matin »"), ("Ps 2", "Horizon final"), ("I010", "Bris définitif")],
 src=[("Balaq — Étude perspicace (l'étoile messianique)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000546"),
      ("Moab — Étude perspicace (David, +400 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003097"),
      ("Nombres (Livre des) — Étude perspicace (1er accomplissement)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003279"),
      ("Nombres 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/24")],
 img="images/prophe_J006_etoile.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J007", titre="Balaam contraint — Dieu n'est pas homme pour mentir",
 ref="Nombres 23:19-24 ; Nombres 24:20-24 ; 1 Samuel 15:7, 8 ; 1 Chroniques 4:41-43",
 statut="Accomplie (P052, P054)",
 cat="J", syst="Système récits (Saül → Ézéchias → Grecs)",
 reg="Registre : Nombres — P052 (23:19-24 : Dieu ne ment pas, Israël lion), P054 (24:20-24 : Amalek, Kéniens, Kittim)",
 texte=[
  "« Dieu n'est pas HOMME pour mentir, ni fils d'homme pour regretter. » (23:19 — l'axiome !)",
  "« Il n'a pas aperçu de MALHEUR en Jacob, pas de misère en Israël. » (23:21 — innocenté !)",
  "« Des cornes comme celles du TAUREAU SAUVAGE. » (23:22 — la force du re'êm !)",
  "« Le peuple se lève comme une LIONNE, comme un LION… il ne se couche qu'après la proie. » "
  "(23:24 — le fauve !)",
  "« Amalek était la PREMIÈRE des nations, mais sa fin sera la PERDITION. » (24:20)",
  "« Des navires de KITTIM humilieront Assour, humilieront Éber. » (24:24 — l'ouest contre l'est !)",
 ],
 contexte=(
  "Balaam, devin renommé de Péthor sur l'Euphrate — « sans doute dans la haute vallée "
  "de l'Euphrate, près de Haran » (voir 1973722) — a été loué par Balaq, roi de Moab, "
  "pour maudire Israël. Trois stations panoramiques (Bamoth-Baal, le Pisga, le Péor), "
  "trois fois sept autels et trois fois la même surprise : la malédiction commandée "
  "sort en bénédiction. L'épisode de l'ânesse (ch. 22 — C8) a déjà montré qui mène : "
  "Balaam ne peut dire que ce que Jéhovah met dans sa bouche (22:38 — C8). Sans être "
  "Israélite, il connaissait Jéhovah et l'appela une fois « Jéhovah mon Dieu » (22:18 — "
  "voir it-1 « Balaam », 1200000543, et 1978288)."
 ),
 explication=(
  "Second oracle (ch. 23) : l'immutabilité divine — ce que Dieu a dit sur Israël (bénir), "
  "aucun salaire ne le changera. « Pas de malheur aperçu » ne dit pas la perfection "
  "d'Israël, mais son statut d'alliance : aux yeux du Juge qui l'a choisi, le peuple "
  "est innocenté. Le taureau sauvage (re'êm) et le lion disent une force qui ne négocie "
  "pas : le fauve ne se couche qu'après la proie. Oracles courts (24:20-24) : Amalek, le "
  "premier agresseur du désert (Ex 17:8-16 — C8), voué à l'effacement ; les Kéniens, "
  "pourtant alliés d'Israël, emportés dans le jugement d'Assour ; puis le basculement "
  "des empires — des navires venus de l'ouest (Kittim, les îles de Gn 10:4 — C8) "
  "humilient Assour et Éber, les puissances de l'est."
 ),
 interpretation=(
  "Nul ne peut maudire qui Dieu bénit : payé pour détruire, Balaam construit — il bénit "
  "Israël (trois oracles), annonce son roi (l'étoile, voir J006) et date la chute de ses "
  "ennemis. Amalek incarne l'inimitié héréditaire contre le peuple de Dieu : vouée à "
  "disparaître (Ex 17:14 — C8 ; Dt 25:17-19 — C8). Les Kéniens rappellent que la proximité "
  "ne protège pas du jugement collectif. Kittim contre Assour et Éber : les empires "
  "passent, humiliés à tour de rôle — le registre retient pour 24:24 les « conquêtes "
  "grecques »."
  "Israël-lion : le troisième oracle chante les tentes et la force (24:1-9 — P052), et "
  "David accomplit le programme en frappant Philistins, Moabites, Hadadézer et Édom "
  "(2S 8:1-14 — P052). Amalek : Saül frappe « depuis Havila jusqu'à Shur » (1S 15:7-8 — "
  "P054), puis sous Ézéchias cinq cents Siméonites exterminent le reste au mont Séir "
  "« jusqu'à ce jour » (1Ch 4:41-43 — P054) ; la haine amalécite survit jusqu'à Haman "
  "« l'Agaguite » (Est 3:1 — C8), pendu à sa propre potence. Kittim : l'expansion grecque "
  "(Alexandre, IVe s. — repère) humilie les puissances orientales — « conquêtes grecques » "
  "(P054)."
 ),
 accomplissement=[
  ("Péthor", "Bénir × 3 au lieu de maudire"),
  ("David", "Israël-lion (2S 8:1-14)"),
  ("Saül", "Amalek : Havila-Shur (1S 15:7-8)"),
  ("Ézéchias", "Séir : « jusqu'à ce jour » (1Ch 4:41-43)"),
  ("Perse", "Haman l'Agaguite (Est 3:1)"),
  ("IVe s.", "Kittim : conquêtes grecques"),
 ],
 hist=(
  "Saül contre Amalek (1S 15) : campagne datée du début de la monarchie, avec butin, "
  "roi captif (Agag) et exécution par Samuel — récit circonstancié, contrôlable dans sa "
  "logique (Havila-Shur = la piste du nord-Sinaï). Le reliquat du mont Séir sous Ézéchias "
  "(1Ch 4:41-43) clôt le dossier : « jusqu'à ce jour ». Haman « l'Agaguite » (Est 3:1) "
  "prolonge le nom d'Agag jusqu'à l'époque perse. Alexandre (Arbèles, 331 — repère "
  "conventionnel) brise l'empire oriental en une génération : l'ouest humilie l'est, "
  "comme annoncé."
 ),
 geo=(
  "Péthor sur l'Euphrate : le pays du devin, à ~600 km du camp d'Israël ; Bamoth-Baal, "
  "Pisga, Péor : les trois belvédères d'où Balaq espère une malédiction efficace ; "
  "Havila-Shur : l'axe des Amalécites entre Arabie et Égypte ; le mont Séir : le "
  "dernier refuge, pris par les Siméonites ; Kittim : les îles de l'ouest (Chypre et "
  "au-delà, Gn 10:4-5) — la direction d'où viendra Alexandre, par la mer."
 ),
 sci=(
  "Zoologie : le re'êm (23:22 ; 24:8) est le grand bœuf sauvage (aurochs) du Proche-Orient "
  "ancien — le TM dit « taureau sauvage » ; le lion et la lionne (23:24) sont la "
  "comparaison de force standard, ancrée dans une faune alors réelle (voir J010). "
  "Divination : « Balaam n'alla plus chercher des présages » (24:1 — C8) — rupture avec "
  "les techniques mésopotamiennes (hépatoscopie, libanomancie) : l'esprit de Dieu vient "
  "sur lui (24:2) et court-circuite le métier. Nautique : « des navires » comme vecteur "
  "d'empire — la puissance maritime occidentale (Grecs, puis Rome) contre les empires "
  "continentaux de l'est."
 ),
 limites=(
  "La miniature des Kéniens (24:21-23 — Caïn ravagé, Assour, « malheur à qui vivra ») "
  "reste obscure ligne à ligne : aucun découpage daté n'est proposé ici. Le dernier "
  "membre — « lui aussi sera détruit » (24:24b, Kittim ?) — n'est assigné à aucune "
  "puissance nommée. La fin du personnage — conseil de séduction (Nb 31:16 — C8), mort "
  "par l'épée (Nb 31:8 — C8), « voie de Balaam » (2P 2:15-16 ; Jude 11 ; Ré 2:14 — C8) — "
  "appartient à un autre dossier du registre."
 ),
 tl=[("Péthor", "Le devin loué"), ("3 stations", "Bénir × 3"), ("Saül", "Havila-Shur"),
     ("Ézéchias", "Mont Séir : fin"), ("Perse", "Haman l'Agaguite"), ("IVe s.", "Conquêtes grecques")],
 src=[("Balaam — Étude perspicace (devin, Jéhovah mon Dieu)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000543"),
      ("Un homme qui s'opposa à la volonté de Dieu (1978)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1978288"),
      ("Nombres 23 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/23"),
      ("Nombres 24 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/24")],
 img="images/prophe_J007_balaam.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J008", titre="La maison de David — Salomon nommé avant sa naissance",
 ref="2 Samuel 7:8-16 ; 1 Chroniques 22:9, 10 ; 1 Chroniques 17:14 ; Luc 1:32, 33",
 statut="Accomplie (P073, P522, P575)",
 cat="J", syst="Système règnes (David 40 ans → Salomon 40 ans)",
 reg="Registre : Samuel/Chroniques — P073 (2S 7:8-16 : maison et trône pour toujours), P522 (1Ch 22:9-10 : Salomon nommé, il bâtira), P575 (1Ch 17:14 : trône affermi pour toujours)",
 texte=[
  "« Je te ferai un GRAND NOM, comme le nom des grands de la terre. » (2S 7:9)",
  "« J'élèverai ta POSTÉRITÉ après toi… j'affermirai son règne. » (7:12)",
  "« Ce sera lui qui bâtira une MAISON à mon nom. » (7:13 — le fils bâtisseur !)",
  "« J'affermirai pour TOUJOURS le trône de son royaume. » (7:13 — toujours !)",
  "« Je serai pour lui un PÈRE, et il sera pour moi un FILS. » (7:14)",
  "« Voici qu'un fils te naîtra… SALOMON sera son nom… homme de REPOS… il bâtira. » "
  "(1Ch 22:9-10 — le nom avant la naissance !)",
 ],
 contexte=(
  "David est installé dans sa maison de cèdre pendant que l'arche loge sous une tente "
  "(7:1-2 — C8) ; Nathan approuve d'abord (« fais tout ce que tu as »), puis reçoit "
  "dans la nuit le correctif divin (7:3-7 — C8). Le renversement est total : ce n'est pas "
  "David qui bâtira une maison à Dieu, c'est Dieu qui bâtira une maison — une dynastie — "
  "à David (7:11 — C8). Motif du refus : David est un homme de guerre, qui a versé le "
  "sang (1Ch 22:8 — C8) ; le bâtisseur sera un homme de repos. L'alliance est conclue "
  "au cours du règne de David à Jérusalem (voir it-1 « Alliance », 1200011034)."
 ),
 explication=(
  "Double don, un seul mot : « maison » — la dynastie donnée à David, le temple à bâtir "
  "par son fils. « Salomon » signifie « Pacifique » (voir it-1 « David », 1200011102) : "
  "le nom porte le programme — repos des guerres et construction. « Pour toujours » "
  "(7:13, 16 ; 1Ch 17:14) dépasse par définition le règne d'un mortel : la promesse a "
  "deux étages, Salomon puis l'Héritier permanent. « Je serai son père » (7:14) scelle "
  "l'adoption royale — formule reprise pour le Christ (Hé 1:5 — C8). L'alliance avec "
  "David est une alliance pour le Royaume : un fils de sa lignée possédera le trône à "
  "jamais et bâtira une maison au nom de Jéhovah (voir 1200011034)."
 ),
 interpretation=(
  "Premier étage : Salomon — temple bâti, repos accordé, nom accompli. Étage définitif : "
  "Jésus, « l'Héritier permanent de l'alliance conclue avec David, pour le Royaume » "
  "(voir 1101965088) : Gabriel annonce à Marie que « Jéhovah Dieu lui donnera le trône "
  "de David son père, et il régnera sur la maison de Jacob à jamais » (Lc 1:32-33 — "
  "P073, P575). Le Psaume 89:3-4 chante l'alliance (« j'ai fait alliance avec mon élu » — "
  "P073) ; Matthieu 1:1 ouvre l'Évangile sur « Jésus Christ, fils de David » (P575). "
  "Ésaïe (9:6-7) et Jérémie (le « germe juste » suscité à David — voir 1200011102) "
  "prolongent la même ligne."
  "Salomon écrit à Hiram : le temple sera bâti « comme Jéhovah l'a dit à David » "
  "(1R 5:5 — P522) ; le chantier court de la 4e année à la 11e année (1R 6:1, 38 — P522 : "
  "sept ans). À la dédicace, Salomon proclame : « Jéhovah a accompli ce qu'il avait dit… "
  "je me suis levé à la place de David » (1R 8:17-20 — P073). L'Héritier : Gabriel (Lc "
  "1:32-33), la généalogie (Mt 1:1), la foule (« Hosanna au Fils de David » — C8, Mt 21:9), "
  "puis l'intronisation céleste (voir F017) : le trône affermi « pour toujours » a son "
  "titulaire définitif."
 ),
 accomplissement=[
  ("Alliance", "Une maison → une dynastie (2S 7:11)"),
  ("Nom", "« Salomon » avant la naissance (1Ch 22:9)"),
  ("4e-11e an", "Temple bâti : 7 ans (1R 6:1, 38)"),
  ("Dédicace", "« Jéhovah a accompli » (1R 8:17-20)"),
  ("Nazareth", "Gabriel : le trône de David (Lc 1:32-33)"),
  ("Mt 1:1", "« Fils de David » → F017"),
 ],
 hist=(
  "La dynastie est attestée hors de la Bible : stèle araméenne de Tel Dan (IXe s., "
  "découverte 1993 — « maison de David ») ; stèle de Mésha (~840) lue par plusieurs "
  "épigraphistes avec la même formule. Hiram de Tyr, le fournisseur du chantier (1R 5), "
  "est connu aussi par la tradition littéraire : l'historien Josèphe conserve son "
  "souvenir d'après Ménandre d'Éphèse (Contre Apion I, 18). Le récit du chantier (cèdre "
  "du Liban, pierres de taille, or, bronze, 1R 6-7 — C8) décrit une économie de palais "
  "orientale cohérente du Xe siècle."
 ),
 geo=(
  "Jérusalem : la ville de David, devenue capitale de la dynastie et du temple ; Tyr : "
  "le port d'Hiram, d'où le cèdre descend par mer jusqu'à Japho (2Ch 2:16 — C8) ; le "
  "Liban : la forêt des poutres ; le sanctuaire : 60 coudées sur 20, 30 de haut (1R 6:2 — "
  "C8) — environ 27 × 9 m avec la coudée commune (~45 cm). L'emplacement — le mont du "
  "Temple — n'est pas fouillable : aucun vestige direct du sanctuaire salomonien n'est "
  "attendu (voir les limites)."
 ),
 sci=(
  "Métrologie : la coudée commune (~45 cm) donne un sanctuaire d'environ 27 × 9 m pour "
  "11 m de haut — proportions 3:1, élancement modeste, couvrement sans pilier "
  "intermédiaire (poutres de cèdre). Chronologie interne : « la 480e année après la "
  "sortie d'Égypte » (1R 6:1 — C8) — système biblique interne, assumé comme tel et non "
  "converti ici (voir F pour les conversions). Chantier : sept ans pour le temple "
  "(6:38), treize pour le palais (7:1 — C8) — le texte lui-même fournit le comparatif "
  "de effort."
 ),
 limites=(
  "Les 480 ans de 1 Rois 6:1 appartiennent au système chronologique interne de la Bible : "
  "aucune conversion en dates absolues n'est proposée ici (voir la catégorie F). Aucun "
  "vestige direct du temple de Salomon n'existe — l'esplanade n'est pas fouillée et ne "
  "peut pas l'être : l'historicité du règne s'appuie sur les textes et les attestations "
  "dynastiques (Tel Dan), pas sur des pierres du sanctuaire. Hiram chez Josèphe est une "
  "tradition littéraire, pas une preuve. Le « pour toujours » s'accomplit en Christ : "
  "aucune date pour l'avenir."
 ),
 tl=[("Maison de cèdre", "Nathan : non, puis oui"), ("Alliance", "Maison → dynastie"), ("4e-11e an", "Temple : 7 ans"),
     ("Dédicace", "« Jéhovah a accompli »"), ("Nazareth", "Gabriel : le trône"), ("F017", "L'Héritier intronisé")],
 src=[("David — Étude perspicace (Salomon le Pacifique)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011102"),
      ("Alliance — Étude perspicace (l'alliance davidique)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011034"),
      ("Royaume — l'Héritier permanent (Lc 1:32-33)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965088"),
      ("2 Samuel 7 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/10/7")],
 img="images/prophe_J008_david.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J009", titre="La maison d'Éli jugée — le signe des deux fils en un jour",
 ref="1 Samuel 2:27-36 ; 1 Samuel 3:11-14 ; 1 Samuel 4:11-18 ; 1 Rois 2:26, 27",
 statut="Accomplie (P068, P069)",
 cat="J", syst="Système générations (Éli → Abiathar → Tsadoq)",
 reg="Registre : Samuel — P068 (1S 2:27-36 : maison d'Éli jugée, sacrificateur fidèle), P069 (1S 3:11-14 : Samuel confirme)",
 texte=[
  "« Je m'étais CLAIREMENT révélé à la maison de ton père en Égypte. » (2:27 — la grâce rappelée !)",
  "« Tu honores tes fils PLUS QUE MOI. » (2:29 — le réquisitoire en une phrase !)",
  "« LOIN DE MOI !… ceux qui me méprisent seront AVILIS. » (2:30 — la révocation !)",
  "« Je RETRANCHERAI ton bras et le bras de la maison de ton père. » (2:31 — le bras brisé !)",
  "« Tes DEUX FILS mourront LE MÊME JOUR — ceci te sera un SIGNE. » (2:34 — le signe daté !)",
  "« Je me susciterai un sacrificateur FIDÈLE… maison STABLE… devant mon OINT. » (2:35)",
 ],
 contexte=(
  "Silo, sanctuaire central (Jos 18:1 — C8). Les fils du grand prêtre Éli, Hophni et "
  "Phinéhas, rackettent les sacrifices au trident (2:12-17 — C8) et couchent avec les "
  "femmes à l'entrée de la tente (2:22 — C8). Éli, vieux et pesant, se contente d'une "
  "réprimande molle (2:23-25 — C8). En contraste, le petit Samuel « grandissait » devant "
  "Jéhovah (2:21, 26 — C8). C'est alors qu'arrive un homme de Dieu anonyme — comme celui "
  "de Béthel (voir J002) : pas de nom, pas de CV, une sentence. Samuel enfant recevra "
  "ensuite la confirmation nocturne : « les deux oreilles de quiconque l'entendra "
  "tinteront » (3:11 — P069)."
 ),
 explication=(
  "Le réquisitoire a trois temps : la grâce passée (l'élection en Égypte, 2:27-28), le "
  "crime présent (mépriser le sacrifice et engraisser la famille, 2:29), la sentence "
  "(2:30-36). « Loin de moi ! » révoque la promesse conditionnelle faite à la maison "
  "d'Aaron : l'élection ne protège pas du jugement. « Retrancher le bras » (2:31), c'est "
  "briser la force sacerdotale de la lignée. Le signe est daté au jour près : Hophni et "
  "Phinéhas mourront « le même jour » (2:34). Et le vide sera comblé : un « sacrificateur "
  "fidèle », à la « maison stable », marchant « devant mon oint » — au service du roi "
  "davidique à venir (2:35)."
 ),
 interpretation=(
  "L'accomplissement de cette prophétie — rejet de la maison d'Éli (1S 2:31 ; 3:12-14 ; "
  "1R 2:27) — est présenté comme une preuve de l'authenticité du livre de Samuel (voir "
  "it-1 « Samuel (Livres de) », 1200013736). Le « sacrificateur fidèle » est Tsadoq : "
  "Salomon dépose Abiathar, dernier pontife éliade, et établit Tsadoq (1R 2:26-27, 35 — "
  "C8, P068) — « pour accomplir la parole de Jéhovah dite à Silo » (2:27 : le texte "
  "lui-même fait le lien !). Les « fils de Tsadoq » garderont le sanctuaire jusque dans "
  "la vision d'Ézéchiel (Éz 44:15 — C8)."
  "Apheq : l'arche est prise, Hophni et Phinéhas meurent le même jour (4:11 — P068) ; "
  "Éli, 98 ans, 40 ans de juge, tombe de son siège et se brise le cou (4:15-18 — P068). "
  "Nob : Saül fait tuer 85 prêtres par Doëg ; seul Abiathar s'échappe (22:18-20 — P068). "
  "Anathoth : Salomon exile Abiathar — « pour accomplir la parole » (1R 2:26-27 — P068). "
  "Trois générations, trois lieux, une sentence : la maison d'Éli sort du sanctuaire, "
  "la maison de Tsadoq y entre."
 ),
 accomplissement=[
  ("Silo", "Sentence de l'anonyme (2:27-36)"),
  ("Nuit", "Samuel confirme (3:11-14, P069)"),
  ("Apheq", "Les deux fils le même jour (4:11)"),
  ("Nob", "85 prêtres (22:18-20)"),
  ("Anathoth", "Abiathar déposé (1R 2:26-27)"),
  ("Jérusalem", "Tsadoq, maison stable"),
 ],
 hist=(
  "Apheq (plaine de Sharon) et Ében-Ézer : le champ de bataille de 1 Samuel 4, sur la "
  "route des Philistins vers l'intérieur. Nob, ville sacerdotale au nord de Jérusalem, "
  "rayée par Saül (22:19 — C8). Anathoth, ville lévitique d'exil d'Abiathar — patrie, "
  "trois siècles plus tard, de Jérémie (Jr 1:1 — C8). Silo : les fouilles (Shiloh) "
  "placent une destruction vers le milieu du XIe siècle — l'horizon des Philistins de "
  "1 Samuel 4 (repère archéologique, non preuve datée)."
 ),
 geo=(
  "Silo (collines d'Éphraïm) : le sanctuaire jugé ; Apheq ↔ Ében-Ézer : les deux camps, "
  "à une journée de marche ; Nob : la ville des pains de proposition, à vue de "
  "Jérusalem ; Anathoth : à quelques kilomètres au nord-est, l'exil à domicile "
  "d'Abiathar ; Jérusalem : le sanctuaire définitif, où officiera Tsadoq. La géographie "
  "de la sentence va du sanctuaire perdu (Silo) au sanctuaire promis (Jérusalem), en "
  "passant par le sang (Nob)."
 ),
 sci=(
  "Onomastique : Hophni et Phinéhas portent des noms égyptiens — Phinéhas (« le Nubien ») "
  "est bien identifié — en plein sacerdoce israélite : clin d'œil du récit à 2:27 (« en "
  "Égypte »), la maison replonge dans ce dont elle était sortie. Médecine : Éli, « pesant » "
  "(4:18), 98 ans, aveugle (4:15), meurt d'une chute en arrière — rupture cervicale du "
  "vieillard obèse : tableau médico-légal cohérent. Démographie : 85 prêtres à Nob (22:18) "
  "plus femmes, enfants et bétail (22:19) — une ville sacerdotale entière."
 ),
 limites=(
  "L'identification du « sacrificateur fidèle » à Tsadoq est suivie ici via 1 Rois 2:35 "
  "— la lignée tsadoqite postérieure (Éz 44:15 cité, non commenté) n'est pas développée. "
  "La destruction de Silo au XIe siècle est un repère archéologique, pas une preuve "
  "datée de 1 Samuel 4. La mort des fils « le même jour » est le signe demandé et reçu : "
  "cette fiche n'en propose aucune reconstitution tactique. L'homme de Dieu reste anonyme "
  "— le texte ne donne aucun nom à chercher."
 ),
 tl=[("Silo", "Trident et scandale"), ("Anonyme", "Sentence + signe"), ("Nuit", "Samuel confirme (P069)"),
     ("Apheq", "Le même jour"), ("Nob", "85 prêtres"), ("Anathoth", "« Pour accomplir »")],
 src=[("Samuel (Livres de) — Étude perspicace (preuve d'authenticité)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013736"),
      ("1 Samuel 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/9/2"),
      ("1 Samuel 4 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/9/4"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_J009_eli.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J010", titre="Samson annoncé — naziréen dès le ventre, il commencera",
 ref="Juges 13:3-5 ; Juges 13:24 ; Juges 14:5—16:31 ; Hébreux 11:32 (C8)",
 statut="Accomplie (P979)",
 cat="J", syst="Système cycles (40 ans oppression → 20 ans juge)",
 reg="Registre : Juges — P979 (Jg 13:3-5 : un fils, naziréen, il sauvera Israël des Philistins)",
 texte=[
  "« Tu es STÉRILE… mais tu concevras et tu enfanteras un fils. » (13:3 — le schéma de Sara !)",
  "« Ne bois ni VIN ni boisson enivrante, ne mange rien d'IMPUR. » (13:4 — le régime de la mère !)",
  "« Le RASOIR ne passera pas sur sa tête. » (13:5 — le signe visible !)",
  "« L'enfant sera NAZIRÉEN de Dieu DÈS LE VENTRE. » (13:5 — à vie, dès avant de naître !)",
  "« C'est lui qui COMMENCERA à sauver Israël de la main des Philistins. » (13:5 — commencera !)",
 ],
 contexte=(
  "« Les fils d'Israël firent de nouveau ce qui est mauvais… Jéhovah les livra aux "
  "Philistins pendant quarante ans » (13:1). À Tsoréa, en Dan, la femme stérile de Manoah "
  "reçoit deux visites de l'ange (13:3-5, puis 13:9-14 — C8) ; le régime de naziréat est "
  "répété trois fois (13:4, 7, 14 — C8). L'holocauste monte dans la flamme et l'ange "
  "avec lui (13:19-21 — C8). « Jéhovah bénissait » l'enfant, et « l'esprit de Jéhovah "
  "commença à l'agiter à Mahané-Dan » (13:24-25 — C8). Avant même d'être conçu, Samson "
  "avait une tâche assignée (voir 2005206)."
 ),
 explication=(
  "Stérilité + annonce + nom de mission : le schéma de Sara (voir J004) et d'Anne (1S 1 — "
  "C8). Le naziréat (Nb 6 — C8 : pas de vin, pas de cadavre, pas de rasoir) est ici à vie "
  "et dès le ventre — régime imposé d'abord à la mère, comme pour Jean-Baptiste (« ni vin "
  "ni boisson », Lc 1:15 — C8). Le verbe décisif est « COMMENCERA » (yāḥēl) : la mission "
  "est partielle par cahier des charges — « ce sera lui qui commencera à délivrer Israël » "
  "(voir 1962600). Samson n'est pas chargé d'achever, mais d'entamer : vingt ans de "
  "brèches (16:31 — C8), pas l'extermination."
 ),
 interpretation=(
  "La force de Samson est l'esprit de Jéhovah, pas le muscle : l'esprit « s'empare » de "
  "lui à chaque exploit (14:6, 19 ; 15:14 — C8), et se retire quand le signe est trahi "
  "(16:19-20 — C8). Les cheveux ne sont pas la source, mais le signe du vœu. Naziréen "
  "touchant des cadavres ? Sa mission de juge — « délivrer Israël » — l'amenait à tuer ; "
  "consacré à vie, il ne pouvait « recommencer » son naziréat comme un vœu temporaire "
  "(voir 1969088). Il figure parmi les hommes de foi (Hé 11:32 — C8) : « par leur foi, "
  "ils furent vaillants » (voir 1962600)."
  "Naissance : « la femme enfanta un fils et l'appela Samson » (13:24 — P979). Puis le "
  "programme de 14:5 à 16:31 (P979) : le lion de Timna déchiré à mains nues (14:5-9), les "
  "trente d'Ashkelon (14:19), « cuisse et hanche » (15:8), les mille de Léhi à la "
  "mâchoire fraîche (15:14-16), les portes de Gaza arrachées (16:3), et le final : "
  "arc-bouté aux deux colonnes de Dagon, « il tua plus d'ennemis à sa mort que de son "
  "vivant » — quelque trois mille (16:27-30 — voir 2005206, 1962600)."
 ),
 accomplissement=[
  ("Tsoréa", "Annonce à la stérile (13:3-5)"),
  ("Naissance", "« Jéhovah bénissait » (13:24)"),
  ("20 ans", "Juge en Israël (16:31)"),
  ("Timna-Léhi", "Lion, trente, mille (ch. 14-15)"),
  ("Gaza", "Les portes arrachées (16:3)"),
  ("Dagon", "Plus qu'en sa vie (16:27-30)"),
 ],
 hist=(
  "Les Philistins relèvent des Peuples de la mer illustrés par les reliefs égyptiens de "
  "Médinet Habou (XIIe s.) ; leur pentapole — Gaza, Ashkelon, Ashdod, Ékron, Gath "
  "(Jos 13:3 — C8) — verrouille la côte. Monopole du fer : « il n'y avait pas de forgeron "
  "dans tout Israël » (1S 13:19-22 — C8) — la supériorité matérielle qui rendait "
  "l'oppression sans issue… et la mâchoire d'âne inévitable. Le temple à deux colonnes "
  "centrales : à Tell Qasile, un sanctuaire philistin du XIIe siècle repose sur deux "
  "piliers — le dispositif architectural de Juges 16 (analogie, voir les limites)."
 ),
 geo=(
  "Tsoréa et Eshtaol (piémont danite) : le pays de Manoah ; Timna : le lion et le "
  "mariage ; Ashkelon : les trente dépouillés ; Léhi (Ramath-Léhi, « hauteur de la "
  "mâchoire ») : les mille ; Gaza : les portes portées vers Hébron ; la vallée de Sorek : "
  "Delila et la trahison (16:4 — C8) ; le temple de Dagon : le tombeau commun. Chaque "
  "exploit est ancré : la fiche suit la piste, ville par ville."
 ),
 sci=(
  "Zoologie : le « jeune lion » (kephîr) de Timna — les lions asiatiques peuplaient le "
  "Levant jusqu'à l'époque romaine. Apiculture : l'essaim et le miel « dans le corps du "
  "lion » (14:8-9 — C8) — une carcasse séchée au soleil offre une cavité sèche comme une "
  "autre aux abeilles opportunistes. Armement improvisé : la mâchoire d'âne « fraîche » "
  "(15:15) — encore souple et résistante — comme arme de choc ; les portes de Gaza "
  "(16:3) arrachées avec barres : le texte attribue l'effort à l'esprit, pas au muscle "
  "(voir les limites)."
 ),
 limites=(
  "Les chiffres des exploits (les mille de Léhi, les trois mille de Dagon) sont le texte "
  "reçu : aucune reconstitution tactique n'est proposée. La force est un don de l'esprit : "
  "aucune explication biomécanique ne la « rend crédible » ni ne la remplace. Tell Qasile "
  "est une analogie architecturale (temple à deux colonnes), pas le temple de Gaza. La vie "
  "privée de Samson (Timna, Delila) n'est racontée que dans la mesure où elle sert la "
  "mission : cette fiche est une fiche de prophétie, pas une biographie."
 ),
 tl=[("40 ans", "Oppression philistine"), ("Tsoréa", "Double visite"), ("Naissance", "« Jéhovah bénissait »"),
     ("20 ans", "Juge en Israël"), ("Léhi", "Les mille"), ("Dagon", "Plus qu'en sa vie")],
 src=[("Samson a triomphé grâce à la force de Jéhovah", "https://wol.jw.org/fr/wol/d/r30/lp-f/2005206"),
      ("Soyez fort, comme Samson ! (commencera, 20 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1962600"),
      ("Samson naziréen et les cadavres (Questions, 1969)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1969088"),
      ("Juges 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/7/13")],
 img="images/prophe_J010_samson.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="J011", titre="Houlda à Josias — « recueilli en paix » avant la tempête",
 ref="2 Rois 22:15-20 ; 2 Chroniques 34:23-28 (C8) ; 2 Rois 23:29, 30 ; 2 Chroniques 35:23, 24",
 statut="Accomplie (P099)",
 cat="J", syst="Système règne (8 ans → 18e année → 31 ans)",
 reg="Registre : Rois — P099 (2R 22:15-20 : Josias recueilli en paix, il ne verra pas le malheur)",
 texte=[
  "« Je fais venir du MALHEUR sur ce lieu… parce qu'ils m'ont abandonné. » (22:16-17 — la nation condamnée !)",
  "« Parce que ton cœur s'est ATTENDRI… tu as déchiré tes vêtements… tu as PLEURÉ devant moi… » "
  "(22:19 — le dossier du roi !)",
  "« Moi aussi je t'ai ENTENDU, déclare Jéhovah. » (22:19 — entendu !)",
  "« Je te réunirai à tes ANCÊTRES. » (22:20 — auprès des pères !)",
  "« Dans la PAIX, tu seras déposé dans ta tombe. » (22:20 — en paix !)",
  "« Tes YEUX ne verront pas tout le malheur que je fais venir sur ce lieu. » (22:20 — épargné du spectacle !)",
 ],
 contexte=(
  "Dix-huitième année de Josias : pendant la réparation du Temple, Hilqiya trouve « le "
  "livre de la Loi » (22:8 — C8) ; à sa lecture, le roi déchire ses vêtements (22:11 — "
  "C8). Une délégation de cinq — Hilqiya, Ahiqam, Akbor, Shaphân, Asaya (22:12-14 — C8) "
  "— va consulter la prophétesse Houlda, femme de Shalloum le garde-robe, habitant le "
  "second quartier de Jérusalem (22:14 : état civil complet !). Un an avant Béthel "
  "(voir J002), la prophétesse parle : double oracle — la nation est condamnée, le roi "
  "est épargné. Parallèle : 2 Chroniques 34:23-28 (C8). Jérémie prophétise pourtant "
  "depuis la 13e année de Josias (Jr 1:2 — C8), et Sophonie sous Josias (So 1:1 — C8) : "
  "la délégation va à Houlda — le texte ne dit pas pourquoi (voir les limites)."
 ),
 explication=(
  "« Cœur attendri » (rak) : le contraire du cœur endurci de Manassé et d'Amon — "
  "déchirer ses vêtements et pleurer « devant moi », c'est le repentir documenté, et "
  "« je t'ai entendu » en est le récépissé. « Réuni à tes ancêtres » est l'expression "
  "de la mort (note TM) : Josias mourra avant la catastrophe et rejoindra le sépulcre "
  "de ses pères (voir 1965082 §29-30). « En paix » (beshalom) ne promet pas une mort "
  "douce — Josias mourra blessé au combat — mais une mort à l'abri : « tes yeux ne "
  "verront pas » le malheur. La paix ici, c'est l'épargne du spectacle."
 ),
 interpretation=(
  "Le repentir personnel ne détourne pas le jugement national : le malheur viendra "
  "quand même (22:16-17), mais le repentant ne le verra pas. Josias, « l'un des rois "
  "fidèles » qui ramena son peuple à la loi pour éviter le désastre (voir 1965082 §29), "
  "reçoit le salaire de l'obéissance : le repos avant la tempête. La promesse est "
  "nominative et datée par sa mort même : tout le reste du règne — la Pâque de la 18e "
  "année (23:21-23 — C8, « pas de Pâque pareille depuis les juges »), la réforme jusqu'à "
  "Béthel (voir J002) — se joue sous cette parole."
  "Meguiddo : le pharaon Néco monte vers l'Euphrate ; Josias, contre « les paroles de "
  "Neco qui venaient de la bouche de Dieu » (2Ch 35:22 — C8), tente de lui barrer la "
  "route et est mortellement blessé par les archers (2Ch 35:23 — P099). Transbordé sur "
  "un second char, ramené à Jérusalem, il meurt en chemin ou à l'arrivée (voir it-1 "
  "« Josias », 1200012469) et « fut enterré dans le sépulcre de ses pères » (2Ch 35:24 — "
  "P099 ; 2R 23:29-30 — P099). « Tout Juda et Jérusalem pleurèrent Josias » (2Ch 35:24). "
  "Quatre rois lui succèdent, puis vient ce que ses yeux n'ont pas vu (2R 23:31—25:21 — "
  "C8, sans date)."
 ),
 accomplissement=[
  ("18e année", "Le livre trouvé (22:8)"),
  ("Houlda", "Double oracle (22:15-20)"),
  ("Pâque", "« Pas de pareille » (23:21-23)"),
  ("Béthel", "Réforme jusqu'au nord (J002)"),
  ("Meguiddo", "Blessé par les archers (2Ch 35:23)"),
  ("Jérusalem", "Sépulcre des pères (35:24)"),
 ],
 hist=(
  "Neco II (XXVIe dynastie, Saïs) : le pharaon de la fin de l'Assyrie, en marche vers "
  "Carkémish — cadre géopolitique du choc. Meguiddo : le tell-verrou de la Via Maris "
  "(voir I009 — le même tell que Har-Maguédon !), fouillé depuis un siècle (portes, "
  "écuries, niveaux de destructions). Josias : 8 ans à l'avènement, 31 ans de règne "
  "(22:1 — C8) — la chronologie interne tient : 18e année (le livre), réforme, Pâque, "
  "puis Meguiddo. Le deuil national (« tout Juda et Jérusalem ») est attesté par les "
  "deux récits (Rois et Chroniques)."
 ),
 geo=(
  "Le second quartier (Mishné) : l'extension ouest de Jérusalem, où habite Houlda — le "
  "« Mur Large » dégagé par les fouilles (Avigad, quartier juif) illustre cette "
  "extension à l'époque royale. La Via Maris : la route côtière que Neco emprunte et que "
  "Josias veut couper ; Meguiddo : le défilé qui commande la plaine de Yizréel ; "
  "Jérusalem : le retour en char et le sépulcre des pères, dans la cité de David. "
  "Carkémish sur l'Euphrate : la destination de Neco, jamais atteinte avec Josias "
  "vivant."
 ),
 sci=(
  "Médecine : « les archers tirèrent sur le roi » (2Ch 35:23) — blessures de guerre par "
  "flèches, hémorragie, transbordement (premier char → second char, 2Ch 35:24) : la "
  "logistique d'évacuation d'un blessé royal, mort en route ou à l'arrivée (voir "
  "1200012469). Balistique antique : arcs composites, chars, archers — l'arme qui tue à "
  "distance, cohérente avec un roi au combat. Psychologie du texte : « pour une raison "
  "que la Bible ne révèle pas » (voir 1200012469), Josias ignore l'avertissement — le "
  "récit assume son silence."
 ),
 limites=(
  "Pourquoi Houlda plutôt que Jérémie (en activité depuis la 13e année) ou Sophonie ? Le "
  "texte ne motive pas le choix de la délégation : cette fiche ne spécule pas. « Les "
  "paroles de Neco qui venaient de la bouche de Dieu » (2Ch 35:22) sont l'affirmation du "
  "Chroniqueur ; le mécanisme n'est pas expliqué. La date de Meguiddo n'est pas "
  "convertie ici (repère conventionnel, système du règne seul). « En paix » est défini "
  "par le contexte — épargné du spectacle — et non comme une mort sans souffrance : "
  "Josias meurt de ses blessures."
 ),
 tl=[("8 ans", "Avènement"), ("13e année", "Jérémie appelé (C8)"), ("18e année", "Le livre trouvé"),
     ("Houlda", "Double oracle"), ("+13 ans", "Pâque, Béthel (J002)"), ("Meguiddo", "Recueilli en paix")],
 src=[("Josias — Étude perspicace (Houlda, Meguiddo, Neco)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012469"),
      ("Les morts qui doivent ressusciter (recueilli, 1965)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965082"),
      ("2 Rois 22 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/22"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_J011_houlda.jpg",
))
