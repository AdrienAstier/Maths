class Plateau:

    lignesPlateau = []
    longueur = 0
    largeur = 0

    def __init__(self, lignes):
        self.lignesPlateau = lignes
        self.longueur = len(lignes[0])
        self.largeur = len(lignes)

    def getCase(self, i, j) :
        return self.lignesPlateau[i][j]

    def setCase(self, i, j, nouvelleValeur) :
        ligne = self.lignesPlateau[i]
        self.lignesPlateau[i] = ligne[:j] + nouvelleValeur + ligne[j+1:]

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

    def getLongueur(self) :
        return self.longueur

    def getLargeur(self) :
        return self.largeur

    def __str__(self):
        chaine = "\n"
        for i in range(self.getLargeur()) :
            chaine += self.lignesPlateau[i] + "\n"
        return chaine