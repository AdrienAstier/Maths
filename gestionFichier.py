# gestionFichier.py

from plateau import Plateau
import os

# Import plateau, renvoie plateau
def importationPlateau(cheminFichier):

    plateauLu = None

    try:
        with open(cheminFichier, 'r') as fichier:
            lignes = fichier.readlines()
            
            for i in range(len(lignes)) : #Récupère les lignes du fichier
                lignes[i] = lignes[i].replace("\n", "") #Remplace les \n lu par rien

            plateauLu = Plateau(lignes)
            
            return plateauLu
    
    except FileNotFoundError:
        print(f"Le fichier {cheminFichier} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

# Génére un nouveau fichier et écrit le plateau dedans
def genererFichier(plateau, nomFichier):
    lignes = plateau.getLignes()
    
    cheminPlateaux = "plateaux_generes/"
    cheminFichier = cheminPlateaux + nomFichier + ".txt"
    
    try:
        os.makedirs(cheminPlateaux, exist_ok = True) # Crée le dossier s'il n'existe pas.
        with open(cheminFichier, 'w') as fichier: #Ecriture ligne par ligne
            for i in range(len(lignes) - 1) :
                fichier.write(lignes[i] + '\n')
            fichier.write(lignes[len(lignes) - 1]) #Nécessaire pour enlever le dernier saut de ligne

        return cheminFichier
    
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")
        return None