import json
import FormGraph as fg
import re
from pathlib import Path
from os import listdir
from jsonschema import validate
from customtkinter import filedialog

def obj_dict(obj):
    return obj.__dict__

def fileNumber(name):
    match = re.match("^save([1-9][0-9]{0,9}).json", name)
    return int(match.group(1))

def saveData(data):
    jsonString = json.dumps(data, default=obj_dict)

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

def loadData():
    schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
        {
        "type": "array",
        "items": [
            {
            "type": "array",
            "items": [
                {
                "type": "number"
                }
            ],
            "additionalItems": True
            },
            {
            "type": "array",
            "items": [
                {
                "type": "number"
                }
            ],
            "additionalItems": True
            },
            {
            "type": "array",
            "items": [
                {
                "type": "number"
                }
            ],
            "additionalItems": True
            }
        ],
        "additionalItems": False
        }
    ],
    "additionalItems": True
    }

    file_path = filedialog.askopenfilename(initialdir="Save/", filetypes=[("Json File", "*.json")])

    f = open(file_path)
    data = json.load(f)
    f.close()
    try:
        validate(instance=data, schema=schema)
        print("fichier valide")
    except:
        data = None
        print("fichier non valide")
    
    return data