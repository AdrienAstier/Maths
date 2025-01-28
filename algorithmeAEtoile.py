# algorithmeAEtoile.py                                         28 janvier 2025
# IUT de Rodez, pas de droits réservés

import plateau

# Implémente un algorithme afin de trouver le plus court chemin 
# dans n'importe quels graphes.
#
# Dans notre cas, il se base sur une heuristique ainsi qu'un plateau
# avec des obstacles, un point de départ et d'arrivé.
class AlgorithmeAEtoile:

    # Construit une instance de l'algorithme de parcours.
    # plateau : une instance d'un plateau généré.
    # calculHeuristique : une méthode avec en entrée un tuple du point actuel
    #                     et un plateau. 
    #                     Permet de calculer l'heuristique d'un point donné.
    def __init__(plateau: Plateau, calculHeuristique: lambda):

        # Méthode qui permet de calculer l'heuristique des points voisins
        # avec en entrée le plateau , le point actuel et le point d'arrivée.
        self.calculHeuristique = calculHeuristique
        
        # Liste de tuples des points à ignorer car déjà traités.
        self.listeFermee = []

        # Liste de points du chemin critique.
        self.cheminCritique = []
        
        # Plateau sélectionné
        self.plateauParcouru = plateau

        self.depart = (0,0)#TODO
        self.arrive = (0,0)#TODO
        self.pointActuel = (0,0) #TODO
    
    def getCheminCritique() :
        if (len(cheminCritique) == 0) {
            raise Exception("Plateau non résolu, pas de chemin critique !")
        }
        # else
        return cheminCritique

    # Exécute la prochaine étape de l'algorithme et met à jour le plateau.
    def parcourirProchainPoint():
        
        # TODO méthode
        pass
    
    # Calcul le chemin critique à la fin de l'algorithme et l'ajoute au plateau
    def calculCheminCritique() :
        pass