# Ce fichier liste les changements apportés à l'application
# Modifiez le quand vous ajoutez quelque-chose


# Liens des overleafs

Cahier des charges :  https://www.overleaf.com/14941843qjwkbwdxwcjs

Rapport :             https://www.overleaf.com/14940005vncwktrdjpwn

Présentation :        https://www.overleaf.com/16027254zkkgffdjzttd


# Rappel pour faire fonctionner l'application :

Vous pouvez télécharger le fichier Application v1.zip qui fonctionne directement (une fois dézippé bien sûr).

Dans un même répertoire, mettez le fichier Application.py, et des dossiers nommés Données, Modules et Images

Dans le fichier Application.py, il faut remplacer emplacement = 'D:\\Documents\\Application' par emplacement = os.getcwd() ou emplacement = 'le chemin où vous avec mis le programme et les dossiers'.

Le dossier Données doit contenir le fichier .json

Le dossier Modules doit contenir tous les autres programmes .py

Le dossier Images doit contenir une image logo.png

Vous pouvez exécuter directement le fichier Application.py avec python ou pythonw, sans passer par un éditeur de type Pyzo ou Spyder pour lancer l'application.


# 13/05 18:00 Nico

Normalement il n'y a plus aucun bugs. L'affichage a été légèrement amélioré (il y avait un léger problème sur la dernière page).

La possibilité d'exporter les vins choisis a été ajoutée.


# 13/05 02:30 Nico

Quasiment pas de changement à l'usage. J'ai mis tout le programme principal en classe (plus propre et plus pratique), et j'ai ajouté de la doc string partout. J'ai aussi enlevé quelques bouts inutiles par ci pa là. Maintentnant le code est super clean.

Les autres fonctionnalités ne sont pas encore intégrées, mais il n'y a plus de bug si on essaye de les lancer via le menu (il se passe juste rien pour l'instant).


# 12/05 15:30 Nico

Maintenant l'application a son logo.

On peut sélectionner les critères, les modifier éventuellement, puis revenir au menu principal ou afficher la population. Le menu de tri est fait, mais j'ai pas encore rempli les fonctions de tri (pour l'instant elles font juste pass).

Normalement il n'y a aucun bug, SAUF si vous touchez à une des fonctions des menus Traitements ou Exporter (les fonctions ne sont pas encore intégrées), ou si vous mettez des inputs incorrects dans les cases où c'est possible (par exemple dans les critères de variables quantitatives, ou le numéro de page dans l'affichage, j'ai pas encore mis de tests pour vérifier les inputs + messages d'erreurs).

Je vais ajouter les fonctions de Killian (tris, stat univariée, chi-deux, clustering) et les menus/écrans nécessaires avec et l'application sera terminée.


# 09/05 17:30 Nico

J'ai essayé de remplacer la plume de tkinter par autre chose en logo de fenêtre, mais pour l'instant ça marche pas.

La séléction d'une sous-population fonctionne bien, la navigation sur les variables à la souris n'est pas encore faite.

Quand on valide la sélection, on arrive sur un menu intermédiaire. J'ai pas encore ajouté les programmes de Killian (chi-deux, etc.) ; pour l'instant on peut juste afficher la sous-population sélectionnée via la barre de menu (pour l'instant je n'ai fait afficher que 3 variables, je vais ajouter un écran entre les deux pour que l'utilisateur puisser choisir quelles variables il veut afficher).

Pour l'affichage, il faut que j'ajoute des boutons de navigation pour faire défiler les lignes ou colonnes (pour l'instant ça dépasse un poil de la fenêtre ^^').
