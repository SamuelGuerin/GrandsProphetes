import json
import FormGraph as fg
from pathlib import Path
from os import listdir
import re

generationsObjects = fg.generateLulus()
generations = []
lulus = []

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

jsonString = json.dumps(generations, default=obj_dict)

Path("Save/").mkdir(parents=True, exist_ok=True)

filenames = listdir("Save/")

reggex = re.compile("^save[1-9][0-9]{0,9}.json")
filenames = [name for name in filenames if reggex.match(name)]

filenames = sorted(filenames, key=fileNumber)

if (len(filenames) == 0):
    test = 1
else:
    test = fileNumber(filenames[len(filenames) - 1]) + 1

f = open("Save/save" + str(test) + ".json", "w")
f.write(jsonString)
f.close()

# f = open("Save/save1.json")
# test = json.load(f)
# f.close()
