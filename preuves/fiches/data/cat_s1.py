#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CATEGORIE S — LES PSAUMES MESSIANIQUES (vague 17)
Donnees source de verite. Le generateur ne fait que les mettre en forme.

Regles :
 - dix blocs par fiche, bloc 'limites' jamais vide ;
 - >= 2 sources wol.jw.org / www.jw.org par fiche ;
 - un seul systeme chronologique par fiche + dates neutres signalees ;
 - aucune date pour l'avenir.
"""

CAT = dict(
    code="S",
    nom="Les Psaumes messianiques",
    vague="17",
    intro=(
        "Dix-septième vague : les Psaumes messianiques — le psautier comme livre de "
        "prophéties. S001 : le Psaume 2 — rois coalisés, Roi installé sur Sion, « tu es "
        "mon fils », sceptre de fer. S002 : le Roi de gloire aux portes levées (Ps 24), "
        "le sceptre de justice (Ps 45), la pluie sur le regain (Ps 72). S003 : le "
        "Psaume 110 — verge depuis Sion, prêtre à la manière de Melchisédek, torrent du "
        "guerrier. S004 : la Passion chantée d'avance — trahi, haï sans cause, percé, "
        "dernier cri (Ps 22, 27, 31, 35, 55, 69, 109). S005 : offert, gardé, délivré — "
        "le corps préparé (Ps 40), les anges porteurs (Ps 91), les eaux profondes "
        "(Ps 18), les mains entraînées (Ps 144). S006 : l'alliance chantée — serment à "
        "David (Ps 89, 132), Hosanna (Ps 118), Royaume sans fin (Ps 145, 146). Mêmes "
        "dix blocs, mêmes règles."
    ),
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S001", titre="Psaume 2 — le Roi installé sur Sion, le sceptre de fer",
 ref="Psaume 2:1-12",
 statut="Accomplie (P523, P611, P524, P599) / À venir (P525)",
 cat="S", syst="Système intronisation (Sion → résurrection → fer)",
 reg="Registre : Psaumes — P523 (2:1-6 : coalisés, Roi installé), P611 (2:1-2 : rois massés), P524 (2:7 : « tu es mon fils »), P599 (2:7 : baptême, résurrection), P525 (2:8-12 : nations, sceptre de fer) ; rappels R004 (Ré 2:26-27, Thyatire), I010 (Ré 19:15)",
 texte=[
  "« Les rois de la terre SE MASSENT contre Jéhovah et son OINT. » (2:1-2 — P523, P611 : la coalition !)",
  "« Celui qui SIÈGE dans les cieux RIT. » (2:4 — P523 : le rire du trône !)",
  "« C'est MOI qui ai INSTALLÉ mon roi sur SION, ma montagne sainte. » (2:6 — P523 : l'installation !)",
  "« Tu es MON FILS ; moi, AUJOURD'HUI, je suis devenu ton père. » (2:7 — P524, P599 : l'aujourd'hui !)",
  "« DEMANDE-moi, et je te donnerai les NATIONS pour héritage. » (2:8 — P525 : la demande !)",
  "« Tu les BRISERAS avec un SCEPTRE DE FER. » (2:9 — P525 : le fer !)",
  "« Comme un VASE DE POTIER tu les fracasseras. » (2:9 — P525 : le vase !)",
  "« Servez Jéhovah avec CRAINTE… Heureux tous ceux qui SE RÉFUGIENT en lui. » (2:11-12 — P525 : le refuge !)",
 ],
 contexte=(
  "Psaume sans suscription — anonyme strict — mais la prière de la congrégation "
  "l'attribue à David : « par la bouche de David » (Ac 4:25 — P523, P611). David est "
  "l'auteur principal du psautier (voir si « Psaumes » n° 19, 1101990080 : David et "
  "autres rédacteurs), et Jésus lisait les Psaumes comme le troisième volet des "
  "Écritures : « la Loi, les Prophètes et les Psaumes » (Lc 24:44 — voir 1101990080 ; "
  "le même chapitre envoie les disciples d'Emmaüs relire « Moïse et tous les "
  "Prophètes »). Le Psaume 2 est bâti en quatre voix : les nations rebelles (2:1-3), "
  "Jéhovah qui répond (2:4-6), l'Oint qui proclame le décret (2:7-9), le psalmiste "
  "qui avertit les rois (2:10-12). Psaume d'intronisation du roi davidique — et, "
  "d'un même mouvement, portrait du Messie : Pierre l'applique à « ton saint "
  "serviteur Jésus que tu as oint » (Ac 4:27 — P523, P611)."
 ),
 explication=(
  "« Oint » (2:2 — mashiah en hébreu) : le mot « Messie » en toutes lettres — dès "
  "le deuxième psaume, le titre est posé. Les coalisés « méditent du vide » (2:1) : "
  "leurs cordes et leurs liens (2:3) sont le vocabulaire des vassaux qui secouent "
  "le traité du suzerain. « Celui qui siège rit » (2:4) : non la moquerie cruelle, "
  "mais la sérénité du trône — voir les limites. « J'ai installé » (2:6) : le verbe "
  "de l'onction-intronisation ; Sion, la montagne du roi, devient l'adresse du "
  "Règne — « depuis Sion » (voir S003 : Ps 110:2). « Aujourd'hui » (2:7) : le "
  "registre verse trois applications — le baptême (Mt 3:17 — P599), la résurrection "
  "(Ac 13:33 — P524, P599), l'exaltation (Hé 1:5 ; 5:5 — P524, P599) — sans les "
  "hiérarchiser : voir les limites. « Demande-moi » (2:8) : le Fils reçoit, il ne "
  "prend pas — l'héritage passe par la demande. « Sceptre de fer » (2:9) : "
  "l'instrument qui brise sans se briser ; « vase de potier » : la coalition, "
  "cuite et cassante, fracassée d'un coup. « Heureux les réfugiés » (2:12) : le "
  "psaume de la colère royale se ferme sur un refuge."
 ),
 interpretation=(
  "La coalition (Ac 4:25-28 — P523, P611) : Pierre, relâché par le Sanhédrin, cite "
  "Ps 2:1-2 en prière — « Hérode et Ponce Pilate, avec les nations et les peuples "
  "d'Israël, se sont rassemblés contre ton saint serviteur Jésus » : le tétrarque, "
  "le gouverneur, les nations, le peuple — les quatre visages des « rois de la "
  "terre ». « Aujourd'hui » à la résurrection (Ac 13:33 — P524, P599) : Paul, à "
  "Antioche de Pisidie, applique Ps 2:7 au relèvement de Jésus ; au baptême, la "
  "voix disait déjà « Celui-ci est mon Fils » (Mt 3:17 — P599) ; aux Hébreux, "
  "« auquel des anges a-t-il jamais dit : Tu es mon fils ? » (Hé 1:5 — P524). Le "
  "couple royal-sacerdotal (Hé 5:5-6 — P524, P599, P554, P609) : le même « "
  "aujourd'hui » fait le Fils (Ps 2:7) ET le Prêtre (Ps 110:4) — voir 1974167, qui "
  "présente les deux versets pairés, et voir S003. L'héritage des nations (Ps 2:7-9 "
  "cités dans l'article sur le Psaume 72 — voir 1996800) : au Fils de David les "
  "« extrémités de la terre ». Le fer, lui, est À venir : « il les fera paître "
  "avec un bâton de fer » (Ré 2:26-27 — P525, rappel R004 : Thyatire) et « c'est "
  "avec un sceptre de fer qu'il frappera » (Ré 19:15 — P525, rappel I010)."
 ),
 hist=(
  "Intronisations du Proche-Orient ancien : onction d'huile, proclamation du décret "
  "royal, hommage des vassaux — le Psaume 2 suit le protocole (décret proclamé en "
  "2:7, sommation aux vassaux en 2:10-12). Vassalité : « servez avec crainte » (2:11) "
  "est le langage des traités suzerain-vassal — le baiser au fils (2:12) est "
  "l'hommage rendu au suzerain (repère de coutume, sans lien). « Vase de potier » "
  "(2:9) : l'Égypte connaissait les vases d'exécration — poteries inscrites aux "
  "noms des ennemis, rituellement brisées (repère EXTERNE, sans lien : parallèle de "
  "pratique, NON versé comme preuve — voir les limites). Hérode Antipas et Ponce "
  "Pilate (Ac 4:27 — P523, P611) : le tétrarque de Galilée et le cinquième préfet "
  "de Judée, ennemis devenus alliés d'un jour (Lc 23:12 — C8 : aucun P, vérifié)."
 ),
 geo=(
  "Sion (2:6) : la montagne sainte, la citadelle de David devenue adresse du trône — "
  "« depuis Sion » partira aussi le sceptre (voir S003). Les nations, les rois, "
  "les juges (2:1-2, 10) : la terre entière convoquée — « les extrémités de la "
  "terre » (2:8) en héritage. « La terre » donnée au Fils (2:8) : pas un district, "
  "le domaine entier — « d'une mer à l'autre » chantera le Psaume 72 (voir S002). "
  "Le refuge (2:12) : pas de lieu nommé — le refuge, c'est une personne."
 ),
 sci=(
  "Céramique (2:9) : le vase de potier, une fois cuit, ne se répare pas — le bris "
  "est irréversible : la poterie dit la définitivité du jugement. Métallurgie : "
  "le fer contre l'argile — le sceptre qui frappe ne s'ébrèche pas, le vase qui "
  "reçoit vole en éclats ; l'âge du fer a rendu l'image évidente à tout ancien "
  "(repère, sans lien). Philologie : mashiah (« oint », 2:2) — le titre ; nashek "
  "(« baisez », 2:12) — le baiser d'hommage ; le « rire » (2:4) — l'anthropopathisme "
  "biblique : Dieu décrit en langage humain, sans que l'image épuise le réel — "
  "voir les limites. Onction : l'huile versée, parfumée, qui consacre — chimie du "
  "rite royal (voir S003 : Melchisédek, le prêtre-roi)."
 ),
 limites=(
  "« Aujourd'hui » (2:7) : baptême, résurrection, exaltation — les trois applications "
  "du registre sont versées SANS hiérarchie tranchée ici. Le rire (2:4) : image, "
  "pas moquerie — Dieu ne ricane pas des perdus, il siège au-dessus des tumultes. "
  "« Baisez le fils » (2:12) : hébreu discuté (nashqu-bar, tournure rare) — "
  "l'hommage au Fils est sûr, la lettre reste débattue ; paraphrase prudente. "
  "Auteur : strictement anonyme ; David par Ac 4:25. Vases d'exécration : parallèle "
  "EXTERNE (sans lien — règle : jw.org/wol uniquement), PAS preuve. Sceptre de fer "
  "(P525) : À venir — AUCUNE date. C8 : Lc 23:12 (Hérode-Pilate réconciliés) — aucun "
  "P (vérifié : P523-P525 seuls sur Ps 2 ; P611 doublon de P523)."
 ),
 accomplissement=[("Contre l'Oint", "Hérode + Pilate + nations (Ac 4:25-28 — P523, P611)"),
     ("Roi installé", "Sion — décret proclamé (2:6-7 — P523, P524)"),
     ("Aujourd'hui", "Baptême, résurrection, exaltation (P524, P599)"),
     ("Nations demandées", "Héritage promis au Fils (2:8 — P525)"),
     ("Roi-Prêtre", "Ps 2:7 + Ps 110:4 pairés (Hé 5:5-6 — voir S003)"),
     ("Fer à venir", "Bâton de fer (Ré 2:27 ; 19:15 — P525)")],
 tl=[("Époque de David (repère)", "Psaume d'intronisation (P523-P525, P611)"),
     ("33 (ère commune)", "Hérode + Pilate coalisés (P523, P611)"),
     ("Pentecôte 33", "Pierre cite Ps 2:1-2 (Ac 4:25-28)"),
     ("Baptême → résurrection", "« Aujourd'hui » accompli (P524, P599)"),
     ("Antioche (Paul)", "Ps 2:7 à la résurrection (Ac 13:33)"),
     ("À venir", "Sceptre de fer (P525) — aucune date")],
 src=[("Les Psaumes — si n° 19 (David, Lc 24:44, Emmaüs)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Le Psaume 72 (cite Ps 2:7-9, l'héritage des nations)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996800"),
      ("Roi et Prêtre (Ps 2:7 + Ps 110:4 pairés)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1974167"),
      ("Psaume 2 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/2")],
 img="images/prophe_S001_psaume2.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S002", titre="Portes levées, sceptre de justice, pluie sur le regain",
 ref="Psaume 24:7-10 ; Psaume 45:2-7 ; Psaume 72:1-20",
 statut="Accomplie (P534, P540) / Accomplie, 1er accomplissement (P547)",
 cat="S", syst="Système royauté (arche → noces → Salomon)",
 reg="Registre : Psaumes — P534 (24:7-10 : portes, Roi de gloire), P540 (45:2-7 : trône pour toujours), P547 (72:1-20 : roi juste, mer à mer) ; rappels L005 (Tarsis, non tranché), R003 (Mi 4:4, vigne-figuier)",
 texte=[
  "« ÉLEVEZ vos têtes, PORTES… que le ROI DE GLOIRE entre ! » (24:7 — P534 : l'entrée !)",
  "« Jéhovah, FORT et PUISSANT… PUISSANT dans la bataille. » (24:8 — P534 : le guerrier !)",
  "« Les portes ÉTERNELLES… Jéhovah des ARMÉES, c'est lui le Roi de gloire. » (24:9-10 — P534 : les armées !)",
  "« Ton TRÔNE est pour TOUJOURS… un SCEPTRE DE JUSTICE. » (45:6 — P540 : le sceptre !)",
  "« Il sera comme la PLUIE sur le REGAIN. » (72:6 — P547 : la pluie !)",
  "« Il DOMINERA d'une MER à l'autre… jusqu'aux BOUTS de la terre. » (72:8 — P547 : l'étendue !)",
  "« Il DÉLIVRERA le pauvre… leur SANG sera PRÉCIEUX à ses yeux. » (72:12, 14 — P547 : le sang précieux !)",
  "« On PRIERA pour lui SANS CESSE. » (72:15 — P547 : la prière !)",
 ],
 contexte=(
  "Trois psaumes royaux, trois cortèges. Psaume 24 : la montée — « À Jéhovah la "
  "terre et tout ce qu'elle contient » (24:1), puis « qui montera à la montagne ? "
  "— celui qui a les mains innocentes et le cœur pur » (24:3-4), puis les portes "
  "sommées de s'ouvrir devant le Roi de gloire (24:7-10 — P534). Premier arrière-plan : "
  "la montée de l'arche à Jérusalem (2S 6 — C8 : aucun P, vérifié). Psaume 45 : le "
  "psaume du roi-époux — ton nuptial, mais les versets retenus (45:2-7 — P540) "
  "chantent le trône, pas les noces (45:8-17 : voir les limites) ; l'épître aux "
  "Hébreux l'applique au Fils (Hé 1:8-9 — P540). Psaume 72 : « au sujet de "
  "Salomon » — la prière de David, sur ses vieux jours, pour le règne de son fils "
  "(voir si Psaumes, 1101990080 : « prière pour un règne pacifique » ; voir 1996800 : "
  "David âgé, « plus que Salomon ») ; 1er accomplissement sous Salomon (1R 4:20, 21, 25 "
  "— P547), plénitude dans le Messie."
 ),
 explication=(
  "« Roi de gloire » (24:7-10) : la question fuse deux fois (« qui est-il ? »), la "
  "réponse deux fois — liturgie antiphonée, deux chœurs qui se répondent aux portes. "
  "« Portes éternelles » (24:9) : les portes « de toujours » — assez anciennes, "
  "assez basses pour devoir « lever la tête » devant le Roi qui entre. « Fort et "
  "puissant… dans la bataille » (24:8) : le Roi de gloire est un Roi de guerre — "
  "le même que S001 (sceptre de fer) et S003 (il jugera). « Sceptre de justice » "
  "(45:6 — P540) : la droiture comme instrument de règne ; « tu as aimé la justice, "
  "tu as haï l'illégalité » (Hé 1:9 — P540). « Pluie sur le regain » (72:6 — "
  "P547) : le roi comme l'averse d'arrière-saison sur l'herbe tondue — la douceur "
  "qui fait repousser. « Sang précieux » (72:14 — P547, voir 1996800) : la vie des "
  "pauvres a du prix aux yeux du roi — l'économie du Royaume à l'envers de celle "
  "des tyrans. « On priera sans cesse » (72:15 — P547) : l'intercession perpétuelle "
  "pour le Roi — et du Roi."
 ),
 interpretation=(
  "Les portes et l'élévation (Ac 1:9-11 — P534) : le Roi monte, une nuée le "
  "dérobe, « il reviendra de la même manière » — les portes du ciel se sont levées "
  "comme celles de Jérusalem. Le trône pour toujours (Hé 1:8-9 — P540) : « Mais au "
  "sujet du Fils : Ton trône, ô Dieu, est pour toujours » — le psaume nuptial "
  "devient acte d'intronisation. Salomon, 1er accomplissement (1R 4:20, 21, 25 — "
  "P547) : « Juda et Israël étaient nombreux comme le sable » (4:20), le royaume "
  "« depuis le Fleuve jusqu'au pays des Philistins » (4:21 — l'Euphrate à la mer, "
  "comme 72:8), « chacun sous sa vigne et sous son figuier » (4:25 — voir R003 : "
  "Mi 4:4). « Plus que Salomon » (Mt 12:42 — C8, cité via 1996800 : aucun P, "
  "vérifié) : Jésus se déclare supérieur au fils de David — la prière de David "
  "dépasse David. Tarsis, Shéba, Séba (72:10 — P547) : les rois lointains apportent "
  "l'offrande — Tarsis, voir L005 (non tranché) ; la reine de Shéba montera "
  "effectivement à Jérusalem (1R 10 — C8 : aucun P, vérifié). « L'or de Shéba » "
  "(72:15 — P547) : le tribut devenu hommage."
 ),
 hist=(
  "L'arche à Jérusalem (2S 6 — C8) : halte chez Obed-Édom, seconde montée dans "
  "l'allégresse, David « dansant de toutes ses forces » — le Psaume 24 chante ce "
  "jour-là. Portes antiques : vantaux de bois sur gonds de pierre, linteaux bas — "
  "« levez vos têtes » (24:7) suppose des portes personnifiées sommées de s'ouvrir "
  "tout grand (repère d'architecture, sans lien). Noces royales du Proche-Orient "
  "ancien : cortèges, parfums, ivoire (45:8-17 — HORS P540 : voir les limites, non "
  "développé). Salomon (1R 4 — P547) : quarante ans de paix, douze intendants, "
  "provisions « comme le sable de la mer » ; la visite de Shéba (1R 10 — C8) "
  "confirme le rayonnement — « il n'y eut plus d'esprit en elle » (paraphrase du "
  "récit, C8). « Lécheront la poussière » (72:9 — P547) : la prosternation totale "
  "des vaincus — geste attesté des cours orientales (repère, sans lien)."
 ),
 geo=(
  "Jérusalem et ses portes (24:7-10) : la montée — ville basse vers ville haute, "
  "l'arche vers Sion. « D'une mer à l'autre » (72:8 — P547) : de la Méditerranée à "
  "la mer Morte (ou au golfe d'Aqaba — non tranché ici), « jusqu'au Fleuve » "
  "(l'Euphrate, 1R 4:21 — P547) : le croissant salomonien. Tarsis (72:10 — P547, "
  "voir L005 : localisation non tranchée), Shéba et Séba (72:10 — P547 : Arabie du "
  "Sud et régions du pourtour — hedged, voir les limites). Le désert (72:9 — "
  "P547) : « ceux du désert fléchiront le genou » — les marges nomades soumises. "
  "Le regain (72:6) : les chaumes de Judée après la fauche — la pluie qui les "
  "reverdit."
 ),
 sci=(
  "Hydraulique (72:6) : la pluie d'arrière-saison (malkosh) sur le regain — le cycle "
  "des averses judéennes, la repousse des chaumes : le roi-fécondité en image "
  "agronomique. Botanique (1R 4:25 — P547) : « vigne et figuier » — la polyculture "
  "vivrière judéenne, chacun nourri de son lot : voir R003. Architecture : portes, "
  "gonds, linteaux — la mécanique des vantaux antiques derrière « levez vos têtes ». "
  "Acoustique liturgique : l'antiphonie (24:7-10) — deux chœurs, dehors et dedans, "
  "question et réponse : le psaume est une partition. Métallurgie-tribut : « l'or "
  "de Shéba » (72:15 — P547) — les routes de l'or arabique (repère, sans lien ; "
  "Shéba : voir les limites)."
 ),
 limites=(
  "Psaume 45:8-17 (noces, parfums, fille de Tyr, ivoire) : HORS P540 (45:2-7 seul) — "
  "non développé ; aucun P sur 45:8+ (vérifié : P540 seul sur Ps 45). Psaume 24 : "
  "aucun article wol (TM seule — nwtsty 19/24, texte intégral versé). Shéba/Séba : "
  "localisations hedged (Arabie et pourtour) ; Tarsis : voir L005 (non tranché). "
  "1R 10 (reine de Shéba), 2S 6 (arche), Mt 12:42 (« plus que Salomon ») : C8 — "
  "aucun P (vérifiés). P766 (Hé 1:5-9) est LIBRE : non cité comme P — Hé 1:8-9 n'est "
  "versé que comme accomplissement de P540. P547 : 1er accomplissement (Salomon) — "
  "la plénitude messianique reste partiellement À venir, AUCUNE date."
 ),
 accomplissement=[("Portes levées", "Le Roi de gloire entre (24:7-10 — P534)"),
     ("Élévation", "Nuée, « reviendra ainsi » (Ac 1:9-11 — P534)"),
     ("Trône pour toujours", "« Au sujet du Fils » (Hé 1:8-9 — P540)"),
     ("Prière pour Salomon", "David âgé (Ps 72 — P547, voir 1996800)"),
     ("Paix salomonienne", "Nombreux, en sécurité (1R 4 — P547)"),
     ("Plus que Salomon", "Jésus supérieur (Mt 12:42 — C8, via article)")],
 tl=[("Montée de l'arche (repère)", "David danse (2S 6 — C8)"),
     ("Vieux jours de David (repère)", "Prière pour Salomon (Ps 72 — P547)"),
     ("Règne de Salomon (repère)", "Mer à mer, vigne-figuier (1R 4 — P547)"),
     ("Ascension (33)", "Portes du ciel levées (Ac 1:9-11 — P534)"),
     ("Hébreux (Ier s.)", "Trône pour toujours au Fils (Hé 1:8-9 — P540)"),
     ("À venir (partiel)", "Plénitude du règne (P547) — aucune date")],
 src=[("Les Psaumes — si n° 19 (Ps 72, prière pour Salomon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Le Psaume 72 (David âgé, sang précieux, plus que Salomon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1996800"),
      ("Psaume 24 — Bible d'étude, texte intégral", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/24"),
      ("Psaume 45 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/45"),
      ("Psaume 72 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/72")],
 img="images/prophe_S002_portes.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S003", titre="Psaume 110 — prêtre pour toujours à la manière de Melchisédek",
 ref="Psaume 110:1-7",
 statut="Accomplie (P554, P609) / En cours (P553) / À venir (P555) ; 110:1 en rappel d1",
 cat="S", syst="Système Melchisédek (Salem → serment → torrent)",
 reg="Registre : Psaumes — P553 (110:2-3 : verge depuis Sion), P554 (110:4 : prêtre Melchisédek), P609 (110:4 : Hé 5-7), P555 (110:5-7 : jugera, torrent) ; rappels P552/P608 (110:1 : voir d1 — Mt 22:44, Ac 2:34-35, Hé 1:13), P073 (2S 7:8-16 : voir j2)",
 texte=[
  "« ASSIEDS-TOI à ma droite. » (110:1 — rappels P552/P608, voir d1 : le verset le plus cité !)",
  "« La VERGE de ta force : Jéhovah étendra ton sceptre DEPUIS SION. » (110:2 — P553 : depuis Sion !)",
  "« Ton peuple S'OFFRIRA VOLONTAIREMENT au jour de ta force. » (110:3 — P553 : les volontaires !)",
  "« Jéhovah a JURÉ, et il ne le regrettera pas. » (110:4 — P554, P609 : le serment !)",
  "« Tu es PRÊTRE POUR TOUJOURS à la manière de MELCHISÉDEK. » (110:4 — P554, P609 : pour toujours !)",
  "« Il JUGERA parmi les nations… il boira au TORRENT en chemin. » (110:5-7 — P555 : le torrent !)",
 ],
 contexte=(
  "« De David » (suscription) — et le psaume le plus cité du Nouveau Testament : "
  "son premier verset (« assieds-toi à ma droite ») est traité en d1 (P552 : "
  "Mt 22:44 ; Ac 2:34-35 ; Hé 1:13 — P608 : voir d1), non re-traité ici. Reste le "
  "psaume du Roi-Prêtre : un dialogue — Jéhovah parle au « Seigneur » de David "
  "(110:1) — puis un serment (110:4), puis une marche guerrière (110:5-7). Jésus "
  "s'en est servi face aux Pharisiens (Mt 22:41-46 — voir d1 via P552) : « Si David "
  "l'appelle Seigneur, comment est-il son fils ? » — la question qui fait taire. "
  "L'épître aux Hébreux en fait sa charte sacerdotale (Hé 5-7 — P554, P609) : le "
  "Christ prêtre « à la manière de Melchisédek » — voir 1974167 (les deux versets "
  "pairés : Ps 2:7 + Ps 110:4) et 1968282 (le serment, le 16 nisan 33)."
 ),
 explication=(
  "« À ma droite » (110:1 — rappels P552/P608) : la place du co-régent, l'escabeau "
  "promis pour les ennemis — voir d1. « Depuis Sion » (110:2 — P553) : le sceptre "
  "ne reste pas à Sion, il EN PART — « au milieu de tes ennemis » : le règne "
  "contesté, étendu en territoire hostile ; Sion, voir S001 (2:6) et S002 (24). "
  "« Volontairement » (110:3 — P553) : pas de conscrits — le peuple s'offre au jour "
  "de la force ; l'hébreu du verset est difficile (rosée, aurore, jeunesse — "
  "paraphrase prudente, voir les limites). « Jéhovah a juré » (110:4 — P554, P609) : "
  "Dieu JURE — sans appel, sans regret (voir 1968282). « À la manière de "
  "Melchisédek » (110:4 — P554, P609) : NON une succession lévitique — un ORDRE "
  "autre (voir 1974167 : Hé 7:11-14 — Jésus, de Juda, pas de Lévi). Melchisédek "
  "(Gn 14:18-20 — C8 : aucun P, vérifié) : roi de Salem ET prêtre du Très-Haut, "
  "pain et vin à Abraham, bénédiction, dîme reçue — « Roi de Justice » (son nom), "
  "« Roi de Paix » (Salem) — voir 1968282. « Il boira au torrent » (110:7 — "
  "P555) : le guerrier qui se désaltère SANS s'arrêter — la victoire en marche."
 ),
 interpretation=(
  "Le couple Roi-Prêtre (Hé 5:5-6 — P524/P599 et P554/P609) : « Tu es mon fils » "
  "(Ps 2:7) + « Tu es prêtre pour toujours » (Ps 110:4) — le même « aujourd'hui » "
  "fait les deux (voir 1974167 ; voir S001). Grand Prêtre nommé (Hé 5:10 ; 6:20 ; "
  "7:17, 21 — P554 ; Hé 5:5-6, 10 ; 7:15-17 — P609) : « nommé par Dieu grand prêtre "
  "à la manière de Melchisédek », « précurseur entré pour nous » (6:20), « prêtre "
  "pour toujours » (7:17) — « avec serment » (7:21). Non-Lévi (Hé 7:11-14 — voir "
  "1974167) : « notre Seigneur est issu de Juda » — la perfection ne venant pas du "
  "sacerdoce lévitique, il faut un prêtre d'un autre ordre. Le 16 nisan 33 (voir "
  "1968282) : le serment prend effet à la résurrection — le Prêtre vivant entre au "
  "ciel. En cours (P553) : le sceptre étendu « au milieu de tes ennemis » — le "
  "règne contesté, encore combattu. À venir (P555) : « il jugera parmi les nations » "
  "— Ré 19:15 (P555) et Dn 2:44 (P555) ; le torrent bu en chemin — la marche ne "
  "s'arrête pas."
 ),
 hist=(
  "Melchisédek (Gn 14:18-20 — C8) : après la campagne des quatre rois de l'est "
  "contre les cinq de la plaine, le roi de Salem sort au-devant d'Abram avec du "
  "pain et du vin, bénit « Abram par le Dieu Très-Haut », reçoit la dîme « de "
  "tout ». Pain et vin : l'hospitalité du Proche-Orient ancien (repère de coutume, "
  "sans lien). Dîme antérieure à Lévi : Abram donne 10 % des siècles avant la Loi — "
  "l'ordre melchisédekien précède et dépasse l'ordre lévitique (voir 1974167). "
  "Salem : la ville du prêtre-roi — la future Jérusalem (identification "
  "traditionnelle : voir les limites). Serment divin : Dieu ne jure que par "
  "lui-même — le serment de 110:4 est sans instance supérieure (voir 1968282). "
  "Nathan à David (2S 7:8-16 — rappel P073, voir j2) : la maison, le trône, le "
  "royaume — le serment de Ps 110:4 en est l'écho sacerdotal."
 ),
 geo=(
  "Salem (Gn 14:18 — C8) : la cité du prêtre-roi — sur les monts de Judée, là où "
  "s'élèvera Jérusalem. Sion (110:2 — P553) : le point de départ du sceptre — la "
  "montagne d'où part l'extension. « Au milieu de tes ennemis » (110:2 — P553) : "
  "le territoire contesté — le règne ne s'étend pas sur du vide, mais sur de "
  "l'hostile. Les nations jugées (110:6 — P555) : « plein de cadavres » — le champ "
  "du jugement dernier (voir S001 : vase de potier). Le torrent (110:7 — P555) : "
  "les oueds de Palestine — l'eau vive bue en marchant, sans quitter la poursuite."
 ),
 sci=(
  "Philologie : adoni (« mon Seigneur », 110:1) — David appelle « Seigneur » son "
  "propre descendant, l'énigme de Mt 22 (voir d1) ; al-divrati (« à la manière de », "
  "110:4) — l'ordre, non la succession ; Melchisédek (« roi de justice »), Salem "
  "(« paix ») — voir 1968282. Hydrologie : le torrent (110:7) — l'oued à débit "
  "saisonnier, l'eau courante du guerrier en marche ; physiologie : boire sans "
  "rompre la poursuite — l'endurance du vainqueur. Chronologie : « prêtre POUR "
  "TOUJOURS » (110:4 — P554, P609) — la perpétuité contre la mortalité : les "
  "prêtres lévitiques meurent et se succèdent, celui-ci demeure — l'argument de "
  "Hé 7 tout entier (voir 1974167). Astronomie-poétique (110:3) : aurore, rosée — "
  "la jeunesse du peuple comme rosée du matin (paraphrase prudente — voir les "
  "limites)."
 ),
 limites=(
  "Psaume 110:1 : HORS fiche — rappels P552 (Mt 22:44 ; Ac 2:34-35 ; Hé 1:13) et P608, "
  "voir d1 ; le verset n'est pas re-traité, seulement cité en tête. Psaume 110:3 : "
  "hébreu difficile — paraphrase prudente (« peuple volontaire »), pas de leçon "
  "tranchée. Salem = Jérusalem : identification traditionnelle, non démontrée ici — "
  "le récit dit « Salem », point (Gn 14:18 — C8). Melchisédek : le récit ne donne "
  "ni généalogie ni fin — aucune spéculation versée (voir 1968282, 1974167). "
  "P553 (En cours) : le « depuis quand » n'est pas daté ici. P555 (À venir) : "
  "AUCUNE date. C8 : Gn 14:18-20 (Melchisédek) — aucun P (vérifié)."
 ),
 accomplissement=[("À ma droite", "Escabeau promis (110:1 — rappels P552/P608, d1)"),
     ("Sceptre depuis Sion", "Étendu parmi les ennemis (110:2-3 — P553, En cours)"),
     ("Serment", "Jurée, sans regret (110:4 — P554, P609)"),
     ("Prêtre Melchisédek", "Nommé, entré, pour toujours (Hé 5-7 — P554, P609)"),
     ("16 nisan 33", "Le Prêtre vivant (résurrection — voir 1968282)"),
     ("Torrent à venir", "Jugera, boira en chemin (110:5-7 — P555)")],
 tl=[("Abram (repère)", "Pain, vin, dîme à Salem (Gn 14 — C8)"),
     ("David (repère)", "« De David » — le dialogue (Ps 110)"),
     ("Ministère (Ier s.)", "« Comment est-il son fils ? » (Mt 22 — voir d1)"),
     ("16 nisan 33", "Serment en effet (résurrection — P554, P609)"),
     ("Hébreux (Ier s.)", "Charte sacerdotale (Hé 5-7 — P554, P609)"),
     ("En cours → À venir", "Sceptre étendu, jugement (P553, P555) — aucune date")],
 src=[("Les Psaumes — si n° 19 (David, les Psaumes messianiques)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Roi et Prêtre (Ps 2:7 + Ps 110:4, Hé 7:11-14)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1974167"),
      ("Le serment (prêtre pour toujours, 16 nisan 33)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1968282"),
      ("Psaume 110 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/110")],
 img="images/prophe_S003_melchisedek.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S004", titre="Trahi, haï, percé — la Passion chantée d'avance",
 ref="Psaume 22:7, 8, 16 ; Psaume 27:12 ; Psaume 31:5, 11-13 ; Psaume 35:11-19 ; Psaume 55:12-14 ; Psaume 69:4, 9, 22-28 ; Psaume 109:25",
 statut="Accomplie (P541, P616, P543, P544, P606, P546, P621, P537, P619, P620, P631, P633, P637, P535)",
 cat="S", syst="Système Passion (trahison → procès → poteau → remise)",
 reg="Registre : Psaumes — P541/P616 (55:12-14 : trahi par l'ami), P543 (69:4 : haï sans cause), P544/P606 (69:9 : zèle dévoré), P546 (69:22-28 : table-piège, sa charge), P621 (35:19 ; 69:4 : haï sans cause), P537/P619 (35:11-19 : faux témoins), P620 (27:12 : faux témoins), P631 (22:7-8 : raillent, hochent), P633 (22:16 : percé), P637 (109:25 : hochent la tête), P535 (31:5, 11-13 : remets mon esprit) ; rappels P539/P613 (41:9 : voir d1), P545/P635 (69:21 : voir e1), P551/P617 (109:8 : voir d1), P529/P531/P532/P630/P634 (Ps 22 : voir d1), P632 (Ps 22 : voir e1), P527/P642 (Ps 16 : voir d1)",
 texte=[
  "« Ce n'est pas un ENNEMI qui m'outrage… mais TOI, mon COMPAGNON. » (55:12-14 — P541, P616 : l'ami !)",
  "« Ceux qui me HAÏSSENT SANS CAUSE sont plus nombreux que les CHEVEUX de ma tête. » (69:4 — P543, P621 : sans cause !)",
  "« Le ZÈLE pour ta maison m'a DÉVORÉ. » (69:9 — P544, P606 : le zèle !)",
  "« Que leur TABLE devienne un PIÈGE… qu'un AUTRE prenne sa CHARGE. » (69:22-28 — P546 : la charge !)",
  "« De FAUX TÉMOINS se lèvent. » (35:11 ; 27:12 — P537, P619, P620 : les faux !)",
  "« Tous ceux qui me voient me RAILLENT… ils HOCHENT la tête. » (22:7-8 ; 109:25 — P631, P637 : les hochements !)",
  "« Il s'est appuyé sur Jéhovah — qu'IL LE DÉLIVRE ! » (22:8 — P631 : le défi !)",
  "« Ils ont PERCÉ mes MAINS et mes PIEDS. » (22:16 — P633 : les clous !)",
  "« Je suis en BUTTE À L'EFFROI… OUBLIÉ comme un mort. » (31:11-13 — P535 : l'effroi !)",
  "« Entre tes MAINS je REMETS mon esprit. » (31:5 — P535 : le dernier cri !)",
 ],
 contexte=(
  "Sept psaumes, une Passion. Le Psaume 55 : David trahi — l'ami devenu ennemi "
  "(arrière-plan : Achitophel, le conseiller passé à Absalom, 2S 15-17 — C8 : "
  "aucun P, vérifié) ; application à Judas (P541 : « application à la trahison de "
  "Judas » ; P616 : Mt 26:47-50 ; Jn 13:18 — et le talon levé de 41:9, rappels "
  "P539/P613, voir d1). Le Psaume 69 : le zélé persécuté — zèle (Jn 2:17 — P544 ; "
  "Jn 2:13-17 — P606), haine gratuite (Jn 15:25 — P543), table-piège et charge "
  "reprise (Ac 1:20 — P546 ; et 109:8, rappels P551/P617, voir d1 ; le fiel de 69:21, "
  "rappels P545/P635, voir e1). Le Psaume 35 et le 27:12 : les faux témoins du procès "
  "(Mt 26:59-61 — P537, P619, P620 ; Mc 14:55-59 — P619 ; « ils me haïssent sans "
  "cause », Jn 15:25 — P537, et Jn 15:23-25 — P621). Le Psaume 22 : les railleries "
  "et les clous (Mt 27:39-43 — P631 ; Jn 19-20 — P633 ; le reste du psaume, rappels "
  "d1/e1). Le Psaume 109:25 : les hochements (Mt 27:39 — P637). Le Psaume 31 : "
  "l'effroi, l'abandon (Mt 26:56 — P535) et le dernier cri (Lc 23:46 — P535). Le "
  "procès et le poteau, détaillés, sont en D (D001-D009) : ici, les psaumes seuls."
 ),
 explication=(
  "« Pas un ennemi » (55:12-14 — P541, P616) : la trahison ne vient pas du dehors — "
  "« toi, mon compagnon, mon intime ami » (P616) : la table partagée, le baiser "
  "(Mt 26:49 — P616). « Sans cause » (hinnam — 35:19 ; 69:4 — P543, P621, P537) : "
  "gratuitement, pour rien — trois fois dans les psaumes, une fois dans la bouche "
  "de Jésus : « ils m'ont haï sans cause » (Jn 15:25). « Zèle dévoré » (69:9 — "
  "P544, P606) : le feu pour la maison consume son porteur — les disciples "
  "« se souvinrent » (Jn 2:17). « Table-piège » (69:22 — P546) : l'hospitalité "
  "inversée — la table qui nourrit devient le piège qui prend ; « sa charge » "
  "(episkopé, 69:25 — P546 ; 109:8 — rappels P551/P617) : la fonction reprise par "
  "Matthias (Ac 1:20-26 — P546). « Faux témoins » (35:11 ; 27:12 — P537, P619, "
  "P620) : « violents », questionnant « sur ce que je ne sais pas » (P619) — et "
  "« leurs témoignages ne concordaient pas » (Mc 14:56-59 — P619). « Percé » (22:16 "
  "— P633) : l'hébreu est discuté (ka'ari/karu), la Traduction du monde nouveau "
  "tranche « ils ont percé » — voir nwtsty 19/22 et les limites. « Remets » (31:5 — "
  "P535) : le dépôt confié — l'esprit remis comme en garde, avant l'abandon de "
  "tous (Mt 26:56 — P535 : « tous l'abandonnèrent »)."
 ),
 interpretation=(
  "Judas (Mt 26:47-50 ; Jn 13:18 — P616 ; application — P541) : la foule, les épées, "
  "le baiser — « Compagnon, fait ce pour quoi tu es venu » ; « celui qui mangeait "
  "mon pain a levé son talon contre moi » (41:9 — rappels P539/P613, voir d1). Le "
  "Temple purifié (Jn 2:13-17 — P606 ; Jn 2:17 — P544) : les tables renversées, les "
  "colombes libérées — « ne faites pas de la maison de mon Père une maison de "
  "commerce » — et les disciples se souviennent du zèle dévorant. La haine (Jn "
  "15:23-25 — P621 ; Jn 15:25 — P543, P537) : « ils ont haï et moi et mon Père… "
  "ils m'ont haï sans cause » — la haine gratuite, annoncée deux fois (35:19 ; "
  "69:4). Le procès (Mt 26:59-61 — P537, P619, P620 ; Mc 14:55-59 — P619) : le "
  "Sanhédrin de nuit cherche de faux témoignages — « je peux détruire le temple » — "
  "détails en D. Les railleries (Mt 27:39-43 — P631 ; Mt 27:39 — P637) : passants, "
  "prêtres, hochements — « il s'est appuyé sur Dieu, qu'il le délivre » (22:8). "
  "Les clous (Jn 19:18, 23, 37 — P633) : dressé, partagé, transpercé ; Thomas : "
  "« mets ton doigt… » (Jn 20:25-27 — P633). Le dernier cri (Lc 23:46 — P535) : "
  "« Père, entre tes mains je remets mon esprit » — le 31:5 sur les lèvres du "
  "mourant ; et l'effroi, l'oubli « comme un mort » (31:11-13 — P535), quand tous "
  "s'enfuient (Mt 26:56 — P535)."
 ),
 hist=(
  "Achitophel (2S 15-17 — C8) : le conseiller de David passé à Absalom — son avis "
  "« comme une parole de Dieu », son suicide à la défaite : l'archétype de "
  "l'ami-traître (repère de récit, C8). Le Sanhédrin de nuit : procès nocturne, faux "
  "témoins cherchés puis discordants (Mc 14:56-59 — P619) — les irrégularités du "
  "procès, voir D (renvoi, pas de doublon). Le supplice romain : dressement, "
  "partage des vêtements (tirés au sort — 22:18, voir d1), transpercement — voir D "
  "pour le poteau ; ici : les clous annoncés (22:16 — P633). Le fiel et le vinaigre "
  "(69:21 — rappels P545/P635, voir e1) : non développés. La fosse non vue (Ps 16 — "
  "rappels P527/P642, voir d1) : la résurrection après la Passion — renvoi."
 ),
 geo=(
  "La maison (69:9 — P544, P606) : le Temple — ses parvis, ses tables de change, "
  "ses colombes : le zèle y éclate. La table (69:22 — P546) : la table judéenne — "
  "tapis, plats partagés — devenue piège. Le prétoire et la nuit (Mt 26:59 — P537, "
  "P619, P620) : Jérusalem haute, la maison de Caïphe — voir D. Le lieu du "
  "supplice (Mt 27 — P631, P637 ; Jn 19 — P633) : hors les murs — passants qui "
  "hochent, soldats qui percent — voir D. « Entre tes mains » (31:5 — P535) : pas "
  "de lieu — les mains du Père, la seule géographie du dernier cri."
 ),
 sci=(
  "Philologie : hinnam (« sans cause », 35:19 ; 69:4) — gratuitement, pour rien ; "
  "episkopé (« charge de surveillance », 69:25 ; 109:8) — la fonction reprise ; "
  "ka'ari/karu (« percé », 22:16) — le massorétique discuté, les versions anciennes "
  "(grecque : « ils ont percé ») tranchant avec la TM — voir nwtsty 19/22. Médecine "
  "du supplice : mains et pieds percés (22:16 — P633), « la marque des clous » "
  "(Jn 20:25 — P633) — voir D pour le poteau. Psychologie : la trahison intime "
  "(55:12-14 — le baiser fait plus mal que l'épée), la foule qui hoche (22:7 ; "
  "109:25 — le ricanement grégaire), l'abandon total (31:11-13 ; Mt 26:56 — "
  "« oublié comme un mort »). Mnémotechnique : « ils se souvinrent » (Jn 2:17 — "
  "P544) — l'Écriture reconnue APRÈS, la prophétie comme mémoire à retardement."
 ),
 limites=(
  "Psaume 22:1, 14-15, 17-18 : rappels (P529/P531/P532/P630/P634 voir d1 ; P632 voir "
  "e1) — non re-traités ; seul 22:7-8 (P631) et 22:16 (P633) sont versés ici. "
  "Psaume 69:21 (fiel, vinaigre) : rappels P545/P635, voir e1 — non développé. "
  "Psaume 109:8 (sa charge) : rappels P551/P617, voir d1 — seul 109:25 (P637) est "
  "versé. Psaume 41:9 (talon levé) : rappels P539/P613, voir d1. Psaume 16 (la "
  "fosse non vue) : rappels P527/P642, voir d1. Psaume 22:16 : hébreu discuté — la "
  "TM tranche « percé » (voir nwtsty 19/22) ; aucune leçon concurrente tranchée ici. "
  "Procès et poteau détaillés : voir D (renvoi systématique, pas de doublon). C8 : "
  "2S 15-17 (Achitophel) — aucun P (vérifié)."
 ),
 accomplissement=[("Ami-traître", "Baiser de Judas (Mt 26:47-50 — P541, P616)"),
     ("Zèle dévorant", "Temple purifié (Jn 2:13-17 — P544, P606)"),
     ("Haine gratuite", "« Sans cause » (Jn 15:23-25 — P543, P621, P537)"),
     ("Table-piège", "Charge reprise (Ac 1:20 — P546)"),
     ("Faux témoins", "Procès de nuit (Mt 26:59-61 — P537, P619, P620)"),
     ("Raillés, percé, remis", "Hochements, clous, dernier cri (P631, P633, P637, P535)")],
 tl=[("David trahi (repère)", "L'ami Achitophel (2S 15-17 — C8)"),
     ("Début du ministère", "Zèle au Temple (Jn 2 — P544, P606)"),
     ("Dernière nuit", "Baiser, fuite (Mt 26 — P616, P535)"),
     ("Procès de nuit", "Faux témoins (Mt 26:59-61 — P537, P619, P620)"),
     ("Poteau (33)", "Railleries, clous (Mt 27 ; Jn 19 — P631, P633, P637)"),
     ("Dernier cri", "« Je remets » (Lc 23:46 — P535)")],
 src=[("Les Psaumes — si n° 19 (David, psaumes de la Passion)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Psaume 22 — Bible d'étude, notes (percé)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/22"),
      ("Psaume 69 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/69"),
      ("Psaume 35 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/35"),
      ("Psaume 55 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/55")],
 img="images/prophe_S004_passion.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S005", titre="Offert, gardé, délivré — le Serviteur préservé",
 ref="Psaume 18:2-19 ; Psaume 40:6-8 ; Psaume 91:11, 12 ; Psaume 144:1, 2",
 statut="Accomplie (P538, P550) / Accomplie, 1er accomplissement (P528, P560)",
 cat="S", syst="Système délivrance (eaux → tente → combat)",
 reg="Registre : Psaumes — P528 (18:2-19 : eaux profondes, ennemi fort), P538 (40:6-8 : sacrifice non voulu, je viens), P550 (91:11-12 : anges porteurs), P560 (144:1-2 : mains entraînées, forteresse) ; renvoi C (tentation, ministère)",
 texte=[
  "« Il m'a TIRÉ des EAUX PROFONDES… DÉLIVRÉ de mon ennemi FORT. » (18:16-17 — P528 : les eaux !)",
  "« SACRIFICE et offrande, tu n'en as pas VOULU. » (40:6 — P538 : non voulu !)",
  "« VOICI, je viens FAIRE TA VOLONTÉ. » (40:8 — P538 : je viens !)",
  "« Tu m'as PRÉPARÉ un CORPS… dans le ROULEAU, il est écrit à mon sujet. » (Hé 10:5, 7 — P538 : le corps !)",
  "« Il donnera ORDRE à ses ANGES… ils te PORTERONT sur leurs mains. » (91:11-12 — P550 : les porteurs !)",
  "« Il ENTRAÎNE mes mains au COMBAT… mon REFUGE et ma FORTERESSE. » (144:1-2 — P560 : l'entraîneur !)",
 ],
 contexte=(
  "Quatre psaumes, une préservation. Psaume 18 : le chant du délivré — suscription : "
  "« le jour où Jéhovah l'avait délivré de la main de tous ses ennemis et de la "
  "main de Saül » (voir 1980885) ; le même chant figure en 2 Samuel 22 (P528 : « 2 "
  "Samuel 22 (récit) ; application messianique ») — deux exemplaires, un délivré. "
  "Psaume 40 : l'offert — « sacrifice non voulu… je viens faire ta volonté » "
  "(40:6-8 — P538), repris en Hébreux 10:5-10 (P538) : « tu m'as préparé un corps… "
  "Vois ! Je viens… pour faire ta volonté… Il supprime le premier afin d'établir le "
  "second… sanctifiés grâce à l'offrande du corps… une fois pour toutes ». Psaume 91 "
  "(anonyme) : le gardé — Satan lui-même le CITE (Mt 4:6 ; Lc 4:10-11 — P550 : "
  "« Accomplie (citation) ») : la seule prophétie du registre accomplie par "
  "citation détournée ! Psaume 144 (« de David ») : le guerrier instruit — Dieu "
  "entraîne les mains (144:1-2 — P560) ; le verset 2 (« Celui qui me fait échapper ») "
  "est cité dans l'article sur l'évasion divine (voir 1980885 : 18:2 ; 40:17 ; "
  "70:5 ; 144:2 — 40:17 est C8 : aucun P, vérifié)."
 ),
 explication=(
  "« Sacrifice non voulu » (40:6 — P538) : Dieu veut l'obéissance, pas le rituel — "
  "« obéir vaut mieux que sacrifice » (1S 15:22 — C8 : aucun P, vérifié). « Corps "
  "préparé » (Hé 10:5 — P538) : là où l'hébreu dit « des oreilles ouvertes » "
  "(40:6), la version grecque citée par Paul dit « un corps » — les deux disent "
  "l'obéissance incarnée (voir nwtsty 19/40 et 58/10 ; voir les limites). « Dans le "
  "rouleau » (Hé 10:7 — P538) : la Torah parlait de lui — « les Psaumes » de "
  "Lc 24:44 (voir si, 1101990080). « Supprime le premier » (Hé 10:9 — P538) : "
  "l'alliance de la Loi abolie par l'offrande « une fois pour toutes » (10:10). "
  "« Anges porteurs » (91:11-12 — P550) : la garde rapprochée — mais Satan OMET "
  "« dans toutes tes voies » (91:11) : il cite, il tronque, il tente. « Eaux "
  "profondes » (18:16 — P528) : le chaos, la mort — « il m'a tiré » : le sauvetage ; "
  "1er accomplissement David, « application messianique » (P528) — prudence du "
  "registre, voir les limites. « Entraîne mes mains » (144:1 — P560) : Dieu "
  "instructeur de guerre — le Roi guerrier de S003 (110:5-7) fait ses classes."
 ),
 interpretation=(
  "Le « je viens » (Hé 10:5-10 — P538) : du baptême au poteau — une vie offerte, "
  "un corps préparé, une offrande unique : « sanctifiés… une fois pour toutes ». "
  "La tentation (Mt 4:6 ; Lc 4:10-11 — P550) : « Si tu es fils de Dieu, jette-toi — "
  "car il est écrit… » — Satan théologien, citant le Psaume 91 ; Jésus répond par "
  "le Deutéronome : « tu ne dois pas mettre Jéhovah à l'épreuve » (Dt 6:16 — C8 : "
  "aucun P, vérifié) — détails en C (ministère). David délivré : la lance de Saül "
  "— « Saül lança sa lance… David esquiva deux fois » (1S 18 — C8 : aucun P, "
  "vérifié ; voir 2008682 : Ps 18:17-19, 48) ; puis le chant jumeau (Ps 18 = 2S 22 — "
  "P528) : « il m'a fait sortir au large » (18:19). « Celui qui donne d'échapper » "
  "(voir 1980885) : le titre divin en chaîne — 18:2, 40:17 (C8), 70:5 (C8 : voir "
  "les limites), 144:2 (P560) — Dieu l'évasion, Dieu le refuge, Dieu la forteresse "
  "(144:2 — P560)."
 ),
 hist=(
  "La lance (1S 18 — C8 ; voir 2008682) : le javelot du roi — Saül le lance en "
  "jouant David de la harpe, deux esquives : la guérilla avant la royauté. Les "
  "sacrifices (40:6 — P538) : holocaustes, offrandes pour le péché — le système "
  "lévitique que le « je viens » vient accomplir ET supprimer (Hé 10:9 — P538 ; "
  "voir R002 : l'alliance). La tentation au sommet : « le haut du Temple » (Mt 4:5 "
  "— paraphrase du récit) — le vide sous les pieds, les anges en promesse. Les "
  "guerres de David (arrière-plan de 144:1 — P560) : Philistins, Moab, Aram — des "
  "mains entraînées par les batailles, attribuées à Dieu l'instructeur."
 ),
 geo=(
  "« Les eaux profondes » (18:16 — P528) : la mer-chaos du Proche-Orient — le "
  "sauvetage comme sortie des flots. « Au large » (18:19 — P528) : l'espace ouvert "
  "après l'étreinte — la délivrance comme élargissement. Le désert de la tentation "
  "(Mt 4 — P550) : la Judée pierreuse — quarante jours, les bêtes, puis le "
  "Tentateur (détails en C). Le haut du Temple (Mt 4:5 — P550) : Jérusalem, le "
  "parvis royal — le saut proposé, refusé. La forteresse (144:2 — P560) : Sion, "
  "Adullam, les refuges de David — Dieu comme lieu."
 ),
 sci=(
  "Philologie : « oreilles » (hébreu, 40:6) contre « corps » (grecque, Hé 10:5) — "
  "les deux leçons versées, l'obéissance incarnée dans les deux cas (voir nwtsty "
  "19/40 ; 58/10) ; palat (« échapper », 18:2 ; 40:17 ; 144:2) — le verbe devenu "
  "titre divin (voir 1980885). Balistique : la lance lancée à bout portant (1S 18 — "
  "C8) — vitesse, surprise, double esquive : les réflexes du futur roi (voir "
  "2008682). Stratégie : « entraîne mes mains » (144:1 — P560) — la formation "
  "martiale attribuée à Dieu : fronde, épée, arc — l'école du berger devenu roi. "
  "Textologie : Ps 18 = 2S 22 — le même chant en deux exemplaires, variantes "
  "mineures : la transmission à l'œuvre (P528)."
 ),
 limites=(
  "« Corps » contre « oreilles » (40:6 ; Hé 10:5) : les deux leçons sont versées "
  "SANS que l'une annule l'autre — Paul cite la grecque, l'hébreu dit les oreilles "
  "ouvertes (voir nwtsty). Psaume 91 : auteur anonyme — non tranché ; aucun article "
  "wol (externes seuls — non versés). Psaume 40 : aucun article wol (Hé 10 fait "
  "foi — nwtsty 58/10, texte intégral versé). P528/P560 : 1ers accomplissements "
  "(David) — « application messianique » prudente selon le registre, non forcée. "
  "Tentation détaillée : voir C (ministère). C8 : 1S 15:22 (obéir vaut mieux), 1S 18 "
  "(la lance), Dt 6:16 (ne pas mettre à l'épreuve), Ps 40:17 et 70:5 (échapper) — "
  "aucun P (vérifiés)."
 ),
 accomplissement=[("Eaux profondes", "Tiré, délivré (18:16-19 — P528, 1er acc.)"),
     ("Chant jumeau", "Ps 18 = 2S 22 (P528) ; lance esquivée (1S 18 — C8)"),
     ("Je viens", "Corps préparé, volonté faite (Hé 10:5-10 — P538)"),
     ("Une fois pour toutes", "Premier supprimé, sanctifiés (Hé 10:9-10 — P538)"),
     ("Anges cités", "Satan tronque, Jésus refuse (Mt 4:6 — P550)"),
     ("Mains entraînées", "Refuge, forteresse (144:1-2 — P560, 1er acc.)")],
 tl=[("Saül (repère)", "Lance esquivée ×2 (1S 18 — C8, voir 2008682)"),
     ("Roi délivré (repère)", "Chant jumeau (Ps 18 = 2S 22 — P528)"),
     ("Baptême → poteau", "« Je viens » vécu (Hé 10:5-10 — P538)"),
     ("Tentation (Ier s.)", "Ps 91 cité et refusé (Mt 4:6 — P550)"),
     ("Guerres de David (repère)", "Mains entraînées (Ps 144 — P560)"),
     ("Évasion divine", "18:2 → 40:17 → 144:2 (voir 1980885)")],
 src=[("Les Psaumes — si n° 19 (David, Lc 24:44)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Celui qui donne d'échapper (Ps 18, suscription, 144:2)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1980885"),
      ("Délivré de Saül (Ps 18:17-19, 48 ; 1S 18)", "https://wol.jw.org/fr/wol/d/r30/lp-f/2008682"),
      ("Psaume 40 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/40"),
      ("Hébreux 10 — Bible d'étude, texte intégral", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/58/10"),
      ("Psaume 91 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/91")],
 img="images/prophe_S005_delivre.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
 n="S006", titre="L'alliance chantée — Hosanna et Royaume sans fin",
 ref="Psaume 89:3, 4, 35-37 ; Psaume 118:25, 26 ; Psaume 132:11, 12 ; Psaume 145:13 ; Psaume 146:3-10",
 statut="Accomplie (P576, P558, P577, P557) / Accomplie et À venir (P549, P561) / En cours et À venir (P562)",
 cat="S", syst="Système alliance davidique (serment → Hosanna → Royaume)",
 reg="Registre : Psaumes — P549 (89:3-4, 35-37 : alliance ferme), P576 (89:3-4, 35-36 : trône, jours du ciel), P558 (132:11 : fruit du ventre), P577 (132:11-12 : sur le trône), P557 (118:25-26 : Hosanna, Béni), P561 (145:13 : Royaume toutes époques), P562 (146:3-10 : pas aux nobles, Dieu de Jacob) ; rappels P556/P607 (118:22 : voir d1 et r1), P073 (2S 7 : voir j2)",
 texte=[
  "« J'ai conclu une ALLIANCE avec mon ÉLU… ta DESCENDANCE pour TOUJOURS. » (89:3-4 — P549, P576 : l'alliance !)",
  "« Ton TRÔNE comme le SOLEIL… comme la LUNE, ferme pour toujours. » (89:36-37 — P549, P576 : le soleil !)",
  "« Du FRUIT de ton VENTRE, je mettrai sur ton TRÔNE. » (132:11 — P558, P577 : le fruit !)",
  "« HOSANNA… BÉNI soit celui qui vient au nom de Jéhovah ! » (118:25-26 — P557 : Hosanna !)",
  "« Ton ROYAUME est un royaume pour TOUTES LES ÉPOQUES. » (145:13 — P561 : toutes les époques !)",
  "« Ne mettez PAS votre confiance dans les NOBLES… HEUREUX qui a pour secours le Dieu de JACOB. » (146:3-10 — P562 : les nobles !)",
 ],
 contexte=(
  "Cinq psaumes, une alliance qui chante jusqu'au Royaume. Psaume 89 (Éthan "
  "l'Ezrahite) : le serment — « alliance avec mon élu » (89:3-4 — P549, P576), « je "
  "ne mentirai pas à David » (89:35 — P549, P576), « trône comme le soleil, comme "
  "la lune » (89:36-37 — P549, P576 ; TM intégrale versée : 19/89) ; la plainte "
  "finale (89:38-51 — hors P : voir les limites ; 89:49 est C8 : aucun P, vérifié). "
  "Psaume 132 (montée) : le fruit du ventre sur le trône (132:11-12 — P558, P577 ; "
  "Ac 2:30 ; Lc 1:32) ; Sion choisie (132:13-18 — hors P : voir les limites). "
  "Psaume 118 (Hallel pascal — voir les limites) : Hosanna (118:25) et Béni "
  "(118:26 — P557 ; Mt 21:9) ; la pierre rejetée (118:22 — rappels P556/P607, voir "
  "d1 et r1). Psaume 145 (acrostiche, dernier psaume signé David) : le Royaume de "
  "toutes les époques (145:13 — P561 ; Dn 2:44 ; Ré 11:15). Psaume 146 (Hallel "
  "final) : pas aux nobles — au Dieu de Jacob (146:3-10 — P562 ; Ré 21:3-4). "
  "L'oracle de Nathan (2S 7:8-16 — rappel P073, voir j2) : la source de l'alliance."
 ),
 explication=(
  "« Alliance avec mon élu » (89:3 — P549, P576) : Dieu contracte — avec David, "
  "pour sa descendance ; « je ne mentirai pas » (89:35) : le serment comme en "
  "110:4 (voir S003). « Soleil, lune » (89:36-37 — P549, P576 ; « comme les jours "
  "du ciel », P576) : la pérennité cosmique — tant qu'il y aura des astres, il y "
  "aura un trône. « Fruit du ventre » (132:11 — P558, P577) : la descendance "
  "PHYSIQUE — le Messie fils de David par le sang (Ac 2:30 — P558, P577 ; "
  "Lc 1:32 — P558). « Hosanna » (118:25 — P557) : hoshi'a-na — « sauve, je te prie "
  "! » — le cri de détresse devenu acclamation royale ; « Béni soit celui qui "
  "vient » (118:26 — P557) : la formule d'accueil du pèlerin-roi. « Toutes les "
  "époques » (olam — 145:13 — P561) : le Royaume sans ère de fin. « Pas aux nobles » "
  "(146:3 — P562) : nedivim — les puissants ; « son esprit sort, il retourne au "
  "sol » (146:4 — paraphrase) : la mortalité comme argument politique ; « heureux » "
  "(146:5 — P562) : le bonheur placé, pas aux palais, au Dieu de Jacob."
 ),
 interpretation=(
  "L'Annonciation (Lc 1:32-33 — P549, P576, P558) : « il sera grand… Jéhovah Dieu "
  "lui donnera le trône de David son père… il règnera sur la maison de Jacob pour "
  "toujours » — Gabriel récite l'alliance (89:3-4 ; 132:11) à Marie. La Pentecôte "
  "(Ac 2:30 — P549, P558, P577) : David « prophète » — Dieu « lui avait juré par "
  "serment de faire asseoir sur son trône un de ses descendants » — Pierre applique "
  "le serment au ressuscité. Antioche (Ac 13:22-23 — P576) : « j'ai trouvé David… "
  "de sa descendance Dieu a amené à Israël un sauveur, Jésus ». Les Rameaux "
  "(Mt 21:9 — P557) : la foule acclame — « Hosanna… Béni soit celui qui vient ! » — "
  "et les enfants dans le Temple (Mt 21:15-16 citant 8:2 — C8 : aucun P, vérifié) ; "
  "manteaux sous les pieds — comme pour Jéhu (2R 9:13 — C8 : aucun P, vérifié). Le "
  "Royaume (Dn 2:44 — P561 ; Ré 11:15 — P561 : « le royaume du monde est devenu "
  "celui de notre Seigneur et de son Christ »). Le Dieu de Jacob (Ré 21:3-4 — "
  "P562) : « il essuiera toute larme » — la fin des nobles, le début des époques."
 ),
 hist=(
  "Nathan à David (2S 7:8-16 — rappel P073, voir j2) : « ta maison, ton royaume "
  "affermis pour toujours » — l'oracle-source de 89:3-4 et 132:11. Les Rameaux "
  "(Mt 21:9 — P557) : entrée royale — branches, manteaux étendus : le protocole de "
  "Jéhu (2R 9:13 — C8 : « ils prirent chacun son vêtement… et sonnèrent du cor : "
  "Jéhu est roi ! ») — la foule traite Jésus en roi oint. Le Hallel (Ps 113-118, "
  "chantés à la Pâque — coutume juive, repère sans lien) : Jésus et ses disciples "
  "venaient de chanter ces psaumes — la foule de Mt 21:9 chante le 118 dans la rue. "
  "Les enfants (Mt 21:15-16 — Ps 8:2, C8) : « par la bouche des enfants… tu as "
  "établi la louange » — les prêtres indignés, Jésus citant. Éthan l'Ezrahite "
  "(suscription de 89) : le sage contemporain de Salomon (1R 4:31 — C8 : voir les "
  "limites) — le serment chanté par un sage."
 ),
 geo=(
  "Sion choisie (132:13 — HORS P558/P577 : voir les limites) : le trône a une "
  "adresse — non développée ici. « La maison de Jacob » (Lc 1:33 — P549, P576) : "
  "le peuple comme maisonnée — le Royaume-maison. Jérusalem des Rameaux (Mt 21:9 — "
  "P557) : la montée, les pentes, la ville en émoi — « toute la ville fut dans "
  "l'agitation » (Mt 21:10 — paraphrase du récit). Les nations du Royaume "
  "(Dn 2:44 — P561) : la pierre qui remplit « toute la terre ». La tente de Dieu "
  "(Ré 21:3 — P562) : « la tente de Dieu est avec les humains » — la géographie "
  "finale : Dieu emménage."
 ),
 sci=(
  "Astronomie (89:36-37 — P549, P576) : soleil et lune « témoins fidèles dans le "
  "ciel » — la pérennité du trône calée sur la mécanique céleste ; « les jours du "
  "ciel » (P576) : le temps cosmique comme garantie. Philologie : Hosanna "
  "(hoshi'a-na, 118:25) — l'impératif devenu hourra ; olam (« époques », 145:13) — "
  "la durée indéfinie ; nedivim (« nobles », 146:3) — les puissants généreux… et "
  "mortels. Acrostiche (Ps 145) : l'alphabet comme structure — une lettre manque "
  "en hébreu massorétique (le noun, présent dans la grecque et à Qumrân — voir "
  "nwtsty 19/145, sans trancher ici). Médecine-mortalité (146:4 — P562) : « son "
  "souffle sort » — la biologie contre les régimes : tout pouvoir humain expire. "
  "Acoustique des foules (Mt 21:9 — P557) : Hosanna crié à gorge — le psaume "
  "devenu clameur."
 ),
 limites=(
  "Psaume 89:38-51 (plainte : « où sont tes bontés ? », 89:49 C8) : HORS P549/P576 — "
  "non développé ; le psaume de l'alliance ébranlée attend sa propre fiche. Psaume "
  "132:13-18 (Sion, lampe, couronne) : HORS P558/P577 — non développé. Psaume 118:22 "
  "(pierre rejetée) : rappels P556/P607 (voir d1 et r1) — seul 118:25-26 (P557) est "
  "versé. Le Hallel pascal : coutume (repère sans lien — règle : jw.org/wol "
  "uniquement), PAS preuve. Acrostiche de 145 (noun manquant) : signalé, non "
  "tranché (voir nwtsty 19/145). P549/P561 : Accomplie ET À venir ; P562 : En cours "
  "ET À venir — AUCUNE date pour l'avenir. C8 : Ps 89:49 (où sont tes bontés ?), "
  "Ps 8:2 (enfants), 2R 9:13 (Jéhu), 1R 4:31 (Éthan) — aucun P (vérifiés)."
 ),
 accomplissement=[("Alliance jurée", "Élu, descendance, soleil-lune (89 — P549, P576)"),
     ("Fruit promis", "Sur le trône (132:11-12 — P558, P577)"),
     ("Annoncé à Marie", "Trône de David (Lc 1:32-33 — P549, P576, P558)"),
     ("Prêché à la Pentecôte", "Serment au ressuscité (Ac 2:30 — P549, P558, P577)"),
     ("Acclamé aux Rameaux", "Hosanna, Béni (Mt 21:9 — P557)"),
     ("Royaume sans fin", "Toutes époques, larmes essuyées (P561, P562)")],
 tl=[("Nathan (repère)", "Oracle-source (2S 7 — rappel P073, j2)"),
     ("Éthan (repère)", "Serment chanté (Ps 89 — P549, P576)"),
     ("Montées (repère)", "Fruit promis (Ps 132 — P558, P577)"),
     ("Annonciation", "Gabriel récite l'alliance (Lc 1 — P549, P576, P558)"),
     ("Rameaux (33)", "Hosanna dans les rues (Mt 21:9 — P557)"),
     ("Pentecôte → Royaume", "Serment prêché, fin promise (P549-P562) — aucune date")],
 src=[("Les Psaumes — si n° 19 (Lc 24:44, les Psaumes prophétiques)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990080"),
      ("Psaume 89 — Bible d'étude, texte intégral", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/89"),
      ("Psaume 132 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/132"),
      ("Psaume 118 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/118"),
      ("Psaume 145 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/145"),
      ("Psaume 146 — Bible d'étude, notes", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/19/146")],
 img="images/prophe_S006_hosanna.jpg",
))
