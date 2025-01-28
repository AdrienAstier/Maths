# gestionFichier.py

from plateau import Plateau
import os

# Import plateau
def importationPlateau(cheminFichier):

    plateauLu = None

    try:
        with open(cheminFichier, 'r') as fichier:
            lignes = fichier.readlines()
            
            for i in range(len(lignes)) :
                lignes[i] = lignes[i].replace("\n", "") #Remplace les \n lu par rien

            plateauLu = plateau.Plateau(lignes)
            
            return plateauLu
    
    except FileNotFoundError:
        print(f"Le fichier {cheminFichier} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

# Génére un nouveau fichier
def genererFichier(plateau, nomFichier):
    lignes = plateau.getLignes()
    
    cheminFichier = "plateaux_generes/" + nomFichier + ".txt"
    
    try:
        with open(cheminFichier, 'w') as fichier:
            for ligne in lignes:
                fichier.write(ligne + '\n')

        return cheminFichier
    
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")
        return None

if __name__ == "__main__":
    lignes = ["AO", "XX", "OD"]
    plateau = Plateau(lignes)
    genererFichier(plateau, "Bonjour")
