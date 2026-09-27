#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE B — PROPHETIES SUR JERUSALEM ET JUDA
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Chronologie unique : 607 / 539 / 537 / 455 / 29 / 33 / 36 / 70 / 1914.
Dates neutres signalees comme telles. Aucune date pour l'avenir.
"""

CAT = dict(
    code="B",
    nom="Prophéties sur Jérusalem et Juda",
    sous="Silo, les 70 ans, le retour, le second temple, 70 de notre ère",
    intro=(
        "Jérusalem est le fil conducteur du dossier, et c'est aussi son point le plus dense : "
        "la ville est annoncée dévastée, puis rebâtie, puis de nouveau détruite, et enfin "
        "« foulée aux pieds » jusqu'à une échéance que la Bible chiffre ailleurs. Cette "
        "catégorie suit cet arc du début à la fin. Elle contient aussi la seule prophétie du "
        "recueil que l'organisation déclare expressément **non accomplie sur son objet "
        "littéral** — Aggée 2:9, la gloire du second temple. Une fiche lui est consacrée, "
        "et elle est traitée comme les autres : avec ses preuves et ses limites."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B001", titre="Silo — le précédent invoqué contre le temple",
 ref="Jérémie 7:1-15 ; 26:1-9 ; Psaume 78:60-64 ; Josué 18:1",
 statut="Accomplie",
 cat="B", syst="Date neutre (XIᵉ siècle av. n. è.)",
 reg="Registre : partie 4 (Jérémie 1-25)",
 texte=[
  "« Allez donc à mon lieu qui était à Silo, où j'ai fait résider mon nom au commencement, "
  "et voyez ce que j'en ai fait, à cause de la méchanceté de mon peuple Israël. » (Jér 7:12)",
  "« Je traiterai cette maison sur laquelle mon nom est invoqué… de la même manière que "
  "j'ai traité Silo. » (Jér 7:14)",
  "« Je ferai de cette ville un objet de malédiction pour toutes les nations de la terre. » "
  "(Jér 26:6)",
 ],
 contexte=(
  "Jérémie prononce son « sermon du temple » à la porte de la maison de Jéhovah, au début "
  "du règne de Joaqim. La population de Jérusalem tient pour acquis que le temple garantit "
  "la sécurité de la ville : la formule « le temple de Jéhovah, le temple de Jéhovah » est "
  "devenue une incantation (Jér 7:4). Jérémie retourne l'argument en citant un précédent "
  "vieux de plus de trois siècles : Silo, premier sanctuaire d'Israël en terre promise, "
  "où le tabernacle avait été dressé et où Samuel avait grandi."
 ),
 explication=(
  "L'argument est de forme juridique : Dieu invoque son propre précédent. Silo portait le "
  "nom de Dieu (« où j'ai fait résider mon nom ») exactement comme Jérusalem — et Silo a "
  "été détruite. La conclusion implicite est que le nom porté par un lieu ne le protège "
  "pas. Le Psaume 78:60-64 garde la mémoire de l'événement en termes presque identiques : "
  "« Il abandonna la demeure de Silo » ; l'arche fut prise, les prêtres tombèrent. "
  "Jérémie 26:6 ajoute une seconde image : la ville deviendra « un objet de malédiction » "
  "— c'est-à-dire que son nom servira de formule de malédiction chez les nations."
 ),
 interpretation=(
  "La compréhension retenue est celle d'un avertissement conditionnel devenu arrêt : le "
  "précédent de Silo sert à démontrer que la présence du temple ne suspend pas le "
  "jugement. L'organisation relève que l'avertissement fut répété pendant des décennies "
  "avant de s'exécuter, et que Jérémie faillit être mis à mort précisément pour l'avoir "
  "prononcé (Jérémie 26:7-11)."
 ),
 accomplissement=[
  ("XIIᵉ-XIᵉ s. av. n. è.", "Silo abrite le tabernacle et l'arche ; c'est le centre cultuel d'Israël (Josué 18:1 ; 1 Samuel 1-4)"),
  ("XIᵉ s. av. n. è.", "Défaite d'Israël à Ében-Ézer ; l'arche est prise, les fils d'Héli meurent, le sanctuaire est détruit (1 Samuel 4)"),
  (" vers 648 av. n. è.", "Le sermon du temple : Jérémie cite Silo comme précédent (Jérémie 7)"),
  ("607 av. n. è.", "Jérusalem est dévastée et le temple brûlé — « de la même manière que j'ai traité Silo »"),
  (" aujourd'hui", "Le tell de Silo (Khirbet Seilun) conserve une couche de destruction et le site est resté inhabité pendant des siècles à l'époque de Jérémie"),
 ],
 hist=(
  "Aucun document profane ne mentionne Silo : la connaissance du sanctuaire repose "
  "uniquement sur la Bible et sur la fouille. L'histoire profane ne peut donc ni confirmer "
  "ni infirmer ; elle est muette, ce qui est une position différente de la contradiction."
 ),
 geo=(
  "Silo (Khirbet Seilun) se trouve en Samarie, à une trentaine de kilomètres au nord de "
  "Jérusalem, sur un éperon rocheux dominant une vallée fertile — un site choisi pour être "
  "discret, non pour être défendu. C'est cette absence de fortification qui rend la "
  "comparaison avec Jérusalem encore plus tranchante : Jérusalem, elle, avait des "
  "murailles, et cela ne l'a pas sauvée."
 ),
 sci=(
  "Les fouilles conduites sur le tell, en particulier les campagnes récentes, ont mis au "
  "jour une couche de destruction généralisée avec effondrement des murs et cendres, "
  "datée par le carbone 14 de la seconde moitié du XIᵉ siècle avant notre ère — cohérente "
  "avec le récit de 1 Samuel 4. Le site montre ensuite une réoccupation clairsemée à l'âge "
  "du fer II, puis une destruction violente au IIᵉ siècle avant notre ère. Au temps de "
  "Jérémie, plus de trois siècles après l'événement, Silo était donc effectivement en "
  "ruines : le précédent invoqué par le prophète était vérifiable par ses auditeurs."
 ),
 limites=(
  "Le lien entre la destruction de Silo et la bataille d'Ében-Ézer repose sur le seul "
  "récit biblique ; l'archéologie date la destruction mais n'en nomme pas l'auteur. Cette "
  "fiche ne prétend donc pas démontrer l'identité des destructeurs. Elle retient le fait "
  "archéologique — un sanctuaire détruit et resté en ruines pendant des siècles — qui est "
  "tout ce dont l'argument de Jérémie a besoin."
 ),
 tl=[("XIIᵉ s.", "Tabernacle à Silo"), ("XIᵉ s.", "Destruction"), ("648", "Sermon de Jérémie"),
     ("607", "Jérusalem dévastée"), ("Auj.", "Tell en ruines")],
 src=[("Jérémie 7 (texte et notes)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/24/7"),
      ("Silo — le sanctuaire et sa destruction", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200014121"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_B001_silo.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B002", titre="Les soixante-dix ans — Jérusalem dévastée, puis visitée",
 ref="Jérémie 25:11, 12 ; 29:10-14 ; 2 Chroniques 36:20, 21 ; Daniel 9:2 ; Zacharie 1:12",
 statut="Accomplie",
 cat="B", syst="Système biblique (607 / 537)",
 reg="Registre : partie 4 (Jérémie) — P221 ; P222 ; P385",
 texte=[
  "« Tout ce pays deviendra une ruine, un désert, et ces nations seront asservies au roi "
  "de Babylone pendant soixante-dix ans. » (Jér 25:11)",
  "« Quand soixante-dix ans seront révolus à Babylone, je vous visiterai et j'accomplirai "
  "ma bonne parole à votre égard, en vous ramenant vers ce lieu-ci. » (Jér 29:10)",
  "« Il [le pays] se reposa tout le temps qu'il fut dévasté, jusqu'à l'accomplissement de "
  "soixante et dix ans. » (2 Chron 36:21)",
  "« Moi, Daniel, je portai mon attention… sur le nombre des années… soixante-dix ans. » "
  "(Dan 9:2)",
 ],
 contexte=(
  "Jérémie annonce les soixante-dix ans une première fois la quatrième année de Joaqim "
  "(Jérémie 25), soit vingt-trois ans avant la destruction, et une seconde fois dans une "
  "lettre envoyée aux exilés déjà déportés (Jérémie 29). L'intervalle est important : la "
  "prophétie n'est pas prononcée après coup. Daniel, à Babylone, lit Jérémie et comprend, "
  "vers la fin de la période, que l'échéance approche."
 ),
 explication=(
  "Trois points d'exégèse. (1) Le nombre est **soixante-dix**, et Daniel le commente "
  "expressément comme « le nombre des années » — un chiffre, non un symbole. (2) Le verbe "
  "employé en 2 Chroniques 36:21 est « le pays se reposa » : la terre bénéficie du repos "
  "sabbatique qu'Israël ne lui avait jamais accordé, ce qui donne au chiffre une dimension "
  "juridique. (3) La période porte sur la **désolation du pays**, et non sur la durée de "
  "la captivité de chaque individu : un exilé déporté en 617 n'a pas passé soixante-dix "
  "ans à Babylone."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que les soixante-dix ans se sont écoulés "
  "de l'automne 607 à l'automne 537, l'arrivée effective des exilés à Jérusalem marquant "
  "la fin de la désolation — non la signature du décret de Cyrus. La Bibliothèque en ligne "
  "souligne que Jérémie et Daniel affirment tous deux une durée de soixante-dix ans, et "
  "non de cinquante, ce qui porte la destruction de Jérusalem à 607 et non à 587."
 ),
 accomplissement=[
  ("625 av. n. è. env.", "Jérémie annonce les soixante-dix ans, vingt-trois ans avant la destruction (Jérémie 25)"),
  ("607 av. n. è.", "Jérusalem tombe le 9 Tammouz ; le 10 Ab, Nébuzaradan détruit la ville et le temple"),
  (" après 607", "Le pays reste désolé : aucun peuple n'est installé à la place des Juifs, contrairement à la pratique assyrienne"),
  ("539 av. n. è.", "Babylone tombe ; le décret de Cyrus est publié (date neutre)"),
  (" automne 537", "Les exilés arrivent à Jérusalem avant le 7ᵉ mois ; l'autel est relevé ; les soixante-dix ans s'achèvent"),
 ],
 hist=(
  "Josèphe écrit que « la Judée, Jérusalem et le Temple demeurèrent déserts durant "
  "soixante-dix ans » (Histoire ancienne des Juifs, livre X, chap. XI, § 9) : le "
  "témoignage d'un historien juif du Iᵉʳ siècle, indépendant du calcul chrétien. "
  "L'histoire profane admet quant à elle le retour des exilés en 537."
 ),
 geo=(
  "La désolation porte sur un territoire précis : le royaume de Juda, soit une bande de "
  "terre d'environ 90 km du nord au sud, de Béthel à Beer-Schéba. Les fouilles régionales "
  "montrent pour cette période une interruption quasi complète de l'habitat sédentaire "
  "dans les collines de Judée, avec une survie de population dans la région de Benjamin, "
  "au nord — exactement le secteur que Nébuzaradan laissa en place pour cultiver les "
  "vignes (2 Rois 25:12)."
 ),
 sci=(
  "L'archéologie régionale est ici l'argument décisif : les prospections au sol menées "
  "dans les collines de Judée recensent des dizaines de sites détruits à la fin de l'âge "
  "du fer, puis désertés pendant plusieurs générations avant une réoccupation à l'époque "
  "perse. La céramique permet de dater ces deux phases. Le « vide » constaté correspond à "
  "l'intervalle annoncé."
 ),
 limites=(
  "La chronologie profane place la destruction de Jérusalem en 587, soit cinquante ans "
  "avant le retour, et non soixante-dix. Cette fiche suit le système biblique (607) et "
  "signale l'écart, qui est l'objet de l'article de référence cité en source. Les deux "
  "dates ne doivent jamais être présentées comme équivalentes dans un même document."
 ),
 tl=[("625", "Jérémie annonce 70 ans"), ("607", "Jérusalem dévastée"), ("539", "Chute de Babylone"),
     ("537", "Retour"), ("fin", "Pays de nouveau occupé")],
 src=[("Quand l'ancienne Jérusalem a-t-elle été détruite ? (1)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
      ("Quand Jérusalem a-t-elle été dévastée par Babylone ?", "https://wol.jw.org/fr/wol/d/r30/lp-f/101972329"),
      ("Une date pivot de l'Histoire — 537", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_B002_70ans.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B003", titre="La fuite en Égypte — l'avertissement et son échec",
 ref="Jérémie 42:1-22 ; 43:1-13 ; 44:1-30",
 statut="Accomplie",
 cat="B", syst="Système biblique (607)",
 reg="Registre : partie 4 (Jérémie 26-38 et 39-52)",
 texte=[
  "« Si vous tournez vraiment vos faces vers l'Égypte… l'épée dont vous avez peur vous "
  "atteindra là, au pays d'Égypte. » (Jér 42:15, 16)",
  "« Neboukadnetsar… dressera son trône… et il frappera le pays d'Égypte. » (Jér 43:10, 11)",
  "« Ainsi vous saurez que ma parole s'accomplira contre vous, pour votre malheur. » "
  "(Jér 44:29)",
 ],
 contexte=(
  "Après l'assassinat de Guedalia, gouverneur laissé en place par les Babyloniens, les "
  "rescapés de Juda veulent fuir en Égypte. Ils viennent trouver Jérémie et lui demandent "
  "de prier pour connaître la volonté de Dieu — en annonçant d'avance qu'ils feront "
  "l'inverse. La réponse vient dix jours plus tard : ne descendez pas en Égypte. Ils y "
  "descendent, et emmènent Jérémie de force."
 ),
 explication=(
  "Le texte est l'un des plus nets du livre sur la mécanique de la prophétie : la requête "
  "est formulée, la réponse est donnée, la réponse est rejetée, et l'événement annoncé se "
  "produit. Jérémie 43:10 est d'une précision remarquable : Neboukadnetsar « dressera son "
  "trône » et « étendra sa tente royale » sur les dalles de briques de Tahpanhès. Ce "
  "n'est pas une invasion décrite en termes vagues, mais un acte royal accompli en un "
  "lieu nommé."
 ),
 interpretation=(
  "La compréhension retenue est que la prophétie s'est accomplie lorsque Neboukadnetsar "
  "monta contre l'Égypte, quelques années après 607, et que les fugitifs juifs qui "
  "comptaient y trouver refuge y trouvèrent l'épée. La Bibliothèque en ligne rappelle "
  "que les rescapés « ne purent échapper aux Babyloniens », et rattache cet événement au "
  "début des quarante années de désolation de l'Égypte annoncées en Ézéchiel 29."
 ),
 accomplissement=[
  ("607 av. n. è.", "Assassinat de Guedalia ; les rescapés veulent fuir en Égypte"),
  ("607 av. n. è.", "Jérémie transmet la réponse après dix jours d'attente : ne descendez pas"),
  (" après 607", "Les rescapés descendent en Égypte et emmènent Jérémie de force (Jérémie 43:6, 7)"),
  (" après 607", "Neboukadnetsar monte contre l'Égypte et la conquiert ; les fugitifs sont atteints"),
  (" après 607", "Début probable de la période de désolation annoncée en Ézéchiel 29:11,12"),
 ],
 hist=(
  "Des inscriptions égyptiennes du VIᵉ siècle et des fragments d'archives babyloniennes "
  "attestent des campagnes de Neboukadnetsar vers l'Égypte. Le détail — le lieu précis, "
  "Tahpanhès, et le geste du trône dressé — n'est en revanche confirmé par aucun document "
  "profane retrouvé à ce jour."
 ),
 geo=(
  "Tahpanhès est identifiée à Tell Defenneh, dans l'est du delta du Nil, sur la branche "
  "pélusiaque : c'est la porte d'entrée de l'Égypte pour qui vient de Juda. Le site a "
  "livré une plateforme de briques crues à l'extérieur de la forteresse — une esplanade "
  "sur laquelle une tente royale ou un trône pouvait effectivement être dressé."
 ),
 sci=(
  "Les fouilles de Tell Defenneh, menées à la fin du XIXᵉ siècle par Flinders Petrie, ont "
  "mis au jour une grande plateforme de briques crues devant la forteresse, que Petrie "
  "identifia à « la voûte de briques » mentionnée dans la Bible. L'identification reste "
  "discutée, mais l'existence de la structure, à l'endroit dit, est établie."
 ),
 limites=(
  "L'accomplissement de la campagne égyptienne de Neboukadnetsar n'est documenté que "
  "partiellement par l'histoire profane : les sources égyptiennes de cette période sont "
  "lacunaires. Cette fiche retient le témoignage biblique complété par les données "
  "archéologiques du delta, sans prétendre à une confirmation documentaire complète."
 ),
 tl=[("607", "Mort de Guedalia"), ("607", "Avertissement rejeté"), ("après 607", "Fuite en Égypte"),
     ("après 607", "Neboukadnetsar"), ("après 607", "Épée annoncée")],
 src=[("Points marquants du livre d'Ézékiel — II", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007562"),
      ("Jérémie 42 (texte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/24/42"),
      ("Quand l'ancienne Jérusalem a-t-elle été détruite ? (1)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2011736"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_B003_fuite_egypte.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B004", titre="Cyrus nommé d'avance — le berger et l'oint",
 ref="Isaïe 44:24-45:7 ; Jérémie 50:1-3 ; 51:11 ; Esdras 1:1-4",
 statut="Accomplie",
 cat="B", syst="Système biblique (537) + date neutre (539)",
 reg="Registre : partie 3 (Isaïe) — P155 à P162",
 texte=[
  "« Moi, je dis de Cyrus : ‹Il est mon berger, et tout ce qui me plaît, il l'exécutera› ; "
  "oui, je dirai de Jérusalem : ‹Qu'elle soit rebâtie›, et du temple : ‹Que tes fondations "
  "soient posées›. » (Is 44:28)",
  "« Voici ce que j'ai dit à mon oint, à Cyrus, dont j'ai saisi la droite. » (Is 45:1)",
  "« Je marcherai devant toi… je briserai les portes d'airain et je couperai les barres de "
  "fer. » (Is 45:2)",
 ],
 contexte=(
  "Isaïe écrit au VIIIᵉ siècle avant notre ère. Cyrus naît au VIᵉ siècle : l'écart est de "
  "plus de cent cinquante ans, et l'objection classique des critiques est précisément là. "
  "Le texte est d'autant plus frappant qu'il emploie deux titres qui, dans la Bible, ne "
  "s'appliquent qu'à des serviteurs de Dieu : « berger » et « oint » — le même mot que "
  "celui dont on se sert pour les rois d'Israël et, plus tard, pour le Messie."
 ),
 explication=(
  "Trois détails du texte méritent l'attention. (1) Le nom : Cyrus est nommé "
  "« l'oint », littéralement, alors qu'il ne connaît pas le Dieu d'Israël — ce qui "
  "signale une fonction d'instrument, non une conversion. (2) Le titre de « berger », "
  "employé pour un conquérant : le même prophète qui dénonce les bergers infidèles "
  "d'Israël applique le mot à un roi païen. (3) Les « portes d'airain et les barres de "
  "fer » : le texte annonce une ville prise sans que ses défenses soient forcées."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que la prophétie s'est accomplie en 539, "
  "lors de la chute de Babylone, et en 537, lors du décret qui rendit le retour possible. "
  "L'organisation souligne que l'objection d'une rédaction tardive d'Isaïe — le "
  "« deutéro-Isaïe » des critiques — se tranche sur les manuscrits de la mer Morte, où le "
  "livre d'Isaïe figure en un seul rouleau, complet, antérieur de plus d'un millénaire "
  "aux plus anciens manuscrits hébraïques connus avant 1947."
 ),
 accomplissement=[
  ("VIIIᵉ s. av. n. è.", "Isaïe nomme Cyrus, le berger et l'oint (Is 44:28 ; 45:1)"),
  ("539 av. n. è.", "Cyrus prend Babylone dans la nuit, par le lit détourné de l'Euphrate (date neutre)"),
  (" début 537", "Le décret de Cyrus est publié ; il autorise le retour et la reconstruction du temple"),
  (" automne 537", "Les exilés arrivent à Jérusalem ; l'autel est relevé"),
  ("536 av. n. è.", "Les fondations du second temple sont posées"),
 ],
 hist=(
  "Le cylindre de Cyrus, document cunéiforme découvert à Babylone en 1879 et conservé au "
  "British Museum, rapporte la prise de la ville et la politique religieuse du conquérant "
  "envers les dieux des peuples déportés — une politique qui cadre avec le décret "
  "d'Esdras 1. La Chronique de Nabonide fixe la chute de la ville."
 ),
 geo=(
  "Babylone était protégée par une double enceinte et par l'Euphrate, qui traversait la "
  "ville. Le point faible était le fleuve : là où ses eaux étaient basses, des troupes "
  "pouvaient passer à gué. La stratégie de Cyrus consista à détourner le cours pendant "
  "une nuit de fête, ce qui correspond exactement à l'annonce d'Isaïe sur les eaux "
  "desséchées."
 ),
 sci=(
  "L'argument décisif est manuscripturaire, non archéologique : le grand rouleau d'Isaïe "
  "découvert à Qumrân (1QIsaᵃ), daté du IIᵉ siècle avant notre ère, contient l'ensemble "
  "du livre, chapitres 40 à 66 compris, sans rupture. Comparé au texte massorétique "
  "médiéval, il en diffère très peu. L'hypothèse d'un second auteur écrivant après "
  "l'événement se heurte donc à un témoin matériel antérieur de plus de mille ans."
 ),
 limites=(
  "Le cylindre de Cyrus ne mentionne ni Jérusalem ni le Dieu d'Israël : il confirme la "
  "politique générale du conquérant, pas le décret particulier rapporté par Esdras. Cette "
  "fiche ne cite donc pas le cylindre comme une preuve du décret, mais comme une preuve "
  "de la cohérence du contexte. La date de 539 est une date neutre."
 ),
 tl=[("VIIIᵉ s.", "Isaïe nomme Cyrus"), ("539", "Babylone tombe"), ("537", "Décret publié"),
     ("537", "Retour"), ("536", "Fondations posées")],
 src=[("Le nom de Cyrus annoncé d'avance", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200274646"),
      ("La vérité sur les manuscrits de la mer Morte", "https://wol.jw.org/fr/wol/d/r30/lp-f/2001120"),
      ("La Bible a survécu aux tentatives de falsification", "https://wol.jw.org/fr/wol/d/r30/lp-f/2016247"),
      ("Une date pivot de l'Histoire — 537", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684")],
 img="images/prophe_B004_cyrus.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B005", titre="La gloire du second temple — une prophétie qui ne s'est pas accomplie sur la pierre",
 ref="Aggée 2:1-9 ; Esdras 3:10-13 ; Zacharie 4:6-10",
 statut="Accomplissement typique (voir limites)",
 cat="B", syst="Système biblique (520 / 515)",
 reg="Registre : partie 6 (les Douze), Aggée",
 texte=[
  "« Qui reste parmi vous qui ait vu cette maison dans sa gloire première ? Et comment la "
  "voyez-vous maintenant ? N'est-elle pas comme rien à vos yeux ? » (Agg 2:3)",
  "« L'objet du désir de toutes les nations devra entrer ; et je remplirai cette maison de "
  "gloire. » (Agg 2:7)",
  "« La gloire de cette dernière maison deviendra plus grande que celle de l'ancienne. » "
  "(Agg 2:9)",
 ],
 contexte=(
  "Le chantier a repris depuis un mois seulement. Les travaux ont été interrompus pendant "
  "seize ans, depuis l'opposition des Samaritains et l'interdiction perse. Les anciens qui "
  "avaient vu le temple de Salomon pleurent en voyant les fondations du nouveau (Esdras "
  "3:12) : le second bâtiment est plus petit, plus pauvre, sans l'or du premier. Aggée "
  "intervient alors, non pour consoler, mais pour déplacer le regard."
 ),
 explication=(
  "Le raisonnement du prophète est en deux temps. D'abord il constate la médiocrité — "
  "« n'est-elle pas comme rien à vos yeux ? » — sans la nier. Ensuite il annonce un "
  "renversement : « j'ébranlerai les cieux et la terre, la mer et le sol sec », et "
  "« l'objet du désir de toutes les nations devra entrer ». Le vocabulaire de "
  "l'ébranlement est celui des théophanies : il annonce un acte de Dieu, pas un "
  "agrandissement du chantier."
 ),
 interpretation=(
  "**C'est la fiche la plus importante de la catégorie pour la méthode.** La Bibliothèque "
  "en ligne écrit expressément : « La prophétie d'Aggée ne se réalisa jamais vraiment sur "
  "le temple que le gouverneur Zorobabel acheva quatre ans plus tard, ni sur celui "
  "d'Hérode qui lui succéda, bien que Jésus-Christ se rendît à ce temple et enseignât "
  "dans ses cours. » L'organisation rattache donc l'accomplissement au **grand temple "
  "spirituel** de Dieu, entré en fonction en 29 de notre ère lors de l'onction de Jésus, "
  "et dont la gloire finale est encore future. Cette position est présentée comme telle, "
  "avec sa source — elle n'est pas dissimulée."
 ),
 accomplissement=[
  ("520 av. n. è.", "Deuxième année de Darius Iᵉʳ : les travaux reprennent après seize ans d'interruption"),
  ("520 av. n. è.", "Deux mois plus tard, Aggée prononce la prophétie de la gloire (Aggée 2:1-9)"),
  ("515 av. n. è.", "Le temple de Zorobabel est achevé — objectivement moins imposant que celui de Salomon"),
  ("Iᵉʳ s. av. n. è.", "Hérode reconstruit et agrandit le temple ; le bâtiment est somptueux"),
  ("70 de n. è.", "Le temple d'Hérode est détruit par les Romains"),
  ("29 de n. è. →", "Selon la compréhension de l'organisation, accomplissement sur le grand temple spirituel"),
 ],
 hist=(
  "Le contraste entre les deux temples n'est contesté par personne : les descriptions "
  "anciennes (1 Rois 6-7 ; Esdras 3) comme les données archéologiques concordent sur la "
  "supériorité matérielle du bâtiment de Salomon. Le Temple Scroll et les écrits de "
  "Josèphe confirment l'ampleur du chantier d'Hérode, achevé peu avant sa destruction."
 ),
 geo=(
  "Le second temple fut édifié sur l'emplacement du premier, sur le mont Moriah, sur une "
  "esplanade dont Hérode doubla la surface en la soutenant par des murs de retenue — "
  "dont subsiste le Mur occidental. La contrainte géographique explique la différence "
  "avec Salomon : l'espace disponible au sommet de l'éperon était limité, et le retour "
  "d'exil disposait de moyens infiniment moindres."
 ),
 sci=(
  "Les mesures conservées par Josèphe et par le traité mishnique des Midot permettent de "
  "comparer objectivement les deux édifices : le temple de Zorobabel, tel que le décrit "
  "le décret de Cyrus rapporté en Esdras 6:3, mesurait soixante coudées de haut et autant "
  "de large, sans indication de longueur. Aucune donnée ne permet de soutenir qu'il "
  "surpassait celui de Salomon en dimensions."
 ),
 limites=(
  "**Cette fiche ne prétend pas démontrer un accomplissement matériel.** Le texte "
  "massorétique dit que la gloire de la dernière maison surpassera la première ; "
  "l'organisation elle-même reconnaît que cela ne s'est pas réalisé sur la pierre, et "
  "propose une lecture typologique vers le temple spirituel. D'autres lectures existent "
  "— notamment celle qui rapporte la gloire à la présence de Jésus dans le temple "
  "d'Hérode. Cette fiche donne la position de l'organisation avec sa source, signale les "
  "autres, et ne tranche pas par l'argument d'autorité."
 ),
 tl=[("536", "Fondations posées"), ("520", "Reprise du chantier"), ("515", "Temple achevé"),
     ("Iᵉʳ s.", "Temple d'Hérode"), ("70", "Destruction")],
 src=[("La maison remplie de gloire", "https://wol.jw.org/fr/wol/d/r30/lp-f/1953766"),
      ("Les choses désirables de toutes les nations devront entrer", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101972015"),
      ("Le grand temple spirituel de Jéhovah", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996483"),
      ("Temple (article de référence)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200014259")],
 img="images/prophe_B005_temple.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B006", titre="Jérusalem rebâtie — la ville mesurée au cordeau",
 ref="Jérémie 31:38-40 ; Zacharie 1:16 ; 8:3-5 ; Daniel 9:25 ; Néhémie 3:1-32",
 statut="Accomplie",
 cat="B", syst="Système biblique (455 / 537)",
 reg="Registre : partie 4 (Jérémie) et partie 5 (Daniel) — P385",
 texte=[
  "« Voici que des jours viennent… où la ville de Jéhovah sera rebâtie, depuis la tour de "
  "Hananéel jusqu'à la porte de l'Angle. » (Jér 31:38)",
  "« Ma maison sera rebâtie en elle, et le cordeau à mesurer sera tendu sur Jérusalem. » "
  "(Zach 1:16)",
  "« Des places publiques de Jérusalem… seront encore remplies de garçons et de filles qui "
  "joueront. » (Zach 8:5)",
  "« Depuis la sortie de la parole de rétablir et de rebâtir Jérusalem. » (Dan 9:25)",
 ],
 contexte=(
  "Jérémie annonce la reconstruction au moment même où il annonce la destruction : les "
  "deux volets du même livre, à quelques chapitres d'intervalle. Zacharie, revenu "
  "d'exil, reprend le même thème à une époque où Jérusalem est encore en grande partie "
  "en ruines et où la population découragée a cessé de construire. Daniel fixe "
  "l'échéance : soixante-neuf semaines d'années après la sortie de la parole."
 ),
 explication=(
  "Jérémie 31:38-40 est remarquable par sa précision topographique. Le texte décrit un "
  "tracé : la tour de Hananéel, la porte de l'Angle, la colline de Gareb, Goath, et « "
  "toute la vallée des cadavres ». Ce n'est pas une promesse spirituelle, c'est un "
  "relevé. La mention de la « vallée des cadavres » — probablement la vallée de Hinnom, "
  "le lieu du culte de Moloch où Josias avait profané les autels — ajoute un détail : "
  "cette zone impure sera elle aussi « sainte pour Jéhovah »."
 ),
 interpretation=(
  "La compréhension retenue est un double accomplissement : le retour effectif de 537, "
  "qui rend la ville de nouveau habitée, et l'ordre de rebâtir de 455, qui relance la "
  "muraille et fixe le point de départ des soixante-dix semaines. La Bibliothèque en "
  "ligne souligne que la parole de rebâtir **prit effet à Jérusalem**, non à Suse : "
  "l'ordre ne commence à courir qu'à son exécution."
 ),
 accomplissement=[
  (" avant 607", "Jérémie annonce la reconstruction avec le relevé topographique (Jérémie 31:38-40)"),
  ("537 av. n. è.", "Retour des exilés ; Jérusalem est de nouveau habitée et l'autel relevé"),
  ("520 av. n. è.", "Zacharie : « le cordeau à mesurer sera tendu sur Jérusalem »"),
  ("455 av. n. è.", "Néhémie obtient d'Artaxerxès l'ordre de rebâtir la muraille (Néhémie 2:1-8)"),
  ("455 av. n. è.", "La muraille est achevée en cinquante-deux jours (Néhémie 6:15)"),
 ],
 hist=(
  "Les fouilles de la ville ont livré, pour l'époque perse, une muraille dont le tracé "
  "correspond à la description de Néhémie 3 : porte des Brebis, porte des Poissons, "
  "porte de la Vallée, porte du Fumier, porte de la Source. Les segments mis au jour sur "
  "l'Ophel et dans la vieille ville datent de cette période."
 ),
 geo=(
  "Jérusalem occupe un éperon rocheux entre la vallée du Cédron à l'est et la vallée de "
  "Hinnom à l'ouest, alimenté par la source de Guihôn. Cette configuration dicte le tracé "
  "des murailles : elles suivent les lignes de crête, et les portes s'ouvrent là où les "
  "chemins arrivent. Le « cordeau à mesurer » de Zacharie est un instrument d'arpenteur, "
  "et il suppose ce relief."
 ),
 sci=(
  "L'hydrologie est ici déterminante. La source de Guihôn se trouvait hors des murs, "
  "c'est-à-dire vulnérable : d'où le tunnel d'Ézéchias, percé dans le roc sur 533 mètres "
  "pour amener l'eau à l'intérieur de l'enceinte. Une datation au carbone 14 des matières "
  "organiques incluses dans l'enduit du tunnel, publiée en 2003, confirme l'époque de ce "
  "roi. La viabilité de la ville rebâtie dépendait de ce type d'ouvrage."
 ),
 limites=(
  "Jérémie 31:38-40 est parfois lu comme une prophétie à portée eschatologique, la "
  "« ville de Jéhovah » désignant une réalité future. Cette fiche retient "
  "l'accomplissement historique, qui est vérifiable, et ne se prononce pas sur "
  "l'existence d'un accomplissement ultérieur : ce qui n'est pas encore accompli reste "
  "sans date."
 ),
 tl=[("av. 607", "Jérémie décrit le tracé"), ("537", "Ville réhabitée"), ("520", "Cordeau tendu"),
     ("455", "Ordre de rebâtir"), ("455", "Muraille en 52 jours")],
 src=[("Néhémie — la reconstruction de la muraille", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013310"),
      ("Le saviez-vous ? — le tunnel d'Ézéchias et sa datation", "https://wol.jw.org/fr/wol/d/r30/lp-f/2009333"),
      ("Jérusalem — article de référence", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200012382"),
      ("Soixante-dix semaines", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013825")],
 img="images/prophe_B006_jerusalem_rebatie.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B007", titre="La palissade de pieux — Jésus décrit le siège de 70",
 ref="Luc 19:41-44 ; 21:20-24 ; Matthieu 24:15-22 ; Marc 13:14-20",
 statut="Accomplie",
 cat="B", syst="Dates neutres (66, 70, 73)",
 reg="Registre : partie 9-10, le signe composite et Jérusalem 70 — P679 à P690",
 texte=[
  "« Tes ennemis feront une fortification autour de toi, avec des pieux taillés en "
  "pointe, et t'encercleront, et te presseront de toutes parts. » (Luc 19:43)",
  "« Ils te fracasseront sur le sol, toi et tes enfants au-dedans de toi. » (Luc 19:44)",
  "« Quand vous verrez Jérusalem encerclée par des armées qui campent, alors sachez que "
  "sa désolation s'est approchée. » (Luc 21:20)",
  "« Que ceux qui sont en Judée se mettent à fuir vers les montagnes. » (Luc 21:21)",
 ],
 contexte=(
  "Jésus prononce ces paroles vers 33 de notre ère, en descendant du mont des Oliviers "
  "vers Jérusalem, en vue des murailles et du temple. Trente-sept ans plus tard, la ville "
  "est assiégée. La prophétie est prononcée à une époque où rien ne laisse présager une "
  "rupture entre Rome et la Judée : le temple est en travaux depuis des décennies et "
  "vient tout juste d'être achevé."
 ),
 explication=(
  "Deux détails portent la valeur probante du texte. (1) La **fortification de pieux "
  "taillés en pointe** : il ne s'agit pas d'un siège en règle contre les murailles, mais "
  "d'un ouvrage d'investissement construit autour de la ville pour affamer ses habitants "
  "— un procédé que Jésus décrit avec le vocabulaire exact. (2) La consigne de fuir « vers "
  "les montagnes », sans entrer dans la ville : elle suppose que le siège connaîtra une "
  "interruption permettant la fuite, ce qui est historiquement le cas en 66."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus décrivait d'avance la "
  "circonvallation romaine : une palissade fortifiée de pieux aiguisés, longue de huit "
  "kilomètres, destinée à empêcher toute sortie. La Bibliothèque en ligne relève que le "
  "siège dura 142 jours, du 14 Nisan au 7 Élul, soit jusqu'au 30 août 70 selon le "
  "calendrier grégorien, et que 97 000 Juifs furent épargnés — « quelque chair sauvée »."
 ),
 accomplissement=[
  ("33 de n. è. env.", "Jésus annonce la fortification de pieux et la destruction de la ville"),
  ("66 de n. è.", "Cestius Gallus assiège Jérusalem, puis se retire brusquement — fenêtre de fuite"),
  ("66 de n. è.", "Les disciples avertis fuient vers Pella, au-delà du Jourdain, dans le pays de Galaad"),
  ("printemps 70", "Titus revient avec quatre légions ; la ville est encerclée à l'approche de la Pâque"),
  ("70 de n. è.", "Circonvallation de pieux aiguisés ; siège de 142 jours ; la ville tombe le 7 Élul (30 août)"),
  ("73 de n. è.", "Massada, dernière forteresse juive, tombe"),
 ],
 hist=(
  "Josèphe, témoin oculaire passé du côté romain, décrit la construction de la "
  "circonvallation et les horreurs du siège (Guerre des Juifs, livres V-VI). L'arc de "
  "Titus, à Rome, commémore la victoire et montre le butin du temple emporté. Les pièces "
  "frappées en 71 portant la mention IVDAEA CAPTA — « Judée captive » — avec une femme "
  "assise en deuil et un captif enchaîné, confirment la déportation annoncée en Luc 21:24."
 ),
 geo=(
  "Jérusalem est alimentée par des citernes et par les sources environnantes ; une ville "
  "assiégée y résiste mieux qu'ailleurs, ce qui obligeait l'assaillant à couper les "
  "sorties plutôt qu'à forcer les murs. Le tracé de la circonvallation, sur les collines "
  "qui dominent la ville d'environ 800 mètres d'altitude, explique sa longueur de huit "
  "kilomètres."
 ),
 sci=(
  "Les fouilles ont mis au jour, sur les pentes nord et ouest de la ville, des vestiges "
  "de la circonvallation romaine et des camps de légions, ainsi que les blocs de "
  "catapulte retrouvés dans les niveaux de destruction. Les données stratigraphiques "
  "confirment un incendie généralisé, cohérent avec le récit de Josèphe sur l'embrasement "
  "du temple."
 ),
 limites=(
  "La prophétie de Luc 21 a un double horizon, et l'organisation le dit : une partie "
  "s'accomplit en 66-70, une partie regarde plus loin. Cette fiche s'en tient au premier "
  "accomplissement, qui est vérifiable. Aucune date n'est avancée pour le second : « Quant "
  "à ce jour-là et à cette heure-là, personne ne les connaît » (Matthieu 24:36)."
 ),
 tl=[("33", "Jésus annonce le siège"), ("66", "Cestius Gallus"), ("66", "Fuite à Pella"),
     ("70", "Circonvallation"), ("70", "Ville prise")],
 src=[("Le « signe » annoncé sera bientôt accompli", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101973026"),
      ("Que le lecteur exerce son discernement (66-70)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1999323"),
      ("Fuite vers les montagnes — Cestius Gallus et Pella", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996404"),
      ("Luc 21 (texte et notes)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/42/21"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_B007_siege_70.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B008", titre="« Pas pierre sur pierre » — la fin du temple",
 ref="Matthieu 24:1, 2 ; Marc 13:1, 2 ; Luc 21:5, 6",
 statut="Accomplie",
 cat="B", syst="Dates neutres (70, 73)",
 reg="Registre : partie 9-10, Jérusalem 70 — P679 à P690",
 texte=[
  "« Vraiment je vous le dis : il ne restera pas ici pierre sur pierre, rien qui ne soit "
  "démoli. » (Matthieu 24:2)",
  "« Vois quelles pierres et quelles constructions ! » (Marc 13:1)",
  "« Quant à ces choses que vous contemplez, des jours viendront où il ne sera laissé "
  "pierre sur pierre qui ne soit démolie. » (Luc 21:6)",
 ],
 contexte=(
  "Les disciples admirent le temple. Le bâtiment qu'ils ont sous les yeux est celui "
  "d'Hérode, une reconstruction colossale entreprise vers 19 avant notre ère, dont le "
  "chantier venait de s'achever. Josèphe rapporte que les pierres du temple mesuraient "
  "jusqu'à une dizaine de mètres de long et que ses portes, immenses, exigeaient "
  "plusieurs hommes pour être manœuvrées. L'admiration des disciples est donc fondée : "
  "c'est l'un des bâtiments les plus impressionnants du monde antique."
 ),
 explication=(
  "La formule « pas pierre sur pierre » est une hyperbole orientale courante pour dire "
  "« détruit de fond en comble ». Le débat exégétique porte donc sur le degré de "
  "littéralité. Deux remarques : (1) la formule est employée deux fois dans les trois "
  "Évangiles synoptiques, ce qui en fait un élément solide de la tradition ; (2) Jésus "
  "avait averti que le temple serait laissé « désert » (Matthieu 23:38) — le jugement "
  "précède la destruction."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que la prophétie s'est accomplie de façon "
  "remarquable en 70 : la ville fut complètement rasée, à l'exception d'une partie de la "
  "muraille et de trois tours que Titus laissa volontairement debout pour témoigner de la "
  "puissance de ses fortifications. La Bibliothèque en ligne relève également que l'or du "
  "toiture fondit dans les interstices des pierres sous l'effet de l'incendie, et que la "
  "récupération de ce métal précipita le démontage pierre par pierre."
 ),
 accomplissement=[
  ("33 de n. è. env.", "Jésus annonce : il ne restera pas pierre sur pierre"),
  (" printemps 70", "Titus encercle la ville ; les factions juives incendient une partie des réserves"),
  (" été 70", "Le temple est incendié ; l'or de la toiture fond entre les pierres"),
  ("70 de n. è.", "La ville est rasée, sauf une partie de la muraille et trois tours laissées par Titus"),
  ("73 de n. è.", "Massada tombe ; la Judée est entièrement soumise"),
  (" aujourd'hui", "Il subsiste des vestiges des murs de soutènement de l'esplanade, mais aucun vestige du temple lui-même au-dessus du rocher"),
 ],
 hist=(
  "Josèphe décrit l'incendie du temple et le massacre. L'arc de Titus, érigé à Rome, "
  "représente le chandelier à sept branches et la table des pains emportés comme butin. "
  "La mention juive de la destruction est conservée dans le Talmud et dans la liturgie du "
  "9 Av."
 ),
 geo=(
  "Le temple occupait le sommet de l'éperon du mont Moriah. Hérode avait fait construire "
  "une esplanade soutenue par des murs de retenue colossaux, dont le Mur occidental est "
  "un vestige : ce mur n'appartient pas au temple lui-même, mais à la plateforme qui le "
  "portait — distinction essentielle, car c'est précisément ce que les Romains laissèrent "
  "debout."
 ),
 sci=(
  "L'archéologie confirme deux points. (1) Les pierres de l'esplanade d'Hérode, "
  "caractéristiques par leur bossage à refends et leur cadre saillant, sont visibles "
  "aujourd'hui dans les parties basses du Mur occidental et dans les fondations de "
  "l'époque : le bâtiment dont parlaient les disciples a bien existé. (2) Les fouilles "
  "menées au pied du Mur et sur l'Ophel ont livré, dans les niveaux de la destruction, "
  "les pierres effondrées du portique royal et des objets calcinés datés de 70."
 ),
 limites=(
  "La destruction ne fut pas totale au sens absolu : Titus laissa trois tours (Hippicus, "
  "Mariamne, Phasaël) et une portion de muraille, et les murs de soutènement de "
  "l'esplanade subsistent. L'organisation le signale elle-même. L'expression de Jésus "
  "doit donc être comprise comme une destruction intégrale du temple et de la ville "
  "antique — ce qui fut le cas — et non comme la disparition de toute pierre du site."
 ),
 tl=[("33", "Annonce de Jésus"), ("70", "Temple incendié"), ("70", "Ville rasée"),
     ("73", "Massada"), ("Auj.", "Aucun vestige du temple")],
 src=[("Notes d'étude sur Matthieu chapitre 24", "https://wol.jw.org/fr/wol/d/r30/lp-f/1001070624"),
      ("Une prophétie biblique que vous voyez s'accomplir", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101989040"),
      ("Matthieu 24 (texte et notes)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/40/24"),
      ("La Bible et l'Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/")],
 img="images/prophe_B008_pas_pierre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="B009", titre="Jérusalem foulée aux pieds — jusqu'à ce que les temps soient accomplis",
 ref="Luc 21:24 ; Daniel 4:16, 23-25 ; Romains 11:25",
 statut="En cours",
 cat="B", syst="Système biblique (607 / 1914)",
 reg="Registre : partie 8 et 10 — P370 ; P371 ; P690",
 texte=[
  "« Jérusalem sera foulée aux pieds par les nations jusqu'à ce que les temps fixés des "
  "nations soient accomplis. » (Luc 21:24)",
  "« Sept temps passeront sur lui. » (Daniel 4:16, 23, 25)",
  "« Un jour pour une année, un jour pour une année, voilà ce que je t'ai donné. » "
  "(Ézéchiel 4:6)",
 ],
 contexte=(
  "La phrase de Luc 21:24 est la seule de tout le discours de Jésus qui porte sur la "
  "durée, et non sur les événements. Elle clôt le passage sur la destruction de "
  "Jérusalem et ouvre sur la suite : la ville ne sera pas seulement détruite, elle sera "
  "pour une période indéfinie sous domination étrangère. Jésus renvoie à une expression "
  "qu'il n'invente pas — « les temps des nations » sont déjà chez Daniel."
 ),
 explication=(
  "L'expression grecque est composée : « temps fixés » (kairoi) et « nations » (ethnōn). "
  "Elle désigne une période déterminée, non un état permanent — la préposition « jusqu'à "
  "ce que » pose une borne. La durée n'est pas donnée ici mais dans Daniel 4 : sept "
  "temps. Le lien entre les deux textes est fait par Jésus lui-même, qui renvoie "
  "explicitement au livre de Daniel dans le même discours (Matthieu 24:15)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que les temps fixés des nations ont "
  "commencé en octobre 607, lorsque le trône de la royauté de Jéhovah à Jérusalem cessa "
  "d'être occupé, et qu'ils se sont achevés en octobre 1914, au terme des 2 520 ans "
  "annoncés symboliquement par les sept temps de Daniel 4. Le calcul est exposé en détail "
  "dans le carnet de fiches de dates du dossier, fiche 8."
 ),
 accomplissement=[
  ("607 av. n. è.", "Jérusalem est dévastée ; le trône davidique cesse ; le foulage commence"),
  ("539-332 av. n. è.", "Domination perse, puis grecque"),
  ("63 av. n. è. - 70 de n. è.", "Domination romaine ; Jérusalem est détruite en 70"),
  ("70 - 1914", "La ville passe de main en main : Romains, Byzantins, Perses, Arabes, Croisés, Ottomans"),
  ("1914 de n. è.", "Fin des temps fixés des nations selon le calcul du dossier"),
  (" depuis 1914", "La ville reste disputée : la phase du foulage aux pieds a cessé d'être la seule clé de lecture"),
 ],
 hist=(
  "L'histoire de Jérusalem depuis 70 est l'une des mieux documentées qui soient : la "
  "ville a changé de mains une vingtaine de fois en deux mille ans. Ce fait, en lui-même, "
  "n'est pas un argument : aucune prophétie n'annonce simplement qu'une ville sera "
  "disputée. L'argument porte sur le point de départ (607) et sur la durée (2 520 ans), "
  "donnés par la Bible, non par l'histoire profane."
 ),
 geo=(
  "Jérusalem est un carrefour : sur la ligne de crête qui relie la plaine côtière à la "
  "vallée du Jourdain, à mi-chemin entre Damas et l'Égypte. Cette position explique "
  "qu'elle n'ait jamais été laissée tranquille. C'est aussi pour cela que le foulage aux "
  "pieds, comme image, est géographiquement exact : toutes les armées y sont passées."
 ),
 sci=(
  "La seule donnée scientifique pertinente ici est chronologique, et elle tient en un "
  "point technique souvent négligé : le passage de 1 avant notre ère à 1 de notre ère ne "
  "comporte pas d'année zéro. Le calcul des 2 520 ans en tient compte — 606 ans + 1 an + "
  "1 913 ans — et c'est précisément ce qui fixe l'arrivée en octobre 1914 plutôt "
  "qu'octobre 1915."
 ),
 limites=(
  "**Cette fiche ne fixe aucune date d'avenir et ne se prononce pas sur ce qui suit "
  "1914.** Elle constate un terme, pas une fin du monde. L'organisation elle-même "
  "distingue la fin des temps fixés des nations — une date calculée — de la fin du système "
  "de choses — qui n'est pas datée. Toute présentation qui ferait de 1914 une échéance "
  "irait contre le texte et contre la position de l'organisation."
 ),
 tl=[("607", "Foulage commence"), ("539", "Perse"), ("63 av.", "Rome"),
     ("70", "Destruction"), ("1914", "Fin des temps fixés")],
 src=[("La scène de ce monde est en train de changer", "https://wol.jw.org/fr/wol/d/r30/lp-f/2004084"),
      ("Le Roi règne !", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101981014"),
      ("Le mystère du grand arbre est élucidé", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999025"),
      ("Que révèle la chronologie de la Bible sur l'année 1914 ?", "https://wol.jw.org/fr/wol/d/r30/lp-f/502014148")],
 img="images/prophe_B009_foulee.jpg",
))
