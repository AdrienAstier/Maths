# main.py

from gestionFichier import genererFichier
from gestionFichier import importationPlateau
from generationPlateau import genererPlateau

def affichermMenu():
    continuer = True
    while(continuer) :
        print("Bienvenue sur notre application d'optimisation")
        print("=== Menu Principal ===")
        print("1 - Importer un plateau")
        print("2 - Générer un plateau")
        print("3 - Exécuter l'algorithme A*")
        print("4 - Comparer les algorithmes")
        print("5 - Quitter le logiciel")

        plateau = None

        try:
            choix = int(input("Veuillez choisir une option (1-5) : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
            continuer = False

        if choix == 1:
            chemin = input("Saisissez le chemin du plateau à importer : ")
            plateau = importationPlateau(chemin)
        elif choix == 2:
            try :
                nomFichier = input("Veuillez renseigner un nom de fichier : ")
                longueur = int(input("Entrez un entier pour la longueur du plateau (longueur ligne) : "))
                largeur = int(input("Entrez un entier la largeur du plateau (nombre de ligne) : "))
                taux = float(input("Entrez un nombre flottant pour le taux de murs : "))
                coins = bool(input("Entrez un booléen, true ou false, pour placer les départs et arrivé dans les coins : "))

                plateauGenere = genererPlateau(longueur, largeur, taux, coins)
                genererFichier(plateauGenere, nomFichier)
                print("Le plateau a été généré avec succès dans le dossier 'plateaux_generes'")
            except ValueError:
                print("Entrée invalide. Mauvais type.")
                continuer = False
            
        elif choix == 3:
            print("Résoudre un plateau")
        elif choix == 4:
            print("Comparer Algo")
        elif choix == 5:
            print("Vous avez choisi de quitter le logiciel")
            continuer = False
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
            continuer = False

if __name__ == "__main__":
    affichermMenu()