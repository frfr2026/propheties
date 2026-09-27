#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE T — JEREMIE, 1re PARTIE : LE JUGEMENT (vague 18)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="T",
    nom="Jérémie, 1re partie — le jugement",
    vague="18",
    intro=(
        "Dix-huitième vague : Jérémie, première partie — le jugement annoncé et tombé. "
        "T001 : le malheur vient du nord — marmite, lion, feux-signaux, paille au vent. "
        "T002 : le Temple ne sauvera pas — Silo, Topheth, ossements, chacals, sabbat, "
        "palais en feu. T003 : quatre rois jugés — Shallum, Yehoïaqim, Konia sans "
        "postérité régnante, les deux paniers de figues. T004 : Tsidqiya et la chute — "
        "sortez et vivez, Lakish et Azéqa, Ribla, les yeux crevés. T005 : faux "
        "prophètes contre Jérémie — Pashhour, Ouriya, Hanania et son joug brisé. T006 : "
        "signes en actes — ceinture, célibat, potier, cruche, joug, champ, Rékabites, "
        "rouleau brûlé. Mêmes dix blocs, mêmes règles."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T001", titre="Le malheur vient du nord — marmite, lion, feux-signaux",
 ref="Jérémie 1:13-16 ; 4:5-8 ; 5:14-17 ; 6:1-5 ; 6:22-26 ; 13:24-27 ; 25:27-38",
 statut="Accomplie (P181, P185, P186, P187, P188, P200, P224)",
 cat="T", syst="Système invasions (647 → 607)",
 reg="Registre : Jérémie — P181 (1:13-16 : marmite du nord), P185 (4:5-8 : lion, cor), P186 (5:14-17 : nation lointaine), P187 (6:1-5 : feux-signaux), P188 (6:22-26 : peuple du nord), P200 (13:24-27 : paille au vent), P224 (25:27-38 : bergers hurlent) ; rappels P221/P222 (Jr 25:1-14 : voir B), P384 (Dn 9 : voir E/F)",
 texte=[
  "« Une MARMITE QUI BOUT, face tournée vers le NORD. » (1:13 — P181 : la marmite !)",
  "« C'est du NORD que le malheur se DÉCHAÎNERA. » (1:14 — P181 : le nord !)",
  "« Le LION est monté de son fourré, le DESTRUCTEUR des nations. » (4:7 — P185 : le lion !)",
  "« SONNEZ du cor… ÉLEVEZ l'étendard vers Sion ! » (4:5-6 — P185 : l'alerte !)",
  "« Une NATION LOINTAINE… dont tu ne connais pas la LANGUE. » (5:15 — P186 : la langue !)",
  "« SONNEZ à Thekoa, élevez un SIGNAL sur Béth-Hakkérem ! » (6:1 — P187 : les feux !)",
  "« Un PEUPLE vient du NORD… des EXTRÉMITÉS de la terre. » (6:22 — P188 : les extrémités !)",
  "« Dispersés comme la PAILLE livrée au vent du désert. » (13:24 — P200 : la paille !)",
  "« Malheur de NATION en NATION… une GRANDE TEMPÊTE se lève. » (25:32 — P224 : la tempête !)",
 ],
 contexte=(
  "Jérémie, fils du prêtre Hilqia, d'Anathoth — ville de prêtres à moins de 5 km au "
  "nord-nord-est du mont du Temple (voir it-1 « Jérémie », 1200002421). Appelé jeune "
  "homme, en 647, la treizième année de Yoshiya (voir 1200002421 ; chronologie 647, "
  "voir 102012208) : « Avant que je ne te forme dans le ventre, je te connaissais » "
  "(1:5 — C8 : aucun P, vérifié) ; « ne dis pas : je suis jeune » (1:7 — C8 : aucun "
  "P, vérifié) ; mission : « arracher et planter » (1:10 — C8 : aucun P, vérifié). "
  "Plus de quarante ans de service (voir 1200002421), sous cinq rois, jusqu'à la chute. "
  "Le cadre : l'Assyrie tombe (Ninive renversée, 632 — voir 102012208), Babylone monte "
  "(Neboukadnetsar, 625 — voir 102012208), Juda pris entre l'Égypte et le nouveau "
  "maître. Jérémie nomme le maître : « mon SERVITEUR Neboukadnetsar » (25:9 — rappel "
  "P221, voir B) — l'envahisseur comme instrument."
 ),
 explication=(
  "La marmite (1:13 — P181) : le chaudron qui bout, penché — son contenu va se "
  "déverser vers le sud : l'invasion comme débordement. Le nord (1:14 — P181) : la "
  "direction d'arrivée — les armées ne traversent pas le désert, elles descendent "
  "le Croissant fertile puis longent la côte : « du nord » est la route, pas "
  "l'ethnie. Le lion (4:7 — P185) : « destructeur des nations » — le fauve sorti du "
  "fourré, la machine babylonienne en chasse. Le cor et l'étendard (4:5-6 — P185) : "
  "l'alerte — sonner, signaler, fuir vers Sion : la défense civile du VIIe siècle. "
  "La langue inconnue (5:15 — P186) : l'akkadien — sémitique comme l'hébreu, mais "
  "incompréhensible : l'ennemi qu'on ne comprend pas. Les feux-signaux (6:1 — "
  "P187) : Thekoa (la patrie d'Amos), Béth-Hakkérem (la hauteur) — la chaîne "
  "optique des collines, confirmée par les lettres de Lakish (voir T004 : Jr 34:7). "
  "Les bergers et leurs troupeaux (6:3 — P187) : les chefs et leurs armées autour "
  "de la ville-pâturage. La paille (13:24 — P200) : le vannage — le grain reste, "
  "la paille vole : la dispersion comme tri. La tempête (25:32 — P224) : « de "
  "nation en nation » — le malheur en système, pas en accident."
 ),
 interpretation=(
  "Le siège (2R 25:1-4 — P188) : la neuvième année de Tsidqiya, les armées du nord "
  "campent contre Jérusalem — la marmite se déverse. La première déportation (2R "
  "24:10-16 — P186) : 617 — « la nation lointaine » mange « les récoltes et les "
  "villes fortes » — voir T003. La prise (Jr 39:1-9 — P181 ; Jr 52:12-14 — P185) : "
  "brèche, fuite, incendie — voir T004. Les deux dernières (Jr 34:7 — P187 ; P255, "
  "voir T004) : Lakish et Azéqa — les feux-signaux de 6:1 s'éteignent un à un, "
  "Azéqa d'abord (lettre IV de Lakish — voir T004). Les soixante-dix ans (rappels "
  "P221/P222, voir B) : la servitude chiffrée — 25:9-11. Daniel lit Jérémie (rappel "
  "P384, voir E/F : Dn 9:1-19 — « les soixante-dix ans reconnus dans la prière ») : "
  "le prophète de l'exil relit le prophète du siège — la boucle des 70 ans. Les "
  "bergers hurlent (25:34-38 — P224) : « hurlez, bergers ! » — les pâturages "
  "paisibles ravagés (Jr 49 — cités ailleurs, non versés ici)."
 ),
 hist=(
  "Ninive tombe (632 — voir 102012208) : l'Assyrie s'efface, Babylone hérite — le "
  "nord change de maître, pas de direction. Neboukadnetsar (625-582 — voir "
  "102012208) : le « serviteur » malgré lui — voir B (rappel P221). L'akkadien "
  "(5:15 — P186) : langue de l'administration et des chroniques babyloniennes — "
  "cunéiforme, incompréhensible au Judéen moyen (repère linguistique, sans lien). "
  "Thekoa : la patrie d'Amos — le berger devenu prophète du nord (sans verset "
  "d'Amos versé — registre à venir). Karkemish et la Chronique babylonienne : NON "
  "versés (vague suivante — voir les limites). La coupe des nations (25:15-26 — "
  "rappel : cité en transition C, non versé ici — seul 25:27-38 est versé, P224)."
 ),
 geo=(
  "Le nord : l'Euphrate, Qarqar excepté (sujet à caution — non versé), la Bekaa, "
  "la côte — la route des invasions depuis toujours. Thekoa (6:1 — P187) : les "
  "collines au sud de Bethléhem — le cor d'alarme. Béth-Hakkérem (6:1 — P187) : "
  "la hauteur du signal — site discuté (Ramat-Rahel ? — non tranché, voir les "
  "limites). Lakish et Azéqa (voir T004) : le sud-ouest fortifié — les feux qui "
  "s'éteignent. Les extrémités de la terre (6:22 — P188) : l'empire lointain — "
  "Mésopotamie vue de Juda. Le Négev fermé (13:19 — P199, voir T003) : le sud "
  "bouclé — plus d'issue."
 ),
 sci=(
  "Métallurgie (1:13) : le chaudron — bronze ou cuivre martelé, posé sur le feu : "
  "la marmite qui bout comme modèle de pression. Acoustique (4:5 ; 6:1) : le cor "
  "(shofar) — l'alarme sonore, longue portée en terrain vallonné ; l'étendard — "
  "l'alarme visuelle. Optique (6:1 — P187) : les feux-signaux — chaîne de collines, "
  "relais de flammes, nuit : le télégraphe antique (confirmé à Lakish — voir "
  "T004). Linguistique (5:15) : akkadien contre hébreu — deux sémitiques "
  "mutuellement opaques à l'oreille. Météorologie (13:24 ; 25:32) : le vent du "
  "désert (hamsin) qui emporte la paille ; la tempête « de nation en nation » — "
  "le front qui balaie. Agronomie (13:24) : le vannage — fourche, vent, tri : la "
  "dispersion en technique agricole."
 ),
 limites=(
  "Marmite (1:13) : traduction hedged (« marmite qui bout » — voir nwtsty 24/1). "
  "Béth-Hakkérem : site discuté — non tranché. Qarqar : sujet à caution — non "
  "versé. Karkemish, Chronique babylonienne, Égypte de Néko : vague suivante — non "
  "versés (aucun P nommé). Soixante-dix ans : voir B (rappels P221/P222) — non "
  "re-traités. Daniel 9 : voir E/F (rappel P384) — non re-traité. Jr 25:15-26 "
  "(coupe) : cité en transition C — seul 25:27-38 (P224) est versé ici. C8 : Jr "
  "1:5 (connu avant formation), 1:7 (je suis jeune), 1:10 (arracher-planter) — "
  "aucun P (vérifiés : P181-P182 seuls sur Jr 1)."
 ),
 accomplissement=[("Marmite du nord", "Malheur déchaîné (1:13-16 — P181)"),
     ("Lion monté", "Cor, étendard, invasion (4:5-8 — P185)"),
     ("Nation lointaine", "Langue inconnue, villes mangées (5:14-17 — P186)"),
     ("Feux-signaux", "Thekoa, Lakish, Azéqa (6:1-5 — P187 ; voir T004)"),
     ("Peuple du nord", "Siège an 9 (6:22-26 — P188 ; 2R 25)"),
     ("Paille et tempête", "Vannés, balayés (13:24-27 — P200 ; 25:27-38 — P224)")],
 tl=[("647 (appel)", "Jeune homme à Anathoth (voir 1200002421)"),
     ("632 (Ninive)", "Le nord change de maître (voir 102012208)"),
     ("625 (Neboukadnetsar)", "« Mon serviteur » (rappel P221, B)"),
     ("617 (1re déportation)", "Nation lointaine (P186 ; voir T003)"),
     ("An 9 de Tsidqiya", "Siège — marmite versée (P188 ; voir T004)"),
     ("607 (chute)", "Tempête accomplie (P224 ; voir T004)")],
 src=[("Jérémie — it-1 (Anathoth, appel 647, 40 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002421"),
      ("Jérémie — si n° 24 (plan du livre, thèmes)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990085"),
      ("Prophéties véridiques (chrono 647-537, 70 ans)", "https://wol.jw.org/fr/wol/d/r30/lp-f/102012208"),
      ("Jérémie 1 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/1")],
 img="images/prophe_T001_nord.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T002", titre="Le Temple ne sauvera pas — Silo, Topheth, chacals",
 ref="Jérémie 7:1-15 ; 7:30-34 ; 8:1-3 ; 9:11 ; 17:19-27 ; 21:11-14 ; 22:1-9 ; 26:1-6",
 statut="Accomplie (P189, P190, P191, P192, P207, P212, P213, P225)",
 cat="T", syst="Système Temple (Silo → 607)",
 reg="Registre : Jérémie — P189 (7:1-15 : Silo), P190 (7:30-34 : Topheth), P191 (8:1-3 : ossements), P192 (9:11 : chacals), P207 (17:19-27 : sabbat, portes), P212 (21:11-14 : forêt brûlée), P213 (22:1-9 : maison en ruine), P225 (26:1-6 : procès du Temple) ; rappel K008 (sabbats de la terre) ; cross T005 (procès), T006 (cruche-Hinnom), T003 (cèdre)",
 texte=[
  "« TEMPLE de Jéhovah, TEMPLE de Jéhovah, TEMPLE de Jéhovah ! » (7:4 — P189 : le slogan !)",
  "« Allez à SILO… je ferai à cette maison COMME À SILO. » (7:12-14 — P189 : le précédent !)",
  "« Les hauts lieux de TOPHETH… chose qui ne m'était pas MONTÉE AU CŒUR. » (7:31 — P190 : l'horreur !)",
  "« VALLÉE DU CARNAGE… les voix de joie CESSERONT. » (7:32-34 — P190 : le silence !)",
  "« Les OSSEMENTS… ÉTALÉS devant le soleil et la lune. » (8:1-2 — P191 : les os !)",
  "« Un TAS DE RUINES, un REPAIRE DE CHACALS. » (9:11 — P192 : les chacals !)",
  "« Un FEU aux PORTES de Jérusalem. » (17:27 — P207 : les portes !)",
  "« Cette MAISON deviendra une RUINE. » (22:5 — P213 ; 26:6 — P225 : la ruine !)",
 ],
 contexte=(
  "Le discours de la porte (7:2 — P189 ; 26:2 — P225) : Jérémie prêche À l'entrée du "
  "Temple — le lieu même qu'il condamne. Le slogan (7:4 — P189) : « temple de "
  "Jéhovah » répété trois fois — le bâtiment comme amulette. Le précédent (7:12-14 — "
  "P189) : Silo — là où Dieu « avait fait résider son nom », l'arche prise, les "
  "fils d'Éli morts (1S 4 — C8 : aucun P sur 1S 4, vérifié). Le procès (26:1-11 — "
  "P225 ; détails voir T005) : « tu mourras » — Jérémie arrêté pour avoir dit que "
  "la maison deviendrait « comme Silo » (26:6-9 — P189, P225). Topheth (7:30-34 — "
  "P190) : les hauts lieux dans la vallée de Hinnom — enfants brûlés (voir 1986728, "
  "2011252) ; Josias avait souillé le lieu (2R 23:10 — C8 : aucun P, vérifié) — "
  "en vain, la pratique a repris. Le sabbat (17:19-27 — P207) : les fardeaux aux "
  "portes le jour du repos — le test. Le palais (21:11-14 — P212 ; 22:1-9 — P213) : "
  "la « maison du roi », lambrissée de cèdre (22:14 — P215, voir T003) — condamnée "
  "avec le Temple."
 ),
 explication=(
  "« Paroles mensongères » (7:8 — P189) : le slogan-temple est un mensonge — Dieu "
  "n'est pas otage de sa maison. Silo (7:12-14) : l'argument massue — Dieu a DÉJÀ "
  "abandonné un lieu saint : le précédent tue l'amulette. Topheth (7:31 — P190) : "
  "rattaché à « tambour » (explication courante — voir les limites) ; « pas montée "
  "au cœur » : Dieu DÉSAVOUE — il n'a pas ordonné, il n'a même pas imaginé (voir "
  "2011252 : l'argument contre les tourments — Dieu ne fait pas ce qui lui répugne ; "
  "voir aussi 1101989234). « Vallée du carnage » (7:32 — P190) : le lieu des "
  "sacrifices devient le charnier du jugement — Topheth engorge (« plus de place », "
  "19:11 — P209, voir T006). Ossements étalés (8:1-2 — P191) : rois, princes, "
  "prêtres, prophètes — exhumés et exposés « devant l'armée des cieux » qu'ils "
  "adoraient : les astres-idoles contemplent leurs adorateurs en os. Chacals (9:11 — "
  "P192 ; « renards », Lm 5:18 — P192) : la faune des ruines — Jérusalem rendue aux "
  "bêtes. Sabbat (17:21-22 — P207) : « ne portez pas de fardeau » — le repos "
  "profané ; « sinon, feu aux portes » (17:27). Forêt (21:14 — P212) : le palais de "
  "cèdre comme « forêt » — le feu commence par les portes, finit par la forêt."
 ),
 interpretation=(
  "L'arrestation (Jr 26:6-9 — P189) : prêtres, prophètes, peuple saisissent Jérémie "
  "— « tu mourras » — voir T005 (procès). L'incendie (2Ch 36:17-20 — P189 ; 2Ch "
  "36:19 — P207 ; Jr 39:8 — P207, P213 ; 2R 25:9 — P212, P213) : maison de Dieu "
  "brûlée, murailles démolies, palais consumé — 607. Les sabbats rendus (2Ch 36:21 — "
  "P190 ; Jr 25:11 — P190, rappel P221/B) : la terre « jouit de ses sabbats » — "
  "voir K008 (sabbats de la terre). Ribla (Jr 39:6 ; 52:10, 24-27 — P191) : les fils "
  "de Tsidqiya égorgés, les chefs exécutés — les ossements des grands, d'abord "
  "les corps (voir T004). Les ruines vues (Né 2:3, 13-17 — P192) : Néhémie inspecte "
  "de nuit — « comment ne pas pleurer, la ville en ruine ? » ; « les renards s'y "
  "promènent » (Lm 5:18 — P192). La maison-ruine (22:5 — P213 ; 26:6 — P225) : "
  "« dévastée » — le serment accompli (« j'ai juré par moi-même », 22:5)."
 ),
 hist=(
  "Silo (1S 4 — C8) : Éli, Hophni et Pinhéas, l'arche prise par les Philistins — "
  "le lieu saint abandonné une première fois : résumé seul, voir les limites. "
  "Tophet de Carthage (voir 1986728) : 6 000 m², neuf niveaux, jusqu'à 20 000 "
  "urnes (400-200) — la pratique phénicienne à l'échelle industrielle ; « Manassé "
  "entraînait Juda à agir plus mal que les nations » (voir 1986728) ; « sang des "
  "innocents » (Jr 19:4 — P209, voir T006). Achaz et Manassé : voir 2011252 (versets "
  "non cités ici — voir les limites). La décharge (voir 2011252 : exégète Kimhi) : "
  "la vallée devenue incinérateur — feux au soufre, ordures, cadavres d'animaux, "
  "corps de criminels (voir 1101989234) — la géhenne-symbole : destruction totale, "
  "pas tourment. Ribla (P191 — voir T004) : le QG de Neboukadnetsar sur l'Oronte — "
  "tribunal et exécutions."
 ),
 geo=(
  "La porte du Temple (7:2 — P189) : la chaire de Jérémie — prêcher la ruine sur "
  "le seuil du monument. Silo (7:12 — P189) : Éphraïm, au nord — les ruines "
  "avertissent la capitale. Topheth-Hinnom (7:31-32 — P190) : au sud de Jérusalem — "
  "la vallée des sacrifices, puis le charnier, puis la décharge (voir 2011252). "
  "Les portes (17:19-27 — P207) : battants de bois, gonds — le feu les prend "
  "d'abord. La forêt (21:14 — P212) : le palais-cèdre — voir T003 (22:14). Ribla "
  "(P191 — voir T004) : la Syrie — les grands y meurent. Les ruines (Né 2 — P192) : "
  "portes consumées, murailles brèches — l'inspection nocturne."
 ),
 sci=(
  "Funéraire (8:1-2 — P191) : l'exhumation-profanation — les tombes royales et "
  "sacerdotales violées, les os « au soleil » : le déshonneur posthume maximal. "
  "Zoologie (9:11 — P192) : chacals (et renards, Lm 5:18) — la recolonisation des "
  "ruines : prédateurs opportunistes, terriers dans les décombres. Pyrotechnique "
  "(17:27 ; 21:14) : portes de bois + palais de cèdre — le feu de siège : braises, "
  "tirage, embrasement. Acoustique-démographie (7:34 — P190) : « voix de l'époux, "
  "voix de l'épouse » — le silence des noces : indicateur de dépopulation (voir "
  "T006-vague suivante : les voix reviendront). Hygiène publique (voir 2011252, "
  "1101989234) : incinérateur au soufre — destruction complète, cendres : la "
  "géhenne comme traitement des déchets — et comme symbole."
 ),
 limites=(
  "Topheth-« tambour » : explication courante (toph), non tranchée — voir nwtsty "
  "24/7. Silo (1S 4) : résumé seul — C8 (P sur 1S 2-3 : versets disjoints, non "
  "nommés). Achaz/Manassé : versets non cités (un P couvre 2Ch 28:9-11, verset "
  "disjoint, non nommé) — voir 2011252. Procès de Jérémie : voir T005 (P226, C8 "
  "26:24). Jr 19 (Topheth, cruche) : voir T006 (P209). Cèdre du palais (22:14) : "
  "voir T003 (P215). Sabbats (2Ch 36:21) : voir K008. C8 : 1S 4 (arche prise), 2R "
  "23:10 (Josias souille Topheth) — aucun P (vérifiés)."
 ),
 accomplissement=[("Slogan brisé", "Temple-amulette dénoncé (7:1-15 — P189)"),
     ("Comme Silo", "Précédent appliqué (7:12-14 — P189 ; 26:6 — P225)"),
     ("Topheth-charnier", "Vallée du carnage (7:30-34 — P190)"),
     ("Os au soleil", "Grands exhumés (8:1-3 — P191 ; Ribla)"),
     ("Chacals", "Ruines habitées par les bêtes (9:11 — P192)"),
     ("Feu aux portes", "Sabbat profané, palais brûlé (P207, P212, P213)")],
 tl=[("Silo (repère)", "Lieu abandonné (1S 4 — C8)"),
     ("Discours (609-608 ?)", "Porte du Temple (7 ; 26 — P189, P225)"),
     ("Procès", "« Tu mourras » (26 — P225 ; voir T005)"),
     ("Siège (an 9-11)", "Portes, palais menacés (P207, P212)"),
     ("607 (chute)", "Incendie total (2Ch 36 ; 2R 25 — P189-P213)"),
     ("Néhémie (après)", "Ruines inspectées (Né 2 — P192)")],
 src=[("Jérémie — si n° 24 (discours du Temple, ch. 7 et 26)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990085"),
      ("Sacrifices d'enfants (Jr 7:31, Tophet de Carthage)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1986728"),
      ("La géhenne (Hinnom, Kimhi, Jr 7:30-33 ; 19:6-7)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2011252"),
      ("Enfer — it (géhenne, soufre, Jr 7:31)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101989234"),
      ("Jérémie 7 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/7")],
 img="images/prophe_T002_temple.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T003", titre="Quatre rois jugés — Shallum, Yehoïaqim, Konia, les figuiers",
 ref="Jérémie 13:18-19 ; 22:10-12 ; 22:13-19 ; 22:20-23 ; 22:24-30 ; 24:1-10",
 statut="Accomplie (P199, P214, P215, P216, P217, P220)",
 cat="T", syst="Système quatre rois (609 → 617)",
 reg="Registre : Jérémie — P199 (13:18-19 : roi et reine mère), P214 (22:10-12 : Shallum), P215 (22:13-19 : Yehoïaqim), P216 (22:20-23 : bergers emportés), P217 (22:24-30 : Konia), P220 (24:1-10 : figuiers) ; cross T004 (Tsidqiya), T006 (rouleau 36:30)",
 texte=[
  "« Dites au ROI et à la REINE MÈRE : abaissez-vous, ASSEYEZ-VOUS. » (13:18 — P199 : l'abaissement !)",
  "« Ne pleurez pas le MORT, pleurez CELUI QUI S'EN VA. » (22:10 — P214 : les pleurs !)",
  "« Malheur à qui bâtit sa maison SANS JUSTICE. » (22:13 — P215 : le malheur !)",
  "« LAMBRISSÉE de cèdre, PEINTE en vermillon. » (22:14 — P215 : le luxe !)",
  "« La SÉPULTURE D'UN ÂNE : traîné, jeté HORS des portes. » (22:19 — P215 : l'âne !)",
  "« ANNEAU à ma main droite, je T'ARRACHERAIS. » (22:24 — P217 : l'anneau !)",
  "« INSCRIVEZ cet homme COMME SANS ENFANT. » (22:30 — P217 : sans enfant !)",
  "« Les BONS figuiers… les MAUVAIS, pour le mal. » (24:5, 8 — P220 : les paniers !)",
 ],
 contexte=(
  "Après Josias tué à Meguiddo, quatre rois en vingt ans. Shallum-Yehoahaz (22:10-12 "
  "— P214) : trois mois, déposé par Néko, emmené en Égypte (2R 23:31-34 — P214). "
  "Yehoïaqim-Éliakim (22:13-19 — P215) : placé par Néko, vassal de Babylone trois ans "
  "puis rebelle (2R 24:1 — P215, P227), mort pendant le siège (voir 1102010141 ; voir "
  "it-1 Yehoïakîn, 1200002375 : rébellion en 618, siège). Yehoïakîn-Konia (22:24-30 — "
  "P217) : fils de Yehoïaqim et de Nehoushta (voir 1200002421 ? non — voir 1200002375), "
  "18 ans, trois mois et dix jours, reddition en 617 (voir 1200002375 ; 102012208). "
  "La reine mère (13:18 — P199 ; Nehoushta, voir 1200002375) : abaissée avec son fils "
  "(2R 24:8-16 — P199). Puis Tsidqiya — voir T004. Et les deux paniers (24:1-10 — "
  "P220) : après 617, devant le Temple — les exilés « pour le bien », Tsidqiya et "
  "son reste « pour le mal »."
 ),
 explication=(
  "Shallum (22:11 — P214) : le nom propre de Yehoahaz — « fils de Josias » : pleurez "
  "le vivant exilé, pas le mort pleuré. Cent talents (2R 23:33 — P214) : l'amende de "
  "Néko — cent talents d'argent, un d'or : le prix du trône. Maison sans justice "
  "(22:13 — P215) : Yehoïaqim bâtit — corvées impayées (« son prochain le sert pour "
  "rien », 22:13) : le luxe sur le dos du peuple. Cèdre et vermillon (22:14 — P215) : "
  "le lambris royal — « ton père mangeait et buvait, MAIS pratiquait le droit » "
  "(22:15 — P215) : Josias festoyait ET jugeait. Sépulture d'âne (22:19 — P215) : "
  "pas de tombeau — traîné, jeté : le roi-immondice ; « pas de descendant sur le "
  "trône » et « cadavre exposé » (Jr 36:30 — P215, et P258 : voir T006 ! — la "
  "sentence est DANS le rouleau brûlé). Anneau arraché (22:24 — P217) : le sceau "
  "royal — Dieu retire sa signature. « Comme sans enfant » (22:30 — P217) : Konia "
  "aura SEPT fils (1Ch 3:16-18 — C8 : aucun P, vérifié ; Schéaltiel, Pédaïah — voir "
  "1984450) — mais aucun ne régnera à Jérusalem : « comme » sans enfant, sans "
  "SUCCESSION. Figuiers (24:2-3 — P220) : deux paniers — les précoces excellents, "
  "les mauvais immangeables : 617 trie."
 ),
 interpretation=(
  "Ribla (2R 23:31-34 — P214) : Néko dépose Yehoahaz à Ribla, l'emmène en Égypte — "
  "« il ne reverra pas ce pays » (22:11-12 — P214). Le siège mortel (2R 24:1-6 — "
  "P215) : vassal, rebelle, assiégé — Yehoïaqim meurt pendant le siège (voir "
  "1102010141, 1200002375) — et la sépulture d'âne (22:19). Le rouleau vengeur (Jr "
  "36:30 — P215 ; P258, voir T006) : Yehoïaqim brûle le rouleau qui le condamne — "
  "le rouleau réécrit le condamne encore (36:32 — P258). La reddition (2R 24:8-16 — "
  "P199 ; 2R 24:12-16 — P216) : roi, reine mère, chefs, artisans — « les bergers "
  "emportés » (22:20-23 — P216). Les rations (voir 1200002375) : des tablettes "
  "babyloniennes listent les rations de « Yehoïakîn et cinq de ses fils » — le roi "
  "déchu nourri par l'intendance ennemie. Le sceau (voir 1200012325) : « Éliakim, "
  "intendant de YWKN » — Yehoïakîn a encore un intendant ! La généalogie (Mt 1:11-12 "
  "— C8 : aucun P, vérifié) : Jéconias dans la lignée de Jésus — paradoxe résolu "
  "(voir 1984450) : le décret ferme le trône TERRESTRE, pas la lignée — Joseph "
  "transmet le droit légal, Jésus hérite le trône céleste. Évil-Merodak (2R 25:27-30 "
  "— P217 ; Jr 52:31-34 — C8 : aucun P, vérifié ; 580, voir 1102010141) : Yehoïakîn "
  "relevé, à la table du roi — vivant, nourri, jamais régnant. Les paniers (24:5-10 "
  "— P220) : les exilés de 617 « pour leur bien » (24:5-7), Tsidqiya « pour le mal » "
  "(24:8-10 — voir T004)."
 ),
 hist=(
  "Néko II (2R 23 — P214) : le pharaon de Meguiddo — dépose, impose, emmène : "
  "l'Égypte tuteur éphémère. Vassalité (2R 24:1 — P215) : trois ans de sujétion, "
  "puis révolte en 618 (voir 1200002375) — le calcul perdant. Le siège de 617 "
  "(commencé sous Yehoïaqim — voir 1200012325, sans verset de Daniel cité ici) : "
  "père mort, fils rendu — trois mois et dix jours de règne (voir 1200002375). "
  "Tablettes des rations (voir 1200002375) : l'administration babylonienne — "
  "Yehoïakîn pensionnaire. Sceau YWKN (voir 1200012325) : l'intendant Éliakim — "
  "une cour fantôme en exil. Évil-Merodak (580 — voir 1102010141) : la grâce — "
  "trône au-dessus des rois captifs (2R 25:28 — P217). Zorobabel (Mt 1:12 — C8, "
  "même famille) : petit-fils de Konia, gouverneur — pas roi (voir 1984450 : la "
  "lignée continue, le trône attend)."
 ),
 geo=(
  "Ribla (2R 23:33 — P214 ; 52:9 — voir T004) : deux fois le tribunal — Néko, puis "
  "Neboukadnetsar : la Syrie comme antichambre. L'Égypte (22:11-12 — P214) : "
  "Yehoahaz y meurt — le pays-refuge devenu tombe. Hors des portes (22:19 — P215) : "
  "le cadavre du roi aux immondices — hors les murs. Babylone (22:26-28 — P217) : "
  "« jetés dans un pays qu'ils ne connaissaient pas » — l'exil. Le Temple (24:1 — "
  "P220) : les deux paniers « devant le temple » — le tri exposé au lieu saint. "
  "Le Négev fermé (13:19 — P199) : le sud bouclé — Juda exilé, les villes du Négev "
  "closes."
 ),
 sci=(
  "Botanique (24:2-3 — P220) : les figues précoces (bikkourah) — excellentes — "
  "contre les tardives gâtées : le calendrier des figues dit le tri de 617. "
  "Sigillographie (22:24 — P217) : l'anneau-sceau — signer, sceller, régner : "
  "arracher l'anneau, c'est révoquer ; le sceau YWKN (voir 1200012325) : "
  "l'épigraphie confirme l'intendance. Métrologie (2R 23:33 — P214) : cent talents "
  "d'argent — de l'ordre de trois tonnes et demie (calcul hedged) : l'amende "
  "pharaonique. Démographie paradoxale (22:30 — P217) : sept fils (1Ch 3 — C8) et "
  "« sans enfant » — la descendance biologique contre la succession royale : deux "
  "comptes, deux verdicts. Diététique captive (voir 1200002375) : les rations — le "
  "roi à la gamelle babylonienne."
 ),
 limites=(
  "Josias à Meguiddo : SANS date versée (non tranchée ici). Onze ans de Yehoïaqim : "
  "non versé (verset non vérifié — voir les limites). Daniel 1:1-2 : non cité "
  "(voir 1200012325). Talents : calcul hedged (« de l'ordre de »). Konia : le "
  "paradoxe généalogique est résolu par 1984450 (trône terrestre fermé, lignée "
  "ouverte) — pas de spéculation ajoutée. Tsidqiya et les « mauvais figuiers » : "
  "voir T004. Jr 36:30 : voir T006 (P258). C8 : 1Ch 3:16-18 (sept fils), Mt 1:11-12 "
  "(Jéconias), Jr 52:31-34 (Évil-Merodak) — aucun P (vérifiés)."
 ),
 accomplissement=[("Roi abaissé", "Reine mère déportée (13:18-19 — P199 ; 2R 24)"),
     ("Shallum", "Égypte, jamais revu (22:10-12 — P214)"),
     ("Yehoïaqim", "Sépulture d'âne (22:13-19 — P215 ; Jr 36:30)"),
     ("Bergers emportés", "617 déportés (22:20-23 — P216)"),
     ("Konia", "Sans succession, lignée ouverte (22:24-30 — P217)"),
     ("Figuiers triés", "Exilés bien, reste mal (24:1-10 — P220)")],
 tl=[("Meguiddo (repère)", "Josias tué — quatre rois suivent"),
     ("609 ? (Yehoahaz)", "Trois mois, Égypte (P214)"),
     ("618 (révolte)", "Yehoïaqim rompt (voir 1200002375)"),
     ("617 (reddition)", "Konia 3 mois 10 jours (P199, P216, P217, P220)"),
     ("Exil (rations)", "Yehoïakîn pensionné (voir 1200002375)"),
     ("580 (grâce)", "Évil-Merodak relève (P217 ; C8 Jr 52)")],
 src=[("Yehoïakîn — it-1 (18 ans, 617, rations, 7 fils)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002375"),
      ("Konia et Jésus (Questions : Jr 22:30, droit légal)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1984450"),
      ("Jérémie — si n° 24 (Konia 22:24-27, plan)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990085"),
      ("Jérémie 22 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/22")],
 img="images/prophe_T003_rois.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T004", titre="Tsidqiya et la chute — sortez, Lakish, Ribla",
 ref="Jérémie 21:1-10 ; 32:1-5 ; 34:1-7 ; 34:8-22 ; 37:6-10 ; 37:17-21 ; 38:1-4 ; 38:14-23 ; 52:7-11 ; 52:12-27",
 statut="Accomplie (P211, P246, P255, P256, P259, P260, P261, P262, P295, P296)",
 cat="T", syst="Système siège (an 9 → an 11 de Tsidqiya)",
 reg="Registre : Jérémie — P211 (21:1-10 : sortez, vie sauve), P246 (32:1-5 : yeux contre yeux), P255 (34:1-7 : mourra en paix, Lakish), P256 (34:8-22 : esclaves, veau), P259 (37:6-10 : Égypte repartira), P260 (37:17-21 : pain épuisé), P261 (38:1-4 : sortez), P262 (38:14-23 : ville prise), P295 (52:7-11 : fuite, yeux), P296 (52:12-27 : incendie, déportations) ; cross T006 (Néria, Yaazania, Cour de la Garde), T002 (2R 25:8-10), T005 (citerne) ; voir B (70 ans)",
 texte=[
  "« Qui SORTIRA vers les Chaldéens aura la VIE SAUVE pour butin. » (21:9 — P211 ; 38:2 — P261 : sortez !)",
  "« Ses YEUX verront les YEUX du roi de Babylone. » (32:4 — P246 : les yeux !)",
  "« Tu ne mourras pas par l'ÉPÉE… tu mourras en PAIX. » (34:4-5 — P255 : en paix !)",
  "« LAKISH et AZÉQA — les villes fortifiées qui RESTAIENT. » (34:7 — P255 : les dernières !)",
  "« Le VEAU qu'ils ont COUPÉ EN DEUX. » (34:18 — P256 : le veau !)",
  "« L'Égypte RETOURNERA… les Chaldéens REVIENDRONT et BRÛLERONT. » (37:7-8 — P259 : le retour !)",
  "« Du PAIN jusqu'à ce qu'il n'y en ait PLUS. » (37:21 — P260 : le pain !)",
  "« La ville sera PRISE… femmes et fils LIVRÉS. » (38:22-23 — P262 : la prise !)",
  "« Il CREVA les yeux… LIENS DE BRONZE. » (52:11 — P295 : les yeux crevés !)",
  "« Trois DÉPORTATIONS chiffrées : 3023, 832, 745. » (52:28-30 — P296 : les chiffres !)",
 ],
 contexte=(
  "Tsidqiya, oncle de Yehoïakîn, placé par Neboukadnetsar — qui lui fait prêter "
  "serment au nom de Jéhovah (voir 1200273097 ; 2Ch 36:13 — C8 : aucun P, vérifié). "
  "Serment violé : rébellion, appel à l'Égypte. Le siège : neuvième année de "
  "Tsidqiya (2R 25:1 — P188, P256 ; Jr 39:1 — P181, P185) — interruption égyptienne "
  "(37:6-10 — P259 : « l'armée de Pharaon sortie… retournera »), retour des "
  "Chaldéens, famine, brèche (onzième année — 2R 25:2-3, Jr 52:5-6 — P256, P260, "
  "P296). La délégation (21:1 — P211) : Pashhour fils de Malkija et Sophonie — "
  "« consulte pour nous » : réponse : sortez ! Yiriya (37:13-15 — C8 : aucun P, "
  "vérifié) : fausse accusation de désertion — coups, prison. La citerne (38:6 — "
  "C8 ; 38:7-13 — C8 : aucun P, vérifiés) : boue, cordes, chiffons — Ébed-Mélek "
  "sort Jérémie (voir T005 : 38:1-6). La fuite (52:7 — P295) : nuit, porte double, "
  "Araba — prise à Jéricho (52:8 — P295). Ribla (52:9-10 — P295) : jugement, fils "
  "égorgés « sous ses yeux », yeux crevés. L'incendie (52:12-14 — P296 ; 2R 25:8-10 "
  "— P225, P209) : maison, palais, murailles. Les chiffres (52:28-30 — P296) : "
  "7e année 3023, 18e 832, 23e 745."
 ),
 explication=(
  "« Sortez » (21:9 — P211 ; 38:2 — P261) : la reddition comme plan de survie — "
  "scandale patriotique, sagesse divine : « la vie pour butin ». « Yeux contre "
  "yeux » (32:4 — P246) : voir Neboukadnetsar en face — puis ne plus rien voir : "
  "Ribla accomplit les deux moitiés (voir, puis aveugler). « En paix » (34:5 — "
  "P255) : pas par l'épée — aveuglé, enchaîné, mais vivant jusqu'à Babylone ; "
  "« on brûlera en ton honneur » : les aromates funéraires, pas le bûcher. Lakish "
  "et Azéqa (34:7 — P255) : les deux dernières fortifiées — les feux de 6:1 "
  "(P187, voir T001) s'éteignent. Le veau coupé (34:18 — P256) : le rite antique "
  "du partage des victimes — passer entre les moitiés : « qu'il m'arrive comme au "
  "veau » — serment par l'horreur. Les esclaves (34:8-11 — P256) : libération "
  "proclamée pendant le siège — puis reprise : l'affranchissement révoqué, le "
  "jugement tombe (34:17-22). Le pain (37:21 — P260) : la ration de siège — "
  "« jusqu'à épuisement » : le compte à rebours comestible. Les femmes (38:22 — "
  "P262) : « tes amis t'ont séduit » — la chanson moqueuse des captives. La porte "
  "double (52:7 — P295) : la fuite nocturne — entre deux murs, vers l'Araba. "
  "Bronze (52:11 — P295) : les entraves — le roi enchaîné comme butin."
 ),
 interpretation=(
  "Le siège (2R 25:1-3 — P188, P256, P231 ; Jr 39:1 — P181, P185 ; Jr 52:4-6 — P211, "
  "P260, P296) : an 9 → an 11 — rampes, famine, brèche. L'interruption (37:6-10 — "
  "P259) : Pharaon sort, les Chaldéens lèvent le camp — puis « reviendront et "
  "brûleront » : l'Égypte comme parenthèse (Jr 46 — vague suivante, non versé). "
  "La famine (Jr 52:6 — P260 ; Jr 38:9 — P260 : « plus de pain ») : le siège par "
  "le ventre. Les sortis (Jr 39:9 — P211, P261 ; Jr 52:15-16 — P261) : ceux qui "
  "sont sortis vivent — les pauvres restent vignerons. Ribla (2R 25:4-7 — P246, "
  "P255, P262, P295 ; Jr 52:9-11 — P295 ; Jr 52:10-11 — P255) : fuite, capture, "
  "fils tués, yeux crevés, bronze — « yeux contre yeux » (32:4), « pas par l'épée » "
  "(34:5) : les deux moitiés ensemble. Lakish (voir 2007843, 1101990136) : 44-45 km "
  "au sud-ouest, fouilles 1930/1935, 21 ostraca, Yaosh le commandant, langue de "
  "Jérémie, lettre IV (« nous ne voyons pas Azéqah »), feu-signal (6:1 — P187), "
  "11 fois le nom divin en 7 lettres, cinq noms communs avec Jérémie : Guemaria et "
  "Elnathân (Jr 36 — C8, voir T006), Néria (32:12 — P247, voir T006), Yaazania "
  "(35:3 — P257, voir T006), Hoshaïa (Jr 42 — vague suivante, non versé). Azéqa "
  "(voir 1200000491) : Tell Zakariya, fortifiée par Rehabam — tombée avant Lakish. "
  "607 (voir 102012208 ; voir B : rappels P221/P222) : la chute, les 70 ans "
  "commencent. Évil-Merodak (580 — voir 1102010141 ; Jr 52:31-34 — C8, voir T003) : "
  "la grâce, trente-sept ans après."
 ),
 hist=(
  "Le serment (2Ch 36:13 — C8 ; voir 1200273097) : prêté au nom de Jéhovah, violé — "
  "Ézéchiel y reviendra (registre — non versé ici, voir les limites). Yiriya "
  "(37:13-15 — C8 ; voir 1200001853 : petit-fils d'un Hanania) : la Porte de "
  "Benjamin — accusation, coups, « maison de détention » (voir 1102010141). La "
  "citerne (38:6 — C8 ; voir 1102010141 : « jeté dans une citerne boueuse ») : "
  "Ébed-Mélek l'Éthiopien — trente hommes, cordes, chiffons sous les aisselles "
  "(38:7-13 — C8) : le sauvetage technique. Ribla (52:9 — P295) : le QG — deux "
  "rois de Juda y sont jugés (Yehoahaz par Néko — voir T003 ; Tsidqiya). L'incendie "
  "(52:12-14 — P296 ; 2R 25:8-10 — P225, P209) : cinquième mois — maison, palais, "
  "« toutes les grandes maisons ». Les colonnes (52:17-23 — P296) : bronze découpé, "
  "emporté — chapiteaux, grenades : le Temple en ferraille. Seraiah et Sophonie "
  "(52:24-27 — P191, P296) : exécutés à Ribla — voir T002."
 ),
 geo=(
  "Lakish (34:7 — P255) : 44 km au sud-ouest de Jérusalem (voir 2007843) — forteresse "
  "des collines, cendres du second incendie, salle de garde aux ostraca. Azéqa "
  "(34:7 — P255) : Tell Zakariya (voir 1200000491) — tombée la première. La porte "
  "double (52:7 — P295) : entre deux murs — la sortie nocturne. L'Araba (52:7 — "
  "P295) : la dépression du Jourdain — la fuite vers l'est. Jéricho (52:8 — P295) : "
  "la capture — les plaines referment le piège. Ribla (52:9 — P295) : la Syrie, "
  "l'Oronte — le tribunal. Babylone (52:11 — P295) : la mort en exil — « en paix » "
  "(34:5). Les murs démolis (52:14 — P296) : Jérusalem ouverte — voir Né 2 (P192, "
  "T002)."
 ),
 sci=(
  "Poliorcétique (2R 25 — P211, P256) : siège de trente mois (an 9 → an 11, avec "
  "interruption) — rampes, camps, blocus : la guerre d'usure. Épigraphie (voir "
  "2007843, 1101990136) : ostraca — encre sur tesson, paléo-hébreu cursif : le "
  "courrier militaire ; onomastique théophore (Yahou/Yah) + 11 Tétragrammes : le "
  "nom divin au quotidien. Optique (6:1 — P187 ; 34:7 — P255) : chaîne de "
  "feux-signaux — Lakish voit, Azéqa ne répond plus : le silence comme information. "
  "Métallurgie (52:11, 17-23 — P295, P296) : entraves de bronze ; colonnes découpées "
  "— le bronze du Temple fondu et pesé (« sans poids », 52:20 — P296). Démographie "
  "(52:28-30 — P296) : 3023 + 832 + 745 — trois vagues chiffrées : la comptabilité "
  "de l'exil. Médecine de siège (52:6 — P260 ; 37:21 — P260) : famine — « plus de "
  "pain » : la fin des rations. Ophtalmologie rapportée (52:11 — P295) : "
  "l'aveuglement après le dernier spectacle — dit, non décrit."
 ),
 limites=(
  "Jr 46 (Égypte) : vague suivante — non versé (37:5 et 46:25-26 non cités). "
  "Ézéchiel 17 (serment) : registre — non versé (aucun P nommé). Guedalia et Jr 40 : "
  "vague suivante — non mentionnés. 607 : voir 102012208 et B (rappels P221/P222) — "
  "non re-traité. Hoshaïa (Jr 42) : vague suivante — nommé par l'article seul. "
  "Chiffres 52:28-30 : versés (TM). Aveuglement : rapporté, non décrit (modération). "
  "C8 : 2Ch 36:13 (serment), Jr 37:13-15 (Yiriya), Jr 38:6 (citerne), Jr 38:7-13 "
  "(Ébed-Mélek) — aucun P (vérifiés)."
 ),
 accomplissement=[("Sortez, vivez", "Vie pour butin (21:1-10 — P211 ; 38:1-4 — P261)"),
     ("Yeux contre yeux", "Vu, puis aveuglé (32:1-5 — P246 ; 52:11)"),
     ("En paix", "Pas par l'épée (34:1-7 — P255 ; 2R 25:7)"),
     ("Lakish-Azeqa", "Dernières tombées (34:7 — P255 ; ostraca)"),
     ("Veau et esclaves", "Serment violé, jugement (34:8-22 — P256)"),
     ("Égypte parenthèse", "Repartie, Chaldéens revenus (37:6-10 — P259)"),
     ("Pain fini", "Famine (37:17-21 — P260 ; 52:6)"),
     ("Ville prise", "Femmes, fils livrés (38:14-23 — P262)"),
     ("Fuite manquée", "Ribla, bronze (52:7-11 — P295)"),
     ("Incendie, chiffres", "Brûlé, compté (52:12-27 — P296)")],
 tl=[("Serment (début)", "Au nom de Jéhovah (2Ch 36:13 — C8)"),
     ("An 9 (siège)", "Camps contre la ville (2R 25:1 — P256)"),
     ("Parenthèse", "Pharaon sort, revient (37:6-10 — P259)"),
     ("Famine", "Plus de pain (52:6 — P260)"),
     ("An 11 (brèche)", "Fuite, Ribla (52:7-11 — P295)"),
     ("607 (incendie)", "Brûlé, démoli, déporté (52:12-27 — P296)")],
 src=[("Derniers jours d'une dynastie (procès, détention, 580)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102010141"),
      ("Tessons confirment (Lakish, 44 km, Yaosh, feux)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007843"),
      ("Archéologie et texte inspiré (21 ostraca, noms)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990136"),
      ("Jérémie 34 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/34")],
 img="images/prophe_T004_chute.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T005", titre="Faux prophètes contre Jérémie — Pashhour, Ouriya, Hanania",
 ref="Jérémie 1:17-19 ; 14:10-16 ; 20:1-6 ; 23:9-40 ; 26:20-23 ; 28:1-17 ; 29:20-23 ; 29:24-32",
 statut="Accomplie (P182, P201, P210, P219, P226, P229, P232, P233)",
 cat="T", syst="Système imposteurs (609 → 607)",
 reg="Registre : Jérémie — P182 (1:17-19 : ville fortifiée), P201 (14:10-16 : épée sur les faux), P210 (20:1-6 : Pashhour), P219 (23:9-40 : absinthe), P226 (26:20-23 : Ouriya), P229 (28:1-17 : Hanania), P232 (29:20-23 : rôtis), P233 (29:24-32 : Shemayah) ; cross T004 (citerne 38:1-6), T002 (procès 26:1-6)",
 texte=[
  "« VILLE FORTIFIÉE, colonne de FER, murs de BRONZE. » (1:18 — P182 : l'armure !)",
  "« Ils COMBATTRONT contre toi, mais ne L'EMPORTERONT pas. » (1:19 — P182 : la garde !)",
  "« VISION MENSONGÈRE… ils vous PROPHÉTISENT. » (14:14 — P201 : le mensonge !)",
  "« MAGOR-MISSABIB : terreur de TOUS CÔTÉS. » (20:3 — P210 : le nom !)",
  "« PAILLE ou FROMENT ?… ma parole comme un FEU, comme un MARTEAU. » (23:28-29 — P219 : le tri !)",
  "« D'ici DEUX ANNÉES entières, je briserai le joug. » (28:11 — P229 : deux ans !)",
  "« CETTE ANNÉE, tu mourras. » (28:16 — P229 : cette année !)",
  "« Comme ceux que le roi a RÔTIS AU FEU. » (29:22 — P232 : les rôtis !)",
  "« AUCUN descendant au milieu de ce peuple. » (29:32 — P233 : retranché !)",
 ],
 contexte=(
  "L'armure (1:17-19 — P182) : « ceins tes reins » — Jérémie blindé AVANT le combat : "
  "ville, colonne, murs — contre « rois, princes, prêtres, peuple » (1:18). Pashhour "
  "(20:1-6 — P210 ; 20:1-2 — P182) : « intendant en chef de la maison » — il frappe "
  "Jérémie, le met aux entraves « toute la nuit » (20:2) — le lendemain, renommé : "
  "Magor-Missabib (20:3 — P210). Le procès (26:8 — P182 : « ils le saisirent » ; "
  "26:1-6 — P225, voir T002) : « tu mourras » — les anciens rappellent Mika (26:17-18 "
  "— C8 : aucun P, vérifié ; voir si, 1101990085) ; Ahikam protège (26:24 — C8 : "
  "aucun P, vérifié). Ouriya (26:20-23 — P226) : de Qiryath-Yearim, même message — "
  "fuite en Égypte, ramené, exécuté par Yehoïaqim (26:21-23) : le vrai prophète qui "
  "meurt. Hanania (28:1-17 — P229 ; voir it-1, 1200001853) : fils d'Azzour, de "
  "Guibéôn — 4e année de Tsidqiya, 5e mois (28:1) : « deux ans » (28:11), joug "
  "brisé (28:10) — réponse : joug de FER (28:13-14), « cette année, tu mourras » "
  "(28:16) — mort le 7e mois (28:17), environ deux mois plus tard (voir 1979805 ; "
  "614, voir 1979805). Ahab et Tsidqiya (29:20-23 — P232) : faux prophètes EN EXIL — "
  "« rôtis au feu » par Neboukadnetsar (29:22). Shemayah (29:24-32 — P233) : le "
  "Néhelamite — lettre contre Jérémie (29:25), sentence : retranché (29:32)."
 ),
 explication=(
  "L'armure (1:18 — P182) : le prophète-forteresse — assiégé, imprenable : « je suis "
  "avec toi pour te délivrer » (1:19). Les entraves (20:2 — P182, P210) : le bloc — "
  "pieds et cou pliés, une nuit : le pilori du Temple. Magor (20:3 — P210) : le "
  "nom-prophétie — Pashhour (« prospérité » ?) devient « Terreur-de-tous-côtés » : "
  "l'homme renommé par son châtiment. « Paix » mensongère (14:13 — P201) : « ni épée "
  "ni famine » — le faux message ; « par l'épée et la famine ils périront » (14:15-16 "
  "— P201) : les rassurants périssent les premiers. Absinthe (23:15 — P219) : "
  "« nourris d'absinthe » (registre) — l'amertume au menu des menteurs. Paille et "
  "froment (23:28 — P219) : « que le prophète qui a un rêve raconte un rêve — "
  "mais qui a MA parole dise MA parole » : le tri. Feu et marteau (23:29 — P219) : "
  "la parole qui consume et qui brise — contre la paille. Deux ans (28:11 — P229) : "
  "le délai précis — testable, falsifiable : le faux se date. Cette année (28:16 — "
  "P229) : le contre-délai — plus court, mortel. Rôtis (29:22 — P232) : le supplice "
  "babylonien — devenu proverbe-maudissement (« que Jéhovah te rende comme… »). "
  "Retranché (29:32 — P233) : pas de descendant, pas de témoin du bien — "
  "l'effacement."
 ),
 interpretation=(
  "Frappé (20:1-2 — P182) : Pashhour frappe, entrave — Jérémie tient (1:19). Saisi "
  "(26:8 — P182) : prêtres, prophètes, peuple — « tu mourras » (voir T002). En "
  "citerne (38:1-6 — P182 ; voir T004) : boue — « ils ne l'emporteront pas » (1:19). "
  "Renommé et déporté (20:3-6 — P210) : Magor-Missabib — « toi et tes amis à "
  "Babylone, tu y mourras » (20:6) ; « ses amis tombent » (39:6 — P210 : Ribla, voir "
  "T004). Ouriya tué (26:23 — P226 ; 26:24 — P182) : exécuté, Jérémie protégé — "
  "deux vrais, deux sorts. Hanania mort (28:16-17 — P229 ; P219) : 5e mois → 7e "
  "mois — « cette année-là » : le délai tient, le faux meurt. Le joug de fer "
  "(28:13-14 — P229) : bois brisé, fer imposé — voir T006 (27:1-11). Les rôtis "
  "(29:21-22 — P232 ; P219) : Ahab et Tsidqiya — le feu babylonien. Le retranché "
  "(29:32 — P233) : Shemayah — accompli en interne."
 ),
 hist=(
  "Guibéôn (voir 1200001853) : la ville benjaminite d'Hanania — l'imposteur du cru. "
  "Les ceps (20:2 — P182, P210) : le pilori à trous — cou, mains, pieds : "
  "l'immobilisation douloureuse (repère de dispositif, sans lien). Qiryath-Yearim "
  "(26:20 — P226) : la ville d'Ouriya, à l'ouest — l'arche y avait séjourné (sans "
  "verset versé — voir les limites). L'Égypte-refuge (26:21 — P226) : Ouriya y fuit "
  "— Yehoïaqim l'en fait ramener : l'extradition royale. Néhelam (29:24 — P233) : "
  "lieu inconnu — non tranché (voir les limites). Le feu babylonien (29:22 — "
  "P232) : le supplice — fournaise de Babylone (sans verset de Daniel versé — voir "
  "les limites). Mika (26:17-18 — C8 ; voir 1101990085) : le précédent — « Sion "
  "labourée comme un champ » (citation DANS Jr 26:18 — Michée non versé, voir les "
  "limites). 614 (voir 1979805) : l'année d'Hanania — 4e de Tsidqiya."
 ),
 geo=(
  "Le Temple (20:1-2 — P182, P210 ; 28:1 — P229) : le théâtre — entraves à la porte "
  "Haute de Benjamin (20:2), joug brisé « devant tout le peuple » (28:10-11). "
  "Guibéôn (voir 1200001853) : au nord-ouest — la ville du faux. Qiryath-Yearim "
  "(26:20 — P226) : à l'ouest — la ville du vrai tué. L'Égypte (26:21 — P226) : la "
  "fuite manquée. Babylone (20:6 — P210 ; 29:21 — P232) : Pashhour y meurt, les faux "
  "y rôtissent — l'exil comme tribunal. La citerne (38:6 — P182, voir T004) : la "
  "boue — Jérémie en sort vivant."
 ),
 sci=(
  "Onomastique (20:3 — P210) : Magor-Missabib — le nom-phrase, renomination "
  "prophétique : l'identité réécrite par le jugement. Toxicologie (23:15 — P219) : "
  "l'absinthe — amertume extrême : le menu des menteurs. Métallurgie (1:18 — P182 ; "
  "28:13 — P229) : fer et bronze — l'armure du vrai ; bois contre fer — le joug "
  "brisé remplacé par l'incassable. Pyrotechnique (23:29 — P219 ; 29:22 — P232) : "
  "parole-feu, parole-marteau — forge ; supplice-feu — fournaise. Chronologie "
  "(28:1, 17 — P229) : 5e mois → 7e mois — environ deux mois (voir 1979805) : le "
  "délai le plus court du registre ? Épistolaire (29:25 — P233) : la lettre de "
  "Shemayah — l'écrit contre le prophète, l'écrit jugé."
 ),
 limites=(
  "Jr 26:7-19 : seuls 26:8 (P182) et 26:17-18 (C8) sont cités — le reste (dont 26:11, "
  "26:19) non versé. Michée 3:12 : NON versé (un P couvre Mi 3, non nommé) — seule "
  "la citation DANS Jr 26:18 (C8) est versée. Arche à Qiryath-Yearim : sans verset. "
  "Fournaise (Daniel) : sans verset — voir les limites (E couvre Dn 2, 7, 8, 11, "
  "pas Dn 3). Néhelam : inconnu — non tranché. Citerne : voir T004 (C8 38:6-13). "
  "C8 : Jr 26:17-18 (Mika rappelé), Jr 26:24 (Ahikam protège) — aucun P (vérifiés : "
  "P225-P226 seuls sur Jr 26)."
 ),
 accomplissement=[("Blindé", "Ville, fer, bronze (1:17-19 — P182)"),
     ("Frappé, saisi, jeté", "Entraves, procès, citerne (P182 ; T002, T004)"),
     ("Faux périssent", "Épée et famine (14:10-16 — P201)"),
     ("Pashhour renommé", "Magor, Babylone, mort (20:1-6 — P210)"),
     ("Absinthe", "Paille triée, feu (23:9-40 — P219)"),
     ("Ouriya tué", "Même message, martyr (26:20-23 — P226)"),
     ("Hanania mort", "Joug de fer, 7e mois (28:1-17 — P229)"),
     ("Rôtis, retranché", "Feu, effacement (29:20-32 — P232, P233)")],
 tl=[("Appel (647)", "Armure avant combat (1:17-19 — P182)"),
     ("Pashhour (avant 609 ?)", "Nuit aux entraves (20 — P182, P210)"),
     ("Procès (début règne ?)", "« Tu mourras » (26 — P182, P225)"),
     ("Ouriya (Yehoïaqim)", "Fuite, retour, mort (26:20-23 — P226)"),
     ("614 (Hanania)", "5e → 7e mois (28 — P229)"),
     ("Exil (faux)", "Rôtis, retranchés (29 — P232, P233)")],
 src=[("Hanania — it-1 (Guibéôn, joug brisé, mort)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200001853"),
      ("Jugement des faux prophètes (2 ans, 2 mois, 614)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1979805"),
      ("Jérémie — si n° 24 (ch. 26-28, Mika, Ouriya)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990085"),
      ("Jérémie 28 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/28")],
 img="images/prophe_T005_faux.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="T006", titre="Signes en actes — potier, cruche, joug, champ, rouleau",
 ref="Jérémie 13:9-14 ; 16:1-9 ; 18:1-12 ; 19:1-13 ; 27:1-11 ; 32:6-15 ; 35:1-19 ; 36:1-3, 27-32",
 statut="Accomplie (P198, P204, P208, P209, P227, P247, P257, P258)",
 cat="T", syst="Système signes (625 → 607)",
 reg="Registre : Jérémie — P198 (13:9-14 : orgueil, cruches), P204 (16:1-9 : célibat, deuil), P208 (18:1-12 : potier), P209 (19:1-13 : cruche), P227 (27:1-11 : joug), P247 (32:6-15 : champ), P257 (35:1-19 : Rékabites), P258 (36:1-3, 27-32 : rouleau) ; cross T003 (36:30), T004 (32:1-5, Jr 36), T002 (Hinnom) ; 27:16-22 = vague suivante (non versé)",
 texte=[
  "« Je GÂTERAI l'orgueil de Juda… BRISÉS l'un contre l'autre. » (13:9, 14 — P198 : le bris !)",
  "« Ne prends pas de FEMME… pas de DEUIL, pas de FESTIN. » (16:2, 5, 8 — P204 : l'interdit !)",
  "« Comme l'ARGILE dans la main du POTIER. » (18:6 — P208 : l'argile !)",
  "« REVENEZ… rendez BONNES vos voies. » (18:11 — P208 : revenez !)",
  "« Je BRISERAI comme on brise un VASE — IRRÉPARABLE. » (19:11 — P209 : la cruche !)",
  "« Mettez votre COU sous le JOUG de Babylone et VIVEZ. » (27:8, 12 — P227 : le joug !)",
  "« On ACHÈTERA encore des maisons et des champs. » (32:15 — P247 : le champ !)",
  "« Nous ne BOIRONS PAS de vin. » (35:6 — P257 : le refus !)",
  "« TOUJOURS un homme devant moi. » (35:19 — P257 : toujours !)",
  "« BEAUCOUP D'AUTRES paroles ajoutées. » (36:32 — P258 : l'ajout !)",
 ],
 contexte=(
  "Huit signes joués, pas seulement dits. La ceinture (13:1-8 — C8 : aucun P, "
  "vérifié ; voir 1200273097) : lin porté, caché près du Perath, retrouvé pourri — "
  "Perath : Euphrate ou proche ? (voir les limites). Le célibat (16:1-9 — P204) : "
  "pas de femme, pas d'enfants — « car » (16:3-4) : ils mourraient ; pas de deuil "
  "(16:5-7), pas de festin (16:8) : « j'ai retiré ma paix ». Le potier (18:1-4 — "
  "P208) : « descends à la maison du potier » — le vase manqué, refait (voir "
  "1965442, 402016443). La cruche (19:1-2, 10-11 — P209) : flacon acheté, brisé "
  "devant les anciens DANS la vallée de Hinnom (19:2, 6 — voir T002) : « comme "
  "Topheth » (19:12). Le joug (27:2-4 — P227) : liens et barres sur le cou — "
  "envoyés aux rois d'Édom, Moab, Ammon, Tyr, Sidon (27:3) : « trois générations » "
  "(27:7 — P227 ; voir si, 1101990085). Le champ (32:6-15 — P247) : Hanamel le "
  "cousin, Anathoth, 17 sicles pesés (32:9), actes ouvert et scellé, jarre de terre "
  "(32:14) — Jérémie en prison (32:2 — P246, voir T004 ; Baruch scribe — voir "
  "2006604). Les Rékabites (35:1-19 — P257 ; voir 1102010145, 1101984337, 1979889) : "
  "descendants de Yehonadab le Qénite (compagnon de Jéhu — 2R 10:15-16 — C8 : le P "
  "sur ce chapitre couvre 10:30, verset disjoint, non nommé) — tentes, pas de vin, "
  "pas de semence — éprouvés dans la salle de Hanân (35:4 — P257 ; voir 1200001850), "
  "Yaazania en tête (35:3 — P257 ; « Jéhovah entend » — voir 1979889). Le rouleau "
  "(36:1-32 — P258 : 36:1-3, 27-32) : 4e année de Yehoïaqim, 625 (voir 1200002422, "
  "2006604) — dictée à Baruch (36:4 — C8), « enfermé » (36:5 — C8), lecture publique "
  "(36:8-10 — C8 ; cabinet de Guemaria — voir 2006604), princes effrayés (36:11-19 — "
  "C8 : Mikaïa, Elnathân — Lakish, voir T004), Yehoudi lit, le roi coupe au canif, "
  "jette au brasier — 9e mois, appartement d'hiver (36:20-26 — C8) — réécriture "
  "augmentée (36:27-32 — P258) dont 36:30 (voir T003 !)."
 ),
 explication=(
  "Ceinture pourrie (13:7 — C8 ; 13:9 — P198) : Juda collé à Dieu comme le lin aux "
  "reins — puis caché, mouillé, gâté : « bonne à rien ». Cruches brisées (13:14 — "
  "P198) : « l'un contre l'autre » — pères et fils : la guerre civile comme "
  "choc de poteries. Célibat (16:2 — P204) : miséricorde par l'interdit — pas "
  "d'enfants à pleurer. Deuil interdit (16:5-6 — P204) : « j'ai retiré ma paix » — "
  "quand tous meurent, on ne pleure plus personne. Potier (18:4 — P208) : le vase "
  "manqué REFAIT — « si la nation revient, je me repens » (18:7-8 — P208 ; voir "
  "1965442) : le CRU se refaçonne — encore temps. Cruche (19:11 — P209) : le vase "
  "CUIT brisé — irréparable : trop tard. Le contraste 18/19 est la leçon : cru = "
  "grâce, cuit = jugement. Joug (27:2, 8 — P227) : porter = vivre — « servez et "
  "restez » ; refuser = « épée, famine, peste » (27:8). Trois générations (27:7 — "
  "P227) : père, fils, petit-fils — la servitude bornée. 17 sicles (32:9 — P247) : "
  "pesés — l'achat réel en pleine invasion : la foi monnayée. Double acte (32:11 — "
  "P247) : ouvert + scellé — copie de consultation, copie de preuve. Jarre (32:14 — "
  "P247) : « pour qu'ils se conservent longtemps » — les archives enterrées "
  "attendront le retour. Vin refusé (35:6 — P257) : obéir à un mort (Jonadab, Xe "
  "siècle — voir 1979889) quand Juda désobéit au Vivant — le contraste qui accuse. "
  "Rouleau augmenté (36:32 — P258) : brûlé → réécrit + « beaucoup » : la parole "
  "coupée repousse."
 ),
 interpretation=(
  "Déportés et brisés (2R 24:12-16 ; 25:1-11 — P198) : orgueil abaissé, cruches "
  "choquées. Morts sans deuil (Jr 14:12 — P204 : « ni jeûne ni offrande » ; 2R "
  "25:3-4 — P204 : famine, fuite) : le célibat justifié. Le potier prêché (18:11-17 "
  "— P208) : « revenez » refusé — « nous suivrons nos plans » (18:12) : l'argile "
  "dure (voir 402016443). La cruche accomplit le potier (19:1-13 — P208 ; 19:14-15 "
  "— P209 : proclamation au Temple ; 2R 25:8-10 — P209) : brisée devant les "
  "anciens, la ville suit. Le joug porté ou subi (27:12-15 — P227 : aux rois, "
  "prêtres, peuple — « servez et vivez » ; 2R 24:1 — P227 : Yehoïaqim vassal ; 2R "
  "25:1-11 — P227 : les rebelles écrasés ; 27:16-22 — vague suivante, NON versé : "
  "voir les limites). Le champ prouvé (32:43-44 — P247 : « on achètera » ; Né "
  "11:25-30 — P247 : Anathoth habitée au retour). Les Rékabites protégés (35:19 — "
  "P257 ; « survie d'un reste en 607 » — P257) : « toujours un homme devant moi » — "
  "toujours. La parole revenue (36:32 — P258) : réécrite, augmentée — "
  "dont 36:30 contre Yehoïaqim (voir T003)."
 ),
 hist=(
  "Perath (13:4 — C8) : Euphrate (plusieurs centaines de km, deux voyages !) ou "
  "lieu proche (Parah ?) — NON TRANCHÉ (voir les limites) : dans les deux cas, le "
  "signe coûte. Potiers (voir 1965442, 402016443) : tour, argile, eau — le vase "
  "manqué recyclé : l'atelier antique ne gaspille pas le cru. Jougs (27:2 — P227) : "
  "barres de bois, liens de cuir — le harnais porté par l'homme : l'humiliation "
  "marchante (brisée par Hanania — voir T005). Actes scellés (32:11-14 — P247) : "
  "bulles d'argile, sceaux — l'épigraphie des contrats (repère, sans lien) ; "
  "jarres d'archives — comme à Qumrân (parallèle, sans lien — voir les limites). "
  "Yehonadab (Xe s. — voir 1979889 ; 2R 10:15-16 — C8) : « donne ta main » — sur le "
  "char de Jéhu : l'alliance du Qénite et du réformateur. Hanân (35:4 — P257 ; voir "
  "1200001850) : « homme du vrai Dieu » — sa salle pour l'épreuve. Guemaria (36:10 "
  "— C8 ; voir 2006604) : le cabinet — Mikaïa son fils rapporte (36:11 — C8) ; "
  "Elnathân (36:12 — C8) : Lakish (voir T004) — le prince des deux mondes. Yehoudi "
  "(36:21-23 — C8) : trois-quatre colonnes lues, canif, brasier — 9e mois (hiver) : "
  "le roi au chaud brûle la parole. Baruch (voir 2006604, 2019640, 1200002422) : "
  "23 ans de prophétie à écrire (25:1-3 — rappel P221/B), cachette (36:16-19 — "
  "C8 : « cachez-vous »), jarre aux actes (32:14 — P247)."
 ),
 geo=(
  "Perath (13:4 — C8) : le fleuve ou le proche — le signe voyage (voir les "
  "limites). Hinnom (19:2, 6 — P209 ; voir T002) : la cruche brisée LÀ — devant "
  "Topheth : le vase et le charnier. Anathoth (32:7-9 — P247) : le village — moins "
  "de 5 km (voir 1200002421) : le champ du cousin sous les yeux des assiégeants. "
  "Cour de la Garde (32:2 — P246, voir T004) : la prison — l'achat signé en "
  "captivité. Salle de Hanân (35:4 — P257) : le Temple — le vin refusé au lieu "
  "saint. Cabinet de Guemaria (36:10 — C8) : le parvis — la lecture. Appartement "
  "d'hiver (36:22 — C8) : le brasier — 9e mois, froid dehors, feu dedans."
 ),
 sci=(
  "Textile (13:1-7 — C8) : le lin — fibre végétale, pourrit à l'humidité : la "
  "ceinture cachée près de l'eau devient « bonne à rien » — la dégradation "
  "documentée. Céramique (18:4 — P208 ; 19:11 — P209) : CRU contre CUIT — le vase "
  "cru se refaçonne (grâce), le vase cuit brisé est perdu (jugement) : toute la "
  "théologie du chapitre en technologie. Tour de potier (18:3 — P208) : rotation, "
  "centrifugation, mains d'eau — voir 1965442. Métrologie (32:9 — P247) : 17 "
  "sicles d'argent PESÉS — balance à fléau : le prix vérifié. Conservation (32:14 — "
  "P247) : jarre de terre — obscurité, sécheresse : les actes traversent 70 ans "
  "(+ Qumrân : parallèle, sans lien). Viticulture refusée (35:6-7 — P257) : ni "
  "vigne, ni vin — les Rékabites hors de l'économie sédentaire. Pyrotechnique "
  "(36:22-23 — C8) : brasier d'hiver, rouleau coupé au canif — la combustion "
  "feuillet par feuillet. Acoustique (36:8-10 — C8) : lecture publique dans la cour "
  "— la voix portant : le rouleau lu avant d'être brûlé."
 ),
 limites=(
  "Perath : Euphrate ou lieu proche — NON TRANCHÉ (les deux lectures existent ; le "
  "signe coûte dans les deux cas). Cru/cuit : lecture technique versée (18:4 cru, "
  "19:11 cuit) — voir 1965442. Jr 27:16-22 (ustensiles) : vague suivante — NON "
  "versé ; P227 n'est cité que 27:1-15. Jr 32:1-5 : voir T004 (P246). Jr 36:30 : "
  "voir T003 (P215). Qumrân : parallèle (sans lien), pas preuve. Qénites-Moïse : "
  "sans verset (non vérifié). C8 : Jr 13:1-8 (ceinture), Jr 36:4-5 (dictée, enfermé), "
  "Jr 36:8-26 (lecture, princes, canif, brasier), 2R 10:15-16 (Yehonadab — le P sur "
  "ce chapitre couvre 10:30, verset disjoint, non nommé) — aucun P (vérifiés)."
 ),
 accomplissement=[("Ceinture gâtée", "Orgueil pourri (13:1-14 — C8 + P198)"),
     ("Célibat", "Pas d'enfants à pleurer (16:1-9 — P204)"),
     ("Potier", "Cru refait, appel (18:1-12 — P208)"),
     ("Cruche", "Cuit brisé, fin (19:1-13 — P209)"),
     ("Joug", "Porter et vivre (27:1-15 — P227 ; 27:16+ suiv.)"),
     ("Champ", "17 sicles, jarre (32:6-15 — P247)"),
     ("Rékabites", "Vin refusé, toujours (35:1-19 — P257)"),
     ("Rouleau", "Brûlé, augmenté (36 — C8 + P258)")],
 tl=[("Ceinture (avant ?)", "Perath aller-retour (13 — C8)"),
     ("625 (rouleau)", "4e Yehoïaqim, dictée (36 — P258)"),
     ("Hiver 625 (brasier)", "Canif, feu, cachette (36 — C8)"),
     ("Joug (Tsidqiya)", "Cou chargé, nations (27 — P227)"),
     ("Rékabites (siège ?)", "Épreuve au Temple (35 — P257)"),
     ("An 10 (champ)", "Achat en prison (32 — P247 ; voir T004)")],
 src=[("Le Grand Potier (Jr 18:6-8, argile, Rm 9:21)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965442"),
      ("Baruch secrétaire (625, 23 ans, cachette, jarre)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2006604"),
      ("Obéis (Rékabites, Qénite, Jr 35:1-10, 19)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1102010145"),
      ("Jérémie, livre de — it-1 (rouleau 625, Yehoudi)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002422"),
      ("Jérémie 18 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/24/18")],
 img="images/prophe_T006_signes.jpg",
))
