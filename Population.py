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
    
    def tri_quanti_croissant(liste_vins,nom_variable) :
        """
        Méthode statique de la classe Population.
        liste_vins est un liste d'objets de type vins.
        nom_variable est le nom d'une variable quantitative.
        Renvoie une liste contenant les vins, triées dans l'ordre croissant 
        selon la variable donnée.
        Ne modifie pas la liste donnée en entrée.
        La méthode employée est un algorithme récursif de tri rapide.
        """
        n = len(liste_vins)
        if n <= 1 :
            return liste_vins
        else :
            vin_pivot = liste_vins.pop( randrange(0,n) )
            valeur = getattr(vin_pivot,nom_variable)
            vins_inf = []
            vins_sup = []
            for vin in liste_vins :
                if getattr(vin,nom_variable) < valeur :
                    vins_inf.append(vin)
                else :
                    vins_sup.append(vin)
            return Population.tri_quanti_croissant(vins_inf,nom_variable) + [vin_pivot] + Population.tri_quanti_croissant(vins_sup,nom_variable)
    
    def tri_quanti_croissant_bis(liste_vins,nom_variable) :
        """
        Similaire à tri_quanti_croissant.
        Modifie la liste donnée en entrée.
        Cette fonction est appelée si le nombre maximal de récursions est 
        atteint avec l'algorithme de tri rapide.
        """
        n = len(liste_vins)
        for k in range (1,n) :
            vin1 = liste_vins[k]
            vin2 = liste_vins[k-1]
            while getattr(vin1,nom_variable) < getattr(vin2,nom_variable) and k > 0 :
                liste_vins[k] = vin2
                liste_vins[k-1] = vin1
                k = k-1
                vin2 = liste_vins[k-1]
        return liste_vins
    
    def tri_quanti_decroissant(liste_vins,nom_variable) :
        """
        Méthode statique de la classe Population.
        liste_vins est un liste d'objets de type vins.
        nom_variable est le nom d'une variable quantitative.
        Renvoie une liste contenant les vins, triées dans l'ordre décroissant 
        selon la variable donnée.
        Ne modifie pas la liste donnée en entrée.
        La méthode employée est un algorithme récursif de tri rapide.
        """
        n = len(liste_vins)
        if n <= 1 :
            return liste_vins
        else :
            vin_pivot = liste_vins.pop( randrange(0,n) )
            valeur = getattr(vin_pivot,nom_variable)
            vins_inf = []
            vins_sup = []
            for vin in liste_vins :
                if getattr(vin,nom_variable) >= valeur :
                    vins_inf.append(vin)
                else :
                    vins_sup.append(vin)
            return Population.tri_quanti_decroissant(vins_inf,nom_variable) + [vin_pivot] + Population.tri_quanti_decroissant(vins_sup,nom_variable)
    
    def tri_quanti_decroissant_bis(liste_vins,nom_variable) :
        """
        Similaire à tri_quanti_decroissant.
        Modifie la liste donnée en entrée.
        Cette fonction est appelée si le nombre maximal de récursions est 
        atteint avec l'algorithme de tri rapide.
        """
        n = len(liste_vins)
        for k in range (1,n) :
            vin1 = liste_vins[k]
            vin2 = liste_vins[k-1]
            while getattr(vin1,nom_variable) > getattr(vin2,nom_variable) and k > 0 :
                liste_vins[k] = vin2
                liste_vins[k-1] = vin1
                k = k-1
                vin2 = liste_vins[k-1]
        return liste_vins
    
    def tri_quali_croissant(liste_vins,nom_variable) :
        """
        Méthode statique de la classe Population.
        liste_vins est un liste d'objets de type vins.
        nom_variable est le nom d'une variable qualitative.
        Renvoie une liste contenant les vins, triées dans l'ordre croissant 
        selon la variable donnée (tri alphanumérique).
        Ne modifie pas la liste donnée en entrée.
        """
        #
        variable = dico_variables[nom_variable]
        modalites = variable.modalites
        #
        modalites.sort()
        #
        liste_triee = []
        for mod in modalites :
            for vin in liste_vins :
                if getattr(vin,nom_variable) == mod :
                    liste_triee.append(vin)
        return liste_triee
    
    def tri_quali_decroissant(liste_vins,nom_variable) :
        """
        Méthode statique de la classe Population.
        liste_vins est un liste d'objets de type vins.
        nom_variable est le nom d'une variable qualitative.
        Renvoie une liste contenant les vins, triées dans l'ordre décroissant 
        selon la variable donnée (tri alphanumérique).
        Ne modifie pas la liste donnée en entrée.
        """
        #
        variable = dico_variables[nom_variable]
        modalites = variable.modalites
        #
        modalites.sort(reverse=True)
        #
        liste_triee = []
        for mod in modalites :
            for vin in liste_vins :
                if getattr(vin,nom_variable) == mod :
                    liste_triee.append(vin)
        return liste_triee
    
    def __init__(self,liste_vins) :
        """
        L'argument population est une liste d'objets de type Vin.
        """
        self.vins = deepcopy(liste_vins)
        self.nb_vins = len(liste_vins)
    
    def __getitem__(self,i) :
        return self.vins[i]
    
    def __add__(self,population) :
        t = type(population)
        if t == Population :
            return Population(self.vins + population.vins)
        elif t == list :
            return Population(self.vins + population)
        else :
            msg = "Opération + impossible entre 'Population' et '%s'." %(t)
            raise TypeError(msg)

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
        variable = dico_variables[nom_variable]
        if variable.type_variable == 'quanti' :
            try :
                self.vins = Population.tri_quanti_croissant(self.vins,nom_variable)
            except RuntimeError :
                self.vins = Population.tri_quanti_croissant_bis(self.vins,nom_variable)
        else :
            self.vins = Population.tri_quali_croissant(self.vins,nom_variable)
    
    def tri_decroissant(self,nom_variable) :
        """
        Trie la liste des vins selon une variable dans l'ordre décroissant.
        """
        variable = dico_variables[nom_variable]
        if variable.type_variable == 'quanti' :
            try :
                self.vins = Population.tri_quanti_decroissant(self.vins,nom_variable)
            except RuntimeError :
                self.vins = Population.tri_quanti_decroissant_bis(self.vins,nom_variable)
        else :
            self.vins = Population.tri_quali_decroissant(self.vins,nom_variable)

    def valeur_min_pop(self,nom_variable) :
        """
        nom_variable est le nom d'une variable quantitative (str).
        Renvoie la plus faible sur la variable donnée 
        au sein de la population.
        """
        res = self.vins[0]
        val_min = res[nom_variable]
        for vin in self.vins :
            val = vin[nom_variable]
            if val < val_min :
                res = vin
                val_min = val
        return val_min
    
    def valeur_max_pop(self,nom_variable) :
        """
        nom_variable est le nom d'une variable quantitative (str).
        Renvoie la valeur la plus élevée sur la variable donnée 
        au sein de la population.
        """
        res = self.vins[0]
        val_max = res[nom_variable]
        for vin in self.vins :
            val = vin[nom_variable]
            if val > val_max :
                res = vin
                val_max = val
        return val_max

base_vins = Population(base_vins_objets)
