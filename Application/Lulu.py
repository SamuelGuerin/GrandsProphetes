#Classe Lulu
class Lulu():
    def __init__(self, speed, sense, energyRemaining, FoodCollected, force, lastPostion, isEnabled):
        self.speed = speed
        self.sense = sense
        self.energyRemaining = energyRemaining
        self.FoodCollected = FoodCollected
        self.force = force
        self.lastPostion = lastPostion
        self.isEnabled = isEnabled

    def __repr__(self) -> str:
        return "Lulu"