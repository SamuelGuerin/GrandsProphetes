import customtkinter as ct
import tkinter as tk
from tkinter import ttk
from PIL import Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import FormGraph as fg
import math
import SimulationManager as Simulation
from JsonManager import saveData, loadData
import threading
import Form as f

global canvasR
canvasR = None

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

class Form(ct.CTk):
    """Méthode

    .. code-block:: python

        def show_info(
            txt
        )

    La fonction est appelé lorsque l'utilisateur passe le curseur sur l'un des button info

    :param txt: txt est le texte qui est afficher pour exposer à l'utilisateur ce qu'il doit entrer.
    :type txt: string

    .. code-block:: python

        def hide_info()

    La fonction est appelé lorsque le curseur de l'utilisateur quitte l'un des button info

    .. code-block:: python

        def get_inputMapSizeX()

    C'est function valide que la valeur entrée pour la grandeur du territoire en X est bonne.

    :return: Cette fonction retourne la valeur entrée dans le champ. (Taille du territoire en X)
    :rtype: int 

    .. code-block:: python

        def get_inputMapSizeY()  

    C'est function valide que la valeur entrée pour la grandeur du territoire en Y est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (Taille du territoire en Y)
    :rtype: int 

    .. code-block:: python

        def get_inputStartFood()  

    C'est function valide que la valeur entrée pour le nombre de nourriture présent lors du début d'une génération est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (Nourriture présent lors du début d'une génération)
    :rtype: int 

    .. code-block:: python

        def get_infoStartFood()  
    
    Génère le texte pour indiquer à la l'utilisateur ce qu'il doit entré dans le champs nourriture.

    :return: Cette fonction retourne les informations que l'on doit entrée dans le champ pour la nourriture.
    :rtype: string

    .. code-block:: python

        def get_inputStartLulu()  

    C'est function valide que la valeur entrée pour les Lulus présent lors du début de la simulation est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (Nombre de Lulus au début de la simmulation)
    :rtype: int 
     
    .. code-block:: python

        def get_infoStartLulu()  

    Génère le texte pour indiquer à la l'utilisateur ce qu'il doit entré dans le champs qui indique les nombre de Lulu au départ.

    :return: Cette fonction retourne les informations que l'on doit entrée dans le champ pour le nombre de Lulu au départ.
    :rtype: string

    .. code-block:: python

        def get_inputEnergy()   

    C'est function valide que la valeur entrée pour l'énergie est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (Énergie des Lulus au début de chaque génération)
    :rtype: int 

    .. code-block:: python

        def get_inputSpeed()  
        
    C'est function valide que la valeur entrée pour le % de variation de la vitesse est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (% de variation de la vitesse)
    :rtype: int 

    .. code-block:: python

        def get_inputSense() 

    C'est function valide que la valeur entrée pour le % de variation de la vision est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (% de variation de la vision)
    :rtype: int 
 
    .. code-block:: python

        def get_inputSize() 

    C'est function valide que la valeur entrée pour le % de variation de la taille est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (% de variation de la taille)
    :rtype: int 
 
    .. code-block:: python

        def get_inputMutation() 

    C'est function valide que la valeur entrée pour le % de chance de mutation est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (% de chance de mutation)
    :rtype: int 
  
    .. code-block:: python

        def get_inputGeneration() 

    C'est function valide que la valeur entrée pour le nombre de génération généré est bonne. 

    :return: Cette fonction retourne la valeur entrée dans le champ. (Nombre de génération à simuler)
    :rtype: int 
   
    .. code-block:: python

        def get_allBeforeSimulation() 

    C'est function appelle toute les fonctions pour valider chacun des champs et la fonction pour lancer la simulation.
 
    .. code-block:: python

        def add_Graph() 

    Cette fonction permet de généré les graphiques pour chaque génération de plus des button généré,
    pour pouvoir naviguer dans les différente génération ou pour changer l'angle de vue du graphique.
            
    .. code-block:: python

        def preview() 

    Cette fonction permet d'afficher la prévisualisation du commencement de la simulation
 

    """

    def cancelSimulation():
        Simulation.check = True
        btnCancel.grid_remove()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        index = fg.Index()

        width = 1920
        height = 1080

        current_path = os.path.dirname(os.path.realpath(__file__))
        path = current_path + "/logo.ico"
        self.wm_iconbitmap(path)

        # Setup de base de l'interface
        self.geometry("900x800")
        self.title("Lulus World")
        self.resizable(True, True)
        self.maxsize(width, height)
        self.minsize(830, 700)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Ajout du background
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ct.CTkImage(Image.open(current_path + "/evo.jpeg"),
                                               size=(width, height))
        self.bg_image = ct.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image.grid(row=0, column=0, columnspan=5)
        self.bg_image.rowconfigure(0, weight=1)
        self.bg_image.columnconfigure(0, weight=1)

        # Ajout du frame
        self.frame_1 = ct.CTkFrame(master=self)
        self.frame_1.grid(row=0, column=0, columnspan=5, sticky="ns")

        #Méthode afficher l'information que l'utilisateur doit entrer
        def show_info(event, txt):
            lblErrorInForm.configure(text=txt, corner_radius=90, text_color="#dce4ee", fg_color="#343638")

        def hide_info(event):
            lblErrorInForm.configure(text="", fg_color="#2b2b2b")

        # Créer une image pour le bouton
        circle_image = ct.CTkImage(Image.open(current_path + "/circle.png"))

        # Enter 1 -- MapSizeX
        lblMapSizeX = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille X du territoire")
        lblMapSizeX.grid(row=0, column=0, pady=10, padx=10)

        infoMapSizeX = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMapSizeX.grid(row=0, column=1, pady=10, padx=10)
        infoMapSizeX.bind("<Enter>", lambda event: show_info(event, "Déterminer la grandeur du territoire en X.\r (Cette valeur doit être entre 100 et 1 000)"))
        infoMapSizeX.bind("<Leave>", hide_info)

        txtMapSizeX = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="200"))
        txtMapSizeX.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

        lblMapSizeXGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMapSizeXGood.grid(row=0, column=3, pady=10, padx=10)


        # Enter 2 -- MapSizeY
        lblMapSizeY = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille Y du territoire")
        lblMapSizeY.grid(row=1, column=0, pady=10, padx=10)

        infoMapSizeY = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMapSizeY.grid(row=1, column=1, pady=10, padx=10)
        infoMapSizeY.bind("<Enter>", lambda event: show_info(event, "Déterminer la grandeur du territoire en Y.\r (Cette valeur doit être entre 100 et 1 000)"))
        infoMapSizeY.bind("<Leave>", hide_info)

        txtMapSizeY = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="200"))
        txtMapSizeY.grid(row=1, column=2, padx=20, pady=10, sticky="ew")

        lblMapSizeYGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMapSizeYGood.grid(row=1, column=3, pady=10, padx=10)

        # Enter 3 -- StartFood
        lblStartFood = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nourriture disponible par génération")
        lblStartFood.grid(row=2, column=0, pady=10, padx=10)

        infoStartFood = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoStartFood.grid(row=2, column=1, pady=10, padx=10)
        infoStartFood.bind("<Enter>", lambda event: show_info(event, get_infoStartFood()))
        infoStartFood.bind("<Leave>", hide_info)

        txtStartFood = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="50"))
        txtStartFood.grid(row=2, column=2, padx=20, pady=10, sticky="ew")

        lblStartFoodGood = ct.CTkLabel(master=self.frame_1, text="")
        lblStartFoodGood.grid(row=2, column=3, pady=10, padx=10)

        # Enter 4 -- StartLulu
        lblStartLulu = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre de Lulus initial")
        lblStartLulu.grid(row=3, column=0, pady=10, padx=10)

        infoStartLulu = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoStartLulu.grid(row=3, column=1, pady=10, padx=10)
        infoStartLulu.bind("<Enter>", lambda event: show_info(event, get_infoStartLulu()))
        infoStartLulu.bind("<Leave>", hide_info)

        txtStartLulu = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="10"))
        txtStartLulu.grid(row=3, column=2, padx=20, pady=10, sticky="ew")

        lblStartLuluGood = ct.CTkLabel(master=self.frame_1, text="")
        lblStartLuluGood.grid(row=3, column=3, pady=10, padx=10)

        # Enter 5 -- Energy
        lblEnergy = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Énergie des Lulus")
        lblEnergy.grid(row=4, column=0, pady=10, padx=10)

        infoEnergy = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoEnergy.grid(row=4, column=1, pady=10, padx=10)
        infoEnergy.bind("<Enter>", lambda event: show_info(event, "Énergie que les Lulus auront pour\r ce déplacer lors d'une génération.\r (Cette valeur doit être entre 100 et 100 000)"))
        infoEnergy.bind("<Leave>", hide_info)

        txtEnergy = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="3000"))
        txtEnergy.grid(row=4, column=2, padx=20, pady=10, sticky="ew")

        lblEnergyGood = ct.CTkLabel(master=self.frame_1, text="")
        lblEnergyGood.grid(row=4, column=3, pady=10, padx=10)

        # Enter 6 -- Speed
        lblSpeed = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la vitesse (en %)")
        lblSpeed.grid(row=5, column=0, pady=10, padx=10)

        infoSpeed = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSpeed.grid(row=5, column=1, pady=10, padx=10)
        infoSpeed.bind("<Enter>", lambda event: show_info(event, "Variation de leur vitesse en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 100)"))
        infoSpeed.bind("<Leave>", hide_info)

        txtSpeed = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="25"))
        txtSpeed.grid(row=5, column=2, padx=20, pady=10, sticky="ew")

        lblSpeedGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSpeedGood.grid(row=5, column=3, pady=10, padx=10)

        # Enter 7 -- Sense
        lblSense = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la vision (en %)")
        lblSense.grid(row=6, column=0, pady=10, padx=10)

        infoSense = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSense.grid(row=6, column=1, pady=10, padx=10)
        infoSense.bind("<Enter>", lambda event: show_info(event, "Variation de leur vision en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 100)"))
        infoSense.bind("<Leave>", hide_info)

        txtSense = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="25"))
        txtSense.grid(row=6, column=2, padx=20, pady=10, sticky="ew")

        lblSenseGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSenseGood.grid(row=6, column=3, pady=10, padx=10)

        # Enter 8 -- Size
        lblSize = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la taille (en %)")
        lblSize.grid(row=7, column=0, pady=10, padx=10)

        infoSize = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSize.grid(row=7, column=1, pady=10, padx=10)
        infoSize.bind("<Enter>", lambda event: show_info(event, "Variation de leur taille en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 100)"))
        infoSize.bind("<Leave>", hide_info)

        txtSize = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="25"))
        txtSize.grid(row=7, column=2, padx=20, pady=10, sticky="ew")

        lblSizeGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSizeGood.grid(row=7, column=3, pady=10, padx=10)

        # Entrer 9 -- Mutation
        lblMutation = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="% de chance de mutation")
        lblMutation.grid(row=8, column=0, pady=10, padx=10)

        infoMutation = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMutation.grid(row=8, column=1, pady=10, padx=10)
        infoMutation.bind("<Enter>", lambda event: show_info(event, "Représente le % de chance qu'une mutation\r soit effectuée lors de la reproduction.\r (Cette valeur doit être entre 0 et 100)"))
        infoMutation.bind("<Leave>", hide_info)

        txtMutation = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="50"))
        txtMutation.grid(row=8, column=2, padx=20, pady=10, sticky="ew")

        lblMutationGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMutationGood.grid(row=8, column=3, pady=10, padx=10)

        # Enter 10 -- Generation
        lblGeneration = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre de générations")
        lblGeneration.grid(row=9, column=0, pady=10, padx=10)

        infoGeneration = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoGeneration.grid(row=9, column=1, pady=10, padx=10)
        infoGeneration.bind("<Enter>", lambda event: show_info(event, "Nombre de générations\r qui sera effectuées lors de la simulation.\r (Cette valeur doit être entre 1 et 1 000)"))
        infoGeneration.bind("<Leave>", hide_info)

        txtGeneration = ct.CTkEntry(master=self.frame_1, textvariable=tk.StringVar(value="25"))
        txtGeneration.grid(row=9, column=2, padx=20, pady=10, sticky="ew")

        lblGenerationGood = ct.CTkLabel(master=self.frame_1, text="")
        lblGenerationGood.grid(row=9, column=3, pady=10, padx=10)

        # Enter 1 -- Validation
        def get_inputMapSizeX():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                if(mapSizeXValue < 0):
                    raise ValueError
                if(mapSizeXValue < 100 or mapSizeXValue > 1000):
                    lblMapSizeXGood.configure(text="Cette valeur doit être entre 100 et 1 000", text_color="red")
                else:
                    lblMapSizeXGood.configure(text="")
                    return mapSizeXValue
            except ValueError:
                lblMapSizeXGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")


        # Enter 2 -- Validation
        def get_inputMapSizeY():
            try:
                mapSizeYValue = int(txtMapSizeY.get())
                if(mapSizeYValue < 0):
                    raise ValueError
                if(mapSizeYValue < 100 or mapSizeYValue > 1000):
                    lblMapSizeYGood.configure(text="Cette valeur doit être entre 100 et 1 000", text_color="red")
                else:
                    lblMapSizeYGood.configure(text="")
                    return mapSizeYValue
            except ValueError:
                lblMapSizeYGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 3 -- Validation
        def get_inputStartFood():
            try:
                startFoodValue = int(txtStartFood.get())
                if(startFoodValue < 0):
                    raise ValueError
                try:
                    mapSizeXValue = get_inputMapSizeX()
                    mapSizeYValue = get_inputMapSizeY()
                    maxFood = mapSizeXValue * mapSizeYValue * 0.50
                    if(startFoodValue > maxFood):
                        txt = "Cette valeur doit être inférieur ou égal à " 
                        + str(int(maxFood)) + "\r(Cette valeur dépend de la taille du territoire)"
                        lblStartFoodGood.configure(text=txt, text_color="red")
                    else:
                        lblStartFoodGood.configure(text="")
                        return startFoodValue
                except TypeError:
                    lblStartFoodGood.configure(text="Les tailles du territoire doivent être valides" + 
                                               "\ravant de choisir le nombre de nourritures", text_color="red")
            except ValueError:
                lblStartFoodGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        def get_infoStartFood():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                mapSizeYValue = int(txtMapSizeY.get()) 
                if(mapSizeXValue < 0 or mapSizeYValue < 0):
                    raise ValueError
                maxFood = mapSizeXValue * mapSizeYValue * 0.50
                return "Nombre de nourritures présent sur le territoire.\r (Le nombre de nourritures doit être inférieur ou égal\r à 50% du territoire soit " + str(math.floor(maxFood)) + ")"
            except ValueError:
                return "Nombre de nourritures présent sur le territoire.\r (Le nombre de nourritures doit être inférieur ou égal\r à 50% du territoire\r(Les valeurs en X et Y doivent être mise\r pour pouvoir savoir la valeur maximale))"

        # Enter 4 -- Validation
        def get_inputStartLulu():
            try:
                startLuluValue = int(txtStartLulu.get())
                if(startLuluValue < 0):
                    raise ValueError
                try:
                    mapSizeXValue = get_inputMapSizeX()
                    mapSizeYValue = get_inputMapSizeY()
                    maxLulu = (mapSizeXValue * 2 + mapSizeYValue * 2) - 4
                    if(startLuluValue > maxLulu):
                        lblStartLuluGood.configure(text="Cette valeur doit être inférieur ou égal à " 
                                                + str(int(maxLulu)) + "\r(Cette valeur dépend de la taille du territoire)", text_color="red")
                    else:
                        lblStartLuluGood.configure(text="")
                        return startLuluValue
                except TypeError:
                    lblStartLuluGood.configure(text="Les tailles du territoire doivent être valides" + 
                                               "\ravant de choisir le nombre de lulus", text_color="red")
            except ValueError:
                lblStartLuluGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        def get_infoStartLulu():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                mapSizeYValue = int(txtMapSizeY.get()) 
                if(mapSizeXValue < 0 or mapSizeYValue < 0):
                    raise ValueError
                maxLulu = (mapSizeXValue * 2 + mapSizeYValue * 2) - 4
                return "Nombre de Lulus présent sur le territoire au début.\r (Le nombre de Lulus doit être inférieur ou égal\r au périmètre du territoire - 4 soit " + str(math.floor(maxLulu)) + ")"
            except ValueError:
                return "Nombre de Lulus présent sur le territoire au début.\r (Le nombre de Lulus doit être inférieur ou égal\r au périmètre du territoire - 4\r (Les valeurs en X et Y doivent être mise\r pour pouvoir savoir la valeur maximale))"

        # Enter 5 -- Validation
        def get_inputEnergy():
            try:
                energyValue = int(txtEnergy.get())
                if(energyValue < 0):
                    raise ValueError
                if(energyValue < 100 or energyValue > 100000):
                    lblEnergyGood.configure(text="Cette valeur doit être entre 100 et 100 000", text_color="red")
                else:
                    lblEnergyGood.configure(text="")
                    return energyValue
            except ValueError:
                lblEnergyGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 6 -- Validation
        def get_inputSpeed():
            try:
                speedValue = int(txtSpeed.get())
                if(speedValue < 0):
                    raise ValueError
                if(speedValue > 100):
                    lblSpeedGood.configure(text="Cette valeur doit être inférieur ou égal à 100", text_color="red")
                else:
                    lblSpeedGood.configure(text="")
                    return speedValue
            except ValueError:
                lblSpeedGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 7 -- Validation
        def get_inputSense():
            try:
                senseValue = int(txtSense.get())
                if(senseValue < 0):
                    raise ValueError
                if(senseValue > 100):
                    lblSenseGood.configure(text="Cette valeur doit être plus petite ou égal 100", text_color="red")
                else:
                    lblSenseGood.configure(text="")
                    return senseValue
            except ValueError:
                lblSenseGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 8 -- Validation
        def get_inputSize():
            try:
                sizeValue = int(txtSize.get())
                if(sizeValue < 0):
                    raise ValueError
                if(sizeValue > 100):
                    lblSizeGood.configure(text="Cette valeur doit être plus petite ou égal 100", text_color="red")
                else:
                    lblSizeGood.configure(text="")
                    return sizeValue
            except ValueError:
                lblSizeGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 9 -- Validation
        def get_inputMutation():
            try:
                mutationValue = int(txtMutation.get())
                if(mutationValue < 0):
                    raise ValueError
                if(mutationValue < 0 or mutationValue > 100):
                    lblMutationGood.configure(text="Cette valeur doit être entre 0 et 100", text_color="red")
                else:
                    lblMutationGood.configure(text="")
                    return mutationValue
            except ValueError:
                lblMutationGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 10 -- Validation
        def get_inputGeneration():
            try:
                generationValue = int(txtGeneration.get())
                if(generationValue < 0):
                    raise ValueError
                if(generationValue < 1 or generationValue > 1000):
                    lblGenerationGood.configure(text="Cette valeur doit être entre 1 et 1 000", text_color="red")
                else:
                    lblGenerationGood.configure(text="")
                    return generationValue
            except ValueError:
                lblGenerationGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")


        # -------------------------------------------------
        def get_allBeforeSimulation():
            validMapSizeX = get_inputMapSizeX()
            validMapSizeY = get_inputMapSizeY()
            validStartFood = get_inputStartFood()
            validStartLulu = get_inputStartLulu()
            validEnergy = get_inputEnergy()
            validSpeed = get_inputSpeed()
            validSense = get_inputSense()
            validSize = get_inputSize()
            validMutation = get_inputMutation()
            validGeneration = get_inputGeneration()
            if(type(validMapSizeX) is int
               and type(validMapSizeY) is int
               and type(validStartFood) is int
               and type(validStartLulu) is int
               and type(validEnergy) is int
               and type(validSpeed) is int
               and type(validSense) is int
               and type(validSize) is int
               and type(validMutation) is int
               and type(validGeneration) is int):
                
                btnCancel.grid(row=12, column=0, columnspan=3, padx=20, pady=10, sticky="we")
                btnGraph.grid_remove()
                btnSave.grid_remove()
                btnSimulate.configure(state="disable")
                btnImport.configure(state="disable")

                #Simule
                th = threading.Thread(target=Simulation.__run__, args=(validMapSizeX, validMapSizeY, validStartFood, validStartLulu, validSpeed, validSense, validSize, validEnergy, validGeneration, validMutation))
                th.start()

                progress_bar.grid(row=14, column=0, columnspan=3, padx=20, pady=10, sticky="we")
                progress_bar.configure(maximum=validGeneration)
                while(th.is_alive()):
                    progress_var.set(float(Simulation.generation))
                    progress_bar.update()
                th.join()

                fg.generations = fg.objectsToCoordinates(Simulation.getGenerationsSave().generations)
                btnGraph.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="we")
                btnSave.grid(row=11, column=2, padx=20, pady=10, sticky="we")
                progress_bar.grid_remove()
                btnSimulate.configure(state="normal")
                btnImport.configure(state="normal")
                btnCancel.grid_remove()

                lblErrorInForm.configure(text="La simulation est terminée", text_color="green")
            else:
                lblErrorInForm.configure(text="Erreur: Veuillez remplir convenablement le formulaire", text_color="red")

        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(master=self.frame_1, variable=progress_var)
                  
        btnSimulate = ct.CTkButton(master=self.frame_1, text="Lancer la simulation", command=get_allBeforeSimulation)
        btnSimulate.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="we")

        def importSimulation():
            importData = loadData()
            if importData is not None:
                fg.generations = fg.objectsToCoordinates(importData.generations)
                changeInputs(importData)
                btnGraph.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="we")
            else:
                lblErrorInForm.configure(text="Erreur: Fichier non valide", text_color="red")

        def save():
            saveData(Simulation.getGenerationsSave())
            lblErrorInForm.configure(text="Le fichier a été sauvegardé.", text_color="green")

        def changeInputs(data):
            changeInputText(txtMapSizeX,str(data.sizeX))
            changeInputText(txtMapSizeY,str(data.sizeY))
            changeInputText(txtStartFood,str(data.nbFood))
            changeInputText(txtStartLulu,str(data.nbLulu))
            changeInputText(txtEnergy,str(data.energy))
            changeInputText(txtSpeed,str(data.varSpeed))
            changeInputText(txtSense,str(data.varSense))
            changeInputText(txtSize,str(data.varSize))
            changeInputText(txtMutation,str(data.mutationChance))
            changeInputText(txtGeneration,str(data.nbGen))
        
        def changeInputText(input,text):
            input.delete(0,'end')
            input.insert(0,text)
            
        # Graph
        def add_Graph():
            global canvasR
            index.azim = 130
            index.elev = 30
            index.setAxis()
            graphData = fg.graphGeneration.first(index)
            global ax
            ax = graphData[1]
            fig = graphData[0]
            canvasR = FigureCanvasTkAgg() 
            canvasG = FigureCanvasTkAgg(fig, self)
            canvasG.get_tk_widget().grid(row=0, column=0, columnspan=5, sticky="wesn")
            canvasR = canvasG

            def previous(canvas):
                if index.isMin():
                    return
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.previous(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def next(canvas):
                if index.isMax():
                    return
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.next(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def last(canvas):
                if index.isMax():
                    return
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.last(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def first(canvas):
                if index.isMin():
                    return
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.first(index)
                updateGraph(canvas, graphData)
                refreshButtons() 
            
            def speedSize(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.speedSize(index)
                updateGraph(canvas, graphData)
                refreshButtons()
            
            def sizeSense(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.sizeSense(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def senseSpeed(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                index.xaxis = ax.get_xlim()
                index.yaxis = ax.get_ylim()
                index.zaxis = ax.get_zlim()
                graphData = fg.graphGeneration.senseSpeed(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def remove_graph(canvas):
                canvas.get_tk_widget().destroy()
                btnPreviousGeneration.destroy()
                btnNextGeneration.destroy()
                btnLastGeneration.destroy()
                btnFirstGeneration.destroy()
                buttonDestroyGraph.destroy()
                buttonSpeedSize.destroy()
                buttonSenseSize.destroy()
                buttonSpeedSense.destroy()

            def updateGraph(canvas, graphData):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                fig = graphData[0]
                ax = graphData[1]
                global canvasR

                if canvasR != None:
                    canvasR.get_tk_widget().destroy()
                canvasR = None

                canvasR = FigureCanvasTkAgg(fig, self)
                canvasR.get_tk_widget().grid(row=0, column=0, columnspan=5, sticky="wesn")
            
            def refreshButtons():
                global buttonSpeedSize
                global buttonSenseSize
                global buttonSpeedSense
                if (buttonSpeedSize is not None):
                    buttonSpeedSize.destroy()
                if (buttonSenseSize is not None):
                    buttonSenseSize.destroy()
                if (buttonSpeedSense is not None):
                    buttonSpeedSense.destroy()
                buttonSpeedSize = ct.CTkButton(self, text="Vitesse - Taille", command=lambda:speedSize(canvasR), corner_radius=0)
                buttonSenseSize = ct.CTkButton(self, text="Taille - Vision", command=lambda:sizeSense(canvasR), corner_radius=0)
                buttonSpeedSense = ct.CTkButton(self, text="Vision - Vitesse", command=lambda:senseSpeed(canvasR), corner_radius=0)
                buttonSpeedSize.grid_configure(row=0, column=2, sticky="se", padx=5, pady=5)
                buttonSenseSize.grid_configure(row=0, column=3, sticky="se", padx=5, pady=5)
                buttonSpeedSense.grid_configure(row=0, column=4, sticky="se", padx=5, pady=5)

            def createButtons():
                btnPreviousGeneration.grid(row=1, column=3, padx=5, pady=10, sticky="we")
                btnNextGeneration.grid(row=1, column=4, padx=5, pady=10, sticky="we")
                btnLastGeneration.grid(row=1, column=2, padx=5, pady=10, sticky="we")
                btnFirstGeneration.grid(row=1, column=1, padx=5, pady=10, sticky="we")
                buttonDestroyGraph.grid(row=1, column=0, padx=10, pady=10, sticky="we")

            btnPreviousGeneration = ct.CTkButton(self, text="Génération Précédente", command=lambda:previous(canvasR))
            btnNextGeneration = ct.CTkButton(self, text="Prochaine Génération", command=lambda:next(canvasR))
            btnLastGeneration = ct.CTkButton(self, text="Dernière Génération", command=lambda:last(canvasR))
            btnFirstGeneration = ct.CTkButton(self, text="Première Génération", command=lambda:first(canvasR))
            buttonDestroyGraph = ct.CTkButton(self, text="Menu Principal", command=lambda:remove_graph(canvasR))
            global buttonSpeedSize
            global buttonSenseSize
            global buttonSpeedSense
            buttonSpeedSize = None
            buttonSenseSize = None
            buttonSpeedSense = None
            createButtons()
            refreshButtons()            

        btnImport = ct.CTkButton(master=self.frame_1, text="Importer une simulation...", command=importSimulation)
        btnImport.grid(row=10, column=2, padx=20, pady=10, sticky="we")

        btnGraph = ct.CTkButton(master=self.frame_1, text="Visualiser les graphiques", command=add_Graph)
        btnSave = ct.CTkButton(master=self.frame_1, text="Sauvegarder la simulation", command=save)

        global btnCancel
        btnCancel = ct.CTkButton(master=self.frame_1, text="Annuler la simulation", command=f.Form.cancelSimulation)

        global lblErrorInForm
        lblErrorInForm = ct.CTkLabel(master=self.frame_1, height=100, justify=ct.CENTER, text="")
        lblErrorInForm.grid(row=13, column=0, columnspan=3, padx=20, pady=10)
