# Hypothèses

## Déplacement des lulus
- Un lulu va fuir face à un lulu assez gros pour le manger même s'il est proche d'une nourriture.
- Un lulu qui a récupéré 0 nourriture et qui n'a plus d'énergie va s'arrêter sur place. Il
pourra donc être mangé par les autres lulus assez gros. S'il ne se fait pas manger, il meurt à la fin de la "génération".
- Un lulu qui a récupéré 1 nourriture va continuer à chercher pour une deuxième nourriture. S'il manque
d'énergie, il reste sur place. Il pourra donc être mangé par les autres lulus assez gros. S'il ne se fait pas manger, il survit et passe à la prochaine génération sans se reproduire.
- Un lulu qui a récupéré 2 nourritures tente de retourner à l'abri sur les bordures sans prendre en compte l'énergie. Il peut quand même se faire intercepter (manger) par un lulu assez gros sur son chemin. À la fin de la génération, il se reproduit.

## Fonctionnement de l'application
### Interface utilisateur
- En ouvrant l'application, l'utilisateur est accueilli par une interface graphique qui l'invitera à entrer les variables qui influenceront la simulation (Grosseur du territoire, Quantité de lulus, Quantité de nourriture, vitesse de déplacement au départ, nombre de générations, etc.).
- Bouton Simuler pour démarrer la simulation en prenant compte des variables entrées.
### Simulation
- Au départ, les lulus apparaissent aléatoirement sur les bordures du territoire.
- La nourriture va apparaître aléatoirement sur le territoire sauf sur les bordures.
- Les lulus vont se déplacer (voir déplacement des lulus plus haut).
- Les lulus qui ont 2 nourritures se reproduisent asexuellement. Lors de cet acte, il y a une chance de mutation pour l'enfant / nouveau-né.
### Résultat / Graphiques
- À la fin de la simulation :
    - Le logiciel présente les résultats finaux de la dernière génération (nombre d'individus vivants, vitesse moyenne, taille moyenne, etc.)
    - Un bouton "Statistiques" va permettre à l'utilisateur de visionner les statistiques des différentes générations dans des graphiques (2D/3D). L'utilisateur pourra naviguer de génération en génération à l'aide de flèches pour voir la variation des résultats. De plus, l'utilisateur pourra cocher les variables affichées dans le graphique.
