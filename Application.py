# -*- coding: utf-8 -*-
"""
Application traitement de données

Programme principal.
Lance l'application et assure la gestion des menus, 
qui permettent à l'utilisateur de naviguer dans les différentes fonctionnalités.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


## Définition des répertoires
import os

#emplacement = os.getcwd()
emplacement = 'D:\\Documents\\Application'
emplacement_modules = emplacement + '\\Modules'
emplacement_donnees = emplacement + '\\Données'
emplacement_images = emplacement + '\\Images'


## Import des modules
os.chdir(emplacement_modules)

from Affichage import *
# Affichage -> Population -> Selection -> Vins -> Data

from Stat_uni import *
from Test_chi_deux import *
from Clustering import *

from Exports import *


## Application

class Application(Tk) :
    
    def __init__(self) :
        
        # Initialisation
        Tk.__init__(self)
        # Titre
        self.title("Application")
        # Dimensions
        self.geometry("800x550+100+70")
        # Coleur de fond
        self.configure(bg='ivory')
        # Logo
        os.chdir(emplacement_images)
        logo = PhotoImage(file='logo.png')
        self.call('wm', 'iconphoto', self._w, logo)
        # Barre de menu
        self.barre_de_menu()
        
        # Menu principal
        
        texte_titre = "Projet traitement de données\n\nEnsai - 1ère année"
        self.label_titre = Label(self, text=texte_titre, background='lightblue',font='Arial 24')
        
        texte_noms = "Tanguy Barthélémy, Killian Poulain, Nicolas Sénave"
        self.label_noms = Label(self, text=texte_noms, background='lightblue',font='Arial 18')
        
        # Menu intermédiaire
        
        self.texte_population = StringVar()
        self.label_population = Label(self,textvariable=self.texte_population, background='ivory',font='Arial 12')
        
        texte_indication = "Utilisez le menu pour sélectionner l'opération souhaitée.\n\n"
        texte_indication += "Si vous souhaitez ensuite effectuer une autre action, utilisez le bouton permettant de revenir sur ce menu."
        self.label_indication = Label(self,text=texte_indication, background='ivory',font='Arial 10')
        
        self.bouton_retour = Button(self, text="Retour à l'écran d'accueil",font='Arial 12',command=self.menu_principal)
        
        # Ecran de chargement
        
        self.etiquette_chargement = Label(self,text="Chargement en cours...",background='ivory',font='Arial 10')
        
        # Défintion des fonctions de naviguation des fonctionnalités
        
        Selection.fonction_valider = self.selection_fin
        Selection.fonction_retour = self.menu_principal
        
        ParametresAffichage.fonction_sortie = self.affichage
        
        AffichagePopulation.fonction_sortie = self.menu_intermediaire
        
        AffichageUnivariee.fonction_chargement = self.stat_uni_resultats
        AffichageUnivariee.fonction_sortie = self.menu_intermediaire
        
    
    ## Barre de menu
    
    def barre_de_menu(self) :
        """
        Crée la barre de menu.
        """
        barre_menu = Menu(self)
        
        self.menu_select = Menu(barre_menu, tearoff=0)
        self.menu_select.add_command(label="Travailler sur la base complète", command = self.menu_intermediaire)
        self.menu_select.add_separator()
        self.menu_select.add_command(label="Sélectionner une sous-population", command=self.selection)
        self.menu_select.add_command(label="Modifier les criètres de sélection", command=self.selection)
        barre_menu.add_cascade(label="Sélection", menu=self.menu_select)
        
        self.menu_traitements = Menu(barre_menu, tearoff=0)
        self.menu_traitements.add_command(label="Lancer une analyse descriptive",command=self.stat_uni_choix_variable)
        self.menu_traitements.add_separator()
        self.menu_traitements.add_command(label="Lancer un test d'indépendance",command=self.test_chi_deux)
        self.menu_traitements.add_separator()
        self.menu_traitements.add_command(label="Regrouper les vins en classes",command=self.clustering)
        barre_menu.add_cascade(label="Traitements",menu=self.menu_traitements)
        
        self.menu_affichage = Menu(barre_menu, tearoff=0)
        self.menu_affichage.add_command(label="Afficher la population choisie",command=self.parametres_affichage)
        self.menu_affichage.add_separator()
        self.menu_affichage.add_command(label="Trier les vins de la population",command=self.tri_affichage)
        barre_menu.add_cascade(label="Affichage",menu=self.menu_affichage)
        
        self.menu_exporter = Menu(barre_menu, tearoff=0)
        self.menu_exporter.add_command(label="Exporter la population sélectionnée", command=self.export)
        barre_menu.add_cascade(label="Exporter", menu=self.menu_exporter)
        
        self.config(menu=barre_menu)
    
    def enable_traitements(self) :
        """
        Active la section "Traitements" de la barre de menu.
        """
        self.menu_traitements.entryconfigure(0, state=NORMAL)
        self.menu_traitements.entryconfigure(2, state=NORMAL)
        self.menu_traitements.entryconfigure(4, state=NORMAL)
    
    def disable_traitements(self) :
        """
        Désactive la section "Traitements" de la barre de menu.
        """
        self.menu_traitements.entryconfigure(0, state=DISABLED)
        self.menu_traitements.entryconfigure(2, state=DISABLED)
        self.menu_traitements.entryconfigure(4, state=DISABLED)
        
    def enable_all(self) :
        """
        Active toutes les fonctions de la barre de menu.
        """
        self.menu_select.entryconfigure(0, state=NORMAL)
        self.menu_select.entryconfigure(2, state=NORMAL)
        self.menu_select.entryconfigure(3, state=NORMAL)
        self.enable_traitements()
        self.menu_affichage.entryconfigure(0, state=NORMAL)
        self.menu_affichage.entryconfigure(2, state=NORMAL)
        self.menu_exporter.entryconfigure(0, state=NORMAL)
    
    def disable_all(self) :
        """
        Désactive toutes les fonctions de la barre de menu.
        """
        self.menu_select.entryconfigure(0, state=DISABLED)
        self.menu_select.entryconfigure(2, state=DISABLED)
        self.menu_select.entryconfigure(3, state=DISABLED)
        self.disable_traitements()
        self.menu_affichage.entryconfigure(0, state=DISABLED)
        self.menu_affichage.entryconfigure(2, state=DISABLED)
        self.menu_exporter.entryconfigure(0, state=DISABLED)
    
    ## Menus
        
    def menu_principal(self) :
        """
        Affiche le menu principal.
        La population est réinitialisée.
        Depuis ce menu, on peut choisir la population d'étude.
        """
        # Nettoyage de l'écran
        self.reinit_ecran()
        # Gestion de la barre de menu
        self.menu_select.entryconfigure(0, state=NORMAL)
        self.menu_select.entryconfigure(2, state=NORMAL)
        self.menu_select.entryconfigure(3, state=DISABLED)
        self.disable_traitements()
        self.menu_affichage.entryconfigure(0, state=DISABLED)
        self.menu_affichage.entryconfigure(2, state=DISABLED)
        self.menu_exporter.entryconfigure(0, state=DISABLED)
        # Affichage du menu
        self.label_titre.pack(expand=True,fill=BOTH)
        self.label_noms.pack(expand=True,fill=BOTH)
        # Initialisation de la population
        self.population = deepcopy(base_vins)
        # Réinitialisation des variables (qui contiennent les critères)
        Selection.liste_variables = deepcopy(liste_variables)
        # Initialisation de l'écran de sélecion des critères
        self.ecran_selection = Selection(self)
        # Initialisation de l'écran de sélection des variables affichées
        self.ecran_parametres = ParametresAffichage(self)
    
    def menu_intermediaire(self) :
        """
        Affiche le menu intermédiaire.
        Depuis ce menu, on peut utiliser les autres fonctionnalités.
        """
        # Nettoyage de l'écran
        self.reinit_ecran()
        # Gestion de la barre de menu
        self.menu_select.entryconfigure(0, state=DISABLED)
        self.menu_select.entryconfigure(2, state=DISABLED)
        self.menu_select.entryconfigure(3, state=NORMAL)
        self.enable_traitements()
        self.menu_affichage.entryconfigure(0, state=NORMAL)
        self.menu_affichage.entryconfigure(2, state=DISABLED)
        self.menu_exporter.entryconfigure(0, state=NORMAL)
        # Affichage du menu
        resume = "La population séléctionnée contient %s vins." %(self.population.nb_vins)
        self.texte_population.set(resume)
        self.label_population.pack(expand=True,fill=BOTH)
        self.label_indication.pack(expand=True,fill=BOTH)
        self.bouton_retour.pack(side=BOTTOM)
        
    def reinit_ecran(self) :
        """
        Nettoie l'affichage pour permettre à une fonctionnalité de s'afficher.
        """
        # Désafficher le menu principal
        self.label_titre.forget()
        self.label_noms.forget()
        # Désafficher le menu intermédiaire
        self.label_population.forget()
        self.label_indication.forget()
        self.bouton_retour.forget()
    
    def ecran_chargement(self) :
        """
        Affiche un écran de chargement.
        """
        self.etiquette_chargement.pack(expand=True,fill=BOTH)
    
    def fin_chargement(self) :
        """
        Désaffiche l'écran de chargement.
        """
        self.etiquette_chargement.forget()
    
    ## Sélection
    
    def selection(self) :
        """
        Fonctions "Séléctionner une sous-population" 
        et "Modifier les criètres de sélection" du menu.
        Lance l'écran de sélection de critères.
        Si un population a déjà été sélectionnée,
        permet de revenir à l'écran de sélection des critères.
        """
        # Nettoyage de l'écran
        self.reinit_ecran()
        # Gestions de la barre de menu
        self.disable_all()
        # Lancer la sélection
        self.ecran_selection.__main__()

    def selection_fin(self) :
        """
        Fonction lancée après validation des critères.
        Applique les critères sélectionnés sur la population, 
        et renvoie au menu de sélection des opérations.
        """
        # Application des critères sur la population
        self.ecran_chargement()
        self.update()
        self.population.appliquer_criteres()
        self.fin_chargement()
        # Affichage du menu intermédiaire
        self.menu_intermediaire()
    
    ## Affichage
    
    def parametres_affichage(self) :
        """
        Fonction "Afficher la population choisie" du menu.
        """
        # Nettoyage de l'écran
        self.reinit_ecran()
        # Gestion de la barre de menu
        self.disable_all()
        self.menu_exporter.entryconfigure(0, state=NORMAL)
        # Lancer le menu de sélection des variables à afficher
        self.ecran_parametres.__main__()
    
    def affichage(self) :
        """
        Cette fonction est lancée juste après parametres_affichage.
        Lance l'affichage de la population sélectionnée.
        """
        # Gestion de la barre de menu
        self.menu_affichage.entryconfigure(2, state=NORMAL)
        # Initialisation de l'écran d'affichage de la population
        self.ecran_chargement()
        self.update()
        self.ecran_affichage = AffichagePopulation(self,self.population,ParametresAffichage.variables_affichees)
        self.fin_chargement()
        # Lancer l'affichage de la population
        self.ecran_affichage.__main__()
    
    def tri_affichage(self) :
        """
        Fonction "Trier les vins de la population" du menu.
        Cette fonction ne peut être lancée que depuis l'écran d'affichage de la population.
        Lance la procédure de tri selon une variable.
        """
        self.ecran_affichage.tri()
    
    ## Statistique univariée
    
    def stat_uni_choix_variable(self) :
        """
        Fonction "Lancer une analyse descriptive" du menu.
        L'utilisateur choisit la variable à étudier.
        """
        # Nettoyage de l'écran
        self.reinit_ecran()
        # Gestion de la barre de menu
        self.disable_all()
        # Menu de statistique univariée
        self.ecran_univariee = AffichageUnivariee(self,self.population)
        self.ecran_univariee.menu_choix_variable()
    
    def stat_uni_resultats(self) :
        """
        Fonction lancée après stat_uni_choix_variable.
        Affiche les résultats.
        """
        # Calculs
        self.ecran_chargement()
        self.update()
        self.ecran_univariee.calculs()
        self.fin_chargement()
        # Affichage des résultats
        self.ecran_univariee.affichage_resultats()
    
    ## Test d'indépendance
    
    def test_chi_deux(self) :
        """
        Fonction "Lancer un test d'indépendance" du menu.
        """
        pass
    
    ## Clustering
    
    def clustering(self) :
        """
        Fonction "Regrouper les vins en classes" du menu.
        """
        pass
    
    ## Export
    
    def export(self) :
        """
        Fonction "Exporter la population sélectionnée" du menu.
        """
        # L'utilisateur définit l'emplacment
        emplacement_export = askdirectory(title="Exporter la population dans une feuille de calcul .xls")
        
        # Initialisation du classeur
        classeur = Workbook()
        feuille = classeur.add_sheet("Vins")
        
        # Ajout du nom des variables
        feuille.write(0,0,'Id')
        for j in range(0,nb_variables) :
            nom_variable = liste_noms_affiches_variables[j]
            feuille.write(0,j+1,nom_variable)
        
        # Ajout des valeurs
        for i in range(0,self.population.nb_vins) :
            vin = self.population[i]
            feuille.write(i+1,0,vin.id)
            for j in range(0,nb_variables) :
                nom_variable = liste_noms_variables[j]
                valeur = getattr(vin, nom_variable)
                feuille.write(i+1,j+1,valeur)
        
        # Enregistrement du fichier
        classeur.save(emplacement_export + '/Vins.xls')


## Mainloop

fen = Application()
fen.menu_principal()
fen.mainloop()
