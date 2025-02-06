# algorithmeAEtoile.py                                          28 janvier 2025
# IUT de Rodez, pas de droits réservés

import plateau, copy

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
        
        # vérifie que le plateau donné est valide
        if not plateau.estValide() :
            raise Exception("Plateau non valide !")

        # réalise une copie du plateau sélectionné, pour la modifier
        self.plateauParcouru = copy.deepcopy(plateau)

        # Méthode qui permet de calculer l'heuristique des points voisins
        # avec en entrée le plateau , le point actuel et le point d'arrivée.
        self.calculHeuristique = calculHeuristique
        
        # Liste de tuples des points à ignorer car déjà traités.
        self.listeFermee = []

        # Liste des points dont la distance depuis le départ
        # et l'heuristique ont déjà été estimées mais pas validées
        self.listeOuverte = []

        # Liste de points du chemin critique.
        self.cheminCritique = []
        
        # récupère le départ, l'arrivé
        self.depart = self.recherchePlateau('D')
        self.arrive = self.recherchePlateau('A')

        # positionne le point actuel sur l'arrivée et calcul son heuristique
        self.pointActuel = (self.depart[0], self.depart[1], 0,
                            calculHeuristique(self.depart, self.arrive))

        # le premier point de la liste est le départ
        self.listeFermee.append(self.pointActuel)
    

    # recherche et renvoie la première position trouvée
    # du caractère cherché dans le plateau
    def recherchePlateau(self, caractere) :
        for i in range(self.plateauParcouru.getLargeur()) :
            for j in range(self.plateauParcouru.getLongueur()) :
                if self.plateauParcouru.getCase(i, j) == caractere :
                    return (i, j)


    # renvoi le chemin critique si le plateau est résolu,
    # sinon lève une exception
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


    # Exécute la prochaine étape de l'algorithme et met à jour le plateau
    # si le plateau n'est pas résolu, sinon lève un exception.
    def parcourirProchainPoint(self):

        if len(self.cheminCritique) != 0 :
            raise Exception("Plateau déjà résolu !")
        
        # traite les voisins du point actuel
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
            
            # vérifie que le voisin n'est pas dans la liste fermée
            # et que c'est un point valide (pas 'X' et dans le plateau)
            dansListeFermee = self.rechercheListePoints(
                                   (i, j), self.listeFermee) != False
            if (not dansListeFermee and i >= 0 and j >= 0
                and i < self.plateauParcouru.getLargeur()
                and j < self.plateauParcouru.getLongueur()
                and self.plateauParcouru.getCase(i, j) != 'X') :
                
                # calcul de l'heuristique et de la distance depuis le départ
                heuristiquePoint = self.calculHeuristique((i, j), self.arrive)
                distanceDepartPoint = self.pointActuel[2] + 1
                
                # cas où le voisin est déjà dans la liste ouverte
                pointDejaPresent = self.rechercheListePoints(
                                        (i, j), self.listeOuverte)
                if pointDejaPresent != False:
                    # ne modifie les infos du point que si la nouvelle somme
                    # "distance depuis le départ" et heuristique
                    # est plus petite que l'ancienne
                    if (pointDejaPresent[2] + pointDejaPresent[3]
                        > distanceDepartPoint + heuristiquePoint) :
                        
                        pointRemplacement = (pointDejaPresent[0],
                                             pointDejaPresent[1],
                                             distanceDepartPoint,
                                             heuristiquePoint)
                        
                        self.listeOuverte.remove(pointDejaPresent)
                        self.listeOuverte.append(pointRemplacement)
                else :
                    self.listeOuverte.append((i, j, distanceDepartPoint,
                                              heuristiquePoint))
        
        self.selectionProchainPoint()
        

    # sélectionne le prochain point dans la recherche du chemin le plus court
    def selectionProchainPoint(self) :

        if len(self.listeOuverte) == 0 :
            raise Exception("Liste ouverte vide !")

        # recherche le point dans la liste ouverte dont la somme
        # de la distance depuis le départ et de l'heuristique est la plus petite
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


    # Calcul le chemin critique et l'ajoute au plateau
    # si le plateau a été résolu, sinon lève une exception
    def calculCheminCritique(self) :
        if (self.pointActuel[0], self.pointActuel[1]) != self.arrive :
            raise Exception("Le plateau n'a pas été résolu  "
                            + "ou le chemin critique a déjà été calculé !")
        
        self.cheminCritique.insert(0, (self.pointActuel[0], self.pointActuel[1]))

        while (self.pointActuel[0], self.pointActuel[1]) != self.depart :
            self.prochaineEtapeCheminCritique()
        

    # recherche et ajoute le prochain point du chemin critique (arrivée -> départ)
    def prochaineEtapeCheminCritique(self) :
        for point in self.listeFermee :
            
            # sélectionne le point adjacent faisant parti du chemin critique
            if ((self.pointActuel[0] == point[0]
                 and abs(self.pointActuel[1] - point[1]) == 1
                 or self.pointActuel[1] == point[1]
                 and abs(self.pointActuel[0] - point[0]) == 1)
                and (point[2] + 1) == self.pointActuel[2]):

                # ajoute le voisin au chemin critique et se positionne dessus
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
                
            

# test de la classe (utilise heuristique.py)
if __name__ == "__main__":
    lignes = [
        "DXOOOXOXOOOOOOOXOOOX",
        "OOOXOOOXXXOOXXOOOXOO",
        "OOOXOXOOOOOOOOOOXOOO",
        "OOXOXXOXOOXOOXOOOOOX",
        "XOXOOOOXOXOOOOOOOOXO",
        "XOOOOXXOOXOOOXXOOOOA"
    ]
    
    import heuristiques as h
    
    plateauTest = plateau.Plateau(lignes)

    test = AlgorithmeAEtoile(plateauTest, h.heuristiqueNulle)
    print(test.plateauParcouru)

    test.executionAlgo()
    print(test.plateauParcouru)
    print(len(test.cheminCritique))

    test = AlgorithmeAEtoile(plateauTest, h.heuristiqueVille)
    test.executionAlgo()
    print(test.plateauParcouru)
    print(len(test.cheminCritique))
    
    test = AlgorithmeAEtoile(plateauTest, h.heuristiqueOiseau)
    test.executionAlgo()
    print(test.plateauParcouru)
    print(len(test.cheminCritique))
    

