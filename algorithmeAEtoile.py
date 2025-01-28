# 
# algorithmeAEtoile.py                                         28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

#
# Implémente un algorithme afin de trouver le plus court chemin 
# dans n'importe quels graphes.
#
# Dans notre cas, il se base sur une heuristique ainsi qu'un plateau
# avec des obstacles, un point de départ et d'arrivé.
#
#
class AlgorithmeAEtoile:
    
    #
    # Construit une instance de l'algorithme de parcours.
    # plateau : une instance d'un plateau généré.
    # calculHeuristique : une méthode avec en entrée un tuple du point 
    #                     et un plateau. 
    #                     Permet de calculer l'heuristique d'un point donné.
    #
    def __init__(plateau: Plateau, calculHeuristique: lambda):
        
        # TODO algorithme de base
        
        #
        # Méthode qui permet de calculer l'heuristique des points voisins
        # avec en entrée une liste de tuples des prochains points
        # et le plateau.
        #
        self.calculHeuristique = calculHeuristique
        
        # Liste de tuples des points encore en analyse.
        self.listeOuverte = []
        
        # Liste de tuples des points à ignorer.
        self.listeFermee = []
        
        # Plateau sélectionné
        self.plateau = plateau
        
    # TODO méthode pour effectuer la prochaine action de l'algorithme
    # ex : prochainPoint()