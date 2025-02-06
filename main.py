# 
# main.py                                           28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

from gestionFichier import genererFichier
from gestionFichier import importationPlateau
from generationPlateau import genererPlateau

# TODO tourner le menu en boucle même en cas d'erreur

#
# Lance le menu principal avec toutes
# les options associées.
#
def afficherMenuPrincipal():

    print("\nBienvenue sur notre application d'optimisation sur le parcours des graphes !\n")

    # Plateau importé
    plateau = None
    chemin_plateau = "N/A"

    continuer = True
    while(continuer) :
        
        print("\n=== Menu Principal ===")
        print("1 - Importer un plateau")
        print("2 - Générer un plateau")
        print("3 - Exécuter l'algorithme A*")
        print("4 - Comparer les algorithmes")
        print("5 - Quitter le logiciel\n")
        
        print("Plateau importé : " + chemin_plateau)

        try:
            choix = int(input("\nVeuillez choisir une option (1-5) : "))
        except ValueError:
            choix = -1

        if choix == 1:
            
            chemin_plateau = input("Saisissez le chemin du plateau à importer : ")
            plateau = importationPlateau(chemin_plateau)
            
            if plateau == None:
                chemin_plateau = "N/A"
            
        elif choix == 2:
            afficherMenuGeneration()
            
        elif choix == 3:
            afficherMenuResolution()
            
        elif choix == 4:
            afficherMenuComparaison()
            
        elif choix == 5:
            print("Vous avez choisi de quitter le logiciel")
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

#
# Affiche le menu de génération de plateaux.
#
def afficherMenuGeneration():
    
    # TODO éventuellement faire une option pour résoudre après génération le plateau.
    
    try:
        nomFichier = input("Veuillez renseigner le nom du fichier à enregistrer : ")
        longueur = int(input("Entrez un entier pour la longueur du plateau (longueur des lignes) : "))
        largeur = int(input("Entrez un entier la largeur du plateau (nombre de lignes) : "))
        taux = float(input("Entrez un nombre flottant entre 0 et 1 pour le taux de murs : "))
        coins = bool(input("Entrez un booléen, true ou false, pour placer les départs et arrivé dans les coins : "))

        plateauGenere = genererPlateau(longueur, largeur, taux, coins)
        genererFichier(plateauGenere, nomFichier)
        print("Le plateau a été généré avec succès dans le dossier 'plateaux_generes'")
    
    except ValueError:
        print("Entrée invalide. Mauvais type.")

#
# Affiche le menu de génération de plateaux.
#
def afficherMenuResolution():
    # TODO menu
    print("Résoudre un plateau")
   
#
# Affiche le menu de comparaison algorithmique.
#
def afficherMenuComparaison():
    # TODO menu
    print("Comparer algorithmes")

# Lance le menu principal
if __name__ == "__main__":
    afficherMenuPrincipal()