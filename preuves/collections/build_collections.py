#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAGUE 6 — Collections audio thématiques.

Lit      : preuves/audio/*.mp3                 (les 108 pistes deja produites)
           preuves/collections/durations.json   (durees reelles, calculees trame par trame)
Ecrit    : preuves/COLLECTIONS_AUDIO.html       (12 fiches de collection)
           preuves/PLANS_ECOUTE.html            (parcours + fiches imprimables)
           preuves/audio/playlists/C01..C12.m3u (listes de lecture)

Regles de fabrication :
  - aucune date pour l'avenir ;
  - un seul systeme chronologique (607 / 537 / 455 / 29 / 33 / 36 / 66-70 / 1914) ;
  - liens exclusivement www.jw.org et wol.jw.org ;
  - aucune reproduction de contenu protege : on cite, on ne recopie pas ;
  - aucune image ni ressource distante dans les HTML (tout est inline).
"""

import os, json, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUD = os.path.join(ROOT, "audio")
OUT_PL = os.path.join(AUD, "playlists")
os.makedirs(OUT_PL, exist_ok=True)

DUR = json.load(open(os.path.join(ROOT, "collections", "durations.json")))

# Pistes enregistrees pendant cette vague (capsules d'ouverture).
CAPSULES = {f"collections_{i:02d}": None for i in range(1, 11)}

# ----------------------------------------------------------------------------
# LIENS OFFICIELS (seuls domaines autorises)
# ----------------------------------------------------------------------------
LIENS = [
    ("jw.org — accueil", "https://www.jw.org/fr/"),
    ("Bibliothèque en ligne (wol)", "https://wol.jw.org/fr/wol/h/r30/lp-f"),
    ("La Bible et l’Histoire", "https://www.jw.org/fr/la-bible-et-vous/histoire/"),
    ("La Bible et la science", "https://www.jw.org/fr/la-bible-et-vous/science/"),
    ("Questions bibliques", "https://www.jw.org/fr/la-bible-et-vous/questions-bibliques/"),
    ("Cours biblique particulier", "https://www.jw.org/fr/la-bible-et-vous/cours-biblique-particulier/"),
    ("Demandez une visite", "https://www.jw.org/fr/temoins-de-jehovah/demandez-une-visite/"),
    ("tv.jw.org", "https://www.tv.jw.org/"),
]

def lien(cle):
    for t, u in LIENS:
        if cle.lower() in t.lower():
            return (t, u)
    return (cle, "https://www.jw.org/fr/")

# ----------------------------------------------------------------------------
# TITRES LISIBLES DES PISTES
# ----------------------------------------------------------------------------
TITRE = {
 "registre_01_ouverture_genese": "Ouverture — la première promesse (Genèse)",
 "registre_02_abraham_400_ans": "Abraham et les 400 ans",
 "registre_03_jacob_esau_joseph": "Jacob, Ésaü, Joseph",
 "registre_04_jacob_douze_tribus": "Les douze tribus",
 "registre_05_exode": "L’Exode",
 "registre_06_levitique_nombres_deuteronome": "Lévitique, Nombres, Deutéronome",
 "registre_07_josue_samuel": "Josué à Samuel",
 "registre_08_rois_chroniques": "Rois et Chroniques",
 "registre_09_isaie_1_39": "Isaïe 1-39",
 "registre_10_isaie_40_66": "Isaïe 40-66",
 "registre_11_jeremie_1_25": "Jérémie 1-25",
 "registre_12_jeremie_26_38": "Jérémie 26-38",
 "registre_13_jeremie_nations": "Jérémie — les nations",
 "registre_14_jeremie_babylone": "Jérémie — Babylone",
 "registre_15_ezechiel_1_24": "Ézéchiel 1-24",
 "registre_16_ezechiel_tyr_egypte": "Ézéchiel — Tyr et l’Égypte",
 "registre_17_ezechiel_restauration": "Ézéchiel — la restauration",
 "registre_18_daniel_1_6": "Daniel 1-6",
 "registre_19_daniel_7_9": "Daniel 7-9",
 "registre_20_daniel_10_12": "Daniel 10-12",
 "registre_21_osee": "Osée",
 "registre_22_joel_amos": "Joël et Amos",
 "registre_23_abdias_jonas_michee": "Abdias, Jonas, Michée",
 "registre_24_nahum_habacuc_sophonie": "Nahum, Habaquq, Sophonie",
 "registre_25_haggee_zacharie1_8": "Aggée, Zacharie 1-8",
 "registre_26_zacharie9_14": "Zacharie 9-14",
 "registre_27_malachie_complements": "Malachie et compléments",
 "registre_28_psaumes_messianiques_1": "Psaumes messianiques (1)",
 "registre_29_psaumes_messianiques_2": "Psaumes messianiques (2)",
 "registre_30_cloture_vague3": "Clôture de la vague 3",
 "registre_31_messianiques_origine": "Le Messie — origine",
 "registre_32_messianiques_naissance": "Le Messie — naissance",
 "registre_33_messianiques_ministere": "Le Messie — ministère",
 "registre_34_messianiques_proces": "Le Messie — procès",
 "registre_35_messianiques_mort": "Le Messie — mort",
 "registre_36_messianiques_resurrection": "Le Messie — résurrection",
 "registre_37_signe_composite_1": "Le signe composite (1)",
 "registre_38_signe_composite_2": "Le signe composite (2)",
 "registre_39_jerusalem_70": "Jérusalem et 70 de n. è.",
 "registre_40_royaume_disciples": "Le Royaume et les disciples",
 "registre_41_partie10_actes_romains": "Actes et Romains",
 "registre_42_partie10_corinthiens_thessaloniciens": "Corinthiens et Thessaloniciens",
 "registre_43_partie10_timothee_hebreux": "Timothée, Tite, Hébreux",
 "registre_44_partie10_pierre_jean_jude_revelation1": "Pierre, Jean, Jude, Révélation 1",
 "registre_45_partie11_congregations_trone": "Les congrégations et le trône",
 "registre_46_partie11_sceaux_grande_foule": "Les sceaux et la grande foule",
 "registre_47_partie11_trompettes_deux_temoins": "Les trompettes et les deux témoins",
 "registre_48_partie12_betes_marque": "Les bêtes et la marque",
 "registre_49_partie12_moisson_bols_babylone": "Moisson, bols, chute de Babylone la Grande",
 "registre_50_partie12_chute_noces": "La chute et les noces",
 "registre_51_har_magedon_1": "Har-Maguédôn (1)",
 "registre_52_har_magedon_2_abime": "Har-Maguédôn (2) — l’abîme",
 "registre_53_jugement_nouveaux_cieux": "Le jugement et les nouveaux cieux",
 "registre_54_nouvelle_jerusalem": "La Nouvelle Jérusalem",
 "registre_55_fleuve_fin": "Le fleuve de vie — la fin du livre",
 "registre_56_fin_registre": "Fin du registre P001-P1000",
 "registre_57_recapitulatif_parties": "Récapitulatif des 14 parties",
 "registre_58_recapitulatif_corpus_regles": "Récapitulatif du corpus et des règles",
 "registre_59_grand_dossier_intro": "Introduction au grand dossier",
 "registre_60_preuve1_cyrus": "Preuve 1 — Cyrus nommé d’avance",
 "registre_61_preuves_2_3_babylone_tyr": "Preuves 2 et 3 — Babylone et Tyr",
 "registre_62_preuves_4_5_ninive_70ans": "Preuves 4 et 5 — Ninive et les 70 ans",
 "registre_63_preuves_6_7_semaines_daniel11": "Preuves 6 et 7 — les 70 semaines et Daniel 11",
 "registre_64_preuve8_sept_temps_1914": "Preuve 8 — les sept temps et 1914",
 "registre_65_preuves_9_10_signe_pella": "Preuves 9 et 10 — le signe et Pella",
 "registre_66_preuves_11_12_esaie53_avenir": "Preuves 11 et 12 — Isaïe 53 et l’avenir",
 "registre_67_huit_objections": "Les huit objections courantes",
 "registre_68_grand_dossier_cloture": "Clôture du grand dossier",
 "site_01_presentation": "Présentation du site local",
 "site_02_accueil_regles": "Accueil et règles du site",
 "site_03_registre_recherche": "Le registre et la recherche",
 "site_04_quatorze_parties": "Les quatorze parties",
 "site_05_douze_preuves": "Les douze preuves",
 "site_06_medias": "La page médias",
 "site_07_liens_officiels": "Les liens officiels",
 "site_08_regles_usage": "Les règles d’usage",
 "site_09_methode_presentation": "La méthode de présentation",
 "site_10_cloture": "Clôture de la visite du site",
 "livres_01_presentation_trois_livres": "Présentation des trois livres",
 "livres_02_enquete_sommaire": "Livre 1 — sommaire de l’enquête",
 "livres_03_enquete_mode_emploi": "Livre 1 — mode d’emploi",
 "livres_04_enquete_babylone_tyr": "Livre 1 — Babylone et Tyr",
 "livres_05_enquete_sennacherib_belshatsar": "Livre 1 — Sennachérib et Belshatsar",
 "livres_06_les_975_presentation": "Livre 2 — présentation",
 "livres_07_les_975_totaux_statuts": "Livre 2 — totaux et statuts",
 "livres_08_detail_presentation": "Livre 3 — présentation du détail",
 "livres_09_detail_belshatsar_trente_deux": "Livre 3 — Belshatsar, trente-deux entrées",
 "livres_10_cloture_impression": "Clôture et impression des livres",
 "visuels_01_presentation_vague4": "Présentation de la vague visuels",
 "visuels_02_frises_mode_emploi": "Les frises — mode d’emploi",
 "visuels_03_frise_1_ancetres": "Frise 1 — des ancêtres à la Loi",
 "visuels_04_frise_3_josias": "Frise 3 — de Josias à la désolation",
 "visuels_05_frise_8_daniel_raphia": "Frise 8 — Daniel et Raphia",
 "visuels_06_frise_12_1914_aujourdhui": "Frise 12 — de 1914 à aujourd’hui",
 "visuels_07_cartes_trois_volets": "Les cartes à trois volets",
 "visuels_08_coffret_etiquettes": "Le coffret et les étiquettes",
 "visuels_09_cartes_qr": "Les cartes QR",
 "visuels_10_complements_1000": "Compléments du millier d’entrées",
 "videos_01_presentation_vague5": "Présentation de la vague vidéos",
 "videos_02_fiche_technique": "La fiche technique 9:16",
 "videos_03_voix_off_v1_cyrus": "Voix off V1 — Cyrus",
 "videos_04_voix_off_v2_babylone": "Voix off V2 — Babylone 539",
 "videos_05_voix_off_v3_tyr": "Voix off V3 — Tyr 332",
 "videos_06_voix_off_v5_soixante_dix_ans": "Voix off V5 — les 70 ans",
 "videos_07_voix_off_v8_1914": "Voix off V8 — 607 à 1914",
 "videos_08_voix_off_v9_signe_et_v10": "Voix off V9 et V10 — le signe, Pella",
 "videos_09_liste_plans_generer": "La liste des 85 plans",
 "videos_10_cloture_vague5": "Clôture de la vague vidéos",
}

CAP_TITRE = {
 "collections_01": "Capsule 1 — Par où commencer",
 "collections_02": "Capsule 2 — Les douze preuves",
 "collections_03": "Capsule 3 — Les objections",
 "collections_04": "Capsule 4 — Babylone et Cyrus",
 "collections_05": "Capsule 5 — Tyr, l’Égypte, Ninive",
 "collections_06": "Capsule 6 — Les dates",
 "collections_07": "Capsule 7 — Le Messie",
 "collections_08": "Capsule 8 — Le signe des derniers jours",
 "collections_09": "Capsule 9 — Le livre de la Révélation",
 "collections_10": "Capsule 10 — Le monde nouveau",
 "collections_11": "Capsule 11 — Comment le texte est arrivé",
 "collections_12": "Capsule 12 — Présenter le dossier",
 "dates_01_607": "Fiche 1 — 607 : Jérusalem dévastée",
 "dates_02_539": "Fiche 2 — 539 : Babylone tombe",
 "dates_03_537": "Fiche 3 — 537 : le retour d’exil",
 "dates_04_455": "Fiche 4 — 455 : l’ordre de rebâtir",
 "dates_05_29": "Fiche 5 — 29 : le Messie paraît",
 "dates_06_33": "Fiche 6 — 33 : le Messie retranché",
 "dates_07_36": "Fiche 7 — 36 : la faveur s’ouvre aux nations",
 "dates_08_1914": "Fiche 8 — 1914 : la fin des sept temps",
 "cahier_01_mode_emploi": "Le cahier de l’auditeur — mode d’emploi",
 "cahier_02_corrige": "Corrigé des huit fiches à trous",
 "objection_01_apres_coup": "Carte 1 — « Écrites après coup »",
 "objection_02_poesie_vague": "Carte 2 — « Trop de prophéties ressemblent à de la poésie »",
 "objection_03_texte_instrumentalise": "Carte 3 — « On fait dire au texte »",
 "objection_04_dates_inverifiables": "Carte 4 — « Les dates sont invérifiables »",
 "objection_05_1914_apres_coup": "Carte 5 — « 1914 fixé après coup »",
 "objection_06_revelation_interpretation": "Carte 6 — « Vous interprétez la Révélation »",
 "objection_07_et_si_vous_vous_trompez": "Carte 7 — « Et si vous vous trompez ? »",
 "objection_08_images_fausses": "Carte 8 — « Ces images sont fausses »",
}

POCHETTES = {
 1:"images/collection_01_porte_entree.jpg",   2:"images/collection_02_douze_preuves.jpg",
 3:"images/collection_03_objections.jpg",     4:"images/collection_04_babylone_cyrus.jpg",
 5:"images/collection_05_tyr_egypte_ninive.jpg", 6:"images/collection_06_les_dates.jpg",
 7:"images/collection_07_le_messie.jpg",      8:"images/collection_08_le_signe.jpg",
 9:"images/collection_09_revelation.jpg",     10:"images/collection_10_monde_nouveau.jpg",
}

def d(nom):
    if nom in DUR:
        return DUR[nom]
    if nom.startswith("collections_"):
        return DUR.get(nom, 0.0)
    return 0.0

def titre(nom):
    if nom in TITRE:
        return TITRE[nom]
    if nom in CAP_TITRE:
        return CAP_TITRE[nom]
    return nom.replace("_", " ")

def mmss(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"

def hmm(s):
    s = int(round(s))
    if s >= 3600:
        return f"{s // 3600} h {s % 3600 // 60:02d}"
    return f"{s // 60} min {s % 60:02d} s"

# ----------------------------------------------------------------------------
# LES 12 COLLECTIONS
# ----------------------------------------------------------------------------
C = []

C.append(dict(
 n=1, titre="Par où commencer",
 sous="Ouvrir le dossier sans rien connaître d’avance",
 objet="Donner en moins de deux minutes l’ordre de lecture et la règle du jeu : on ne débat pas d’une religion, on examine des faits datés.",
 usage="À écouter seul, avant toute autre collection. C’est la porte d’entrée.",
 support="SITE_LOCAL.html — onglet Accueil",
 p=["collections_01","site_01_presentation","site_02_accueil_regles",
    "registre_01_ouverture_genese","registre_59_grand_dossier_intro",
    "livres_01_presentation_trois_livres"],
 cle="La Bible ne s’ouvre pas par une preuve, mais par une promesse.",
 lien=("jw.org — accueil","Cours biblique")))

C.append(dict(
 n=2, titre="Les douze preuves",
 sous="Le grand dossier, d’un bout à l’autre",
 objet="Suivre les douze grandes preuves dans l’ordre : chacune tient en une date, un lieu, un document.",
 usage="Le cœur du dossier. Une preuve par écoute, jamais deux le même soir.",
 support="22_GRAND_DOSSIER.md",
 p=["collections_02","registre_59_grand_dossier_intro","registre_60_preuve1_cyrus",
    "registre_61_preuves_2_3_babylone_tyr","registre_62_preuves_4_5_ninive_70ans",
    "registre_63_preuves_6_7_semaines_daniel11","registre_64_preuve8_sept_temps_1914",
    "registre_65_preuves_9_10_signe_pella","registre_66_preuves_11_12_esaie53_avenir"],
 cle="Une prophétie datée ne se discute pas : elle s’est produite, ou non.",
 lien=("La Bible et l’Histoire","Bibliothèque en ligne (wol)")))

C.append(dict(
 n=3, titre="Les huit objections",
 sous="Répondre sans s’énerver, sans débattre",
 objet="Reprendre les huit objections les plus courantes et la réponse que l’on peut donner, en privé, avec un document.",
 usage="À écouter avant une conversation difficile. On ne convainc pas : on montre.",
 support="22_GRAND_DOSSIER.md — annexe",
 p=["collections_03","registre_67_huit_objections",
    "registre_58_recapitulatif_corpus_regles","site_08_regles_usage",
    "livres_03_enquete_mode_emploi","visuels_09_cartes_qr"],
 cle="Une objection bien comprise est déjà à moitié une question.",
 lien=("Questions bibliques","Cours biblique")))

C.append(dict(
 n=4, titre="Babylone et Cyrus",
 sous="Une ville, un fleuve, un nom — cent cinquante ans d’avance",
 objet="Isaïe nomme Cyrus plus d’un siècle avant sa naissance ; Jérémie annonce le dessèchement du fleuve et les portes ouvertes.",
 usage="La collection la plus solide pour une première démonstration.",
 support="LIVRE_1_ENQUETE.html — chapitre Babylone",
 p=["collections_04","registre_60_preuve1_cyrus",
    "videos_03_voix_off_v1_cyrus","livres_04_enquete_babylone_tyr",
    "registre_61_preuves_2_3_babylone_tyr","videos_04_voix_off_v2_babylone",
    "registre_14_jeremie_babylone"],
 cle="Le nom de Cyrus est écrit avant qu’il existe ; le gué de l’Euphrate est annoncé avant d’être franchi.",
 lien=("La Bible et l’Histoire","Bibliothèque en ligne (wol)")))

C.append(dict(
 n=5, titre="Tyr, l’Égypte et les nations",
 sous="Quand la prophétie décrit la méthode avant l’événement",
 objet="Ézéchiel annonce que les pierres de Tyr seront jetées dans la mer et qu’Alexandre raclera sa poussière. Édom disparaît ; Ninive est oubliée.",
 usage="Pour qui objecte que les prophéties sont vagues. Ici le détail est matériel.",
 support="videos/SCRIPTS_VIDEOS.html — V3 Tyr",
 p=["collections_05","registre_16_ezechiel_tyr_egypte","videos_05_voix_off_v3_tyr",
    "registre_13_jeremie_nations","registre_23_abdias_jonas_michee",
    "registre_24_nahum_habacuc_sophonie","registre_62_preuves_4_5_ninive_70ans"],
 cle="On ne raclait pas la poussière d’une ville : on construisait dessus. Tyr a été raclée.",
 lien=("La Bible et l’Histoire","Bibliothèque en ligne (wol)")))

C.append(dict(
 n=6, titre="Les dates",
 sous="607 · 537 · 455 · 29 · 36 · 1914",
 objet="Tenir la chaîne des dates sans la casser : la désolation, le retour, l’ordre de rebâtir, le Messie, la fin de la faveur spéciale, les sept temps.",
 usage="Collection technique. À écouter avec les frises sous les yeux.",
 support="visuels/FRISES_CHRONOLOGIQUES.html",
 p=["collections_06","registre_62_preuves_4_5_ninive_70ans",
    "registre_63_preuves_6_7_semaines_daniel11","registre_64_preuve8_sept_temps_1914",
    "videos_06_voix_off_v5_soixante_dix_ans","videos_07_voix_off_v8_1914",
    "visuels_05_frise_8_daniel_raphia","visuels_06_frise_12_1914_aujourdhui"],
 cle="Un système chronologique par document : jamais deux dans le même.",
 lien=("Bibliothèque en ligne (wol)","La Bible et l’Histoire")))

C.append(dict(
 n=7, titre="Le Messie",
 sous="L’origine, la naissance, le ministère, la mort",
 objet="Reprendre les prophéties messianiques une par une et leur accomplissement dans les Évangiles — en laissant les questions dogmatiques de côté.",
 usage="Collection longue : six écoutes. Ne pas chercher de total : la Bibliothèque en ligne déconseille de se montrer trop affirmatif sur le nombre.",
 support="LIVRE_3_DETAIL.html — parties 7 et 8",
 p=["collections_07","registre_31_messianiques_origine",
    "registre_32_messianiques_naissance","registre_33_messianiques_ministere",
    "registre_34_messianiques_proces","registre_35_messianiques_mort",
    "registre_36_messianiques_resurrection","registre_28_psaumes_messianiques_1",
    "registre_09_isaie_1_39"],
 cle="On ne compte pas les prophéties : on les vérifie.",
 lien=("Questions bibliques","Cours biblique")))

C.append(dict(
 n=8, titre="Le signe des derniers jours",
 sous="Guerres, famines, pestes, et le signe composé",
 objet="Le signe donné par Jésus, ses éléments, et la manière de le présenter sans jamais annoncer de date.",
 usage="À écouter avant d’aborder l’actualité. Aucune date, jamais.",
 support="SITE_LOCAL.html — onglet Signe",
 p=["collections_08","registre_37_signe_composite_1",
    "registre_38_signe_composite_2","registre_39_jerusalem_70",
    "registre_40_royaume_disciples","videos_08_voix_off_v9_signe_et_v10",
    "registre_51_har_magedon_1","registre_52_har_magedon_2_abime"],
 cle="Le signe se constate ; la date ne se calcule pas.",
 lien=("jw.org — accueil","Questions bibliques")))

C.append(dict(
 n=9, titre="Le livre de la Révélation",
 sous="Les sceaux, les trompettes, les bêtes, la grande foule",
 objet="Traverser la Révélation dans l’ordre du livre, sans allégorie inventée et sans identification hasardeuse.",
 usage="Sept écoutes. Seule collection qui suit un livre entier, chapitre après chapitre.",
 support="LIVRE_3_DETAIL.html — parties 11 et 12",
 p=["collections_09","registre_44_partie10_pierre_jean_jude_revelation1",
    "registre_45_partie11_congregations_trone","registre_46_partie11_sceaux_grande_foule",
    "registre_47_partie11_trompettes_deux_temoins","registre_48_partie12_betes_marque",
    "registre_49_partie12_moisson_bols_babylone","registre_50_partie12_chute_noces"],
 cle="Le livre se lit dans l’ordre ; il ne se découpe pas en morceaux choisis.",
 lien=("Bibliothèque en ligne (wol)","jw.org — accueil")))

C.append(dict(
 n=10, titre="Le monde nouveau",
 sous="Nouveaux cieux, nouvelle terre, la ville, le fleuve",
 objet="Finir par où la Bible finit : la restauration annoncée, la Nouvelle Jérusalem, le fleuve de vie.",
 usage="La collection à proposer quand la conversation fatigue. Elle repose.",
 support="videos/SCRIPTS_VIDEOS.html — L1",
 p=["collections_10","registre_53_jugement_nouveaux_cieux",
    "registre_54_nouvelle_jerusalem","registre_55_fleuve_fin",
    "registre_17_ezechiel_restauration","registre_10_isaie_40_66",
    "registre_27_malachie_complements"],
 cle="La Bible ne s’arrête pas sur une catastrophe : elle s’arrête sur une eau vive.",
 lien=("jw.org — accueil","Cours biblique")))

C.append(dict(
 n=11, titre="Comment le texte est arrivé jusqu’à nous",
 sous="Les copistes, les manuscrits, les rouleaux",
 objet="Répondre à l’objection la plus fréquente : « le texte a été recopié mille fois, donc il a changé. » Les rouleaux de la mer Morte permettent la comparaison sur plus de mille ans.",
 usage="Collection courte. À proposer à qui vient des sciences ou de l’histoire.",
 support="preuves/23_REGISTRE_PROPHETIES_7.md",
 p=["livres_05_enquete_sennacherib_belshatsar","livres_09_detail_belshatsar_trente_deux",
    "registre_18_daniel_1_6","registre_19_daniel_7_9",
    "site_03_registre_recherche","visuels_03_frise_1_ancetres"],
 p_caps=["collections_11"],
 cle="Les copistes comptaient les lettres. Le rouleau le plus ancien de Daniel précède de plus d’un millénaire les copies médiévales, et le texte concorde.",
 lien=("Bibliothèque en ligne (wol)","La Bible et l’Histoire")))

C.append(dict(
 n=12, titre="Présenter le dossier à quelqu’un",
 sous="La méthode, les supports, les liens",
 objet="Comment transmettre un fichier à la fois, en privé, sans jamais publier ni héberger quoi que ce soit.",
 usage="Dernière collection. À réécouter avant chaque remise de document.",
 support="visuels/COFFRET.html",
 p=["site_09_methode_presentation","site_07_liens_officiels","site_06_medias",
    "site_10_cloture","livres_10_cloture_impression",
    "visuels_08_coffret_etiquettes","visuels_07_cartes_trois_volets"],
 p_caps=["collections_12"],
 cle="Un fichier à la fois, une personne à la fois, et un lien officiel.",
 lien=("Demandez une visite","Cours biblique")))

C.append(dict(
 n=13, titre="Les huit dates",
 sous="Une fiche, une date, un calcul écrit ligne par ligne",
 objet="Tenir la chaîne 607 · 539 · 537 · 455 · 29 · 33 · 36 · 1914 sans jamais la rompre, avec le détail de chaque opération et la limite de chaque fiche.",
 usage="Collection de référence. À écouter avec le carnet de fiches ouvert devant soi.",
 support="FICHES_DATES.html",
 p=["dates_01_607","dates_02_539","dates_03_537","dates_04_455",
    "dates_05_29","dates_06_33","dates_07_36","dates_08_1914"],
 capdef=True,
 cle="Huit dates vérifiées valent mieux qu’un chiffre qu’on oppose à quelqu’un.",
 lien=("Bibliothèque en ligne (wol)","La Bible et l’Histoire")))

C.append(dict(
 n=14, titre="Les objections en poche",
 sous="Huit cartes, huit réponses, huit liens",
 objet="Répondre aux huit objections les plus courantes en trois lignes, avec le lien officiel écrit en clair au dos de chaque carte.",
 usage="Collection de poche. Quatre cartes sur soi, jamais huit : une carte jamais sortie ne sert à rien.",
 support="CAHIER_AUDITEUR.html — partie C",
 p=["objection_01_apres_coup","objection_02_poesie_vague",
    "objection_03_texte_instrumentalise","objection_04_dates_inverifiables",
    "objection_05_1914_apres_coup","objection_06_revelation_interpretation",
    "objection_07_et_si_vous_vous_trompez","objection_08_images_fausses"],
 capdef=True,
 cle="On ne convainc pas : on montre, et on laisse la source ouverte.",
 lien=("Questions bibliques","Bibliothèque en ligne (wol)")))

C.append(dict(
 n=15, titre="Le cahier de l’auditeur",
 sous="Remplir, vérifier, corriger — la boucle complète",
 objet="Suivre le cahier dans l’ordre : le mode d’emploi, les huit fiches de dates à compléter, puis le corrigé. C’est la seule collection qui se pratique un stylo à la main.",
 usage="À faire seul, sur une semaine. Une fiche par jour, corrigée le lendemain.",
 support="CAHIER_AUDITEUR.html",
 p=["cahier_01_mode_emploi","dates_01_607","dates_02_539","dates_03_537",
    "dates_04_455","dates_05_29","dates_06_33","dates_07_36","dates_08_1914",
    "cahier_02_corrige"],
 capdef=True,
 cle="On ne retient que ce qu’on a écrit soi-même.",
 lien=("Bibliothèque en ligne (wol)","jw.org — accueil")))

# ----------------------------------------------------------------------------
# CALCULS
# ----------------------------------------------------------------------------
for c in C:
    c.setdefault("p_caps", [])
    c["duree"] = sum(d(p) for p in c["p_caps"] + c["p"])
    c["np"] = len(c["p_caps"]) + len(c["p"])

TOTAL_C = sum(c["duree"] for c in C)
TOTAL_PISTES = sum(c["np"] for c in C)
N_INCONNUES = sorted({p for c in C for p in c["p_caps"] + c["p"] if p not in DUR})

# ----------------------------------------------------------------------------
# STYLE COMMUN
# ----------------------------------------------------------------------------
CSS = """
:root{--bleu:#0B2545;--or:#E9C46A;--creme:#F7F4EC;--gris:#5b6472;}
*{box-sizing:border-box;}
body{margin:0;background:var(--creme);color:#1b2430;
 font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.5;}
.wrap{max-width:960px;margin:0 auto;padding:0 22px 70px;}
header{background:var(--bleu);color:#fff;padding:34px 22px 28px;}
header .in{max-width:960px;margin:0 auto;}
header h1{margin:0 0 6px;font-size:27px;letter-spacing:.3px;}
header p{margin:0;color:#c9d3e4;font-size:14px;}
.kicker{color:var(--or);text-transform:uppercase;letter-spacing:2.4px;
 font-size:11px;font-weight:700;margin-bottom:10px;}
h2{color:var(--bleu);font-size:20px;margin:42px 0 12px;
 padding-bottom:7px;border-bottom:2px solid var(--or);}
h3{color:var(--bleu);font-size:16px;margin:22px 0 8px;}
p{margin:0 0 10px;}
table{border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:13.5px;background:#fff;}
th,td{border:1px solid #d8d2c4;padding:6px 9px;text-align:left;vertical-align:top;}
th{background:var(--bleu);color:#fff;font-weight:600;font-size:12.5px;
 text-transform:uppercase;letter-spacing:.4px;}
td.c,th.c{text-align:center;}
tr:nth-child(even) td{background:#fbf9f4;}
.coll{background:#fff;border:1px solid #dcd6c6;border-left:7px solid var(--bleu);
 border-radius:5px;padding:0;margin:0 0 26px;overflow:hidden;}
.coll .hd{background:var(--bleu);color:#fff;padding:14px 18px 12px;}
.coll .hd .num{color:var(--or);font-weight:800;font-size:12px;letter-spacing:2px;}
.coll .hd h3{margin:2px 0 3px;color:#fff;font-size:20px;}
.coll .hd .sous{color:#c9d3e4;font-size:13px;}
.coll .bd{padding:16px 18px 6px;}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px;}
.badge{background:#eef1f6;border:1px solid #d3dae6;border-radius:20px;
 padding:3px 11px;font-size:11.5px;color:var(--bleu);font-weight:600;}
.badge.or{background:#fdf6e3;border-color:var(--or);color:#7a5b12;}
.objet{background:#f4f7fb;border-left:4px solid var(--or);padding:10px 13px;
 font-size:13.5px;margin:0 0 12px;}
.piste{display:flex;gap:10px;align-items:baseline;padding:5px 0;
 border-bottom:1px dotted #d8d2c4;font-size:13.5px;}
.piste:last-child{border-bottom:none;}
.piste .n{color:var(--or);font-weight:800;min-width:22px;}
.piste .t{flex:1;}
.piste .f{color:var(--gris);font-size:11.5px;font-family:Consolas,monospace;}
.piste .d{color:var(--bleu);font-weight:700;font-variant-numeric:tabular-nums;}
.cle{background:#0B2545;color:#fff;border-radius:4px;padding:9px 13px;
 font-size:13px;margin:10px 0 4px;}
.cle b{color:var(--or);}
.liens{font-size:12.5px;color:var(--gris);padding:0 18px 14px;}
.liens a{color:#1a4a8a;}
.note{background:#fff8e8;border:1px solid var(--or);border-radius:4px;
 padding:11px 14px;font-size:13px;margin:14px 0;}
ul{padding-left:20px;margin:0 0 12px;}
li{margin-bottom:5px;font-size:13.5px;}
footer{background:var(--bleu);color:#cfd8e6;padding:20px 22px;font-size:12px;}
footer .in{max-width:960px;margin:0 auto;}
footer a{color:var(--or);}
.pb{page-break-after:always;}
.grille{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.carte{border:2px solid var(--bleu);border-radius:8px;padding:14px;background:#fff;}
.carte.pleine{grid-column:1 / -1;}
.carte h4{margin:0 0 6px;color:var(--bleu);font-size:15px;}
.carte .q{font-size:12.5px;color:var(--gris);margin-top:8px;}
.ligne{border-bottom:1px solid #cfd8e6;height:22px;margin:5px 0;}
.case{display:inline-block;width:13px;height:13px;border:1.5px solid var(--bleu);
 margin-right:7px;vertical-align:-2px;}
@media print{
 body{background:#fff;}
 header,footer{background:#0B2545 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
 .coll,.carte{break-inside:avoid;}
}
"""

def head(titre_, sous):
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titre_)}</title>
<style>{CSS}</style></head><body>
<header><div class="in">
<div class="kicker">Bibliothèque privée — projet PREUVES</div>
<h1>{html.escape(titre_)}</h1>
<p>{html.escape(sous)}</p>
</div></header>
<div class="wrap">
"""

FOOT = f"""</div><footer><div class="in">
<b>Bibliothèque privée locale.</b> Aucun contenu protégé n’est reproduit : les références sont citées.
Aucune publication, aucun extrait, aucune image de l’organisation n’est hébergé ici.
Les liens renvoient exclusivement vers <a href="https://www.jw.org/fr/">www.jw.org</a>
et <a href="https://wol.jw.org/fr/wol/h/r30/lp-f">wol.jw.org</a>.
Transmission uniquement de personne à personne, fichier par fichier.
<br>Généré le {datetime.date.today().isoformat()} — vague 6.
</div></footer></body></html>
"""

def bloc_liens(c):
    a, b = c["lien"]
    ta, ua = lien(a)
    tb, ub = lien(b)
    return (f'<div class="liens">Liens officiels pour cette collection : '
            f'<a href="{ua}">{html.escape(ta)}</a> · '
            f'<a href="{ub}">{html.escape(tb)}</a></div>')

# ----------------------------------------------------------------------------
# FICHIER 1 — COLLECTIONS_AUDIO.html
# ----------------------------------------------------------------------------
H = [head("COLLECTIONS AUDIO THÉMATIQUES",
          f"{len(C)} collections · {TOTAL_PISTES} écoutes · {hmm(TOTAL_C)} au total — "
          f"construites à partir des {len(DUR)} pistes déjà enregistrées")]

H.append(f"""<div class="note">
<b>Comment utiliser ce classeur sonore.</b> Chaque collection est un <b>ordre d’écoute</b>, pas un
résumé : on écoute dans l’ordre indiqué, un fichier à la fois, avec le support indiqué ouvert
devant soi. Les durées sont réelles, calculées piste par piste. Les capsules d’ouverture
(« collections_01 » à « collections_10 ») servent à annoncer le sujet en moins de vingt secondes
avant de lancer la série.
</div>""")

H.append("<h2>Vue d’ensemble</h2>")
H.append("<table><thead><tr><th class='c'>N°</th><th>Collection</th><th>Objet</th>"
         "<th class='c'>Pistes</th><th class='c'>Durée</th><th>Support à ouvrir</th></tr></thead><tbody>")
for c in C:
    H.append(f"<tr><td class='c'><b>C{c['n']:02d}</b></td>"
             f"<td><b>{html.escape(c['titre'])}</b><br><span style='color:#5b6472;font-size:12px'>"
             f"{html.escape(c['sous'])}</span></td>"
             f"<td style='font-size:12.5px'>{html.escape(c['objet'])}</td>"
             f"<td class='c'>{c['np']}</td><td class='c'><b>{mmss(c['duree'])}</b></td>"
             f"<td style='font-size:12px;font-family:Consolas,monospace'>{html.escape(c['support'])}</td>"
             f"<td class='c' style='font-size:11.5px'>{'C{:02d}'.format(c['n']) if c['n'] in POCHETTES else '—'}</td></tr>")
H.append(f"<tr style='background:#0B2545;color:#fff'><td></td><td><b>TOTAL</b></td><td></td>"
         f"<td class='c'><b>{TOTAL_PISTES}</b></td><td class='c'><b>{hmm(TOTAL_C)}</b></td><td></td></tr>")
H.append("</tbody></table>")

H.append("""<div class="note"><b>Trois règles d’usage, valables pour les douze collections.</b>
<ol style="margin:6px 0 0">
<li><b>Un système chronologique par document.</b> 607 av. n. è. pour la désolation de Jérusalem,
539 pour la chute de Babylone, 537 pour le retour, 455 pour l’ordre de rebâtir, 29 de n. è. pour
l’onction du Messie, 33 pour sa mort, 36 pour la fin de la faveur spéciale accordée aux Juifs,
1914 pour la fin des sept temps. On ne mélange jamais deux systèmes dans un même document.</li>
<li><b>Aucune date pour l’avenir.</b> Ce qui n’est pas accompli reste sans date.</li>
<li><b>Aucun total dogmatique.</b> La Bibliothèque en ligne elle-même écrit qu’il est préférable de
ne pas se montrer trop affirmatif quant au nombre exact des prophéties messianiques. Ce dossier est
un inventaire de travail, pas un chiffre à opposer à quelqu’un.</li>
</ol></div>""")

for i, c in enumerate(C):
    if i and i % 3 == 0:
        H.append('<div class="pb"></div>')
    H.append('<div class="coll"><div class="hd">')
    H.append(f"<div class='num'>COLLECTION C{c['n']:02d}</div>")
    H.append(f"<h3>{html.escape(c['titre'])}</h3>")
    H.append(f"<div class='sous'>{html.escape(c['sous'])}</div></div><div class='bd'>")
    caps = c["p_caps"] + [p for p in c["p"] if p.startswith("collections_")]
    corps = [p for p in c["p"] if not p.startswith("collections_")]
    H.append("<div class='meta'>")
    H.append(f"<span class='badge or'>{c['np']} pistes</span>")
    H.append(f"<span class='badge'>{hmm(c['duree'])}</span>")
    H.append(f"<span class='badge'>{html.escape(c['usage'])}</span>")
    if caps:
        H.append(f"<span class='badge or'>{len(caps)} capsule d’ouverture</span>")
    else:
        H.append("<span class='badge'>capsule d’ouverture : vague suivante</span>")
    H.append("</div>")
    H.append(f"<div class='objet'><b>Objectif.</b> {html.escape(c['objet'])}</div>")
    H.append("<table><thead><tr><th class='c' style='width:30px'>#</th><th>Écoute</th>"
             "<th style='width:31%'>Fichier (dossier audio/)</th><th class='c' style='width:52px'>Durée</th>"
             "</tr></thead><tbody>")
    k = 0
    for p in caps + corps:
        k += 1
        cls = " style='background:#fdf6e3'" if p.startswith("collections_") else ""
        H.append(f"<tr{cls}><td class='c'><b>{k}</b></td><td>{html.escape(titre(p))}</td>"
                 f"<td class='f' style='font-family:Consolas,monospace;font-size:11px'>{p}.mp3</td>"
                 f"<td class='c'>{mmss(d(p))}</td></tr>")
    H.append(f"<tr style='background:#eef1f6'><td></td><td><b>Total</b></td><td></td>"
             f"<td class='c'><b>{hmm(c['duree'])}</b></td></tr>")
    H.append("</tbody></table>")
    H.append(f"<div class='cle'><b>À retenir.</b> {html.escape(c['cle'])}</div>")
    H.append(f"<p style='font-size:12.5px;color:#5b6472'><b>Support à ouvrir en même temps :</b> "
             f"<span style='font-family:Consolas,monospace'>{html.escape(c['support'])}</span></p>")
    if c["n"] in POCHETTES:
        H.append(f"<p style='font-size:12.5px;color:#5b6472'><b>Pochette de la collection :</b> "
                 f"<span style='font-family:Consolas,monospace'>{POCHETTES[c['n']]}</span>"
                 f"<br><i>Illustration. Aucune de ces images n’est un document : ni photo d’un site "
                 f"réel, ni reproduction d’un artefact. Elles servent uniquement à identifier "
                 f"visuellement une série.</i></p>")
    H.append("</div>")
    H.append(bloc_liens(c))
    H.append("</div>")

H.append("<h2>Annexe — index complet des pistes par durée décroissante</h2>")
H.append("<table><thead><tr><th class='c'>#</th><th>Piste</th>"
         "<th class='c'>Durée</th><th class='c'>#</th><th>Piste</th><th class='c'>Durée</th>"
         "</tr></thead><tbody>")
items = sorted(DUR.items(), key=lambda kv: -kv[1])
half = (len(items) + 1) // 2
for i in range(half):
    cells = ""
    for j in (i, i + half):
        if j < len(items):
            k, v = items[j]
            cells += (f"<td>{html.escape(titre(k))}</td><td class='c'>{mmss(v)}</td>")
        else:
            cells += "<td></td><td></td>"
    H.append(f"<tr><td class='c'>{i+1}</td>{cells}</tr>")
H.append("</tbody></table>")
H.append(f"<p style='font-size:12.5px;color:#5b6472'>"
         f"{len(DUR)} pistes · {hmm(sum(DUR.values()))} d’écoute cumulée.</p>")

H.append("</div><footer><div class='in'><b>Bibliothèque privée locale.</b> "
         "Aucun contenu protégé n’est reproduit : les références sont citées. "
         "Aucune publication, aucun extrait, aucune image de l’organisation n’est hébergé ici. "
         "Les liens renvoient exclusivement vers "
         "<a href='https://www.jw.org/fr/'>www.jw.org</a> et "
         "<a href='https://wol.jw.org/fr/wol/h/r30/lp-f'>wol.jw.org</a>. "
         "Transmission uniquement de personne à personne, fichier par fichier."
         f"<br>Généré le {datetime.date.today().isoformat()} — vague 6.</div></footer></body></html>")

open(os.path.join(ROOT, "COLLECTIONS_AUDIO.html"), "w", encoding="utf-8").write("\n".join(H))

# ----------------------------------------------------------------------------
# FICHIER 2 — PLANS_ECOUTE.html (parcours + fiches imprimables)
# ----------------------------------------------------------------------------
P = [head("PLANS D’ÉCOUTE ET FICHES IMPRIMABLES",
          "Quatre parcours, une fiche d’écoute par collection, une carte de prêt — à imprimer en A4")]

P.append("<h2>1 · Quatre parcours</h2>")
P.append("<p>Un parcours est un engagement de durée. On choisit le parcours <i>avant</i> de commencer, "
         "et on s’y tient : c’est la régularité, pas la quantité, qui fait qu’un dossier devient familier.</p>")

SEM_C = [("C01",""),("C04",""),("C05",""),("C02",""),("C07",""),("C06",""),
         ("C03",""),("C11",""),("C12",""),("C15",""),("C13",""),("C14",""),
         ("C08",""),("C10","")]
TOUTES = [(f"C{c['n']:02d}", "") for c in C]

PARCOURS = [
 ("Parcours A — Une soirée",
  "Une seule séance, en deux temps avec une pause. Pour quelqu’un qui veut voir l’ensemble avant de décider s’il continue.",
  [("C01",""), ("C02",""), ("C06","")], 1,
  "À réserver à une personne déjà curieuse. Ne pas dépasser trois collections dans une soirée : au-delà, rien ne reste."),
 ("Parcours B — Deux semaines",
  "Une collection par jour ouvré, week-end libre. Le parcours le plus utilisé : il laisse le temps de relire le support entre deux écoutes. Le cahier (C15) arrive avant les dates (C13) et les cartes (C14) : on apprend la méthode avant les réponses.",
  SEM_C, 1,
  "Ordre pensé pour que les preuves datées précèdent toujours les questions d’interprétation."),
 ("Parcours C — Quatre semaines",
  "Trois collections par semaine pendant trois semaines, puis une semaine entière de revision sans rien découvrir de nouveau.",
  TOUTES, 1,
  "Pour qui veut lire les supports en même temps. Prévoir le dossier imprimé à côté du lecteur."),
 ("Parcours D — Douze semaines",
  "Une collection par semaine, écoutée deux fois : une fois pour comprendre, une fois pour retenir.",
  TOUTES, 2,
  "Le parcours le plus efficace sur la mémoire à long terme : la première réécoute doit intervenir dans les 24 heures, avant que la courbe de l’oubli ne vide la moitié de ce qui a été entendu."),
]

def cols_of(lst):
    codes = [x[0] for x in lst]
    return [c for c in C if f"C{c['n']:02d}" in codes]

for nom, desc, cols, fois, conseil in PARCOURS:
    sel = cols_of(cols)
    duree = sum(c["duree"] for c in sel) * fois
    P.append(f"<h3>{html.escape(nom)} — {mmss(duree)}"
             + (" (deux passages)" if fois == 2 else "") + "</h3>")
    P.append(f"<p>{html.escape(desc)}</p>")
    P.append("<table><thead><tr><th class='c' style='width:34px'>N°</th><th>Collection</th>"
             "<th class='c' style='width:50px'>Pistes</th><th class='c' style='width:60px'>Durée</th>"
             "<th>Support</th></tr></thead><tbody>")
    for cc in sel:
        P.append(f"<tr><td class='c'><b>C{cc['n']:02d}</b></td><td>{html.escape(cc['titre'])}</td>"
                 f"<td class='c'>{cc['np']}</td><td class='c'>{mmss(cc['duree'])}</td>"
                 f"<td style='font-size:12px;font-family:Consolas,monospace'>{html.escape(cc['support'])}</td></tr>")
    P.append(f"<tr style='background:#eef1f6'><td></td><td><b>Total"
             + (" — deux passages" if fois == 2 else "") + "</b></td>"
             f"<td class='c'><b>{sum(x['np'] for x in sel)}</b></td>"
             f"<td class='c'><b>{hmm(duree)}</b></td><td></td></tr>")
    P.append("</tbody></table>")
    P.append(f"<p style='font-size:12.5px;color:#5b6472'><b>Conseil.</b> {html.escape(conseil)}</p>")

P.append('<div class="pb"></div>')
P.append("<h2>2 · Fiche d’écoute (une par collection — à imprimer)</h2>")
P.append("<p>Une demi-page par collection : on coche au fur et à mesure, on note une seule phrase "
         "à la fin. Ce qui n’est pas écrit est oublié dans les 24 heures.</p>")
P.append('<div class="grille">')
for c in C:
    P.append('<div class="carte">')
    P.append(f"<h4>C{c['n']:02d} — {html.escape(c['titre'])}</h4>")
    P.append(f"<div style='font-size:12px;color:#5b6472'>{c['np']} pistes · {hmm(c['duree'])} · "
             f"{html.escape(c['support'])}</div>")
    for k, p in enumerate(c["p"], 1):
        P.append(f"<div style='font-size:12px;margin-top:3px'><span class='case'></span>"
                 f"<b>{k}.</b> {html.escape(titre(p))} <span style='color:#8b93a1'>({mmss(d(p))})</span></div>")
    P.append(f"<div class='q'><b>Ce que je retiens :</b><div class='ligne'></div>"
             f"<div class='ligne'></div></div>")
    P.append(f"<div class='q'><b>Question à poser :</b><div class='ligne'></div></div>")
    P.append("</div>")
P.append("</div>")

P.append('<div class="pb"></div>')
P.append("<h2>3 · Carte de prêt (à découper, 4 par page A4)</h2>")
P.append("<p>On remet un fichier, pas un classeur. La carte accompagne le fichier et rappelle "
         "l’ordre de lecture, la durée, et le lien officiel vers lequel revenir.</p>")
P.append('<div class="grille">')
for c in C[:4]:
    P.append('<div class="carte">')
    P.append(f"<h4>C{c['n']:02d} — {html.escape(c['titre'])}</h4>")
    P.append(f"<div style='font-size:12.5px'>{html.escape(c['sous'])}</div>")
    P.append(f"<div style='font-size:12px;color:#5b6472;margin-top:6px'>"
             f"{c['np']} pistes · <b>{hmm(c['duree'])}</b></div>")
    P.append("<div style='font-size:11.5px;margin-top:6px'>")
    for k, p in enumerate(c["p"], 1):
        P.append(f"{k}. {html.escape(titre(p))}<br>")
    P.append("</div>")
    a, b = c["lien"]
    ta, ua = lien(a); tb, ub = lien(b)
    P.append(f"<div class='q'>Pour aller plus loin : <b>{html.escape(ta)}</b><br>"
             f"<span style='font-family:Consolas,monospace;font-size:10.5px'>{ua}</span><br>"
             f"<b>{html.escape(tb)}</b><br>"
             f"<span style='font-family:Consolas,monospace;font-size:10.5px'>{ub}</span></div>")
    P.append("<div class='q'>Prêté à : <span style='display:inline-block;width:60%;"
             "border-bottom:1px solid #cfd8e6'>&nbsp;</span></div>")
    P.append("<div class='q'>Rendu le : <span style='display:inline-block;width:30%;"
             "border-bottom:1px solid #cfd8e6'>&nbsp;</span></div>")
    P.append("</div>")
P.append("</div>")
P.append("<p style='font-size:12px;color:#5b6472'>Modèle reproduisible pour les collections "
         "C05 à C12 : même mise en page, mêmes champs.</p>")

P.append("<h2>4 · Règles de transmission</h2>")
P.append("""<table><thead><tr><th style="width:26%">Règle</th><th>Application concrète</th></tr></thead>
<tbody>
<tr><td><b>Un à un</b></td><td>Transmission uniquement de personne à personne. Jamais de diffusion
publique, jamais de groupe, jamais de lien partagé en masse.</td></tr>
<tr><td><b>Un fichier à la fois</b></td><td>On remet la piste ou le document demandé. On n’envoie
pas le dossier entier : il cesse d’être lu.</td></tr>
<tr><td><b>Liens officiels seulement</b></td><td>Tout renvoi vers une source passe par
www.jw.org ou wol.jw.org. Aucun extrait de publication n’est copié, hébergé ni republié.</td></tr>
<tr><td><b>Aucune collecte</b></td><td>Aucune donnée personnelle n’est demandée, stockée ni
transmise. La carte de prêt reste entre les mains de celui qui prête.</td></tr>
<tr><td><b>Aucune automatisation</b></td><td>Aucun envoi groupé, aucun robot, aucun compte destiné
à enseigner à la place d’une personne.</td></tr>
<tr><td><b>Aucune date</b></td><td>Ce qui n’est pas encore accompli n’est jamais daté.</td></tr>
</tbody></table>""")

P.append("<h2>5 · Liens officiels</h2><table><thead><tr><th>Ressource</th><th>Adresse</th>"
         "</tr></thead><tbody>")
for t, u in LIENS:
    P.append(f"<tr><td>{html.escape(t)}</td><td style='font-family:Consolas,monospace;font-size:12px'>"
             f"<a href='{u}'>{html.escape(u)}</a></td></tr>")
P.append("</tbody></table>")

P.append(FOOT)
open(os.path.join(ROOT, "PLANS_ECOUTE.html"), "w", encoding="utf-8").write("\n".join(P))

# ----------------------------------------------------------------------------
# FICHIER 3 — playlists .m3u
# ----------------------------------------------------------------------------
for c in C:
    lignes = ["#EXTM3U"]
    for p in c["p_caps"] + c["p"]:
        if d(p) <= 0:
            continue
        lignes.append(f"#EXTINF:{int(round(d(p)))},{titre(p)}")
        lignes.append(f"..\\{p}.mp3")
    open(os.path.join(OUT_PL, f"C{c['n']:02d}_{c['titre'].replace(' ', '_')}.m3u"),
         "w", encoding="utf-8").write("\n".join(lignes) + "\n")

# ----------------------------------------------------------------------------
print("Collections :", len(C))
print("Pistes totales (avec doublons) :", TOTAL_PISTES)
print("Duree totale :", mmss(TOTAL_C))
for c in C:
    print(f"  C{c['n']:02d} {c['titre'][:34]:<34} {c['np']:>2} p  {mmss(c['duree'])}")
print("Pistes sans duree (capsules non encore enregistrees) :", N_INCONNUES)
print("COLLECTIONS_AUDIO.html :", os.path.getsize(os.path.join(ROOT, "COLLECTIONS_AUDIO.html")) // 1024, "Ko")
print("PLANS_ECOUTE.html :", os.path.getsize(os.path.join(ROOT, "PLANS_ECOUTE.html")) // 1024, "Ko")
print("Playlists :", len(os.listdir(OUT_PL)))
