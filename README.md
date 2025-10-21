# Présentation :
Le fichier algo.py est le point d’entrée principal du programme lorsqu’on veut analyser le fonctionnement du jeu sur un grand nombre de parties.
Il ne contient pas directement la logique du jeu (qui se trouve dans main.py), mais il orchestre les simulations afin de mesurer les performances globales du système.

## Fonctionnement détaillé :
Demande des paramètres à l’utilisateur :
Le script commence par demander :
- Le nombre de parties à simuler (population), c’est-à-dire combien de fois le jeu complet doit être exécuté.
- Le nombre maximum de tours (tour_max) autorisés par partie avant de la considérer comme “non terminée”.

## Boucle de simulation :
Le programme crée une boucle qui s’exécute autant de fois que le nombre de parties demandées.