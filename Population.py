# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Population

Ce programme définit la classe Population et définit base_vins.
La méthode appliquer_criteres permet d'appliquer les critères sélectionnés.
Des méthodes de tris permettent de trier la population selon une variable.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


from Selection import *


class Population :
    """
    Un objet de type Population est définit par une liste d'objets de type Vin.
    """
    
    def __init__(self,population) :
        """
        L'argument population est une liste d'objets de type Vin.
        """
        self.vins = deepcopy(population)
        self.nb_vins = len(population)
    
    def __getitem__(self,i) :
        return self.vins[i]

    def appliquer_criteres(self) :
        """
        Modifie la liste des vins de sorte que tous les vins remplissant les 
        critères enregistrés dans la classe Selection.
        """
        
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
    
    def tri_croissant(self,nom_variable) :
        """
        Trie la liste des vins selon une variable dans l'ordre croissant.
        """
        pass
    
    def tri_decroissant(self,nom_variable) :
        """
        Trie la liste des vins selon une variable dans l'ordre décroissant.
        """
        pass

    def valeur_min_pop(self,nom_variable) :
        """
        Renvoie le vin ayant la valeur la plus faible sur la variable donnée
        au sein de la population.
        """
        res = self.vins[0]
        val_min = res[nom_variable]
        for vin in self.vins :
            val = vin[nom_variable]
            if val < val_min :
                res = vin
                val_min = val
        return res
    
    def valeur_max_pop(self,nom_variable) :
        """
        Renvoie le vin ayant la valeur la plus élevée sur la variable donnée 
        au sein de la population.
        """
        res = self.vins[0]
        val_max = res[nom_variable]
        for vin in self.vins :
            val = vin[nom_variable]
            if val > val_max :
                res = vin
                val_max = val
        return res

base_vins = Population(base_vins_objets)
