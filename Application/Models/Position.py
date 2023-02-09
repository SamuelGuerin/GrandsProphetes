class Position:
    """Une :class:`Position` représente un couple de coordonnées en x et en y. Les positions sont également utilisées comme clés pour chaque item dans la carte (map) dans :class:`Territory`

    :param x: coordonnée en x
    :type x: int
    :param y: coordonnée en y
    :type y: int
    """
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other) -> bool:
        return not(self == other)

    def __repr__(self) -> str:
        return ('(' + str(self.x) + ', ' + str(self.y) + ')')