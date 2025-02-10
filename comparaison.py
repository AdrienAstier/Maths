import matplotlib.pyplot as plt
import generationPlateau as gen
import algorithmeAEtoile as algo
import heuristiques as heuri



def calculComparaisons(largeur, longueur, tauxMin, tauxMax, coins, nbPlateaux, precision) :
    
    moyennesDijkstra = []
    moyennesVille = []
    moyennesOiseau = []
    tauxCasesInterdites = []
    
    for t in range( int(tauxMin * precision), int(tauxMax * precision + 1)) :
        
        taux = t / precision
        
        tauxCasesInterdites.append(taux)
        
        sommeDijkstra = 0
        sommeVille = 0
        sommeOiseau = 0
        
        for i in range(nbPlateaux) :
            plateau = gen.genererPlateau(longueur, largeur, taux, coins)
            
            # permet de vérifier que le plateau peut être résolu
            resolu = False

            while not resolu :
                # ne récupère les données que si le plateau peut être résolu
                try :
                    dijkstra = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueNulle)
                    dijkstra.executionAlgo()
                    sommeDijkstra += len(dijkstra.listeFermee)
                    
                    ville = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueVille)
                    ville.executionAlgo()
                    sommeVille += len(ville.listeFermee)
                    
                    oiseau = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueOiseau)
                    oiseau.executionAlgo()
                    sommeOiseau += len(oiseau.listeFermee)

                    resolu = True
                except :
                    # génère un nouveau plateau si l'ancien n'a pas pu être résolu
                    plateau = gen.genererPlateau(longueur, largeur, taux, coins)

        moyennesDijkstra.append(sommeDijkstra / nbPlateaux)
        moyennesVille.append(sommeVille / nbPlateaux)
        moyennesOiseau.append(sommeOiseau / nbPlateaux)
        
    return (moyennesDijkstra, moyennesOiseau, moyennesVille, tauxCasesInterdites)


def comparaisonHeuristiquesDeux(moyennesPremiere, moyennesSeconde, taux,
                                labelPremiere, labelSeconde) :
    
    fig, graph = plt.subplots(1, 1, sharex=True, constrained_layout=True)
    
    graph.plot(taux, moyennesPremiere, label=labelPremiere)
    graph.plot(taux, moyennesSeconde, label=labelSeconde)
    graph.legend(loc='upper right')
    graph.set_ylabel('Nombre d\'étapes')
    graph.set_xlabel('Taux de cases interdites')

    plt.show()
    
def comparaisonHeuristiquesTroix(moyennesPremiere, moyennesDeuxieme, moyennesTroisieme,
                            taux, labelPremiere, labelDeuxieme, labelTroisieme) :
    
    fig, graph = plt.subplots(1, 1, sharex=True, constrained_layout=True)
    
    graph.plot(taux, moyennesPremiere, label=labelPremiere)
    graph.plot(taux, moyennesDeuxieme, label=labelDeuxieme)
    graph.plot(taux, moyennesTroisieme, label=labelTroisieme)
    graph.legend(loc='upper right')
    graph.set_ylabel('Nombre d\'étapes')
    graph.set_xlabel('Taux de cases interdites')

    plt.show()


if __name__ == "__main__":
    
    (dijkstra, oiseau, ville, taux) = calculComparaisons(20, 20, 0, 0.95, False, 50, 20)

    comparaisonHeuristiquesTroix(dijkstra, ville, oiseau, taux, "Dijkstra", "Ville", "Oiseau")