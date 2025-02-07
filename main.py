# 
# main.py                                           28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

# En rapport avec l'algorithme
from algorithmeAEtoile import AlgorithmeAEtoile
import heuristiques

from gestionFichier import genererFichier
from gestionFichier import importationPlateau
from generationPlateau import genererPlateau

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
            elif not plateau.estValide():
                print("Le plateau est invalide est n'a donc pas pu être importé.")
                chemin_plateau = "N/A"
            
        elif choix == 2:
            afficherMenuGeneration(True)
            
        elif choix == 3:
            afficherMenuResolution(plateau)
            
        elif choix == 4:
            afficherMenuComparaison()
            
        elif choix == 5:
            print("Vous avez choisi de quitter le logiciel")
            continuer = False
            
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")

#
# Affiche le menu de génération de plateaux.
#
# aExporter : True pour que le fichier soit exporté dans le dossier
#             plateaux_generes, sinon False
# Retourne le plateau généré
#
def afficherMenuGeneration(aExporter: bool):
    
    try:
        
        if aExporter:
            nomFichier = input("\nVeuillez renseigner le nom du fichier "
                             + "à enregistrer => ")
        
        # Variables à vérifier
        longueur = ""
        largeur = ""
        taux= ""
        coins = ""
        
        # Demande des variables à l'utilisateur.
        
        longueurOK = False
        while not longueurOK:
            longueur = input("Entrez un entier pour la longueur du plateau (longueur des lignes >= 3) => ")
            longueurOK = longueur.isnumeric() and int(longueur) >= 3
            if not longueurOK:
                print("L'entier rentré est invalide, il doit supérieur ou égal à 3\n")
        longueur = int(longueur)
        
        largeurOK = False
        while not largeurOK:
            largeur = input("Entrez un entier pour la largeur du plateau (nombre de lignes >= 3) => ")
            largeurOK = largeur.isnumeric() and int(largeur) >= 3
            if not largeurOK:
                print("L'entier rentré est invalide, il doit supérieur ou égal à 3\n")
        largeur = int(largeur)
        
        tauxOK = False
        while not tauxOK:
            taux = input("Entrez un nombre entre 0 et 1 pour le taux de murs (ex : 0.2) => ")
            tauxOK = taux.replace('.', '', 1) and float(taux) >= .0 and float(taux) <= 1.0
            if not tauxOK:
                print("Le flottant rentré est invalide, ou n'est pas inclut entre 0 et 1\n")
        taux = float(taux)
        
        coinsOK = False
        while not coinsOK:
            coins = input("Entrez 'oui', pour placer le départ et l'arrivé dans les coins, sinon 'non' => ")
            coinsOK = coins == "oui" or coins == "non" 
            if not coinsOK:
                print("La réponse doit s'agir de 'oui' ou 'non'\n") 
        coins = coins == "oui"

        plateauGenere = genererPlateau(longueur, largeur, taux, coins)
        
        if aExporter:
            genererFichier(plateauGenere, nomFichier)
            print("\nLe plateau a été généré avec succès dans le dossier 'plateaux_generes' avec le nom '" + nomFichier + ".txt'")
        
        # Pour qu'il soit utilisé dans d'autres menu.
        return plateauGenere
    
    except ValueError:
        print("Entrée invalide. Mauvais type.")

#
# Affiche le menu de génération de plateaux.
#
def afficherMenuResolution(plateau):
    
    reponse = ""
    questionOK = False;
    while not questionOK:
        reponse = input("Rentrez '1' pour résoudre le plateau importé, '2' pour résoudre un plateau généré => ")
        questionOK = reponse == "1" or reponse == "2"
        if not questionOK:
            print("La réponse doit être '1' ou '2'\n")
    
    if reponse == "1":
        
        if plateau != None:
            resoudrePlateau(plateau)
        else:
            print("\nVeuillez importer un plateau avant d'utiliser cette option.\n")
    else:
        resoudrePlateau(afficherMenuGeneration(False))
   
#
# Affiche le menu de comparaison algorithmique.
#
def afficherMenuComparaison():
    # TODO menu
    print("Comparer algorithmes")

#
# Résout un plateau donné et donne le résultat
# dans un message.
#
def resoudrePlateau(plateau):
    
    instanceAStar = AlgorithmeAEtoile(plateau, heuristiques.heuristiqueVille)
    
    print("\nPlateau à résoudre : \n")
    print(plateau)
    print("Validité du plateau : " + str(plateau.estValide()))
    
    print("\nRésolution du plateau avec A* (par distance de Manhattan) : \n")
    try:
        instanceAStar.executionAlgo()
        print(instanceAStar.plateauParcouru)
    except Exception:
        print("Le chemin entre 'D' et 'A' est impossible !\n")

# Lance le menu principal
if __name__ == "__main__":
    afficherMenuPrincipal()