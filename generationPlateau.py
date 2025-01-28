# 
# generationPlateau.py                                      28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

import plateau as p

import random

#
# Gère la construction des tableaux.
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
    
    # TODO vérifications valeurs invalides
    
    # Placement des murs et des chemins aléatoires.
    for i in range(largeur):
        for o in range(longueur):
            
            if tauxMurs >= random.random():
                lignes_plateau[i] += "X"
            else:
                lignes_plateau[i] += "O"
    
    # Création du plateau pour modifier ses cases.
    plateau = p.Plateau(lignes_plateau)
    
    # Placement du point A et D
    
    # Définition de l'emplacement des points A et D
    coinXYA = [0, 0]
    coinXYD = [longueur - 1, largeur - 1]
    if coins:
        coinXYA[0] = int((longueur - 1) / 2)
        coinXYA[1] = int((largeur - 1) / 2)
        coinXYD = coinXYA
        
        # Le point A aura plus tendance à aller en bas à droite
        # alors que le point D aura plus tendance à aller en haut à gauche.
        
    # Détermination de manière aléatoire de l'emplacement des points.
    pointA = (random.randint(coinXYA[1], largeur - 1), random.randint(coinXYA[0], longueur - 1))
    pointD = (random.randint(0, coinXYD[1]), random.randint(0, coinXYD[0]))
        
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
        
    return plateau
        
if __name__ == "__main__":
    print(genererPlateau(14, 10, .2, True).estValide())