# 
# main.py                                           28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

# En rapport avec l'algorithme
from algorithmeAEtoile import AlgorithmeAEtoile
import heuristiques

from comparaison import calculComparaisons
from comparaison import comparaisonHeuristiques

from gestionFichier import genererFichier
from gestionFichier import importationPlateau
from generationPlateau import genererPlateau

#
# Lance le menu principal avec toutes
# les options associées.
#
def afficherMenuPrincipal():

    print("\nBienvenue sur notre application d'optimisation sur le parcours des graphes !\n")

    # Chemins des dossiers pour l'exportation
    cheminDossierExportation = "plateaux_generes/"
    cheminDossierResolution = "plateaux_resolus/"

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
                        
            chemin_plateau_candidat = input("Saisissez le chemin du plateau à importer : ")
            plateau_candidat = importationPlateau(chemin_plateau_candidat)
            
            if plateau_candidat == None or not plateau_candidat.estValide():
                print("Le plateau est invalide est n'a donc pas pu être importé.")
            else: # Cas nominal
                chemin_plateau = chemin_plateau_candidat
                plateau = plateau_candidat
            
        elif choix == 2:
            afficherMenuGeneration(True, cheminDossierExportation)
            
        elif choix == 3:
            afficherMenuResolution(plateau, cheminDossierResolution)
            
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
#             plateaux_generes, sinon False.
# cheminDossierExportation : chemin du fichier en cas d'exportation.
# Retourne le plateau généré
#
def afficherMenuGeneration(aExporter: bool, cheminDossierExportation: str):
        
    if aExporter:
        nomFichier = input("\nVeuillez renseigner le nom du fichier "
                         + "à enregistrer => ")
        
    # Demande des variables à l'utilisateur.
        
    longueurOK = False
    while not longueurOK:
        longueur = input("Entrez un entier pour la longueur du plateau (nombre de colonnes >= 3) => ")
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
        tauxOK = taux.replace('.', '', 1).isnumeric() and float(taux) >= .0 and float(taux) <= 1.0
        if not tauxOK:
            print("Le flottant rentré est invalide, ou n'est pas inclut entre 0 et 1\n")
    taux = float(taux)
        
    coinsOK = False
    while not coinsOK:
        coins = input("Entrez 'oui' pour placer le départ et l'arrivé dans les coins, sinon 'non' => ")
        coinsOK = coins == "oui" or coins == "non" 
    if not coinsOK:
        print("La réponse doit s'agir de 'oui' ou 'non'\n") 
    coins = coins == "oui"

    plateauGenere = genererPlateau(longueur, largeur, taux, coins)
        
    if aExporter:
        genererFichier(plateauGenere, cheminDossierExportation, nomFichier)
        print("\nLe plateau a été généré avec succès dans le dossier '" 
              + cheminDossierExportation + "' avec le nom '" + nomFichier + ".txt'")
        
    # Pour qu'il soit utilisé dans d'autres menu.
    return plateauGenere

#
# Affiche le menu de génération de plateaux.
#
# plateau : le plateau à résoudre, généralement celui importé.
# cheminDossierResolution : dossier d'exportation du plateau résolu.
#
def afficherMenuResolution(plateau, cheminDossierResolution):
    
    reponse = ""
    questionOK = False;
    while not questionOK:
        reponse = input("Rentrez '1' pour résoudre le plateau importé, '2' pour résoudre un plateau généré => ")
        questionOK = reponse == "1" or reponse == "2"
        if not questionOK:
            print("La réponse doit être '1' ou '2'\n")
    
    if reponse == "1":
        
        if plateau != None:
            resoudrePlateau(plateau, cheminDossierResolution)
        else:
            print("\nVeuillez importer un plateau avant d'utiliser cette option.\n")
    else:
        resoudrePlateau(afficherMenuGeneration(False, ""), cheminDossierResolution)
   
