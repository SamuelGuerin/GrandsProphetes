class Save:
    def __init__(self,sizeX = 0,sizeY = 0,nbFood = 0, nbLulu = 0,energy = 0,varSpeed = 0,varSense = 0,varSize = 0,mutationChance = 0,nbGen = 0,generations = []):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.nbFood = nbFood
        self.nbLulu = nbLulu
        self.energy = energy
        self.varSpeed = varSpeed
        self.varSense = varSense
        self.varSize = varSize
        self.mutationChance = mutationChance
        self.nbGen = nbGen
        self.generations = generations

    def createSaveLulu(lstLulus):
        lstSaveLulu = []
        for lulu in lstLulus[:]:
            saveLulu = (lulu.speed,lulu.sense,lulu.size)
            lstSaveLulu.append(saveLulu)
        return lstSaveLulu
