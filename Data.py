# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Data

Ce programme sert à importer les informations de la base de donnée. 
Il importe également les modules python nécessaires aux autres programmes.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


import json


## Modules nécessaires pour d'autres programmes fils

from tkinter import *

from copy import copy,deepcopy


## Définition de répertoire des données

import os

emplacement_modules = os.getcwd()

emplacement_donnees = emplacement_modules[ : -len('Modules')] + 'Données\\'

## Importation des données

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
