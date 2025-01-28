# main.py



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
        print("1 - Importer un plateau")
        return 1
    elif choix == 2:
        print("2 - Générer un plateau")
        return 2
    elif choix == 3:
        print("Vous avez choisi l'Option 3.")
        return 3
    elif choix == 4:
        print("Vous avez choisi l'Option 4.")
        return 4
    elif choix == 5:
        print("Vous avez choisi de quitter.")
        return
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
        return None

if __name__ == "__main__":
    affichermMenu()