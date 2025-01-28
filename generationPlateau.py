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
def genererPlateau(longueur: int, largeur: int, tauxMurs: float, coins: bool) -> list:
    
    # TODO largeur et longueur aléatoire
    
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
    
    # Création du plateau
    plateau = p.Plateau(lignes_plateau)
    
    if coins:
        
        # TODO forcer le placement des points dans les coins
        pass
    else:
        
        pointA = (random.randint(0, largeur - 1), random.randint(0, longueur - 1))
        pointD = (random.randint(0, largeur - 1), random.randint(0, longueur - 1))
        
        plateau.setCase(pointD[0], pointD[1], "D")
        
        if pointA[0] != pointD[0] or pointA[1] != pointD[1]:
            plateau.setCase(pointA[0], pointA[1], "A") 
        
        # Résolution du placement de A si les deux points se superposent.
        else:
            
            # En résumé, on décale d'un de hauteur.
            if pointA[0] != 0:
                plateau.setCase(pointA[0] - 1, pointA[1], "A")   
            else:
                plateau.setCase(pointA[0] + 1, pointA[1], "A")  
        
    return plateau
        
if __name__ == "__main__":
    for i in range(1000):
        print(genererPlateau(10, 10, .9, False))