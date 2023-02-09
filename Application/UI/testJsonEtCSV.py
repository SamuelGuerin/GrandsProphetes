import json
import FormGraph as fg
from pathlib import Path

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

jsonString = json.dumps(generations, default=obj_dict)

Path("Save/").mkdir(parents=True, exist_ok=True)

f = open("Save/save1.json", "w")
f.write(jsonString)
f.close()

# f = open("Save/save1.json")
# test = json.load(f)
# f.close()
