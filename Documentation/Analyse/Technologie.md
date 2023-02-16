# Technologies Utilisées

## Langage de Programmation

Pour le langage de programmation, nous avons décidé de programmer en python, parce que le langage est fort pour le traitement de grandes quantités de données et il y avait des librairies disponibles et faciles d'utilisation qui nous permettait de faire nos graphiques (Matplotlib) et notre interface visuels (CustomTkinter) et les animations (ManimCE).

## Architecture Logicielle

Niveau architectural, nous avons fait une simple application formulaire qui permet d'entrée des données de la simulation et ensuite d'accéder à une autre fenêtre qui comporte les graphiques.

Étant donné qu'il s'agit d'une application utilisable hors-ligne, nous n'avons pas de bases de données/de serveur pour héberger l'application. Nous avons des fichiers JSON locaux qui permettent à l'utilisateur de sauvegarder des résultats et l'application.

---

## Sécurité

L'application ne comporte pas de sécurité très élevée, car elle n'est pas vraiment nécessaire, car l'application n'a pas de données sensibles et qu'elle est locale. Une vérification sur les fichiers de sauvegarde JSON est en place afin de s'assurer qu'un utilisateur n'essaie pas de charger des mauvais fichiers dans l'application.

---

## Stratégie de Tests

Nous avons mis en place une batterie de tests unitaires et automatisés afin de s'assurer du bon fonctionnement des algorithmes de la simulation

---

## Faisabilité

Nous pensons que l'application est faisable dans le temps alloué par le cadre du cours et que nous serons capables de produire un résultat satisfaisant pour le client. Dans le cas ou nous ne sommes pas en mesure d'atteindre nos objectifs, nous avons mis en place une documentation pour futur programmeur robuste afin de permet un bon transfert de connaissances du projet.
