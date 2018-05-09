# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Affichage

Ce programme gère l'affichage de la population sélectionnée.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


from Population import *
# tkinter est importé via Selection, importé dans Population


# # à enlenver une fois le module terminé
# import os
# 
# emplacement = 'D:\\Documents\\Application'
# emplacement_modules = emplacement + '\\Modules'
# os.chdir(emplacement_modules)
# 
# fen = Tk()
# population_test = Population(base_vins_objets[0:20])
variables_test = liste_noms_variables[0:4]
#


class AffichagePopulation :
    
    fonction_sortie = None
    
    def donnees(population,variables) :
        """
        Méthode statique de la classe AffichagePopulation
        Construit le tableau dont les éléments sont de type str, avec 
        en ligne les vins et en colonne les variables retenues pour l'affichage
        """
        res = []
        # Sur la première ligne on affiche le nom des variables
        res.append(['Id'])
        for variable in variables :
            res[-1].append( dico_noms_affiches[variable] )
        # On remplit le tableau
        for vin in population :
            res.append( [str(getattr(vin,'id'))] )
            for variable in variables :
                res[-1].append( str(getattr(vin,variable)) )
        return res
    
    def __init__(self, fenetre, population=Population(), variables=liste_noms_variables ) :
        self.cadre = Frame(fenetre,bg='ivory')
        self.population = population
        self.variables_affichees = variables
        self.nb_lignes = len(population.vins)
        self.nb_colonnes = len(variables)
        self.donnees = AffichagePopulation.donnees(population,variables)
        self.tableau = []
    
    def afficher_tableau(self) :
        self.tableau = []
        for i in range(0,self.nb_lignes) : 
            ligne = [] 
            for j in range(0,self.nb_colonnes) : 
                cellule = Label(self.cadre,text=self.donnees[i][j],background='ivory') 
                ligne.append(cellule) 
                cellule.grid(row = i, column = j) 
            self.tableau.append(ligne)
    
    def __main__(self) :
        self.afficher_tableau()
        self.cadre.pack(fill=BOTH)
    
    def fin(self) :
        self.cadre.forget()

# #
# AffichagePopulation(fen,population_test,variables_test).__main__()
# 
# fen.mainloop()
# #

