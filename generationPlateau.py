# 
# generationPlateau.py                                      28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

import plateau as p

import random

#
# Gère la construction des plateaux aléatoires.
#
    
#
# Génère un plateau aléatoirement avec les données rentrées.
#
# longueur : la longueur du plateau
# largeur : largeur du plateau
# tauxMurs : la fréquence de murs dans le plateau, de 0 à 1.
# coins : force la mise en place de l'arrivée
#         et du départ dans les coins opposées.
#
def genererPlateau(longueur: int, largeur: int, tauxMurs: float, coins: bool) -> p.Plateau:

    # Génération des lignes vides
    lignes_plateau = [""] * largeur
    
    # Si le plateau est trop petit
    if longueur < 3 or largeur < 3:
        raise Exception("La longueur est la largeur d'un plateau doit être supérieur ou égal à 3.")
    
    # Placement des murs et des chemins aléatoires.
    for i in range(largeur):
        for o in range(longueur):
            
            if tauxMurs >= random.random():
                lignes_plateau[i] += "X"
            else:
                lignes_plateau[i] += "O"
    
    # Création du plateau pour modifier ses cases.
    plateau = p.Plateau(lignes_plateau)
    
    # Définition de l'emplacement des points A et D
    
    if coins:
        __placerPointsADCoinsPlateau(plateau)
    else:
        __placerPointsADAleatoirePlateau(plateau)
        
    return plateau

#
# Place le point A et D dans le plateau
# de manière aléatoire.
#
# plateau : un plateau partiellement généré.
#
def __placerPointsADAleatoirePlateau(plateau: p.Plateau):
    
    longueur = plateau.getLongueur()
    largeur = plateau.getLargeur()
    
    pointA = (random.randint(0, largeur - 1), random.randint(0, longueur - 1))
    pointD = (random.randint(0, largeur - 1), random.randint(0, longueur - 1))
    
    # On place d'abord le point D
    plateau.setCase(pointD[0], pointD[1], "D")
    
    if pointA[0] != pointD[0] or pointA[1] != pointD[1]:
        plateau.setCase(pointA[0], pointA[1], "A") 
        
    # Résolution du placement de A si les deux points se superposent.
    else:
            
        # En résumé, on décale d'un de hauteur selon la position de A.
        if pointA[0] != 0:
            plateau.setCase(pointA[0] - 1, pointA[1], "A")   
        else:
            plateau.setCase(pointA[0] + 1, pointA[1], "A")  

#
# Place le point A et D dans les coins du plateau.
# Force le point A en bas à droite et le point D en haut à gauche.
#
# plateau : un plateau partiellement généré.
#
def __placerPointsADCoinsPlateau(plateau: p.Plateau):
    
    pointA = (plateau.getLargeur() - 1, plateau.getLongueur() - 1)
    pointD = (0, 0)
    
    plateau.setCase(pointA[0], pointA[1], "A")
    plateau.setCase(pointD[0], pointD[1], "D")
        
# Debug
if __name__ == "__main__":
    print(genererPlateau(3, 3, .2, True))