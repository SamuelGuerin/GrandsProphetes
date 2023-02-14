from Models.Position import Position
#Classe Food

class Food():
    """Food est la classe qui représente un item de nourriture. Chaque nourriture contient sa propre :class:`Position`.

    :param position: La position de la nourriture dans la carte (map) dans :class:`Territory`
    :type position: :class:`Position`
    """
    def __init__(self, position):

        self.position = position

    def __repr__(self) -> str:
        return "Food"