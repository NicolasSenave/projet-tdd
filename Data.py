"""
Application traitement de données
Module Data

Ce programme sert à importer et à accéder aux informations de la base de 
donnée. Il permet également quelques traitements élémentaires sur ces 
informations.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""

import json
import os


## Définition du répoertoire contenant les données

emplacement = os.getcwd()
emplacement = emplacement[ : -len('Modules')]
emplacement_donnees = emplacement + 'Données\\'


## Choix de la base de données

#fichiers = os.listdir(emplacement)
# Insérer un traitement : si il y a plusieurs fichier alors sélection fichier


## Importation des données choisies

with open(emplacement_donnees + 'vinData.json') as fichier :
    base_vins_dicos = json.load(fichier)

nb_vins_base = len(base_vins_dicos)

liste_noms_variables = ['quality',
                        'type',
                        'alcohol',
                        'density',
                        'pH',
                        'sulphates',
                        'chlorides',
                        'residual_sugar',
                        'citric_acid',
                        'fixed_acidity',
                        'volatile_acidity',
                        'free_sulfur_dioxide',
                        'total_sulfur_dioxide']

liste_noms_affiches_variables = ['Quality              ',
                               'Type                 ',
                               'Alcohol              ',
                               'Density              ',
                               'pH                   ',
                               'Sulfates             ',
                               'Chlorides            ',
                               'Residual sugar       ',
                               'Citric acid          ',
                               'Fixed acidity        ',
                               'Volatile acidity     ',
                               'Free sulfure dioxyde ',
                               'Total sulfure dioxyde']

def creer_dico(cles,valeurs) :
    """
    Entrée : deux listes
    Renvoie un dictionnaire dont les clés sont les éléments de la première
    liste et dont les valeurs sont les éléments de la deuxième.
    Les deux listes doivent être de la même longueur.
    """
    n = len(cles)
    assert len(valeurs) == n, "Les listes des clés et des valeurs doivent avoir la même longueur."
    #
    res = {}    
    for k in range(0,n) :
        res[cles[k]] = valeurs[k]
    return res

dico_noms_affiches = creer_dico(liste_noms_variables,liste_noms_affiches_variables)

nb_variables = len(liste_noms_variables)
