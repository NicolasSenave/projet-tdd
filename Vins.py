# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Vins

Ce programme définit la classe Vin et génère une liste des vins.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


from Data import *


class Vin :
    
    def __init__(self,vin) :
        """
        L'argument vin est un vin de type dictionnaire.
        """
        # Identifiant
        self.id = vin['wine identity']
        # Variable de qualité
        self.quality = vin['quality']
        # Variables qualitatives
        self.type = vin['type']
        # Variables quantitatives
        self.alcohol = vin['alcohol']
        self.density = vin['density']
        self.pH = vin['pH']
        self.sulphates = vin['sulphates']
        self.chlorides = vin['chlorides']
        self.residual_sugar = vin['residual sugar']
        self.citric_acid = vin['citric acid']
        self.fixed_acidity =  vin['fixed acidity']
        self.volatile_acidity = vin['volatile acidity']
        self.free_sulfur_dioxide = vin['free sulfur dioxide']
        self.total_sulfur_dioxide = vin['total sulfur dioxide']
    
    def __str__(self) :
        res = '\nWine identity        ' + ': ' + str(self.id) + '\n'
        for nom_variable in dico_noms_affiches :
            nom_affiche = dico_noms_affiches[nom_variable]
            valeur = getattr(self,nom_variable)
            res += nom_affiche + ': ' + str(valeur) + '\n'
        return res
    
    def __repr__(self) :
        return "Vin " + str(self.id)
    
    def __eq__(self,vin) :
        """
        Deux vins sont égaux si leurs identifiants sont égaux.
        """
        return self.id == vin.id

base_vins_objets = [Vin(vin) for vin in base_vins_dicos]
