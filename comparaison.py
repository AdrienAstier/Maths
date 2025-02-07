#import matplotlib.pyplot as plt
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
        
        nbPlateuxResolus = 0
        
        for i in range(nbPlateaux) :
            plateau = gen.genererPlateau(longueur, largeur, taux, coins)
            
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

                nbPlateuxResolus += 1
            except :
                pass # ne rien faire
        
        moyennesDijkstra.append(sommeDijkstra / nbPlateuxResolus)
        moyennesVille.append(sommeVille / nbPlateuxResolus)
        moyennesOiseau.append(sommeOiseau / nbPlateuxResolus)
        print(sommeDijkstra / nbPlateuxResolus)
        
    return (moyennesDijkstra, moyennesOiseau, moyennesVille, tauxCasesInterdites)

"""
def comparaisonHeuristiques(moyennesPremiere, moyennesSeconde, taux, labelPremiere, labelSeconde) :
    
    fig, graph = plt.subplots(1, 1, sharex=True, constrained_layout=True)
    
    graph.plot(taux, moyennesPremiere, label=labelPremiere)
    graph.plot(taux, moyennesSeconde, label=labelSeconde)
    graph.legend(loc='upper right')
    graph.set_ylabel('TEST $[^oC]$')
    
    
"""

if __name__ == "__main__":
    
    print(calculComparaisons(50, 50, 0, 0.3, True, 50, 1))
