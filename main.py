# main.py

class Main:
    def __init__(self):
        self.menu = Menu()  # Création de l'objet Menu dans la classe Main

    def run(self):
        # Appel de la méthode affichermMenu de l'objet Menu
        choix = self.menu.affichermMenu()
        if choix == 5:
            print("Fin du programme.")
            return
        # Vous pouvez ajouter d'autres traitements ici en fonction du choix

class Menu:
    def affichermMenu(self):
        print("Bienvenue sur notre application d'optimisation")
        print("=== Menu Principal ===")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Quitter")

        try:
            choix = int(input("Veuillez choisir une option (1-5) : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 5.")
            return None

        if choix == 1:
            print("Vous avez choisi l'Option 1.")
            return 1
        elif choix == 2:
            print("Vous avez choisi l'Option 2.")
            return 2
        elif choix == 3:
            print("Vous avez choisi l'Option 3.")
            return 3
        elif choix == 4:
            print("Vous avez choisi l'Option 4.")
            return 4
        elif choix == 5:
            print("Vous avez choisi de quitter.")
            return 5
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
            return None

if __name__ == "__main__":
    application = Main()
    application.run()