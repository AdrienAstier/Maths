# 
# generationPlateau.py                                      28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

import plateau

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
#         et du départ dans les coins opposées (false par défaut.)
#
def genererPlateau(longueur: int, largeur: int, tauxMurs: float, coins: bool) -> list:
    
    # TODO vérifications valeurs invalides
    
    # TODO placement des murs et des chemins en une fois 
    
    # Placement des murs aléatoires
    for i in range(largeur):
        for o in range(longueur):
            lignes_plateau.append("O" ou "X")
            pass
        
if __name__ == "__main__":
    print(genererPlateau(10, 2, 0.1, True))