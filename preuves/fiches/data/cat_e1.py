#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE D-E (vague de transition) — FIN DU MESSIE SOUFFRANT + LES EMPIRES (1re partie)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="D–E",
    nom="Fin du Messie souffrant · Les empires (1re partie)",
    vague="6",
    intro=(
        "Cette vague de transition ferme la catégorie D et ouvre la catégorie E. "
        "Côté Messie souffrant, trois dernières fiches : le vinaigre de Golgotha "
        "(avec l'énigme roseau-hysope), le berger frappé et les brebis dispersées "
        "dans la nuit du 14 Nisan, et le serpent d'airain — le regard qui sauve, "
        "de Moïse à Nicodème. La catégorie D compte ainsi 12 fiches et est terminée. "
        "Côté empires, six premières fiches suivent Daniel : la statue du songe "
        "(chapitre 2), les quatre bêtes (chapitre 7), le bélier et le bouc "
        "(chapitre 8), les rois du nord et du sud jusqu'en 164 (chapitre 11 "
        "antique), la nuit de Belschatsar (chapitre 5), et l'énigme de Darius le "
        "Mède — traitée avec toutes ses hypothèses, y compris non conclusives. "
        "Deux renvois de périmètre : Daniel 4 (les sept temps) et Daniel 9 (les "
        "soixante-dix semaines) appartiennent à la catégorie F (chronologies) ; "
        "Daniel 12 et la synthèse des sept puissances viendront dans la 2e partie "
        "des empires (vague 7)."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D010", titre="Le vinaigre — j'ai soif, tout est accompli",
 ref="Psaume 69:21 ; Psaume 22:15 ; Matthieu 27:34, 47-50 ; Marc 15:23, 36 ; Jean 19:28-30",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Psaumes — P545, P635 (69:21) ; P632 (22:15)",
 texte=[
  "« Pour nourriture ils m'ont donné du poison ; pour ma soif, ils m'ont abreuvé "
  "de vinaigre. » (Ps 69:21)",
  "« Jésus, sachant que tout était déjà accompli, dit, afin que l'Écriture fût "
  "accomplie : J'ai soif. » (Jn 19:28 — il a soif ET il accomplit)",
  "« Il y avait là un vase plein de vinaigre. On remplit de vinaigre une éponge, "
  "on la fixa à une branche d'hysope et on l'approcha de sa bouche. Quand Jésus "
  "eut pris le vinaigre, il dit : Tout est accompli. » (Jn 19:29-30)",
  "« On lui donna à boire du vin mêlé de fiel ; mais quand il l'eut goûté, il "
  "ne voulut pas boire. » (Mt 27:34 — le premier breuvage, refusé)",
 ],
 contexte=(
  "Le Psaume 69 (David : la noyade, puis « le zèle de ta maison me dévore », v. 9, "
  "cité pour la purification du Temple en Jn 2:17 — même psaume aux deux bouts du "
  "ministère !) promet le fiel et le vinaigre. À Golgotha, deux breuvages se "
  "succèdent : d'abord le vin drogué offert avant la mise au poteau — stupéfiant "
  "des condamnés (Pr 31:6-7 : « donnez des liqueurs fortes à celui qui va périr »), "
  "refusé après un goût : Jésus veut sa pleine conscience. Puis, à la 9e heure, "
  "le vinaigre des soldats, accepté — aussitôt suivi de tetelestai."
 ),
 explication=(
  "Deux offrandes, deux sens : le narcotique refusé (lucidité du sacrifice) et "
  "le vinaigre accepté (l'Écriture jusqu'au bout). Le vinaigre (oxos), c'est la "
  "posca, la piquette du légionnaire : le vase est aux soldats romains, pas aux "
  "Juifs. L'hysope est l'herbe de la Pâque : avec elle, en 1513, on a mis le sang "
  "sur les linteaux (Ex 12:22) — la même plante présente le vinaigre à l'Agneau "
  "(voir D004). « J'ai soif » est la seule parole de souffrance physique : "
  "Psaume 22:15 (« ma langue colle ») et Psaume 69:21 — deux psaumes, une soif. "
  "Et « tout est accompli » vient juste après la gorgée : le vinaigre est le "
  "dernier accomplissement avant la mort."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus, maître de l'heure "
  "jusqu'au bout, provoque lui-même le dernier accomplissement : sachant que "
  "« tout était déjà accompli », il dit « j'ai soif » afin que le reste — "
  "le Psaume 69:21 — s'accomplisse aussi. Les soldats, « sans le savoir », "
  "exécutent l'ordonnance : éponge, hysope, bouche. Les bystanders, entendant "
  "« Eli », comprennent « Élie » (Mt 27:47-49) : le malentendu araméen fait "
  "partie de la scène — on attend Élie qui ne viendra pas, pendant que l'Écriture "
  "s'achève."
 ),
 accomplissement=[
  ("Xe s. av. n. è.", "Psaumes 69:21 et 22:15 : le vinaigre et la langue collée"),
  ("33 de n. è., 14 Nisan, matin", "Le vin mêlé de fiel proposé puis refusé (Mt 27:34 ; Mc 15:23)"),
  ("33 de n. è., 9e heure", "« Eli » confondu avec « Élie » par les assistants (Mt 27:47-49)"),
  ("33 de n. è., 9e heure", "« J'ai soif » ; éponge de vinaigre sur l'hysope (Jn 19:28-29)"),
  ("33 de n. è., 9e heure", "« Tout est accompli » — et il rend l'esprit (Jn 19:30)"),
 ],
 hist=(
  "La posca (eau vinaigrée) est la boisson réglementaire du soldat romain : le "
  "vase plein au pied du poteau est l'équipement de l'escouade. Proverbes 31:6-7 "
  "fonde l'usage du vin stupéfiant aux condamnés, et la tradition juive "
  "postérieure (Talmud) l'attribue aux femmes de Jérusalem — citée comme "
  "tradition, pas comme preuve. L'hysope pascale (Ex 12:22) boucle les quinze "
  "siècles : la plante des linteaux sert l'Agneau. Marc 15:23 précise le premier "
  "breuvage : « vin parfumé de myrrhe » — la myrrhe, analgésique antique."
 ),
 geo=(
  "Le vase est là, au poste de garde : Golgotha est un lieu d'exécution romain "
  "tenu par une escouade avec son équipement. L'hysope pousse sur les vieux murs "
  "(1R 4:33, « depuis le cèdre jusqu'à l'hysope qui sort du mur ») : plante des "
  "pierres de Jérusalem. Reste l'énigme de la hauteur : une tige d'hysope "
  "(quelques dizaines de centimètres) ne hisse pas une éponge à une bouche "
  "d'homme — les synoptiques disent « roseau » (Mt 27:48, kalamos). Voir Limites."
 ),
 sci=(
  "La médecine de la suspension explique la soif : hémorragies (flagellation, "
  "clous), sueur, asphyxie progressive — la déshydratation est le symptôme "
  "cardinal, et « langue collée » (Ps 22:15) le signe clinique. La botanique "
  "identifie généralement l'hysope biblique à l'origan de Syrie (Origanum "
  "syriacum, le za'atar) — identification débattue (voir Limites). La "
  "pharmacologie antique confirme vin + myrrhe/fiel comme sédatif : le premier "
  "breuvage est une anesthésie, refusée."
 ),
 limites=(
  "Roseau (synoptiques) ou hysope (Jean) ? La fiche rapporte les deux sans les "
  "confondre ; la conjecture de critiques lisant « javelot » (hyssos) au lieu "
  "d'« hysope » (hyssopos) est une hypothèse, non tranchée ici. L'espèce exacte "
  "de l'hysope est débattue. « Élie » est le malentendu des assistants (Eli "
  "araméen), pas une attente de Jésus. Le vase de posca est un équipement "
  "romain, pas un vase rituel."
 ),
 tl=[("Xe s.", "Ps 69:21 + 22:15"), ("Pr 31", "Le vin des condamnés"), ("14 Nisan, matin", "Vin refusé"),
     ("9e heure", "« J'ai soif »"), ("9e heure", "Vinaigre, tetelestai")],
 src=[("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Psaume 69 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/69"),
      ("Matthieu 27 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/27"),
      ("Jean 19 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/19")],
 img="images/prophe_D010_vinaigre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D011", titre="Le berger frappé — tous s'enfuirent, cette nuit",
 ref="Zacharie 13:7 ; Matthieu 26:31-32, 56 ; Marc 14:27, 50-52 ; Jean 16:32 ; Luc 22:31-32",
 statut="Accomplie",
 cat="D", syst="Système 33",
 reg="Registre : Zacharie — P622 (13:7) ; contexte nuit : P705 (reniement, cité)",
 texte=[
  "« Épée, réveille-toi contre mon berger, contre l'homme qui est mon compagnon, "
  "dit Jéhovah des armées. Frappe le berger, et les brebis seront dispersées ; "
  "et je ramènerai ma main sur les petits. » (Za 13:7)",
  "« Vous trébucherez tous à cause de moi, cette nuit ; car il est écrit : Je "
  "frapperai le berger, et les brebis du troupeau seront dispersées. » (Mt 26:31)",
  "« Mais après ma résurrection, je vous précéderai en Galilée. » (Mt 26:32 — "
  "la restauration promise AVANT la chute)",
  "« Alors tous les disciples l'abandonnèrent et s'enfuirent. » (Mt 26:56)",
 ],
 contexte=(
  "Zacharie 13 (après les idoles retranchées et les faux prophètes confus, "
  "13:2-6) ordonne à l'épée de frapper — vers 520-518. La nuit du 14 Nisan 33 : "
  "la Cène (l'annonce, Mt 26:31-32 ; le discours d'adieu : « vous me laisserez "
  "seul », Jn 16:32), Gethsémani (les trois dorment pendant l'agonie), "
  "l'arrestation (cohorte et gardes, Jn 18:3, 12), la fuite de tous — puis Pierre "
  "suit de loin jusqu'à la cour, et renie (Mt 26:33-35, 69-75 : l'autre face de "
  "la nuit, citée ici, P705)."
 ),
 explication=(
  "« Mon berger… l'homme qui est mon compagnon » (amit : prochain, égal) : le "
  "Berger est dans une proximité unique avec Dieu — et c'est Dieu qui commande "
  "l'épée (« réveille-toi ») : le Père frappe le Fils (cf. Is 53:10). « Tous » "
  "est universel : même les trois de Gethsémani, même Jean — qui reviendra le "
  "premier au pied du poteau (Jn 19:26). La fin du verset 7 est la restauration : "
  "« je ramènerai ma main sur les petits » — la main qui frappe revient protéger ; "
  "Matthieu 26:32 la traduit : « je vous précéderai en Galilée ». Le Berger "
  "précède toujours (cf. Mc 10:32). Marc 14:51-52 ajoute le jeune homme en drap "
  "qui s'enfuit nu : détail d'autopsie honteux — la tradition y voit Marc "
  "lui-même (non prouvé, voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus cite l'oracle PAR AVANCE, "
  "comme avertissement : la prophétie précède la chute de quelques heures, et la "
  "restauration (Galilée) est promise dans la même phrase. La fuite de tous "
  "accomplit la dispersion ; le rassemblement en Galilée (Mt 28:16 ; Jn 21 — "
  "dont Pierre rétabli par trois « m'aimes-tu ? ») accomplit la main revenue. "
  "À Pierre, la restauration est promise nominativement : « quand tu seras "
  "revenu, fortifie tes frères » (Lc 22:32) — avant même le coq."
 ),
 accomplissement=[
  ("520-518 av. n. è.", "Zacharie 13:7 : l'épée, la dispersion, la main revenue"),
  ("33 de n. è., 14 Nisan au soir", "La Cène : l'annonce (Mt 26:31-32) et l'avertissement à Pierre (Lc 22:31-32)"),
  ("33 de n. è., nuit", "Gethsémani : sommeil des trois ; arrestation ; fuite de tous (Mt 26:56)"),
  ("33 de n. è., nuit", "Le jeune homme du drap (Mc 14:51-52) ; Pierre suit, puis renie"),
  ("33 de n. è., après le 16", "Galilée : le Berger précède, les brebis reviennent (Mt 28:16 ; Jn 21)"),
 ],
 hist=(
  "L'arrestation mobilise une force disproportionnée (cohorte romaine + gardes "
  "du Temple, Jn 18:3, 12) : la peur d'une émeute pascale. Pierre est trahi par "
  "son accent : « ton langage te fait reconnaître » (Mt 26:73) — le dialecte "
  "galiléen dans une cour judéenne. Le « chant du coq » désigne aussi la 3e "
  "veille romaine (le gallicinium, vers 3 heures ; cf. Mc 13:35 qui liste les "
  "veilles) : l'heure du reniement est militaire. Le critère de l'embarras "
  "plaide pour l'authenticité : aucune communauté n'invente la fuite de tous ses "
  "chefs et un témoin en fuite nue."
 ),
 geo=(
  "Cénacle (Jérusalem) → Cédron franchi de nuit (Jn 18:1) → Gethsémani (pied des "
  "Oliviers) → palais d'Anne et Caïphe (Pierre dans la cour, au feu de braise, "
  "Jn 18:18) : la nuit descend et disperse. Puis la remontée : Jérusalem "
  "(chambre haute, Jn 20) → Galilée (montagne, Mt 28:16 ; lac, Jn 21) — la "
  "restauration a une région, celle de l'appel (voir C008). « Je vous précéderai » : "
  "le Berger rouvre la marche."
 ),
 sci=(
  "La chronologie de la nuit est resserrée : Cène le soir, arrestation dans la "
  "nuit, procès à l'aube, Golgotha à 9 heures — une douzaine d'heures, dont le "
  "coq vers 3 heures. La physiologie éclaire Gethsémani : nuit pascale, repas, "
  "tristesse — « leurs yeux étaient appesantis » (Mt 26:43) ; la fiche ne "
  "diagnostique pas au-delà. La critique textuelle note la stabilité de Marc "
  "14:51-52 dans tous les manuscrits : l'Église a gardé sa honte sans retouche."
 ),
 limites=(
  "Le jeune homme du drap (Marc lui-même ?) : tradition non prouvée. « Mon "
  "compagnon » (amit) dit une proximité unique : la fiche reste lexicale, sans "
  "débat trinitaire (règle 7). Le reniement de Pierre (P705) est cité en contexte, "
  "non développé. Le coq : animal et nom de veille — les deux sens coexistent, "
  "non tranchés. Zacharie 13:8-9 (deux tiers retranchés, le tiers éprouvé) : "
  "portée débattue, signalée et non développée."
 ),
 tl=[("520-518", "Za 13:7"), ("14 Nisan au soir", "L'annonce"), ("Nuit", "Fuite de tous"),
     ("Nuit", "Pierre"), ("Après le 16", "Galilée : main revenue")],
 src=[("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Zacharie 13 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/38/13"),
      ("Matthieu 26 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/26"),
      ("Marc 14 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/41/14")],
 img="images/prophe_D011_berger.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="D012", titre="Le serpent d'airain — élevé, regardé, vivant",
 ref="Nombres 21:4-9 ; Jean 3:14-16 ; Jean 8:28 ; 12:32-34 ; 2 Rois 18:4",
 statut="Accomplie",
 cat="D", syst="Système 1513/33/36",
 reg="Registre : Nb 21:4-9 sans entrée dédiée (lacune signalée, C8 — comme Mt 2:23 en C014)",
 texte=[
  "« Fais-toi un serpent brûlant et mets-le sur une perche : quiconque aura été "
  "mordu et le regardera vivra. » (Nb 21:8)",
  "« Et comme Moïse éleva le serpent dans le désert, il faut de même que le Fils "
  "de l'homme soit élevé, afin que quiconque croit ait la vie éternelle. » "
  "(Jn 3:14-15 — suivi de Jean 3:16)",
  "« Quand vous aurez élevé le Fils de l'homme, alors vous connaîtrez qui je "
  "suis. » (Jn 8:28)",
  "« Et moi, quand j'aurai été élevé de la terre, j'attirerai tous les hommes "
  "à moi. » (Jn 12:32 — « il indiquait de quelle mort il allait mourir », 12:33)",
  "« Il mit en pièces le serpent d'airain que Moïse avait fait, car les Israélites "
  "lui brûlaient du parfum : on l'appelait Nehoushtan. » (2R 18:4)",
 ],
 contexte=(
  "Quarantième année du désert : Édom refuse le passage (Nb 20:14-21), il faut "
  "contourner par la mer Rouge ; le peuple murmure contre la manne (« ce pain "
  "misérable », Nb 21:5) ; les serpents « brûlants » frappent ; Moïse intercède. "
  "Sept siècles plus tard, Ézéchias brise l'objet conservé, devenu idole encensée "
  "(2R 18:4). Et Jésus, par trois fois (Jn 3, 8, 12 — à Nicodème de nuit, aux "
  "Juifs, aux Grecs venus voir), fait du serpent élevé l'image de sa propre "
  "élévation."
 ),
 explication=(
  "« Brûlants » (seraphim — le mot même des séraphins d'Ésaïe 6 !) : le venin "
  "brûle. Le remède est le paradoxe : l'image du fléau guérit du fléau — le mal "
  "cloué sauve (cf. Rm 8:3). « Regarder et vivre » : pas de rite, pas de prix — "
  "le salut le plus simple, la foi comme regard. « Élevé » (hypsoô) a chez Jean "
  "un double sens : élevé sur le poteau ET exalté — la honte est la gloire "
  "(Jn 3:14 ; 8:28 ; 12:32). Nehoushtan, c'est « un bout de bronze » (nahash, "
  "serpent + nehoshet, bronze) : Ézéchias désacralise sept siècles de superstition "
  "d'un mot méprisant."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que Jésus s'applique à lui-même "
  "le type : élevé sur le poteau à Golgotha (Jean 12:33 le précise), il attire "
  "« tous » — Juifs et nations (Corneille, 36 ; voir C012). Le verset le plus "
  "célèbre (Jn 3:16) suit immédiatement le serpent : « Dieu a tant aimé le monde » "
  "est le commentaire de l'airain. Et Nehoushtan donne la leçon inverse : l'objet "
  "du salut, conservé sept cents ans puis encensé, est brisé par le roi fidèle — "
  "le moyen n'est jamais l'objet du culte, comme les premiers chrétiens n'ont "
  "pas vénéré le poteau (voir D002)."
 ),
 accomplissement=[
  ("1473 av. n. è. env.", "Le désert : les serpents, la perche, le regard qui sauve (Nb 21:4-9)"),
  ("715 av. n. è. env.", "Ézéchias brise Nehoushtan : le salut n'est pas une idole (2R 18:4)"),
  ("30-33 de n. è.", "« Élevé » trois fois : Nicodème (Jn 3), les Juifs (Jn 8), les Grecs (Jn 12)"),
  ("33 de n. è., 14 Nisan", "Golgotha : l'élévation — honte et gloire ensemble"),
  ("36 de n. è.", "Corneille : « tous » commence (Ac 10 ; voir C012)"),
 ],
 hist=(
  "Les vipères du Néguev et de l'Araba (cérastes, échides) ont des venins "
  "« brûlants » et mortels sans traitement : le fléau a une faune. Le bronze "
  "(cuivre + étain) est le métal du sanctuaire (autel, Ex 27) : le serpent est "
  "coulé dans le métal sacré. Ézéchias (2R 18:4) met Nehoushtan au rang des hauts "
  "lieux, stèles et Achera : le serpent rejoint les idoles au rebut. Nicodème, "
  "pharisien du Sanhédrin instruit de nuit (Jn 3), ensevelira Jésus au grand jour "
  "(Jn 19:39) : l'élève du serpent porte l'Agneau."
 ),
 geo=(
  "Le contour d'Édom : refusé au passage direct (Nb 20), Israël redescend vers "
  "la mer Rouge par l'Araba — la géographie du murmure. Punon (Féinan), étape "
  "voisine (Nb 33:42-43), est une zone de mines de cuivre exploitées depuis "
  "l'Antiquité : le bronze du serpent vient de ce désert. Le Néguev et l'Araba, "
  "rocailleux et chauds, sont le pays des serpents — le décor mord."
 ),
 sci=(
  "L'ophiologie confirme le fléau : vipères à cornes et échides de l'Araba, "
  "venins hémotoxiques cytolysants — « brûlants » au sens clinique. La "
  "métallurgie du cuivre à Féinan et Timna (mines, scories, fours datés du "
  "IIe-Ier millénaire) atteste le bronze du désert. Aucun antidote antique "
  "n'existait contre ces venins : le regard qui guérit est un miracle rapporté, "
  "pas une médecine — la fiche le dit."
 ),
 limites=(
  "Nombres 21:4-9 n'a pas d'entrée au registre : lacune signalée (C8), comme "
  "Matthieu 2:23 en C014 — la fiche se cale sur le texte. L'espèce des serpents "
  "n'est pas précisée (« brûlants ») : pas de détermination. Le mécanisme "
  "(regarder = croire) est rapporté, non expliqué. Les sept cents ans de "
  "conservation sont déduits (« jusqu'alors », 2R 18:4). « Tous » (Jn 12:32) : "
  "portée universelle de l'offre, citée comme compréhension, sans débat."
 ),
 tl=[("1473 env.", "Le désert : Nb 21"), ("715 env.", "Nehoushtan brisé"), ("30-33", "« Élevé » ×3"),
     ("14 Nisan 33", "Golgotha"), ("36", "Corneille : « tous »")],
 src=[("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Nombres 21 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/4/21"),
      ("Jean 3 — Bible d'étude, notes (Nicodème)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/3"),
      ("2 Rois 18 — Bible d'étude, notes (Nehoushtan)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/18")],
 img="images/prophe_D012_serpent.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E001", titre="La statue du songe — de l'or à la pierre",
 ref="Daniel 2 ; Daniel 1:1-21 (contexte) ; Daniel 7 (parallèle, voir E002)",
 statut="Accomplie (frappe à venir, sans date)",
 cat="E", syst="Système 607/539/1914",
 reg="Registre : Daniel — P370 (2:1-43), P371 (2:34-35, 44-45)",
 texte=[
  "« Ô roi, tu regardais, et voici une grande statue : sa tête d'or fin, sa "
  "poitrine et ses bras d'argent, son ventre et ses cuisses de bronze, ses "
  "jambes de fer, ses pieds en partie de fer et en partie d'argile. » (Dn 2:31-33)",
  "« Une pierre se détacha sans le secours d'aucune main, frappa les pieds de "
  "la statue et les mit en pièces. » (Dn 2:34)",
  "« C'est toi qui es la tête d'or. » (Dn 2:38 — à Nebucadnetsar)",
  "« Dans les jours de ces rois, le Dieu des cieux établira un royaume qui ne "
  "sera jamais détruit ; il broiera tous ces royaumes et subsistera toujours. » "
  "(Dn 2:44)",
 ],
 contexte=(
  "La 2e année de Nebucadnetsar (Dn 2:1), après les trois ans de formation de "
  "Daniel et ses compagnons (Dn 1:5, 18-21) : le roi, troublé par un songe, exige "
  "des sages non seulement l'interprétation mais le songe lui-même — « la chose "
  "est résolue » (Dn 2:5) — sous peine de mort. Ariok exécute ; Daniel demande du "
  "temps, prie avec Hanania, Mishaël et Azaria ; la révélation vient de nuit ; "
  "action de grâces (Dn 2:19-23) ; puis l'audience : « il y a dans les cieux un "
  "Dieu qui révèle les secrets » (Dn 2:28). Daniel a environ vingt ans."
 ),
 explication=(
  "Les métaux décroissent en valeur (or → argile) et croissent en dureté : la "
  "statue dit la dévaluation morale et le durcissement des empires. « Inférieur » "
  "(2:39) : chaque royaume moindre en gloire que le précédent. Les pieds mêlés — "
  "fer et argile, « ils se mêleront par des alliances humaines » (2:43) — figurent "
  "la phase finale : forte et fragile à la fois. « Sans mains » : le Royaume ne "
  "vient d'aucune révolution — il est détaché par Dieu. « Dans les jours de ces "
  "rois » : le Royaume coexiste d'abord avec les derniers pouvoirs humains. "
  "« Comme la balle d'été » (2:35) : disparition totale, « nulle trace »."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah nomme les quatre premiers métaux : "
  "l'or, c'est Babylone — Daniel le dit au roi (2:37-38) ; l'argent, la "
  "Médo-Perse ; le bronze, la Grèce ; le fer, Rome. La dynastie babylonienne "
  "« commençant par Nebucadnetsar et se terminant soixante-huit ans plus tard, "
  "à la mort de Belschatsar » (607 → 539). Les pieds de fer et d'argile sont la "
  "phase finale, mêlée et fragile, contemporaine de l'établissement du Royaume — "
  "le détail est renvoyé au livre « Prêtons attention à la prophétie de Daniel » "
  "(voir Limites). La pierre, c'est le Royaume de Dieu : établi en 1914 (voir "
  "B009), il frappera à venir — sans date."
 ),
 accomplissement=[
  ("An 2 de Nebucadnetsar", "Le songe oublié, la révélation, Daniel promu (Dn 2:48-49)"),
  ("539 av. n. è.", "L'argent : la Médo-Perse prend Babylone (voir E005)"),
  ("331 av. n. è.", "Le bronze : Alexandre à Gaugamèles (voir E003)"),
  ("63 av. n. è.", "Le fer à Jérusalem : Pompée prend la ville (voir E003-E004)"),
  ("1914 de n. è.", "La pierre détachée : le Royaume établi (voir B009) ; la frappe à venir"),
 ],
 hist=(
  "La succession est celle des manuels : Babylone (jusqu'en 539), la Perse "
  "(539-331), la Grèce (331 et les diadoques), Rome (dès le IIe siècle, Pompée "
  "en Judée en 63). L'arithmétique interne est du système 607/539 : soixante-huit "
  "ans de tête d'or. Cyrus (E005), Alexandre (E003), Pompée (E003-E004) ont chacun "
  "leur fiche : la statue est le sommaire, les chapitres 5, 7, 8, 11 le "
  "développement. Daniel, promu avec ses trois compagnons (Dn 2:48-49), traverse "
  "ensuite toute la tête d'or jusqu'à Cyrus (Dn 1:21)."
 ),
 geo=(
  "Le songe a un lieu : la cour de Babylone — et les capitales glissent vers "
  "l'ouest à chaque métal : Babylone, Suse et Persépolis, Pella puis Alexandrie, "
  "Antioche et Pergame, Rome. La pierre « devient une grande montagne et remplit "
  "toute la terre » (2:35) : la montagne, c'est Sion — « la montagne de la maison "
  "de Jéhovah » (Is 2:2). De la cour babylonienne à la montagne universelle : "
  "la géographie du songe est une expansion."
 ),
 sci=(
  "La linguistique plaide pour l'authenticité : en plein verset 4, le livre "
  "bascule de l'hébreu à l'araméen — « les Chaldéens parlèrent au roi en araméen » "
  "— et y reste jusqu'à la fin du chapitre 7 : la langue de la cour est "
  "l'araméen impérial. Huit copies de Daniel à Qumrân (IIe-Ier siècle avant notre "
  "ère) placent le livre avant l'ère chrétienne. La statue colossale elle-même a "
  "son contexte : l'Orient élevait des statues composites monumentales."
 ),
 limites=(
  "L'an 2 de Nebucadnetsar n'est pas converti en année avant notre ère : les "
  "comptages babylonien et judéen divergent (Dn 1:1 // Jr 25:1) — signalé, non "
  "tranché. Le détail des pieds (identification exhaustive) est renvoyé au livre "
  "« Prêtons attention à la prophétie de Daniel ». La frappe de la pierre est à "
  "venir : sans date. 1914 est l'établissement céleste (voir B009), pas la frappe. "
  "« Soixante-huit ans » est l'arithmétique du système 607/539."
 ),
 tl=[("An 2 Neb.", "Le songe"), ("539", "Argent : Perses"), ("331", "Bronze : Grecs"),
     ("63", "Fer : Rome"), ("1914", "Pierre : Royaume")],
 src=[("La marche des puissances mondiales d'après les prophéties (Dn 2)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1961441"),
      ("Daniel, un authentique livre de prophéties", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986721"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112"),
      ("Daniel 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/2")],
 img="images/prophe_E001_statue.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E002", titre="Les quatre bêtes — et le Fils d'homme",
 ref="Daniel 7 ; Daniel 2 (parallèle, voir E001) ; Psaume 90:2 ; 1 Corinthiens 15:25",
 statut="Accomplie (tribunal à venir, sans date)",
 cat="E", syst="Système 539/1914",
 reg="Registre : Daniel — P377 (7:1-7), P378 (7:8, 24-26), P379 (7:9-14), P380 (7:27), P584 (7:13-14)",
 texte=[
  "« Quatre bêtes énormes montaient de la mer : la première comme un lion avec "
  "des ailes d'aigle ; la deuxième comme un ours ; la troisième comme un léopard "
  "à quatre ailes et quatre têtes ; la quatrième, effrayante, avec des dents de "
  "fer et dix cornes. » (Dn 7:3-7)",
  "« Une petite corne monta parmi elles, avec des yeux d'homme et une bouche "
  "qui proférait de grandes choses ; trois cornes furent arrachées devant elle. » "
  "(Dn 7:8)",
  "« Je regardais pendant que des trônes furent placés, et l'Ancien des jours "
  "s'assit ; mille milliers le servaient ; des livres furent ouverts. » (Dn 7:9-10)",
  "« Quelqu'un de semblable à un fils d'homme vint avec les nuées ; on lui donna "
  "domination, dignité et royaume — domination éternelle. » (Dn 7:13-14)",
 ],
 contexte=(
  "La 1re année de Belschatsar (Dn 7:1) : Daniel, vieillard ayant traversé tout "
  "l'empire de Nebucadnetsar, reçoit en songe le même défilé que la statue — "
  "sous l'angle bestial : le pouvoir vu par Dieu, non par les rois. L'ange "
  "interprète (7:15-27) : quatre royaumes, dix rois, « un autre », les saints à "
  "la fin. La mer, c'est l'humanité agitée (Is 17:12 : « le tumulte des peuples "
  "comme les eaux »). Les bêtes « montent » vers le prophète : l'histoire vient "
  "à Daniel."
 ),
 explication=(
  "Lion ailé : Babylone — les lions de la voie processionnelle en briques "
  "émaillées ; « ailes arrachées, cœur d'homme » (7:4) : Nebucadnetsar humilié "
  "puis restauré (Dn 4 dans Dn 7 !). Ours penché d'un côté, trois côtes aux dents : "
  "la Médo-Perse, la Perse dominant — comme la grande corne de Dn 8:3 (voir "
  "E003). Léopard à quatre ailes et quatre têtes : la vitesse d'Alexandre et ses "
  "quatre successeurs (voir E003-E004). Quatrième bête, sans nom animal — Rome, "
  "inédite : dents de fer (le fer de Dn 2 !), dix cornes — dix rois, la totalité "
  "(pas de liste nominative, voir Limites). Petite corne : yeux d'homme "
  "(intelligence), bouche (arrogance) — la Bretagne romaine devenue Empire "
  "britannique, « un quart de la surface terrestre et de la population mondiale » "
  "au XIXe siècle. Ancien des jours : Jéhovah (Ps 90:2), Juge aux livres ouverts. "
  "Fils d'homme : Jésus recevant la domination — 1914 (voir B009)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah lit les quatre bêtes comme la statue : "
  "Babylone, Médo-Perse, Grèce, Rome — « effrayante, terrible, extraordinairement "
  "forte » (7:7), née « sous la forme du pouvoir politique et militaire de Rome ». "
  "La petite corne, c'est la Grande-Bretagne : province romaine devenue « la plus "
  "grande puissance coloniale et commerciale du monde », elle « dévora toute la "
  "terre » (7:23). Puis le regard quitte les bêtes pour le ciel : tribunal, "
  "livres, et remise de la domination éternelle au Fils d'homme (1914) — les "
  "saints recevant le royaume à la fin (7:27, voir la catégorie G)."
 ),
 accomplissement=[
  ("1re année de Belschatsar", "Le songe des bêtes ; l'ange interprète (Dn 7:1, 15-27)"),
  ("539 av. n. è.", "L'ours : la Médo-Perse (voir E005)"),
  ("331 av. n. è.", "Le léopard : Alexandre (voir E003) ; 301 : les quatre têtes"),
  ("Rome, puis XIXe s.", "La 4e bête ; la petite corne : l'Empire britannique, quart du globe"),
  ("1914 de n. è.", "Le Fils d'homme reçoit (voir B009) ; le tribunal à venir"),
 ],
 hist=(
  "Les lions ailés de Babylone (voie processionnelle, ~120 lions émaillés "
  "dégagés par Koldewey dès 1899, reconstitués à Berlin et in situ) sont le "
  "portrait archéologique de la première bête. L'Empire britannique du XIXe "
  "siècle (Pax Britannica, quart du globe) accomplit la petite corne « dévorant "
  "toute la terre ». Rome (légions, droit, routes) est la bête « différente de "
  "toutes » : république devenue empire mondial. Chaque bête a son musée."
 ),
 geo=(
  "La « grande mer » (la Méditerranée, à l'ouest) : les bêtes montent vers "
  "Daniel. La Bretagne, à l'extrémité nord-ouest de l'Empire romain : la petite "
  "corne pousse aux marges — l'empire naît aux confins. Les capitales glissent "
  "toujours vers l'ouest (voir E001) : Babylone, Suse, Pella, Rome, Londres. "
  "Le tribunal, lui, n'a pas de lieu terrestre : trônes, fleuve de feu, nuées — "
  "la cour est céleste."
 ),
 sci=(
  "La zoologie symbolique est exacte en psychologie des empires : lion-aigle "
  "(majesté), ours (force lourde), léopard ailé (vitesse — Alexandre : Granique "
  "334, Issos 333, Gaugamèles 331, Indus 326, mort 323 : un monde en onze ans !), "
  "bête innommée (terreur inédite). Huit copies de Daniel à Qumrân (IIe-Ier "
  "siècle) placent la vision avant Rome impériale. La numismatique suit le "
  "défilé : dariques perses, tétradrachmes d'Alexandre, deniers romains, "
  "sovereigns britanniques."
 ),
 limites=(
  "Les dix cornes : pas de liste nominative dans les publications — dix, c'est "
  "la totalité. Les trois côtes de l'ours (proies : le livre Daniel détaille) : "
  "renvoyées à cet ouvrage. La 1re année de Belschatsar n'est pas convertie "
  "(corégence, voir E005-E006). Le tribunal (livres ouverts, 4e bête détruite) "
  "est à venir : sans date. 1914 est la remise céleste (voir B009), pas la "
  "destruction."
 ),
 tl=[("1re Belschatsar", "Le songe"), ("539", "Ours : Perses"), ("331", "Léopard : Grecs"),
     ("Rome → XIXe s.", "4e bête, petite corne"), ("1914", "Fils d'homme")],
 src=[("Qui dominera le monde ? (Dn 7, petite corne, Ancien des jours)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999028"),
      ("Daniel, un authentique livre de prophéties", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986721"),
      ("Daniel 7 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/7"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E002_betes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E003", titre="Le bélier et le bouc — Alexandre nommé par fonction",
 ref="Daniel 8 ; Daniel 7 (parallèle) ; Daniel 11:2-4 (suite, voir E004)",
 statut="Accomplie (« sans main » à venir, sans date)",
 cat="E", syst="Dates neutres (539, 331, 323, 301, 63, 70)",
 reg="Registre : Daniel — P381 (8:1-8, 20-21), P382 (8:8, 22), P383 (8:9-14, 23-25)",
 texte=[
  "« Un bélier à deux cornes, la plus grande montant après ; il frappait vers "
  "l'ouest, le nord et le sud, et nul ne lui résistait. » (Dn 8:3-4)",
  "« Un bouc venait de l'ouest, sans toucher la terre, avec une grande corne "
  "entre les yeux ; il brisa le bélier. » (Dn 8:5-7)",
  "« La grande corne fut brisée, et quatre cornes montèrent vers les quatre "
  "vents. » (Dn 8:8)",
  "« Le bélier, ce sont les rois de Médie et de Perse. Le bouc, c'est le roi de "
  "Javan ; la grande corne, c'est le premier roi. » (Dn 8:20-21 — l'ange Gabriel)",
  "« Jusqu'à deux mille trois cents soirs et matins ; puis le lieu saint sera "
  "rétabli. » (Dn 8:14)",
 ],
 contexte=(
  "La 3e année de Belschatsar (Dn 8:1), à Suse en Élam, près de l'Oulaï (Dn 8:2 — "
  "voir A012 : Daniel voit depuis la future capitale perse, lieu du deuxième "
  "empire !). Gabriel — premier ange nommé de la Bible (Dn 8:16) — explique : "
  "c'est la seule vision aussi auto-interprétée. « Vision pour le temps de la fin » "
  "(8:17, 19, 26) : le viseur est lointain. Daniel s'évanouit et reste malade "
  "(8:27) : la vision coûte."
 ),
 explication=(
  "Bélier aux cornes inégales : Mèdes puis Perses dominant — comme l'ours penché "
  "(E002) ; trois directions de conquête, comme trois côtes. Bouc « sans toucher "
  "terre » : la vitesse d'Alexandre — comme le léopard ailé (E002). « Javan » "
  "(la Grèce) et « le premier roi » : Alexandre, nommé par fonction deux cents "
  "ans d'avance. « Brisée en pleine force » : mort à 32 ans, à Babylone (323) — "
  "dans la capitale du premier empire ! Quatre cornes : les quatre diadoques "
  "(voir E004). Petite corne : sortie d'un des quatre, grandissant « vers le "
  "pays de la parure » (la Judée — Éz 20:6) : Rome, de Pompée (63) à Titus (70). "
  "2 300 soirs et matins : durée limitée de l'agression contre le sanctuaire, "
  "puis rétablissement — le sens ; le calendrier est renvoyé aux publications "
  "(voir Limites). « Brisé sans main » (8:25) : comme la pierre (E001) — fin "
  "divine."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah suit l'ange : bélier = Médo-Perse "
  "(8:20), bouc = Grèce, premier roi = Alexandre (8:21), quatre = les successeurs "
  "(8:22). La petite corne, c'est Rome : née du monde grec divisé, elle foule le "
  "sanctuaire — Pompée dans le Saint des saints (63), Titus rasant le Temple "
  "(70, voir B007-B008). Les versets 9-14 forment un tout : l'agresseur (v. 9), "
  "l'agression du sanctuaire (v. 10-12), la question « jusqu'à quand ? » (v. 13), "
  "la réponse et le rétablissement (v. 14) — le contexte interdit d'isoler le "
  "verset 14."
 ),
 accomplissement=[
  ("3e année de Belschatsar", "La vision à Suse ; Gabriel explique (Dn 8:1-2, 16)"),
  ("539 av. n. è.", "Le bélier maître du monde (voir E005)"),
  ("334-331 av. n. è.", "Le bouc : Granique, Issos, Gaugamèles — trois batailles, trois ans"),
  ("323 av. n. è.", "La grande corne brisée à Babylone ; 301 (Ipsos) : les quatre"),
  ("63 av. n. è. - 70", "La petite corne en Judée : Pompée, puis Titus (voir B007)"),
 ],
 hist=(
  "Gaugamèles (1er octobre 331) est la date la plus sûre de l'Antiquité grecque : "
  "une éclipse de lune (20 septembre 331) la précède de onze jours — l'astronomie "
  "date Alexandre. Ipsos (301) fixe les quatre : Cassandre, Lysimaque, Séleucus, "
  "Ptolémée (voir E004). Pompée (63) prend Jérusalem et pénètre dans le Saint des "
  "saints (Josèphe, Tacite) : la petite corne touche le sanctuaire. Josèphe "
  "raconte Alexandre épargnant Jérusalem devant le grand prêtre Jaddus (Antiquités "
  "XI) : tradition non confirmée ailleurs (voir Limites)."
 ),
 geo=(
  "Suse (le lieu de la vision — voir A012) ; l'ouest (le bouc vient de Macédoine) ; "
  "Gaugamèles (plaine d'Arbèles, nord mésopotamien) ; « le pays de la parure » "
  "(la Judée, Éz 20:6) ; les quatre vents (les quatre royaumes aux quatre points). "
  "Alexandre meurt à Babylone : le bouc expire dans la capitale du lion (E002) — "
  "la boucle géographique se ferme."
 ),
 sci=(
  "L'astronomie (éclipse du 20 septembre 331) ancre Gaugamèles au 1er octobre 331. "
  "La numismatique montre le conquérant cornu : les tétradrachmes posthumes de "
  "Lysimaque coiffent Alexandre des cornes de bélier d'Ammon — le « bouc » de "
  "Daniel a son portrait monnayé en bélier. Huit copies de Daniel à Qumrân "
  "placent la vision avant les diadoques accomplis. La céramique hellénistique "
  "date les strates des quatre royaumes."
 ),
 limites=(
  "Le calendrier des 2 300 soirs et matins (8:14) est renvoyé aux publications "
  "citées (l'article en contexte) : la fiche en donne le sens (agression limitée, "
  "rétablissement), pas le comput. Alexandre à Jérusalem (Josèphe seul) : "
  "tradition, pas preuve. « Brisé sans main » (8:25) : sans date. La 3e année de "
  "Belschatsar n'est pas convertie. Le développement Rome (Pompée, Hérode, 70) "
  "appartient pour l'exhaustivité au livre Daniel."
 ),
 tl=[("3e Belschatsar", "Suse : Gabriel"), ("539", "Bélier maître"), ("334-331", "Bouc : 3 batailles"),
     ("323 / 301", "Corne brisée / les 4"), ("63 - 70", "Petite corne")],
 src=[("Daniel 8:14 dans son contexte (petite corne, 2 300)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1997527"),
      ("L'Empire médo-perse et les prophéties (le bélier)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1977007"),
      ("Daniel 8 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/8"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E003_belier.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E004", titre="Les rois du nord et du sud — Raphia, Panium, l'abomination",
 ref="Daniel 10-11:1-35 ; Daniel 11:36-45 (renvoi, voir Limites) ; Jean 10:22 (la Dédicace)",
 statut="Accomplie (11:36-45 : renvoi aux publications récentes)",
 cat="E", syst="Système 537 · dates neutres (480-164)",
 reg="Registre : Daniel — P387-P402 (11:2-35) ; P403 (11:36-45, modernes, renvoi)",
 texte=[
  "« Je vais t'annoncer ce qui est inscrit dans l'Écriture de vérité. » "
  "(Dn 10:21 — le sceau : écrit avant !)",
  "« Trois rois se lèveront en Perse, puis un quatrième, très riche, soulèvera "
  "tout contre le royaume de Javan. » (Dn 11:2 — Xerxès contre la Grèce)",
  "« Un roi puissant se lèvera ; son royaume sera brisé et partagé vers les "
  "quatre vents, mais pas à sa postérité. » (Dn 11:3-4 — Alexandre)",
  "« Le roi du sud s'emportera ; mais il n'exploitera pas sa position. » "
  "(Dn 11:11-12 — Raphia, 217)",
  "« Des forces profaneront le sanctuaire, la forteresse ; ils feront cesser le "
  "sacrifice continuel et placeront l'abomination qui désole. » (Dn 11:31 — 167)",
 ],
 contexte=(
  "La 3e année de Cyrus (Dn 10:1), sur le Tigre (10:4), après vingt et un jours "
  "de jeûne : un homme vêtu de lin — et Mikaël, « l'un des premiers princes » "
  "(10:13, 21), nommé ici pour la première fois. Suit la prophétie la plus "
  "détaillée de la Bible : deux siècles de guerres syro-égyptiennes, au nord et "
  "au sud de la Judée (« le pays de la parure », 11:16) — quinze versets pour "
  "quinze rois, mariages, batailles et trahisons nommés d'avance."
 ),
 explication=(
  "Nord et Sud se mesurent depuis la Judée : Séleucides (Syrie) contre Ptolémées "
  "(Égypte). « Pas à sa postérité » (11:4) : ni Alexandre IV ni Héraclès ne "
  "règnent — assassinés (le fils posthume vers 310). Les mariages : Bérénice "
  "(252, fille du Sud au Nord — répudiée, assassinée avec son fils, 11:6) et "
  "Cléopâtre Ire (193, fille du Nord au Sud — elle prend le parti de son mari, "
  "11:17 : « elle ne tiendra pas »). Raphia (217) : Ptolémée IV gagne — « des "
  "dizaines de milliers » tombent — mais « n'exploite pas » (11:12 : retour aux "
  "plaisirs, paix rapide — Polybe confirme). Panium (198) : Antiochos III prend "
  "la Cœlé-Syrie — « il s'établira dans le pays de la parure » (11:16) : la Judée "
  "change de maître. Magnésie (190) : Rome (Scipion) — « le prince » qui arrête "
  "le Nord (11:18) ; Apamée (188) : 15 000 talents d'indemnité. L'exacteur "
  "(Séleucus IV, rançonné par Rome — Héliodore au Temple !) « brisé, ni par "
  "colère ni par guerre » (11:20 : assassiné). L'homme méprisé (Antiochos IV, "
  "« Épiphane », par flatteries, 11:21). Les Kittim (11:30 : Chypre = les Romains "
  "de l'ouest — Popilius et son cercle dans le sable, Éleusis, 168, l'été même "
  "de Pydna !). L'abomination (11:31 : autel à Zeus, 25 Kislev 167 — les "
  "Maccabées, histoire juive). « Ceux qui ont de l'intelligence » (11:33, 35) "
  "résistent « jusqu'au temps de la fin » — la charnière."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah suit le tableau : 11:5 Séleucus Ier / "
  "Ptolémée Ier (les fondateurs) ; 11:6 Antiochos II / Ptolémée II ; Évergète "
  "vengeur ; Raphia — Ptolémée IV « emportant » 10 000 fantassins, 300 cavaliers "
  "et 4 000 prisonniers ; Antiochos III, Panium, Magnésie ; Séleucus IV ; "
  "Antiochos IV, les Kittim, 167. L'ange ne nomme personne (11:5-35) « car leur "
  "identité et leur nationalité changeraient au cours des siècles » : les titres "
  "(nord/sud) survivent aux dynasties. Les versets 36-45 (identités modernes) "
  "sont renvoyés aux publications récentes (voir Limites)."
 ),
 accomplissement=[
  ("3e année de Cyrus", "La vision sur le Tigre ; Mikaël ; « l'Écriture de vérité » (Dn 10)"),
  ("480 av. n. è.", "Le 4e riche : Xerxès soulève tout contre Javan (Salamine)"),
  ("323-301 av. n. è.", "Alexandre ; « pas à sa postérité » ; Ipsos : les quatre (voir E003)"),
  ("252-241 av. n. è.", "Bérénice assassinée ; Évergète venge (11:6-9)"),
  ("217 av. n. è.", "Raphia : le Sud gagne et n'exploite pas (11:11-12 ; Polybe)"),
  ("198 av. n. è.", "Panium : le Nord prend la Cœlé-Syrie ; la Judée change de maître (11:15-16)"),
  ("193-187 av. n. è.", "Cléopâtre Ire ; Magnésie (190, Rome) ; mort d'Antiochos III (187)"),
  ("175-168 av. n. è.", "Séleucus IV ; Épiphane ; Kittim-Popilius (168, été de Pydna)"),
  ("167-164 av. n. è.", "L'abomination (25 Kislev 167) ; purification (164, Hanoukka — Jn 10:22)"),
 ],
 hist=(
  "Polybe (Histoires, V et XXIX) est le procès-verbaliste : Raphia (effectifs, "
  "éléphants indiens contre africains — « la bataille des éléphants »), le "
  "cercle de Popilius (« réponds avant d'en sortir »). Le décret de Raphia "
  "(stèle trilingue de 217) célèbre officiellement la victoire. Tite-Live (XLV) "
  "confirme 168. Les livres des Maccabées (histoires juives non canoniques : "
  "Apollonius, l'autel, les porcs, les livres brûlés, Judas, 164) documentent "
  "11:31-35 — cités comme sources, pas comme Écriture. Héliodore au Temple "
  "(2 Maccabées 3) illustre l'exacteur. Jésus fréquente la fête née de 164 "
  "(la Dédicace, Jn 10:22)."
 ),
 geo=(
  "Raphia (frontière Gaza-Sinaï : la porte de l'Égypte) ; Panium (sources du "
  "Jourdain — Jésus y mènera les disciples : « Tu es Pierre », Mt 16:13, sur le "
  "champ de bataille de Daniel 11 !) ; la Cœlé-Syrie (pomme de discorde) ; "
  "Magnésie (Asie Mineure) ; Éleusis (faubourg d'Alexandrie : le cercle) ; "
  "le « pays de la parure » au milieu, tiraillé cent cinquante ans. Pydna "
  "(Macédoine, 22 juin 168) : la petite corne romaine écrase le monde grec "
  "l'été même où elle humilie le Nord."
 ),
 sci=(
  "L'épigraphie trilingue (décret de Raphia, 217 : hiéroglyphique, démotique, "
  "grec) atteste officiellement la bataille. La numismatique monnaye l'orgueil : "
  "Antiochos IV « Théos Épiphane » (« Dieu manifesté ») sur ses tétradrachmes — "
  "surnommé « Épimane » (le Fou) par ses sujets (Polybe). Les fouilles de "
  "Jérusalem (parking Givati, 2015 : forteresse séleucide, frondes, monnaies "
  "d'Antiochos IV) sont proposées comme l'Acra — identification débattue "
  "(voir Limites)."
 ),
 limites=(
  "Daniel 11:36-45 (identités modernes) est renvoyé aux publications récentes : "
  "cette fiche s'arrête à 164. L'article de 1981 identifiait le Nord à l'URSS : "
  "actualisé par les publications postérieures à 1991 — signalé, pas caché. "
  "1-2 Maccabées : histoires juives non canoniques, citées comme sources. L'Acra "
  "(Givati) : identification débattue. Les effectifs antiques sont des ordres de "
  "grandeur. « Jusqu'au temps de la fin » (11:35) : charnière non datée."
 ),
 tl=[("3e Cyrus", "Tigre : vision"), ("480", "Xerxès"), ("217", "Raphia"), ("198", "Panium"),
     ("190", "Magnésie"), ("168", "Kittim + Pydna"), ("167-164", "Abomination, purification")],
 src=[("Deux rois en conflit (Dn 11:5-19, tableau, Raphia)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101999032"),
      ("L'issue du conflit (les deux rois rivaux)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1981522"),
      ("Daniel 11 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/11"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E004_raphia.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E005", titre="La nuit de Belschatsar — compté, pesé, divisé",
 ref="Daniel 5 ; Ésaïe 13 ; 21:5 ; 44:27-45:2 ; Jérémie 50-51 ; Esdras 1:7-11",
 statut="Accomplie",
 cat="E", syst="Système 539",
 reg="Registre : Daniel — P374 (5:5-28), P375 (5:23-24) ; Babylone : voir F003 (désolation)",
 texte=[
  "« Belschatsar donna un grand festin à ses dignitaires, au nombre de mille ; "
  "on apporta les vases d'or et d'argent pris dans le temple de Jérusalem, et "
  "le roi et ses dignitaires y burent. » (Dn 5:1-3)",
  "« À ce moment apparurent les doigts d'une main d'homme, qui écrivirent, face "
  "au chandelier, sur la chaux de la muraille du palais royal. » (Dn 5:5)",
  "« Quiconque lira cette écriture sera revêtu de pourpre, avec une chaîne d'or, "
  "et sera le troisième dans le royaume. » (Dn 5:7, 29)",
  "« MENE, MENE, TEQEL, PARSIN : compté, compté, pesé, divisé. » (Dn 5:25-28)",
  "« Cette nuit-là, Belschatsar, le roi chaldéen, fut tué. » (Dn 5:30)",
 ],
 contexte=(
  "La nuit du 11 au 12 octobre 539 : Opis tombée, Sippar prise (14 Tashritu), les "
  "Perses marchent sur Babylone — et le palais festoie. Nabonide, le roi en titre, "
  "est effacé (retour de Tayma, défaite) ; Belschatsar, son fils et corégent, "
  "tient la ville. Les prophètes avaient annoncé le festin-surprise : « Dressez "
  "la table, posez la garde, mangez, buvez — debout, chefs ! » (Is 21:5) ; "
  "« Quand ils seront échauffés, je leur préparerai un festin » (Jr 51:39) ; "
  "« Je les enivrerai d'un sommeil éternel » (Jr 51:57). Voir F003 pour la "
  "désolation durable : ici, la nuit."
 ),
 explication=(
  "Le sacrilège : boire aux dieux d'or et d'argent dans les vases de Jéhovah "
  "(5:3-4) — le festin est un blasphème avant d'être une fête. « Troisième » : "
  "Nabonide 1er, Belschatsar 2nd — la corégence explique le rang offert. La reine "
  "qui entre (5:10-12), c'est probablement la reine-mère — non identifiée sûrement "
  "(voir Limites). Daniel refuse les dons AVANT de lire (5:17) : le prophète ne "
  "se paie pas. MENE (compter — la mine, poids-monnaie : les jours sont comptés), "
  "TEQEL (peser — le sicle : « trop léger » à la balance), PERES (diviser… et "
  "« Perse » ! le jeu de mots : divisé, donné aux Mèdes et aux Perses). « Cette "
  "nuit-là » : prophétie et chute la même nuit. Face au chandelier, sur la chaux : "
  "le détail visuel du témoin — les palais mésopotamiens sont enduits de plâtre."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah est que l'écriture est l'arrêt : "
  "compté (le règne), pesé et trop léger (le roi), divisé (le royaume). "
  "Belschatsar tient parole et revêt Daniel de pourpre (5:29) — « non pour se "
  "glorifier, mais pour honorer Jéhovah ». Pendant ce temps, dans le lit du "
  "fleuve, les Mèdes et Perses avancent des deux côtés vers le centre — les "
  "portes des quais, en cette nuit de fête, « auront été laissées ouvertes » : "
  "entrée sans coup férir. Ésaïe 44:27 (« à l'abîme : dessèche-toi ») et 45:1-2 "
  "(« les portes ne seront pas fermées », verrous de fer brisés) s'accomplissent "
  "dans l'hydraulique."
 ),
 accomplissement=[
  ("VIIIe-VIe s. av. n. è.", "Ésaïe 13, 21, 44-45 ; Jérémie 50-51 : le festin, le fleuve, les portes"),
  ("556-539 av. n. è.", "Nabonide (Tayma) ; Belschatsar corégent à Babylone"),
  ("Octobre 539", "Opis, puis Sippar (14 Tashritu) : les verrous sautent"),
  ("Nuit du 11/12 octobre 539", "Festin, vases, écriture, Daniel 3e — et le fleuve détourné"),
  ("12 octobre 539 (16 Tashritu)", "Entrée de Gobryas ; Belschatsar tué (Dn 5:30) ; Darius reçoit (voir E006)"),
 ],
 hist=(
  "La Chronique de Nabonide (tablette cunéiforme BM 35382) date : Sippar le 14, "
  "Babylone le 16 Tashritu — Gobryas entre, qu'on nomme gouverneur. Le cylindre "
  "de Cyrus clame une entrée « sans bataille » : la ville festoie, la propagande "
  "triomphe. Hérodote (I, 190-191) : Euphrate détourné vers les marais, fête, "
  "les quartiers extrêmes ignorant la prise. Xénophon (Cyropédie VII, 5) : "
  "le fleuve abaissé, les portes du fleuve ouvertes un soir de fête — Gobryas "
  "et Gadatas. Un cylindre de Nabonide (Ur) prie pour « Belschatsar, mon fils "
  "premier-né » : le corégent a son inscription. Et les vases profanés regagnent "
  "Jérusalem sous Cyrus (Esd 1:7-11 : 5 400 pièces) : la boucle."
 ),
 geo=(
  "L'Euphrate traverse Babylone : quais, portes fluviales, pont — le fleuve est "
  "la faille de l'imprenable. Les doubles murailles (Imgur-Enlil, Nemed-Enlil) "
  "et le fossé défient les armées, pas l'assèchement. La salle du trône fouillée "
  "(52 × 17 mètres, murs enduits) est le décor de la chaux éclairée. Opis et "
  "Sippar, au nord, sont les verrous : tombés, la route de Babylone est ouverte. "
  "Octobre, c'est les basses eaux : la date fait partie du plan."
 ),
 sci=(
  "L'hydraulique rend le récit faisable : en basses eaux (octobre), barrer "
  "l'Euphrate et le dériver vers les marais abaisse le lit intra-muros jusqu'au "
  "gué — Xénophon dit l'eau aux genoux. L'archéologie (Koldewey, 1899-1917 : "
  "palais sud, salle du trône, voie processionnelle, porte d'Ishtar) confirme "
  "le décor palatial. Les briques estampillées et les cylindres de Nabonide "
  "nommant Belschatsar établissent la corégence — expliquant le « troisième » "
  "que les critiques du XIXe siècle jugeaient absurde."
 ),
 limites=(
  "F003 traite la désolation durable : pas de doublon — ici, la nuit. La reine "
  "(reine-mère ? Nitocris d'Hérodote ?) : non identifiée sûrement. Hérodote et "
  "Xénophon écrivent un à deux siècles après : cadre, pas procès-verbal. La "
  "Chronique est lacunaire à l'endroit crucial. « Troisième » par la corégence : "
  "reconstitution (solide). Belschatsar tué (Dn 5:30) : la Chronique mutilée ne "
  "confirme ni n'infirme au complet."
 ),
 tl=[("Is 13-45, Jr 50-51", "Festin, fleuve, portes"), ("556-539", "Nabonide / Belschatsar"),
     ("Oct. 539", "Opis, Sippar"), ("Nuit 11/12 oct.", "Écriture"), ("12 oct. 539", "Gobryas entre")],
 src=[("La chute de Babylone (Dn 5 : festin, écriture, fleuve)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101963013"),
      ("Babylone — Étude et histoire (voir F003)", "https://wol.jw.org/fr/wol/d/r30/lp-f/101972329"),
      ("Daniel 5 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/5"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_E005_babylone.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="E006", titre="Darius le Mède — l'énigme en quatre hypothèses",
 ref="Daniel 5:31 ; Daniel 6 ; Daniel 9:1 ; Daniel 11:1 ; Esdras 1:1-4 ; 2 Chroniques 36:22-23",
 statut="Accomplie (identité débattue — voir Limites)",
 cat="E", syst="Système 539/537",
 reg="Registre : Daniel — P374 (ch. 5, contexte), P376 (6:24), P384 (9:1-19)",
 texte=[
  "« Et Darius le Mède reçut le royaume, étant âgé d'environ soixante-deux "
  "ans. » (Dn 5:31 — « reçut » : il ne prend pas, on lui donne)",
  "« La première année de Darius, fils d'Assuérus, de la race des Mèdes, lequel "
  "était devenu roi du royaume des Chaldéens. » (Dn 9:1 — « devenu » : on l'a fait)",
  "« Darius établit sur le royaume cent vingt satrapes. » (Dn 6:1-2)",
  "« Daniel prospéra sous le règne de Darius et sous le règne de Cyrus le "
  "Perse. » (Dn 6:28 — deux règnes, pas un)",
 ],
 contexte=(
  "La nuit de 539 : Belschatsar tué, un Mède de 62 ans « reçoit » le royaume des "
  "Chaldéens — fils d'un Assuérus, pas « roi de Perse » (le titre de Cyrus), "
  "mais roi « du royaume des Chaldéens » : juridiction chaldéenne, sous un "
  "monarque supérieur. Il nomme 120 satrapes et trois ministres (Daniel premier), "
  "signe l'édit irrévocable de trente jours (6:6-9, « loi des Mèdes et des Perses » "
  "— la même formule qu'en Esther 1:19 ; 8:8), jette Daniel aux lions, puis "
  "proclame « devant le Dieu de Daniel » (6:26-27). Puis Cyrus (6:28 ; Esd 1). "
  "Aucun document profane ne nomme un « Darius » en 539 : l'énigme est réelle."
 ),
 explication=(
  "Le vocabulaire est celui du vice-roi : « reçut » (qabbel, araméen : recevoir) "
  "et « devenu roi » (causatif : « fut fait roi ») — Darius est installé, pas "
  "conquérant. « Du royaume des Chaldéens », jamais « de Perse » : sa juridiction "
  "est l'ex-empire babylonien. Soixante-deux ans et « fils d'Assuérus, race des "
  "Mèdes » : signalement qui exclut (voir les hypothèses). Les 120 satrapes "
  "trouvent un parallèle : la Chronique de Nabonide dit que Gobryas, le preneur "
  "de Babylone, « installa des gouverneurs à Babylone » — gouverneur de "
  "gouverneurs, « probablement salué comme roi par ses subordonnés » (Whitcomb, "
  "cité par les publications). Daniel 6:28 distingue deux règnes successifs : "
  "Darius PUIS Cyrus."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah passe en revue quatre hypothèses. "
  "(1) Cyrus lui-même ? Écartée : Perse par son père Cambyse Ier (le cylindre), "
  "pas « Mède, fils d'Assuérus » — et 6:28 distingue les règnes. (2) Cambyse II ? "
  "Écartée : trop jeune en 539 pour les 62 ans. (3) Cyaxare II, l'oncle de Cyrus "
  "chez Xénophon ? Fragile : Hérodote dit Astyage mort sans fils ; la Cyropédie "
  "est un roman pédagogique. (4) Gobryas (Gubaru), preneur puis gouverneur de "
  "Babylone ? Le meilleur candidat — MAIS non conclusif, les publications le "
  "disent noir sur blanc. Pour : juridiction identique (tout l'ex-empire, "
  "« au-delà du Fleuve » jusqu'à l'Égypte), gouverneurs installés (// 120 "
  "satrapes), vice-royauté (« reçut », « fut fait ») — et Belschatsar non plus "
  "n'est pas « roi » dans les tablettes ! Contre : 14 ans de charge contre un "
  "règne apparemment bref ; nationalité et parenté inconnues (pas de « Mède, "
  "fils d'Assuérus ») ; aucun édit attesté ; la place de Cambyse à Babylone en "
  "538 complique le tableau. Darius régna au moins un an — la 1re année de Cyrus "
  "ne commence qu'en 538 (vers 537)."
 ),
 accomplissement=[
  ("Nuit du 11/12 octobre 539", "Belschatsar tué ; Darius, 62 ans, reçoit le royaume (5:30-31)"),
  ("539-538 av. n. è.", "1re année : 120 satrapes, édit de 30 jours, fosse aux lions (ch. 6)"),
  ("539-538 av. n. è.", "Proclamation « devant le Dieu de Daniel » (6:26-27) ; Daniel prie (9:1)"),
  ("538 av. n. è.", "1re année de Cyrus à Babylone (voir la fiche sur la date pivot)"),
  ("537 av. n. è.", "Le décret : retour (voir B002) — Darius s'efface, Cyrus accomplit"),
 ],
 hist=(
  "La Chronique de Nabonide (BM 35382) : Gobryas entre à Babylone le 16 Tashritu, "
  "« installe des gouverneurs » — le parallèle des 120 satrapes (Whitcomb, "
  "Olmstead, cités par les publications). Le cylindre de Cyrus (généalogie : "
  "Cambyse Ier, Perse) exclut l'identité Cyrus-Darius. Hérodote (Astyage sans "
  "fils) fragilise Cyaxare. Xénophon (Cyropédie : Cyaxare, Gobryas, Gadatas) "
  "fournit un cadre romancé. « Loi des Mèdes et des Perses » (Dn 6 ; Est 1:19 ; "
  "8:8) : le droit irrévocable du même empire. La proclamation de Darius (6:26-27) "
  "préfigure le décret de Cyrus (Esd 1) : deux Mèdes-Perses confessant Jéhovah."
 ),
 geo=(
  "Babylone : le royaume reçu. La juridiction : tout l'ex-empire babylonien — "
  "des tablettes montrent Gobryas régnant sur Babylone ET « au-delà du Fleuve » "
  "(Syrie, Phénicie, Palestine jusqu'à l'Égypte) : tout le Croissant fertile, "
  "exactement « le royaume des Chaldéens » élargi. La fosse aux lions : ménagerie "
  "royale — les rois mésopotamiens entretenaient des lions (reliefs de chasse "
  "d'Assurbanipal à Ninive, VIIe siècle, British Museum : les lions du roi, "
  "attestés)."
 ),
 sci=(
  "Le cunéiforme (Chronique, tablettes économiques datées, cylindre) fournit le "
  "cadre : noms, dates, juridictions. L'onomastique propose « Darius » comme nom "
  "de trône (Darayavahush, « qui tient le bien ») de Gobryas — hypothèse "
  "signalée (les rois antiques portent plusieurs noms : Pulu/Tiglath-Piléser, "
  "Xerxès/Assuérus). La zoologie (lion asiatique, Panthera leo persica, alors "
  "présent en Mésopotamie — reliefs de Ninive) rend la fosse vraisemblable. "
  "L'extinction locale postérieure n'efface pas les reliefs."
 ),
 limites=(
  "L'identification (Gobryas) est NON conclusive : les publications le disent, "
  "cette fiche le répète — une fiche qui tranche serait malhonnête. Un ou deux "
  "Gobryas dans la Chronique (preneur ? gouverneur 14 ans ? mort ?) : débattu. "
  "Assuérus : titre ou nom ? (homonymes en Esther et Esdras 4:6) — non tranché. "
  "Cambyse associé à Babylone en 538 (tablettes) : coexistence à expliquer. "
  "La fosse (ménagerie ?) : reconstitution. Le règne bref (539-538) appartient "
  "au système 539/537."
 ),
 tl=[("Nuit oct. 539", "Reçoit, 62 ans"), ("539-538", "120 satrapes, fosse"), ("539-538", "Proclamation"),
     ("538", "Cyrus 1re année"), ("537", "Décret, retour")],
 src=[("Qui était Darius le Mède ? (4 hypothèses, non conclusif)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1972407"),
      ("Darius — Étude perspicace (le Mède, Gubaru)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200011096"),
      ("Une date pivot de l'Histoire (Darius 1 an, Cyrus 538)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965684"),
      ("Daniel 6 — Bible d'étude, notes (satrapes, fosse)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/27/6")],
 img="images/prophe_E006_darius.jpg",
))
