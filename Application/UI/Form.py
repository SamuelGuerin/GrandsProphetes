import customtkinter as ct
from PIL import Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import FormGraph as fg
from JsonManager import saveData, loadData

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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        index = fg.Index()

        width = 1920
        height = 1080
        

        # Setup de base de l'interface
        self.geometry("900x800")
        self.title("Sélection naturel Form.py")
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
            lblErrorInForm.configure(text=txt, corner_radius=90, text_color="green", fg_color="#343638")

        def hide_info(event):
            lblErrorInForm.configure(text="", fg_color="#2b2b2b")

        # Créer une image pour le bouton
        current_path = os.path.dirname(os.path.realpath(__file__))
        circle_image = ct.CTkImage(Image.open(current_path + "/circle.png"))

        # Enter 1 -- MapSizeX
        lblMapSizeX = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille X du territoire")
        lblMapSizeX.grid(row=0, column=0, pady=10, padx=10)

        infoMapSizeX = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMapSizeX.grid(row=0, column=1, pady=10, padx=10)
        infoMapSizeX.bind("<Enter>", lambda event: show_info(event, "Ce champs va déterminer la grandeur du territoire en X.\r (Cette valeur doit être entre 100 et 1 000 000)"))
        infoMapSizeX.bind("<Leave>", hide_info)

        txtMapSizeX = ct.CTkEntry(master=self.frame_1)
        txtMapSizeX.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

        lblMapSizeXGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMapSizeXGood.grid(row=0, column=3, pady=10, padx=10)


        # Enter 2 -- MapSizeY
        lblMapSizeY = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille Y du territoire")
        lblMapSizeY.grid(row=1, column=0, pady=10, padx=10)

        infoMapSizeY = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMapSizeY.grid(row=1, column=1, pady=10, padx=10)
        infoMapSizeY.bind("<Enter>", lambda event: show_info(event, "Ce champs va déterminer la grandeur du territoire en Y.\r (Cette valeur doit être entre 100 et 1 000 000)"))
        infoMapSizeY.bind("<Leave>", hide_info)

        txtMapSizeY = ct.CTkEntry(master=self.frame_1)
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

        txtStartFood = ct.CTkEntry(master=self.frame_1)
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

        txtStartLulu = ct.CTkEntry(master=self.frame_1)
        txtStartLulu.grid(row=3, column=2, padx=20, pady=10, sticky="ew")

        lblStartLuluGood = ct.CTkLabel(master=self.frame_1, text="")
        lblStartLuluGood.grid(row=3, column=3, pady=10, padx=10)

        # Enter 5 -- Energy
        lblEnergy = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Énergie des Lulus")
        lblEnergy.grid(row=4, column=0, pady=10, padx=10)

        infoEnergy = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoEnergy.grid(row=4, column=1, pady=10, padx=10)
        infoEnergy.bind("<Enter>", lambda event: show_info(event, "Ce champs représente le nombre mouvement\r que les Lulus pourront faire lors d'une génération.\r (Cette valeur doit être entre 100 et 1 000 000)"))
        infoEnergy.bind("<Leave>", hide_info)

        txtEnergy = ct.CTkEntry(master=self.frame_1)
        txtEnergy.grid(row=4, column=2, padx=20, pady=10, sticky="ew")

        lblEnergyGood = ct.CTkLabel(master=self.frame_1, text="")
        lblEnergyGood.grid(row=4, column=3, pady=10, padx=10)

        # Enter 6 -- Speed
        lblSpeed = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la vitesse lors \rde la mutation (en %)")
        lblSpeed.grid(row=5, column=0, pady=10, padx=10)

        infoSpeed = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSpeed.grid(row=5, column=1, pady=10, padx=10)
        infoSpeed.bind("<Enter>", lambda event: show_info(event, "Ce champs représente la variation\r de leur vitesse en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 33)"))
        infoSpeed.bind("<Leave>", hide_info)

        txtSpeed = ct.CTkEntry(master=self.frame_1)
        txtSpeed.grid(row=5, column=2, padx=20, pady=10, sticky="ew")

        lblSpeedGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSpeedGood.grid(row=5, column=3, pady=10, padx=10)

        # Enter 7 -- Sense
        lblSense = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la vision lors \rde la mutation (en %)")
        lblSense.grid(row=6, column=0, pady=10, padx=10)

        infoSense = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSense.grid(row=6, column=1, pady=10, padx=10)
        infoSense.bind("<Enter>", lambda event: show_info(event, "Ce champs représente la variation\r de leur vision en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 33)"))
        infoSense.bind("<Leave>", hide_info)

        txtSense = ct.CTkEntry(master=self.frame_1)
        txtSense.grid(row=6, column=2, padx=20, pady=10, sticky="ew")

        lblSenseGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSenseGood.grid(row=6, column=3, pady=10, padx=10)

        # Enter 8 -- Size
        lblSize = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Variation de la taille lors \rde la mutation (en %)")
        lblSize.grid(row=7, column=0, pady=10, padx=10)

        infoSize = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoSize.grid(row=7, column=1, pady=10, padx=10)
        infoSize.bind("<Enter>", lambda event: show_info(event, "Ce champs représente la variation\r de leur taille en % si une mutation est effectuée.\r (Cette valeur doit être inférieur ou égal à 33)"))
        infoSize.bind("<Leave>", hide_info)

        txtSize = ct.CTkEntry(master=self.frame_1)
        txtSize.grid(row=7, column=2, padx=20, pady=10, sticky="ew")

        lblSizeGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSizeGood.grid(row=7, column=3, pady=10, padx=10)

        # Entrer 9 -- Mutation
        lblMutation = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="% de chance de mutation\r lors de la reproduction")
        lblMutation.grid(row=8, column=0, pady=10, padx=10)

        infoMutation = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoMutation.grid(row=8, column=1, pady=10, padx=10)
        infoMutation.bind("<Enter>", lambda event: show_info(event, "Ce champs représente le % de chance qu'une mutation\r soit effectuée lors de la reproduction.\r (Cette valeur doit être entre 1 et 100)"))
        infoMutation.bind("<Leave>", hide_info)

        txtMutation = ct.CTkEntry(master=self.frame_1)
        txtMutation.grid(row=8, column=2, padx=20, pady=10, sticky="ew")

        lblMutationGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMutationGood.grid(row=8, column=3, pady=10, padx=10)

        # Enter 10 -- Generation
        lblGeneration = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre de générations")
        lblGeneration.grid(row=9, column=0, pady=10, padx=10)

        infoGeneration = ct.CTkButton(master=self.frame_1, image=circle_image, text="", fg_color="#2b2b2b", width=10, state="disabled")
        infoGeneration.grid(row=9, column=1, pady=10, padx=10)
        infoGeneration.bind("<Enter>", lambda event: show_info(event, "Ce champs représente le nombre de générations\r qui sera effectuées lors de la simulation.\r (Cette valeur doit être entre 1 et 1 000 000)"))
        infoGeneration.bind("<Leave>", hide_info)

        txtGeneration = ct.CTkEntry(master=self.frame_1)
        txtGeneration.grid(row=9, column=2, padx=20, pady=10, sticky="ew")

        lblGenerationGood = ct.CTkLabel(master=self.frame_1, text="")
        lblGenerationGood.grid(row=9, column=3, pady=10, padx=10)

        # Enter 1 -- Validation
        def get_inputMapSizeX():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                if(mapSizeXValue < 0):
                    raise ValueError
                if(mapSizeXValue < 100 or mapSizeXValue > 1000000):
                    lblMapSizeXGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
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
                if(mapSizeYValue < 100 or mapSizeYValue > 1000000):
                    lblMapSizeYGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
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
                    lblStartFoodGood.configure(text="Les tailles du territoire doivent être valide" + 
                                               "\ravant de choisir le nombre de nourriture", text_color="red")
            except ValueError:
                lblStartFoodGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        def get_infoStartFood():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                mapSizeYValue = int(txtMapSizeY.get()) 
                if(mapSizeXValue < 0 or mapSizeYValue < 0):
                    raise ValueError
                maxFood = mapSizeXValue * mapSizeYValue * 0.50
                return "Ce champs représente le nombre\r de nourriture présent sur le territoire.\r (Le nombre de nourriture doit être inférieur ou égal\r à 50% du territoire soit " + str(int(maxFood) + ")")
            except ValueError:
                return "Ce champs représente le nombre\r de nourriture présent sur le territoire.\r (Le nombre de nourriture doit être inférieur ou égal\r à 50% du territoire\r(Les valeur en X et Y doivent être mise\r pour pouvoir savoir la valeur maximal))"

        # Enter 4 -- Validation
        def get_inputStartLulu():
            try:
                startLuluValue = int(txtStartLulu.get())
                if(startLuluValue < 0):
                    raise ValueError
                try:
                    mapSizeXValue = get_inputMapSizeX()
                    mapSizeYValue = get_inputMapSizeY()
                    maxLulu = mapSizeXValue * mapSizeYValue * 0.75
                    if(startLuluValue > maxLulu):
                        lblStartLuluGood.configure(text="Cette valeur doit être inférieur ou égal à " 
                                                + str(int(maxLulu)) + "\r(Cette valeur dépend de la taille du territoire)", text_color="red")
                    else:
                        lblStartLuluGood.configure(text="")
                        print(startLuluValue)
                        return startLuluValue
                except TypeError:
                    lblStartLuluGood.configure(text="Les tailles du territoire doivent être valide" + 
                                               "\ravant de choisir le nombre de lulu", text_color="red")
            except ValueError:
                lblStartLuluGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        def get_infoStartLulu():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                mapSizeYValue = int(txtMapSizeY.get()) 
                if(mapSizeXValue < 0 or mapSizeYValue < 0):
                    raise ValueError
                maxLulu = mapSizeXValue * mapSizeYValue * 0.75
                return "Ce champs représente le nombre\r de Lulus présent sur le territoire au début.\r (Le nombre de Lulus doit être inférieur ou égal\r à 75% du territoire soit " + str(int(maxLulu) + ")")
            except ValueError:
                return "Ce champs représente le nombre\r de Lulus présent sur le territoire au début.\r (Le nombre de Lulus doit être inférieur ou égal\r à 75% du territoire\r(Les valeur en X et Y doivent être mise\r pour pouvoir savoir la valeur maximal))"

        # Enter 5 -- Validation
        def get_inputEnergy():
            try:
                energyValue = int(txtEnergy.get())
                if(energyValue < 0):
                    raise ValueError
                if(energyValue < 100 or energyValue > 1000000):
                    lblEnergyGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
                else:
                    lblEnergyGood.configure(text="")
                    print(energyValue)
                    return energyValue
            except ValueError:
                lblEnergyGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 6 -- Validation
        def get_inputSpeed():
            try:
                speedValue = int(txtSpeed.get())
                if(speedValue < 0):
                    raise ValueError
                if(speedValue > 33):
                    lblSpeedGood.configure(text="Cette valeur doit être inférieur ou égal à 33", text_color="red")
                else:
                    lblSpeedGood.configure(text="")
                    print(speedValue)
                    return speedValue
            except ValueError:
                lblSpeedGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 7 -- Validation
        def get_inputSense():
            try:
                senseValue = int(txtSense.get())
                if(senseValue < 0):
                    raise ValueError
                if(senseValue > 33):
                    lblSenseGood.configure(text="Cette valeur doit être plus petite ou égal à 33", text_color="red")
                else:
                    lblSenseGood.configure(text="")
                    print(senseValue)
                    return senseValue
            except ValueError:
                lblSenseGood.configure(text="Ce n'est pas un nombre entier positif", text_color="red")

        # Enter 8 -- Validation
        def get_inputSize():
            try:
                sizeValue = int(txtSize.get())
                if(sizeValue < 0):
                    raise ValueError
                if(sizeValue > 33):
                    lblSizeGood.configure(text="Cette valeur doit être plus petite ou égal à 33", text_color="red")
                else:
                    lblSizeGood.configure(text="")
                    print(sizeValue)
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
                if(generationValue < 1 or generationValue > 1000000):
                    lblGenerationGood.configure(text="Cette valeur doit être entre 1 et 1 000 000", text_color="red")
                else:
                    lblGenerationGood.configure(text="")
                    print(generationValue)
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
            print(validMapSizeX)
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
                
                #Simule
                #__run__(validMapSizeX, validMapSizeY, validStartFood, validStartLulu, validSpeed, validSense, validSize, validEnergy, validGeneration)

                #__run__(validMapSizeX, validMapSizeY, validStartFood, validStartLulu, validSpeed, validSense, validSize, validEnergy, validGeneration, validMutation)
                fg.generations = fg.objectsToCoordinates(fg.generateLulus())
                btnGraph.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="we")
                btnSave.grid(row=11, column=2, padx=20, pady=10, sticky="we")

                lblErrorInForm.configure(text="OK", text_color="green")
            else:
                #fg.generations = fg.objectsToCoordinates(fg.generateLulus())
                #btnGraph.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="we")
                #btnSave.grid(row=11, column=2, padx=20, pady=10, sticky="we")
                lblErrorInForm.configure(text="Erreur: Veuillez remplir convenablement le formulaire", text_color="red")
                  
        btnSimulate = ct.CTkButton(master=self.frame_1, text="Lancer la simulation", command=get_allBeforeSimulation)
        btnSimulate.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="we")

        def importSimulation():
            btnGraph.grid_remove()
            btnSave.grid_remove()

            fg.generations = loadData()
            if fg.generations is not None:
                add_Graph()
    
        # Graph
        def add_Graph():
            global canvasR
            graphData = fg.graphGeneration.first(index)
            index.elev = 30
            index.azim = 130
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
                graphData = fg.graphGeneration.first(index)
                updateGraph(canvas, graphData)
                refreshButtons() 
            
            def speedSize(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                graphData = fg.graphGeneration.speedSize(index)
                updateGraph(canvas, graphData)
                refreshButtons()
            
            def sizeSense(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
                graphData = fg.graphGeneration.sizeSense(index)
                updateGraph(canvas, graphData)
                refreshButtons() 

            def senseSpeed(canvas):
                global ax
                canvas.get_tk_widget().destroy()
                index.elev = ax.elev
                index.azim = ax.azim
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
                canvasN = FigureCanvasTkAgg(fig, self)
                canvasN.get_tk_widget().grid(row=0, column=0, columnspan=5, sticky="wesn")
                global canvasR
                canvasR = canvasN
            
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

        def preview():
            current_path = os.path.dirname(os.path.realpath(__file__))
            preview = ct.CTkImage(Image.open(current_path + "/preview.png"), size=(700, 350))
            previewImage = ct.CTkLabel(master=self, text="", image=preview)
            previewImage.grid(row=0, column=0, sticky="snwe")
            btnClose = ct.CTkButton(master=self, text="Fermer la prévisualisation", command=lambda:closePreview(previewImage, btnClose))
            btnClose.grid(row=1, column=0, padx=20, pady=10, sticky="we")

        def closePreview(previewImage, btnClose):
            previewImage.destroy()
            btnClose.destroy()

        btnImport = ct.CTkButton(master=self.frame_1, text="Importer une Simulation...", command=importSimulation)
        btnImport.grid(row=10, column=2, padx=20, pady=10, sticky="we")

        btnGraph = ct.CTkButton(master=self.frame_1, text="Visualiser les graphiques", command=add_Graph)
        btnSave = ct.CTkButton(master=self.frame_1, text="Sauvegarder la simulation", command=lambda:saveData(fg.generations))

        btnPreview = ct.CTkButton(master=self.frame_1, text="Prévisualiser le Territoire", command=preview)
        btnPreview.grid(row=12, column=0, columnspan=3, padx=20, pady=10, sticky="we")

        lblErrorInForm = ct.CTkLabel(master=self.frame_1, height=100, justify=ct.CENTER, text="")
        lblErrorInForm.grid(row=13, column=0, columnspan=3, padx=20, pady=10)

if __name__ == "__main__":
    app = Form()
    app.mainloop()