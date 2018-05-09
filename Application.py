"""
Application traitement de données

Programme principal
Ce script lance l'application et assure la gestion des menus, 
qui permettent à l'utilisateur de naviguer dans les différentes fonctionnalités.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


## Import des modules

import os

#emplacement = os.getcwd()
emplacement = 'D:\\Documents\\Application'
emplacement_modules = emplacement + '\\Modules'
os.chdir(emplacement_modules)

from Population import *
# Population contient Selection, qui contient lui-même Vins

from Affichage import *

from Stat_uni import *
from Test_chi_deux import *
from Clustering import *

from Exports import *


## Définition de la fenetre principale

from tkinter import *

fen = Tk()
fen.title("Application")
fen.geometry("800x500+100+100")
fen.configure(bg='ivory')

emplacement_images = emplacement + '\\Images'
os.chdir(emplacement_images)
#logo = PhotoImage(file='logo.png')
#fen.call('wm', 'iconphoto', fen._w, logo)
fen.wm_iconbitmap(bitmap = 'logo.png')


## Menu principal

#etiquette_menu = PanedWindow(fen, orient=HORIZONTAL)
#width=30,height=10,bg='lightblue',

texte_titre = "Projet traitement de données\nEnsai - 1ère année"
label_titre = Label(fen, text=texte_titre, background='lightblue',font='Arial 24')

texte_noms = "Tanguy Barthélémy, Killian Poullain, Nicolas Sénave"
label_noms = Label(fen, text=texte_noms, background='lightblue',font='Arial 18')

def menu_principal() :
    """
    Affiche le menu principal
    """
    reinit_ecran()
    #
    label_titre.pack(expand=True,fill=BOTH)
    label_noms.pack(expand=True,fill=BOTH)

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
# NB : en vrai désafficher tous les objets de l'écran à n'importe quel moment 
# c'est pas simplbe du tout
# On va peut être laisser tomber cette fonction en la transformant en 
# menu_pricipal_fin
# et n'afficher la barre de menus qu'au menu principal ;
# on utilisera des boutons ou autre dans le reste de l'application


## Menu intermédiaire
# On ajoutera des boutons du type "retour menu principal" etc.

texte_population = StringVar()
label_population = Label(fen,textvariable=texte_population, background='ivory',font='Arial 12')

texte_indication = "Utilisez le menu pour sélectionner l'opération souhaitée."
label_indication = Label(fen,text=texte_indication, background='ivory',font='Arial 10')

def menu_intermediaire(population) :
    resume = "La population séléctionnée contient %s vins." %(population.nb_vins)
    texte_population.set(resume)
    label_population.pack(expand=True,fill=BOTH)
    label_indication.pack(expand=True,fill=BOTH)
    

## Ecran de chargement

etiquette_chargement = Label(fen,text="Calcul en cours...",background='ivory',font='Arial 10')

def ecran_chargement() :
    etiquette_chargement.pack(expand=True,fill=BOTH)

def fin_chargement() :
    etiquette_chargement.forget()


## Fonctionnalité : Séléction des critères

def selection() :
    """
    Fonction "Séléctionner une sous-population" du menu
    """
    reinit_ecran()
    #
    Selection.fonction_sortie = selection_fin
    Selection(fen).__main__()

def modif_criteres() :
    """
    Si des critères on déjà été validés,
    permet de revenir à l'écran de sélection des critères
    Sinon, affiche un popup d'erreur
    """
    print("coucou modif criteres")

def selection_fin() :
    """
    Fonction lancée après validation des critères
    """
    #
    print("coucou selection terminée")
    ecran_chargement()
    fen.update()
    population.appliquer_criteres()
    fin_chargement()
    print(len(population.vins))
    #
    menu_intermediaire(population)


## Fonctionnalité : Affichage d'une liste de vins

def affichage() :
    """
    Lance l'affichage de la population sélectionnée
    """
    reinit_ecran()
    #
    global population
    AffichagePopulation.fonction_sortie = affichage_fin()
    AffichagePopulation(fen,population,variables_test).__main__()

def tri_affichage() :
    """
    Lance la procédure de tri selon une variable
    """
    print("coucou tri affichage")

def affichage_fin() :
    print("coucou affichage fin")


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
    Fonction "Exporter la population sélectionnée en .csv" du menu
    """
    print("coucou exports")
    

## Barre des menus

barre_menu = Menu(fen)

menu_select = Menu(barre_menu, tearoff=0)
menu_select.add_command(label="Sélectionner une sous-population", command=selection)
menu_select.add_separator()
menu_select.add_command(label="Modifier les criètres de sélection", command=modif_criteres)
barre_menu.add_cascade(label="Sélection", menu=menu_select)

menu_traitements = Menu(barre_menu, tearoff=0)
menu_traitements.add_command(label="Lancer une analyse descriptive",command=stat_uni)
menu_traitements.add_command(label="Lancer un test d'indépendance",command=test_chi_deux)
menu_traitements.add_command(label="Regrouper les vins en classes",command=clustering)
barre_menu.add_cascade(label="Traitements",menu=menu_traitements)

menu_affichage = Menu(barre_menu, tearoff=0)
menu_affichage.add_command(label="Afficher la sous-population en cours",command=affichage)
menu_affichage.add_command(label="Trier",command=tri_affichage)
barre_menu.add_cascade(label="Affichage",menu=menu_affichage)

menu_exporter = Menu(barre_menu, tearoff=0)
menu_exporter.add_command(label="Exporter la population sélectionnée en .csv", command=exports)
barre_menu.add_cascade(label="Exporter", menu=menu_exporter)

fen.config(menu=barre_menu)


## Mainloop

population = deepcopy(base_vins)

menu_principal()
fen.mainloop()
