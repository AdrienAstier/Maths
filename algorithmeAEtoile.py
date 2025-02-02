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
    def __init__(self, plateau, calculHeuristique):

        # Plateau sélectionné
        self.plateauParcouru = plateau

        if not plateau.estValide() :
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
        
        self.depart = self.recherchePlateau('D')
        self.arrive = self.recherchePlateau('A')
        self.pointActuel = (self.depart[0], self.depart[1], 0, calculHeuristique(self.depart, self.arrive))

        # le premier point de la liste est le départ
        self.listeFermee.append(self.pointActuel)
    
    # recherche et renvoie la première position trouvée du caractère donné dans le plateau
    def recherchePlateau(self, caractere) :
        for i in range(self.plateauParcouru.getLargeur()) :
            for j in range(self.plateauParcouru.getLongueur()) :
                if self.plateauParcouru.getCase(i, j) == caractere :
                    return (i, j)

    # renvoi le chemin critique si le plateau est résolu, sinon lève une exception
    def getCheminCritique(self) :
        if len(self.cheminCritique) == 0 :
            raise Exception("Plateau non résolu, pas de chemin critique !")
        # else
        return self.cheminCritique

    # recherche un point dans la liste et le renvoi
    def rechercheListePoints(self, pointCherche, liste) :
        for point in liste :
            if point[0] == pointCherche[0] and point[1] == pointCherche[1] :
                return point
        
        return False

    # Exécute la prochaine étape de l'algorithme et met à jour le plateau si le plateau n'est pas résolu, sinon lève un exception.
    def parcourirProchainPoint(self):

        if len(self.cheminCritique) != 0 :
            raise Exception("Plateau déjà résolu !")

        for nbPointsAdj in range(4) :
            if nbPointsAdj == 0 :
                i = self.pointActuel[0] + 1
                j = self.pointActuel[1]
            elif nbPointsAdj == 1 :
                i = self.pointActuel[0]
                j = self.pointActuel[1] + 1
            elif nbPointsAdj == 2 :
                i = self.pointActuel[0]
                j = self.pointActuel[1] - 1
            else :
                i = self.pointActuel[0] - 1
                j = self.pointActuel[1]
            
            dansListeFermee = self.rechercheListePoints((i, j), self.listeFermee) != False
            if not dansListeFermee and i >= 0 and j >= 0 and i < self.plateauParcouru.getLargeur() and j < self.plateauParcouru.getLongueur() and self.plateauParcouru.getCase(i, j) != 'X' :

                heuristiquePoint = self.calculHeuristique((i, j), self.arrive)
                distanceDepartPoint = self.pointActuel[2] + 1

                pointDejaPresent = self.rechercheListePoints((i, j), self.listeOuverte)
                if pointDejaPresent != False:
                    if pointDejaPresent[2] + pointDejaPresent[3] > distanceDepartPoint + heuristiquePoint :
                        pointRemplacement = (pointDejaPresent[0], pointDejaPresent[1], distanceDepartPoint, heuristiquePoint)
                        self.listeOuverte.remove(pointDejaPresent)
                        self.listeOuverte.append(pointRemplacement)
                else :
                    self.listeOuverte.insert(0, (i, j, distanceDepartPoint, heuristiquePoint))
        
        self.selectionProchainPoint()
        
    # sélectionne le prochain point
    def selectionProchainPoint(self) :

        if len(self.listeOuverte) == 0 :
            raise Exception("Liste ouverte vide !")

        min = self.listeOuverte[0][2] + self.listeOuverte[0][3]
        pointMin = self.listeOuverte[0]
        for point in self.listeOuverte :
            sommeDistances = point[2] + point[3]
            if sommeDistances < min :
                min = sommeDistances
                pointMin = point
        
        self.pointActuel = pointMin
        self.listeOuverte.remove(self.pointActuel)
        self.listeFermee.append(self.pointActuel)

        if (self.pointActuel[0], self.pointActuel[1]) != self.arrive:
            self.plateauParcouru.setCase(pointMin[0], pointMin[1], '*')

    # Calcul le chemin critique et l'ajoute au plateau si le plateau a été résolu, sinon lève une exception
    def calculCheminCritique(self) :
        if (self.pointActuel[0], self.pointActuel[1]) != self.arrive :
            raise Exception("Le plateau n'a pas été résolu !")
        
        self.cheminCritique.insert(0, (self.pointActuel[0], self.pointActuel[1]))

        while (self.pointActuel[0], self.pointActuel[1]) != self.depart :
            self.prochaineEtapeCheminCritique()
        
    # recherche et ajoute le prochain point du chemin critique (arrivée -> départ)
    def prochaineEtapeCheminCritique(self) :
        for point in self.listeFermee :
            if (self.pointActuel[0] == point[0] and abs(self.pointActuel[1] - point[1]) == 1 or self.pointActuel[1] == point[1] and abs(self.pointActuel[0] - point[0]) == 1) and (point[2] + 1) == self.pointActuel[2]:

                self.cheminCritique.insert(0, (point[0], point[1]))
                self.pointActuel = point

                if (point[0] != self.depart[0] or point[1] != self.depart[1]) :
                    self.plateauParcouru.setCase(point[0], point[1], '.')
    
    # exécute l'algorithme A* sur le plateau
    def executionAlgo(self) :
        resolu = False
        while not resolu :
            self.parcourirProchainPoint()
            resolu = (self.pointActuel[0], self.pointActuel[1]) == self.arrive
        self.calculCheminCritique()
                
            

if __name__ == "__main__":
    lignes = [
        "DXOOOXOXOOOOOOOXOOOX",
        "OOOXOOOXXXOOXXOOOXOO",
        "OOOXOXOOOOOOOOOOXOOO",
        "OOXOXXOXOOXOOXOOOOOX",
        "XOXOOOOXOXOOOOOOOOXO",
        "XOOOOXXOOXOOOXXOOOOA"
    ]

    lignesCopie = [
        "DXOOOXOXOOOOOOOXOOOX",
        "OOOXOOOXXXOOXXOOOXOO",
        "OOOXOXOOOOOOOOOOXOOO",
        "OOXOXXOXOOXOOXOOOOOX",
        "XOXOOOOXOXOOOOOOOOXO",
        "XOOOOXXOOXOOOXXOOOOA"
    ]

    def heuristiqueNulle(pointActuel, arrive) :
        return 0

    def heuristiqueVille(pointActuel, arrive) :
        return abs(arrive[0] - pointActuel[0]) + abs(arrive[1] - pointActuel[1])

    def heuristiqueOiseau(pointActuel, arrive) :
        return abs(arrive[0] - pointActuel[0]) + abs(arrive[1] - pointActuel[1])

    plateauTest = plateau.Plateau(lignes)

    test = AlgorithmeAEtoile(plateauTest, heuristiqueNulle)
    print(test.plateauParcouru)

    test.executionAlgo()
    print(test.plateauParcouru)
    print(len(test.getCheminCritique()))

    test = AlgorithmeAEtoile(plateau.Plateau(lignesCopie), heuristiqueVille)
    test.executionAlgo()
    print(test.plateauParcouru)
    print(len(test.getCheminCritique()))

