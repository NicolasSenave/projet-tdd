# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Population

Ce programme définit la classe Population.
base_vins est un objet de type Population contenant par défaut tous les vins,
classés par identifiants.
La méthode appliquer_criteres permet de réduire la population via les critères 
contenus dans les objets de type Variable de liste_variable (module Selection).
Des méthodes de tris permettent de trier la population selon une variable.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


from Selection import *
# Le module copy est importé via Selection

        
class Population :
    
    def __init__(self,population=[],criteres=None) :
        """
        L'argument optionnel population est par défaut une liste vide,
        sinon une liste d'objets de type Vin
        """
        self.vins = deepcopy(population)
        self.nb_vins = len(population)
    
    def __getitem__(self,i) :
        return self.vins[i]

    def appliquer_criteres(self) :
        
        self.vins = deepcopy(base_vins.vins)
        self.nb_vins = len(self.vins)

        for variable in Selection.liste_variables :
            
            if variable.type_variable == 'quanti' :
                k = 0
                while k < self.nb_vins :
                    vin = self.vins[k]
                    test_min = getattr(vin,variable.nom) >= variable.critere_min
                    test_max = getattr(vin,variable.nom) <= variable.critere_max
                    if not (test_min and test_max) :
                        self.vins.remove(vin)
                        self.nb_vins -= 1
                    else :
                        k += 1
            
            else :
                k = 0
                while k < self.nb_vins :
                    vin = self.vins[k]
                    mod = getattr(vin,variable.nom)
                    if mod not in variable.critere_modalites :
                        self.vins.remove(vin)
                        self.nb_vins -= 1
                    else :
                        k += 1
    
    def tri_croissant(self,variable) :
        pass
    
    def tri_decroissant(self,variable) :
        pass

    def valeur_min_pop(self,variable) :
        """
        Entrée : une sous-population de vins non vide (list)
        et le nom d'une variable quantitative (str)
        Renvoie le vin ayant la valeur la plus faible sur la variable donnée
        au sein de la populaton donnée
        """
        res = self.vins[0]
        val_min = res[variable]
        for vin in self.vins :
            val = vin[variable]
            if val < val_min :
                res = vin
                val_min = val
        return res
    
    def valeur_max_pop(self,variable) :
        """
        Entrée : une sous-population de vins non vide (list)
        et le nom d'une variable quantitative (str)
        Renvoie le vin ayant la valeur la plus élevée sur la variable donnée 
        au sein de la population donnée
        """
        res = self.vins[0]
        val_max = res[variable]
        for vin in self.vins :
            val = vin[variable]
            if val > val_max :
                res = vin
                val_max = val
        return res

base_vins = Population(base_vins_objets)
