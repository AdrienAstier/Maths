# 
# heuristiques.py                                           06 février 2025
# IUT de Rodez, pas de droits réservés
#

# Script regroupant les différentes heuristiques possibles de A*
# Requis par l'algorithme.

# On peut aussi faire x ** 0.5
# mais cela est plus lent sur certains processeurs.
from math import sqrt

#
# Calcule l'heuristique utilisé par Dijkstra.
# 
# pointActuel : coordonnées du point où se trouve actuellement l'algorithme.
# arrive : coordonnées de l'arrivée (en supposant que nous le connaissons.)
#
def heuristiqueNulle(pointActuel: tuple, arrive: tuple) -> int :
    return 0

#
# Calcule l'heuristique avec la distance de Manhattan.
# 
# pointActuel : coordonnées du point où se trouve actuellement l'algorithme.
# arrive : coordonnées de l'arrivée (en supposant que nous le connaissons.)
#
def heuristiqueVille(pointActuel: tuple, arrive: tuple) -> int:
    return abs(arrive[0] - pointActuel[0]) + abs(arrive[1] - pointActuel[1])

#
# Calcule l'heuristique en utilisant la distance par vol d'oiseau.
# 
# pointActuel : coordonnées du point où se trouve actuellement l'algorithme.
# arrive : coordonnées de l'arrivée (en supposant que nous le connaissons.)
#
def heuristiqueOiseau(pointActuel: tuple, arrive: tuple) -> int:
        return sqrt((abs(arrive[0] - pointActuel[0])) ** 2 
                  + (abs(arrive[1] - pointActuel[1])) ** 2)