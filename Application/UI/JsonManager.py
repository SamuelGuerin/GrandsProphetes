import json
import re
from pathlib import Path
from os import listdir
from jsonschema import validate
from customtkinter import filedialog

def fileNumber(name):
    """Permet de savoir le numéro du fichier save.

    :return: Retourne le numéro du fichier save.
    :rtype: int
    """

    match = re.match("^save([1-9][0-9]{0,9}).json", name)
    return int(match.group(1))

def saveData(data):
    """Enregistre les données des coordonnées dans un fichier Json dans le dossier "Save".

    :param data: Liste des coordonnées des générations de la simulation.
    :type data: `[[[float],[float],[float]]]`
    """

    def obj_dict(obj):
        return obj.__dict__

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
    """Permet à un utilisateur de choisir un fichier json à importer et de retourner les valeurs.

    :return: Retourne une liste de coordonnées pour le graphique 3d.
    :rtype: [[[float],[float],[float]]]
    """

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

    data = None

    try:
        file_path = filedialog.askopenfilename(initialdir="Save/", filetypes=[("Json File", "*.json")])

        f = open(file_path)
        data = json.load(f)
        f.close()

        validate(instance=data, schema=schema)

        if not validateData(data):
            raise Exception()
        
        print("fichier valide")
    except:
        data = None
        print("fichier non valide")
    return data

def validateData(data):
    """Permet à un utilisateur de choisir un fichier json à importer et de retourner les valeurs.

    :param data: Liste des coordonnées des générations de la simulation.
    :type data: `[[[float],[float],[float]]]`

    :return: Retourne `True` si les données sont valides.
    :rtype: bool
    """
    for generation in data:
        if not (len(generation[0]) == len(generation[1]) == len(generation[2])):
            return False
        
    return True