# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Affichage

Ce programme gère l'affichage de la population sélectionnée.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""

## Notes de tests

# Méthode choisie pour l'affichage :
# on affiche les vins de la population par groupe de 50,
# avec possiblité de choisir la "page" qu'on veut afficher via boutons ou entrée du numéro
# quand on change de page, les éléments de l'ancienne sont détruits
# inconvénient : si on retourne sur une page, il faut la reconstruire
# avantage : pas d'accumulation d'objets, et donc de ralentissements, si l'utilisateur regarde plein de pages

# J'ai pas testé l'autre méthode (on garde les pages chargées), on pourrait essayer

# # à enlenver une fois le module terminé
# import os
# 
# emplacement = 'D:\\Documents\\Application'
# emplacement_modules = emplacement + '\\Modules'
# os.chdir(emplacement_modules)
# #



from Population import *
# tkinter est importé via Selection, importé dans Population


# # à enlenver une fois le module terminé
# fen = Tk()
# fen.geometry("800x500+100+100")
# population_test = Population(base_vins_objets[0:311])
# from copy import copy
# variables_test = copy(liste_noms_variables)
# #


class ParametresAffichage :
    
    variables_affichees = copy(liste_noms_variables)
    
    fonction_sortie = None
    
    def __init__(self,fen) :
        self.etiquette = Label(fen,text="Sélectionnez les variables que vous souhaitez afficher",font='Arial 12', background='ivory')
        self.vars_variables = {}
        self.cases_variables = []
        for nom_variable in liste_noms_variables :
            nom_affiche = dico_noms_affiches[nom_variable]
            var = IntVar()
            case = Checkbutton(fen, text=nom_affiche,font='Consolas 12', variable=var, background='ivory')
            case.select()
            self.cases_variables.append(case)
            self.vars_variables[nom_variable] = var
        self.bouton_valider = Button(fen, text="Valider",font='Arial 12', command=self.fin)
    
    def actualiser_parametres(self) :
        ParametresAffichage.variables_affichees = copy(liste_noms_variables)
        for nom_variable in self.vars_variables :
            var = self.vars_variables[nom_variable]
            if var.get() == 0 :
                ParametresAffichage.variables_affichees.remove(nom_variable)
    
    def __main__(self) :
        self.etiquette.pack()
        for case in self.cases_variables :
            case.pack()
        self.bouton_valider.pack()
    
    def fin(self) :
        self.actualiser_parametres()
        #
        self.etiquette.forget()
        for case in self.cases_variables :
            case.forget()
        self.bouton_valider.forget()
        ParametresAffichage.fonction_sortie()


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
    
    def __init__(self, fen, population, variables) :
        
        # Fenêtre globale de l'application
        self.fenetre = fen
        
        # Cadre du tableau
        self.cadre = Frame(fen,bg='ivory')
        
        # Données à afficher
        self.population = population
        self.variables_affichees = variables
        self.nb_lignes = len(population.vins)
        self.nb_colonnes = len(variables)
        self.donnees = AffichagePopulation.donnees(population,variables)
        
        # On affiche 50 vins par page
        self.page = 0
        if self.population.nb_vins == 0 :
            self.nb_pages = 0
        else :
            self.nb_pages = (self.nb_lignes - 1) // 50
        
        # Création des outils de navigation de pages
        if self.nb_pages >= 1 :
            #
            self.texte_page = StringVar()
            self.actualiser_texte_page()
            self.label_pages = Label(fen,textvariable=self.texte_page)
            #
            self.bouton_page_suiv = Button(fen,text="Page suivante",font='Arial 12',command=self.page_suivante)
            self.bouton_page_prec = Button(fen,text="Page précédente",font='Arial 12',command=self.page_precedente)
            self.entree_page = Entry(fen,width=5,font='Arial 12')
            self.entree_page.bind('<Return>',self.choix_page)
            #
            self.bouton_retour = Button(fen,text="Retour au menu",font='Arial 12',command=self.fin)
        
        # Création des barres de défilement
        self.barre_v = Scrollbar(self.cadre,orient=VERTICAL)
        self.barre_v.grid(row=0,column=1,sticky=N+S)
        self.barre_h = Scrollbar(self.cadre,orient=HORIZONTAL)
        self.barre_h.grid(row=1,column=0,sticky=E+W)
        
        # Création du canevas qui contient le tableau (frame) qui contient les cellules (labels)
        self.canvas = Canvas(self.cadre, bg='ivory', yscrollcommand=self.barre_v.set,xscrollcommand=self.barre_h.set)#♥width=600,height=400,
        
        # Fait que les barres de défilement s'ajustent à la taille de la fenêtre
        self.cadre.grid_columnconfigure(0,weight=1)
        self.cadre.grid_rowconfigure(0,weight=1)
        
        # Création du tableau (frame), dans le canevas, qui contient les cellules (labels) 
        self.tableau = Frame(self.canvas,background='ivory')
        
        # Création des cellules
        self.creer_cellules()
        
        # Pack du canevas 
        self.canvas.grid(row=0,column=0,sticky=N+S+E+W)
        
        # Pour utiliser les fleches des barres
        self.barre_v.config(command=self.canvas.yview)
        self.barre_h.config(command=self.canvas.xview)
        
        # Positionnement du canevas au début
        self.canvas.create_window(0,0,window=self.tableau)
        self.tableau.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.canvas.yview_moveto(0)
        self.canvas.xview_moveto(0)
        
        # Gestion de la liaison de la molette avec la fenêtre
        self.cadre.bind('<Enter>',self.activer_molette)
        self.canvas.bind('<Enter>',self.activer_molette)
        self.cadre.bind('<Leave>',self.desactiver_molette)
        
        # Création du menu de tri
        
        # Message d'indication
        texte_tri = "Sélectionnez une des variables avec les flèches du clavier ou le clic de la souris, \n"
        texte_tri += "puis utilisez un des boutons pour valider.\n"
        self.label_tri = Label(self.fenetre, text=texte_tri, font='Arial 12',justify=LEFT, background='ivory')
        
        # Liste des variables
        self.canvas_variables = Canvas(self.fenetre, background='ivory')
        self.labels_variables = []
        self.nb_variables = len(ParametresAffichage.variables_affichees)
        for nom_variable in ParametresAffichage.variables_affichees :
            nom_affiche = dico_noms_affiches[nom_variable]
            label = Label(self.canvas_variables, text=nom_affiche, padx=50, font='Consolas 12', background='ivory')
            label.pack()
            self.labels_variables.append(label)
        self.curseur = 0
        self.labels_variables[0].configure(background='lightblue')
        self.canvas_variables.bind('<Key>',self.choix_variable_tri)
        
        # Boutons valider/annuler
        self.bouton_tri_croissant = Button(self.fenetre, text="Tri croissant",font='Arial 12',bg='lightgreen', command=self.valider_tri_croissant)
        self.bouton_tri_decroissant = Button(self.fenetre, text="Tri décroissant",font='Arial 12',bg='lightgreen',  command=self.valider_tri_decroissant)
        self.bouton_annuler = Button(self.fenetre, text="Annuler",font='Arial 12', command=self.annuler_tri)
        
    
    def creer_cellules(self) :
        # On vide le tableau (frame)
        for cellule in self.tableau.winfo_children() :
            cellule.destroy()
        self.cadre.update()
        # Intitulé des variables
        Label(self.tableau,text='Id       ',background='ivory').grid(row=0,column=0,sticky=NW)
        for j in range (1,self.nb_colonnes + 1) :
            nom_variable = self.donnees[0][j]
            cellule = Label(self.tableau,text=nom_variable,background='ivory')
            cellule.grid(row=0,column=j,sticky=NW)
        # Ajout des valeurs
        p_debut = self.page*50 + 1
        p_fin = min( (self.page+1)*50 + 1, self.nb_lignes + 1)
        for i in range(p_debut, p_fin) :
            for j in range(0,self.nb_colonnes + 1) :
                valeur = self.donnees[i][j]
                cellule = Label(self.tableau,text=valeur,background='ivory') 
                if i < p_fin - 1 :
                    cellule.grid(row=i%50,column=j,sticky=NW)
                else :
                    cellule.grid(row=i,column=j,sticky=NW)
    
    def page_suivante(self) :
        if self.page == 0 :
            self.bouton_page_prec.pack(side=BOTTOM,anchor=W)
        self.page += 1
        if self.page == self.nb_pages :
            self.bouton_page_suiv.forget()
        self.actualiser_texte_page()
        self.creer_cellules()
    
    def page_precedente(self) :
        if self.page == self.nb_pages :
            self.bouton_page_suiv.pack(side=BOTTOM,anchor=E)
        self.page -= 1
        if self.page == 0 :
            self.bouton_page_prec.forget()
        self.actualiser_texte_page()
        self.creer_cellules()
    
    def choix_page(self,evenement=None) :
        self.page = int(self.entree_page.get()) - 1
        self.actualiser_texte_page()
        # Ici insérer un pop_up d'erreur
        # si l'utilisateur rentre autre chose qu'un nombre
        # Insérer ausi un test pour vérifier que la page demandée est valide
        if self.page == 0 :
            self.bouton_page_prec.forget()
            self.bouton_page_suiv.pack(side=BOTTOM,anchor=E)
        elif self.page == self.nb_pages :
            self.bouton_page_suiv.forget()
            self.bouton_page_prec.pack(side=BOTTOM,anchor=W)
        else :
            self.bouton_page_suiv.pack(side=BOTTOM,anchor=E)
            self.bouton_page_prec.pack(side=BOTTOM,anchor=W)
        self.entree_page.delete(0,END)
        self.creer_cellules()
    
    def actualiser_texte_page(self):
        self.texte_page.set( "Page %s sur %s" %(self.page+1,self.nb_pages+1) )
    
    def deplacement_molette(self,evenement):
        """
        Fonction permettant de lier le déplacement de la fenêtre avec 
        la molette de la souris 
        """ 
        if evenement.delta > 0 : 
            self.canvas.yview_scroll(-2,'units') 
        else: 
            self.canvas.yview_scroll(2,'units') 
    
    def activer_molette(self,event) :
        """
        Cette fonction active la molette lorsque le pointeur de la souris 
        est dans la fenêtre.
        """
        self.cadre.bind('<MouseWheel>', self.deplacement_molette) 
        self.canvas.bind_all('<MouseWheel>', self.deplacement_molette)
    
    def desactiver_molette(self,event):
        """
        Cette fonction désactive la liaison avec la molette quand le pointeur 
        de la souris sort de la fenêtre.
        """
        self.cadre.unbind('<MouseWheel>')
        self.canvas.unbind('<MouseWheel>')
    
    def __main__(self) :
        self.cadre.pack(expand=True,fill=BOTH)
        self.bouton_retour.pack(side=BOTTOM)
        self.label_pages.pack(side=BOTTOM)
        self.entree_page.pack(side=BOTTOM)
        self.bouton_page_suiv.pack(side=BOTTOM,anchor=E)
    
    def tri(self) :
        # Nettoyage de l'écran
        self.cadre.forget()
        self.label_pages.forget()
        self.bouton_page_suiv.forget()
        self.bouton_page_prec.forget()
        self.entree_page.forget()
        self.bouton_retour.forget()
        # Affichage du menu de tri
        self.label_tri.pack()
        self.canvas_variables.pack()
        self.canvas_variables.focus_set()
        self.bouton_annuler.pack(side=BOTTOM)
        self.bouton_tri_decroissant.pack(side=BOTTOM)
        self.bouton_tri_croissant.pack(side=BOTTOM)
    
    def choix_variable_tri(self,evenement) :
        
        touche = evenement.keysym
        
        if touche == "Down" :
            
            # if self.curseur == None :
            #     self.curseur = 0
            #     self.labels_variables[0].configure(background='lightblue')
            
            if self.curseur < self.nb_variables - 1 :
                self.labels_variables[self.curseur].configure(background='ivory')
                self.curseur += 1
                self.labels_variables[self.curseur].configure(background='lightblue')
            
            elif self.curseur == self.nb_variables - 1 :
                self.labels_variables[self.nb_variables - 1].configure(background='ivory')
                self.curseur = 0
                self.labels_variables[0].configure(background='lightblue')
            
        elif touche == "Up" :
            
            # if self.curseur == None :
            #     self.curseur = self.nb_variables - 1
            #     self.labels_variables[self.nb_variables - 1].configure(background='lightblue')
            
            if self.curseur > 0 :
                self.labels_variables[self.curseur].configure(background='ivory')
                self.curseur -= 1
                self.labels_variables[self.curseur].configure(background='lightblue')
            
            elif self.curseur == 0 :
                self.labels_variables[0].configure(background='ivory')
                self.curseur = self.nb_variables - 1
                self.labels_variables[self.nb_variables - 1].configure(background='lightblue')
    
    def valider_tri_croissant(self) :
        #
        self.label_tri.forget()
        self.canvas_variables.forget()
        self.bouton_tri_croissant.forget()
        self.bouton_tri_decroissant.forget()
        self.bouton_annuler.forget()
        #
        variable_tri = ParametresAffichage.variables_affichees[self.curseur]
        self.population.tri_croissant(variable_tri)
        #
        self.page = 0
        self.actualiser_texte_page()
        self.creer_cellules()
        #
        self.__main__()
    
    def valider_tri_decroissant(self) :
        #
        self.label_tri.forget()
        self.canvas_variables.forget()
        self.bouton_tri_croissant.forget()
        self.bouton_tri_decroissant.forget()
        self.bouton_annuler.forget()
        #
        variable_tri = ParametresAffichage.variables_affichees[self.curseur]
        self.population.tri_decroissant(variable_tri)
        #
        self.page = 0
        self.actualiser_texte_page()
        self.creer_cellules()
        #
        self.__main__()
    
    def annuler_tri(self) :
        #
        self.label_tri.forget()
        self.canvas_variables.forget()
        self.bouton_tri_croissant.forget()
        self.bouton_tri_decroissant.forget()
        self.bouton_annuler.forget()
        #
        self.__main__()
    
    def fin(self) :
        #
        self.cadre.forget()
        #
        self.label_pages.forget()
        self.bouton_page_suiv.forget()
        self.bouton_page_prec.forget()
        self.entree_page.forget()
        self.bouton_retour.forget()
        #
        AffichagePopulation.fonction_sortie()
        

# #
# def f() : pass
# AffichagePopulation.fonction_sortie = f
# AffichagePopulation(fen,population_test,variables_test).__main__()
# fen.mainloop()
# #

