#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE F-G (vague de transition) — LES CHRONOLOGIES (2e partie) + RESTAURATION
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="F–G",
    nom="Les chronologies (2e partie) · Restauration et monde nouveau",
    vague="8",
    intro=(
        "Cette vague de transition ferme la catégorie F et ouvre la catégorie G. "
        "Côté chronologies, quatre dernières fiches : les trois ans et demi en "
        "sept passages (avec le comput sourcé des deux témoins : octobre 1914 "
        "au 26/27 mars 1918, jours littéraux), le millénium (mille années "
        "solaires, encore à venir, avec réfutation datée du millénium de 1799), "
        "les fêtes-calendrier (trois rendez-vous tenus au printemps 33 en "
        "cinquante jours), et le signe de Jonas (trois jours et trois nuits au "
        "comput juif inclusif — double preuve : Esther et les pharisiens "
        "eux-mêmes). La catégorie F compte ainsi 10 fiches et est terminée. "
        "Côté restauration, cinq premières fiches : Ézéchiel 37 (trois niveaux "
        "distingués, jamais confondus : 537, 1919, et l'image de la résurrection), "
        "la nouvelle alliance (la loi au cœur, la coupe, « désuète » dès 61), "
        "le paradis d'Ésaïe (le loup « hôte » de l'agneau, les maisons et les "
        "vignes), la résurrection (neuf types avant Jésus, vingt milliards de "
        "places), et le nouveau ciel avec la nouvelle terre (renouvelés, pas "
        "remplacés — kainos, pas neos). Périmètre : Gog et le détail de "
        "Révélation appartiennent aux catégories H et I."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F016", titre="Trois ans et demi, sept fois — les deux témoins",
 ref="Daniel 7:25 ; 12:7 ; Révélation 11:2-13 ; 12:6, 14 ; 13:5 ; Luc 4:25 ; Jacques 5:17",
 statut="Accomplie (femme, bête : renvois E002, E008, I)",
 cat="F", syst="Système 29/33 · dates neutres (1914-1919)",
 reg="Registre : Daniel — P378 (7:25), P407 (12:7) ; Révélation — P852 (11:1-2), P853 (11:3-6), P854 (11:7-10), P855 (11:11-13), P859 (12:6), P867 (13:5-6)",
 texte=[
  "« Les saints seront livrés en sa main un temps, des temps et la moitié "
  "d'un temps. » (Dn 7:25)",
  "« Je ferai prophétiser mes deux témoins, vêtus d'une toile de sac, pendant "
  "1 260 jours. » (Ré 11:3)",
  "« Quand ils auront fini de rendre témoignage, la bête sauvage leur fera la "
  "guerre, les vaincra et les tuera. » (Ré 11:7 — quand, pas avant !)",
  "« Ils sont ramenés à la vie au bout de trois jours et demi ; une voix : "
  "Montez ici. » (Ré 11:11-12)",
  "« Le ciel fut fermé trois ans et six mois. » (Lc 4:25 — Élie : l'Ancien "
  "Testament raconte, le Nouveau chiffre)",
 ],
 contexte=(
  "Sept passages, une durée : Daniel 7:25 et 12:7 (voir E002, E008), Révélation "
  "11:2 (42 mois de foulée), 11:3 (1 260 jours des témoins), 12:6 et 12:14 "
  "(1 260 jours puis trois temps et demi de la femme), 13:5 (42 mois de la bête). "
  "Deux types : Élie (1 Rois 17-18 racontent la sécheresse sans la chiffrer — "
  "Luc 4:25 et Jacques 5:17 donnent « trois ans six mois ») et le ministère "
  "(quatre Pâques, 29-33 — voir F015). Au centre : les deux témoins en sac, tués, "
  "ranimés — le seul des sept computs daté au jour près par les publications."
 ),
 explication=(
  "Trois et demi, c'est sept divisé : la semaine brisée — persécution limitée, "
  "le mal n'a que la moitié. 1 260 = 42 × 30 = 3,5 × 360 (mois de 30 jours, "
  "année de 360 — convention signalée). Deux témoins : le témoignage valide "
  "(Dt 19:15 !), les deux oliviers et lampes (Za 4 — Zorobabel et Josué : le "
  "modèle !). Le sac : le deuil (Jacob en Gn 37:34, Tyr en Éz 27:31 — « amené "
  "bas dans la tristesse »). Fermer le ciel (Élie !) et changer l'eau en sang "
  "(Moïse !) : les témoins cumulent la Loi et les Prophètes (cf. Mt 17:3). "
  "La bête tue QUAND le témoignage est achevé (11:7) : pas un jour avant. "
  "« Sodome et Égypte » (11:8) : la grande ville — la chrétienté, « où leur "
  "Seigneur a été attaché ». Trois jours et demi morts (11:9) : la mort "
  "miniature — puis « montez ici » (11:12) : état élevé, pas altitude."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : les témoins, c'est le reste oint "
  "(« ils étaient déjà ses témoins en 1918 »). Les 1 260 jours sont LITTÉRAUX — "
  "exprimés en mois (11:2) PUIS en jours (11:3) : la double expression prouve la "
  "littéralité. Comput : mi-octobre 1914 → 26/27 mars 1918. Puis le témoignage "
  "est tué (juin 1918, Atlanta — l'œuvre des imprimés spéciaux), trois jours et "
  "demi d'opprobre (« infecte réputation » jetée par la chrétienté), et 1919 : "
  "ranimés — « montez ici », hors d'atteinte. Et la jonction : Ézéchiel 37 AVEC "
  "Révélation 11 — « leur accomplissement moderne frappant en 1919 » (voir G001). "
  "La femme (12:6, 14), la bête (13:5), Daniel (7:25, 12:7) : tableau donné, "
  "détails renvoyés (E002, E008, catégorie I)."
 ),
 accomplissement=[
  ("IXe s. av. n. è.", "Élie : 3 ans 6 mois, ciel fermé (1R 17-18 ; Lc 4:25 ; Jc 5:17)"),
  ("29-33 de n. è.", "Le ministère : 3 ans et demi, quatre Pâques (voir F015)"),
  ("Oct. 1914 - 26/27 mars 1918", "1 260 jours littéraux : les témoins en sac"),
  ("Juin 1918", "Témoignage tué : Atlanta (l'œuvre des imprimés)"),
  ("1919 de n. è.", "Ranimés : « montez ici » — avec Ézéchiel 37 (voir G001)"),
 ],
 hist=(
  "Octobre 1914 : la guerre — le sac commence. Mars 1918 : les 1 260 jours "
  "s'achèvent (26/27). Juin 1918 : huit dirigeants condamnés (Atlanta) — le "
  "témoignage tué ; la presse jette l'opprobre (« infecte réputation »). Le "
  "livre « Le mystère accompli » (1917) avait attisé la persécution et les "
  "interdictions. 26 mars 1919 : libération sous caution (voir E008) ; septembre "
  "1919 : Cedar Point — « Annoncez le Roi » : les témoins sont debout, « montés » "
  "hors d'atteinte."
 ),
 geo=(
  "La « grande ville » (11:8) : Sodome-Égypte spirituelles — la chrétienté "
  "occidentale : lieu symbolique, pas de GPS. Le « ciel » de 11:12 : état "
  "spirituel élevé, pas altitude. Élie : Kérith, Sarepta, Carmel — le triangle de "
  "la sécheresse. Le Jourdain : les 3 ans et demi du ministère (voir F015). "
  "Ohio 1919 : la résurrection géographique des témoins."
 ),
 sci=(
  "1 260 = 42 × 30 : arithmétique exacte. 26/27 mars 1918 moins 1 260 jours = "
  "13/14 octobre 1914 : vérifiable au calendrier. Méthode : « exprimé en mois "
  "PUIS en jours, donc littéral » — l'argument du livre Révélation, cité. "
  "3,5 = 7/2 : la moitié — le mal, en persécution, n'obtient jamais le tout. "
  "Pas d'uniformité forcée : les 1 260 des témoins sont littéraux ; chaque autre "
  "« trois et demi » suit son passage (voir Limites)."
 ),
 limites=(
  "Révélation 11:13 (7 000, le dixième) : renvoyé à la catégorie I. La femme "
  "(12:6, 14) et la bête (13:5) : renvoyées à I. Daniel 7:25 et 12:7 : renvoyés "
  "à E002 et E008. Élie : mois non datés (IXe siècle). Les sept « trois et demi » "
  "ne sont pas uniformisés : littéral ici (témoins), selon les passages ailleurs."
 ),
 tl=[("IXe s.", "Élie : 3,5 ans"), ("29-33", "Ministère : 3,5 ans"), ("Oct. 1914", "Sac : 1 260 j"),
     ("26/27 mars 1918", "Fin des 1 260"), ("Juin 1918", "Tués"), ("1919", "Ranimés + Éz 37")],
 src=[("La mort et la résurrection des deux témoins (1260 j, 26/27 mars 1918)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101969049"),
      ("Révélation 11 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/11"),
      ("Révélation 12 — Bible d'étude, notes (la femme, 1260 j)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/12"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F016_temoins.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F017", titre="Les mille ans — Satan lié, la mort meurt en dernier",
 ref="Révélation 20 ; 1 Corinthiens 15:24-28 ; 2 Pierre 3:8 ; Genèse 3:15 ; Révélation 1:18",
 statut="À venir (sans date)",
 cat="F", syst="Système 1914 · avenir sans date",
 reg="Registre : Révélation — P931-P942 (20:1-13) ; 1 Corinthiens — P735 (15:22-26), P736 (15:27-28) ; 2P 3:8 sans entrée (C8)",
 texte=[
  "« Un ange descendit avec la clé de l'abîme et une grande chaîne ; il saisit "
  "le dragon, le serpent originel — le Diable et Satan — et le lia pour mille "
  "ans. » (Ré 20:1-2)",
  "« L'abîme fermé et scellé sur lui, pour qu'il n'égare plus les nations "
  "jusqu'à la fin des mille ans ; après, il doit être délié pour peu de temps. » "
  "(Ré 20:3)",
  "« Heureux et saint qui a part à la première résurrection ; ils seront prêtres "
  "de Dieu et du Christ et régneront avec lui pendant les mille ans. » (Ré 20:4-6)",
  "« La mort et l'hadès furent jetés dans le lac de feu : c'est la seconde "
  "mort. » (Ré 20:14 — même la mort meurt)",
  "« Le dernier ennemi à être détruit, c'est la mort ; puis le Fils remettra le "
  "Royaume, pour que Dieu soit tout en tous. » (1Co 15:26-28)",
 ],
 contexte=(
  "Après Armaguédon (Révélation 19 — renvoi H/I) : l'ange à la clé — Jésus (clé "
  "de l'abîme : Ré 1:18 ; « semence » promise à meurtrir le serpent : Gn 3:15). "
  "« Mille ans » répété SIX fois (20:2, 3, 4, 5, 6, 7) : l'insistance comme "
  "preuve — « mille années solaires », pas symbolique. À venir (« très proche » "
  "— sans date, jamais). Séquence : Satan lié → résurrection et perfection → "
  "délié « peu » → Gog (20:8 — renvoi H/I) → lac de feu → « Dieu tout en tous »."
 ),
 explication=(
  "Lié (deo) : neutralisé, pas détruit. La chaîne : l'impuissance, pas du fer. "
  "L'abîme (abyssos) : la prison des démons (Lc 8:31 !) — l'inactivité, pas le "
  "tombeau. Scellé (sphragizo) : fermeture officielle — comme la tombe (Mt 27:66 "
  "!). « Qu'il n'égare plus les nations » : le but — un monde SANS tentateur. "
  "« Peu de temps » : le test final après mille ans. Première résurrection : "
  "céleste — les 144 000 (« heureux et saint », seconde mort sans pouvoir, "
  "prêtres ET rois). « Les autres morts » (20:5) : les terrestres — pendant les "
  "mille ans : l'ordre, pas la simultanéité. Les livres (20:12) : jugés sur les "
  "actes MILLÉNAIRES — pas les passés ! « La mort jetée » (20:14) : le tombeau "
  "aboli, la mort détruite — « dernier ennemi » (1Co 15:26). « Dieu tout en tous » "
  "(15:28) : le Fils remet le mandat — la fin de la mission. « Mille ans comme "
  "un jour » (2P 3:8) : RELATIVITÉ divine — pas une équation ! Cette fiche REFUSE "
  "le « septième millénaire » spéculatif (voir Limites)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : mille ans littéraux et solaires, à "
  "venir ; Satan et ses démons RÉELLEMENT dans l'abîme ; Jésus et ses 144 000 "
  "cohéritiers régnant « sans que l'organisation du Diable ne s'oppose » ; morts "
  "ressuscités, humanité ramenée à la perfection (Ré 20:12, 21:1-4 — voir G004, "
  "G005). Réfutations datées : le millénium catholique « achevé en 1799 » (pape "
  "déposé par les Français — faux, le vrai est à venir) ; Augustin (règne "
  "« commencé à la naissance de l'Église » — allégorie amalgamée au platonisme, "
  "Britannica citée). Précurseur XIXe : Henry Dunn — « le rétablissement de "
  "toutes choses » (Ac 3:21), perfection terrestre sous le millénium."
 ),
 accomplissement=[
  ("1914 de n. è.", "Satan jeté du ciel vers la terre (Ré 12:7-12 — voir B009)"),
  ("Avenir", "Armaguédon (renvoi H/I) — sans date"),
  ("Mille ans (à venir)", "Satan lié ; résurrection ; perfection ; livres ouverts"),
  ("« Peu de temps » (à venir)", "Délié ; Gog (20:7-10 — renvoi H/I)"),
  ("Fin", "Lac de feu (Satan, démons, mort, hadès) ; « Dieu tout en tous »"),
 ],
 hist=(
  "1798-1799 : Berthier entre à Rome, Pie VI déporté — mort à Valence (août 1799). "
  "Le clergé y vit la fin du millénium et la libération de Satan : millénium "
  "faux, réfuté — le vrai n'a pas commencé. Augustin (Cité de Dieu) : "
  "l'amillénarisme — règne « spirituel » depuis l'Église, explication "
  "« allégorique » (Encyclopédie catholique citée). Henry Dunn (XIXe s.) : "
  "Ac 3:21 — rétablissement terrestre sous mille ans. 1914 : « malheur à la "
  "terre » (Ré 12:12) — Satan à terre, en attendant l'abîme."
 ),
 geo=(
  "L'abîme : un non-lieu — l'inactivité contrainte, pas de GPS. « Les nations "
  "aux quatre coins » (20:8) : Gog vient de partout — renvoi H/I. La terre : "
  "le théâtre du millénium (voir G003, G005). Le ciel : les trônes (20:4) — le "
  "gouvernement. Ciel et terre enfin accordés — jusqu'à « Dieu tout en tous »."
 ),
 sci=(
  "« Mille années solaires » : littéralité affirmée — pas « mille » pour "
  "« longtemps ». Six répétitions (20:2-7) : l'insistance textuelle comme indice. "
  "2 Pierre 3:8 : anti-comput explicite — la relativité divine (« aux yeux de "
  "Dieu ») n'est pas une équation calendaire ; aucun « septième millénaire » "
  "n'est construit ici. Ordre des résurrections (céleste d'abord, terrestres "
  "pendant) : séquence lue, pas supposée."
 ),
 limites=(
  "Armaguédon : renvoi H/I — sans date, jamais. Gog (20:7-10, Éz 38-39) : renvoyé "
  "à H/I. « Peu de temps » : pas de comput. 2 Pierre 3:8 : pas d'équation — et "
  "sans entrée au registre (C8). L'Épouse, les trônes, les détails de Révélation : "
  "renvoi I ; les conditions terrestres : G003-G005."
 ),
 tl=[("1914", "Satan à terre"), ("Avenir", "Armaguédon (renvoi)"), ("Mille ans", "Lié, résurrection"),
     ("Peu de temps", "Délié, Gog (renvoi)"), ("Fin", "« Dieu tout en tous »")],
 src=[("D'ores et déjà organisés en vue des mille ans (1000 ans solaires)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1989645"),
      ("La vie éternelle sur la terre (millénium, Augustin, Dunn)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2009603"),
      ("Satan — Étude perspicace (abîme, délié, lac de feu)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200003845"),
      ("Révélation 20 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/20")],
 img="images/prophe_F017_millenium.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F018", titre="Les fêtes-rendez-vous — trois dates tenues au printemps 33",
 ref="Lévitique 23 ; 1 Corinthiens 5:7 ; 15:20-23 ; Actes 2:1-4 ; Jean 7:37-38 ; Hébreux 9:11-12",
 statut="Accomplie (trompettes : renvoi)",
 cat="F", syst="Système 1513/33/36",
 reg="Registre : Lv 23 sans entrée (C8) ; 1Co 15 — P734 (15:3-4), P735 (15:20-23)",
 texte=[
  "« Ce sont les fêtes de Jéhovah, les saintes assemblées : la Pâque, le 14 "
  "Nisan ; les gâteaux sans levain, du 15 au 21 ; la gerbe des prémices, le 16 ; "
  "puis vous compterez cinquante jours. » (Lv 23:4-16 — moedim : RENDEZ-VOUS)",
  "« Christ, notre Pâque, a été sacrifié. » (1Co 5:7 — le 14 Nisan 33)",
  "« Christ a été relevé — prémices de ceux qui dorment. » (1Co 15:20 — "
  "le 16 Nisan 33, jour de la gerbe)",
  "« Le jour de la Pentecôte, ils furent tous remplis d'esprit saint. » "
  "(Ac 2:1-4 — le 50e jour, 6 Sivan 33)",
  "« Le grand jour de la fête, Jésus cria : Si quelqu'un a soif, qu'il vienne "
  "à moi et qu'il boive. » (Jn 7:37 — les Huttes)",
 ],
 contexte=(
  "Lévitique 23 : les « fêtes de Jéhovah » — moedim, RENDEZ-VOUS : Dieu donne ses "
  "dates. Trois pèlerinages annuels (Ex 23:14-17) : Pâque, Pentecôte, Huttes — "
  "tout Israël monte. Quatre au printemps (Pâque 14, pains 15-21, gerbe 16, "
  "Pentecôte 50e jour), trois en automne (trompettes 1er Tishri, Kippour 10, "
  "huttes 15-21). Printemps 33 : trois rendez-vous tenus en cinquante jours — "
  "le calendrier comme preuve."
 ),
 explication=(
  "Pâque 14 (agneau sans défaut, Ex 12:5) : « Christ notre Pâque » (1Co 5:7) — "
  "mort LE 14 (voir D). Pains 15-21 : sans levain = sans péché (« ni vieux levain "
  "de malice », 1Co 5:8) — sept jours : la semaine complète. Gerbe 16 : l'orge, "
  "PREMIÈRE moisson — aucune moisson avant (Lv 23:14) — Jésus relevé PRÉCISÉMENT "
  "ce jour-là : « prémices » (1Co 15:20, 23) — premier rang ! Pentecôte 50e "
  "(7×7+1, 6 Sivan, blé) : l'esprit sur 120, puis 3 000 (Ac 1:15, 2:41) — "
  "« une sorte de prémices » (Jc 1:18) : deuxième rang ! Notez : la gerbe est "
  "SANS levain (Jésus, Hé 7:26), les deux pains de Pentecôte AVEC levain "
  "(Lv 23:17 — seule offrande levée : les disciples, pécheurs !). Trompettes "
  "(1er Tishri, « mémorial ») : antitype RENVOYÉ (voir Limites). Kippour "
  "(10 Tishri) : deux boucs (Lv 16) — pour Jéhovah (le sacrifice : Hé 9:11-12, "
  "« une fois pour toutes ») et pour Azazel (Satan — résumé, développement "
  "renvoyé) ; le grand prêtre SEUL (Lv 16:17, « personne » !) — Jésus SEUL "
  "(Hé 9:24). Huttes (15-21 Tishri) : 70 taureaux (Nb 29:13-32 : 13+12+11+10+9+"
  "8+7 = 70 — les 70 nations de Genèse 10 !) — la cueillette (oints + « grande "
  "foule ») ; les cabanes : fragilité, pèlerinage ; Néhémie 8 (« depuis Josué » !) ; "
  "Jésus « le grand jour » (Jn 7:37-38 : « fleuves d'eau vive » !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : au printemps 33, trois fêtes, trois "
  "événements — 14 : l'Agneau ; 16 : les prémices relevées ; 50e jour : l'esprit "
  "sur les suivants. La gerbe (Jésus, sans levain) précède les pains (disciples, "
  "avec levain) : deux rangs de prémices. Les Huttes : la cueillette finale — "
  "oints et grande foule. Kippour : le sacrifice entré au ciel (Hébreux). Les "
  "trompettes : antitype renvoyé aux publications."
 ),
 accomplissement=[
  ("1513 av. n. è.", "Première Pâque (Ex 12) ; Sinaï : la Loi (tradition : à la Pentecôte)"),
  ("14 Nisan 33", "L'Agneau : « Christ notre Pâque » (voir D)"),
  ("16 Nisan 33", "La gerbe : « précisément ce jour-là », Jésus relevé"),
  ("6 Sivan 33 (50e jour)", "L'esprit : 120, puis 3 000 (Ac 2)"),
  ("36 de n. è.", "Corneille : le deuxième rang s'ouvre aux nations (voir C012)"),
  ("Huttes (en cours)", "La cueillette : oints et grande foule"),
 ],
 hist=(
  "Trois pèlerinages (Ex 23) : Jérusalem bondée — Josèphe décrit les foules "
  "pascales immenses. 70 taureaux (Nb 29 : 13→7, somme 70 — arithmétique exacte) "
  "pour 70 nations (Gn 10). Néhémie 8:14-17 : les Huttes restaurées — « depuis "
  "Josué » : mille ans d'oubli ! 6 Sivan : date fixe de Pentecôte. 120 → 3 120 "
  "en un jour (Ac 1:15, 2:41). Tradition juive citée comme tradition : la Loi "
  "donnée à la Pentecôte — Loi (1513) et esprit (33), même fête ?"
 ),
 geo=(
  "Jérusalem : les trois montées — tout Israël converge. Le Sinaï : la Loi (à la "
  "Pentecôte selon la tradition). La chambre haute (Ac 1:13) : les 120. Les "
  "nations : 70 taureaux — Genèse 10 en sacrifice. Les cabanes : le désert "
  "reconstitué en ville — fragilité annuelle."
 ),
 sci=(
  "7 × 7 + 1 = 50 : l'arithmétique des semaines (Dt 16:9-10 : compter « depuis la "
  "faucille »). Orge AVANT blé : agronomie — l'orge précoce (avril), le blé tardif "
  "(mai-juin) : l'ordre des moissons impose l'ordre des fêtes — la nature écrit "
  "le calendrier. Deux pains AVEC levain : la seule offrande levée — l'exception "
  "qui parle. 13+12+11+10+9+8+7 = 70 : exact."
 ),
 limites=(
  "Lévitique 23 sans entrée au registre (C8). Les trompettes : antitype renvoyé "
  "aux publications. Azazel (Lv 16:8) : résumé ici (Satan), développement "
  "renvoyé. Sinaï = Pentecôte : tradition juive, citée comme telle. « Depuis "
  "Josué » (Néh 8:17) : le texte dit — signalé."
 ),
 tl=[("1513", "Pâque, Loi"), ("14 Nisan 33", "Agneau"), ("16 Nisan 33", "Gerbe : relevé"),
     ("50e jour", "Esprit : 3 000"), ("36", "Nations"), ("Huttes", "Cueillette")],
 src=[("Tu ne seras que joyeux (14, 16 Nisan, 70 taureaux)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007005"),
      ("Pentecôte — Étude perspicace (50e jour, 6 Sivan, prémices)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013352"),
      ("Lévitique 23 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/3/23"),
      ("Actes 2 — Bible d'étude, notes (Pentecôte 33)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/2")],
 img="images/prophe_F018_fetes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="F019", titre="Trois jours et trois nuits — le signe de Jonas",
 ref="Jonas 1:17 - 2:10 ; Jonas 3-4 ; Matthieu 12:38-42 ; 27:62-64 ; 1 Corinthiens 15:4 ; Esther 4:16 - 5:1",
 statut="Accomplie",
 cat="F", syst="Système 33",
 reg="Registre : Jonas — P644 (1:17 ; Mt 12:39-40), P448 (3:4) ; Jon 2 (prière) sans entrée (C8)",
 texte=[
  "« Jéhovah assigna un grand poisson pour avaler Jonas ; et Jonas resta trois "
  "jours et trois nuits dans le ventre du poisson. » (Jon 1:17 — mana : assigné !)",
  "« Du ventre du shéol j'ai crié ; tu as fait remonter ma vie. Le salut est à "
  "Jéhovah ! » (Jon 2:2, 6, 9 — yeshoua : le nom de Jésus !)",
  "« Tout comme Jonas a passé trois jours et trois nuits dans le ventre de "
  "l'énorme poisson, le Fils de l'homme passera trois jours et trois nuits au "
  "cœur de la terre. » (Mt 12:40)",
  "« Après trois jours je dois être relevé » — « fais garder la tombe jusqu'au "
  "troisième jour. » (Mt 27:63-64 — les pharisiens équivalent les deux !)",
  "« Jeûnez pour moi trois jours, nuit et jour ; puis j'entrerai chez le roi. » "
  "— « Le troisième jour, Esther se présenta. » (Est 4:16 - 5:1 — 72 heures "
  "impossibles : comput inclusif prouvé)",
 ],
 contexte=(
  "Jonas, fils d'Amitthaï (2 Rois 14:25 — le même Jonas, sous Jéroboam II, VIIIe "
  "siècle : historicité ancrée) : Jaffa → Tarsis (fuite vers l'ouest !), tempête, "
  "sort, « jetez-moi » (1:12 — le substitut volontaire), poisson assigné, prière "
  "du shéol, Ninive (trois jours de marche, 3:3 !), « encore quarante jours » "
  "(3:4), repentance — bêtes en sacs (3:7-8 !) — ricin (4:6-11 : pitié pour une "
  "plante contre 120 000 + bêtes !). Huit siècles plus tard, des pharisiens "
  "réclament un signe (Mt 12:38) : UN SEUL — Jonas."
 ),
 explication=(
  "« Assigna » (mana) : le poisson est convoqué. « Grand poisson » (dag gadol ; "
  "ketos en Mt 12:40 : monstre marin) — PAS « baleine » : espèce NON précisée "
  "(voir Limites). « Ventre du shéol » (2:2) : Jonas se dit MORT — flots, algues "
  "(2:3, 5 : noyade), « racines des montagnes » (2:6 : le fond), « tu as fait "
  "remonter ma vie » : lexique de résurrection. « Le salut est à Jéhovah » (2:9) : "
  "yeshoua — le cri de Jonas est le nom du Christ. Quarante jours (3:4) : le "
  "nombre de l'épreuve. Bêtes en sacs (3:7-8) : décret total — le bétail jeûne ! "
  "120 000 (4:11 : « sans distinguer droite et gauche » + « bêtes en grand "
  "nombre ») : Dieu compte le bétail ! « Plus que Jonas » (Mt 12:41) : les "
  "Ninivites jugeront « cette génération ». Le comput : « environ trois jours », "
  "« séjour s'étalant sur trois jours » (inclusif !) — vendredi 14 après-midi → "
  "sabbat 15 → dimanche 16 avant l'aube (Jn 20:1 : « ténèbres encore ») : trois "
  "jours civils, ~36-40 heures. Double preuve de l'inclusif : Esther (3 jours "
  "« nuit et jour » puis « le troisième jour ») et les pharisiens (« après trois "
  "jours » = « jusqu'au troisième jour »)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : Jonas HISTORIQUE — Jésus fonde le "
  "signe dessus ; si parabole, le signe s'effondre (argument interne, signalé). "
  "La résurrection « le troisième jour » (1Co 15:4 — le credo) = « après trois "
  "jours » (Mc 8:31) = « trois jours et trois nuits » (Mt 12:40) : trois "
  "formules, un comput — l'inclusif juif (« environ », « s'étalant sur »). "
  "Ninive repentante contre génération dure : le signe juge."
 ),
 accomplissement=[
  ("Début VIIIe s. av. n. è.", "Jonas sous Jéroboam II (2R 14:25) : fuite, poisson, Ninive"),
  ("« 40 jours »", "Ninive repent — hommes ET bêtes (Jon 3:5-10)"),
  ("Ven. 14 Nisan 33 (après-midi)", "Mort et mise au tombeau (voir D)"),
  ("Sam. 15 Nisan 33", "Sabbat : le tombeau gardé et scellé (Mt 27:62-66)"),
  ("Dim. 16 Nisan 33 (avant l'aube)", "« Le troisième jour » : relevé (voir F018, la gerbe)"),
 ],
 hist=(
  "2 Rois 14:25 : Jonas ancré sous Jéroboam II — pas un conte flottant. Ninive, "
  "« trois jours de marche » : le Grand Ninive (murailles + faubourgs — "
  "Kuyunjik et ses dépendances). Jaffa : le port de la fuite. Tarsis : l'ouest "
  "lointain — le bout du monde connu. Décret total (bêtes incluses) : plausible "
  "en pouvoir absolu antique. 120 000 : la population du Grand Ninive — ordre "
  "admis. Matthieu 27:62-66 : garde romaine + sceau — le 15 Nisan."
 ),
 geo=(
  "Jaffa → la mer (tempête !) → … Ninive (900 km à l'est, sur le Tigre) : le lieu "
  "où le poisson « vomit » N'est PAS précisé (voir Limites). Ninive : trois jours "
  "de traversée. L'est de Ninive (4:5) : Jonas attend sous son ricin. « Racines "
  "des montagnes » (2:6) : le fond marin — géographie du shéol."
 ),
 sci=(
  "Espèce : NON déterminée — ni baleine, ni requin-baleine, ni cachalot : « grand "
  "poisson » — la fiche refuse de trancher (voir Limites). Survie trois jours : "
  "miracle rapporté — « sans miracle, impossible » (dit, comme D012). Comput "
  "inclusif : double preuve indépendante (Esther ; les pharisiens). ~36-40 heures "
  "sur trois jours civils (vendredi partiel + sabbat + dimanche partiel) : "
  "reconstitution ordinaire, pas heure par heure (voir Limites)."
 ),
 limites=(
  "Espèce du poisson : non déterminée — « grand poisson », un point c'est tout. "
  "Lieu du « vomissement » : non précisé. Pas de reconstitution heure par heure : "
  "« environ trois jours ». Jonas 2 (prière) sans entrée au registre (C8). "
  "120 000 (enfants ? population ?) : « le texte dit ». Historicité : argument "
  "interne (Jésus), signalé comme tel."
 ),
 tl=[("VIIIe s.", "Jonas : poisson, Ninive"), ("40 jours", "Repentance + bêtes"), ("Ven. 14 (pm)", "Tombeau"),
     ("Sam. 15", "Garde, sceau"), ("Dim. 16 (aube)", "« Le 3e jour »")],
 src=[("Matthieu 12 — Bible d'étude, notes (signe de Jonas, ~3 jours)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/12"),
      ("Jonas 1 — Bible d'étude, notes (grand poisson, 3 j / 3 n)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/32/1"),
      ("Matthieu 28 — Bible d'étude, notes (premier jour, relevé)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/40/28"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_F019_jonas.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G001", titre="La vallée des ossements — 537, 1919, et l'image",
 ref="Ézéchiel 37 ; Ézéchiel 36:26-27 ; Révélation 11:11 (voir F016) ; Jérémie 30:9 ; Osée 3:5",
 statut="Accomplie (trois niveaux distingués)",
 cat="G", syst="Système 537/1919",
 reg="Registre : Ézéchiel — P358 (37:1-14), P359 (37:15-28), P583 (37:24-25)",
 texte=[
  "« La plaine était remplie d'ossements, très nombreux et TRÈS SECS. » "
  "(Éz 37:1-2 — morts depuis longtemps : pas de réanimation)",
  "« Fils d'homme, ces os revivront-ils ? — Ô Seigneur Jéhovah, TU LE SAIS. » "
  "(37:3 — le prophète s'abstient)",
  "« Prophétise : os, nerfs, chair, peau — mais pas de souffle. Puis : souffle "
  "des quatre vents — et ils vécurent, armée très nombreuse. » (37:4-10 — deux "
  "temps : comme Genèse 2:7, RE-CRÉATION)",
  "« Ces os, c'est toute la maison d'Israël : Nos os sont desséchés, notre "
  "attente a péri ! » (37:11 — le dicton des exilés)",
  "« J'ouvrirai vos tombeaux et je vous ramènerai sur votre sol ; mon serviteur "
  "David sera roi ; alliance de paix éternelle, mon sanctuaire au milieu, pour "
  "toujours. » (37:12-14, 24-28)",
 ],
 contexte=(
  "Tel-Abib, au Kébar (voir F013) : Ézéchiel, après le siège mimé (ch. 4) et la "
  "chute de la ville (ch. 33), entend le dicton des exilés — « attente péri » "
  "(Psaume 137 : « au bord des fleuves » !). Contexte immédiat : Ézéchiel 36 — "
  "« cœur de pierre → cœur de chair » (36:26-27 !). Arrière-plan : le schisme "
  "(~931 : Jéroboam, 1R 12) — quatre cents ans de division Nord/Sud à effacer. "
  "Transporté « en esprit » : vision, pas excursion (voir Limites)."
 ),
 explication=(
  "« Très secs » (meod yebeshot) : la vision EXCLUT le naturel — pas de restes "
  "frais. « Tu le sais » : humilité du prophète. Deux temps — corps PUIS souffle : "
  "l'ordre de Genèse 2:7 (poussière + souffle) : re-création. Quatre vents : de "
  "partout — la diaspora. « Armée très nombreuse » (chayil gadol meod) : les morts "
  "deviennent soldats. « TOUTE la maison » : pas Juda seul. CLÉ : les tombeaux, "
  "c'est l'EXIL — « sortir de vos tombeaux » = « ramener sur le sol » (37:12-14, "
  "21) : la vision PARLE résurrection pour DIRE retour. « Mon esprit en vous » "
  "(37:14) : comme 36:27. Deux bâtons (Juda + Joseph/Éphraïm → UN, 37:15-22) : "
  "« plus deux nations » (37:22) — le schisme effacé. « David » (37:24) : mort "
  "depuis 400 ans — le Messie ! (cf. Jr 30:9, Os 3:5). Alliance de paix "
  "ÉTERNELLE, sanctuaire AU MILIEU « pour toujours » (37:26-28) : les nations "
  "« sauront » (37:28)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah distingue TROIS niveaux — jamais "
  "confondus : (1) 537 : le retour littéral (voir B002) — tombeaux = exil, sol = "
  "Canaan ; (2) 1919 : la restauration spirituelle — AVEC Révélation 11:11 "
  "(voir F016 : « accomplissement moderne frappant en 1919 ») : ossements ranimés "
  "= le reste ; (3) la résurrection : l'IMAGE, pas l'événement — la vision "
  "illustre avec le vocabulaire de la résurrection (qui est promise ailleurs : "
  "Dn 12:2, voir E008 et G004). Trois niveaux, une vision — la fiche refuse "
  "le mélange."
 ),
 accomplissement=[
  ("Exil (~607-537 av. n. è.)", "« Notre attente a péri » (37:11 ; Ps 137)"),
  ("537 av. n. è.", "Tombeaux ouverts : le retour (voir B002)"),
  ("1919 de n. è.", "Restauration : avec Ré 11:11 (voir F016)"),
  ("29 de n. è. +", "« David » : le Messie (voir C)"),
  ("Avenir", "Sanctuaire au milieu, pour toujours (voir G005)"),
 ],
 hist=(
  "L'exil : désespoir documenté (Ps 137 — « comment chanter ? »). 537 : Cyrus "
  "(voir B002, E005-E006). Le schisme (~931-537) : quatre siècles (Jéroboam : "
  "1R 12 — veaux d'or !). 1919 : 26 mars (libération) + septembre (Cedar Point : "
  "« Annoncez le Roi » — voir F016, E008). « David leur roi » : même langage "
  "en Jérémie 30:9 et Osée 3:5 — trois prophètes, un Messie."
 ),
 geo=(
  "La plaine (biq'a) : NON localisée — lieu visionnaire, pas de GPS (voir "
  "Limites). Tel-Abib : le prophète voit depuis l'exil (voir F013). « Votre sol » "
  "(37:12, 14, 21) : Canaan — le retour est GÉOGRAPHIQUE. Deux bâtons : la carte "
  "réunifiée — Juda (sud) + Joseph (nord) : le schisme effacé sur la carte."
 ),
 sci=(
  "« Très secs » : taphonomie — ossements anciens, pas de restes frais : le texte "
  "lui-même exclut la réanimation naturelle. Deux temps : squelette → tissus → "
  "souffle — ordre de reconstitution + animation (cf. Gn 2:7). Quatre vents : "
  "météorologie de la totalité — le souffle vient de partout, comme les exilés."
 ),
 limites=(
  "La plaine n'est pas localisée : vision, pas excursion. Les trois niveaux "
  "(537, 1919, image) sont distingués — la fiche refuse le mélange. 1919 : détail "
  "renvoyé (F016 + publications). « David » = Messie : compréhension citée. "
  "Sanctuaire éternel : voir G005 — pas anticipé ici."
 ),
 tl=[("Exil", "« Attente péri »"), ("537", "Tombeaux : retour"), ("1919", "+ Ré 11 : ranimés"),
     ("29 +", "« David » : Messie"), ("Avenir", "Sanctuaire, toujours")],
 src=[("Ézéchiel 37 — Bible d'étude, notes (ossements, deux bâtons)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/37"),
      ("Ézéchiel 36 — Bible d'étude, notes (cœur nouveau, contexte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/26/36"),
      ("Révélation 11 — Bible d'étude, notes (ranimés, 1919, voir F016)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/11"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_G001_ossements.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G002", titre="L'alliance nouvelle — la loi au cœur, le sang pour sceau",
 ref="Jérémie 31:31-40 ; Luc 22:20 ; 1 Corinthiens 11:25 ; Hébreux 8:8-13 ; 9:15",
 statut="Accomplie",
 cat="G", syst="Système 33/36/70",
 reg="Registre : Jérémie — P237-P245 (31:1-40) ; Hébreux — P768 (8:6-13), P769 (9:11-12)",
 texte=[
  "« Des jours viennent où je conclurai avec Israël et Juda une alliance "
  "nouvelle — PAS COMME celle que j'ai conclue avec leurs ancêtres, qu'ils ont "
  "rompue. » (Jr 31:31-32 — rupture, pas réparation)",
  "« Je mettrai ma loi au-dedans d'eux, dans leur cœur je l'écrirai ; tous me "
  "connaîtront, du petit au grand ; je ne me souviendrai plus de leur péché. » "
  "(31:33-34)",
  "« Si le soleil, la lune et les étoiles s'écartent, alors Israël cessera. » "
  "(31:35-37 — garantie COSMIQUE)",
  "« Cette coupe signifie la nouvelle alliance en vertu de mon sang. » "
  "(Lc 22:20 ; 1Co 11:25 — 14 Nisan 33)",
  "« En disant “nouvelle”, il a rendu la première DÉSÈTE — près de disparaître. » "
  "(Hé 8:13 — écrit ~61, AVANT 70)",
 ],
 contexte=(
  "Jérémie, en plein siège (~607) : il ACHÈTE un champ pendant le siège "
  "(ch. 32 — 17 sicles !) — la foi en actes sous les béliers. « Des jours "
  "viennent » (31) : futur — l'ancienne est ROMPUE (« qu'ils ont rompue », 31:32 : "
  "constat). Cène, 14 Nisan 33 : la coupe « après le repas » (1Co 11:25) — une "
  "coupe de Pâque DÉTOURNÉE vers l'alliance. Hébreux (~61) : « près de disparaître » "
  "— neuf ans avant Titus (voir B007)."
 ),
 explication=(
  "« Pas comme » : rupture — pas une rustine. Pierre → cœur (31:33 ; 2Co 3:3 : "
  "« tables de chair » !) : intériorisation. « Tous me connaîtront » (31:34) : "
  "fin des castes religieuses — du petit au grand. « Je ne me souviendrai plus » : "
  "l'amnésie DIVINE — pardonner = oublier : Dieu s'engage (anthropomorphisme "
  "signalé, voir Limites). Soleil-lune-étoiles (31:35-37) : SI l'astronomie "
  "s'arrête, ALORS… — garantie falsifiable en principe ! Ville rebâtie (31:38-40 : "
  "Hananel et la topographie — « sainte pour Jéhovah » ; détail : voir B006). "
  "« En vertu de mon sang » : le sceau est le SANG — comme Exode 24:8 (« sang de "
  "l'alliance » !). « Désuète » (palaioo : vieillie, obsolète — en 61, avant 70 : "
  "Hébreux date Titus !). Médiateur (Hé 9:15 ; 1Tm 2:5 : « un seul » — Moïse → "
  "Jésus). « Ceux qui sont appelés » (9:15) : les oints (144 000) — et la grande "
  "foule (Ré 7:9-10 ; Za 8:23 : « dix hommes saisiront le pan » !) : elle OBSERVE "
  "sans être dedans (« même loi pour l'étranger » : Lv 24:22, Nb 15:15)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : à la Cène, la prophétie « se "
  "réalisait » — pardon + nation SPIRITUELLE (1P 2:9 : « nation sainte » ; Rm 2:28-29 : "
  "« Juif au-dedans » !). La loi du Christ : pas de code écrit — « Jésus n'a "
  "jamais rédigé la moindre loi » — l'amour comme loi (Rm 13:10), « loi d'un "
  "peuple libre » (Jc 1:25), écrite sur le cœur (1P 4:8). Paul reprend Jérémie "
  "31 EN ENTIER (Hé 8:8-12, 10:16-17) : la plus longue citation de l'Ancien "
  "Testament dans le Nouveau."
 ),
 accomplissement=[
  ("~607 av. n. è.", "Siège : Jérémie promet (et achète un champ, ch. 32)"),
  ("14 Nisan 33", "La Cène : « en vertu de mon sang »"),
  ("Pentecôte 33", "L'esprit : la loi AU CŒUR (voir F018) — 3 000"),
  ("36 de n. è.", "Corneille : les nations ENTRÉES (voir C012)"),
  ("~61 de n. è.", "Hébreux : « désuète, près de disparaître »"),
  ("70 de n. è.", "Le Temple : l'ancienne enterrée (voir B007)"),
 ],
 hist=(
  "Jérémie 32 : champ acheté en plein siège (17 sicles, acte scellé !) — le "
  "contexte-foi de la promesse. La Cène : coupe pascale détournée — « après le "
  "repas ». Pentecôte : 3 000 — « tous connaîtront » commence. Zacharie 8:23 "
  "(« dix hommes… un Juif » — dix = totalité : les nations). 70 : le système "
  "lévitique enterré — Hébreux 8:13 accompli."
 ),
 geo=(
  "Jérusalem : assiégée (Jr 32) PUIS rebâtie (31:38-40 — Hananel, topographie). "
  "La chambre haute (« grande chambre garnie », Mc 14:15) : la Cène. Sinaï "
  "(ancienne : Ex 24:8, sang !) contre Sion (nouvelle : Hé 12:22, « Sion "
  "céleste » !). Les nations (« toutes langues », Za 8:23) : l'alliance "
  "déborde."
 ),
 sci=(
  "« Au-dedans » : langage pastoral — intériorisation contre tablettes : la loi "
  "INCARNÉE (pas de neurologie ici — voir Limites). Soleil-lune-étoiles : garantie "
  "falsifiable en principe — SI… ALORS. « Désuète » en ~61 : datation relative — "
  "Hébreux, écrit avant 70, date Titus par anticipation."
 ),
 limites=(
  "« Ne plus se souvenir » : anthropomorphisme — signalé. Oints / grande foule : "
  "distinction citée comme compréhension. Langage pastoral, pas neurologique. "
  "Ville (31:38-40) : détail topographique à B006. Jérémie 33 (David) : pas "
  "développé — renvoi."
 ),
 tl=[("~607", "Siège : promesse + champ"), ("14 Nisan 33", "Cène : sang"), ("Pentecôte 33", "Cœur : 3 000"),
     ("36", "Nations"), ("~61", "« Désuète »"), ("70", "Enterrée")],
 src=[("La loi du Christ (Jr 31:31-34, loi au cœur, foule)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996643"),
      ("Jérémie — livre n° 24 (alliance nouvelle, Cène, Paul)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990085"),
      ("Jérémie 31 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/30/31"),
      ("Hébreux 8 — Bible d'étude, notes (Jr 31 cité, désuète)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/58/8")],
 img="images/prophe_G002_alliance.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G003", titre="Le paradis d'Ésaïe — le loup hôte de l'agneau",
 ref="Ésaïe 11:1-9 ; Ésaïe 35 ; Ésaïe 65:17-25 ; Michée 4:4 ; Luc 23:43",
 statut="En cours (plénitude : millénium, voir F017)",
 cat="G", syst="Système 33 · millénium (renvoi F017)",
 reg="Registre : Isaïe — P123-P125, P579 (11:1-16), P152, P604 (35:1-10), P179 (65:17-25)",
 texte=[
  "« Un rejeton sortira de la souche de Jessé. » (Is 11:1 — de la souche : "
  "comme F010 !)",
  "« Le loup résidera TEMPORAIREMENT avec l'agneau ; un petit garçon sera leur "
  "conducteur ; il ne se fera ni tort ni dommage ; la terre sera remplie de la "
  "connaissance de Jéhovah. » (Is 11:6-9 — gour : séjourner — « l'HÔTE » !)",
  "« Le désert fleurira comme le crocus ; alors les aveugles verront, les sourds "
  "entendront, le boiteux bondira. » (Is 35:1-6 — voir C010 pour le 1er temps !)",
  "« Ils bâtiront des maisons et les habiteront ; ils planteront des vignes ; "
  "ils ne travailleront pas en vain ; le lion mangera de la paille. » "
  "(Is 65:21-25)",
  "« L'enfant mourra centenaire ; le pécheur de cent ans sera maudit. » "
  "(Is 65:20 — à cent ans, le péché sera un choix)",
 ],
 contexte=(
  "Ésaïe, VIIIe siècle (Achaz, Ézéchias — sous la menace assyrienne, 701 !) : "
  "il voit le paradis SOUS LES BÉLIERS. Chapitre 11 : après « la forêt abattue » "
  "(10:34) — de la souche, le rejeton (Jessé, pas David : l'humble origine — "
  "Bethléem, voir C001 !). Chapitre 35 : après Édom jugée (ch. 34) — « la route "
  "sainte » (35:8 : « les insensés n'erreront pas » — impossible de se perdre !). "
  "Chapitre 65 : après « déchire les cieux » (64) — la réponse : « me voici » "
  "(65:1 !)."
 ),
 explication=(
  "Sept esprits (11:2 : 1 + 6 — plénitude : « reposera », nûach !). « Pas selon "
  "les yeux » (11:3-4) : justice non apparente — « il frappera par le souffle ». "
  "« TEMPORAIREMENT » (11:6, gour : séjourner — Maredsous : « le loup sera l'HÔTE "
  "de l'agneau » !) : invité, pas colocataire — les deux traductions données. "
  "Le loup sous protection de l'AGNEAU : le contraste avec aujourd'hui. Petit "
  "garçon conducteur (11:6) : l'enfant mène les fauves — inversion. « Ni tort » "
  "(11:9, yarea : mal — ZÉRO). « Remplie de connaissance » (11:9 : « comme les "
  "eaux couvrent la mer » — totalité !). Crocus (35:1 : chavatseleth — floraison "
  "du désert : phénomène RÉEL !). Aveugles-sourds-boiteux (35:5-6) : C010 "
  "(ministère, 1er temps) + paradis (plénitude) — deux temps distingués ! "
  "Centenaire (65:20) : mort possible = test final (Satan délié — voir F017) — à "
  "100 ans, pécher sera choisir. Maisons-vignes (65:21-22 : « comme les jours "
  "d'un arbre » — longévité végétale ! « pas pour autrui » : fin des spoliations "
  "— Mi 4:4 : « chacun sous sa vigne » !). « Pas en vain… pas pour périr » (65:23) : "
  "travail fructueux, enfants vivants. Lion-paille (65:25) : carnivore → herbivore "
  "— « mangeront de l'herbe » ! Serpent-poussière (65:25) : Genèse 3:14 MAINTENU — "
  "humilié encore : malédiction partielle qui demeure."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : DEUX temps — MAINTENANT spirituel "
  "(la paix du peuple de Dieu : loup-agneau HUMAIN) et paradis LITTÉRAL ensuite "
  "(les animaux : « mangeront de l'herbe » — un lion pour compagnon !). La terre "
  "SUBSISTE : le déluge a pris les occupants, pas la planète — Harmaguédon "
  "pareil. Paradis TERRESTRE (Lc 23:43 — le premier était terrestre, le nouveau "
  "aussi). Air pur, eau fraîche, nourriture (« personne affamé »), « parc » "
  "(gan : Éden retrouvé — oiseaux, bêtes, arbres, fleurs !). Prière exaucée : "
  "« sur la terre » (Mt 6:10)."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe : le paradis promis sous la menace (701)"),
  ("29-33 de n. è.", "Is 35:5-6 : le 1er temps — C010 (aveugles, sourds, boiteux)"),
  ("Maintenant", "Le temps spirituel : la paix du peuple (loup-agneau humain)"),
  ("Millénium", "Le temps littéral : « mangeront de l'herbe » (voir F017)"),
  ("« Ni tort »", "Plénitude : voir G005"),
 ],
 hist=(
  "Achaz, Ézéchias, Sennachérib (VIIIe s.) : le paradis est promis pendant le "
  "siège — l'espoir sous les béliers. C010 (29-33) : le premier temps — aveugles "
  "et sourds guéris. Maredsous (« l'hôte ») : traduction citée pour gour. "
  "Luc 23:43 (« avec moi au paradis ») : le paradis terrestre promis au poteau — "
  "voir D."
 ),
 geo=(
  "Liban → désert (35:2 : « gloire du Liban… Carmel et Saron ») : le désert devient "
  "jardin. « Route sainte » (35:8) : Sion — le pèlerinage final, sans égarement. "
  "« Toute ma montagne sainte » (11:9, 65:25) : Sion ÉTENDUE à la terre. Maisons "
  "et vignes (65:21) : Canaan retrouvé — « chacun sous sa vigne » (Mi 4:4)."
 ),
 sci=(
  "« Sauvages mais non féroces » : l'Éden — à l'écart, pas colocataires : "
  "éthologie du paradis. « Mangeront de l'herbe » : physiologie transformée — "
  "miracle rapporté, mécanisme NON expliqué (voir Limites). Crocus du désert : "
  "floraison après pluie — phénomène réel, image vraie. « Jours d'un arbre » : "
  "séquoias millénaires — longévité végétale réelle. Centenaire : gérontologie "
  "inversée — « l'enfant » de cent ans."
 ),
 limites=(
  "Deux temps DISTINGUÉS : spirituel maintenant, littéral ensuite — jamais "
  "confondus. Mécanisme : miracle rapporté, pas expliqué. « Temporairement » "
  "(gour) : les deux traductions données. Cent ans : test final — voir F017, pas "
  "développé. Serpent (Gn 3:14 maintenu) : signalé."
 ),
 tl=[("VIIIe s.", "Promis sous les béliers"), ("29-33", "C010 : 1er temps"), ("Maintenant", "Spirituel"),
     ("Millénium", "Littéral : herbe !"), ("« Ni tort »", "G005")],
 src=[("Le loup hôte de l'agneau (gour, Questions des lecteurs)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1991688"),
      ("Tu seras avec moi au Paradis (Is 11, paradis terrestre)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101971144"),
      ("L'espoir d'une nouvelle terre (Is 65, terre subsiste)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1954720"),
      ("Ésaïe 11 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/23/11")],
 img="images/prophe_G003_paradis.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G004", titre="Ils se réveilleront — neuf types, vingt milliards de places",
 ref="Jean 5:28-29 ; Actes 24:15 ; Ésaïe 25:8 ; 26:19 ; Osée 13:14 ; 1 Corinthiens 15 ; 1 Thessaloniciens 4:16",
 statut="À venir (types accomplis ; 1re céleste « en cours »)",
 cat="G", syst="Système 33/1914 · millénium (F017)",
 reg="Registre : Jean — P995 (5:28-29) ; Ac 24:15 sans entrée (C8) ; 1Co — P734-P738 (ch. 15) ; Is — P141 (25:1-12), P142 (26:1-19) ; 1Th — P752 (4:15-16), P753 (4:17)",
 texte=[
  "« L'heure vient où TOUS ceux qui sont dans les tombeaux commémoratifs "
  "entendront sa voix et sortiront — vie, ou jugement. » (Jn 5:28-29 — mnemeion : "
  "MÉMOIRE !)",
  "« Il va y avoir une résurrection tant des JUSTES que des INJUSTES. » "
  "(Ac 24:15 — Paul, au tribunal de Félix !)",
  "« Tes morts vivront ; la rosée LUMINEUSE les fera revivre. » (Is 26:19 — "
  "tal orot !)",
  "« Il ENGLOUTIRA la mort ; il essuiera les larmes. » (Is 25:8 — bila : avaler ! "
  "— cité en 1Co 15:54)",
  "« Ô mort, où sont tes aiguillons ? » (Os 13:14 — cité en 1Co 15:55 — "
  "la mort DÉSARMÉE)",
  "« Christ PRÉMICES, puis les siens à sa présence ; le DERNIER ennemi, la mort ; "
  "Dieu TOUT EN TOUS. » (1Co 15:20-28 — voir F018, F017)",
 ],
 contexte=(
  "Jésus DEVANT les Juifs (Jn 5, après Bethesda — « mon Père agit, j'agis », 5:17 : "
  "le sabbat contesté !). Paul DEVANT Félix (Ac 24:10-15 — procès : « j'adore… "
  "je crois… j'espère » — l'espérance au TRIBUNAL !). Corinthe (~55 : « certains "
  "disent : pas de résurrection », 15:12 — le scepticisme grec !). Thessalonique "
  "(~50 : « ceux qui dorment », 4:13 — le deuil !). Ésaïe (VIIIe s. : « TON peuple », "
  "26:19). Daniel (12:2 — voir E008). Partout : la mort contredite."
 ),
 explication=(
  "« Tombeaux commémoratifs » : mnemeion — MÉMOIRE : les morts sont des souvenirs "
  "de Dieu. « Tous » — SAUF la Géhenne (péchés impardonnables, Mt 12:32 : effacé "
  "= pas de souvenir = pas de résurrection — jamais de liste nominative !). "
  "« Jugement » (krisis) : PAS condamnation — période millénaire d'évaluation "
  "(voir F017 !). « Injustes » (adikoi) : les IGNORANTS — pas les méchants : "
  "miséricorde ! « Rosée lumineuse » (tal orot) : la rosée RESSUSCITE. « Engloutira » "
  "(bila) : la mort AVALÉE — + « essuiera les larmes » : Ésaïe 25:8, c'est "
  "Révélation 21:4 AVANT (voir G005 !). « Aiguillons » : le dard (scorpion ?) — "
  "« où ton dard ? » : désarmée. « Prémices » (1Co 15:20, 23 — voir F018, la gerbe "
  "du 16 !) : ORDRE — Christ, puis les siens « à sa présence », puis la fin. "
  "« Dernier ennemi » (15:26) : la mort meurt en DERNIER (voir F017, Ré 20:14). "
  "« Mystère » (15:51) : « nous ne dormirons pas tous » — les vivants CHANGÉS "
  "(« en un instant » — physique non décrite, voir Limites). « Voix d'archange » "
  "(1Th 4:16) : Mikaël = Jésus (voir E008) — l'archange RESSUSCITE. Vingt milliards "
  "(estimation LARGE des humains vécus) : tous ne ressusciteront pas — et la terre "
  "entière les loge (150 M km² : ~133/km² — la fiche CALCULE !). Mer + hadès "
  "(Ré 20:13) : rendent — noyés et enterrés : AUCUN perdu."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : NEUF résurrections-types avant Jésus — "
  "Sarepta (1R 17 !), Sunamite (2R 4 !), ossements d'Élisée (2R 13:21 !), Jaïrus "
  "(Mc 5 !), Naïn (Lc 7 !), Lazare (Jn 11 !), Tabitha (Ac 9 !), Eutychus (Ac 20 !), "
  "saints de Jérusalem (Mt 27:52-53 !) — Jésus « prémices », à part. Terrestre "
  "(justes + injustes-ignorants, pendant le millénium — voir F017) ; céleste "
  "(première : 144 000 — « EN COURS » !). Impartial + miséricorde : « on ne sait pas "
  "toujours QUI — Dieu sait » (humilité citée)."
 ),
 accomplissement=[
  ("IXe-VIIIe s. av. n. è.", "3 types : Sarepta, Sunamite (« 7 éternuements » !), ossements"),
  ("29-33 de n. è.", "3 types : Jaïrus, Naïn (« jeune homme, lève-toi »), Lazare (« 4 jours » !)"),
  ("16 Nisan 33", "Jésus : PRÉMICES (voir F018) — + les saints (Mt 27:52-53)"),
  ("36 + de n. è.", "2 types : Tabitha (Joppé), Eutychus (« 3e étage » !)"),
  ("1914 + de n. è.", "Première céleste : « en cours »"),
  ("Millénium", "Terrestre : « tous » (voir F017) — mer et hadès rendent"),
 ],
 hist=(
  "Sarepta (Phénicie !) : une PAÏENNE ressuscitée — avant Israël. Sunamite : "
  "« l'enfant éternue sept fois » (2R 4:35 — détail !). Ossements (2R 13:21) : un "
  "mort TOUCHE Élisée et VIT — posthume ! Naïn : devant la porte — « jeune homme, "
  "lève-toi » (Lc 7:14). Lazare : « quatre jours », « il sent » (Jn 11:39 — "
  "décomposition COMMENCÉE : irréversible naturellement !). Saints (Mt 27:52-53 : "
  "« après SA résurrection » — Jérusalem !). Eutychus : troisième étage, Paul "
  "prêche longuement (Ac 20:9 — détail humain !)."
 ),
 geo=(
  "Sarepta (nord-ouest, Phénicie) → Sunem (Jezréel) → Naïn (Galilée) → Béthanie "
  "(Lazare, près de Jérusalem) → Joppé (Tabitha) → Troas (Eutychus, Asie) : six "
  "lieux, neuf types. « La mer » (Ré 20:13) : les noyés rendus. La terre ENTIÈRE : "
  "les vingt milliards logés — ~133 au km² : faisable."
 ),
 sci=(
  "« Quatre jours » (Lazare) : rigor + décomposition — irréversible : miracle "
  "rapporté, pas expliqué (dit !). Ossements (2R 13:21) : contact = vie — PAS de "
  "mécanisme (dit !). Vingt milliards / 150 M km² ≈ 133/km² : le calcul tient — "
  "la place ne manque pas. « Changés en un instant » (1Co 15:51-52) : physique "
  "non décrite (voir Limites)."
 ),
 limites=(
  "Actes 24:15 sans entrée au registre (C8). QUI sera ressuscité : pas toujours "
  "su — humilité citée, jamais de liste (Géhenne : pas de noms !). Mécanismes : "
  "miracles rapportés, pas expliqués. « Changés » : physique non décrite. Neuf : "
  "le compte de l'article — suivi."
 ),
 tl=[("IXe-VIIIe s.", "3 types (AT)"), ("29-33", "3 types + saints"), ("16 Nisan 33", "PRÉMICES"),
     ("36 +", "2 types"), ("1914 +", "1re : en cours"), ("Millénium", "« Tous »")],
 src=[("Qui ressuscitera sur la terre ? (Jn 5, Ac 24, 20 milliards)", "https://wol.jw.org/fr/wol/pc/r30/lp-f/1200020044/603/0"),
      ("La première résurrection est en cours ! (neuf types)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2007006"),
      ("Jean 5 — Bible d'étude, notes (tombeaux, vie, jugement)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/43/5"),
      ("Actes 24 — Bible d'étude, notes (justes et injustes)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/44/24")],
 img="images/prophe_G004_resurrection.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="G005", titre="Toutes choses nouvelles — le ciel et la terre renouvelés",
 ref="Ésaïe 65:17 ; 66:22 ; 2 Pierre 3:7-13 ; Révélation 21:1-8 ; Matthieu 6:10 ; Genèse 1:28",
 statut="À venir (sans date)",
 cat="G", syst="Système 64/96 · millénium (F017)",
 reg="Registre : Révélation — P945-P949 (21:1-7) ; 2 Pierre — P786 (3:13) ; Isaïe — P179 (65:17-25)",
 texte=[
  "« Je crée de nouveaux cieux et une nouvelle terre ; on ne se souviendra plus "
  "des choses passées. » (Is 65:17 — amnésie du mal : comme Jr 31:34, voir G002 !)",
  "« Les cieux et la terre de maintenant sont RÉSERVÉS POUR LE FEU. » "
  "(2P 3:7 — symbolique : le système !)",
  "« Nous attendons de nouveaux cieux et une nouvelle terre. » (2P 3:13 — "
  "prosdokao : attente ACTIVE)",
  "« Nouveau ciel, nouvelle terre ; la mer N'EST PLUS ; la Nouvelle Jérusalem "
  "DESCEND ; la tente de Dieu AVEC les humains. » (Ré 21:1-3 — Dieu vient ICI)",
  "« Il essuiera toute larme ; plus de mort, plus de deuil, plus de cri, plus "
  "de douleur. » (Ré 21:4 — cinq fléaux effacés — PROGRESSIVEMENT)",
  "« Voici, je fais TOUTES CHOSES nouvelles. Écris : fidèles et vraies. » "
  "(Ré 21:5 — graphson : ORDRE d'écrire + sceau)",
 ],
 contexte=(
  "Ésaïe (fin du livre, 65-66 — après « déchire les cieux », 64 !). Pierre (~64 : "
  "les moqueurs — « où est sa présence ? depuis que les pères dorment », 3:4 — "
  "DÉJÀ au Ier siècle ! Réponse : le déluge (3:5-6), « mille ans » (3:8), et "
  "« Dieu ne tarde pas : il PATIENTE, ne voulant qu'aucun périsse » (3:9 — le "
  "retard comme miséricorde !). Jean (~96 : APRÈS le millénium du ch. 20 — voir "
  "F017 — chapitres 21-22 : L'APRÈS). « Les choses anciennes ont disparu » (21:4 : "
  "parelthen — PASSÉES)."
 ),
 explication=(
  "« Nouveaux » (kainos) : qualité NEUVE — pas neos (temps) : RENOUVELÉS, pas "
  "remplacés — la terre SUBSISTE (voir G003) ! « On ne se souviendra plus » "
  "(Is 65:17) : le pardon COSMIQUE — comme Jr 31:34 (voir G002). « Réservés pour "
  "le feu » (2P 3:7) : SYMBOLIQUE — le déluge (eau RÉELLE) a détruit le MONDE "
  "méchant (kosmos !), pas la planète — le feu : pareil. « Éléments fondus » "
  "(stoicheia, 3:10 : gouvernements ? systèmes ? — « fondus » : dissous — sens "
  "précis renvoyé, voir Limites). « Nous attendons » (3:13) : ACTIVE — pas passive. "
  "« La mer n'est plus » (21:1) : la mer = masses agitées (Is 17:12, voir E002 !) — "
  "PLUS d'agitation : symbolique (pas d'océanographie — voir Limites !). L'Épouse "
  "(21:2, 9 : Nouvelle Jérusalem = les 144 000 — « parée » : mariage — ville-ÉPOUSE : "
  "un peuple !). « Tente AVEC » (skene, 21:3 : TABERNACLE — Ex 25:8, « j'habiterai » "
  "— Dieu campe AVEC NOUS !). Cinq fléaux (21:4 : larme, mort, deuil, cri, douleur) : "
  "effacés PROGRESSIVEMENT pendant le millénium — pas d'un coup ! « Écris » (21:5) : "
  "ordre + « fidèles et vraies » : le sceau. Seconde mort (21:8) : les LÂCHES en "
  "tête (deilia — contexte : persécutions romaines, renier ou mourir !) et « TOUS "
  "les menteurs » en queue (le mensonge = Satan, Jn 8:44 !)."
 ),
 interpretation=(
  "La compréhension des Témoins de Jéhovah : nouveau CIEL (le Royaume céleste : "
  "Jésus + 144 000) + nouvelle TERRE (la société humaine juste) — PAS une nouvelle "
  "planète. Les larmes : tendresse — « Dieu se soucie tendrement » de qui pleure. "
  "La mort adamique : disparaît — perfection + pardon (« l'Agneau »). Le mandat "
  "restauré (Gn 1:28 : « soumettez » — voir G003). La prière exaucée (« SUR LA "
  "TERRE », Mt 6:10). L'écologie divine (« ruine de ceux qui ruinent la terre », "
  "Ré 11:18 !). « Source de l'eau de la vie » (21:6 : GRATUITE !) — et 21:8 : la "
  "seconde mort pour qui refuse."
 ),
 accomplissement=[
  ("VIIIe s. av. n. è.", "Ésaïe 65-66 : nouveaux cieux promis"),
  ("~64 de n. è.", "2 Pierre 3 : les moqueurs réfutés (déluge, patience)"),
  ("~96 de n. è.", "Révélation 21 : la vision de l'APRÈS"),
  ("Millénium", "Effacement PROGRESSIF des cinq fléaux (voir F017)"),
  ("« Toutes nouvelles »", "La tente AVEC les humains (21:3-5)"),
 ],
 hist=(
  "Les moqueurs (2P 3:4 : « depuis que les pères dorment » — Ier siècle : déjà !). "
  "Le déluge (3:5-6 : « le monde d'alors périt » — kosmos : MONDE, pas planète : "
  "le précédent !). « Patience » (3:9 : « ne voulant qu'aucun périsse » — le retard "
  "= miséricorde). Harmaguédon : la terre SUBSISTE (voir G003). « Lâches » (21:8) : "
  "persécutions romaines — renier ou mourir : le contexte du Ier siècle."
 ),
 geo=(
  "Jérusalem DESCEND (21:2 : ciel → terre — Dieu vient ICI, pas l'inverse !). "
  "« Tente » : le tabernacle — l'Exode (Nb 2 : Dieu campe) — AVEC nous. La montagne "
  "(21:10 : « grande et haute » — le point de vue !). Les nations (21:24, 26 : "
  "« marcheront à sa lumière » — les nations ENTRENT !). Fleuve et arbres (22:1-2 : "
  "« feuilles pour la GUÉRISON des nations » — pharmacie paradisiaque !)."
 ),
 sci=(
  "Kainos contre neos : linguistique — renouvelé, pas remplacé : la terre RESTE "
  "(voir G003). « Éléments fondus » : PAS de physique — symbolique (voir Limites : "
  "pas de thermodynamique !). Cinq fléaux : psychologie du deuil — effacés "
  "PROGRESSIVEMENT : santé mentale restaurée. « Plus de mer » : symbolique — pas "
  "d'océanographie (dit !)."
 ),
 limites=(
  "« Éléments » (stoicheia) : sens précis renvoyé aux publications. « Mer » : "
  "symbolique — pas d'océanographie. Alpha et Oméga (21:6) : attribution NON "
  "débattue ici (règle 7 — question disputée). Ville-cube (21:16, 12 000 stades) : "
  "renvoi à la catégorie I. « Lâches » : pas de chasse — JAMAIS de liste."
 ),
 tl=[("VIIIe s.", "Is 65-66"), ("~64", "2P 3 : moqueurs"), ("~96", "Ré 21 : vision"),
     ("Millénium", "Progressif : 5 fléaux"), ("« Toutes nouvelles »", "Tente AVEC")],
 src=[("Révélation 21:4 : Il essuiera toutes les larmes (expliqué)", "https://wol.jw.org/fr/wol/d/r30/lp-f/502300154"),
      ("Un nouvel ordre : nouveau ciel, nouvelle terre (progressif)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101963030"),
      ("Révélation 21 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/66/21"),
      ("Prophéties — tableau des accomplissements", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101965112")],
 img="images/prophe_G005_nouveauciel.jpg",
))
