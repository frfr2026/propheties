#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE 8 · vague P8-17 (mixte) · RO+CH — Rois (5) + Chroniques (1) : P097-P102."""
# pylint: disable=invalid-name,line-too-long

CAT = dict(
    code="RO+CH",
    nom="Rois (5) + Chroniques (1) — la chute annoncée, les batailles de Jéhovah",
    intro=("Ézéchias montre tout à Babylone, et tout partira ; Manassé mérite "
           "le cordeau de Samarie et le plat retourné ; Josias au cœur tendre "
           "sera recueilli en paix ; Shishaq pille mais Jérusalem survit ; la "
           "bataille de Josaphat n'est pas la sienne ; le sang de Zacharie "
           "crie contre Joas."),
    vague="P8-17",
)

FICHES = []

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="RO097", titre="« Tout sera emporté à Babylone » : les trésors montrés, les fils eunuques",
    ref="2 Rois 20:16-18",
    statut="Accomplie",
    cat="RO", syst="Oracle babylonien (ambassade → visite → questions → tout emporté → eunuques → paix)",
    reg="Registre : 2 Rois — P097 (20:16-18 : trésors et descendants emmenés à Babylone) ; accomplissement 2R 24:13 ; 25:13-17 ; Dn 1:1-7",
    texte=[
        "« MÉRODAK… LETTRES + PRÉSENT… MALADIE APPRISE. » (20:12 — apprise !)",
        "« ÉZÉCHIAS… MONTRA… TOUT… RIEN CACHÉ. » (20:13 — caché !)",
        "« D'OÙ VIENNENT-ILS ?… De LOIN… BABYLONE. » (20:14 — loin !)",
        "« QU'ONT-ILS VU ?… TOUT… RIEN CACHÉ. » (20:15 — vu !)",
        "« ÉCOUTE la PAROLE de JÉHOVAH. » (20:16 — écoute !)",
        "« TOUT… EMPORTÉ à BABYLONE… RIEN RESTERA. » (20:17 — restera !)",
        "« Tes FILS… EUNUQUES… PALAIS de BABYLONE. » (20:18 — Babylone !)",
        "« BONNE… la PAROLE… PAIX… en MES JOURS ? » (20:19 — jours !)",
        "« Il EMPORTA… TRÉSORS… COUPA… l'OR. » (24:13 — coupa !)",
        "« COLONNES… BRISÈRENT… BRONZE… BABYLONE. » (25:13-17 — bronze !)",
        "« USTENSILES… JEUNES… DANIEL… NOMS CHANGÉS. » (Dn 1:1-7 — changés !)",
    ],
    contexte=(
        "Jérusalem, ~703? — APRÈS la GUÉRISON (RO096 : 15 ANS (les SURSIS (les GRÂCES (les "
        "DANGERS (2Ch 32:25 : « son CŒUR S'ÉLEVA » (gavah — S'ÉLEVER (les CŒURS (les GONFLÉS "
        "(les GUÉRIS (les ORGUEILLEUX (les GRÂCES (les MAL-GÉRÉES ! : les ÉLÉVATIONS — les "
        "CARDIAQUES (les SPIRITUELLES (les MORTELLES !). MÉRODAK-BALADAN (20:12 : MARDUK-APLA-IDDINA "
        "(les NOMS (les AKKADIENS (les BABYLONES (les ANTI-ASSYRIE (les RÈGNES (721-710 + 703 (les "
        "DATES (les INSCRIPTIONS (les SARGON (les ANNALES (les REBELLES (les CHERCHENT (les ALLIÉS ! "
        ": les DIPLOMATES — les INTÉRESSÉS (les LETTRES (les PRÉSENTS (les PROTOCOLES (les COALITIONS "
        "(les BRIGUÉES !). La VISITE (20:13 : « ENCHANTÉ » (les BDS (les FLATTÉS (les MALADES (les "
        "GUÉRIS (les VISITÉS (les LOINTAINS (les HONORÉS (les TRÉSORS (les OUVERTS (les ARGENT (les OR "
        "(les AROMATES (les HUILES (les ARSENAUX (les TOUT (les MONTRÉS : les VISITES — les GUIDÉES (les "
        "INTRUS (les RENSEIGNÉS !) + « RIEN CACHÉ » (lo'-hayah davar (20:13 : les TOUT (les ABSOLUS (les "
        "PALAIS (les ROYAUMES (les SECRETS (les ZÉRO (les NAÏVETÉS — les ROYALES (les STRATÉGIQUES (les "
        "SUICIDAIRES !). ÉSAÏE VIENT (20:14 : les PROPHÈTES (les QUESTIONS (les ENQUÊTES (les « D'OÙ ? » "
        "(les « QUOI VU ? » (les INTERROGATOIRES (les DIVINS (les RÉPONSES (les NAÏVES (les AVEUX (les "
        "COMPLETS !)."
    ),
    explication=(
        "« Ils ONT VU (ra'u)… TOUT », 20:15 : ra'ah — VOIR (les YEUX (les ÉTRANGERS (les TRÉSORS (les "
        "VUS (les CONVOITÉS (les PRIS (les CHAÎNES — VOIR → CONVOITER → PRENDRE (ÈVE (Gn 3:6 ! AKAN (Jos 7:21 ! "
        ": les VERBES — les FUNESTES (les REGARDS (les FATALS !). « TOUT (kol)… sera EMPORTÉ (yinnase') », "
        "20:17 : nasa' — EMPORTER (les TOUT (les MONTRÉS (les TOUT (les PRIS (les MIROIRS — les EXACTS (les "
        "VISITES (les INVENTAIRES (les PILLAGES (les ANNONCÉS !) + « RIEN (lo'-yivvater davar) ne RESTERA », "
        "20:17 : yatar — RESTER (les RIEN (les CACHÉS (les RIEN (les RESTANTS (les PARALLÈLES — les TERRIFIANTS "
        "(« RIEN CACHÉ » (20:13 → « RIEN RESTERA » (20:17 : les ÉCHOS — les JUGEMENTS !). « De tes FILS (mibbanekha)… "
        "ils SERONT EUNUQUES (sarisim) », 20:18 : saris — EUNUQUE (les FONCTIONNAIRES (les COURS (les CASTRATS ? "
        "(les OFFICIERS ? (les SENS (les DÉBATTUS (les DANIEL (les ACCOMPLIS (Dn 1:3-7 : ASHPENAZ (les CHEFS (les "
        "EUNUQUES ! : les FILS — les DÉPORTÉS (les NOMS (les CHANGÉS (les IDENTITÉS (les VOLÉES !). « BONNE (tov)… "
        "la PAROLE… N'Y AURA-T-IL PAS PAIX (shalom) en MES JOURS ? », 20:19 : tov + shalom — BON + PAIX (les "
        "RÉACTIONS (les SURPRENANTES (les SOULAGEMENTS ? (les ÉGOÏSMES ? (les JUGEMENTS (les DIFFÉRÉS (les ACCEPTÉS "
        "(les DÉBATS — les SIÈCLES (les APOLOGISTES (les CRITIQUES (les TEXTES (les SOBRE (les VERDICTS (les "
        "SUSPENDUS !)."
    ),
    interpretation=(
        "L'ORGUEIL APRÈS la GRÂCE (RO096 (les GUÉRIS (les FLATTÉS (les TRÉSORS (les EXHIBÉS (les ALLIANCES (les "
        "BRIGUÉES (les DIEUX (les OUBLIÉS (les LEÇONS — les CLASSIQUES (les BÉNIS (les VIGILANTS (les GRÂCES (les "
        "HUMBLES !) + 2Ch 32:26 : « ÉZÉCHIAS S'HUMILIA… la COLÈRE ne VINT PAS de ses JOURS » (les REPENTIRS (les "
        "VRAIS (les JUGEMENTS (les DIFFÉRÉS (les PERSONNELS (les ÉPARGNÉS (les NATIONAUX (les MAINTENUS !). "
        "BABYLONE INSIGNIFIANTE (les VASSALES (les ASSYRIE (les REBELLES (les ÉCRASÉS (les PROPHÉTIES (les "
        "INCRÉDIBLES (les 100 ANS (les AVANT (les FOIS — les PROPHÉTIQUES (les VOIENT (les INVISIBLES (les "
        "ANNOUNCENT (les IMPENSABLES !). DANIEL NOMINAL (Dn 1:6-7 : DANIEL + HANANIA + MISHAËL + AZARIA (les NOMS "
        "(les HÉBREUX (les DIEUX (les VRAIS (les BELTSHATSAR + SHADRAK + MÉSHAK + ABED-NÉGO (les NOMS (les PAÏENS "
        "(les DIEUX (les FAUX (les IDENTITÉS — les ASSIÉGÉES (les FIDÉLITÉS (les GARDÉES (Dn 1:8 ! : les EUNUQUES "
        "— les PROPHÉTISÉS (les NOMMÉS (les FIDÈLES !). VOIR = PERDRE (les LEÇONS (les UNIVERSELLES (les TRÉSORS "
        "(les CACHÉS (les VANITÉS (les EXPOSÉES (les ENNEMIS (les RENSEIGNÉS (les SAGESSES — les STRATÉGIQUES (les "
        "SPIRITUELLES !)."
    ),
    hist=(
        "MÉRODAK-BALADAN (les INSCRIPTIONS (les SARGON II (les ANNALES (les DUR-SHARRUKIN (les REBELLES (les "
        "MATÉS (les 710 (les RETOURS (les 703 (les Sennachérib (les ÉCRASE (les DATES — les CROISÉES (les "
        "ASSYRIENNES (les BIBLIQUES (les CONCORDANTES !). BABYLONE 605 (les NABOPOLASSAR (les 626 (les "
        "INDÉPENDANCES (les NEBUCADNETSAR (les 605 (les KARKÉMISH (les EMPIRES (les NOUVEAUX (les PROPHÉTIES (les "
        "100 ANS (les VÉRIFIÉES (les HISTOIRES — les PATIENTES (les PAROLES (les PONCTUELLES !). 24:13 (les "
        "TRÉSORS (les COUPÉS (qatsats — COUPER (les OR (les SALOMON (les DÉTACHÉS (les FONDUS ? (les TRANSPORTÉS "
        "(les BUTINS (les INVENTORIÉS (les REGISTRES (les BABYLONIENS ? (les RATIONNEMENTS (les JOJAKIN (les "
        "TABLETTES !). DANIEL 1 (les 605 (les PREMIÈRES (les DÉPORTATIONS (les JEUNES (les NOBLES (les FORMÉS (les "
        "3 ANS (les COURS (les PAÏENNES (les SAGESSES — les INFILTRÉES (les FIDÈLES (les INFLUENTS !)."
    ),
    geo=(
        "BABYLONE (les EUPHRATES (les 900 KM (les LOINTAINES (20:14 : « de LOIN (merachoq) » (les DISTANCES (les "
        "SOULIGNÉES (les AMBASSADES (les EXPLOITS (les DIPLOMATIQUES (les VOYAGES — les SEMAINES (les CARAVANES "
        "(les DANGERS (les HONNEURS !). Le PALAIS (les TRÉSORS (les OTSAROT (les MAGASINS (les SALOMON (les AMASSÉS "
        "(les SIÈCLES (les RICHESSES (les CONCENTRÉES (les VISITES — les INVENTAIRES (les PILLAGES (les FUTURS !). "
        "L'ARSENAL (les beyt-kelav (les ARMES (les MONTRÉES (les ALLIÉS (les POTENTIELS (les DISSUASIONS (les "
        "RATÉES (les PROVOCATIONS (les RÉUSSIES (les STRATÉGIES — les INVERSÉES (les FORCES (les EXHIBÉES (les "
        "CONVOITÉES !). La ROUTE (les AMBASSADES (les MÉSOPOTAMIE → JUDA (les ASSYRIE (les TRAVERSÉES (les "
        "PÉRILLEUSES (les SECRÈTES ? (les DÉTECTÉES ? (les GÉOPOLITIQUES — les AUDACIEUSES (les ANTI-ASSYRIENNES !)."
    ),
    sci=(
        "La DIPLOMATIE ANTIQUE (les LETTRES (les sepharim (les PRÉSENTS (les minchah (les PROTOCOLES (les "
        "MALADIES (les PRÉTEXTES (les COALITIONS (les BUTS (les AMARNA (les PRÉCÉDENTS (les TABLETTES (les "
        "FORMULES (les CHANCELLERIES — les CODIFIÉES (les ESPIONNAGES (les DÉGUISÉS !). La MÉTALLURGIE (les OR "
        "(les COUPÉS (24:13 (les FONDUS (les TRANSPORTÉS (les BRONZE (les COLONNES (25:13 (les BRISÉES (les "
        "LIVRES (les TALENTS (les QUANTITÉS (les ÉNORMES (les LOGISTIQUES — les BUTINS (les ORGANISÉS (les "
        "CONVOIS (les PROTÉGÉS !). L'EUNUCHISME de COUR (les sarisim (les FONCTIONS (les HAREMS (les "
        "ADMINISTRATIONS (les CASTRATIONS (les RÉELLES ? (les TITRES ? (les ASSYRIOLOGUES (les DÉBATTENT (les "
        "DANIEL (les MARIÉS ? (les TEXTES (les TAIRENT (les STATUTS — les FLOUS (les RÉELS (les HUMILIATIONS !). "
        "L'ARCHIVISTIQUE (les LETTRES (les CONSERVÉES (les TRÉSORS (les INVENTORIÉS (les MÉMOIRES (les ROYALES "
        "(les SCRIBES (les TÉMOINS (les RÉCITS — les DOCUMENTÉS (les PRÉCIS (les VÉRIFIABLES !)."
    ),
    schema=(
        "BABYLONE EN 10 TEMPS : MALADIE (les GUÉRISONS (RO096 !) → LETTRES (« MÉRODAK… PRÉSENT » : les FLATTERIES !) "
        "→ ENCHANTÉ (les CŒURS (les ÉLEVÉS !) → VISITE (« MONTRA… TOUT… RIEN CACHÉ » : les NAÏVETÉS !) → ÉSAÏE "
        "(« D'OÙ ?… QUOI VU ? » : les INTERROGATOIRES !) → AVEUX (« TOUT… RIEN CACHÉ » : les CANDIDES !) → « ÉCOUTE » "
        "(les VERDICTS !) → « TOUT… EMPORTÉ… RIEN RESTERA » (les MIROIRS !) → « FILS… EUNUQUES… PALAIS » (les "
        "DESCENDANCES !) → « BONNE… PAIX en MES JOURS ? » (les SOULAGEMENTS !) → 605 (« DANIEL… NOMS CHANGÉS » : "
        "les NOMINAUX !). Tout montré — tout emporté ; les fils vus deviendront eunuques."
    ),
    limites=(
        "20:19 (les ÉGOÏSMES ? (les SOULAGEMENTS (les LÉGITIMES (les JUGEMENTS (les DIFFÉRÉS (les GRÂCES (les "
        "RECONNUES (les POSTÉRITÉS (les SACRIFIÉES ? (les COMMENTAIRES (les DIVISÉS (les TEXTES (les SOBRE (les "
        "JUGEMENTS (les SUSPENDUS (les PROPOSÉS (pas les IMPOSÉS !). La DATE (les 713 ? (les 703 ? (les MÉRODAK (les "
        "RÈGNES (les DEUX (les MALADIES (les QUAND (les SIÈGES (les AVANT (les PENDANT (RO096 ! (les CHRONOLOGUES "
        "(les DÉBATTENT (les FOURCHETTES (les PRUDENTES !). « Tes FILS » (lesQUELS (les MANASSÉ ? (les NÉ (les "
        "PETITS-FILS (les DANIEL (les NOBLES (les FAMILLES (les ROYALES (Dn 1:3 (les IDENTIFICATIONS (les PROBABLES "
        "(pas les CERTAINES !). ÉSAÏE 39 (les PARALLÈLES (les QUASI-IDENTIQUES (les DIFFÉRENCES (les MINEURES (les "
        "RÉDACTIONS (les INDÉPENDANTES ? (les SOURCES (les COMMUNES ? (les SYNOPSES (les ÉCLAIRANTES !). Les "
        "EUNUQUES (les CASTRATS (les FONCTIONNAIRES (les LEXIQUES (les DÉBATTENT (les DANIEL (les PREUVES (les "
        "ABSENTES (les STATUTS (les FLOUS (les HUMILIATIONS (les CERTAINES !)."
    ),
    accomplissement=[(("20:12-13", "MÉRODAK (LETTRES) + « TOUT… RIEN CACHÉ »")),
        ((("20:14-16"), "« D'OÙ ?… VU ? » + « ÉCOUTE »")),
        ((("20:17-18"), "« TOUT… RIEN » + « EUNUQUES »")),
        ((("20:19"), "« BONNE… PAIX… JOURS ? »")),
        ((("24:13"), "TRÉSORS (COUPÉS !)")),
        ((("25:13-17"), "BRONZE (BRISÉ !)")),
        ((("Dn 1:1-7"), "DANIEL (NOMS !)"))],
    tl=[((("20:13"), "« RIEN CACHÉ » (TOUT)")),
        ((("20:17"), "« RIEN RESTERA » (BABYLONE)")),
        ((("20:18"), "« EUNUQUES » (FILS)")),
        ((("24:13"), "TRÉSORS (COUPÉS)")),
        ((("Dn 1:7"), "NOMS (CHANGÉS)"))],
    src=[("2 Rois 20 — Bible d'étude (ambassade, oracle babylonien, 20:12-19)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/20"),
        ("2 Rois 20 — Traduction du monde nouveau (Ézéchias, Ésaïe, Babylone)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/12/20"),
        ("Livre de la Bible n° 12 — 2 Rois (aperçu officiel, Ézéchias, Juda)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990073")],
    img="images/prophe_RO097_babylone.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="RO098", titre="« Le cordeau de Samarie » : Jérusalem nettoyée comme un plat retourné",
    ref="2 Rois 21:10-15",
    statut="Accomplie",
    cat="RO", syst="Oracle contre Manassé (pire qu'Amoréens → oreilles → cordeau → plat → rejet → sang)",
    reg="Registre : 2 Rois — P098 (21:10-15 : Jérusalem livrée, reste de l'héritage rejeté) ; accomplissement 2R 24 ; 25",
    texte=[
        "« MANASSÉ… 12 ANS… 55 ANS… JÉRUSALEM. » (21:1 — ans !)",
        "« REBÂTIT les HAUTS LIEUX… BAAL… POTEAU… ARMÉE. » (21:3 — armée !)",
        "« FIT PASSER son FILS par le FEU… ENCHANTEURS. » (21:6 — feu !)",
        "« IDOLE… dans la MAISON… J'AI DIT… MON NOM. » (21:7 — nom !)",
        "« Par ses SERVITEURS les PROPHÈTES… DIT. » (21:10 — dit !)",
        "« PIS que les AMORÉENS… FIT PÉCHER JUDA. » (21:11 — pécher !)",
        "« Je FAIS VENIR un MAL… OREILLES TINTERONT. » (21:12 — tinteront !)",
        "« CORDEAU de SAMARIE… NIVEAU maison d'ACHAB. » (21:13 — Achab !)",
        "« NETTOIERAI… comme un PLAT… RETOURNÉ. » (21:13 — retourné !)",
        "« REJETTERAI le RESTE… LIVRERAI… PILLAGE. » (21:14 — pillage !)",
        "« SANG INNOCENT… REMPLIT… d'un BOUT à l'AUTRE. » (21:16 — autre !)",
        "« À CAUSE de MANASSÉ… PAS PARDONNER. » (24:4 — pardonner !)",
    ],
    contexte=(
        "Jérusalem, ~716-662 — le FILS du SURSIS (RO096 : les 15 ANS (les AJOUTÉS (les MANASSÉ (les NÉS (les "
        "PENDANT (les PARADOXES (les PROVIDENCES (les PIRES (les ROIS (les ENGENDRÉS (les GRÂCES (les DEMANDÉES "
        "(les CONSÉQUENCES (les LOURDES : les SURSIS — les EMBARRASSANTS (les PRIÈRES (les EXAUCÉES (les HISTOIRES "
        "(les TRAGIQUES !). 12 ANS (21:1 : les ENFANTS-ROIS (les RÉGENTS (les HEPHTSIBA (les MÈRES (les COURTS (les "
        "INFLUENTS (les JOAS (les PRÉCÉDENTS (CH102 ! : les MINORITÉS — les MANIPULÉES (les TUTEURS (les IDOLÂTRES "
        "!). 55 ANS (21:1 : les RECORDS (les LONGS (les JUDA (les PIRES (les DURÉES (les DÉSASTRES (les 1200002882 : "
        "« 716-662 » (OFFICIEL ! (les DATES — les ANCRÉES (les RÈGNES (les MESURÉS (les MALHEURS (les PROLONGÉS !). "
        "Le CONTRE-ÉZÉCHIAS (21:3 : « REBÂTIT (vayyiven) les HAUTS LIEUX… qu'ÉZÉCHIAS AVAIT DÉTRUITS » (les "
        "DÉMOLITIONS (les RECONSTRUITES (les RÉFORMES (les ANNULÉES (les PÈRES (les DÉFAITS (les FILS (les "
        "VANDALES (les HÉRITAGES — les SABOTÉS (les PIÉTÉS (les EFFACÉES !). PIRE qu'AMORÉENS (21:11 : les "
        "AUTOCHTONES (les JUGÉS (les DÉPOSSÉDÉS (les ÉTALONS (les DÉPASSÉS (les JUDA (les PIRE (les PAÏENS (les "
        "COMBLES — les DÉPASSÉS (les MESURES (les DÉBORDÉES !)."
    ),
    explication=(
        "« Les 2 OREILLES (oznav) de QUICONQUE… TINTERONT (tetsilenah) », 21:12 : tsalal — TINTER (les "
        "FORMULES (les RARES (1S 3:11 : ÉLI ! (les 2 EMPLOIS (les JUGEMENTS (les INOUÏS (les AUDITIONS — les "
        "TRAUMATIQUES (les NOUVELLES (les ASSOURDISSANTES !). « J'ÉTENDRAI (venatiti)… le CORDEAU (qav) de "
        "SAMARIE », 21:13 : qav — CORDEAU (les MAÇONS (les MESURENT (les CONSTRUISENT (les DÉMOLISSENT (les "
        "INSTRUMENTS (les MÊMES (les USAGES (les INVERSÉS (les SAMARIE (les PRÉCÉDENTS (les 740 ! : les CORDEAUX "
        "— les CONSTRUCTEURS (les DESTRUCTEURS (les MESURES (les FATALES !). « Le NIVEAU (mishqolet) de la "
        "MAISON d'ACHAB », 21:13 : mishqolet — FIL À PLOMB (les VERTICALITÉS (les VÉRIFIÉES (les MURS (les "
        "PENCHÉS (les ACHAB (les DÉMOLIS (RO091 ! (les PRÉCÉDENTS — les CITÉS (les JUGEMENTS (les RÉPÉTÉS !). "
        "« Je NETTOIERAI (umachiti)… comme on NETTOIE un PLAT (tsallachath) », 21:13 : machah — ESSUYER (les "
        "VAISSELLES (les LAVÉES (les VILLES (les RÉCURÉES (les POPULATIONS (les ESSUYÉES (les IMAGES — les "
        "DOMESTIQUES (les JUGEMENTS (les MÉNAGERS !) + « et on le RETOURNE (vehaphakh) SENS DESSUS DESSOUS », "
        "21:13 : haphakh — RETOURNER (les SODOME (Gn 19:25 ! (les PLATS (les VIDES (les VILLES (les VIDÉES (les "
        "RETOURNEMENTS — les TOTAUX (les RIEN (les RESTE (cf. 20:17 : « RIEN RESTERA » (RO097 ! : les ÉCHOS — les "
        "VAISSELLES (les VIDES !). « Je REJETTERAI (venatashti) le RESTE (she'erit) de mon HÉRITAGE », 21:14 : "
        "natash — REJETER (les RESTES (les ABANDONNÉS (les HÉRITAGES (les RÉPUDIÉS (les PROTECTIONS (les RETIRÉES "
        "(les PROIES — les LIVRÉES (les PILLAGES (les BUTINS (baz + mesissah : les DOUBLES (les DÉPOUILLES !)."
    ),
    interpretation=(
        "Les OUTILS INVERSÉS (les CORDEAUX (les NIVEAUX (les CONSTRUISENT (les DÉTRUISENT (les GRÂCES (les MESURES "
        "(les JUGEMENTS (les MESURÉS (les THÉOLOGIES — les INSTRUMENTALES (les MÊMES (les MAINS (les ŒUVRES (les "
        "CONTRAIRES !). Les PRÉCÉDENTS CITÉS (les SAMARIE (les ACHAB (les JUGÉS (les RAPPELÉS (les JUDA (les "
        "AVERTIS (les MÉTHODES — les PÉDAGOGIQUES (les HISTOIRES (les LEÇONS (les IGNORÉES (les RÉPÉTÉES !) + "
        "1101990073 : « il fera venir le MALHEUR sur JÉRUSALEM comme il l'a fait sur SAMARIE, la NETTOYANT et la "
        "RETOURNANT » (OFFICIEL ! (les CONFIRMATIONS — les OFFICIELLES (les PLATS (les RETOURNÉS !). Le REPENTIR "
        "TARDIF (2Ch 33:10-13 : les CAPTIVITÉS (les CROCHETS ? (les HUMILIATIONS (les PRIÈRES (les EXAUCÉES (les "
        "RETOURS (les RÉFORMES (les PARTIELLES (les PERSONNELS (les PARDONNÉS (les NATIONAUX (les JUGÉS (les "
        "DISTINCTIONS — les CRUCIALES (les ÂMES (les SAUVÉES (les VILLES (les BRÛLÉES !). Le SANG IMPARDONNABLE "
        "(21:16 + 24:4 : « REMPLIT… d'un BOUT à l'AUTRE » (les QUANTITÉS (les GÉOGRAPHIQUES (les VILLES (les "
        "PLEINES (les « JÉHOVAH ne CONSENTIT PAS à PARDONNER » (les REFUS (les DIVINS (les COLLECTIFS (les "
        "GRAVITÉS — les ULTIMES (les SANGS (les VERSÉS (les JUGEMENTS (les IRRÉVERSIBLES !)."
    ),
    hist=(
        "La LISTE d'ÉSAR-HADDON (les 22 ROIS (les HATTI (les TRIBUTS (les « MANASSÉ de JUDA » (les NOMMÉS (les "
        "INSCRIPTIONS (les PRISMES (les VASSAUX (les RECENSÉS (les PREUVES — les NOMINALES (les PAÏENNES (les "
        "CONFIRMANTES !) + 1200002882 : « MANASSÉ de JUDA est MENTIONNÉ sur une LISTE… 22 ROIS… qui PAYAIENT "
        "TRIBUT » (OFFICIEL ! (les TRIBUTS — les DOCUMENTÉS (les DEUX (les CÔTÉS !). La CAPTIVITÉ (2Ch 33:11 : "
        "les ASSYRIENS (les CROCHETS (les chôchim ? (les NEZ ? (les TRAITEMENTS (les HUMILIANTS (les BABYLONE (les "
        "VILLES (les ROYALES (les ASSYRIENNES (les DÉTENTIONS (les EXILS (les TEMPORAIRES (les RETOURS (les "
        "GRACIÉS !). ÉSAÏE SCIÉ ? (les TRADITIONS (les RABBINIQUES (les MARTYRES (les LÉGENDES (les Hé 11:37 : « "
        "SCIÉS » (les GÉNÉRIQUES (les IDENTIFICATIONS (les PROPOSÉES : 1200002882 : « D'APRÈS la LITTÉRATURE "
        "RABBINIQUE » (OFFICIEL ! (les PRUDENCES — les OFFICIELLES (les TRADITIONS (les RAPPORTÉES (pas les "
        "GARANTIES !). 607/587 (les 24-25 (les SIÈGES (les DEUX (les DÉPORTATIONS (les TROIS (les TEMPLES (les "
        "BRÛLÉS (les PLATS (les RETOURNÉS (les ORACLES (les SOLDÉS !)."
    ),
    geo=(
        "JÉRUSALEM REMPLIE (21:16 : « d'un BOUT (qatseh) à l'AUTRE » (les EXTRÉMITÉS (les VILLES (les PLEINES (les "
        "SANGS (les GÉOGRAPHIES (les HORREURS (les MESURÉES (les DISTANCES — les SANGLANTES (les CAPITALES (les "
        "SOUILLÉES !). TOPHETH-HINNOM (21:6 : « FIT PASSER… par le FEU » (les VALLÉES (les SACRIFICES (les ENFANTS "
        "(les MOLOK (les ABOMINATIONS (les LIEUX (les MAUDITS (Jr 7:31 ! : les VALLÉES — les HANTÉES (les FEUX (les "
        "INFANTICIDES !). Le TEMPLE PROFANÉ (21:7 : « l'IDOLÂTRE… dans la MAISON » (les SAINTS (les SOUILLÉS (les "
        "NOMS (les INSULTÉS (les DEMEURES (les DIVINES (les OCCUPÉES (les SCANDALES — les SUPRÊMES (les MAISONS (les "
        "VIOLÉES !). SAMARIE (21:13 : les CORDEAUX (les NORD (les TOMBÉS (les 740 (les PRÉCÉDENTS (les GÉOGRAPHIQUES "
        "(les RUINES (les VISIBLES (les LEÇONS (les PAYSAGÈRES (les JUDA (les AVEUGLES !)."
    ),
    sci=(
        "L'ACOUSTIQUE du TINTEMENT (21:12 : les OREILLES (les TINNITUS (les STRESS (les NOUVELLES (les CHOCS (les "
        "PHYSIOLOGIES (les PEURS (les AUDITIONS (les TRAUMAS (les EXPRESSIONS — les UNIVERSELLES (les CORPS (les "
        "RÉVÈLENT (les TERREURS !). La MAÇONNERIE (les CORDEAUX (les qav (les CRAIE (les LIGNES (les NIVEAUX (les "
        "PLOMBS (les VERTICALES (les TECHNIQUES (les ANTIQUES (les ÉGYPTES (les MÉSOPOTAMIES (les OUTILS (les "
        "RETROUVÉS (les TOMBEAUX (les MAQUETTES ! : les ARTS — les BÂTISSEURS (les DÉMOLISSEURS (les MÊMES !). La "
        "CÉRAMIQUE (les PLATS (les tsallachath (les VAISSELLES (les LAVÉES (les ESSUYÉES (les RETOURNÉES (les "
        "ÉGOUTTÉES (les GESTES (les DOMESTIQUES (les QUOTIDIENS (les IMAGES — les PARLANTES (les MÉNAGÈRES (les "
        "PROPHÉTIQUES !). La DÉMOGRAPHIE (les 55 ANS (les RÈGNES (les LONGS (les GÉNÉRATIONS (les DEUX (les "
        "ENDOCTRINÉES (les IDOLÂTRIES (les ENRACINÉES (les RÉFORMES (les JOSIAS (les SUPERFICIELLES (les RACINES "
        "(les PROFONDES !)."
    ),
    schema=(
        "MANASSÉ EN 11 TEMPS : 12 ANS (les ENFANTS-ROIS !) → REBÂTIT (« HAUTS LIEUX… qu'ÉZÉCHIAS AVAIT DÉTRUITS » : "
        "les VANDALISMES !) → BAAL + POTEAU + ARMÉE (les PANTHÉONS !) → FEU (« FIT PASSER son FILS » : les HORREURS !) "
        "→ IDOLE (« dans la MAISON » : les SCANDALES !) → PROPHÈTES (« par ses SERVITEURS » : les AVERTIS !) → « PIS "
        "qu'AMORÉENS » (les DÉPASSÉS !) → « OREILLES TINTERONT » (les TRAUMAS !) → « CORDEAU… NIVEAU » (les OUTILS (les "
        "INVERSÉS !) → « PLAT… RETOURNÉ » (les VAISSELLES (les VIDES !) → « REJETTERAI… PILLAGE » (les ABANDONS !) → "
        "SANG (« d'un BOUT à l'AUTRE » : les GÉOGRAPHIES !) → « PAS PARDONNER » (24:4 : les IRRÉVERSIBLES !). Le fils "
        "du sursis démolit tout — le plat sera récuré et retourné."
    ),
    limites=(
        "Le REPENTIR (2Ch 33 : les 2R (les SILENCES (les CHRONIQUES (les RACONTENT (les CONTRADICTIONS (les "
        "APPARENTES (les COMPLÉMENTS (les HARMONIES (les SOURCES (les DIVERSES (les THÉOLOGIES (les COMPLÉMENTAIRES "
        "(les PROPOSÉES (les HARMONISÉES !). La CAPTIVITÉ (2Ch 33:11 : les OÙ (les BABYLONE (les ASSYRIENNE (les "
        "QUAND (les DURÉES (les TEXTES (les SOBRE (les CROCHETS (les SENS (les DÉBATTUS (les DÉTAILS (les RARES (les "
        "FAITS (les AFFIRMÉS !). ÉSAÏE SCIÉ (les TRADITIONS (les RABBINIQUES (les Hé 11:37 (les GÉNÉRIQUES (les "
        "PREUVES (les ABSENTES (les LÉGENDES (les POSSIBLES (les 1200002882 (les PRUDENTS : les MARTYRES — les "
        "PROPOSÉS (pas les PROUVÉS !). Les DATES (716-662 (les 1200002882 (les OFFICIELLES (les CO-RÉGENCES (les "
        "DÉBATTUES (les ÉZÉCHIAS (les 15 ANS (les CHEVAUCHEMENTS (les CHRONOLOGUES (les AJUSTENT (les RELATIVES (les "
        "SÛRES !). Les PROPHÈTES (21:10 : lesQUELS (les ANONYMES (les PLURIELS (les ENVOYÉS (les IGNORÉS (les NOMS "
        "(les TUS (les MESSAGES (les GARDÉS (les MESSAGERS — les EFFACÉS (les PAROLES (les GRAVÉES !)."
    ),
    accomplissement=[(("21:1-9", "12 ANS + 55 ANS + REBÂTIT + FEU + IDOLE")),
        ((("21:10-12"), "PROPHÈTES + « PIS » + « TINTERONT »")),
        ((("21:13"), "CORDEAU + NIVEAU + PLAT (RETOURNÉ !)")),
        ((("21:14-16"), "REJET + PILLAGE + SANG (BOUT !)")),
        ((("24:4"), "« PAS PARDONNER » (MANASSÉ !)")),
        ((("24-25"), "SIÈGES + TEMPLE (BRÛLÉ !)"))],
    tl=[((("21:1"), "12 ANS (55 ANS !)")),
        ((("21:11"), "« PIS » (AMORÉENS)")),
        ((("21:13"), "PLAT (RETOURNÉ)")),
        ((("21:16"), "SANG (BOUT !)")),
        ((("24:4"), "« PAS PARDONNER »"))],
    src=[("Manassé — Étude (55 ans, sang, tribut, Ésar-Haddon)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200002882"),
        ("Livre de la Bible n° 12 — 2 Rois (aperçu, plat nettoyé et retourné)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1101990073"),
        ("2 Rois 21 — Bible d'étude (Manassé, cordeau, 21:10-16)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/21")],
    img="images/prophe_RO098_cordeau.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="RO099", titre="« Recueilli en paix » : Hulda, Josias au cœur tendre et le malheur maintenu",
    ref="2 Rois 22:15-20",
    statut="Accomplie",
    cat="RO", syst="Oracle de Hulda (livre → déchiré → consultée → malheur certain → cœur tendre → paix)",
    reg="Registre : 2 Rois — P099 (22:15-20 : Josias recueilli en paix, ne verra pas le malheur) ; accomplissement 2R 23:29, 30 ; 2Ch 35:23, 24",
    texte=[
        "« JOSIAS… 8 ANS… 31 ANS… DROIT… DAVID. » (22:1-2 — David !)",
        "« HILKIJA… LIVRE de la LOI… TROUVÉ… MAISON. » (22:8 — trouvé !)",
        "« Le ROI… ENTENDIT… DÉCHIRA ses VÊTEMENTS. » (22:11 — déchira !)",
        "« GRANDE… COLÈRE… PÈRES N'ONT PAS ÉCOUTÉ. » (22:13 — écouté !)",
        "« HULDA… PROPHÉTESSE… SECOND QUARTIER… ALLÈRENT. » (22:14 — allèrent !)",
        "« DITES à l'HOMME qui vous a ENVOYÉS. » (22:15 — homme !)",
        "« Je FAIS VENIR le MALHEUR… PAROLES du LIVRE. » (22:16 — livre !)",
        "« M'ONT ABANDONNÉ… COLÈRE NE S'ÉTEINDRA PAS. » (22:17 — éteindra !)",
        "« CŒUR TENDRE… HUMILIÉ… PLEURÉ… ENTENDU. » (22:18-19 — entendu !)",
        "« RECUEILLI vers tes PÈRES… PAIX… YEUX NE VERRONT PAS. » (22:20 — verront !)",
        "« NÉKO… MEGUIDDO… MORT… JÉRUSALEM… PLEURÈRENT. » (23:29-30 — pleurèrent !)",
        "« ARCHERS… BLESSÉ… SECOND CHAR… SÉPULCRE PÈRES. » (2Ch 35:23-24 — pères !)",
    ],
    contexte=(
        "Jérusalem, 622 — JOSIAS 8 ANS (22:1 : les ENFANTS-ROIS (les AMON (les ASSASSINÉ (les PEUPLES (les "
        "COURONNENT (les ENFANTS (les PRÉSERVÉS (les INFLUENCES (les PATERNELLES (les ÉVITÉES (les JÉDIDA (les "
        "MÈRES (les BOTSQATH ! : les ENFANCES — les PROTÉGÉES (les DESTINS (les PRÉPARÉS !). NOMMÉ 300 ANS AVANT "
        "(RO077 : 1R 13:2 : « JOSHIYYAHOU ! » (les NOMS (les CITÉS (les SIÈCLES (les AVANT (les NAISSANCES (les "
        "PROPHÉTIES — les NOMINALES (les VÉRIFIÉES (les JOSIAS (les MARCHE (les DEDANS !). Le LIVRE TROUVÉ (22:8 : "
        "les TRAVAUX (les TEMPLES (les RÉPARATIONS (les HILKIJA (les DÉCOUVRENT (les ROULEAUX (les POUSSIÉREUX "
        "(les DEUTÉRONOMES ? (les LOIS (les OUBLIÉES (les LECTURES (les PUBLIQUES (les DÉCHIRURES (les ROYALES ! "
        ": les TROUVAILLES — les EXPLOSIVES (les PAPIERS (les JUGES (les ROIS !). HULDA (22:14 : les PROPHÉTESSES "
        "(les FEMMES (les PAROLES (les DIVINES (les SHALLUM (les MARIS (les GARDE-ROBES (les MISHNEH (les SECONDS "
        "(les QUARTIERS (les DÉLÉGATIONS (les ROYALES (les CONSULTENT (les FEMMES (les DIEUX (les PARLENT (les "
        "QUI-ILS-VEULENT !)."
    ),
    explication=(
        "« DITES à l'HOMME (la'ish) qui vous a ENVOYÉS », 22:15 : ish — HOMME (les ROI (les NON-NOMMÉS (les "
        "TITRES (les OMIS (les DISTANCES (les PROPHÉTIQUES (les AUTORITÉS — les SUPÉRIEURES (les PAROLES (les "
        "JUGER (les ENVOYEURS !). « Je FAIS VENIR (mevi') le MALHEUR (ra'ah) », 22:16 : bo' — VENIR (les CERTITUDES "
        "(les RÉFORMES (les INUTILITÉS (les COLLECTIVES (les MANASSÉ (les IRRÉVERSIBLES (24:4 ! (les VERDICTS — les "
        "SANS-APPEL (les NATIONAUX (les MAINTENUS !). « Ils M'ONT ABANDONNÉ ('azavuni)… ma COLÈRE (chamati) NE "
        "S'ÉTEINDRA PAS (lo' tikhbeh) », 22:17 : 'azav + kavah — ABANDONNER + ÉTEINDRE (les FEUX (les INEXTINGUIBLES "
        "(les COLÈRES (les ENTRETENUES (les ABANDONS (les PAYÉS (les MIROIRS — les TERRIBLES (cf. CH100 : « "
        "ABANDONNÉ → ABANDONNE » ! : les VERBES — les FATALS !). « Parce que ton CŒUR (levavkha) a été TENDRE (rakh) », "
        "22:19 : rakh — TENDRE (les CŒURS (les MOUS (les DURS (les ENDURCIS (les PHARAONS (les CONTRASTES (les "
        "ÉMPS (les ÉMUS (les LARMES — les SAUVEUSES (les TENDRESSES (les RÉCOMPENSÉES !) + « tu T'ES HUMILIÉ "
        "(tikkana')… tu as PLEURÉ (vattivekh)… J'AI ENTENDU (shama'ti) », 22:19 : kana' + bakhah + shama' — HUMILIER "
        "+ PLEURER + ENTENDRE (les TRIPLES (les RÉPONSES (les DÉCHIRER (les PLEURER (les HUMILIER (les DIEUX (les "
        "ENTENDENT (cf. RO096 : « ENTENDU… VU LARMES » ! : les LARMES — les ENTENDUES (les TOUJOURS !). « Je te "
        "RECUEILLERAI (osiphkha) vers tes PÈRES… en PAIX (beshalom) », 22:20 : asaph — RECUEILLIR (les RASSEMBLER "
        "(les SÉPULCRES (les PÈRES (les PAIX (les PARADOXALES (les MEGUIDDO (les VIOLENTES (les PAIX (les "
        "ESCHATOLOGIQUES (les AVANT-DÉSASTRES (les GRÂCES — les PERSONNELLES (les JUGEMENTS (les COLLECTIFS !) + "
        "1965082 : « je te RECUEILLERAI AUPRÈS de tes PÈRES… RECUEILLI en PAIX dans ton SÉPULCRE » (OFFICIEL ! (les "
        "SÉPULCRES — les PROMIS (les TENUS (2Ch 35:24 !). « Tes YEUX ('enekha) NE VERRONT PAS (lo' tir'enah) », "
        "22:20 : ra'ah — VOIR (les GRÂCES (les NÉGATIVES (les NE-PAS-VOIR (les ÉPARGNÉS (les HORREURS (les FUTURES "
        "(les MORTS (les PRÉMATURÉES (les MISÉRICORDES — les PARADOXALES (les MOURIR (les JEUNES (les VOIR (les "
        "RIEN !)."
    ),
    interpretation=(
        "RÉFORME VRAIE, JUGEMENT MAINTENU (les 622 (les PÂQUES (les INÉGALÉES (23:22 ! (les IDOLÂTRIES (les "
        "EXTERMINÉES (les MANASSÉ (les SANGS (les INEFFAÇABLES (les LEÇONS — les SOBRES (les RÉVEILS (les VRAIS "
        "(les CONSÉQUENCES (les DEMEURENT !). GRÂCE PERSONNELLE, JUGEMENT COLLECTIF (les JOSIAS (les ÉPARGNÉS (les "
        "JUDA (les JUGÉS (les DISTINCTIONS — les DIVINES (les INDIVIDUS (les SAUVÉS (les NATIONS (les FRAPPÉES !). "
        "PAIX PARADOXALE (les MEGUIDDO (les ARCHERS (les BLESSURES (les MORTS (les VIOLENTES (les PAIX (les PROMISES "
        "(les PAIX (les VRAIES (les AVANT (les 607 (les NE-PAS-VOIR (les HORREURS (les MISÉRICORDES — les MYSTÉRIEUSES "
        "(les MOURIR (les BATAILLES (les REPOSER (les PAIX !) + 1965082 : « il ne VIT PAS le TERRIBLE DÉSASTRE » "
        "(OFFICIEL ! (les VÉRIFICATIONS — les OFFICIELLES (les YEUX (les FERMÉS (les AVANT !). HULDA FEMME (les "
        "MYRIAM (les DÉBORA (les HULDA (les ANNE (les PHILIPPE (les FILLES (les PROPHÉTESSES (les BIBLIQUES (les "
        "DIEUX (les PARLENT (les FEMMES (les ROIS (les ÉCOUTENT (les CONSULTATIONS — les OFFICIELLES (les DÉLÉGATIONS "
        "(les ROYALES (les VALIDÉES !)."
    ),
    hist=(
        "NÉKO II 609 (les PHARAONS (les XXVIe (les EUPHRATES (les SECOURS (les ASSYRIENS (les CARQUÉMISH (les "
        "JOSIAS (les INTERCEPTENT (les MEGUIDDO (les BARRAGES (les MOTIFS (les DÉBATTUS (les VASSAUX (les ASSYRIENS ? "
        "(les OPPORTUNISTES ? (les TEXTES (les SOBRE (les MORTS (les CERTAINES !). MEGUIDDO (les TELLS (les "
        "CARREFOURS (les VIA MARIS (les STRATÉGIQUES (les BATAILLES (les MILLÉNAIRES (les ARMAGEDDON (les "
        "APOCALYPTIQUES (Ap 16:16 ! (les PLAINES — les SANGLANTES (les HISTOIRES (les JUGEMENTS !). La PÂQUE 622 "
        "(23:21-23 : « AUCUNE PÂQUE… DEPUIS les JUGES » (les INÉGALÉES (les RÉFORMES (les SOMMETS (les NATIONALES "
        "(les FERVENTES (les DERNIÈRES (les SPLENDEURS (les AVANT-NUIT !). 640-609 (les 31 ANS (les 8 → 39 (les MORTS "
        "(les JEUNES (les PROMESSES (les TENUES (les SÉPULCRES (les PÈRES (les DEUILS (les NATIONAUX (les "
        "LAMENTATIONS (les JÉRÉMIE (2Ch 35:25 ! : les LARMES — les PROPHÉTIQUES (les ROIS (les PLEURÉS !)."
    ),
    geo=(
        "Le TEMPLE (les TRAVAUX (les 18e ANNÉE (les RÉPARATIONS (les CAISSES (les COLLECTES (les LIVRES (les "
        "TROUVÉS (les LIEUX (les SAINTS (les ARCHIVES (les OUBLIÉES (les RESTAURATIONS — les MATÉRIELLES (les "
        "SPIRITUELLES !). Le SECOND QUARTIER (22:14 : mishneh — SECOND (les EXTENSIONS (les OUEST ? (les COLLINES "
        "(les NOUVELLES (les HULDA (les RÉSIDENCES (les DÉLÉGATIONS (les MARCHENT (les PROPHÉTESSES (les URBAINES "
        "(les ACCESSIBLES !). MEGUIDDO (23:29 : les VALLÉES (les JIZREEL (RO091 ! (les MÊMES (les PLAINES (les JÉHU "
        "(les JOSIAS (les SANGS (les ROYAUX (les VERSÉS (les GÉOGRAPHIES — les TRAGIQUES (les CHAMPS (les BATAILLES "
        "(les TOMBES !). Le SÉPULCRE des PÈRES (les CITÉS (les DAVID (les TOMBEAUX (les ROIS (les FOUILLES (les "
        "DÉBATS (les PROMESSES (les TENUES (les OS (les REPOSÉS (les PAIX (les GÉOGRAPHIQUES !)."
    ),
    sci=(
        "La CODICOLOGIE (les LIVRES (les sepher (les ROULEAUX (les CUIRS (les PAPYRUS (les CONSERVATIONS (les "
        "SIÈCLES (les DÉCOUVERTES (les HASARDS (les PROVIDENCES (les TEXTES — les SURVIVANTS (les POUSSIÈRES (les "
        "JUGES !). Le TEXTILE (les SHALLUM (les shomer-begadim (les GARDE-ROBES (les VÊTEMENTS (les ROYAUX (les "
        "FONCTIONS (les COURTS (les HULDA (les ÉPOUSES (les DIGNITAIRES (les SOCIOLOGIES — les ÉLITES (les "
        "PROPHÉTIQUES !). La BALISTIQUE (2Ch 35:23 : les ARCHERS (les yorim (les FLÈCHES (les BLESSURES (les "
        "CHARS (les ROIS (les VULNÉRABLES (les CUIRASSES (les INSUFFISANTES (les DÉGUISÉS (35:22 ! (les RUSES (les "
        "Vaines (les PRÉCISIONS — les MORTELLES (les GUERRES (les ANTIQUES !). La THANATOLOGIE (les SECOND CHAR "
        "(les rekhev mishneh (les TRANSPORTS (les BLESSÉS (les MEGUIDDO → JÉRUSALEM (les ~90 KM (les AGONIES (les "
        "ROUTES (les DEUILS (les NATIONAUX (les EMBÔUMEMENTS ? (les RITES (les ROYAUX !)."
    ),
    schema=(
        "JOSIAS EN 11 TEMPS : 8 ANS (les ENFANTS-ROIS !) → NOMMÉ (« JOSHIYYAHOU » (RO077 !) → 18e ANNÉE (les TRAVAUX !) "
        "→ LIVRE (« TROUVÉ… MAISON » : les EXPLOSIFS !) → DÉCHIRE (« ENTENDIT… DÉCHIRA » : les CONVAINCUS !) → « GRANDE "
        "COLÈRE » (les LUCIDES !) → HULDA (« PROPHÉTESSE… SECOND QUARTIER » : les CONSULTEES !) → « DITES à l'HOMME » "
        "(les DISTANCES !) → « MALHEUR… NE S'ÉTEINDRA PAS » (les MAINTENUS !) → « CŒUR TENDRE… ENTENDU » (les ÉMUS !) → "
        "« RECUEILLI… PAIX… NE VERRONT PAS » (les GRACIÉS !) → MEGUIDDO (« NÉKO… ARCHERS… SÉPULCRE » : les PLEURÉS !). "
        "Le cœur tendre déchire ses vêtements — les yeux se fermeront avant le malheur."
    ),
    limites=(
        "Le LIVRE (les DEUTÉRONOMES ? (les CONSENSUS (les PENTATEUQUES ? (les ENTIERS ? (les PARTIES (les DÉBATS (les "
        "CRITIQUES (les TEXTES (les DISENT (les LOI (les CONTENUS (les PRÉCIS (les INCONNUS (les PROPOSÉS (pas les "
        "IMPOSÉS !). POURQUOI HULDA (les JÉRÉMIE (les CONTEMPORAINS (les JEUNES ? (les ABSENTS ? (les ANATOTH ? (les "
        "TEXTES (les TAIRENT (les CHOIX (les DIVINS (les SOUVERAINS (les FEMMES (les HONORÉES (les RAISONS (les "
        "MYSTÈRES !). « PAIX » vs VIOLENCE (les TENSIONS (les ASSUMÉES (les PAIX (les CIRCONSTANCIELLES (les NON (les "
        "PAIX (les ESCHATOLOGIQUES (les OUI (les THÉOLOGIES (les PARADOXES (les FÉCONDS (les MORTS (les PAISIBLES "
        "(les GUERRES !). MEGUIDDO (les CIRCONSTANCES (les BATAILLES (les RANGÉES (les GUET-APENS (les « DÉGUISÉ » "
        "(2Ch 35:22 (les RUSES (les MOTIFS (les JOSIAS (les INTERCEPTIONS (les DÉBATTUS (les DÉTAILS (les RARES (les "
        "MORTS (les CERTAINES !). Les LAMENTATIONS (2Ch 35:25 : les JÉRÉMIE (les COMPOSA (les TEXTES (les PERDUS (les "
        "CANONS (les ABSENTS (les DEUILS (les LITTÉRAIRES (les MÉMOIRES (les NATIONALES !)."
    ),
    accomplissement=[(("22:8-11", "LIVRE (TROUVÉ) + « DÉCHIRA »")),
        ((("22:13-14"), "« COLÈRE » + HULDA (CONSULTÉE)")),
        ((("22:15-17"), "« HOMME » + « NE S'ÉTEINDRA PAS »")),
        ((("22:18-20"), "TENDRE + ENTENDU + « PAIX… NE VERRONT »")),
        ((("23:29-30"), "MEGUIDDO (NÉKO !) + PLEURÈRENT")),
        ((("2Ch 35:23-24"), "ARCHERS + SÉPULCRE (PÈRES !)"))],
    tl=[((("22:8"), "LIVRE (TROUVÉ)")),
        ((("22:14"), "HULDA (QUARTIER)")),
        ((("22:19"), "« ENTENDU » (PLEURÉ)")),
        ((("22:20"), "« PAIX » (YEUX !)")),
        ((("23:29"), "MEGUIDDO (NÉKO)"))],
    src=[("Les morts qui doivent ressusciter (Hulda, Josias recueilli, 2R 22:20)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1965082"),
        ("2 Rois 22 — Bible d'étude (Hulda, Josias, 22:14-20)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/12/22"),
        ("2 Rois 22 — Traduction du monde nouveau (livre, réforme)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/12/22")],
    img="images/prophe_RO099_paix.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="CH100", titre="« Vous m'avez abandonné » : Shishaq dominera, mais la ruine ne sera pas complète",
    ref="2 Chroniques 12:5-8",
    statut="Accomplie",
    cat="CH", syst="Oracle de Shemaya (affermi → abandon → 5e année → abandonné → humiliés → assujettis)",
    reg="Registre : 2 Chroniques — P100 (12:5-8 : Shishaq dominera, ruine pas complète) ; accomplissement 2Ch 12:9-12",
    texte=[
        "« AFFERMI… FORT… ABANDONNA la LOI… ISRAËL AVEC LUI. » (12:1 — lui !)",
        "« 5e ANNÉE… SHISHAQ… INFIDÉLITÉ. » (12:2 — infidélité !)",
        "« 1 200 CHARS… 60 000 CAVALIERS… INNOMBRABLES. » (12:3 — innombrables !)",
        "« VILLES FORTIFIÉES PRISES… JÉRUSALEM ATTEINTE. » (12:4 — atteinte !)",
        "« Vous M'AVEZ ABANDONNÉ… Je vous ABANDONNE à SHISHAQ. » (12:5 — Shishaq !)",
        "« S'HUMILIÈRENT… JÉHOVAH est JUSTE ! » (12:6 — juste !)",
        "« HUMILIÉS… PAS DÉTRUIRAI… SECOURS… COLÈRE PAS RÉPANDUE. » (12:7 — répandue !)",
        "« ASSUJETTIS… SAURONT… ME SERVIR vs ROYAUMES. » (12:8 — royaumes !)",
        "« TRÉSORS PRIS… TOUT… BOUCLIERS OR. » (12:9 — or !)",
        "« BOUCLIERS CUIVRE… COUREURS… CHAMBRE. » (12:10-11 — chambre !)",
        "« HUMILIÉ… COLÈRE DÉTOURNÉE… RUINE PAS COMPLÈTE. » (12:12 — complète !)",
        "« BONNES CHOSES… en JUDA. » (12:12 — Juda !)",
    ],
    contexte=(
        "Jérusalem, ~925 — ROBOAM 41 ANS (les FILS (les SALOMON (les NAAMA (les AMMONITES (les 17 ANS (les "
        "997 ? (les 930 ? (les DATES (les DÉBATTUES (les DERNIERS (les UNI (les PREMIERS (les SUD (les CHARNIÈRES "
        "— les DYNASTIQUES (les SCHISMES (les SURVIVANTS !). 3 ANS FIDÈLES (11:17 : les DÉBUTS (les BONS (les "
        "LÉVITES (les RALLIÉS (les NORD (les FUIENT (les JÉROBOAM (les FORTIFIE (11:5-12 : les VILLES (les "
        "MURS (les VIVRES (les SYSTÈMES (les DÉFENSIFS (les PUIS… (les SUCCÈS (les CORROMPENT (les AFFERMIS (les "
        "ABANDONNENT ! : les COURBES — les CLASSIQUES (les CRISES (les PIÉTÉS (les PROSPÉRITÉS (les APOS-TASIES "
        "!). SHEMAYA (12:5 : le MÊME (11:2-4 : « NE MONTEZ PAS… contre vos FRÈRES » (les GUERRES (les FRATRICIDES "
        "(les INTERDITES (les PROPHÈTES (les ÉCOUTÉS (les ARMÉES (les RENVOYÉES (les AUTORITÉS — les ÉTABLIES (les "
        "PAROLES (les CRUES (les DEUXIÈMES (les ORACLES !). PARALLÈLE RO076 (1R 14:25-28 : les ROIS (les RACONTENT "
        "(les FAITS (les CHRONIQUES (les EXPLIQUENT (les SENS (les DEUX (les LIVRES (les COMPLÉMENTAIRES (les "
        "THÉOLOGIES — les CROISÉES (les ÉVÉNEMENTS (les INTERPRÉTÉS !)."
    ),
    explication=(
        "« Vous M'AVEZ ABANDONNÉ ('azavtem oti)… Je vous ABANDONNE (ve'ezov) », 12:5 : 'azav — ABANDONNER "
        "(les MIROIRS (les VERBAUX (les MÊMES (les VERBES (les SUJETS (les INVERSÉS (les JUSTICES — les POÉTIQUES "
        "(les ABANDONS (les RENDUS (les MONNAIES !). « Ils S'HUMILIÈRENT (vayyikkane'u)… JÉHOVAH est JUSTE "
        "(tsaddiq) », 12:6 : kana' + tsedeq — HUMILIER + JUSTE (les CONFESSIONS (les PUBLIQUES (les ROIS (les CHEFS "
        "(les ENSEMBLE (les VERDICTS (les ACCEPTÉS (les DIEUX (les JUSTIFIÉS (les REPENTIRS — les COLLECTIFS (les "
        "EFFICACES !). « Ils se sont HUMILIÉS… je ne les DÉTRUIRAI PAS (lo' ashchitem) », 12:7 : shachath — "
        "DÉTRUIRE (les RETENUES (les DIVINES (les COLÈRES (les SUSPENDUES (les DESTRUCTIONS (les ANNULÉES (les "
        "PILLAGES (les MAINTENUS (les GRÂCES — les PARTIELLES (les VIES (les SAUVÉES (les BIENS (les PERDUS !). « "
        "Ils lui SERONT ASSUJETTIS (la'avodim)… ils SAURONT (veyede'u)… ME SERVIR ('avodati) », 12:8 : 'avad — "
        "SERVIR (les PÉDAGOGIES (les VASSALITÉS (les LEÇONS (les SERVITUDES (les COMPARÉES (les JOUG DOUX (les "
        "JOUG FER (les DIFFÉRENCES — les ÉPROUVÉES (les THÉOLOGIES (les EXPÉRIENTIELLES !). « Sa RUINE (venatati "
        "lo' khalah) ne FUT PAS COMPLÈTE », 12:12 : kalah — COMPLÈTE (les TOTALITÉS (les ÉVITÉES (les RESTES (les "
        "PRÉSERVÉS (les BONNES CHOSES (devarim tovim : les SURVIVANTS (les JUSTES (les RÉSIDUS (les ESPOIRS !)."
    ),
    interpretation=(
        "Le MIROIR ABANDON (les ÉQUATIONS (les SPIRITUELLES (les CAUSES (les EFFETS (les SYMÉTRIES — les DIVINES "
        "(les TRAITEMENTS (les MÉRITÉS (les MESURES (les RENDUES !). L'HUMILIATION ARRÊTE (les CONDITIONS (les "
        "REMPLIES (les DESTRUCTIONS (les ÉVITÉES (les PILLAGES (les SUBIS (les GRÂCES — les GRADUÉES (les TOUT (les "
        "NON (les RIEN (les NON (les PARTIEL (les OUI !) + 1200013592 : « Si Roboam… ne s'étaient PAS HUMILIÉS… pas "
        "même JÉRUSALEM n'aurait ÉCHAPPÉ » (OFFICIEL ! (les CONTREFACTUELS — les OFFICIELS (les HUMILIATIONS (les "
        "SAUVEUSES !). SERVIR POUR APPRENDRE (les VASSALITÉS (les ÉCOLES (les PHARAONS (les MAÎTRES (les DURS (les "
        "JÉHOVAH (les MAÎTRES (les BONS (les CONTRASTES — les VÉCUS (les RETOURS (les PRÉPARÉS !). ROIS vs CHRONIQUES "
        "(les FAITS (les SENS (les 1R 14 (les SOBRE (les 2Ch 12 (les THÉOLOGIQUE (les LECTURES — les COMPLÈTES (les "
        "DEUX (les LIVRES (les UNE (les HISTOIRE !)."
    ),
    hist=(
        "SHESHONQ Ier (les XXIIe (les DYNASTIES (les LIBYENNES (les BUBASTIS (les PHARAONS (les FONDATEURS (les "
        "EMPIRES (les RECONSTITUÉS (les LEVANT (les REGARDS (les TRIBUTS (les EXIGÉS !). KARNAK 142 VILLES (les "
        "MURS (les TEMPLES (les LISTES (les GRAVÉES (les TAANAK (les MEGUIDDO (les GIBEON (les JUDA (les ABSENTS ? "
        "(les DÉBATS (les ÉGYPTOLOGUES (les LECTURES (les INCERTAINES (les CAMPAGNES — les CONFIRMÉES (les DÉTAILS "
        "(les DISCUTÉS : fond seul, jamais en sources !). La STÈLE de MEGUIDDO (les FRAGMENTS (les SHESHONQ (les "
        "NOMS (les VICTOIRES (les MARQUÉES (les GARNISONS (les POSÉES (les EMPIRE — les TAMPONNÉ (les PIERRES !). Les "
        "BOUCLIERS d'OR (1R 10:16-17 : les 600 SICLES (les SALOMON (les FASTES (les PILLÉS (les REMPLACÉS (les "
        "CUIVRE (les DÉVALUATIONS — les SYMBOLIQUES (les GLOIRES (les PERDUES (les PAREILS (les PAUVRES !)."
    ),
    geo=(
        "Les VILLES FORTIFIÉES (11:5-12 : les 15 VILLES (les BETHLÉEM (les ÉTAM (les TEQOA (les ADORAÏM (les "
        "SYSTÈMES (les ROBOAM (les BÂTIS (les SHISHAQ (les PREND (les IRONIES — les DÉFENSIVES (les FORTIFICATIONS "
        "(les INUTILES (les SANS-DIEU !). JÉRUSALEM ATTEINTE (12:4 : « ARRIVA (vayyavo')… à JÉRUSALEM » (les "
        "CAPITALES (les MENACÉES (les NON-PRISES (les RANÇONNÉES (les TRÉSORS (les VIDÉS (les MURS (les DEBOUT (les "
        "GRÂCES — les GÉOGRAPHIQUES (les ÉPARGNÉES (les IN-EXTREMIS !). L'ÉGYPTE COALISÉE (12:3 : les LIBYENS (les "
        "SOUKIENS (les ÉTHIOPIENS (les EMPIRES (les MULTIETHNIQUES (les MERCENAIRES (les VASSAUX (les ARMÉES — les "
        "BIGARRÉES (les PUISSANCES (les MONDIALES !). La ROUTE (les DELTA → JUDA (les CÔTIÈRES (les PHILISTINS (les "
        "TRAVERSÉS (les SHÉPHÉLAH (les MONTÉES (les MONTAGNES (les ASSIÉGÉES (les LOGISTIQUES — les IMPÉRIALES (les "
        "RAVITAILLÉES (les ÉCRASANTES !)."
    ),
    sci=(
        "Les CHIFFRES ARMÉES (12:3 : les 1 200 CHARS (les 60 000 CAVALIERS (les INNOMBRABLES (les FANTASSINS (les "
        "HYPERBOLES ? (les RÉELS (les COPIES (les FAUTES (les DÉBATS (les MILITAIRES (les ANTIQUES (les LOGISTIQUES "
        "(les IMPOSSIBLES ? (les POSSIBLES (les EMPIRES (les RICHES : les NOMBRES — les DISCUTÉS (les ORDRES (les "
        "ÉNORMES (les CERTAINS !). La MÉTALLURGIE (les OR → CUIVRE (12:9-10 (les DÉVALUATIONS (les 600 SICLES (les "
        "FASTES (les SALOMON (les FINANCES (les RUINÉES (les TRÉSORS (les DOUBLES (les TEMPLE (les PALAIS (les "
        "ÉCONOMIES — les PILLÉES (les GLOIRES (les FONDUES !). Les FORTIFICATIONS (11:5-12 : les CASEMATES (les "
        "TOURS (les VIVRES (les HUILES (les VINS (les SYSTÈMES (les COMPLETS (les FOULLES (les LAKISH ? (les AZÉQA ? "
        "(les ARCHÉOLOGIES (les PROPOSÉES (les DÉFENSES — les SAVANTES (les VAINES (les SANS-DIEU !). La CÉRÉMONIE "
        "(12:11 : les COUREURS (les ratsim (les BOUCLIERS (les PORTÉS (les ESCORTES (les ROYALES (les PROTOCOLES (les "
        "MAINTENUS (les PAUVRES (les FASTES (les PERSISTANTS (les APPARENCES — les SAUVÉES (les SUBSTANCES (les "
        "PERDUES !)."
    ),
    schema=(
        "SHISHAQ EN 10 TEMPS : AFFERMI (« FORT… ABANDONNA la LOI » : les CORROMPUS !) → 5e ANNÉE (« SHISHAQ… "
        "INFIDÉLITÉ » : les CHÂTIÉS !) → ARMÉE (« 1 200… 60 000… INNOMBRABLES » : les ÉCRASÉS !) → VILLES (« "
        "FORTIFIÉES PRISES… JÉRUSALEM » : les ATTEINTS !) → SHEMAYA (« Vous M'AVEZ ABANDONNÉ… Je vous ABANDONNE » : "
        "les MIROIRS !) → HUMILIÉS (« JÉHOVAH est JUSTE ! » : les CONFESSÉS !) → « PAS DÉTRUIRAI… SECOURS » (les "
        "RETENUS !) → « ASSUJETTIS… SAURONT » (les ÉCOLIERS !) → TRÉSORS (« TOUT… BOUCLIERS OR » : les VIDÉS !) → "
        "CUIVRE (« COUREURS… CHAMBRE » : les DÉVALUÉS !) → « RUINE PAS COMPLÈTE… BONNES CHOSES » (les PRÉSERVÉS !). "
        "Abandonné pour abandon — humilié puis assujetti, mais pas détruit."
    ),
    limites=(
        "Les CHIFFRES (les 1 200 (les 60 000 (les HYPERBOLES (les COPISTES (les ZÉROS (les DÉBATS (les TEXTOLOGUES "
        "(les SEPTANTE (les VARIANTES (les ORDRES (les GRANDEURS (les PLAUSIBLES (les PRÉCISIONS (les SUSPECTES !). "
        "KARNAK (les JUDA (les ABSENTS (les JÉRUSALEM (les ABSENTES (les LECTURES (les INCERTAINES (les NOMS (les "
        "ABÎMÉS (les CAMPAGNES (les CONFIRMÉES (les ITINÉRAIRES (les RECONSTITUÉS (les DÉBATS (les OUVERTS : fond "
        "seul !). Les DATES (les 997 (les it-2 (les 930 (les STANDARD (les CHRONOLOGIES (les DIVERSES (les THIELE (les "
        "GALIL (les 5e ANNÉE (les RELATIVES (les SÛRES (les ABSOLUES (les CIRCA !). Les ÉCRITS de SHEMAYA (12:15 : "
        "les SOURCES (les PERDUES (les CITÉES (les NON-CANONIQUES (les ARCHIVES (les ROYALES (les PROPHÉTIQUES (les "
        "CONTENUS (les INCONNUS (les HISTORIOGRAPHIES — les SOURCÉES (les TRANSPARENTES !). Les SOUKIENS (12:3 : les "
        "PEUPLES (les MYSTÉRIEUX (les TROGLODYTES ? (les IDENTIFICATIONS (les PROPOSÉES (les ÉGYPTOLOGUES (les "
        "CHERCHENT (les NOMS (les RARES (les SENS (les INCERTAINS !)."
    ),
    accomplissement=[(("12:1-4", "ABANDON + 5e ANNÉE + ARMÉE + VILLES")),
        ((("12:5-6"), "« ABANDONNE » + « JUSTE ! »")),
        ((("12:7-8"), "« PAS DÉTRUIRAI » + « ASSUJETTIS »")),
        ((("12:9-11"), "TRÉSORS (TOUT !) + CUIVRE")),
        ((("12:12"), "« PAS COMPLÈTE » + « BONNES »"))],
    tl=[((("12:2"), "5e ANNÉE (SHISHAQ)")),
        ((("12:5"), "« ABANDONNE » (MIROIR)")),
        ((("12:6"), "« JUSTE ! » (HUMILIÉS)")),
        ((("12:9"), "TRÉSORS (TOUT)")),
        ((("12:12"), "« PAS COMPLÈTE »"))],
    src=[("Roboam — Étude (abandon, humiliation, Shishaq, boucliers)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200013592"),
        ("2 Chroniques 12 — Bible d'étude (Shemaya, Shishaq, 12:1-12)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/12"),
        ("2 Chroniques 12 — Traduction du monde nouveau (Roboam, Égypte)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/14/12")],
    img="images/prophe_CH100_shishaq.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="CH101", titre="« La bataille n'est pas la vôtre » : Josaphat, Jahaziel et les chanteurs à l'avant-garde",
    ref="2 Chroniques 20:15-17, 20",
    statut="Accomplie",
    cat="CH", syst="Bataille divine (multitude → jeûne → esprit → pas vôtre → chanteurs → entretués → Berakha)",
    reg="Registre : 2 Chroniques — P101 (20:15-17, 20 : bataille pas la vôtre, tenez-vous, voyez le salut) ; accomplissement 2Ch 20:22-25",
    texte=[
        "« MOAB + AMMON + MÉOUNIM… EN-GUÉDI… MULTITUDE. » (20:1-2 — multitude !)",
        "« JOSAPHAT CRAIGNIT… JEÛNE… CHERCHER. » (20:3 — chercher !)",
        "« PRIÈRE… ABRAHAM… NE SAVONS… YEUX sur TOI. » (20:5-12 — toi !)",
        "« TOUT JUDA… ENFANTS… DEBOUT devant JÉHOVAH. » (20:13 — debout !)",
        "« ESPRIT sur JAHAZIEL… ASAPH… ASSEMBLÉE. » (20:14 — assemblée !)",
        "« PAS PEUR… BATAILLE PAS VÔTRE… mais DIEU. » (20:15 — Dieu !)",
        "« DESCENDEZ… MONTÉE TSITS… VALLÉE JERUEL. » (20:16 — Jeruel !)",
        "« PAS COMBATTRE… TENEZ-VOUS… VOYEZ SALUT. » (20:17 — salut !)",
        "« CROYEZ… SUCCÈS… CROYEZ PROPHÈTES… PROSPÉREREZ. » (20:20 — prospérerez !)",
        "« CHANTEURS… AVANT-GARDE… LOUEZ… BONTÉ. » (20:21 — bonté !)",
        "« EMBUCADES… ENTRETUÉS… AUCUN ÉCHAPPÉ. » (20:22-24 — échappé !)",
        "« 3 JOURS BUTIN… VALLÉE BERAKHA… JOIE. » (20:25-27 — joie !)",
    ],
    contexte=(
        "Jérusalem, ~870-848 — JOSAPHAT (les BONS (les ROIS (les ALLIÉS (les ACHAB (RO083 ! (les JORAM (RO085 ! "
        "(les FAUTES (les ALLIANCES (les PIÉTÉS (les RÉELLES (les RÉFORMES (les JUGES (19:4-11 ! (les ENSEIGNANTS "
        "(les LOI (17:7-9 ! : les BONS — les IMPARFAITS (les ALLIÉS (les MAL (les PIEUX (les QUAND-MÊME !). La "
        "COALITION (20:1 : les MOAB (les AMMON (les MÉOUNIM (les TRANSJORDANIENS (les COALISÉS (les EN-GUÉDI (les "
        "HATSATSON-THAMAR (les OASIS (les MER MORTE (les MENACES — les EXISTENTIELLES (les MULTITUDES (les "
        "CONVERGENTES !). La PEUR SAINTE (20:3 : « JOSAPHAT CRAIGNIT (vayyira')… et se DISPOSA (vayyitten panav) à "
        "CHERCHER » (les PEURS (les AVouÉES (les JEÛNES (les PROCLAMÉS (les NATIONS (les MOBILISÉES (les ENFANTS (les "
        "DEBOUT (20:13 ! (les TOUT-PETITS (les PRÉSENTS (les ASSEMBLÉES — les TOTALES (les FAMILLES (les PRIANTES !). "
        "JAHAZIEL (20:14 : les LÉVITES (les ASAPH (les CHANTRES (les GÉNÉALOGIES (les 5 GÉNÉRATIONS (les ESPRITS (les "
        "TOMBENT (les ASSEMBLÉES (les MILIEUX (les PROPHÉTIES — les SPONTANÉES (les LITURGIQUES (les INSPIRÉES !)."
    ),
    explication=(
        "« La BATAILLE (hammilchamah) N'EST PAS la VÔTRE (lo' lakhem)… mais CELLE de DIEU (le'lohim) », 20:15 : "
        "milchamah — BATAILLE (les POSSESSIONS (les NIÉES (les TRANSFÉRÉES (les GUERRES (les DIVINES (les ARMÉES (les "
        "SPECTATRICES (les GÉNÉRAUX — les CÉLESTES (les STRATÈGES (les INFAILLIBLES !). « N'AYEZ PAS PEUR (al-tire'u) "
        "et NE SOYEZ PAS TERRIFIÉS (al-techattu) », 20:15 : yare' + chathath — PEUR + EFFROI (les DOUBLES (les NÉGATIONS "
        "(les ÉMOTIONS (les INTERDITES (les COURAGES (les COMMANDÉS (les PEURS — les DÉSOBÉISSANCES (les FOIS (les "
        "OBÉISSANCES !). « Vous N'AUREZ PAS à COMBATTRE (lo' lakhem lehillachem) », 20:17 : lacham — COMBATTRE (les "
        "DISPENSES (les TOTALES (les ÉPÉES (les FOURREAUX (les SOLDATS (les TÉMOINS (les VICTOIRES — les SANS-COMBATS "
        "(les GRATUITES (les DIVINES !). « TENEZ-VOUS LÀ (hityatsevu)… et VOYEZ (ure'u) le SALUT (teshu'at) », 20:17 : "
        "yatsav + ra'ah — SE TENIR + VOIR (les POSTURES (les STATIQUES (les REGARDS (les ACTIFS (les FOIS — les "
        "SPECTATRICES (les PRÉSENCES (les REQUISES (les ACTIONS (les INTERDITES !). « CROYEZ (ha'aminu)… vous AUREZ du "
        "SUCCÈS (teamenu)… CROYEZ ses PROPHÈTES… vous PROSPÉREREZ (vehatslichu) », 20:20 : aman — CROIRE (les DOUBLES "
        "(les FOIS (les DIEUX (les PROPHÈTES (les SUCCÈS (les STABILITÉS (les PROSPÉRITÉS (les RÉUSSITES (les ÉQUATIONS "
        "— les SPIRITUELLES (les FOIS (les SUCCÈS (les GARANTIS !) + 1984484 : « AYEZ FOI en JÉHOVAH… et ayez du SUCCÈS ! » "
        "(OFFICIEL ! (les DEVISES — les OFFICIELLES (les FOIS (les VICTORIEUSES !). « Des CHANTEURS (meshorerim)… en AVANT "
        "(lifney) des HOMMES ARMÉS », 20:21 : shir — CHANTER (les AVANT-GARDES (les MUSICALES (les ARMURES (les ORNEMENTS "
        "(les SAINTS (les ÉPÉES (les LOUANGES (les STRATÉGIES — les ABSURDES (les HUMAINEMENT (les GÉNIALES (les "
        "DIVINEMENT !)."
    ),
    interpretation=(
        "La STRATÉGIE DIVINE (les DESCENDRE (les RENCONTRER (les NE-PAS-Frapper (les ORDRES (les PARADOXAUX (les "
        "OBÉISSANCES (les CONFIANTES (les PRÉSENCES (les REQUISES (les ACTIONS (les RÉSERVÉES (les PARTAGES — les "
        "RÔLES (les DIEUX (les COMBATTENT (les HOMMES (les REGARDENT !). La FOI SPECTATRICE (les TENEZ-VOUS (les "
        "VOYEZ (les VERBES (les CONTEMPLATIFS (les SALUTS (les OFFERTS (les GRÂCES — les VISIBLES (les TÉMOINS (les "
        "REQUISES (les MÉRITES (les EXCLUS !). La LOUANGE ARME (les CHANTEURS (les SOLDATS (les CHANTS (les ÉPÉES (les "
        "BONTÉS (les CÉLÉBRÉES (les ENNEMIS (les CONFONDUS (les MUSIQUES — les GUERRIÈRES (les ADORATIONS (les "
        "VICTORIEUSES !). Le GRAND JOSAPHAT (les TYPES (les JÉSUS (les ANTITYPES (les MILLÉNAIRES (les REPOS (les "
        "1984484 : « le DOMAINE ROYAL de JÉSUS CHRIST, le GRAND JOSAPHAT, connaîtra le CALME » (OFFICIEL ! (les "
        "LECTURES — les OFFICIELLES (les JOSAPHAT (les FIGURES (les CHRIST (les RÉALITÉS !). BERAKHA (les BÉNÉDICTIONS "
        "(les VALLÉES (les NOMMÉES (les JOIES (les BAPTISÉES (les LIEUX (les MÉMOIRES (les GÉOGRAPHIES — les "
        "RECONNAISSANTES (les VICTOIRES (les TOPONYMES !)."
    ),
    hist=(
        "La COALITION (les MOAB (les MÉSA ? (les AMMON (les ÉDOM/MÉOUNIM (les TRANSJORDANIE (les COALISÉS (les RARES "
        "(les DANGERS (les MORTELS (les CONTEXTES (les IXe (les SIÈCLES (les GÉOPOLITIQUES — les TROUBLES (les VOISINS "
        "(les LIGUÉS !). EN-GUÉDI (les OASIS (les FOUILLES (les SANCTUAIRES (les CHALCOLITHIQUES (les SOURCES (les "
        "DOUCES (les MER MORTE (les ABORDS (les REFUGES (les DAVID (1S 24 ! (les STRATÉGIQUES — les EAU (les DÉSERTS "
        "(les VIES !). Les 3 JOURS BUTIN (20:25 : les ABONDANCES (les DÉPOUILLES (les RICHESSES (les VÊTEMENTS (les "
        "OBJETS (les PRÉCIEUX (les QUANTITÉS — les DÉMESURÉES (les RAMASSAGES (les PROLONGÉS (les JOIES (les "
        "MATÉRIELLES !). JOSAPHAT ~870-848 (les 25 ANS (les CHRONOLOGIES (les ALLIANCES (les ACHAB (les JORAM (les "
        "RÉFORMES (les JUGES (les ENSEIGNANTS (les BILANS — les POSITIFS (les NUANCÉS (les FIDÈLES (les "
        "GLOBAUX !)."
    ),
    geo=(
        "EN-GUÉDI (20:2 : les HATSATSON-THAMAR (les PALMIERS (les OASIS (les FALAISES (les SOURCES (les MER MORTE (les "
        "OUEST (les ÉTAPES (les INVASIONS (les TÊTES (les PONTS (les DÉSERTS — les FERTILES (les MENACES (les "
        "PROCHES !). La MONTÉE de TSITS (20:16 : les PASSES (les OUEDS (les MONTÉES (les PRÉCISES (les ITINÉRAIRES "
        "(les DIVINS (les RENDEZ-VOUS (les FIXÉS (les TOPOGRAPHIES — les PROPHÉTIQUES (les CARTES (les RÉVÉLÉES !). Le "
        "DÉSERT de JERUEL (20:16 : les FACES (les VALLÉES (les EXTRÉMITÉS (les LIEUX (les INTROUVABLES (les MODERNES "
        "(les LOCALISATIONS (les PROPOSÉES (les NOMS (les PERDUS (les SABLES — les MYSTÉRIEUX (les PAROLES (les "
        "PRÉCISES !). La VALLÉE de BERAKHA (20:26 : les 4e JOURS (les ASSEMBLÉES (les BÉNÉDICTIONS (les WADIS (les "
        "IDENTIFIÉS (les BEREIKOUT ? (les CANDIDATS (les DÉBATS (les TOPONYMES — les JOYEUX (les MÉMOIRES (les "
        "CHANTÉES !)."
    ),
    sci=(
        "Les EMBUCADES DIVINES (20:22 : « JÉHOVAH MIT (natan) des EMBUCADES (me'arvim) » (les MÉCANISMES (les TUS (les "
        "AGENTS (les DIVINS (les EFFETS (les CONFUSIONS (les ENTRETUÉS (les CAUSES — les AFFIRMÉES (les MODES (les "
        "MYSTÉRIEUX !). La PSYCHOLOGIE des PANIQUES (les COALITIONS (les FRAGILES (les MÉFIANCES (les ALLIÉS (les NUIT "
        "(les CRIS (les AMIS (les ENNEMIS (les CONFONDUS (les ENTRETUÉS (les DYNAMIQUES — les FOULES (les PEURS (les "
        "CONTAGIEUSES (les MASSACRES (les FRATRICIDES !). La LOGISTIQUE BUTIN (les 3 JOURS (les RAMASSAGES (les "
        "TRANSPORTS (les ÂNES (les CHARIOTS (les QUANTITÉS (les COLOSSALES (les CADAVRES (les DÉPOUILLÉS (les "
        "RICHESSES — les TRANSFÉRÉES (les ENNEMIS (les DÉPOUILLES (les JUDA (les ENRICHIS !). La MUSICOLOGIE (les "
        "ASAPH (les LÉVITES (les CHANTRES (les ORNEMENTS (les SAINTS (les bigdey-qodesh (les LITURGIES (les GUERRIÈRES "
        "(les PSAUMES (les ARMÉS (les ACOUSTIQUES — les VALLÉES (les CHANTS (les RÉSONNENT (les ENNEMIS (les "
        "ENTENDENT !)."
    ),
    schema=(
        "JOSAPHAT EN 12 TEMPS : MULTITUDE (« MOAB + AMMON… EN-GUÉDI » : les COALISÉS !) → CRAIGNIT (« JOSAPHAT "
        "CRAIGNIT » : les AVouÉS !) → JEÛNE (« PROCLAMA… CHERCHER » : les MOBILISÉS !) → PRIÈRE (« NE SAVONS… YEUX "
        "sur TOI » : les HUMBLES !) → DEBOUT (« TOUT JUDA… ENFANTS » : les ASSEMBLÉS !) → ESPRIT (« sur JAHAZIEL… "
        "ASAPH » : les INSPIRÉS !) → « PAS PEUR… PAS VÔTRE… DIEU » (les TRANSFÉRÉS !) → « DESCENDEZ… TSITS… JERUEL » "
        "(les RENDEZ-VOUS !) → « PAS COMBATTRE… TENEZ… VOYEZ » (les SPECTATEURS !) → « CROYEZ… SUCCÈS… PROSPÉREREZ » "
        "(les ÉQUATIONS !) → CHANTEURS (« AVANT-GARDE… LOUEZ » : les MUSICAUX !) → ENTRETUÉS (« EMBUCADES… AUCUN "
        "ÉCHAPPÉ » : les CONFONDUS !) → BUTIN (« 3 JOURS… BERAKHA… JOIE » : les ENRICHIS !). Descendre sans combattre "
        "— chanter et voir le salut."
    ),
    limites=(
        "Les MÉOUNIM (20:1 : les QUI (les MAON (les MINAÉENS (les ÉDOMITES (les FAUTES (les COPISTES (les ARAM ? (les "
        "ÉDOM ? (les TEXTOLOGUES (les DÉBATTENT (les IDENTITÉS (les INCERTAINES (les COALITIONS (les CERTAINES !). Les "
        "EMBUCADES (20:22 : les COMMENT (les TEXTES (les TAIRENT (les ANGES ? (les ILLUSIONS ? (les CONFUSIONS (les "
        "NATURELLES (les SURNATURELLES (les MÉCANISMES (les NON-DITS (les AGENTS (les DITS (les MYSTÈRES — les ASSUMÉS "
        "!. TSITS + JERUEL (20:16 : les OÙ (les LOCALISATIONS (les PERDUES (les PROPOSÉES (les OUEDS (les CANDIDATS "
        "(les FOUILLES (les VAINES (les NOMS (les DISPARUS (les CARTES (les BLANCHES !). Les EFFECTIFS (les MULTITUDES "
        "(les CHIFFRES (les ABSENTS (les ENNEMIS (les INNOMBRÉS (les JUDA (les INNOMBRÉS (les COMPARAISONS (les "
        "IMPOSSIBLES (les VICTOIRES (les TOTALES (les CERTAINES !). Le GRAND JOSAPHAT (les TYPES (les 1984484 (les "
        "OFFICIELLES (les APPLICATIONS (les MILLÉNAIRES (les LECTURES (les AUTORISÉES (les DÉBATS (les EXÉGÈTES (les "
        "LIBRES !)."
    ),
    accomplissement=[(("20:1-4", "COALITION (EN-GUÉDI) + PEUR + JEÛNE")),
        ((("20:5-14"), "PRIÈRE (« YEUX ») + DEBOUT + ESPRIT (ASAPH)")),
        ((("20:15-17"), "« PAS VÔTRE » + TSITS + « TENEZ… VOYEZ »")),
        ((("20:20-21"), "« CROYEZ » + CHANTEURS (AVANT !)")),
        ((("20:22-25"), "ENTRETUÉS (!) + BUTIN (3 JOURS !)")),
        ((("20:26-30"), "BERAKHA + REPOS (CALME !)"))],
    tl=[((("20:3"), "JEÛNE (CRAIGNIT)")),
        ((("20:15"), "« PAS VÔTRE » (DIEU !)")),
        ((("20:17"), "« TENEZ… VOYEZ »")),
        ((("20:21"), "CHANTEURS (AVANT !)")),
        ((("20:26"), "BERAKHA (BÉNIE)"))],
    src=[("« La bataille n'est pas la vôtre, mais celle de Dieu » (w84, Josaphat, Jahaziel)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1984484"),
        ("2 Chroniques 20 — Bible d'étude (Jahaziel, victoire, 20:1-30)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/20"),
        ("2 Chroniques 20 — Traduction du monde nouveau (Josaphat, Berakha)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwt/14/20")],
    img="images/prophe_CH101_bataille.jpg",
))

