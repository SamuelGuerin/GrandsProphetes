class Lulu:
    def __init__(self,position,speed = 0,sense = 0,size = 0,energy = 0,foodAmount = 0,lastPos = None, isDone = False):
        self.isDone = isDone
        self.speed = speed
        self.sense = sense
        self.size = size
        self.energy = energy
        self.foodAmount = foodAmount
        self.lastPos = lastPos
        self.position = position

    def __repr__(self) -> str:
        return "Lulu"
