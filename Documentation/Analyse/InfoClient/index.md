# Informations du clients

DEVIS – PROJET BIOINFORMATIQUE

PERSONNE RESSOURCE
Luciano Vidali
Enseignant en biologie
Bureau A-2362


BUT DU PROJET
Développer un nouveau laboratoire en bio-informatique sous forme de jeu pour les étudiant.e.s du programme sciences de la nature. Ce laboratoire permettra de simuler la sélection naturelle sur une population de « Lulus », des créatures animales imaginaires.


CONCEPTS THÉORIQUES
Les êtres vivants sont soumis à la sélection naturelle. Voici une courte explication qui vous permettra d’en saisir les grandes lignes.

1.	Les êtres vivants contiennent des unités d’informations nommées « gènes » qui codent pour leurs caractéristiques. L’ensemble des gènes d’un individu se nomme « génotype ». L’ensemble des caractéristiques se nomme « phénotype ».
2.	Les êtres vivants se reproduisent entre eux au sein d’une même « population ». Une population est définie comme un ensemble d’individus capables de se reproduire entre eux.
3.	Les gènes sont transmis des parents à leurs descendants.
4.	Les êtres vivants ont une capacité de reproduction infinie.
5.	La capacité de support de l’environnement est limitée.
6.	À chaque génération, seuls les individus ayant obtenu assez de ressources (territoire, nourriture, partenaire, etc.) peuvent se reproduire.
7.	Certains génotypes amènent des phénotypes qui favorisent la survie et la reproduction. Les individus avec les phénotypes favorables ont une meilleure chance de voir leur génotypes transmis à la génération suivante.
8.	Avec le temps, l’environnement favorise la survie d’individus qui ont le phénotype le mieux adapté. 
9.	La population se transforme graduellement. C’est cela que l’on nomme « évolution par sélection naturelle ».



EXPLICATION DES BESOINS ET CONTRAINTES

1.	BESOINS
•	Simuler la sélection naturelle à l’aide d’outil informatique. 
•	Pouvoir faire varier les conditions initiales de la génération.
•	L’étudiant.e qui joue doit être capable de suivre les changements dans la population à l’aide de graphique ou de tableau.

2.	CONTRAINTES

•	Surface de jeu ou Environnement
Les Lulus se déplacent sur la surface de jeu et luttent pour leur survie en tentant d’accumuler assez de nourriture pour survivre et se reproduire. Chaque déplacement d’une case entraîne une dépense d’énergie. Quand l’énergie d’un individu est épuisée, l’individu arrête de se déplacer. Suggestion : trois surfaces de jeu possible (petite-moyenne-grande).

•	Taille de la population de départ
Elle devrait idéalement pouvoir être contrôlée par l’expérimentateur pour vérifier les effets de l’abondance vs la rareté des ressources. L’étudiant.e qui joue doit pouvoir observer graphiquement les variations de la taille de la population. Suggestion : 0 à 100 individus au départ.

•	Ressources alimentaires disponibles 
Les Lulus ont besoin de nourriture pour survivre à chaque génération. La nourriture apparaît aléatoirement sur la surface de jeu. 
Individu qui obtient 1 ressource = survie jusqu’à la prochaine génération;
Individu qui obtient 2 ressources = survie et se reproduit;
Individu qui obtient 0 ressources = meurt.
Suggestion : 0 à 200 éléments de nourriture. 

•	Nombre de générations
À chaque génération, les Lulus se précipitent sur la zone de jeu et tentent d’obtenir des ressources alimentaires, soit par la cueillette ou la prédation d’autres individus. Les individus ayant obtenu suffisamment de ressources peuvent se reproduire. Une fois que toutes les ressources ont été cueillies, la génération s’arrête et on compile les résultats. La génération suivante débute avec le nombre d’individus restant à la génération précédente. Les individus conservent leurs caractéristiques au fil des générations.

•	Mutation
Chaque Lulu ayant obtenu deux ressources alimentaires se reproduit. Il crée un autre individu identique à lui-même avec une faible chance de mutation qui fera varier légèrement les caractéristiques héritées des parents. Cette propriété du jeu doit être présente si on veut observer les modifications de la population obtenues par sélection naturelle.

•	Pouvoir faire varier les caractéristiques (phénotype) des individus
a)	Énergie au départ : L’énergie permet aux Lulus de se déplacer sur la surface de jeu. Suggestion : faire varier l’énergie de 0 à 100. Avancer sur une case = 1 unité d’énergie dépensée.

b)	Vitesse : Plus le chiffre est élevé, plus les individus se déplacent rapidement sur la surface de jeu.
Avantage : la distance couverte par unité de temps est plus grande pour un Lulu plus rapide.
Désavantage : le coût énergétique de déplacement est plus grand. Un Lulu deux fois plus rapide dépense deux fois plus d’énergie. Il s’agit donc d’une relation au carré :
Coût énergétique de déplacement = vitesse 2

c)	Masse : Plus le chiffre est élevé, plus la masse de l’individu est élevée. 
Avantage : Ils ont plus d’énergie au départ. Ils ont aussi une chance de consommer les individus plus petits qu’eux et ainsi obtenir leur nourriture. 
Désavantage: Les individus plus massifs sont plus lents. Le volume d’un objet s’exprime en cm3. Il s’agit donc d’une relation au cube :
Coût énergétique de déplacement = masse3 * vitesse 2
Suggestion : faire varier la masse de 0 à 10.

d)	Capacité de détection de la nourriture (exemple : chimiotactisme, vision, olfaction…)
La zone de détection de la nourriture de chaque individu doit pouvoir varier. Quand un Lulu détecte la nourriture, il se dirige vers elle. S’il détecte un individu plus massif que lui, l’individus fuit. La capacité de détection plus grande permet de trouver des ressources plus efficacement.


OPTIONS POSSIBLES 
•	Temps de l’expérience
Normalement, chaque génération s’arrête quand toutes les ressources sont épuisées. Si l’expérimentateur le désire, le temps de jeu pourrait devenir l’élément qui décide de la fin de chaque génération, quelque soit la quantité de ressources encore disponible dans l’environnement. On peut laisser ainsi plus de temps à la prédation de faire son effet ou observer l’effet de la rareté de la nourriture dans un environnement.

•	Reproduction possible
Les individus restant à la fin de chaque génération se croisent avec un autre partenaire restant et combinent leur génotype. La descendance obtenue obtient donc une moyenne des caractéristiques parentales. Les individus ayant obtenu les plus de ressources se reproduisent entre eux (ils ont le premier choix des meilleurs partenaires).


MÉDIAGRAPHIE

Cette idée est tirée d’idée tiré du livre « Le gène égoïste » de Richard Dawkins.

Aussi, vous trouverez un super exemple de ce type de jeu sur la chaîne « Primer ». Visionnez la 5e vidéo de cette série est essentiel !
https://www.youtube.com/playlist?list=PLKortajF2dPBWMIS6KF4RLtQiG6KQrTdB 
