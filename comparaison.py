import matplotlib.pyplot as plt
import generationPlateau as gen
import algorithmeAEtoile as algo
import heuristiques as heuri



def calculComparaisons(largeur, longueur, tauxMin, tauxMax, coins, nbPlateaux) :
    
    moyennesDijkstra = []
    moyennesVille = []
    moyennesOiseau = []
    tauxCasesInterdites = []
    
    for taux in range(tauxMin, tauxMax + 1) :
        
        tauxCasesInterdites.append(taux)
        
        sommeDijkstra = 0
        sommeVille = 0
        sommeOiseau = 0
        
        for i in range(nbPlateaux) :
            plateau = gen.genererPlateau(longueur, largeur, taux, coins)
            
            dijkstra = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueNulle)
            dijkstra.executionAlgo()
            sommeDijkstra += len(dijkstra.listeFermee)
            
            ville = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueVille)
            ville.executionAlgo()
            sommeDijkstra += len(ville.listeFermee)
            
            oiseau = algo.AlgorithmeAEtoile(plateau, heuri.heuristiqueOiseau)
            oiseau.executionAlgo()
            sommeDijkstra += len(oiseau.listeFermee)
        
        moyennesDijkstra.append(sommeDijkstra / nbPlateaux)
        moyennesVille.append(sommeVille / nbPlateaux)
        moyennesOiseau.append(sommeOiseau / nbPlateaux)
    
    return (moyennesDijkstra, moyennesOiseau, moyennesVille, tauxCasesInterdites)
        
def comparaisonHeuristiques(moyennesPremiere, moyennesSeconde, taux, labelPremiere, labelSeconde) :
    
    fig, graph = plt.subplots(1, 1, sharex=True, constrained_layout=True)
    
    graph.plot(taux, moyennesPremiere, label=labelPremiere)
    graph.plot(taux, moyennesSeconde, label=labelSeconde)
    graph.legend(loc='upper right')
    graph.set_ylabel('TEST $[^oC]$')
    
