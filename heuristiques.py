# fichier pour les heuristiques

import math

def heuristiqueNulle(pointActuel, arrive) :
    return 0

def heuristiqueVille(pointActuel, arrive) :
    return abs(arrive[0] - pointActuel[0]) + abs(arrive[1] - pointActuel[1])

def heuristiqueOiseau(pointActuel, arrive) :
        return math.sqrt((abs(arrive[0] - pointActuel[0])) ** 2 + (abs(arrive[1] - pointActuel[1])) ** 2)