#
# Affiche le menu de comparaison algorithmique.
#
def afficherMenuComparaison():
        
    # Demande des variables à l'utilisateur.
        
    longueurOK = False
    while not longueurOK:
        longueur = input("Entrez un entier pour la longueur du plateau (nombre de colonnes >= 3) => ")
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
    
    # Gestion des bornes du taux.
    tauxMinInfMax = False
    while not tauxMinInfMax:
        
        tauxMinOK = False
        while not tauxMinOK:
            tauxMin = input("Entrez un nombre entre 0 et 1 (non inclus) pour la borne inférieure de taux de murs testés (ex : 0.2) => ")
            tauxMinOK = tauxMin.replace('.', '', 1).isnumeric() and float(tauxMin) >= .0 and float(tauxMin) < 1.0
            if not tauxMinOK:
                print("Le flottant rentré est invalide, ou n'est pas inclut entre 0 et 1\n")
        tauxMin = float(tauxMin)
        
        tauxMaxOK = False
        while not tauxMaxOK:
            tauxMax = input("Entrez un nombre entre 0 et 1 (non inclus) pour la borne supérieure de taux de murs testés (ex : 0.5) => ")
            tauxMaxOK = tauxMax.replace('.', '', 1).isnumeric() and float(tauxMax) >= .0 and float(tauxMax) < 1.0
            if not tauxMaxOK:
                print("Le flottant rentré est invalide, ou n'est pas inclut entre 0 et 1\n")
        tauxMax = float(tauxMax)
        
        tauxMinInfMax = tauxMin < tauxMax
        if not tauxMinInfMax:
            print("La borne inférieure du taux n'est pas inférieure à la borne supérieure. Veuillez recommencer\n")
    
    nbrPlateauxOK = False
    while not nbrPlateauxOK:
        nbrPlateaux = input("Entrez le nombre de plateaux sur lequel la moyenne sera obtenu (nombre de plateaux > 0) => ")
        nbrPlateauxOK = nbrPlateaux.isnumeric() and int(nbrPlateaux) > 0
        if not nbrPlateauxOK:
            print("L'entier rentré est invalide, il doit être supérieur à 0 \n")
    nbrPlateaux = int(nbrPlateaux)
    
    precisionOK = False
    while not precisionOK:
        precision = input("Entrez le pas de la comparaison (en pourcentage, ex: 1 pour 1%) => ")
        precisionOK = precision.replace('.', '', 1).isnumeric() and float(precision) > 0 and float(precision) < 100
        if not precisionOK:
            print("Le flottant rentré est invalide, ou n'est pas inclut entre 0 et 100\n")
    precision = 100 / float(precision)
    
    coinsOK = False
    while not coinsOK:
        coins = input("Entrez 'oui' pour placer le départ et l'arrivé dans les coins, sinon 'non' => ")
        coinsOK = coins == "oui" or coins == "non" 
    if not coinsOK:
        print("La réponse doit s'agir de 'oui' ou 'non'\n") 
    coins = coins == "oui"
    
    # Début de la comparaison
    
    (dijkstra, oiseau, ville, taux) = calculComparaisons(largeur, longueur, tauxMin, tauxMax, coins, nbrPlateaux, precision)
    comparaisonHeuristiques(dijkstra, ville, oiseau, taux, "Dijkstra", "Ville", "Oiseau", longueur, largeur, nbrPlateaux)

#
# Résout un plateau donné et donne le résultat
# dans un message.
#
# plateau : le plateau à résoudre, généralement celui importé.
# cheminDossierResolution : dossier d'exportation du plateau résolu.
#
def resoudrePlateau(plateau, cheminDossierResolution):
    
    estResolu = False
    instanceAStar = AlgorithmeAEtoile(plateau, heuristiques.heuristiqueVille)
    
    print("\nPlateau à résoudre : \n")
    print(plateau)
    print("Validité du plateau : " + str(plateau.estValide()))
    
    # Résolution du plateau
    print("\nRésolution du plateau avec A* (par distance de Manhattan) : \n")
    try:
        instanceAStar.executionAlgo()
        print(instanceAStar.plateauParcouru)
        estResolu = True
        
    except Exception:
        print("Le chemin entre 'D' et 'A' est impossible !\n")
    
    # Exportation du fichier demandé
    reponseExportation = ""
    if estResolu:
        print("Voulez-vous exporter le plateau résolu dans le dossier '" 
             + cheminDossierResolution + "' ?")
             
        exportationOK = False
        while not exportationOK:
            reponseExportation = input("'oui' pour l'exporter, 'non' sinon => ")
            exportationOK = reponseExportation == "oui" or reponseExportation == "non"
            if not exportationOK:
                print("La réponse doit s'agir de 'oui' ou 'non'\n") 
                
    if reponseExportation == "oui":
        nomFichier = input("\nVeuillez renseigner le nom du fichier "
                         + "à enregistrer => ")
        genererFichier(instanceAStar.plateauParcouru, cheminDossierResolution, nomFichier)
        print("\nLe plateau a été généré avec succès dans le dossier '" 
             + cheminDossierResolution + "' avec le nom '" + nomFichier + ".txt'")
            

# Lance le menu principal
if __name__ == "__main__":
    afficherMenuPrincipal()