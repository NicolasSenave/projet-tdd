# -*- coding: utf-8 -*-
"""
Application traitement de données
Module Stat_uni

Ce programme permet de lancer une analyse de statistique 
descriptive univariée.

@Auteurs :
Tanguy BARTHÉLÉMY, Killian POULAIN, Nicolas SÉNAVE
"""


from Population import *


class Univariee :
    """
    Cette classe définit un objet qui contient les informations d'une analyse 
    de statistique descriptive univariée.
    Les calculs sont effectués à la création d'une instance.
    La méthode resume permet de récupérer les résultats sous forme de paragraphe (str).
    """
    
    def __init__(self, population, variable) :
        """
        population est un objet de type Population.
        variable est un objet de type Variable.
        """
        #
        self.population = deepcopy(population)
        self.variable = variable
        
        if self.variable.type_variable == 'quanti' :
            #
            self.population.tri_croissant(variable.nom)
            self.valeurs = []
            for vin in self.population :
                self.valeurs.append( getattr(vin,variable.nom) )
            self.val_min_pop = self.valeurs[0]
            self.val_max_pop = self.valeurs[-1]
            #
            self.moyenne = self.calcul_moyenne()
            self.variance = self.calcul_variance()
            self.ecart_type = sqrt(self.variance)
            #
            self.mediane = self.calcul_mediane()
            self.quartile1 = self.calcul_quartile1()
            self.quartile3 = self.calcul_quartile3()
        
        else :
            #
            self.nb_occurences = self.calcul_nb_occurences()
            self.mode = self.calcul_mode()
            self.part_modalites = self.calcul_part_modalites()
    
    ## Méthodes pour une variable quantitative
    
    def calcul_moyenne(self):
        """
        Renvoie la moyenne de la population sur la variable étudiée.
        """
        res = 0
        for valeur in self.valeurs :
            res += valeur
        return res / self.population.nb_vins
    
    def calcul_variance(self) :
        """
        Renvoie la moyenne de la population sur la variable étudiée.
        """
        res = 0
        for valeur in self.valeurs :
            res += valeur**2              
        return res / self.population.nb_vins
    
    def calcul_mediane(self):
        """
        Renvoie la médiane de la population sur la variable étudiée.
        """
        nb_vins = self.population.nb_vins
        if nb_vins%2 == 0 :
            val1 = self.valeurs[nb_vins//2 - 1]
            val2 = self.valeurs[nb_vins//2]
            return (val1 + val2) / 2
        else :
            return self.valeurs[nb_vins//2]
    
    def calcul_quartile1(self):
        """
        Renvoie le premier quartile de la population sur la variable étudiée.
        """
        nb_vins = self.population.nb_vins
        if nb_vins%4 == 0 :
            return self.valeurs[nb_vins//4 - 1]
        else :
            return self.valeurs[nb_vins//4]
    
    def calcul_quartile3(self):
        """
        Renvoie le troisième quartile de la population sur la variable étudiée.
        """
        nb_vins = self.population.nb_vins
        if nb_vins%4 == 0 :
            return self.valeurs[3*(nb_vins//4) - 1]
        else :
            return self.valeurs[3*(nb_vins//4)]
    
    def boite_moustache(self) :
        """
        Construction de la boîte à moustache.
        """
        plt.boxplot(self.valeurs)
        plt.ylim(self.val_min_pop-1, self.val_max_pop+1)
        plt.savefig('D:/Documents/Application/Modules/Diagramme.png')
    
    ## Méthodes pour une variable qualitative
    
    def calcul_nb_occurences(self) :
        """
        Renvoie un dictionnaire dont les clés sont le nom des modalités de la variable 
        et les valeurs le nombre d'occurences de ces modalités au sein de la population.
        """
        res = {}
        for mod in self.variable.modalites :
            res[mod] = 0
        for vin in self.population :
            res[getattr(vin,self.variable.nom)] += 1
        return res
    
    def calcul_mode(self) :
        """
        Renvoie le mode de la variable étudiée sur la population.
        """
        nb_occur_max = 0
        for mod in self.nb_occurences :
            nb = self.nb_occurences[mod]
            if nb > nb_occur_max :
                res = mod
        return res
    
    def calcul_part_modalites(self) :
        """
        Nécessite l'initialisation préalable de self.nb_occurences.
        Renvoie un dictionnaire dont les clés sont le nom des modalités de la variable 
        et les valeurs la part de ces modalités au sein de la population.
        """
        res = {}
        for mod in self.nb_occurences :
            nb = self.nb_occurences[mod]
            res[mod] = nb / self.population.nb_vins
        return res
    
    def diagramme(self) :
        """
        Nécessite l'initialisation préalable de self.part_modalites.
        Construction du diagramme.
        """
        #
        sizes = []
        labels = []
        for mod in self.part_modalites :
            part = self.part_modalites[mod]
            sizes.append(part)
            labels.append(mod)
        colors = []
        nb_modalites = self.variable.nb_modalites
        for k in range(0,nb_modalites) :
            couleur = rgb_to_hex((0, 255 - k*255/nb_modalites, 0))
            colors.append(couleur)
        #
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.savefig('D:/Documents/Application/Modules/Diagramme.png')
    
    ## Résultats
    
    def resume(self) :
        """
        Renvoie un résumé des résultats (str).
        """
        
        msg = ""
        
        if self.variable.type_variable == 'quanti' :
            msg += "Moyenne : %s \n" %(round(self.moyenne,4))
            msg += "Variance : %s \n" %(round(self.variance,4))
            msg += "Écart-type : %s \n" %(round(self.ecart_type,4))
            msg += "\n"
            msg += "Minimum : %s \n" %(self.val_min_pop)
            msg += "Maximum : %s \n" %(self.val_max_pop)
            msg += "\n"
            msg += "1er quartile : %s \n" %(self.quartile1)
            msg += "Médiane : %s \n" %(self.mediane)
            msg += "3e quartile : %s \n" %(self.quartile3)
        
        else :
            msg += "Nombre d'occurences des modalités :\n"
            for mod in self.nb_occurences :
                msg += mod + " : %s \n" %(self.nb_occurences[mod])
            msg += "\n"
            msg += "Mode : " + self.mode
        
        return msg


class AffichageUnivariee :
    """
    Cette classe constitue le menu de statistique descriptive univariée.
    """
    
    fonction_chargement = None
    fonction_sortie = None
    
    def __init__(self, fen, population) :
        
        # Fenêtre
        self.fen = fen
        self.population = population
        self.bouton_retour = Button(fen, text="Retour au menu",font='Arial 12', command=self.fin)
        
        # Choix de la variable
        
        texte_indication = "Sélectionnez la variable à étudier.\n"
        texte_indication += "Validez avec la toucher Entrer, en double cliquant sur la variable souhaitée, \n"
        texte_indication += "ou en utilisant le bouton Valider.\n"
        self.indication = Label(fen, text=texte_indication,font='Arial 12',justify=LEFT, background='ivory')
        
        self.canvas_variables = Canvas(fen, background='ivory')
        self.labels_variables = []
        for nom_affiche in liste_noms_affiches_variables :
            label = Label(self.canvas_variables, text=nom_affiche, padx=50, font='Consolas 12', background='ivory')
            label.pack()
            self.labels_variables.append(label)
        self.canvas_variables.bind('<Key>',self.choix_variable)
        
        self.curseur = None
        self.variable_choisie = None
        
        self.bouton_valider = Button(fen, text="Valider",font='Arial 12',background='lightgreen', command=self.chargement)
        
        # Affichage des résultats
        
        self.uni = None
        
        self.texte_uni = StringVar()
        self.etiquette = Label(fen, textvariable=self.texte_uni,font='Arial 14',justify=LEFT, background='ivory')
        
        self.texte_resultats = StringVar()
        self.resultats = Label(fen, textvariable=self.texte_resultats,justify=LEFT, background='ivory')
    
    def menu_choix_variable(self) :
        """
        Affiche le menu de sélection de variable.
        """
        self.indication.pack()
        self.canvas_variables.pack()
        self.canvas_variables.focus_set()
        self.bouton_retour.pack(side=BOTTOM)
        self.bouton_valider.pack(side=BOTTOM)
    
    def choix_variable(self,evenement) :
        """
        Déplace le curseur suite à un input de l'utilisateur.
        """
        
        touche = evenement.keysym
        
        if touche == "Down" :
            
            if self.curseur == None :
                self.curseur = 0
                self.labels_variables[0].configure(background='lightblue')
            elif self.curseur < nb_variables - 1 :
                self.labels_variables[self.curseur].configure(background='ivory')
                self.curseur += 1
                self.labels_variables[self.curseur].configure(background='lightblue')
            
            elif self.curseur == nb_variables - 1 :
                self.labels_variables[nb_variables - 1].configure(background='ivory')
                self.curseur = 0
                self.labels_variables[0].configure(background='lightblue')
        
        elif touche == "Up" :
            
            if self.curseur == None :
                self.curseur = nb_variables - 1
                self.labels_variables[nb_variables - 1].configure(background='lightblue')
            elif self.curseur > 0 :
                self.labels_variables[self.curseur].configure(background='ivory')
                self.curseur -= 1
                self.labels_variables[self.curseur].configure(background='lightblue')
            
            elif self.curseur == 0 :
                self.labels_variables[0].configure(background='ivory')
                self.curseur = nb_variables - 1
                self.labels_variables[nb_variables - 1].configure(background='lightblue')
        
        elif touche == "Return" :
            if self.curseur != None :
                self.chargement()
    
    def chargement(self) :
        """
        Lance l'écran de chargement dans l'application.
        """
        #
        self.indication.forget()
        self.canvas_variables.forget()
        self.bouton_valider.forget()
        self.bouton_retour.forget()
        #
        AffichageUnivariee.fonction_chargement()
    
    def calculs(self) :
        """
        Effectue les calculs de statistique univariée sur la population 
        avec la variable choisie.
        """
        variable_choisie = liste_variables[self.curseur]
        self.uni = Univariee(self.population, variable_choisie)
    
    def affichage_resultats(self) :
        """
        Affiche les résultats.
        """
        #
        titre = "Analyse de statistique descriptive univariée \n"
        titre += "sur la population sélectionnée \n"
        titre += "pour la variable " + self.uni.variable.nom_affiche + "\n"
        self.texte_uni.set(titre)
        #
        resultats = self.uni.resume()
        self.texte_resultats.set(resultats)
        #
        self.etiquette.pack()
        self.resultats.pack()
        self.bouton_retour.pack(side=BOTTOM)
        #
        if self.uni.variable.type_variable == 'quanti' :
            self.uni.boite_moustache()
        else :
            self.uni.diagramme()
    
    def fin(self) :
        """
        Désaffiche l'écran de statistique univariée,
        et renvoie au menu de sélection des opérations.
        """
        #
        self.indication.forget()
        self.canvas_variables.forget()
        self.bouton_valider.forget()
        #
        self.etiquette.forget()
        self.resultats.forget()
        #
        self.bouton_retour.forget()
        #
        AffichageUnivariee.fonction_sortie()
