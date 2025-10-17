import random, os

class File:
    def __init__(self, t):
        self.__taille = t
        self.__data = [None] * self.__taille
        self.__s = 0
        self.__e = 0

    def estVide(self):
        return self.__s == self.__e
    
    def est_pleine(self):
        return self.__e - self.__s == self.__taille 

    def enfiler(self, x):
        if self.est_pleine():
            raise Exception('File pleine')
        else:
            self.__data[self.__e % self.__taille] = x
            self.__e += 1

    def defiler(self):
        if self.estVide():
            raise Exception("Pile vide")
        else:
            x = self.__data[self.__s % self.__taille]
            self.__s += 1
            return x
        
    def __repr__(self):
        res = []
        for i in range(self.__s, self.__e):
            res.append(self.__data[i % self.__taille])
        return str(res)

class Carte:
    def __init__(self, couleur: str, valeur: str):
        self.couleur = couleur
        self.valeur = valeur

class Jeu:
    def __init__(self):
        """Mélange le paquet et distribu les cartes"""
        paquet = [Carte("Coeur", "A"), Carte("Coeur", "R"), Carte("Coeur", "D"), Carte("Coeur", "V"), Carte("Carreau", "A"), Carte("Carreau", "R"), Carte("Carreau", "D"), Carte("Carreau", "V"), Carte("Pique", "A"), Carte("Pique", "R"), Carte("Pique", "D"), Carte("Pique", "V"), Carte("Trefle", "A"), Carte("Trefle", "R"), Carte("Trefle", "D"), Carte("Trefle", "V")]
        random.shuffle(paquet) #Mélange le paquet
        self.J1 = File(16)
        self.J2 = File(16)
        for i in range(len(paquet)):
            if i < 8:
                self.J1.enfiler(paquet[i])
            else:
                self.J2.enfiler(paquet[i])
    
    def gagne(self, c1: Carte, c2: Carte):
        ordre = ["V", "D", "R", "A"]
        v1 = ordre.index(c1.valeur) #Savoir a quel index est la valeur de c1
        v2 = ordre.index(c2.valeur) #Savoir a quel index est la valeur de c2
        if v1 > v2:
            return 1
        elif v2 > v1:
            return 2
        return 0

    def afficher_stats(self, c1: Carte, c2: Carte, resultat: int):
        clear()
        print(f"Joueur 1 : {c1.couleur} {c1.valeur}")
        #print(f"Cartes restantes : {...}") #Pas eu le temps de l'implémenter
        print("")
        print(f"Joueur 2 : {c2.couleur} {c2.valeur}")
        #print(f"Cartes restantes : {...}") #Pas eu le temps de l'implémenter
        print("")
        if resultat == 1:
            print("Joueur 1 a gagner le tour")
        elif resultat == 2:
            print("Joueur 2 a gagner le tour")
        else:
            print("Égalité")

        input("Appuyer sur entré pour continuer")
        clear()
    
    def run(self):
        total = []
        tour = 0
        while not self.J1.estVide() and not self.J2.estVide() and tour < 200:
            tour += 1
            c1 = self.J1.defiler()
            c2 = self.J2.defiler()
            resultat = self.gagne(c1, c2)
            total.append(c1)
            total.append(c2)
            self.afficher_stats(c1, c2, resultat)
            if resultat == 1:
                for k in total:
                    self.J1.enfiler(k)
                total = []
            elif resultat == 2:
                for k in total:
                    self.J2.enfiler(k)
                total = []
        print("Parti fini")
        if tour == 200:
            print("Parti impossible")
        elif self.J1.estVide():
            print("Bravo joueur 2, vous avez gagner !")
        else:
            print("Bravo joueur 1, vous avez gagner !")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #Clear le terminal

Partie_en_cour = Jeu()
Partie_en_cour.run()