import FormGraph as fg
import re
from JsonManager import saveData, loadData

generationsObjects = fg.generateLulus()
generations = []

speeds = []
senses = []
sizes = []

for generation in generationsObjects:
    speeds.clear()
    senses.clear()
    sizes.clear()
    for lulu in generation:
        speeds.append(round(lulu.Speed, 2))
        senses.append(round(lulu.Sense, 2))
        sizes.append(round(lulu.Size, 2))
    generations.append([speeds.copy(), senses.copy(), sizes.copy()])

def obj_dict(obj):
    return obj.__dict__

def fileNumber(name):
    match = re.match("^save([1-9][0-9]{0,9}).json", name)
    return int(match.group(1))

saveData(generations)

data = loadData()

if data == None:
    print("return")
