# Planification des Tests

## Tests pour l'interface utilisateur

### Tests du formulaire d'entrée des paramètres de la simulation

* N'accepte pas de nombres négatifs (Accepte seulement positifs)
* Bornes minimums et maximums sur certains champs
* Vérification du ratio entre la quantité de nourriture et de Lulus par rapport à la taille du territoire (périmètre du territoire)

### Tests des graphiques des données et statistiques des Lulus

* Les données minimum, moyenne et maximum des Lulus de leurs caractéristiques
* Les Lulus s'affichent correctement selon leurs caractéristiques et les 3 axes du graphique
* La couleur des Lulus est influencée par leurs caractéristiques
* Visualisation des graphiques en 2D pour mettre l'accent sur 2 caractéristique précises (Vitesse + Vision, Vitesse + Taille, Vision + Taille)
* L'angle d'affichage du graphique 3D reste le même lorsqu'on change de génération

### Tests animations des générations des Lulus

* La nourriture et les Lulus ont une couleur de base différente
* La couleur des Lulus est influencée par leurs caractéristiques
* La couleur de base des Lulus change de bleu à rouge si elles sont actives ou non

## Tests pour la logique des mouvements des Lulus

* Priorité ennemi, nourriture(Food) et proie par rapport à la vision de la Lulu
* Ennemi: La lulu s'enfui de l'ennemi le plus près d'elle-même présent dans sa vision
* Nourriture(Food): La lulu se dirige vers la nourriture la plus près d'elle-même présente dans sa vision
* Proie: La lulu se dirige vers la proie la plus près d'elle-même présente dans sa vision
* Mouvement vers une position aléatoire si rien n'est présent dans la vision de la Lulu
* Impossibilité de sortir des limites du Territoire

## Tests pour la logique de la reproduction des Lulus

* Assez de nourriture pour se reproduire
* Une mutation se produit en respectant les probabilités
* Le mutation respecte le degré de variance maximale et les limites minimales et maximales des caractéristiques des Lulus
* Le nouveau-né est positionné le plus près possible du parent sur le périmètre du territoire

## Tests pour le territoire

* Le nombre de Lulus et nourritures fournies en paramètres sont toutes générées et présentes dans le territoire
* Le changement de génération garde toutes les informations des Lulus survivantes
