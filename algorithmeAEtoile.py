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
    def __init__(self, plateau: Plateau, calculHeuristique: lambda):

        # Plateau sélectionné
        self.plateauParcouru = plateau

        if !plateau.estValide() :
            raise Exception("Plateau non valide !")

        # Méthode qui permet de calculer l'heuristique des points voisins
        # avec en entrée le plateau , le point actuel et le point d'arrivée.
        self.calculHeuristique = calculHeuristique
        
        # Liste de tuples des points à ignorer car déjà traités.
        self.listeFermee = []

        # Liste des points dont la distance depuis le départ a déjà été estimée mais pas validée
        self.listeOuverte = []

        # Liste de points du chemin critique.
        self.cheminCritique = []
        
        self.depart = recherchePlateau('D')
        self.arrive = recherchePlateau('A')
        self.pointActuel = self.depart

        # le premier point de la liste est le départ
        self.listeFermee.append((self.depart[0], self.depart[1], 0, calculHeuristique(self.plateauParcouru, self.pointActuel, self.arrive)))
    
    # recherche et renvoie la première position trouvée du caractère donné dans le plateau
    def recherchePlateau(caractere) :
        for i in range(plateauParcouru.getLargeur()) :
            for j in range(plateauParcouru.getLongueur()) :
                if plateauParcouru.getCase(i, j) == caractere :
                    return (i, j)


    def getCheminCritique(self) :
        if len(self.cheminCritique) == 0 :
            raise Exception("Plateau non résolu, pas de chemin critique !")
        # else
        return self.cheminCritique

    # Exécute la prochaine étape de l'algorithme et met à jour le plateau.
    def parcourirProchainPoint(self):

        for nbPointsAdj in range(4) :
            if nbPointsAdj % 2 == 0 :
                i = self.pointActuel[0]
                j = self.pointActuel[1] + if nbPointsAdj == 0 : -1 else : 1
            else :
                i = self.pointActuel[0] + if nbPointsAdj == 1 : -1 else : 1
                j = self.pointActuel[1]
            
            dansListeFermee = rechercheListePoints((i, j), listeFermee) == False

            if !(dansListeFermee or i < 0 or j < 0 or i > self.plateauParcouru.getLargeur() or j > self.plateauParcouru.getLongueur() or self.plateauParcouru.getCase(i, j) == 'X') :
                listeOuverte.append((i, j, rechercheListePoints(self.pointActuel, listeFermee)[2] + 1, calculHeuristique(self.plateauParcouru, (i, j), self.arrive)))
        
        min = listeOuverte[0][2] + listeOuverte[0][3]
        pointMin = listeOuverte[0]
        for point in listeOuverte :
            sommeDistances = point[2] + point[3]
            if sommeDistances < min :
                min = sommeDistances
                pointMin = point
        
        self.pointActuel = pointMin
        self.plateauParcouru.setCase(pointMin[0], pointMin[1], '*')

    def rechercheListePoints(pointCherche, liste) :
        for point in liste :
            if point[0] == pointCherche[0] and point[1] == pointCherche[1] :
                return point
        
        return False

    # Calcul le chemin critique à la fin de l'algorithme et l'ajoute au plateau
    def calculCheminCritique(self) :
        pass