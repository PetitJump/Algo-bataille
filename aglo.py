from main import File, Jeu, Carte, clear

population = int(input("Combien voulez vous de population : "))
clear()
tour_max = int(input("A combien de tour voulez vous arreter la partie : "))
parti_reussi = 0

for i in range(population):
    Partie_en_cour = Jeu(tour_max)
    result = Partie_en_cour.run()
    if result == "1":
        parti_reussi += 1
print(f"Il y a {parti_reussi / population * 100} % de reussite")
