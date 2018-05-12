"""
Application traitement de données

Programme principal
Ce script lance l'application et assure la gestion des menus, 
qui permettent à l'utilisateur de naviguer dans les différentes fonctionnalités.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""

#Note gobale :
# On pourrait remplacer les forget par des destroy dans les méthodes fin des modules
# pour gagner un peu d'espace en mémoire et rendre l'application légèrement plus rapide


## Import des modules

import os

#emplacement = os.getcwd()
emplacement = 'D:\\Documents\\Application'
emplacement_modules = emplacement + '\\Modules'
os.chdir(emplacement_modules)

from Affichage import *
# Affichage -> Population -> Selection -> Vins -> Data

from Stat_uni import *
from Test_chi_deux import *
from Clustering import *

from Exports import *


## Définition de la fenetre principale

from tkinter import *

fen = Tk()
fen.title("Application")
fen.geometry("800x550+100+70")
fen.configure(bg='ivory')

emplacement_images = emplacement + '\\Images'
os.chdir(emplacement_images)
logo = PhotoImage(file='logo.png')
fen.call('wm', 'iconphoto', fen._w, logo)


## Nettoyer la fenêtre

def reinit_ecran() :
    """
    Désaffiche tous les objets Tkinter pour préparer l'affichage d'une 
    fonctionnalité
    """
    #
    label_titre.forget()
    label_noms.forget()
    #
    label_population.forget()
    label_indication.forget()
    bouton_retour.forget()
# NB : en vrai désafficher tous les objets de l'écran à n'importe quel moment 
# c'est pas simplbe du tout
# On va peut être laisser tomber cette fonction en la transformant en 
# menu_pricipal_fin
# et n'afficher la barre de menus qu'au menu principal ;
# on utilisera des boutons ou autre dans le reste de l'application


## Menu principal

texte_titre = "Projet traitement de données\nEnsai - 1ère année"
label_titre = Label(fen, text=texte_titre, background='lightblue',font='Arial 24')

texte_noms = "Tanguy Barthélémy, Killian Poullain, Nicolas Sénave"
label_noms = Label(fen, text=texte_noms, background='lightblue',font='Arial 18')

def menu_principal() :
    """
    Affiche le menu principal
    """
    global population
    #
    reinit_ecran()
    #
    population = deepcopy(base_vins)
    #
    menu_select.entryconfigure(0, state=NORMAL)
    menu_select.entryconfigure(2, state=NORMAL)
    menu_select.entryconfigure(3, state=DISABLED)
    disable_traitements()
    menu_affichage.entryconfigure(0, state=DISABLED)
    menu_affichage.entryconfigure(2, state=DISABLED)
    menu_exporter.entryconfigure(0, state=DISABLED)
    #
    label_titre.pack(expand=True,fill=BOTH)
    label_noms.pack(expand=True,fill=BOTH)



## Menu intermédiaire

texte_population = StringVar()
label_population = Label(fen,textvariable=texte_population, background='ivory',font='Arial 12')

texte_indication = "Utilisez le menu pour sélectionner l'opération souhaitée.\n\n"
texte_indication += "Si vous souhaitez ensuite effectuer une autre action, utilisez le bouton permettant de revenir sur ce menu."

label_indication = Label(fen,text=texte_indication, background='ivory',font='Arial 10')

bouton_retour = Button(fen, text="Retour à l'écran d'accueil",font='Arial 12',command=menu_principal)

def menu_intermediaire() :
    global population
    #
    reinit_ecran()
    #
    menu_select.entryconfigure(0, state=DISABLED)
    menu_select.entryconfigure(2, state=DISABLED)
    menu_select.entryconfigure(3, state=NORMAL)
    enable_traitements()
    menu_affichage.entryconfigure(0, state=NORMAL)
    menu_affichage.entryconfigure(2, state=DISABLED)
    menu_exporter.entryconfigure(0, state=NORMAL)
    #
    resume = "La population séléctionnée contient %s vins." %(population.nb_vins)
    texte_population.set(resume)
    label_population.pack(expand=True,fill=BOTH)
    label_indication.pack(expand=True,fill=BOTH)
    bouton_retour.pack(side=BOTTOM)
    


## Ecran de chargement

etiquette_chargement = Label(fen,text="Chargement en cours...",background='ivory',font='Arial 10')

def ecran_chargement() :
    etiquette_chargement.pack(expand=True,fill=BOTH)

def fin_chargement() :
    etiquette_chargement.forget()


## Fonctionnalité : Séléction des critères

def base_complete() :
    global ecran_selection
    #
    Selection.fonction_valider = selection_fin
    Selection.fonction_retour = menu_principal
    ecran_selection = Selection(fen)
    #
    menu_intermediaire()

def selection() :
    """
    Fonction "Séléctionner une sous-population" du menu
    """
    global ecran_selection
    #
    reinit_ecran()
    #
    disable_all()
    # On réinitialise les variables (qui contiennent les critères)
    Selection.liste_variables = deepcopy(liste_variables)
    #
    Selection.fonction_valider = selection_fin
    Selection.fonction_retour = menu_principal
    ecran_selection = Selection(fen)
    ecran_selection.__main__()

def modif_criteres() :
    """
    Si des critères on déjà été validés,
    permet de revenir à l'écran de sélection des critères
    Sinon, affiche un popup d'erreur
    """
    global ecran_selection
    #
    reinit_ecran()
    #
    disable_all()
    #
    ecran_selection.__main__()

def selection_fin() :
    """
    Fonction lancée après validation des critères
    """
    global population
    #
    ecran_chargement()
    fen.update()
    population.appliquer_criteres()
    fin_chargement()
    #
    menu_intermediaire()


## Fonctionnalité : Affichage d'une liste de vins

ecran_parametres = ParametresAffichage(fen)
def parametres_affichage() :
    """
    Fonction "Afficher la population choisie" du menu
    """
    global ecran_parametres
    #
    reinit_ecran()
    #
    disable_all()
    #
    ParametresAffichage.fonction_sortie = affichage
    ecran_parametres.__main__()

def affichage() :
    """
    Cette fonction est lancé juste après parametres_affichage.
    Lance l'affichage de la population sélectionnée
    """
    #
    global population,ecran_affichage,ecran_parametres
    #
    menu_affichage.entryconfigure(2, state=NORMAL)
    #
    ecran_chargement()
    fen.update()
    ecran_affichage = AffichagePopulation(fen,population,ParametresAffichage.variables_affichees)
    fin_chargement()
    #
    AffichagePopulation.fonction_sortie = affichage_fin
    ecran_affichage.__main__()



def tri_affichage() :
    """
    Cette fonction ne peut être lancée que depuis l'écran d'affichage de la population.
    Lance la procédure de tri selon une variable.
    """
    global ecran_affichage
    #
    ecran_affichage.tri()

def affichage_fin() :
    """
    Fonction lancée via le bouton Retour de l'écran d'affichage de la population.
    Renvoie au menu de sélection des fonctionnalités.
    """
    menu_intermediaire()


## Fonctionnalité : Statistique univariée

def stat_uni() :
    """
    Fonction "Lancer une analyse descriptive" du menu
    """
    reinit_ecran()
    #
    Stat_uni.fonction_sortie = stat_uni_fin
    Stat_uni(fen).__main__()

def stat_uni_fin() :
    print("coucou stat uni terminée")

    
## Fonctionnalité : Test d'indépendance

def test_chi_deux() :
    """
    Fonction "Lancer un test d'indépendance" du menu
    """
    reinit_ecran()
    #
    Test_chi_deux.fonction_sortie = test_chi_deux_fin
    Test_chi_deux(fen).__main__()

def test_chi_deux_fin() :
    print("coucou test chi deux terminé")


## Fonctionnalité : clustering

def clustering() :
    """
    Fonction "Regrouper les vins en classes" du menu
    """
    reinit_ecran()
    #
    Clustering.fonction_sortie = clustering_fin
    Clustering(fen).__main__()

def clustering_fin() :
    print("coucou clustering fin")


## Fonctionnalité : Exporter
 
def exports() :
    """
    Fonction "Exporter la population sélectionnée" du menu
    """
    print("coucou exports")
    

## Barre des menus

barre_menu = Menu(fen)

menu_select = Menu(barre_menu, tearoff=0)
menu_select.add_command(label="Travailler sur la base complète", command = base_complete)
menu_select.add_separator()
menu_select.add_command(label="Sélectionner une sous-population", command=selection)
menu_select.add_command(label="Modifier les criètres de sélection", command=modif_criteres)
barre_menu.add_cascade(label="Sélection", menu=menu_select)

menu_traitements = Menu(barre_menu, tearoff=0)
menu_traitements.add_command(label="Lancer une analyse descriptive",command=stat_uni)
menu_traitements.add_separator()
menu_traitements.add_command(label="Lancer un test d'indépendance",command=test_chi_deux)
menu_traitements.add_separator()
menu_traitements.add_command(label="Regrouper les vins en classes",command=clustering)
barre_menu.add_cascade(label="Traitements",menu=menu_traitements)

def enable_traitements() :
    menu_traitements.entryconfigure(0, state=NORMAL)
    menu_traitements.entryconfigure(2, state=NORMAL)
    menu_traitements.entryconfigure(4, state=NORMAL)

def disable_traitements() :
    menu_traitements.entryconfigure(0, state=DISABLED)
    menu_traitements.entryconfigure(2, state=DISABLED)
    menu_traitements.entryconfigure(4, state=DISABLED)

menu_affichage = Menu(barre_menu, tearoff=0)
menu_affichage.add_command(label="Afficher la population choisie",command=parametres_affichage)
menu_affichage.add_separator()
menu_affichage.add_command(label="Trier les vins de la population",command=tri_affichage)
barre_menu.add_cascade(label="Affichage",menu=menu_affichage)

menu_exporter = Menu(barre_menu, tearoff=0)
menu_exporter.add_command(label="Exporter la population sélectionnée", command=exports)
barre_menu.add_cascade(label="Exporter", menu=menu_exporter)

def enable_all() :
    menu_select.entryconfigure(0, state=NORMAL)
    menu_select.entryconfigure(2, state=NORMAL)
    menu_select.entryconfigure(3, state=NORMAL)
    enable_traitements()
    menu_affichage.entryconfigure(0, state=NORMAL)
    menu_affichage.entryconfigure(2, state=NORMAL)
    menu_exporter.entryconfigure(0, state=NORMAL)

def disable_all() :
    menu_select.entryconfigure(0, state=DISABLED)
    menu_select.entryconfigure(2, state=DISABLED)
    menu_select.entryconfigure(3, state=DISABLED)
    disable_traitements()
    menu_affichage.entryconfigure(0, state=DISABLED)
    menu_affichage.entryconfigure(2, state=DISABLED)
    menu_exporter.entryconfigure(0, state=DISABLED)

fen.config(menu=barre_menu)

# https://www.developpez.net/forums/d1027062/autres-langages/python-zope/gui/tkinter/desactiver-commande-d-barre-menu/


## Mainloop

population = deepcopy(base_vins)

menu_principal()
fen.mainloop()
