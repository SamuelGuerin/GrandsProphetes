import json
import jsonpickle
import re
from Models.Saves import Save
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
    :type data: `Save`
    """

    jsonString = jsonpickle.encode(data)

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
    :rtype: Save
    """

    data = None

    try:
        file_path = filedialog.askopenfilename(initialdir="Save/", filetypes=[("Json File", "*.json")])

        with open(file_path) as f:
            contents = f.readlines()
        dataTemp = jsonpickle.decode(contents[0])

        f.close()
        data = Save(dataTemp.sizeX, dataTemp.sizeY,dataTemp.nbFood, dataTemp.nbLulu, dataTemp.energy, dataTemp.varSpeed, dataTemp.varSense, dataTemp.varSize,dataTemp.mutationChance, dataTemp.nbGen, dataTemp.generations)
        
        
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