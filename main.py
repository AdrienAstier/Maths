# main.py

from gestionFichier import genererFichier
from gestionFichier import importationPlateau

def affichermMenu():
    print("Bienvenue sur notre application d'optimisation")
    print("=== Menu Principal ===")
    print("1 - Importer un plateau")
    print("2 - Générer un plateau")
    print("3 - Exécuter l'algorithme A*")
    print("4 - Comparer les algorithmes")
    print("5 - Quitter le logiciel")

    try:
        choix = int(input("Veuillez choisir une option (1-5) : "))
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
        return None

    if choix == 1:
        chemin = input("Saisissez le chemin du plateau à importer : ")
        plateau = importationPlateau(chemin)
        print(plateau)
    elif choix == 2:
        nomFichier = input("Veuillez renseigner un nom de fichier : ")
        plateau = input("")
        genererFichier(plateau, nomFichier)
        print("Le plateau a été généré avec succès dans le dossier 'plateaux_generes'")
        
    elif choix == 3:
        print("Résoudre un plateau")
    elif choix == 4:
        print("Comparer Algo")
    elif choix == 5:
        print("Vous avez choisi de quitter le logiciel")
        return
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        return None

if __name__ == "__main__":
    affichermMenu()