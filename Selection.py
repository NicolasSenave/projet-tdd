"""
Application traitement de données
Module Data

Ce programme gère le menu de séléction des critères.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""

from tkinter import *

from Vins import *
from copy import deepcopy


class Variable :
    """
    Cette classe définit un objet abstrait de variable, 
    caractérisée par son nom.
    La variable peut être qualitative ou quantitative.
    L'objet contient des informations sur la variable,
    ainsi que les critères appliqués sur cette variable.
    """
    
    def type_variable(nom_variable) :
        """
        Méthode statique de la classe Variable
        Renvoie 'quanti' si la variable est quantitative
        renvoie 'quali' si la variable est qualitaive
        """
        if type( getattr(base_vins_objets[0],nom_variable) ) == str :
            return 'quali'
        else :
            return 'quanti'
    
    def valeur_min(nom_variable) :
        """
        Méthode statique de la classe Variable
        Entrée : le nom d'une variable quantitative (str)
        Renvoie la valeur la plus faible sur la variable donnée
        """
        val_min = getattr(base_vins_objets[0],nom_variable)
        for vin in base_vins_objets :
            val = getattr(vin,nom_variable)
            if val < val_min :
                val_min = val
        return val_min
    
    def valeur_max(nom_variable) :
        """
        Méthode statique de la classe Variable
        Entrée : le nom d'une variable quantitative (str)
        Renvoie la valeur la plus faible sur la variable donnée
        """
        val_max = getattr(base_vins_objets[0],nom_variable)
        for vin in base_vins_objets :
            val = getattr(vin,nom_variable)
            if val > val_max :
                val_max = val
        return val_max
    
    def liste_modalites(nom_variable) :
        res = []
        for vin in base_vins_objets :
            mod = getattr(vin,nom_variable)
            if mod not in res :
                res.append(mod)
        return res
    
    def __init__(self,nom_variable) :
        #
        self.nom = nom_variable
        #
        self.nom_affiche = dico_noms_affiches[nom_variable]
        #
        self.type_variable = Variable.type_variable(nom_variable)
        #
        if self.type_variable == 'quanti' :
            self.val_min = Variable.valeur_min(nom_variable)
            self.val_max = Variable.valeur_max(nom_variable)
            self.critere_min = self.val_min
            self.critere_max = self.val_max
        else :
            self.modalites = Variable.liste_modalites(nom_variable)
            self.critere_modalites = deepcopy(self.modalites)
    
    def __repr__(self) :
        return "Variable " + self.nom
    
    def __eq__(self,variable) :
        return self.nom == variable.nom
    
    def copie(self) :
        """
        Renvoie une copie de la variable dans un nouvel objet
        """
        return Variable(self.nom)

liste_variables = [Variable(nom) for nom in liste_noms_variables]


class AffichageVar :
    """
    Contient un canvas définit dans frame_selection 
    et des labels et lignes de saisie définis dans ce canvas 
    permettant d'afficher et de modifier les critères appliqués sur une 
    variable quantitative.
    
    Contient un canvas définit dans frame_selection 
    et des labels et lignes de saisie définis dans ce canvas 
    permettant d'afficher et de modifier les critères appliqués sur une 
    variable qualitative.
    """
    
    def __init__(self,variable,canvas) :
        #
        self.variable = variable
        #
        self.cadre = canvas
        #
        if variable.type_variable == 'quanti' :
            texte = "Les valeurs pour cette variable dans la base\n"
            texte += "sont comprises entre "
            texte += "%s et %s.\n" %(variable.val_min,variable.val_max)
            self.label = Label(self.cadre,text=texte, background='ivory')
            #
            texte_par_defaut = "Pas de critères séléctionnés pour cette variable."
            self.texte_critere = StringVar()
            self.texte_critere.set(texte_par_defaut)
            self.label_critere = Label(self.cadre,textvariable=self.texte_critere, background='ivory')
            #
            texte_min = "Borne inférieure :"
            self.label_min = Label(self.cadre,text=texte_min, background='ivory')
            self.entree_min = Entry(self.cadre,width=5,font='Arial 12')
            self.entree_min.bind('<Return>',self.appliquer_critere_min)
            texte_max = "Borne supérieure :"
            self.label_max = Label(self.cadre,text=texte_max, background='ivory')
            self.entree_max = Entry(self.cadre,width=5,font='Arial 12')
            self.entree_max.bind('<Return>',self.appliquer_critere_max)
            #
            texte_aide = "\nSi vous naviguez au clavier, utilisez la touche Tabulation\n"
            texte_aide += "pour revenir aux choix de la variable après avoir entré une valeur."
            self.label_aide = Label(self.cadre,text=texte_aide, background='ivory',justify=LEFT)
        else :
            self.cases_modalites = []
            self.vars_modalites = {}
            for mod in variable.modalites :
                var = IntVar()
                case = Checkbutton(self.cadre, text=mod, variable=var, background='ivory')
                # Par défaut la modalité est sélectionnée
                case.select()
                self.cases_modalites.append( case )
                self.vars_modalites[mod] = var
    
    def afficher(self) :
        if self.variable.type_variable == 'quanti' :
            self.label.pack()
            self.label_critere.pack()
            self.label_min.pack()
            self.entree_min.pack()
            self.label_max.pack()
            self.entree_max.pack()
            self.label_aide.pack()
        else :
            for case in self.cases_modalites :
                case.pack()
    
    def cacher(self) :
        if self.variable.type_variable == 'quanti' :
            self.label.forget()
            self.label_critere.forget()
            self.label_min.forget()
            self.entree_min.forget()
            self.label_max.forget()
            self.entree_max.forget()
            self.label_aide.forget()
        else :
            for case in self.cases_modalites :
                case.forget()
    
    def appliquer_critere_min(self,evenement=None) :
        self.variable.critere_min = float(self.entree_min.get())
        # Ici insérer un pop_up d'erreur
        # si l'utilisateur rentre autre chose qu'un nombre
        # Insérer ausi un test pour vérifier que le min est plus petit que le max
        self.entree_min.delete(0,END)
        self.actualiser_critere_quanti()
    
    def appliquer_critere_max(self,evenement=None) :
        self.variable.critere_max = float(self.entree_max.get())
        # idem cf appliquer_critere_min
        self.entree_max.delete(0,END)
        self.actualiser_critere_quanti()
    
    def actualiser_critere_quanti(self,evenement=None) :
        borne_inf = self.variable.critere_min
        borne_sup = self.variable.critere_max
        texte_critere = "Intervalle des valeurs retenues pour cette variable :\n"
        texte_critere += "[ %s , %s ]" %(borne_inf,borne_sup)
        self.texte_critere.set(texte_critere)
        self.label_critere.update()
        


class Selection :
    
    # Variables statiques utilisée dans le programme corps
    
    fonction_sortie = None
    
    # Variables et méthodes statiques utilisées dans le constructeur :
    
    texte_selection = "Cliquez avec la souris ou utilisez les flèches du clavier "
    texte_selection += "pour voir les critères appliqués sur les variables.\n"
    texte_selection += "Double-cliquez ou appuyer sur Entrer pour modifier les "
    texte_selection += "critères sur la variable choisie.\n\n"
    
    def labels_variables(can) :
        """
        Méthode statique de la classe Selection
        Crée les labels de la liste des variables du menu de sélection
        et pack ces labels dans le canvas en entrée
        Renvoie les labels créés dans un dictionnaire 
        dont les clés sont les noms des variables
        """
        res = {}
        for variable in liste_variables :
            label = Label(can, text=variable.nom_affiche, padx=50, font='Consolas 12', background='ivory')
            label.pack()
            res[variable.nom] = label
        return res
    
    def objets_criteres(can) :
        """
        Méthode statique de la classe Selection
        Crée les AffichageVar permettant d'afficher et de modifier les critères 
        appliqués sur les variables 
        et affiche ces objets dans le canvas en entrée
        Renvoie les objets créés dans un dictionnaire 
        dont les clés sont les noms des variables
        """
        res = {}
        for variable in liste_variables :
            objet = AffichageVar(variable,can)
            res[variable.nom] = objet
        return res
    
    def __init__(self,fen) :
        #
        self.etiquette = Label(fen, text=Selection.texte_selection,font='Arial 12',bg='ivory',justify=LEFT)
        #
        self.canvas_variables = Canvas(fen, background='ivory')
        self.variables = Selection.labels_variables(self.canvas_variables)
        #
        self.curseur = None
        self.variable_affichee = None
        self.canvas_variables.bind('<Key>',self.choisir_variable)
        #
        self.canvas_criteres = Canvas(fen, height =30,width=30, bg='ivory')
        self.criteres = Selection.objets_criteres(self.canvas_criteres)
        #
        self.bouton_valider = Button(fen, text="Valider les critères",font='Arial 12',bg='lightgreen',command=self.fin)
    
    def choisir_variable(self,evenement) :
        
        touche = evenement.keysym
        
        if touche == "Down" :
            if self.curseur == None :
                self.curseur = 0
            elif self.curseur < nb_variables - 1 :
                self.curseur += 1
            elif self.curseur == nb_variables - 1 :
                self.curseur = 0
            self.afficher_criteres_variable()
        
        elif touche == "Up" :
            if self.curseur == None :
                self.curseur = nb_variables - 1
            elif self.curseur > 0 :
                self.curseur -= 1
            elif self.curseur == 0 :
                self.curseur = nb_variables - 1
            self.afficher_criteres_variable()
        
        elif touche == "Return" :
            Selection.fonction_sortie()
    
    def afficher_criteres_variable(self) :
        self.variable_affichee = liste_variables[self.curseur].copie()
        #
        for variable in liste_variables :
            if variable != self.variable_affichee :
                self.variables[variable.nom].configure(background='ivory')
                self.criteres[variable.nom].cacher()
        #
        self.variables[self.variable_affichee.nom].configure(background='lightblue')
        self.criteres[self.variable_affichee.nom].afficher()
        self.canvas_criteres.pack(side=TOP)
    
    def appliquer_criteres_quali(self) :
        """
        Cette méthode est appelée dans la méthode fin de cette classe,
        elle modifie l'attribut critere_modalites de chaque Variable 
        de liste_variables
        Si la case correspondant à la modalité est cochée, elle est conservée 
        dans critere_modalites, sinon elle est retirée.
        """
        for nom_variable in self.criteres :
            obj = self.criteres[nom_variable]
            if obj.variable.type_variable == 'quali' :
                for mod in obj.vars_modalites :
                    var = obj.vars_modalites[mod]
                    if var.get() == 0 :
                        obj.variable.critere_modalites.remove(mod)
    
    def __main__(self) :
        self.etiquette.pack(side=TOP,fill=Y)
        self.canvas_variables.pack(side=LEFT)
        self.canvas_variables.focus_set()
        self.canvas_criteres.pack(side=TOP)
        self.bouton_valider.pack(side=BOTTOM)
    
    def fin(self) :
        #
        self.appliquer_criteres_quali()
        #
        self.etiquette.forget()
        self.canvas_variables.forget()
        self.canvas_criteres.forget()
        self.bouton_valider.forget()
        Selection.fonction_sortie()
