=============
Examples
=============

Dépendances:
************

-  L’implémentation actuelle a été développée avec python 3.
-  Manim : librairie pour la génération d’images et vidéos

   1. `Installer chocolatey <https://chocolatey.org/install>`__
   2. ``choco install manimce``

-  Installer les dépendances python

   1. ``pip install -r GrandsProphetes\docs\source\requirements.txt``

Installation
************

-  Code : `github <https://github.com/SamuelGuerin/GrandsProphetes>`__
-  Point d’entré du programme : ``python ./Application/main.py``
-  L’application est portable et est composée d’un seul .exe
   `download <https://github.com/SamuelGuerin/GrandsProphetes/release>`__


Documentation
*************

- Faite avec `sphinx <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/install.html>`__
- `syntaxe rst <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__
- `docstrings <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`__
- `extension vsCode <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`__
- `theme utilisé <https://github.com/piccolo-orm/piccolo_theme>`__

Générer une population et la simuler 
************************************
.. code-block:: python
    
    # Créé un singleton avec un territoire 100x100 avec 25 nourritures et 100 lulus
    Territory.createMap(100, 100, 25, 100)

    # Faire bouger les lulus 5000 fois
    for _ in range(5000):

        # Afficher le nombre de lulus qui vont survivre à la prochaine génération
        print("nombre de survivants: " + str(sum(lulu.foodAmount >= 1 for lulu in Territory.getLulus())))

        # Laisser le temps de générer l'image
        time.sleep(0.2)

        # Générer l'image avec manim
        renderAnimation()

        # Bouger les lulus
        for l in Territory.__lulus:
            l.move()