# ---------------------------------------------------------------------------
FICHES.append(dict(
    n="CH102", titre="« Que Jéhovah voie et redemande ! » : Zacharie lapidé, la petite troupe syrienne",
    ref="2 Chroniques 24:20-22",
    statut="Accomplie",
    cat="CH", syst="Sang de Zacharie (7 ans → 130 ans → princes → revêtu → lapidé → redemande → petite troupe)",
    reg="Registre : 2 Chroniques — P102 (24:20-22 : petite troupe syrienne vaincra Juda) ; accomplissement 2Ch 24:23-25",
    texte=[
        "« JOAS… 7 ANS… BIEN… TEMPS de JEHOÏADA. » (24:1-2 — Jehoïada !)",
        "« RÉPARER la MAISON… ARGENT… OUVRIERS. » (24:4-13 — ouvriers !)",
        "« JEHOÏADA… 130 ANS… MORT… SÉPULCRE ROIS. » (24:15-16 — rois !)",
        "« PRINCES VINRENT… ROI ÉCOUTA… ABANDON… IDOLES. » (24:17-18 — idoles !)",
        "« PROPHÈTES ENVOYÉS… PAS ÉCOUTÉ. » (24:19 — écouté !)",
        "« ESPRIT REVÊTIT ZACHARIE… POURQUOI TRANSGRESSEZ ? » (24:20 — transgressez !)",
        "« PAS PROSPÉREREZ… ABANDONNÉ… ABANDONNE. » (24:20 — abandonne !)",
        "« CONSPIRÈRENT… LAPIDÈRENT… COUR… ORDRE ROI. » (24:21 — roi !)",
        "« NE SE SOUVINT PAS… BONTÉ… VOIE et REDEMANDE ! » (24:22 — redemande !)",
        "« PETITE TROUPE SYRIENS… GRANDES FORCES LIVRÉES. » (24:23 — livrées !)",
        "« PRINCES SUPPRIMÉS… BUTIN… DAMAS. » (24:23 — Damas !)",
        "« MALADIES… ASSASSINÉ LIT… PAS SÉPULCRE ROIS. » (24:25 — rois !)",
    ],
    contexte=(
        "Jérusalem, ~835-796 — JOAS 7 ANS (24:1 : les RESCAPÉS (les ATHALIE (les MASSACRES (les JEHOSHÉBA (les "
        "CACHENT (2R 11:2-3 ! (les 6 ANS (les CACHÉS (les TEMPLES (les ENFANTS (les PRÉSERVÉS (les COURONNÉS (les "
        "COUPS (les JEHOÏADA (les MONTÉS (les DETTES — les IMMENSES (les SAUVÉS (les REDEVABLES !). JEHOÏADA 130 ANS "
        "(24:15 : les LONGÉVITÉS (les EXCEPTIONNELLES (les MENTORS (les PRÊTRES (les RÉGENTS (les MORTS (les HONORÉS "
        "(24:16 : « ENTERRÉ… avec les ROIS » (les PRÊTRES (les PANTHÉONS (les ROYAUX (les FUNÉRAILLES — les UNIQUES "
        "(les MÉRITES (les RECONNUS !). Les PRINCES (24:17 : « VINRENT… SE PROSTERNÈRENT… le ROI les ÉCOUTA » (les "
        "FLATTERIES (les COURTISANS (les PRESSIONS (les JEUNES ROIS (les INFLUENÇABLES (les MENTORS (les MORTS (les "
        "VACCUMS (les REMPLIS (les IDOLÂTRES : les COURS — les CORRUPTRICES (les SOLITUDES (les DANGEREUSES !). "
        "ZACHARIE (24:20 : les FILS (les SAUVEURS (les PRÊTRES (les PROPHÈTES (les TUÉS (les SAUVÉS (les INGRATITUDES "
        "— les SUPRÊMES (les DETTES (les VIES (les PAYÉES (les MORTS !)."
    ),
    explication=(
        "« L'ESPRIT (ruach) de DIEU REVÊTIT (laveshah) ZACHARIE », 24:20 : lavash — REVÊTIR (les HABITS (les "
        "DIVINS (les PROPHÈTES (les PORTENT (les ESPRITS (les GÉDÉON (Jg 6:34 ! (les AMASAÏ (1Ch 12:18 ! (les "
        "FORMULES — les RARES (les ONCTIONS (les INTENSES (les PAROLES (les IRRÉSISTIBLES !). « POURQUOI (maddoua') "
        "TRANSGRESSEZ-VOUS ('overim) les COMMANDEMENTS ? », 24:20 : 'avar — TRANSGRESSER (les TRAVERSÉES (les "
        "LIMITES (les FRANCHIES (les QUESTIONS (les ACCUSATRICES (les CONSCIENCES — les PERCÉES (les REPROCHES (les "
        "DIRECTS !). « Vous NE PROSPÉREREZ PAS (lo' tatslichu) », 24:20 : tsalach — PROSPÉRER (les SUCCÈS (les NIÉS "
        "(les CONTRASTES (20:20 : « CROYEZ… PROSPÉREREZ » (CH101 ! (les MÊMES (les VERBES (les SORTS (les INVERSÉS "
        "(les ÉQUATIONS — les RENVERSEES (les FOIS (les SUCCÈS (les RÉBELLIONS (les ÉCHECS !). « Vous M'AVEZ ABANDONNÉ "
        "… je vous ABANDONNE », 24:20 : 'azav — ABANDONNER (les MIROIRS (les MÊMES (CH100 ! (les FORMULES (les "
        "JUGEMENTS (les RÉCURRENTES (les ABANDONS — les RENDUS (les TOUJOURS !). « Ils le LAPIDÈRENT (vayyirgeumuhu)… "
        "dans la COUR (chatsar) », 24:21 : ragam — LAPIDER (les EXÉCUTIONS (les COLLECTIVES (les LIEUX (les SAINTS "
        "(les SACRILÈGES (les ORDRES (les ROIS (les COMPLOTS (les qashar — CONSPIRER (les CONSPIRATIONS — les "
        "OFFICIELLES (les CRIMES (les D'ÉTAT !). « Que JÉHOVAH VOIE (yere') et REDEMANDE (veyidrosh) ! », 24:22 : "
        "ra'ah + darash — VOIR + REDEMANDER (les DERNIÈRES (les PAROLES (les ABEL (Gn 4:10 ! (les SANGS (les CRIENT "
        "(les DIEUX (les ENQUÊTENT (les VENGEANCES — les INVOQUÉES (les MOURANTS (les EXAUCÉS !)."
    ),
    interpretation=(
        "L'INGRATITUDE SUPRÊME (les SAUVÉS (les TUENT (les FILS (les SAUVEURS (les DETTES (les VIES (les NIÉES (24:22 : "
        "« NE SE SOUVINT PAS (lo' zakhar) de la BONTÉ (chesed) » (les OUBLIS (les VOLONTAIRES (les BONTÉS (les "
        "EFFACÉES (les MÉMOIRES — les ASSASSINES (les INGRATITUDES (les MORTELLES !). ABEL → ZACHARIE (les PREMIERS "
        "(les DERNIERS (les CANONS (les JUIFS (les CHRONIQUES (les FINISSENT (les SANGS (les ENCADRENT (les "
        "ÉCRITURES (les JÉSUS (les CITE (Mt 23:35 ! : 1200010556 : « ABEL était ainsi le PREMIER et ZACHARIE le "
        "DERNIER des hommes droits… ASSASSINÉS » (OFFICIEL ! (les INCLUSIONS — les CANONIQUES (les SANGS (les "
        "REDEMANDÉS (les GÉNÉRATIONS (les JUGÉES !). PETITE vs GRANDES (24:23 : « PETITE (mits'ar) TROUPE… GRANDES "
        "(gadol) FORCES » (les INVERSIONS (les NOMBRES (les DIEUX (les LIVRENT (les FORTS (les FAIBLES (les LEÇONS — "
        "les MATHÉMATIQUES (les DIVINES (les EFFECTIFS (les INUTILES (les FAVEURS (les DÉCISIVES !). Les SÉPULCRES "
        "INVERSÉS (les JEHOÏADA (les PRÊTRES (les ROIS (les ENTERRÉS (les JOAS (les ROIS (les REFUSÉS (24:25 : « PAS… "
        "dans les SÉPULCRES des ROIS » (les FUNÉRAILLES — les MIROIRS (les HONNEURS (les MÉRITÉS (les DÉSHONNEURS "
        "(les MÉRITÉS !)."
    ),
    hist=(
        "HAZAËL (2R 12:17-18 : les GATH (les PRISES (les JÉRUSALEM (les MENACÉES (les TRÉSORS (les RANÇONS (les "
        "QODASHIM (les RACLÉS (RO090 ! (les MÊMES (les CAMPAGNES ? (les LIENS (les PROBABLES (les HARMONIES — les "
        "PROPOSÉES (les ROIS (les RANÇONS (les CHRONIQUES (les DÉSastres !). La PETITE TROUPE (24:23 : les RAIDS (les "
        "SYRIENS (les DÉTACHEMENTS (les EXPÉDITIONS (les PUNITIVES (les EFFECTIFS (les NON-DITS (les SUCCÈS (les "
        "DISPROPORTIONNÉS (les EXPLICATIONS — les THÉOLOGIQUES (les DIEUX (les LIVRENT (les NOMBRES (les "
        "SURCLASSÉS !). DAMAS BUTIN (24:23 : les CONVOIS (les ENVOYÉS (les CAPITALES (les SYRIENNES (les TRIOMPHES "
        "(les CÉLÉBRÉS (les JUDA (les HUMILIÉS (les PILLS — les EXPOSÉS (les ENNEMIS (les ENRICHIS !). JOAS ~835-796 "
        "(les 40 ANS (les BILANS (les CONTRASTÉS (les DÉBUTS (les PIEUX (les FINS (les APOSTATES (les ASSASSINATS (les "
        "LITS (les SERVITEURS (les VENGEURS (24:26 : les FILS (les ZACHARIE ? (les JUSTICES — les POÉTIQUES (les "
        "SANGS (les PAYÉS !)."
    ),
    geo=(
        "La COUR (24:21 : les chatsar (les MAISONS (les JÉHOVAH (les AUTELS (les HOLOCAUSTES (les SANCTUAIRES (les "
        "ENTRE-DEUX (Mt 23:35 : « ENTRE le SANCTUAIRE et l'AUTEL » (les PRÉCISIONS (les JÉSUS (les CORROBORÉES : "
        "1200010556 : « Cela CORRESPONDRAIT au LIEU où JÉSUS SITUA l'ÉVÉNEMENT » (OFFICIEL ! (les TOPOGRAPHIES — les "
        "CRIMINELLES (les SACRÉES (les PROFANÉES !). DAMAS (24:23 : les DESTINATIONS (les BUTINS (les CAPITALES (les "
        "ENNEMIES (les TRIOMPHES (les HUMILIATIONS (les CONVOIS — les HONTEUX (les RICHESSES (les EXILÉES !). GATH "
        "(2R 12:17 : les ÉTAPES (les PHILISTINES (les PRISES (les ROUTES (les JÉRUSALEM (les MENACES (les CAMPAGNES "
        "— les PROGRESSIVES (les PRESSIONS (les CROISSANTES !). Les SÉPULCRES (24:25 : les CITÉS (les DAVID (les "
        "REFUS (les ENTERRÉS (les VILLES (les DAVID (les QUAND-MÊME (les DÉSHONNEURS — les NUANCÉS (les ROIS (les "
        "EXCLUS (les PANTHÉONS !)."
    ),
    sci=(
        "La LAPIDATION (24:21 : les EXÉCUTIONS (les COLLECTIVES (les PIERRES (les JETÉES (les FOULES (les PARTICIPES "
        "(les MORTS (les LENTES (les DOULOUREUSES (les RITUELS — les JUDICIAIRES (les PERVERTIS (les JUSTICES (les "
        "ASSASSINES !). La GÉRONTOLOGIE (24:15 : les 130 ANS (les LONGÉVITÉS (les RECORDS (les POST-DILUVIENS (les "
        "LITTÉRAUX (les TEXTES (les AFFIRMENT (les CRITIQUES (les DOUTENT (les FOIS — les SIMPLES (les CHIFFRES (les "
        "GARDÉS !). La MÉDECINE (24:25 : « de NOMBREUSES MALADIES (machaluim rabbim) » (les POLYPATHOLOGIES (les "
        "JUGEMENTS (les SOMATIQUES (les STRESS (les DÉFAITES (les PSYCHOSOMATIQUES (les CORPS — les FRAPPÉS (les ÂMES "
        "(les JUGÉES !). L'ASYMÉTRIE MILITAIRE (les PETITES (les TROUPES (les GRANDES (les FORCES (les GUÉRILLAS (les "
        "RAIDS (les SURPRISES (les TACTIQUES (les EXPLICATIONS (les NATURELLES (les INSUFFISANTES (les FACTEURS — les "
        "DIVINS (les DÉCISIFS (les NOMBRES (les ABOLIS !)."
    ),
    schema=(
        "ZACHARIE EN 12 TEMPS : 7 ANS (les RESCAPÉS !) → RÉPARE (« MAISON… OUVRIERS » : les RESTAURÉS !) → 130 ANS (« "
        "MORT… SÉPULCRE ROIS » : les HONORÉS !) → PRINCES (« VINRENT… ÉCOUTA » : les FLATTÉS !) → ABANDON (« IDOLES » : "
        "les APOSTASIÉS !) → PROPHÈTES (« ENVOYÉS… PAS ÉCOUTÉ » : les IGNORÉS !) → REVÊTU (« ESPRIT… ZACHARIE » : les "
        "HABILLÉS !) → « POURQUOI… PAS PROSPÉREREZ… ABANDONNE » (les ACCUSÉS !) → CONSPIRÈRENT (« ORDRE ROI » : les "
        "COMPLOTÉS !) → LAPIDÉ (« COUR… MAISON » : les SACRILÈGES !) → « VOIE et REDEMANDE ! » (les INVOQUÉS !) → PETITE "
        "TROUPE (« GRANDES FORCES LIVRÉES » : les INVERSÉS !) → PRINCES (« SUPPRIMÉS… DAMAS » : les DÉCAPITÉS !) → "
        "MALADIES (« ASSASSINÉ LIT… PAS SÉPULCRE » : les EXCLUS !). Le fils du sauveur lapidé — la petite troupe livrée "
        "aux grandes forces."
    ),
    limites=(
        "BARACHIE vs JEHOÏADA (Mt 23:35 : les ZACHARIE (les FILS (les BARACHIE (les MATTHIEU (les FILS (les JEHOÏADA "
        "(les CHRONIQUES (les SOLUTIONS (les PÈRE/GRAND-PÈRE (les HOMONYMES (les FAUTES (les COPIES : 1200010556 : « "
        "Il est également ADMIS que JÉSUS PARLAIT ici de ZACHARIE, FILS de JÉHOÏADA » (OFFICIEL ! (les IDENTIFICATIONS "
        "— les OFFICIELLES (les DÉBATS (les TRANCHÉS !). Les 130 ANS (les LITTÉRAUX (les SYMBOLIQUES (les TEXTES (les "
        "AFFIRMENT (les SCEPTIQUES (les CHIFFRES (les RONDS (les FOIS — les SIMPLES (les GARDÉS (les CRITIQUES (les "
        "NOTÉES !). Les EFFECTIFS (les PETITES (les COMBIEN (les GRANDES (les COMBIEN (les TEXTES (les TAIRENT (les "
        "RATIOS (les INCONNUS (les INVERSIONS (les CERTAINES (les NOMBRES (les FLOUS !). Le LIEN 2R 12 (les MÊMES (les "
        "CAMPAGNES (les RANÇONS (les DÉSASTRES (les ORDRES (les CHRONOLOGIES (les HARMONIES (les PROPOSÉES (les "
        "COMPLÉMENTS (les SOURCES (les CROISÉES !). Les ASSASSINS (24:26 : les ZABAD + JEHOZABAD (les FILS (les "
        "AMMONITE + MOABITE (les MÈRES (les ÉTRANGÈRES (les MOTIFS (les VENGEANCES (les ZACHARIE (les PROBABLES (les "
        "TEXTES (les TAISENT (les JUSTICES — les POÉTIQUES (les SUPPOSÉES !)."
    ),
    accomplissement=[(("24:15-19", "130 ANS (ROIS !) + PRINCES + IDOLES + PROPHÈTES")),
        ((("24:20"), "REVÊTU (!) + « PAS PROSPÉREREZ » + « ABANDONNE »")),
        ((("24:21-22"), "LAPIDÉ (COUR !) + « REDEMANDE ! »")),
        ((("24:23"), "PETITE (GRANDES LIVRÉES !) + DAMAS")),
        ((("24:24-25"), "JUGEMENTS + MALADIES + LIT (PAS ROIS !)"))],
    tl=[((("24:16"), "130 ANS (ROIS !)")),
        ((("24:20"), "REVÊTU (ZACHARIE)")),
        ((("24:21"), "LAPIDÉ (COUR !)")),
        ((("24:22"), "« REDEMANDE ! »")),
        ((("24:23"), "PETITE (LIVRÉES !)"))],
    src=[("Barachie — Étude (Zacharie fils de Jehoïada, sang redemandé, petite troupe)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200010556"),
        ("Barakia — Étude (Zekaria, Abel, comptes demandés, 2Ch 24)", "https://wol.jw.org/fr/wol/d/r30/lp-f/1200000558"),
        ("2 Chroniques 24 — Bible d'étude (Zacharie, Joas, 24:20-25)", "https://wol.jw.org/fr/wol/b/r30/lp-f/nwtsty/14/24")],
    img="images/prophe_CH102_petite.jpg",
))
