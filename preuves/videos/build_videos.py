#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAGUE 5 — VIDÉOS (préparation)
Génère, sans aucune ressource externe :
  1. SCRIPTS_VIDEOS.html    — fiche technique + 10 scripts courts + 3 scripts longs, plan par plan
                              (temps · cadrage · action · texte à l'écran · voix off · son · limite honnête)
  2. STORYBOARDS.html       — une planche A4 par vidéo : vignettes 9:16, lignes de tiers, légendes
  3. LISTE_PLANS_A_GENERER.md — un prompt prêt à l'emploi par plan (fichier cible : plans/vNN_pNN.jpg)
Aucune vidéo n'est fabriquée ici : on prépare le tournage. Les textes citent des références bibliques
et renvoient aux sites officiels ; aucun contenu de publication n'est recopié.
"""
import os, html, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_SCRIPTS = os.path.join(HERE, 'SCRIPTS_VIDEOS.html')
OUT_STORY = os.path.join(HERE, 'STORYBOARDS.html')
OUT_PLANS = os.path.join(HERE, 'LISTE_PLANS_A_GENERER.md')

def esc(t): return html.escape(str(t), quote=False)

# --------------------------------------------------------------------- DONNÉES
FICHE = [
 ("Format", "9:16 vertical — 1080 × 1920 px — 30 images/s — H.264 / MP4"),
 ("Durées", "courts : 30 à 40 s · longs : 2 à 3 min · accroche obligatoire dans les 3 premières secondes"),
 ("Zones sûres", "texte et sous-titres dans le tiers central : 12 % de marge en haut, 20 % en bas (interface des applications)"),
 ("Texte à l'écran", "six mots maximum par carton, majuscules, contraste fort, jamais de paragraphe"),
 ("Sous-titres", "incrustés, police lisible, une à deux lignes, jamais au-dessus de la zone basse"),
 ("Son", "nappe sonore fabriquée ou libre de droits ; voix off française posée ; aucun extrait musical protégé"),
 ("Images", "aucun visage identifiable, aucun logo, aucune marque, aucun document réel filmé de près"),
 ("Contenus", "aucune citation de publication à l'écran ; les références bibliques et les liens officiels sont donnés"),
 ("Fin de vidéo", "dernier carton : la question qui ouvre et la mention jw.org · jamais de slogan, jamais d'appel à s'abonner"),
 ("Usage", "privé : montre à une personne, une fois, dans une conversation ; aucun dépôt public, aucune diffusion"),
]
LIMITE_GEN = ("Aucun total dogmatique ; aucune date pour l'avenir ; un seul système chronologique par vidéo, la divergence "
              "profane étant signalée à l'écrit quand elle existe ; aucune image ne remplace une publication.")

V = []
def video(code, titre, duree, refs, accroche, son, limite, plans):
    V.append(dict(code=code, titre=titre, duree=duree, refs=refs, accroche=accroche, son=son, limite=limite, plans=plans))

# ---------------------------------------------------------------- 10 COURTS
video("V1", "UN NOM DEUX SIÈCLES TROP TÔT", "0:30", "Isaïe 44:28 ; 45:1 — registre P160-P161",
 "Un prophète écrit un nom ; ce nom est ensuite gravé dans l'argile.",
 "nappe grave continue, frottement d'un stylet sur l'argile, un seul souffle humain",
 "La datation du livre d'Isaïe est discutée ; la vidéo ne l'affirme pas et ne montre aucun visage.",
 [("0:00–0:04", "macro", "table d'argile humide, la pointe d'un stylet commence à tracer", "UN NOM.", "Un prophète a écrit un nom."),
  ("0:04–0:10", "macro serré", "le stylet achève le tracé, l'argile brille sous la lampe", "DEUX SIÈCLES AVANT.", "Environ deux siècles avant que cet homme ne naisse."),
  ("0:10–0:16", "plan large", "cité antique au bord d'un fleuve au crépuscule, fumée au loin", "CYRUS.", "Ce nom : Cyrus. Le texte décrit aussi ce qu'il fera."),
  ("0:16–0:22", "macro", "cylindre d'argile dans une vitrine, reflet de lampe qui glisse", "RETROUVÉ.", "Un cylindre retrouvé en Mésopotamie décrit la même politique : libérer des captifs, faire rebâtir une ville."),
  ("0:22–0:27", "plan rapproché", "carte à plat, un doigt suit le cours d'un fleuve", "LA MÊME POLITIQUE.", "La même politique, des siècles plus tard."),
  ("0:27–0:30", "carton", "fond sombre, deux lignes de texte", "QUI POUVAIT ÉCRIRE CE NOM ? — jw.org", "Une question : qui pouvait écrire ce nom ?")])

video("V2", "UNE NUIT, ET LA VILLE TOMBE", "0:35", "Jérémie 50-51 ; Daniel 5 — registre P283-P294 ; P374-P375",
 "Une ville réputée imprenable tombe en une seule nuit.",
 "nappe tendue, un fleuve en fond, une coupe posée sur une table de pierre",
 "Le quantième dépend du calendrier employé : le registre retient les 5 et 6 octobre.",
 [("0:00–0:05", "plan large", "murailles gigantesques la nuit, torches, ciel sans lune", "IMPRENABLE.", "Babylone se croyait imprenable."),
  ("0:05–0:12", "macro", "coupe de vin renversée sur une table, main anonyme hors champ", "UN FESTIN.", "Le dernier soir, un festin."),
  ("0:12–0:19", "macro", "paroi de plâtre, une écriture apparaît dans la lumière rasante", "MENÉ, PESÉ, DIVISÉ.", "Sur le mur : mené, pesé, divisé."),
  ("0:19–0:25", "plan large", "le fleuve baissé, le lit découvert sous les portes de la ville", "LE FLEUVE.", "Le fleuve est détourné ; les portes restent ouvertes."),
  ("0:25–0:30", "plan large", "silhouettes qui entrent par le lit du fleuve, poussière", "UNE NUIT. 5 OCTOBRE 539.", "La ville tombe dans la nuit. Les publications datent la prise du 5 octobre 539 avant notre ère."),
  ("0:30–0:35", "carton", "fond sombre", "ANNONCÉ DES SIÈCLES PLUS TÔT — jw.org", "Annoncé des siècles plus tôt : par quel détail ?")])

video("V3", "SEPT MOIS, UNE DIGUE", "0:35", "Ézéchiel 26:4, 12 — registre P337-P339",
 "Une ville insulaire doit devenir un rocher nu, un lieu pour étendre les filets.",
 "vagues lentes, vent, bois qui craque, pierres qui tombent dans l'eau",
 "Arrien rapporte huit mille morts et trente mille personnes vendues ; la digue ne date pas le texte.",
 [("0:00–0:05", "plan large", "île fortifiée au milieu de la mer, vagues contre les rochers", "UNE ÎLE.", "Tyr : une ville sur une île, réputée imprenable."),
  ("0:05–0:11", "macro", "filets étendus à sécher sur un rocher nu, au petit matin", "UN LIEU POUR LES FILETS.", "Un prophète écrit : elle deviendra un lieu pour étendre les filets."),
  ("0:11–0:17", "plan large", "ruines continentales, débris, poussière soulevée par le vent", "TES PIERRES, TON BOIS, TA POUSSIÈRE.", "Et : on jettera à l'eau tes pierres, ton bois et ta poussière."),
  ("0:17–0:24", "plan large", "une jetée se construit dans la mer : pierres déversées, travaux", "332 AV. N. È.", "En 332 avant notre ère, une digue est construite avec les débris de la ville continentale : environ huit cents mètres."),
  ("0:24–0:30", "macro", "la jetée aujourd'hui : rochers, embruns, herbe sèche", "ELLE EST ENCORE LÀ.", "Les restes de cette digue sont encore visibles aujourd'hui."),
  ("0:30–0:35", "carton", "fond sombre", "SEPT MOIS DE SIÈGE — jw.org", "Le siège dura sept mois ; le rocher nu, lui, est toujours là.")])

video("V4", "QUARANTE JOURS", "0:30", "Jonas 3:4 ; Nahum ; Sophonie 2:12-15 — registre P448 ; P465-P469 ; P482",
 "Une ville menacée change de conduite : le délai passe, la ville survit — pour un temps.",
 "vent sec, pas dans la poussière, une cloche lointaine",
 "La chronologie profane situe souvent la chute en 612 ; un contenu n'emploie qu'un seul système et signale la divergence.",
 [("0:00–0:05", "plan large", "ville immense, murailles, fumée d'encens au loin", "NINIVE.", "Ninive, capitale de l'Assyrie."),
  ("0:05–0:11", "macro", "pas dans la poussière, une silhouette seule traverse un marché", "QUARANTE JOURS.", "Un homme traverse la ville et annonce : encore quarante jours."),
  ("0:11–0:17", "plan large", "formes humaines prosternées, vues de loin, sans visage", "ILS ONT CHANGÉ.", "La ville change de conduite : le délai ne s'accomplit pas dans ces quarante jours."),
  ("0:17–0:24", "plan large", "tell de fouilles au coucher du soleil, couches de terre", "PUIS, EN 632.", "Un siècle et demi plus tard, d'autres prophètes annoncent sa fin. Les publications datent la chute en 632 avant notre ère."),
  ("0:24–0:28", "macro", "un tell herbeux, quelques pierres affleurantes", "JAMAIS RELEVÉE.", "Aujourd'hui : un tell de fouilles. La ville n'a jamais retrouvé son rang."),
  ("0:28–0:30", "carton", "fond sombre", "DEUX PROPHÉTIES, DEUX TEMPS — jw.org", "Deux prophéties, deux temps.")])

video("V5", "SOIXANTE-DIX ANS, COMPTÉS PAR UN ROI ÉTRANGER", "0:35", "Jérémie 25:11, 12 ; 2 Chroniques 36:21 ; Daniel 9:2 — registre P221-P222 ; P104 ; P384",
 "Une durée ronde annoncée avant la déportation, puis vérifiée à la lettre.",
 "rouleau qu'on déroule, craquement de la lampe, pas au loin",
 "La chronologie profane situe la chute de Jérusalem en 587 ; la vidéo emploie un seul système et signale la divergence.",
 [("0:00–0:05", "macro", "un rouleau se déroule sous une lampe, main hors champ", "SOIXANTE-DIX ANS.", "Soixante-dix ans : le chiffre est annoncé avant la déportation."),
  ("0:05–0:12", "plan large", "une ville vidée, portes ouvertes, poussière dans un rayon de lumière", "607 AV. N. È.", "Juda est désolé. Les publications datent la désolation de 607 avant notre ère."),
  ("0:12–0:18", "macro", "sceau pressé sur de l'argile, puis tablette posée", "UN PAYS LAISSÉ EN REPOS.", "Et le pays paiera ses sabbats : soixante-dix années de repos."),
  ("0:18–0:25", "plan large", "cour étrangère reconstituée, tablettes empilées, lampes", "COMPTÉS AILLEURS.", "L'annonce est reprise dans un livre rédigé loin de là : un exilé écrit : moi, Daniel, je discernai dans les livres."),
  ("0:25–0:30", "plan large", "une route dans le désert au lever du jour, caravane lointaine", "PUIS LE RETOUR.", "Puis le retour, en 537 : les deux dates se répondent."),
  ("0:30–0:35", "carton", "fond sombre", "SOIXANTE-DIX ANS DANS LES DEUX SENS — jw.org", "Soixante-dix années exactement.")])

video("V6", "QUATRE CENT QUATRE-VINGT-TROIS ANS", "0:40", "Daniel 9:24-27 — registre P385 ; P640-P641",
 "Une date de départ, une durée, un point d'arrivée : une prophétie qui se calcule.",
 "encre et plume, sablier, une pièce de monnaie posée sur une table",
 "Le comput de la vingtième année d'Artaxerxès est discuté ; la vidéo n'entre pas dans ce débat.",
 [("0:00–0:05", "macro", "écritoire, chandelle, main anonyme qui compte des jetons", "UNE DATE DE DÉPART.", "Une prophétie donne une date de départ : un décret."),
  ("0:05–0:12", "plan large", "place antique, un parchemin déroulé devant la foule (texte non lisible)", "455 AV. N. È.", "Le décret de la vingtième année d'Artaxerxès, daté de 455 avant notre ère."),
  ("0:12–0:19", "macro", "soixante-neuf jetons alignés, l'ombre d'un doigt passe", "SOIXANTE-NEUF SEMAINES : 483 ANS.", "Soixante-neuf semaines : quatre cent quatre-vingt-trois années, selon la règle des années pour les jours."),
  ("0:19–0:26", "plan large", "route vers un fleuve, silhouettes, brume du matin", "29 DE N. È.", "L'arrivée : l'année 29 de notre ère, le baptême de Jésus, l'Oint."),
  ("0:26–0:33", "macro", "sept pierres alignées, la quatrième fendue, main hors champ", "LA MOITIÉ DE LA SEMAINE.", "Puis la moitié de la dernière semaine : la mort du Messie, en 33."),
  ("0:33–0:40", "carton", "fond sombre", "455 + 483 = 29 — jw.org", "Une date de départ, une durée, un point d'arrivée.")])

video("V7", "UNE BATAILLE NOMMÉE PAR SON LIEU", "0:35", "Daniel 11:11, 12 — registre P394",
 "Le texte décrit des mouvements de rois sans toujours les nommer : les lieux, eux, se reconnaissent.",
 "tambour lointain, vent de plaine, cuir qui frotte",
 "Certains critiques datent ces chapitres après 166 avant notre ère : la vidéo le dit, sans masquer le débat.",
 [("0:00–0:05", "plan large", "deux colonnes en marche vues de loin, poussière soulevée", "DEUX ROIS.", "Deux rois s'affrontent : celui du midi, celui du nord."),
  ("0:05–0:12", "macro", "carte ancienne à plat, deux points reliés par une route tracée", "UN LIEU.", "Le texte décrit des mouvements, des années, des lieux."),
  ("0:12–0:19", "plan large", "plaine côtière, la mer au fond, aube grise", "RAPHIA, 217 AV. N. È.", "En 217 avant notre ère : Raphia. Le roi du midi frappe et l'emporte."),
  ("0:19–0:26", "macro", "tablettes, comptes, une main qui écrit à la plume", "ATTESTÉ.", "Le déroulement est attesté hors de la Bible."),
  ("0:26–0:31", "plan large", "un temple profané : rideau déchiré, ombre, cendres", "PUIS LA PROFANATION.", "Puis la profanation du temple et la chose immonde qui cause la désolation."),
  ("0:31–0:35", "carton", "fond sombre", "ET CE QUE CELA NE PROUVE PAS — jw.org", "Une précision de ce genre sert aussi les critiques : la question de la date de rédaction reste posée.")])

video("V8", "DE 607 À 1914", "0:40", "Daniel 4:10-27, 31, 32 ; Nombres 14:34 ; Ézéchiel 4:6 — registre P372-P373",
 "Un arbre abattu, sept temps, et une règle donnée deux fois dans la Bible : un jour pour un an.",
 "nappe grave, hache lointaine, vent dans les feuilles puis silence",
 "La vidéo expose le calcul tel que les publications le publient et ne date jamais la fin, qui n'est pas annoncée.",
 [("0:00–0:05", "plan large", "arbre immense dans une plaine, ciel chargé", "UN ARBRE.", "Un arbre immense, abattu, puis un bandeau sur la souche : sept temps."),
  ("0:05–0:12", "macro", "sept marques alignées entaillées dans le bois", "UN JOUR POUR UN AN.", "La règle est donnée deux fois dans la Bible : un jour pour un an."),
  ("0:12–0:20", "macro", "sablier, ombres qui tournent sur un mur de pierre", "SEPT TEMPS : 2 520 JOURS.", "Sept temps : deux mille cinq cent vingt jours, donc deux mille cinq cent vingt années."),
  ("0:20–0:28", "plan large", "enchaînement : ville antique, route caravanière, puis silhouette de ville moderne", "OCTOBRE 607 → OCTOBRE 1914.", "À partir d'octobre 607 avant notre ère, on arrive à octobre 1914."),
  ("0:28–0:35", "plan large", "ville de 1914 : usines, foule lointaine, affiches sans texte", "LE ROYAUME ÉTABLI.", "Les publications situent là l'établissement du Royaume et la fin des temps fixés des nations."),
  ("0:35–0:40", "carton", "fond sombre", "UN CALCUL PUBLIÉ, ÉTAPE PAR ÉTAPE — jw.org", "Un calcul publié, étape par étape, sur le site officiel.")])

video("V9", "DOUZE MARQUES, EN MÊME TEMPS", "0:35", "Matthieu 24 ; Luc 21 ; 2 Timothée 3:1-5 — registre P647-P668 ; P761",
 "Pas une date : un faisceau de signes qui doivent coïncider.",
 "horloge de gare, rumeur de foule, un souffle qui revient par vagues",
 "Chaque marque a existé isolément à d'autres époques ; l'argument porte sur la simultanéité et sur l'ampleur organisée de la prédication.",
 [("0:00–0:05", "plan large", "horloge d'ancien style dans une gare, foule en flou de mouvement", "PAS UNE DATE.", "Jésus ne donne pas une date : il donne des marques."),
  ("0:05–0:12", "mosaïque", "six vignettes rapides : chantier, champ sec, brancard, écran, table vide, journal", "GUERRES. DISETTES. SÉISMES.", "Guerres de nations, disettes, séismes, pestes, spectacles effrayants."),
  ("0:12–0:19", "macro", "une main fait défiler un écran, reflets mouvants", "ET L'AMOUR QUI REFROIDIT.", "Illégalité accrue, amour qui refroidit : vingt traits décrits pour les derniers jours."),
  ("0:19–0:26", "plan large", "salle d'impression, feuilles qui sortent en cadence, sans logo", "PRÊCHÉE PARTOUT.", "Et un signe qui ne ressemble à aucun autre : la bonne nouvelle prêchée dans toute la terre habitée, en plus de mille langues."),
  ("0:26–0:31", "macro", "globe ancien, fils tendus d'un point à l'autre", "SIMULTANÉES.", "L'argument n'est pas un élément isolé, mais leur simultanéité."),
  ("0:31–0:35", "carton", "fond sombre", "LESQUELLES VOYEZ-VOUS ? — jw.org", "Lesquelles avez-vous déjà vues ensemble ?")])

video("V10", "FUIR QUAND C'EST ENCORE POSSIBLE", "0:40", "Luc 21:20, 21 ; Matthieu 24:15, 16 — registre P680-P684",
 "Un avertissement précis : partir pendant qu'une fenêtre reste ouverte.",
 "poussière, cloches lointaines, pas d'un groupe qui marche sur la pierre",
 "Le récit de Pella vient d'un historien postérieur aux faits ; la vidéo le signale.",
 [("0:00–0:05", "plan large", "murailles et tours, poussière soulevée au loin", "UNE VILLE CONDAMNÉE.", "Jérusalem : une ville condamnée, et un avertissement."),
  ("0:05–0:12", "plan large", "colonnes et enseignes vues de loin, campement aux abords", "ENCERCLÉE PAR DES ARMÉES.", "Jésus dit : quand vous verrez Jérusalem entourée d'armées, la désolation s'est approchée."),
  ("0:12–0:20", "plan large", "route vers les collines, silhouettes avec peu de bagages", "66 DE N. È.", "En 66, les armées se retirent brusquement ; des chrétiens partent vers les montagnes, notamment vers Pella."),
  ("0:20–0:28", "macro", "mur de pierres dressé, herbe entre les blocs, fourmilière de vie", "70 DE N. È.", "En 70, la ville est encerclée de nouveau, et cette fois sans issue."),
  ("0:28–0:35", "plan large", "route antique au coucher du soleil, traces dans la poussière", "RAPPORTÉ PAR UN HISTORIEN.", "Un historien ancien écrit qu'un avertissement avait été donné à l'assemblée de quitter la ville avant la guerre."),
  ("0:35–0:40", "carton", "fond sombre", "ET JUSQU'EN 1914 — jw.org", "Les publications rappellent que Jérusalem devait être foulée par les nations jusqu'au début de l'automne 1914.")])

# ---------------------------------------------------------------- 3 LONGS
video("L1", "RÉVÉLATION 21-22 : CE QUI VIENT", "2:30", "Révélation 21:1-22:21 — registre P945-P971",
 "Ce que dit la fin du livre : une ville, un fleuve, des arbres, des larmes essuyées.",
 "nappe très lente, eau qui coule, un souffle d'air clair",
 "Aucune date. Les images restent symboliques et ne prétendent pas représenter ce qui est décrit.",
 [("0:00–0:12", "plan large", "mer calme au lever du jour, horizon vide", "CE QUI VIENT.", "Ce que la Bible place à la fin ne commence pas par un cataclysme : par une promesse."),
  ("0:12–0:30", "plan large", "ciel qui s'ouvre lentement, nuages qui se déchirent", "UN NOUVEAU CIEL, UNE NOUVELLE TERRE.", "Un nouveau ciel et une nouvelle terre : la première création passe."),
  ("0:30–0:50", "plan large", "une ville aux murs clairs dans une lumière rasante, très loin", "LA TENTE DE DIEU AVEC LES HUMAINS.", "La tente de Dieu est avec les humains : il habitera avec eux."),
  ("0:50–1:08", "macro", "une main essuie une larme sur un visage hors champ (pas de visage identifiable)", "IL ESSUIERA TOUTE LARME.", "Il essuiera toute larme : ni mort, ni deuil, ni cri, ni douleur."),
  ("1:08–1:26", "macro", "eau claire qui coule entre des pierres, lumière qui danse", "UN FLEUVE D'EAU DE VIE.", "Un fleuve d'eau de vie, limpide, sort du trône."),
  ("1:26–1:44", "plan large", "rangée d'arbres feuillus le long d'un fleuve, feuilles qui bougent", "DES ARBRES POUR LA GUÉRISON DES NATIONS.", "Des arbres pour la guérison des nations, avec des feuilles qui ne fanent pas."),
  ("1:44–2:00", "plan large", "place ouverte, pierres claires, ombres douces", "JÉHOVAH EST LÀ.", "Le nom de la ville : Jéhovah est là."),
  ("2:00–2:16", "macro", "page qui se tourne, lampe, main hors champ", "LES REPÈRES DU REGISTRE.", "Chaque détail de ces chapitres figure au registre, avec son numéro : P945 à P971."),
  ("2:16–2:30", "carton", "fond sombre, deux lignes", "À VENIR : AUCUNE DATE — jw.org", "Aucune date n'est donnée : les prophéties de l'avenir restent sans date.")])

video("L2", "HUIT OBJECTIONS, HUIT RÉPONSES BRÈVES", "3:00", "Annexe du Grand Dossier — huit objections",
 "Les huit objections qui reviennent, et une réponse courte pour chacune.",
 "nappe neutre, une seule note tenue par objection, silence entre deux objections",
 "Réponses brèves : chaque objection mérite une discussion, jamais un débat improvisé ; le contenu ne demande à personne de se convertir.",
 [("0:00–0:22", "carton + plan large", "une table avec deux chaises, une lampe, un livre fermé", "OBJECTION 1 : LES COPIES SONT TARDIVES.", "Les copies sont tardives, c'est vrai ; mais ce qui est vérifiable, ce sont les faits racontés par des sources extérieures."),
  ("0:22–0:44", "plan large", "rouleaux dans un rouleau à rouleaux: rayonnages de rouleaux dans une pénombre", "OBJECTION 2 : LES TRADUCTIONS DIFFÈRENT.", "Les traductions diffèrent par le vocabulaire, non par les faits datés : une date ne se traduit pas."),
  ("0:44–1:06", "plan large", "une roue de charrette dans le sable, puis une route moderne", "OBJECTION 3 : LA SCIENCE A CHANGÉ LE MONDE.", "Ce que la science observe s'harmonise, sans se substituer : la vidéo ne dit jamais qu'une observation prouve Dieu."),
  ("1:06–1:28", "macro", "un texte écrit à la main, puis le même texte recopié", "OBJECTION 4 : LA BIBLE A ÉTÉ MODIFIÉE.", "Les copies se comptent par milliers et se recoupent ; les divergences connues sont signalées, y compris dans ce dossier."),
  ("1:28–1:50", "plan large", "une ville antique ruinée, puis une ville debout", "OBJECTION 5 : LES PROPHÉTIES SONT VAGUES.", "Certaines le sont ; d'autres nomment une ville, une année, un roi, une durée — celles-là se vérifient."),
  ("1:50–2:12", "plan large", "une horloge et un calendrier sur un mur de pierre", "OBJECTION 6 : TOUT S'EST ÉCRIT APRÈS.", "C'est l'objection sérieuse ; elle se discute par les manuscrits, la datation et les recoupements, pas par l'insistance."),
  ("2:12–2:34", "macro", "deux mains qui discutent autour d'une table, une carte entre elles", "OBJECTION 7 : CHAQUE RELIGION A SES PREUVES.", "Justement : ce dossier ne présente que des faits vérifiables, sans entrer dans les questions propres à chaque religion."),
  ("2:34–3:00", "carton", "fond sombre, trois lignes", "OBJECTION 8 : ET ALORS ? — jw.org", "Et alors : tout cela ne sert à rien s'il ne change rien. La question reste ouverte, à votre rythme.")])

video("L3", "LE KIT EN DEUX MINUTES", "2:00", "Présentation du dossier PREUVES",
 "Ce que contient le kit, dans quel ordre s'en servir, et ce qu'il n'est pas.",
 "nappe claire, papier, intercalaires, une seule nappe de fond",
 "Le kit est privé : aucune publication, aucun site personnel, aucun envoi de masse.",
 [("0:00–0:15", "plan large", "table dressée : volume relié, classeurs, cartes, lampe", "LE KIT EN DEUX MINUTES.", "Ce que contient le dossier, et dans quel ordre s'en servir."),
  ("0:15–0:32", "macro", "mains qui ouvrent le registre à la table des parties", "1 000 ENTRÉES NUMÉROTÉES.", "Un registre de mille entrées numérotées, chacune avec sa référence, sa teneur, son accomplissement et son statut."),
  ("0:32–0:50", "plan large", "un écran d'ordinateur de bureau avec un fichier ouvert (fichier local)", "LE SITE LOCAL.", "Un fichier autonome : recherche par mot, filtres par partie et par statut, sans connexion et sans hébergement."),
  ("0:50–1:08", "macro", "trois volumes empilés, signets de cuir", "TROIS LIVRES À IMPRIMER.", "Trois livres : les douze grandes preuves, le registre mis en pages, et vingt-cinq détails datés."),
  ("1:08–1:26", "plan large", "une frise déroulée sur la table, l'œil parcourt la ligne", "DOUZE FRISES.", "Douze frises chronologiques : deux cent cinquante-huit repères, chacun renvoyé à un numéro du registre."),
  ("1:26–1:44", "macro", "un jeu de cartes à volets, puis un lecteur audio posé à côté", "CARTES ET AUDIO.", "Vingt-quatre cartes à trois volets, et les enregistrements audio en français, à écouter avant de parler."),
  ("1:44–1:52", "macro", "un téléphone qui vise une carte, écran lumineux", "DEPUIS LES SITES OFFICIELS.", "Chaque carte porte un code qui mène à un site officiel, et à rien d'autre."),
  ("1:52–2:00", "carton", "fond sombre, deux lignes", "UNE PERSONNE À LA FOIS — jw.org", "Une personne à la fois, jamais d'envoi de masse : c'est la règle du kit.")])

# --------------------------------------------------------------------- GABARITS
CSS = """
@page { size: A4 portrait; margin: 13mm 12mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, "Times New Roman", serif; color: #16324F; background: #fff; font-size: 9.6pt; line-height: 1.42; margin: 0; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }
h1 { font-size: 20pt; color: #0B2545; margin: 0 0 2mm; }
h2 { font-size: 13.5pt; color: #0B2545; margin: 0 0 2mm; border-bottom: 1.6pt solid #E9C46A; padding-bottom: 1.1mm; }
h3 { font-size: 10.5pt; color: #0B2545; margin: 3.4mm 0 1.4mm; }
.sub { color: #4A5A6A; font-size: 8.6pt; margin: 0 0 3mm; }
.hdr { border-top: 3pt solid #0B2545; padding-top: 3mm; margin-bottom: 3.6mm; }
table { width: 100%; border-collapse: collapse; font-size: 7.8pt; }
th { background: #0B2545; color: #fff; text-align: left; padding: 1.3mm; }
td { border-bottom: .4pt solid #D8D2C4; padding: 1.2mm; vertical-align: top; }
.n { font-family: "Courier New", monospace; font-size: 7pt; color: #0B2545; white-space: nowrap; }
.tx { color: #0B2545; font-weight: 700; }
.voix { font-style: italic; }
.q { background: #F7F4EC; border-left: 2.4pt solid #E9C46A; padding: 2.4mm; margin-top: 3mm; font-size: 9pt; }
.lim { background: #F7F4EC; border: .5pt solid #D8D2C4; padding: 2.2mm; margin-top: 2.4mm; font-size: 8.2pt; }
.foot { font-size: 7.2pt; color: #4A5A6A; border-top: .5pt solid #D8D2C4; margin-top: 2mm; padding-top: 1.2mm; }
.badge { display: inline-block; background: #0B2545; color: #fff; border-radius: 4px; padding: .4mm 1.6mm; font-size: 7pt; margin-right: 1.4mm; }
.frame { border: .7pt solid #0B2545; border-radius: 1.5mm; padding: 2mm; margin-bottom: 2.6mm; page-break-inside: avoid; }
.sb { display: grid; grid-template-columns: 34mm 1fr; gap: 3mm; }
.sb .box { border: .7pt solid #0B2545; border-radius: 1.5mm; position: relative; aspect-ratio: 9 / 16; background: #F7F4EC; }
.sb .box .l1, .sb .box .l2 { position: absolute; background: #D8D2C4; }
.sb .box .l1 { left: 0; right: 0; height: .3pt; top: 33.33%; }
.sb .box .l2 { left: 0; right: 0; height: .3pt; top: 66.66%; }
.sb .box .c1, .sb .box .c2 { position: absolute; background: #D8D2C4; }
.sb .box .c1 { top: 0; bottom: 0; width: .3pt; left: 33.33%; }
.sb .box .c2 { top: 0; bottom: 0; width: .3pt; left: 66.66%; }
.sb .box .num { position: absolute; top: 1mm; left: 1.4mm; font-size: 7pt; color: #0B2545; font-weight: 700; }
.sb .box .dur { position: absolute; bottom: 1mm; right: 1.4mm; font-size: 6.6pt; color: #4A5A6A; }
.sb .box .fmt { position: absolute; bottom: 1mm; left: 1.4mm; font-size: 6.6pt; color: #4A5A6A; }
"""

H = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Scripts vidéos — PREUVES</title><style>%s</style></head><body>' % CSS]
H.append('<div class="page"><div class="hdr"><h1>SCRIPTS VIDÉOS — DOSSIER DE TOURNAGE</h1>'
         '<div class="sub">10 vidéos courtes (30 à 40 s) et 3 vidéos longues (2 à 3 min) — plan par plan : temps · cadrage · action · '
         'texte à l\'écran · voix off · son · limite honnête. Aucune vidéo n\'est produite ici : tout est prêt à tourner ou à générer plan par plan.</div></div>')
H.append('<h2>Fiche technique commune</h2><table><tbody>')
for k, val in FICHE:
    H.append('<tr><td style="width:34mm"><b>%s</b></td><td>%s</td></tr>' % (esc(k), esc(val)))
H.append('</tbody></table>')
H.append('<div class="q"><b>Les trois règles qui ne bougent pas.</b> 1) L\'accroche tombe dans les trois premières secondes. '
         '2) Le dernier carton pose la question et donne la référence officielle, jamais un argument. '
         '3) Chaque vidéo porte une limite écrite : ce qu\'elle ne prouve pas.</div>')
H.append('<div class="lim"><b>%s</b></div>' % esc(LIMITE_GEN))
H.append('<h2>Sommaire</h2><table><thead><tr><th style="width:12mm">N°</th><th>Titre</th><th style="width:16mm">Durée</th>'
         '<th style="width:38mm">Références</th><th style="width:14mm">Plans</th></tr></thead><tbody>')
for v in V:
    H.append('<tr><td class="n">%s</td><td><b>%s</b></td><td>%s</td><td>%s</td><td class="n">%d</td></tr>'
             % (esc(v['code']), esc(v['titre']), esc(v['duree']), esc(v['refs']), len(v['plans'])))
H.append('</tbody></table><div class="foot">Total : %d plans à préparer · %d vidéos</div></div>'
         % (sum(len(v['plans']) for v in V), len(V)))

for v in V:
    H.append('<div class="page"><div class="hdr"><h2>%s — %s</h2>'
             '<div class="sub">Durée : %s · Références : %s</div></div>' % (esc(v['code']), esc(v['titre']), esc(v['duree']), esc(v['refs'])))
    H.append('<p><span class="badge">ACCROCHE</span>%s</p>' % esc(v['accroche']))
    H.append('<table><thead><tr><th style="width:20mm">Temps</th><th style="width:18mm">Cadrage</th><th>Action</th>'
             '<th style="width:38mm">Texte à l\'écran</th><th style="width:52mm">Voix off</th></tr></thead><tbody>')
    for d, cad, act, txt, voix in v['plans']:
        H.append('<tr><td class="n">%s</td><td>%s</td><td>%s</td><td class="tx">%s</td><td class="voix">%s</td></tr>'
                 % (esc(d), esc(cad), esc(act), esc(txt), esc(voix)))
    H.append('</tbody></table>')
    H.append('<div class="lim"><b>Son :</b> %s<br><b>Ce que la vidéo ne prouve pas / ne fait pas :</b> %s</div>'
             % (esc(v['son']), esc(v['limite'])))
    H.append('<div class="foot">Dernier carton : question ouverte + « jw.org » · aucun logo, aucun visage identifiable, aucune citation de publication.</div></div>')

H.append('<div class="page"><div class="hdr"><h2>Feuille de tournage — une page par vidéo</h2>'
         '<div class="sub">À remplir sur le terrain : date, lieu, matériel, plans tournés, plans à refaire.</div></div>')
H.append('<table><thead><tr><th>N°</th><th>Vidéo</th><th>Plans</th><th style="width:26mm">Tourné le</th>'
         '<th style="width:40mm">Décor / lieu</th><th style="width:28mm">Plans à refaire</th></tr></thead><tbody>')
for v in V:
    H.append('<tr><td class="n">%s</td><td>%s</td><td class="n">%d</td><td></td><td></td><td></td></tr>'
             % (esc(v['code']), esc(v['titre']), len(v['plans'])))
H.append('</tbody></table><div class="q"><b>Ordre de tournage conseillé.</b> Regrouper les plans de même nature : '
         'macro d\'objets (argile, écuelles, cartes, jetons), plans larges de paysage, cartons. Une journée « macro », '
         'une journée « extérieur », une journée « cartons » : c\'est ainsi qu\'on tourne trois vidéos dans le temps d\'une seule.</div>'
         '<div class="foot">Scripts vidéos — préparé par videos/build_videos.py · usage privé</div></div>')

H.append('</body></html>')
open(OUT_SCRIPTS, 'w', encoding='utf-8').write(''.join(H))

# ----------------------------------------------------------------- STORYBOARDS
S = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Storyboards — PREUVES</title><style>%s</style></head><body>' % CSS]
S.append('<div class="page"><div class="hdr"><h1>STORYBOARDS</h1>'
         '<div class="sub">%d vidéos · %d vignettes · format des vignettes : 9:16 avec lignes de tiers. '
         'Chaque vignette porte son numéro de plan, sa durée, son cadrage, son action, son texte à l\'écran et sa voix off.</div></div>'
         % (len(V), sum(len(v['plans']) for v in V)))
S.append('<div class="q"><b>Mode d\'emploi.</b> Ces planches servent à cadrer : elles indiquent ce qui doit être vu, pas comment le dessiner. '
         'On peut les remplir à la main, ou générer chaque plan comme image fixe avec la liste de prompts fournie '
         '(<i>videos/LISTE_PLANS_A_GENERER.md</i>), puis animer par léger mouvement.</div>')
S.append('<div class="lim"><b>Trois interdits de cadrage.</b> Aucun visage identifiable. Aucun logo ni marque. '
         'Aucun texte réel lisible — un carton d\'écran est ajouté au montage, jamais photographié.</div>')
S.append('<div class="foot">Storyboards — videos/build_videos.py</div></div>')

PER_PAGE = 6
for v in V:
    plans = v['plans']
    n_pages = (len(plans) + PER_PAGE - 1) // PER_PAGE
    for k in range(n_pages):
        chunk = plans[k * PER_PAGE:(k + 1) * PER_PAGE]
        S.append('<div class="page"><div class="hdr"><h2>%s — %s</h2><div class="sub">Durée %s · planches %d/%d · '
                 'vignettes %d à %d</div></div>' % (esc(v['code']), esc(v['titre']), esc(v['duree']), k + 1, n_pages,
                                                    k * PER_PAGE + 1, k * PER_PAGE + len(chunk)))
        for i, (d, cad, act, txt, voix) in enumerate(chunk, start=k * PER_PAGE + 1):
            S.append('<div class="frame"><div class="sb"><div class="box"><span class="num">PLAN %d</span>'
                     '<span class="l1"></span><span class="l2"></span><span class="c1"></span><span class="c2"></span>'
                     '<span class="fmt">9:16</span><span class="dur">%s</span></div>'
                     '<div><b>%s</b> — %s<br><span class="tx">Écran : %s</span><br><span class="voix">Voix : %s</span></div>'
                     '</div></div>' % (i, esc(d), esc(cad), esc(act), esc(txt), esc(voix)))
        S.append('<div class="foot">%s · son : %s</div></div>' % (esc(v['code']), esc(v['son'])))
S.append('</body></html>')
open(OUT_STORY, 'w', encoding='utf-8').write(''.join(S))

# ------------------------------------------------------------- LISTE DES PROMPTS
SUF = ("hyperréaliste, photoréaliste, cinématographique, éclairage naturel rasant, texture fine, "
       "profondeur de champ maîtrisée, sans texte, sans lettrage, sans logo, sans visage identifiable, "
       "sans violence explicite, format vertical 9:16, très haute qualité")
L = ['# LISTE DES PLANS À GÉNÉRER',
     '',
     'Un prompt par plan. Convention de nommage : `plans/vNN_pNN.jpg` (exemple : `plans/v03_p04.jpg`).',
     'Chaque image est ensuite animée par un léger mouvement (travelling ou zoom lent) au montage.',
     '',
     '**Suffixe commun à ajouter à chaque prompt :** ' + SUF,
     '',
     '**Règles :** aucune image ne doit contenir de texte lisible, de logo, de marque ni de visage identifiable ; '
     'les cartons d\'écran et les sous-titres sont ajoutés au montage. Les images servent la vidéo, elles ne remplacent aucune publication.',
     '']
for v in V:
    L.append('## %s — %s (%s)' % (v['code'], v['titre'], v['duree']))
    L.append('')
    L.append('Références : %s' % v['refs'])
    L.append('')
    for i, (d, cad, act, txt, voix) in enumerate(v['plans'], 1):
        L.append('%d. **%s-P%02d** — *%s* — %s — écran : « %s » — fichier : `plans/%s_p%02d.jpg`'
                 % (i, v['code'], i, cad, act, txt, v['code'].lower(), i))
        L.append('   - Prompt : « %s, %s, %s, %s »' % (cad, act, txt.lower(), SUF))
    L.append('')
L.append('---')
L.append('')
L.append('Total : %d plans pour %d vidéos. Générer par lots de 10, relire chaque image, puis monter par vidéo.' % (sum(len(v['plans']) for v in V), len(V)))
open(OUT_PLANS, 'w', encoding='utf-8').write('\n'.join(L))

print('SCRIPTS : %d vidéos · %d plans (%.0f Ko)' % (len(V), sum(len(v['plans']) for v in V), os.path.getsize(OUT_SCRIPTS) / 1024))
print('STORYBOARDS : %.0f Ko · LISTE_PLANS : %.0f Ko' % (os.path.getsize(OUT_STORY) / 1024, os.path.getsize(OUT_PLANS) / 1024))
