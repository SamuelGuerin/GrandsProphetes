class Position:
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