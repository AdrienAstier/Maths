# 
# algorithmeAEtoile.py                                         28 janvier 2025
# IUT de Rodez, pas de droits réservés
#

import plateau

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

        #
        # Méthode qui permet de calculer l'heuristique des points voisins
        # avec en entrée une liste de tuples des prochains points
        # et le plateau.
        #
        self.calculHeuristique = calculHeuristique
        
        # Change d'état si le chemin est trouvé au fil des itérations.
        self.chemin_trouve = False
        
        # Liste de tuples des points encore en analyse.
        self.listeOuverte = []
        
        # Liste de tuples des points à ignorer.
        self.listeFermee = []

        # Liste de points du chemin critique.
        self.cheminCritique = []
        
        # Plateau sélectionné
        self.plateauParcouru = plateau
    
    #
    # Calcule la suite du chemin avec les points voisins
    # et donne le nouveau point parcouru.
    #
    def parcourirProchainPoint():
        
        # TODO méthode
        pass