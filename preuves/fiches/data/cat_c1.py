#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE A-C (vague de transition) — FIN DES NATIONS + LE MESSIE (1re partie)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="A–C",
    nom="Fin des nations · Le Messie : origine et naissance (1re partie)",
    vague="3",
    intro=(
        "Cette vague de transition ferme la catégorie A et ouvre la catégorie C. "
        "Côté nations, quatre oracles restaient à traiter : Damas, frappée deux fois, "
        "par l'Assyrie puis par Babylone ; Kédar et les campements de Hatsor, la gloire "
        "des archers du désert ; Élam, dont l'arc est brisé ; et l'Assyrie elle-même, "
        "la verge jugée en une nuit sous les murs de Jérusalem. Côté Messie, cinq "
        "premières fiches suivent l'enfant annoncé : le lieu de sa naissance, sa mère, "
        "sa fuite puis son retour d'Égypte, le deuil qui accompagne sa venue, et le "
        "messager qui marche devant lui. Mêmes dix blocs, mêmes règles : un seul "
        "système chronologique par fiche, aucune date pour l'avenir, et des limites "
        "écrites noir sur blanc."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="A010", titre="Damas — ôtée du nombre des villes",
 ref="Ésaïe 17:1-3 ; Amos 1:3-5 ; Jérémie 49:23-27 ; 2 Rois 16:9",
 statut="Accomplie",
 cat="A", syst="Dates neutres (765, 734, 732)",
 reg="Registre : Ésaïe — P115, P131 ; Jérémie — P280 ; Amos — P430",
 texte=[
  "« Voici Damas ôtée du nombre des villes ; elle deviendra un tas de ruines. » (Is 17:1)",
  "« J'enverrai un feu dans la maison de Hazaël ; il dévorera les palais de Ben-Hadad. "
  "Je briserai les verrous de Damas, et le peuple sera exilé à Qir. » (Am 1:4-5)",
  "« Je mettrai le feu à la muraille de Damas ; il dévorera les palais de Ben-Hadad. » (Jr 49:27)",
  "« Le roi d'Assyrie monta contre Damas, s'en empara, en déporta les habitants à Qir, "
  "et fit mourir Retsîn. » (2R 16:9)",
 ],
 contexte=(
  "Deux oracles à cinquante ans d'intervalle visent la même capitale. Amos prophétise "
  "vers 765, sous Jéroboam II, quand Damas domine encore la Syrie. Ésaïe reprend "
  "l'oracle vers 734, en pleine guerre syro-éphraïmite : Retsîn de Damas et Péqah "
  "d'Israël assiègent Achaz de Juda pour le forcer à entrer dans leur coalition "
  "anti-assyrienne. Achaz refuse le signe de Dieu, paie tribut à Tiglath-Piléser III "
  "et l'appelle au secours. Jérémie, deux siècles plus tard, annonce un second "
  "châtiment de Damas, à l'époque babylonienne."
 ),
 explication=(
  "« Ôtée du nombre des villes » ne veut pas dire rasée sans retour : l'expression "
  "vise le statut de la cité — capitale d'un royaume araméen indépendant, avec "
  "« royauté à Damas » (Is 17:3). Amos nomme la dynastie : la maison de Hazaël, les "
  "palais des Ben-Hadad, et le lieu de l'exil, Qir. Le texte d'Ésaïe enveloppe dans "
  "le même jugement Éphraïm, l'allié d'occasion devenu païen par son alliance. "
  "L'oracle de Jérémie 49:23-27, lui, suppose une Damas relevée : c'est un second "
  "jugement, exécuté par d'autres mains."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que le premier oracle s'est accompli "
  "par Tiglath-Piléser III : répondant à l'appel d'Achaz, l'Assyrien envahit la "
  "Syrie, prit Damas en 732, mit à mort Retsîn et déporta la population à Qir, "
  "exactement comme 2 Rois 16:9 le rapporte. Les publications retiennent que les "
  "documents assyriens nomment Rezôn de Damas parmi les tributaires du roi avant la "
  "rupture. Le second oracle, celui de Jérémie, est rattaché aux campagnes de "
  "Nebucadnetsar : Damas, devenue province disputée, subit le sort commun des cités "
  "syriennes au VIe siècle."
 ),
 accomplissement=[
  ("765 av. n. è. env.", "Amos annonce le feu sur la maison de Hazaël et l'exil à Qir"),
  ("735-734 av. n. è.", "Guerre syro-éphraïmite contre Achaz ; Ésaïe 17 reprend l'oracle contre Damas"),
  ("733-732 av. n. è.", "Campagne de Tiglath-Piléser III en Syrie ; prise de Damas"),
  ("732 av. n. è.", "Retsîn mis à mort ; habitants déportés à Qir ; fin du royaume araméen de Damas"),
  ("VIe s. av. n. è.", "Second châtiment à l'époque babylonienne (Jérémie 49:23-27) ; Damas province disputée"),
 ],
 hist=(
  "L'article Tiglath-Piléser III de l'Étude perspicace relève que les documents "
  "assyriens citent Minihimmé (Menahem), Rezôn (Retsîn) de Damas et Hiram de Tyr "
  "comme tributaires du roi : la pression fiscale précède la rupture. 2 Rois 16:9 "
  "fournit le procès-verbal biblique : prise de la ville, déportation à Qir, mort "
  "de Retsîn. Les annales assyriennes de Nimrud (Calach) décrivent la campagne de "
  "733-732, la chute de la ville et le tribut des rois syriens. La stèle araméenne "
  "de Tel Dan (IXe siècle), qui nomme un roi d'Aram vainqueur de rois israélites, "
  "atteste par ailleurs la puissance de la Damas que les prophètes ont vue tomber."
 ),
 geo=(
  "Damas occupe l'oasis du Barada, au pied de l'Anti-Liban : la Ghouta, jardin "
  "irrigué au bord du désert, explique trois mille ans d'occupation. Carrefour des "
  "routes de Mésopotamie, de Phénicie et du Hauran, la ville commande le passage "
  "entre l'Euphrate et la côte. Les « fleuves de Damas », Abana et Parpar (2R 5:12), "
  "sont les cours d'eau de cette oasis. Qir, lieu de la déportation, est nommé "
  "aussi en Amos 9:7 comme pays d'origine des Syriens : un retour forcé aux marges, "
  "dont la localisation exacte reste débattue."
 ),
 sci=(
  "Damas compte parmi les villes habitées en continu depuis le plus longtemps, ce "
  "qui limite paradoxalement la fouille : les niveaux du VIIIe siècle dorment sous "
  "la ville moderne et la citadelle médiévale. L'épigraphie compense : outre les "
  "annales de Tiglath-Piléser III, les inscriptions de Salmanasar III nomment déjà "
  "Hazaël de Damas comme adversaire, confirmant la dynastie visée par Amos 1:4. La "
  "toponymie de la Ghouta et le tracé des canaux du Barada, étudiés par les "
  "hydrologues, confirment l'assise agricole qui faisait la richesse convoitée de "
  "la cité."
 ),
 limites=(
  "Damas est aujourd'hui une capitale peuplée de plusieurs millions d'habitants : "
  "cette fiche ne prétend pas que le site est vide. L'oracle, comme le verset 3 le "
  "précise, vise la royauté araméenne de Damas, qui a cessé en 732 et ne s'est "
  "jamais relevée comme puissance indépendante. La localisation de Qir n'est pas "
  "établie avec certitude. Les dates 765, 734 et 732 sont des dates neutres, "
  "communes à toutes les chronologies."
 ),
 tl=[("765", "Amos"), ("734", "Ésaïe 17"), ("732", "Prise de Damas"),
     ("732", "Mort de Retsîn"), ("VIe s.", "Second châtiment")],
 src=[("Tiglath-Piléser (III) — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200004402"),
      ("Retsîn — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003721"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Ésaïe 17 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/17")],
 img="images/prophe_A010_damas.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="A011", titre="Kédar et Hatsor — la gloire des archers du désert",
 ref="Ésaïe 21:13-17 ; Jérémie 49:28-33 ; Ézéchiel 27:21",
 statut="Accomplie",
 cat="A", syst="Dates neutres (VIIe-Ve s.)",
 reg="Registre : Ésaïe — P137 ; Jérémie — P281",
 texte=[
  "« Dans un an, toute la gloire de Kédar s'achèvera ; il ne restera que peu "
  "d'archers, les guerriers des fils de Kédar. » (Is 21:16-17)",
  "« Levez-vous, montez contre Kédar, détruisez les fils de l'Orient ! On prendra "
  "leurs tentes et leurs troupeaux, leurs tentures et tous leurs effets. » (Jr 49:28-29)",
  "« Hatsor deviendra un repaire de chacals, une désolation pour toujours ; personne "
  "n'y habitera. » (Jr 49:33)",
  "« Nebucadnetsar, roi de Babylone, a pris une résolution contre vous. » (Jr 49:30)",
 ],
 contexte=(
  "Kédar, deuxième fils d'Ismaël (Gn 25:13), a donné son nom à une confédération de "
  "tribus arabes nomades du désert syro-arabe : éleveurs de moutons, de chèvres et "
  "de chameaux, caravaniers de l'encens, archers redoutés. Ésaïe les vise au temps "
  "de la domination assyrienne ; Jérémie, un siècle plus tard, nomme l'exécutant : "
  "Nebucadnetsar. Ézéchiel les montre fournisseurs de Tyr en agneaux et en boucs "
  "(Éz 27:21) : leur gloire est pastorale et militaire, pas urbaine."
 ),
 explication=(
  "« La gloire de Kédar », ce sont ses puissants archers et ses troupeaux : un "
  "peuple sans ville a une gloire mobile, et c'est elle qui sera fauchée « dans un "
  "an ». Les « royaumes de Hatsor » ne sont pas la Hatsor cananéenne du nord "
  "(Tel Hatsor en Galilée), mais des campements retranchés du désert d'Arabie, à "
  "l'est du Jourdain — l'Étude perspicace distingue soigneusement les deux Hatsor. "
  "« Fils de l'Orient » est le nom générique des tribus du désert, et le butin "
  "listé — tentes, tentures, chameaux — est celui d'un peuple de la tente."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est double : l'oracle d'Ésaïe 21 s'est "
  "accompli à l'époque assyrienne — les Kédarites sont les Qidri des inscriptions "
  "d'Assurbanipal, qui se vante du butin pris sur eux — puis celui de Jérémie 49 "
  "par Nebucadnetsar, nommé au verset 30. Les publications retiennent le témoignage "
  "de l'historien babylonien Bérose, cité par Josèphe, sur la conquête de l'Arabie "
  "du nord par Nebucadnetsar. Hatsor du désert, sans pierres à relever, est devenue "
  "ce que le texte disait : un lieu inhabité."
 ),
 accomplissement=[
  ("VIIIe-VIIe s. av. n. è.", "Ésaïe 21 annonce la fin de la gloire de Kédar dans l'année"),
  ("VIIe s. av. n. è.", "Campagnes assyriennes : Assurbanipal frappe les Qidri (Kédar) et prend butin"),
  ("VIe s. av. n. è.", "Nebucadnetsar frappe Kédar et les campements de Hatsor (Jr 49:28-33)"),
  ("Ve s. av. n. è.", "Un « roi de Kédar » est encore attesté en Égypte (coupe de Tell el-Maskhuta) : le nom survit, la gloire est passée"),
  ("Ve-IVe s. av. n. è.", "Les Nabatéens remplacent les Kédarites sur les routes caravanières"),
 ],
 hist=(
  "Le dossier profane est solide. Les annales d'Assurbanipal nomment les Qidri et "
  "les Aribi parmi les Arabes combattus, avec le décompte du butin : ânes, chameaux, "
  "moutons. Bérose, historien babylonien repris par Josèphe (Contre Apion, I), "
  "mentionne la conquête de l'Arabie du nord par Nebucadnetsar. Une coupe d'argent "
  "du Ve siècle trouvée à Tell el-Maskhuta, en Égypte, porte en araméen : « Qaynou "
  "fils de Geshem, roi de Kédar » — et ce Geshem est le « Geshem l'Arabe » qui "
  "s'oppose à Néhémie (Né 2:19 ; 6:1). La Bible et l'épigraphie se rejoignent sur "
  "un nom propre."
 ),
 geo=(
  "Le pays de Kédar, c'est le désert syro-arabe à l'est de la Palestine, au "
  "nord-ouest de la péninsule Arabique : hamadas pierreuses, pâturages d'hiver, "
  "oasis-étapes. Ésaïe 21:14 nomme Théma et Dédan, oasis caravanières où les fuyards "
  "mendieront l'eau et le pain : la géographie de la soif. Les routes de l'encens "
  "et des troupeaux relient ces tribus à Damas, à Tyr et à Gaza. Hatsor du désert, "
  "campement et non ville, ne laisse ni rempart ni tell : son « repaire de chacals » "
  "est le désert rendu à lui-même."
 ),
 sci=(
  "L'épigraphie nord-arabique et les inscriptions assyriennes fournissent le cadre : "
  "le nom Qidri/Qadri des textes d'Assurbanipal correspond au Qédar biblique, et la "
  "coupe de Tell el-Maskhuta donne un roi de Kédar daté du Ve siècle. L'ethnographie "
  "éclaire le texte : les « tentes de Kédar » du Cantique (Ct 1:5), tissées de poil "
  "de chèvre noir, sont encore celles des Bédouins. À Tayma, oasis du pays des "
  "fils de l'Orient, les inscriptions de Harran attestent le long séjour du roi "
  "babylonien Nabonide : l'Arabie du nord était bien dans l'orbite des empires "
  "mésopotamiens au VIe siècle."
 ),
 limites=(
  "Un peuple nomade laisse peu de ruines identifiables : cette fiche ne montre donc "
  "aucun « site de Kédar » fouillé, et elle distingue la Hatsor du désert (Jr 49) "
  "de Tel Hatsor en Galilée, ville cananéenne puis israélite. L'année exacte de la "
  "campagne de Nebucadnetsar en Arabie n'est pas fixée par les sources conservées ; "
  "la fiche la place au VIe siècle sans plus de précision. L'oracle vise la gloire "
  "militaire et pastorale des Kédarites, pas l'existence des Arabes : les Bédouins "
  "dressent toujours leurs tentes noires."
 ),
 tl=[("VIIIe-VIIe s.", "Ésaïe 21"), ("VIIe s.", "Assurbanipal"),
     ("VIe s.", "Nebucadnetsar"), ("Ve s.", "Roi de Kédar"), ("Auj.", "Tentes bédouines")],
 src=[("Kédar — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012523"),
      ("Hatsor — Étude perspicace (§ 5 : Hatsor du désert)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001937"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Jérémie 49 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/49")],
 img="images/prophe_A011_kedar.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="A012", titre="Élam — l'arc brisé",
 ref="Jérémie 49:34-39 ; Jérémie 25:25 ; Daniel 8:2 ; Genèse 14:1",
 statut="Accomplie",
 cat="A", syst="Dates neutres (597, 550)",
 reg="Registre : Jérémie — P223 (coupe des nations), P282",
 texte=[
  "« Voici ce que dit Jéhovah au sujet d'Élam, au commencement du règne de "
  "Sédécias : je brise l'arc d'Élam, le meilleur de sa force. » (Jr 49:34-35)",
  "« J'amènerai sur Élam les quatre vents ; je les disperserai de tous côtés. » (Jr 49:36)",
  "« Je placerai mon trône en Élam ; j'en ferai disparaître roi et princes. » (Jr 49:38)",
  "« Mais dans la suite des jours, je ramènerai les captifs d'Élam. » (Jr 49:39)",
 ],
 contexte=(
  "L'oracle est daté avec une précision rare : le commencement du règne de "
  "Sédécias, vers 597. Élam est alors une vieille puissance du sud-ouest iranien, "
  "capitale Suse : dès Abraham, un roi d'Élam, Kedorlaomer, menait des coalitions "
  "jusqu'à la mer Morte (Gn 14). Allié intermittent de Babylone contre l'Assyrie, "
  "Élam a survécu au sac de Suse par Assurbanipal mais n'est plus que l'ombre de "
  "lui-même. Sa spécialité militaire, célèbre dans tout l'Orient, c'est l'arc : "
  "les archers élamites."
 ),
 explication=(
  "« Briser l'arc », c'est briser l'armée elle-même : l'arme nationale vaut pour "
  "toute la force, comme « l'épée » vaut pour la guerre. « Placer mon trône en "
  "Élam » ne veut pas dire y régner durablement, mais y exercer le jugement sur "
  "place — le trône du juge, pas celui du résident. Les « quatre vents » annoncent "
  "la dispersion, et le verset 39, comme pour Moab (Jr 48:47) et Ammon (Jr 49:6), "
  "ajoute une promesse de retour : le jugement n'est pas le dernier mot. Élam "
  "figure aussi parmi les buveurs de la coupe de fureur (Jr 25:25)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah inscrit cet oracle dans la série des "
  "jugements exécutés à l'époque de la domination babylonienne (Jr 25:9 : "
  "Nebucadnetsar, « mon serviteur ») : comme toutes les nations d'alentour, Élam "
  "boit la coupe. Le pays cesse d'exister comme puissance indépendante et passe "
  "dans l'orbite mède puis perse ; Suse, son ancienne capitale, devient l'une des "
  "capitales achéménides — le lieu de la vision de Daniel 8:2, du palais d'Esther "
  "et du service de Néhémie. La promesse du verset 39 annonce un rétablissement "
  "dont cette fiche ne tranche pas la portée exacte (voir Limites)."
 ),
 accomplissement=[
  ("597 av. n. è. env.", "Oracle de Jérémie 49:34-39, au commencement de Sédécias"),
  ("VIe s. av. n. è.", "Élam boit la coupe des nations (Jr 25:25) ; fin de l'indépendance élamite"),
  ("550 av. n. è. env.", "Cyrus absorbe le pays élamite dans l'empire perse naissant"),
  ("539-522 av. n. è.", "Suse devient capitale achéménide : palais, administration, trésor"),
  ("33 de n. è.", "Des Élamites sont présents à Jérusalem à la Pentecôte (Ac 2:9)"),
 ],
 hist=(
  "Le contexte est documenté des deux côtés. Les annales d'Assurbanipal racontent "
  "le sac de Suse (vers 647-640), antérieur à l'oracle, qui avait déjà brisé la "
  "grandeur élamite. Le cylindre de Cyrus (découvert en 1879, British Museum) "
  "illustre la politique perse d'absorption des anciens royaumes. Les livres "
  "d'Esther, de Néhémie et de Daniel, écrits ou situés à Suse, confirment le "
  "transfert de la capitale élamite à l'empire perse : le trône placé en Élam est "
  "désormais celui des rois de Perse. Les tablettes de Persépolis, rédigées en "
  "élamite, montrent la langue d'Élam devenue langue d'administration perse."
 ),
 geo=(
  "Élam, c'est le Khuzistan actuel : la plaine alluviale de Suse, arrosée par la "
  "Karkheh et le Karun, adossée aux hauts plateaux de l'Anshan. Cette position — "
  "entre la Mésopotamie et le plateau iranien — a fait sa fortune et son malheur : "
  "grenier à blé convoité, couloir des invasions. Suse commande la route royale qui "
  "mènera, sous les Perses, jusqu'à Sardes. L'Oulaï, le cours d'eau de la vision de "
  "Daniel 8, coule à Suse ou à ses abords : la prophétie a une adresse fluviale."
 ),
 sci=(
  "Les fouilles françaises de Suse (de Morgan, dès 1897) ont livré un témoignage "
  "spectaculaire des rapports Élam-Mésopotamie : le Code de Hammurabi, emporté "
  "comme butin par un roi élamite et retrouvé à Suse en 1901. La frise des archers "
  "du palais de Darius (briques émaillées, musée du Louvre) montre l'arme qui fit "
  "la gloire d'Élam devenue garde du roi perse : l'arc a changé de maître, comme "
  "l'oracle le disait. La ziggurat de Tchogha Zanbil (XIIIe siècle, patrimoine "
  "mondial) atteste la civilisation élamite antérieure à sa chute."
 ),
 limites=(
  "Honnêteté oblige, comme pour l'Égypte (F004) : aucune campagne de Nebucadnetsar "
  "contre Élam nommément attestée n'est conservée dans les sources profanes ; la "
  "fiche retient la disparition d'Élam comme puissance indépendante au VIe siècle, "
  "qui, elle, est établie. Le sac de Suse par Assurbanipal est antérieur à l'oracle "
  "(vers 597) et ne peut donc pas en être l'accomplissement direct. Le sens exact "
  "du « retour » du verset 39 — rapatriés du VIe siècle, Élamites du Ier siècle, "
  "ou portée plus large — n'est pas tranché ici. Les dates 597 et 550 sont neutres."
 ),
 tl=[("597", "Oracle"), ("VIe s.", "Fin de l'indépendance"), ("550", "Absorption perse"),
     ("539+", "Suse capitale"), ("33", "Pentecôte : Élamites")],
 src=[("Oulaï — le cours d'eau de Suse en Élam", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200004502"),
      ("L'Empire médo-perse et les prophéties", "https://wol.jw.org/fr/wol/d/r30/lp-f/1977007"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Jérémie 49 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/49")],
 img="images/prophe_A012_elam.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="A013", titre="L'Assyrie — la verge brisée en une nuit",
 ref="2 Rois 19:1-37 ; Ésaïe 10:5-19 ; 14:24-27 ; 30:31 ; 37:36 ; 2 Chroniques 32",
 statut="Accomplie",
 cat="A", syst="Dates neutres (701, 681)",
 reg="Registre : Rois — P094 ; Ésaïe — P121, P129, P153",
 texte=[
  "« Assyrie, verge de ma colère ! Le bâton qu'elle tient, c'est mon indignation. » (Is 10:5)",
  "« Je briserai l'Assyrien dans mon pays ; je le foulerai sur mes montagnes. » (Is 14:25)",
  "« Cette nuit-là, l'ange de Jéhovah sortit et frappa dans le camp des Assyriens "
  "185 000 hommes. » (2R 19:35)",
  "« Sanchérib retourna à Ninive. Et il arriva, comme il adorait dans la maison de "
  "Nisrok son dieu, que ses fils Adrammélek et Sharétser le frappèrent de l'épée. » (2R 19:36-37)",
 ],
 contexte=(
  "La quatorzième année d'Ézéchias, en 701, Sanchérib mène sa troisième campagne : "
  "les villes fortes de Juda tombent l'une après l'autre, Lakis est assiégée, et le "
  "Rabshaqé porte l'ultimatum sous les murs de Jérusalem — en hébreu, devant le "
  "peuple, pour démoraliser. Ézéchias, qui vient d'être guéri et a reçu quinze ans "
  "de vie, étale la lettre devant Jéhovah dans le temple. Ésaïe répond : la ville "
  "ne sera ni prise, ni assiégée, ni même visée par une flèche (2R 19:32)."
 ),
 explication=(
  "Le paradoxe du chapitre 10 fait toute la théologie de l'oracle : l'Assyrie est "
  "à la fois l'instrument du jugement (« verge ») et son prochain objet (« je "
  "punirai le fruit du cœur orgueilleux du roi d'Assyrie », Is 10:12). Le lieu est "
  "précisé : « dans mon pays, sur mes montagnes » — le désastre frappera l'armée "
  "d'invasion en Juda même, pas l'empire au loin. La « rumeur » qui fera repartir "
  "Sanchérib (2R 19:7), c'est l'approche de Tirhaqa le Koushite. Et la garde de la "
  "ville est motivée : « à cause de moi et à cause de David mon serviteur » "
  "(2R 19:34) — l'alliance davidique est l'enjeu caché du siège."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que l'oracle s'est accompli à la "
  "lettre en une nuit : 185 000 Assyriens frappés par l'ange, Sanchérib levant le "
  "camp sans avoir tiré une flèche contre la ville, retour à Ninive, puis "
  "assassinat par ses deux fils. Les publications soulignent que les textes "
  "assyriens eux-mêmes font mention de la mort de Sanchérib sous les coups "
  "d'assassins, confirmant 2 Rois 19:37. La délivrance de 701 devient dès lors le "
  "type de toutes les délivrances : Jérusalem sauvée quand tout était perdu."
 ),
 accomplissement=[
  ("701 av. n. è.", "3e campagne de Sanchérib ; chute des villes fortes de Juda ; siège de Lakis"),
  ("701 av. n. è.", "L'ultimatum du Rabshaqé sous les murs ; prière d'Ézéchias ; réponse d'Ésaïe"),
  ("701 av. n. è.", "En une nuit, 185 000 Assyriens frappés ; Sanchérib lève le camp"),
  ("701-681 av. n. è.", "Retour et règne à Ninive ; aucune nouvelle tentative contre Jérusalem"),
  ("681 av. n. è.", "Assassinat de Sanchérib par Adrammélek et Sharétser ; Assarhaddon lui succède"),
 ],
 hist=(
  "Le prisme de Sanchérib (prisme de Taylor, British Museum) fournit le silence le "
  "plus éloquent de l'historiographie assyrienne : le roi se vante d'avoir enfermé "
  "Ézéchias « comme un oiseau dans une cage », énumère le tribut reçu — et ne "
  "prétend nulle part avoir pris Jérusalem, lui qui détaille chaque ville conquise. "
  "Les bas-reliefs du siège de Lakis, découverts à Ninive par Layard (British "
  "Museum), montrent l'acharnement mis à réduire la seconde ville du royaume. "
  "Hérodote (II, 141) garde un écho déformé du désastre : une invasion de rongeurs "
  "rendant l'armée assyrienne sans défense en une nuit."
 ),
 geo=(
  "La campagne suit la géographie de la peur : la plaine côtière, puis les vallées "
  "du piémont — Lakis (Tell ed-Duweir), à une cinquantaine de kilomètres au "
  "sud-ouest de Jérusalem, verrouille la route. Jérusalem, elle, est une "
  "ville-montagne alimentée par la source de Gihon, dont Ézéchias vient de protéger "
  "l'eau par son tunnel de 533 mètres (voir B006). Le camp assyrien s'étend "
  "« contre toutes les villes fortes » pendant que la capitale, sur ses hauteurs, "
  "attend : le relief fait partie de la prophétie."
 ),
 sci=(
  "Les fouilles de Lakis ont mis au jour un dispositif unique au monde : la rampe "
  "de siège assyrienne et la contre-rampe judéenne édifiée en hâte face à elle, "
  "deux ouvrages adverses fossilisés face à face. Les pointes de flèches, les "
  "pierres de fronde et les restes du massacre confirment la violence décrite par "
  "les bas-reliefs. La chronologie est ancrée : la campagne de 701 est datée par "
  "les éponymes assyriens et admise par toutes les chronologies — date neutre, "
  "sans débat."
 ),
 limites=(
  "Le chiffre de 185 000 n'a aucun parallèle profane : selon le récit lui-même, "
  "l'événement s'est produit en une nuit, sans témoin ennemi survivant pour le "
  "raconter — la fiche ne peut donc offrir que le silence du prisme, compatible "
  "avec le récit mais pas démonstratif à lui seul. Le récit d'Hérodote (les "
  "rongeurs) est une légende, citée ici comme écho lointain et non comme "
  "confirmation. Les ostraca de Lakis, souvent cités, datent du siège babylonien "
  "(vers 589) et non de 701 : ils n'entrent pas dans ce dossier."
 ),
 tl=[("701", "Campagne"), ("701", "Lakis assiégée"), ("701", "La nuit des 185 000"),
     ("701", "Retraite"), ("681", "Assassinat à Ninive")],
 src=[("Prophéties — 2 Rois 18-19, les 185 000", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("La ville qui se confiait en ses fortifications (Lakis)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1960763"),
      ("L'oppression cessera — la délivrance d'Ézéchias", "https://wol.jw.org/fr/wol/d/r30/lp-f/1981648"),
      ("Ninive — Étude perspicace", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013302")],
 img="images/prophe_A013_assyrie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C001", titre="Bethléhem Éphratha — le lieu de naissance",
 ref="Michée 5:2 ; Matthieu 2:1-6 ; Luc 2:1-7 ; Jean 7:42",
 statut="Accomplie",
 cat="C", syst="Système 29/33 (naissance : 2 av. n. è.)",
 reg="Registre : Michée — P457 ; partie messianique — P589 (et P458, P585)",
 texte=[
  "« Et toi, Bethléhem Éphratha, trop petite pour être parmi les clans de Juda, "
  "de toi sortira pour moi celui qui dominera en Israël, et ses origines remontent "
  "aux temps anciens, aux jours des temps indéfinis. » (Mi 5:2)",
  "« Et toi, Bethléhem, terre de Juda, tu n'es nullement la moindre parmi les "
  "gouverneurs de Juda ; car de toi sortira un chef qui fera paître mon peuple "
  "Israël. » (Mt 2:6, cité par les prêtres devant Hérode)",
  "« Joseph monta de Nazareth en Galilée à Bethléhem en Judée, la ville de David, "
  "pour se faire enregistrer avec Marie. » (Lc 2:4-5)",
 ],
 contexte=(
  "Michée prophétise au VIIIe siècle, contemporain d'Ésaïe sous Yotham, Achaz et "
  "Ézéchias. L'oracle suit immédiatement l'annonce du siège et de l'humiliation du "
  "« juge d'Israël » (Mi 5:1) : au creux du jugement, le lieu du relèvement est "
  "nommé. La précision « Éphratha » n'est pas ornementale : à l'époque de Jésus, "
  "deux villes portent le nom de Bethléhem — l'une près de Nazareth, au nord "
  "(Jos 19:15), l'autre près de Jérusalem, en Juda, l'ancienne Éphratha (Gn 35:19). "
  "C'est la seconde que l'oracle désigne, et c'est là que Jésus naît."
 ),
 explication=(
  "« Trop petite pour être parmi les clans » : l'insignifiance du lieu fait partie "
  "du signe — Dieu choisit un bourg, pas une capitale. « Ses origines remontent "
  "aux temps anciens » : le dominateur attendu préexiste à sa naissance terrestre. "
  "La citation de Matthieu 2:6 semble inverser le texte (« tu n'es nullement la "
  "moindre ») : paradoxe seulement apparent — après l'événement, le statut du lieu "
  "a changé, et Matthieu combine librement Michée 5:2 avec 2 Samuel 5:2 (« tu feras "
  "paître mon peuple »). Le verset de Jean 7:42 montre que l'attente était connue "
  "du peuple : « Le Christ ne vient-il pas de Bethléhem ? »"
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que la prophétie, donnée plus de "
  "700 ans d'avance, s'est accomplie au détail près : Jésus est né à Bethléhem "
  "de Juda, l'ancienne Éphratha, ville de David (Lc 2:4, 11). Les publications "
  "soulignent le mécanisme de l'accomplissement : un décret impérial de César "
  "Auguste ordonnant l'enregistrement amène Joseph et Marie, domiciliés à "
  "Nazareth, jusqu'au bourg de leurs ancêtres au moment précis de la naissance — "
  "Rome au service de Michée. Quant aux « origines anciennes », elles désignent "
  "l'existence céleste de Jésus avant sa venue sur terre."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Michée 5:2 nomme Bethléhem Éphratha plus de 700 ans d'avance"),
  ("2 av. n. è. env.", "Décret d'Auguste : Joseph et Marie montent de Nazareth à Bethléhem"),
  ("2 av. n. è., automne", "Naissance de Jésus à Bethléhem de Juda, la ville de David"),
  ("2-1 av. n. è.", "Les prêtres d'Hérode désignent eux-mêmes Bethléhem (Mt 2:4-6) : l'aveu adverse"),
  ("29 de n. è.", "Le baptême au Jourdain : le nouveau-né de Bethléhem devient le Messie"),
 ],
 hist=(
  "Le dossier romain encadre le récit. L'article Quirinius de l'Auxiliaire "
  "biblique suit la carrière du gouverneur de Syrie — consul en 12 avant notre "
  "ère (liste du Chronographus), campagnes en Cilicie relatées par Tacite — sous "
  "lequel Luc place l'enregistrement. Auguste se vante dans ses Res Gestae de "
  "trois cens, et les papyrus d'Égypte attestent des enregistrements périodiques "
  "sous son règne : la pratique est établie. Le sommet du dossier reste Matthieu "
  "2:4-6 : ce sont les grands prêtres et les scribes, convoqués par Hérode, qui "
  "citent Michée contre leur visiteur — un témoignage hostile, donc sans prix."
 ),
 geo=(
  "Bethléhem occupe une crête à environ 8 kilomètres au sud de Jérusalem, sur la "
  "route d'Hébron : position de passage, champs de céréales (Beth-Léhem, « maison "
  "du pain ») et pâturages où, selon Luc 2:8, des bergers gardaient leurs troupeaux "
  "la nuit de la naissance. Le tombeau de Rachel (Gn 35:19-20) borde la même route "
  "(voir C004). La distinction des deux Bethléhem est géographique : celle de "
  "Zabulon, au nord, n'a jamais porté le nom d'Éphratha ; seule celle de Juda "
  "satisfait à l'oracle complet."
 ),
 sci=(
  "L'archéologie atteste un bourg juif d'époque hérodienne sur le site : "
  "habitations, citernes, pressoirs, sépultures du Ier siècle. Elle ne peut en "
  "revanche, par nature, ni confirmer ni infirmer une naissance individuelle : "
  "cette fiche n'offre donc aucune « preuve matérielle » de la naissance, et "
  "l'église de la Nativité (IVe siècle) relève de la tradition constantinienne, "
  "pas du dossier. La papyrologie, elle, confirme le cadre administratif : les "
  "recensements romains périodiques d'Égypte montrent qu'un « enregistrement » "
  "sous Auguste n'a rien d'invraisemblable."
 ),
 limites=(
  "Cette fiche ne donne ni jour ni mois de naissance : le 25 décembre est une date "
  "traditionnelle postérieure, sans fondement biblique. Elle ne tranche pas le "
  "débat des historiens sur l'année de la mort d'Hérode le Grand (4 ou 1 avant "
  "notre ère selon les reconstitutions de l'éclipse lunaire), qui commande la "
  "fenêtre chronologique de la naissance. Le recensement de Quirinius de l'an 6 "
  "rapporté par Josèphe est un événement distinct et postérieur. La naissance "
  "elle-même, comme toute naissance, ne laisse pas de trace archéologique."
 ),
 tl=[("VIIIe s.", "Michée 5:2"), ("2 av. n. è.", "Édit d'Auguste"),
     ("2 av. n. è.", "Naissance"), ("2-1", "L'aveu des prêtres"), ("29", "Baptême")],
 src=[("Jésus Christ, le Messie promis — appendice", "https://wol.jw.org/fr/wol/pc/r30/lp-f/2012007/1/0"),
      ("Éphrathite — habitant de Bethléhem, ou Éphratha", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001407"),
      ("Quirinius — le gouverneur de l'enregistrement", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013528"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_C001_bethlehem.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C002", titre="La vierge — Emmanuel, Dieu avec nous",
 ref="Ésaïe 7:14 ; Matthieu 1:18-23 ; Luc 1:26-35 ; Ésaïe 8:3-4",
 statut="Accomplie",
 cat="C", syst="Système 29/33 (naissance : 2 av. n. è.)",
 reg="Registre : Ésaïe — P113 ; partie messianique — P588",
 texte=[
  "« Jéhovah lui-même vous donnera un signe : voici que la jeune fille deviendra "
  "enceinte, elle mettra au monde un fils et l'appellera Emmanuel. » (Is 7:14)",
  "« Voici que la vierge deviendra enceinte et mettra au monde un fils, et on "
  "l'appellera Emmanuel, ce qui signifie : avec nous est Dieu. » (Mt 1:23)",
  "« Comment cela se fera-t-il, puisque je n'ai pas de relations avec un "
  "homme ? » (Lc 1:34, question de Marie à l'ange)",
 ],
 contexte=(
  "Même crise qu'en A010 : la guerre syro-éphraïmite (vers 734). Achaz refuse de "
  "demander un signe ; le signe est alors donné à toute la « maison de David ». "
  "L'enfant-annonce a un premier rôle daté : « avant que le garçon sache rejeter "
  "le mal et choisir le bien, le pays des deux rois qui t'effraient sera abandonné » "
  "(Is 7:16) — Damas et Samarie tomberont avant quelques années. Mais le nom de "
  "l'enfant, Emmanuel, déborde ce premier horizon : « avec nous est Dieu »."
 ),
 explication=(
  "Tout le débat tient en un mot hébreu : alma, la jeune fille nubile — sept "
  "emplois dans la Bible (Rébecca en Gn 24:43, la sœur de Moïse en Ex 2:8, et "
  "autres), qui ne signifie pas à lui seul « vierge » au sens strict. Mais plus "
  "d'un siècle avant Jésus, les traducteurs juifs d'Alexandrie ont rendu ce mot, "
  "en Ésaïe 7:14, par le grec parthénos, « vierge » : c'est une traduction juive, "
  "pré-chrétienne, que Matthieu reprend. « Emmanuel » est un titre — comme les "
  "noms d'Ésaïe 9:6 — non un prénom d'état civil : aucune contradiction avec "
  "« tu l'appelleras Jésus » (Mt 1:21 ; Lc 1:31)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est celle du double accomplissement : "
  "le terme hébreu convenait à un premier accomplissement du temps d'Ésaïe — "
  "peut-être sur une jeune épouse d'Achaz ou d'Ésaïe — et au second, en la personne "
  "de Marie, fiancée mais vierge. Seul Jésus s'identifie complètement à Emmanuel, "
  "pour ce qui est de sa personne et de sa fonction : par lui, Dieu est "
  "véritablement « avec nous ». La conception est attribuée à l'esprit saint "
  "(Mt 1:20 ; Lc 1:35), non à Joseph — dont les généalogies marquent soigneusement "
  "le rôle : « Joseph, de qui Marie est l'épouse, de laquelle est né Jésus » "
  "(Mt 1:16)."
 ),
 accomplissement=[
  ("734 av. n. è. env.", "Le signe d'Ésaïe 7:14 donné à la maison de David"),
  ("732-722 av. n. è.", "Premier horizon vérifié : Damas puis Samarie abandonnées"),
  ("IIe s. av. n. è.", "La Septante juive traduit alma par parthénos (vierge)"),
  ("3-2 av. n. è.", "L'annonciation à Marie ; Joseph averti en rêve (Mt 1 ; Lc 1)"),
  ("2 av. n. è., automne", "Naissance de Jésus : le second Emmanuel est là"),
 ],
 hist=(
  "Deux témoins matériels verrouillent l'antériorité du texte. Le grand rouleau "
  "d'Ésaïe de Qumrân (1QIsa-a, IIe siècle avant notre ère) contient le chapitre 7 "
  "dans un texte hébreu antérieur au christianisme — voir B004. La Septante "
  "d'Alexandrie, traduction juive du même siècle, emploie parthénos : quand "
  "Matthieu cite « la vierge », il ne tord pas le texte, il suit la Bible de ses "
  "lecteurs. Les généalogies de Matthieu 1 et Luc 3, avec leurs formulations "
  "prudentes sur Joseph (« selon l'opinion », Lc 3:23), montrent un souci "
  "d'état civil incompatible avec une légende tardive."
 ),
 geo=(
  "Le signe naît à Jérusalem, devant Achaz, et s'accomplit à Nazareth de Galilée, "
  "où Marie reçoit l'ange, puis à Bethléhem, où l'enfant naît (voir C001). Le "
  "premier horizon, lui, est syro-palestinien : Damas au nord-est, Samarie au nord "
  "— les deux capitales dont l'abandon doit survenir « avant que l'enfant sache ». "
  "La géographie du signe est donc double, comme son accomplissement : deux "
  "capitales jugées au VIIIe siècle, une mangeoire au Ier."
 ),
 sci=(
  "La linguistique confirme la chaîne : corpus des sept emplois d'alma, version "
  "grecque des Septante, texte massorétique et rouleau de Qumrân concordent sur le "
  "verset. La critique textuelle n'a relevé aucune variante qui affaiblisse le "
  "« signe » : le texte est stable du IIe siècle avant notre ère à nos jours. "
  "Reste une limite de principe, que la fiche énonce : une conception virginale "
  "est un événement singulier rapporté, pas un phénomène reproductible — la "
  "science établit l'antériorité et la stabilité du texte, non le mécanisme du "
  "miracle."
 ),
 limites=(
  "Cette fiche ne prétend pas que le mot alma signifie toujours et partout "
  "« vierge » : c'est la traduction des Septante et la reprise de Matthieu qui "
  "fixent le sens du second accomplissement. L'identité de la jeune fille du "
  "premier accomplissement n'est pas précisée par Ésaïe ; les hypothèses (épouse "
  "d'Achaz ou d'Ésaïe) sont signalées comme telles, avec leur source. Aucune "
  "preuve biologique d'une conception virginale n'est possible par principe. Ni "
  "jour ni mois de la naissance ne sont donnés."
 ),
 tl=[("734", "Le signe"), ("732-722", "Premier horizon"), ("IIe s.", "Septante : parthénos"),
     ("3-2", "Annonciation"), ("2", "Naissance")],
 src=[("Emmanuel — Étude perspicace (double accomplissement)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012103"),
      ("Jésus Christ, le Messie promis — appendice", "https://wol.jw.org/fr/wol/pc/r30/lp-f/2012007/1/0"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Matthieu 1 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/1")],
 img="images/prophe_C002_emmanuel.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C003", titre="D'Égypte j'ai appelé mon fils",
 ref="Osée 11:1 ; Matthieu 2:13-15 ; Exode 4:22-23 ; Matthieu 2:19-23",
 statut="Accomplie",
 cat="C", syst="Système 29/33 (naissance : 2 av. n. è.)",
 reg="Registre : Osée — P420 ; partie messianique — P591",
 texte=[
  "« Quand Israël était jeune, je l'ai aimé, et d'Égypte j'ai appelé mon "
  "fils. » (Os 11:1)",
  "« Joseph se leva, prit de nuit le petit enfant et sa mère, et se retira en "
  "Égypte. Il y resta jusqu'à la mort d'Hérode, afin que s'accomplît ce que "
  "Jéhovah avait dit par le prophète : D'Égypte j'ai appelé mon fils. » (Mt 2:14-15)",
  "« Israël est mon fils, mon premier-né. » (Ex 4:22)",
 ],
 contexte=(
  "Osée prophétise au VIIIe siècle, dans les dernières décennies du royaume du "
  "Nord. Son regard, au chapitre 11, se tourne vers le passé : l'Exode, l'enfance "
  "du peuple, « fils » appelé hors d'Égypte. Huit siècles plus tard, Matthieu "
  "rapporte la fuite de Joseph : averti en rêve qu'Hérode veut tuer l'enfant, il "
  "gagne l'Égypte de nuit et n'en revient qu'après la mort du roi. L'enfant n'est "
  "plus un bébé : la famille s'est installée à Bethléhem, et Jésus est un petit "
  "enfant, peut-être âgé de plus d'un an."
 ),
 explication=(
  "Le « fils » d'Osée 11:1, au sens premier, c'est Israël collectif — Exode 4:22 "
  "l'a nommé « premier-né » dès Moïse. Matthieu, sous inspiration, révèle que ce "
  "fils collectif préfigurait le Fils individuel : le verbe « accomplir » (plêroô) "
  "signifie ici « porter à sa plénitude », non « prédire puis réaliser » au sens "
  "d'un oracle daté. C'est le procédé de la relecture inspirée : l'Exode, "
  "événement fondateur, devient le moule d'un second exode en miniature — sortie "
  "d'Égypte, séjour, retour au pays. Le chapitre 2 de Matthieu est bâti sur ces "
  "correspondances : Bethléhem (Mi 5:2), l'Égypte (Os 11:1), Rama (Jr 31:15), "
  "Nazareth (Mt 2:23)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Joseph, averti par l'ange, a "
  "protégé l'enfant promis en le conduisant en Égypte, réalisant ainsi une "
  "prophétie très ancienne. Les publications présentent Joseph comme le modèle du "
  "père : il ne discute pas, il part de nuit ; la vie de l'enfant compte plus que "
  "tout. Le séjour est bref — « pas très longtemps » — car l'ange annonce bientôt "
  "la mort d'Hérode. Au retour, la peur d'Archélaüs, fils d'Hérode, oriente la "
  "famille vers Nazareth en Galilée : chaque étape est guidée."
 ),
 accomplissement=[
  ("2 av. n. è.", "Naissance à Bethléhem ; installation de la famille dans la ville"),
  ("2-1 av. n. è.", "Visite des astrologues : l'enfant est dans une maison, ce n'est plus un nouveau-né (Mt 2:11)"),
  ("2-1 av. n. è.", "Joseph averti en rêve ; fuite de nuit vers l'Égypte"),
  ("1 av. n. è. env.", "Mort d'Hérode ; l'ange ordonne le retour : « d'Égypte j'ai appelé mon fils »"),
  ("1 av. n. è. env.", "Archélaüs craint en Judée ; installation à Nazareth (Mt 2:22-23)"),
 ],
 hist=(
  "La fuite suppose une Égypte accueillante aux Juifs : elle l'était. La colonie "
  "juive d'Éléphantine, avec son temple (Ve siècle), les papyrus araméens et, à "
  "l'époque de Jésus, l'immense communauté d'Alexandrie — celle de la Septante — "
  "offraient gîte, travail et synagogues. Le contexte hérodien est documenté par "
  "Josèphe : Hérode, qui fit exécuter sa femme Mariamne et trois de ses fils, "
  "était capable de tout massacre utile. Qu'aucune source profane ne rapporte "
  "celui de Bethléhem ne surprend pas : voir C004 et les Limites."
 ),
 geo=(
  "L'itinéraire probable suit la route côtière : Bethléhem, Hébron ou la plaine "
  "philistine, Gaza, puis la piste du nord-Sinaï jusqu'à Péluse et au delta — "
  "trois à cinq cents kilomètres selon la destination, quelques semaines de marche "
  "en famille. Le delta oriental, avec ses colonies juives, est la destination "
  "naturelle. Au retour, la famille évite la Judée d'Archélaüs : la Galilée "
  "d'Hérode Antipas, au nord, offre Nazareth, le village d'origine — bouclant "
  "ainsi la correspondance avec « il sera appelé Nazaréen » (Mt 2:23)."
 ),
 sci=(
  "Les papyrus araméens d'Éléphantine (Ve siècle avant notre ère) prouvent "
  "l'ancienneté de l'installation juive en Égypte : contrats, mariages, temple — "
  "une diaspora organisée quatre siècles avant Jésus. Les inscriptions et les "
  "papyri d'époque ptolémaïque puis romaine confirment la densité du peuplement "
  "juif du delta et d'Alexandrie au Ier siècle. En revanche, le séjour de Jésus "
  "lui-même — bref, d'une famille pauvre et discrète — ne pouvait laisser aucune "
  "trace matérielle identifiable : l'archéologie confirme le cadre, pas le séjour."
 ),
 limites=(
  "Cette fiche distingue trois niveaux : le cadre (diaspora juive en Égypte), "
  "attesté ; le récit (la fuite), rapporté par Matthieu seul ; les traditions "
  "coptes postérieures (Matareya, Vieux-Caire, Haute-Égypte), signalées comme "
  "traditions et non comme preuves — l'Évangile ne donne aucun lieu de séjour. "
  "La durée du séjour n'est pas précisée (« jusqu'à ce que je te prévienne »). "
  "Au sens premier, Osée 11:1 parle de l'Exode d'Israël : la fiche ne le cache "
  "pas, c'est Matthieu qui révèle le second sens. Voir C004 pour le massacre."
 ),
 tl=[("XIIIe s.", "L'Exode"), ("VIIIe s.", "Osée 11:1"), ("2-1", "Fuite en Égypte"),
     ("1 env.", "Retour : le fils appelé"), ("1 env.", "Nazareth")],
 src=[("Joseph — un bon père et un homme de foi (la fuite)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102013265"),
      ("Joseph — il protège sa famille", "https://wol.jw.org/fr/wol/d/r30/lp-f/2012250"),
      ("Matthieu proclame : le Messie est venu !", "https://wol.jw.org/fr/wol/d/r30/lp-f/1981807"),
      ("Jésus Christ, le Messie promis — appendice", "https://wol.jw.org/fr/wol/pc/r30/lp-f/2012007/1/0")],
 img="images/prophe_C003_egypte.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C004", titre="Rachel pleure ses fils — le deuil de Rama",
 ref="Jérémie 31:15-17 ; Matthieu 2:16-18 ; Genèse 35:16-20 ; Jérémie 40:1",
 statut="Accomplie",
 cat="C", syst="Système 607/537/29",
 reg="Registre : Jérémie — P239 ; partie messianique — P590",
 texte=[
  "« À Rama on entend une voix, des gémissements et des pleurs amers : c'est "
  "Rachel qui pleure sur ses fils. Elle a refusé d'être consolée, parce qu'ils "
  "ne sont plus. » (Jr 31:15)",
  "« Alors s'accomplit ce qui avait été dit par Jérémie le prophète : On a "
  "entendu à Rama une voix, des pleurs et de grands gémissements : c'est Rachel "
  "qui pleure ses enfants. » (Mt 2:17-18)",
  "« Retiens ta voix des pleurs : ton travail sera récompensé, et ils reviendront "
  "du pays de l'ennemi. » (Jr 31:16 — la consolation qui suit le deuil)",
 ],
 contexte=(
  "Jérémie 31 appartient au « livre de la consolation », écrit pour l'exil. "
  "Rachel est morte depuis près de mille ans quand Jérémie la fait pleurer : mère "
  "de Joseph et de Benjamin (Gn 30 ; 35), enterrée sur la route d'Éphratha, elle "
  "est l'ancêtre du nord (Joseph) et du sud (Benjamin) — toutes les mères "
  "d'Israël en une seule. Rama, à huit kilomètres au nord de Jérusalem, est le "
  "lieu où, après la chute de la ville, on rassemble les captifs enchaînés vers "
  "Babylone (Jr 40:1) : certains y sont tués, sur la terre de Benjamin où Rachel "
  "repose."
 ),
 explication=(
  "La figure est une prosopopée : la morte pleure les vivants. « Ils ne sont plus » "
  "dit la mort et la déportation sans retour apparent. Le paradoxe géographique — "
  "Rachel pleure à Rama, au nord, les enfants de Bethléhem, au sud — est voulu : "
  "le cri traverse tout le pays, du territoire de Benjamin à celui de Juda. "
  "Matthieu cite le deuil (Jr 31:15) sans citer la consolation qui le suit "
  "(Jr 31:16-17) : mais le contexte garde l'espoir — « ils reviendront du pays de "
  "l'ennemi », la mort elle-même (1Co 15:26). Le deuil d'Hérode est lu dans la "
  "lumière du deuil de l'exil : même pleureuse, même promesse."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est celle du double accomplissement. "
  "Premier deuil : au temps de Jérémie, les descendants de Benjamin tués ou "
  "enchaînés près de Rama, sur la terre de l'ancêtre. Second deuil, des siècles "
  "plus tard : Hérode fait tuer tous les garçons de deux ans et au-dessous à "
  "Bethléhem et dans tout son territoire, et ce sont les mères de Bethléhem que "
  "Rachel personnifie. Dans les deux cas, la même voix dit la peine des mères "
  "juives sur leurs enfants morts — et la même consolation répond : le retour, "
  "et finalement la résurrection."
 ),
 accomplissement=[
  ("XVIIIe s. av. n. è.", "Mort de Rachel sur la route d'Éphratha ; stèle sur son tombeau (Gn 35:19-20)"),
  ("VIIe-VIe s. av. n. è.", "Jérémie 31:15 : Rachel pleure dans le livre de la consolation"),
  ("607 av. n. è.", "Chute de Jérusalem ; captifs rassemblés à Rama (Jr 40:1) : premier deuil"),
  ("537 av. n. è.", "Retour de l'exil : première consolation, « ils reviennent du pays de l'ennemi »"),
  ("1 av. n. è. env.", "Massacre de Bethléhem : second deuil (Mt 2:16-18) ; la résurrection reste sans date"),
 ],
 hist=(
  "Le premier deuil est ancré dans le récit de Jérémie 40:1 : Rama, ville de "
  "Benjamin, sert de camp de rassemblement des captifs après 607. Le second "
  "s'inscrit dans le règne d'Hérode le Grand, dont Josèphe documente la cruauté "
  "familiale : exécution de Mariamne, de ses fils Alexandre, Aristobule puis "
  "Antipater — un roi qui tue ses propres enfants peut ordonner la mort de ceux "
  "de Bethléhem. Aucune source profane ne rapporte directement le massacre : "
  "Bethléhem est un bourg de quelques centaines d'habitants, et les victimes, "
  "selon les estimations démographiques courantes, se comptent par dizaines au "
  "plus — sous le seuil des chroniques impériales."
 ),
 geo=(
  "La fiche tient sur huit kilomètres de part et d'autre de Jérusalem : Rama "
  "(probablement er-Ram), au nord, en Benjamin ; Bethléhem, au sud, en Juda ; et "
  "entre les deux, sur la route, le tombeau de Rachel (Gn 35:19 : « c'est "
  "Bethléhem »). « Tout son territoire » (Mt 2:16) désigne les hameaux et fermes "
  "dépendant du bourg. Que le cri de Bethléhem soit « entendu à Rama » n'est pas "
  "une erreur de carte : c'est la géographie du deuil national, du nord au sud, "
  "comme aux jours de l'exil."
 ),
 sci=(
  "La démographie historique éclaire le silence des sources : un bourg judéen "
  "d'environ 300 à 1 000 habitants compte, en ordre de grandeur, une à deux "
  "dizaines de garçons de deux ans et au-dessous — un crime atroce et local, "
  "invisible à l'échelle de l'historiographie romaine. L'identification de Rama à "
  "er-Ram repose sur la toponymie et la distance à Jérusalem (8 km, conforme à "
  "Juges 19 et 1 Samuel), non sur une inscription : elle est probable, pas "
  "prouvée. Le « tombeau de Rachel » actuel est un sanctuaire de tradition, "
  "entretenu depuis des siècles, pas un site fouillé."
 ),
 limites=(
  "Comme en C003 et selon la méthode de F004, la fiche l'énonce : le massacre de "
  "Bethléhem n'a pas d'attestation profane directe, et elle n'en fabrique pas — "
  "elle offre le contexte (la cruauté documentée d'Hérode) et l'échelle (un bourg, "
  "des dizaines de victimes au plus). Matthieu cite le deuil sans la consolation : "
  "la fiche cite les deux (Jr 31:15-17), pour ne pas faire dire au texte moins "
  "qu'il ne dit. L'identification de Rama et le tombeau de Rachel relèvent de la "
  "tradition probable, pas de la preuve inscrite."
 ),
 tl=[("Gn 35", "Tombeau de Rachel"), ("Jr 31", "L'oracle"), ("607", "Rama : 1er deuil"),
     ("537", "Retour : consolation"), ("1 env.", "Bethléhem : 2nd deuil")],
 src=[("Questions des lecteurs : Rachel pleure sur ses fils ?", "https://wol.jw.org/fr/wol/d/r30/lp-f/402014927"),
      ("Matthieu proclame : le Messie est venu !", "https://wol.jw.org/fr/wol/d/r30/lp-f/1981807"),
      ("Jésus Christ, le Messie promis — appendice", "https://wol.jw.org/fr/wol/pc/r30/lp-f/2012007/1/0"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_C004_rachel.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="C005", titre="Le messager devant lui — Jean le Baptiseur",
 ref="Malaki 3:1 ; 4:5-6 ; Ésaïe 40:3 ; Matthieu 11:7-14 ; 17:10-13 ; Luc 1:16-17",
 statut="Accomplie",
 cat="C", syst="Système 29/33",
 reg="Registre : Malaki — P516 (3:1-6), P519 (4:1-6)",
 texte=[
  "« Voici que j'envoie mon messager, et il préparera le chemin devant moi. Et "
  "soudain viendra à son temple le Seigneur que vous cherchez, et le messager de "
  "l'alliance en qui vous prenez plaisir. » (Ml 3:1)",
  "« Je vous envoie Élie le prophète avant que vienne le jour de Jéhovah, grand "
  "et redoutable. » (Ml 4:5)",
  "« C'est lui l'Élie qui devait venir. » (Mt 11:14, Jésus au sujet de Jean)",
  "« Il marchera devant lui avec l'esprit et la puissance d'Élie. » (Lc 1:17, l'ange au sujet de Jean)",
 ],
 contexte=(
  "Malaki prophétise au Ve siècle, après le retour d'exil : le temple est rebâti, "
  "mais les prêtres méprisent l'alliance de Lévi et le peuple divorce et fraude "
  "(Ml 2). L'oracle répond au découragement : Dieu va envoyer son messager, puis "
  "venir lui-même à son temple avec le messager de l'alliance — pour purifier les "
  "fils de Lévi et juger (Ml 3:2-5). Entre Malaki et Jean, aucun livre prophétique "
  "inspiré : l'attente mûrit pendant des siècles, nourrie par Ésaïe 40:3 — « une "
  "voix dans le désert » — et par Daniel 9."
 ),
 explication=(
  "Le verset distingue deux envoyés : le messager-précurseur, qui prépare le "
  "chemin, puis le Seigneur accompagné du messager de l'alliance, qui vient au "
  "temple. L'« Élie » de Malaki 4:5 n'est pas le prophète ressuscité : Jean "
  "lui-même, interrogé, nie être Élie (Jn 1:21) — et Jésus affirme qu'il est "
  "« l'Élie qui devait venir » (Mt 11:14). La contradiction se résout en Luc 1:17 : "
  "Jean marche « avec l'esprit et la puissance d'Élie » — même fonction, même "
  "vêtement de poil, même désert, même appel à la repentance — sans être la même "
  "personne. Aucune réincarnation : une succession de rôles."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que le messager et l'Élie de "
  "Malaki, c'est Jean le Baptiseur, le précurseur de Jésus — les Évangiles "
  "l'affirment expressément (Mt 11:10-14 ; 17:10-13 ; Mc 9:11-13 ; Lc 1:16-17, 76). "
  "Jésus, lui, est le messager de l'alliance : accompagnant Jéhovah, il vient au "
  "temple pour l'inspecter et le purifier — les deux purifications du temple "
  "(Jn 2 ; Mt 21) en sont les actes visibles. Jean est le portier qui ouvre au "
  "berger (Jn 10:3) : « il faut qu'il grandisse, et que moi je diminue » "
  "(Jn 3:30)."
 ),
 accomplissement=[
  ("Ve s. av. n. è.", "Malaki 3:1 et 4:5 : le messager, puis Élie, sont annoncés"),
  ("29 de n. è.", "15e année de Tibère : la parole de Dieu vient à Jean au désert (Lc 3:1-2)"),
  ("29 de n. è., automne", "Jean baptise Jésus au Jourdain ; Dieu reconnaît son Fils (Mt 3 ; Mc 1 ; Lc 3)"),
  ("30-33 de n. è.", "« Il grandit, je diminue » : arrestation puis exécution de Jean à Machéronte"),
  ("33 de n. è.", "Le messager de l'alliance purifie le temple à Pâque (Mt 21:12-13)"),
 ],
 hist=(
  "Jean est l'une des figures évangéliques les mieux attestées hors de la Bible : "
  "Josèphe (Antiquités, XVIII) rapporte sa prédication, son baptême, sa popularité "
  "et son exécution à Machéronte sur l'ordre d'Hérode Antipas. Le cadre de Luc "
  "3:1-2 est un faisceau de synchronismes vérifiables : Tibère (15e année : 29), "
  "Ponce Pilate — dont l'inscription de Césarée (1961) confirme le titre de "
  "préfet de Judée — Hérode Antipas, Philippe, Lysanias, Anne et Caïphe, dont un "
  "ossuaire inscrit au nom de Qayafa a été découvert à Jérusalem en 1990. Chaque "
  "nom propre de Luc a trouvé sa pierre ou sa monnaie."
 ),
 geo=(
  "Le ministère du précurseur est un ministère du désert et du fleuve : désert de "
  "Judée, Jourdain — Béthanie au-delà du Jourdain (Jn 1:28), Énon près de Salim "
  "« parce qu'il y avait là beaucoup d'eau » (Jn 3:23). Machéronte, forteresse "
  "d'Hérode à l'est de la mer Morte, sur son piton dominant les eaux, est le lieu "
  "de l'emprisonnement et de l'exécution selon Josèphe. Le Jourdain du baptême, "
  "enfin, est le fleuve de la traversée : Israël y était entré dans le pays ; le "
  "Messie y entre dans son ministère."
 ),
 sci=(
  "L'épigraphie a suivi Luc pas à pas. La pierre de Pilate (Césarée, 1961) porte "
  "en latin le nom de Ponce Pilate et son titre de préfet de Judée, confirmant la "
  "fonction exacte donnée par Luc et Tacite. L'ossuaire de Caïphe (1990) atteste le "
  "grand prêtre de la Passion. Les monnaies de Tibère permettent de dater sa 15e "
  "année (29 de notre ère), point de départ du ministère de Jean dans le système "
  "chronologique de cette fiche. Les fouilles de Machéronte ont dégagé le palais-"
  "forteresse hérodien décrit par Josèphe."
 ),
 limites=(
  "L'année de l'exécution de Jean n'est pas fixée dans cette fiche : les récits "
  "la placent avant 33, sans plus. À Machéronte, la forteresse est identifiée et "
  "fouillée, mais le lieu précis de l'exécution dans le palais ne l'est pas. La "
  "fiche ne fait pas de Jean une réincarnation d'Élie : Jean 1:21 l'interdit, et "
  "Luc 1:17 donne le sens — l'esprit et la puissance, c'est-à-dire le rôle. "
  "L'application moderne de Malaki 3:1 (l'inspection de 1918-1919 selon les "
  "publications) sort du cadre de cette fiche, consacrée au Ier siècle."
 ),
 tl=[("Ve s.", "Malaki 3-4"), ("29", "Jean au désert"), ("29", "Baptême de Jésus"),
     ("30-33", "Machéronte"), ("33", "Le temple purifié")],
 src=[("Malaki (livre de) — le messager et Élie", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012800"),
      ("Jean le Baptiste, le portier du berger", "https://wol.jw.org/fr/wol/d/r30/lp-f/1980527"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Malaki 3 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/39/3")],
 img="images/prophe_C005_messager.jpg",
))
