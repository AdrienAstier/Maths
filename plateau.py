# plateau.py

class Plateau:

    lignesPlateau = [] #Structure de données représentant le plateau
    longueur = 0 #Longueur des lignes
    largeur = 0 #Nombre de lignes

    #Constructeur
    def __init__(self, lignes):
        self.lignesPlateau = lignes
        self.longueur = len(lignes[0])
        self.largeur = len(lignes)

    #get la valeur d'un case
    def getCase(self, i, j) :
        return self.lignesPlateau[i][j]

    #set la valeur d'une case
    def setCase(self, i, j, nouvelleValeur) :
        ligne = self.lignesPlateau[i]
        self.lignesPlateau[i] = ligne[:j] + nouvelleValeur + ligne[j+1:]

    #Vérifie si un plateau est valide
    def estValide(self) :
        aPresent = False
        dPresent = False
        valide = True

        longueurLignes = len(self.lignesPlateau[0])
        for i in range(self.getLargeur()) :
            if(len(self.lignesPlateau[i]) != longueurLignes) :
                return False

        for i in range(self.getLargeur()) :
            for j in range(self.getLongueur()) :
                case = self.lignesPlateau[i][j]
                if(case == 'A') :
                    aPresent = True
                elif(case == 'A' and aPresent) :
                    valide = False
                elif(case == 'D') :
                    dPresent = True
                elif(case == 'D' and dPresent) :
                    valide = False
                elif(case != 'O' and case != 'X') :
                    valide = False

        return valide and aPresent and dPresent

    #Renvoie la longueur 
    def getLongueur(self) :
        return self.longueur

    #Renvoie le nombre de ligne
    def getLargeur(self) :
        return self.largeur
    
    def getLignes(self) :
        return self.lignesPlateau

    #To String
    # def __str__(self):
    #     chaine = ""
    #     for i in range(self.getLargeur()) :
    #         chaine += self.lignesPlateau[i] + "\n"
    #     return chaine