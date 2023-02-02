import customtkinter as ct
from PIL import Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import Graph2 as Graph
import FormGraph as fg

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

class Form(ct.CTk):
    width = 1920
    height = 1080

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        index = fg.Index()

        # Setup de base de l'interface
        self.geometry("900x700")
        self.title("Sélection naturel Form.py")
        self.resizable(True, True)
        self.maxsize(self.width, self.height)
        self.minsize(830, 700)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Ajout du background
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ct.CTkImage(Image.open(current_path + "/evo.jpeg"),
                                               size=(self.width, self.height))
        self.bg_image = ct.CTkLabel(self, image=self.bg_image, text="")
        self.bg_image.grid(row=0, column=0, sticky="nswe")
        self.bg_image.rowconfigure(0, weight=1)
        self.bg_image.columnconfigure(0, weight=1)

        # Ajout du frame
        self.frame_1 = ct.CTkFrame(master=self)
        self.frame_1.grid(row=0, column=0, sticky="ns")

        # Enter 1 -- MapSizeX
        lblMapSizeX = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille du territoire en x (en m)")
        lblMapSizeX.grid(row=0, column=0, pady=10, padx=10)
        txtMapSizeX = ct.CTkEntry(master=self.frame_1)
        txtMapSizeX.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        lblMapSizeXGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMapSizeXGood.grid(row=0, column=2, pady=10, padx=10)

        # Enter 2 -- MapSizeY
        lblMapSizeY = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Taille du territoire en y (en m)")
        lblMapSizeY.grid(row=1, column=0, pady=10, padx=10)
        txtMapSizeY = ct.CTkEntry(master=self.frame_1)
        txtMapSizeY.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        lblMapSizeYGood = ct.CTkLabel(master=self.frame_1, text="")
        lblMapSizeYGood.grid(row=1, column=2, pady=10, padx=10)

        # Enter 3 -- StartFood
        lblStartFood = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre de nourriture disponible \rau début")
        lblStartFood.grid(row=2, column=0, pady=10, padx=10)
        txtStartFood = ct.CTkEntry(master=self.frame_1)
        txtStartFood.grid(row=2, column=1, padx=20, pady=10, sticky="ew")
        lblStartFoodGood = ct.CTkLabel(master=self.frame_1, text="")
        lblStartFoodGood.grid(row=2, column=2, pady=10, padx=10)

        # Enter 4 -- StartLulu
        lblStartLulu = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre d'individu au début")
        lblStartLulu.grid(row=3, column=0, pady=10, padx=10)
        txtStartLulu = ct.CTkEntry(master=self.frame_1)
        txtStartLulu.grid(row=3, column=1, padx=20, pady=10, sticky="ew")
        lblStartLuluGood = ct.CTkLabel(master=self.frame_1, text="")
        lblStartLuluGood.grid(row=3, column=2, pady=10, padx=10)

        # Enter 5 -- Energy
        lblEnergy = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Énergie pour ce déplacer")
        lblEnergy.grid(row=4, column=0, pady=10, padx=10)
        txtEnergy = ct.CTkEntry(master=self.frame_1)
        txtEnergy.grid(row=4, column=1, padx=20, pady=10, sticky="ew")
        lblEnergyGood = ct.CTkLabel(master=self.frame_1, text="")
        lblEnergyGood.grid(row=4, column=2, pady=10, padx=10)

        # Enter 6 -- Speed
        lblSpeed = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Augmentation de la vitesse lors \rde la mutation (en %)")
        lblSpeed.grid(row=5, column=0, pady=10, padx=10)
        txtSpeed = ct.CTkEntry(master=self.frame_1)
        txtSpeed.grid(row=5, column=1, padx=20, pady=10, sticky="ew")
        lblSpeedGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSpeedGood.grid(row=5, column=2, pady=10, padx=10)

        # Enter 7 -- Sense
        lblSense = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Augmentation de la porté à laquel \rl'individu détecte la nourriture \rlors de la mutation (en %)")
        lblSense.grid(row=6, column=0, pady=10, padx=10)
        txtSense = ct.CTkEntry(master=self.frame_1)
        txtSense.grid(row=6, column=1, padx=20, pady=10, sticky="ew")
        lblSenseGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSenseGood.grid(row=6, column=2, pady=10, padx=10)

        # Enter 8 -- Size
        lblSize = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Poids supplémentaire lors de la \rprochaine mutation (en %)")
        lblSize.grid(row=7, column=0, pady=10, padx=10)
        txtSize = ct.CTkEntry(master=self.frame_1)
        txtSize.grid(row=7, column=1, padx=20, pady=10, sticky="ew")
        lblSizeGood = ct.CTkLabel(master=self.frame_1, text="")
        lblSizeGood.grid(row=7, column=2, pady=10, padx=10)

        # Enter 9 -- Generation
        lblGeneration = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="Nombre de génération")
        lblGeneration.grid(row=8, column=0, pady=10, padx=10)
        txtGeneration = ct.CTkEntry(master=self.frame_1)
        txtGeneration.grid(row=8, column=1, padx=20, pady=10, sticky="ew")
        lblGenerationGood = ct.CTkLabel(master=self.frame_1, text="")
        lblGenerationGood.grid(row=8, column=2, pady=10, padx=10)

        # Enter 1 -- Validation
        def get_inputMapSizeX():
            try:
                mapSizeXValue = int(txtMapSizeX.get())
                if(mapSizeXValue < 100 or mapSizeXValue > 1000000):
                    lblMapSizeXGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
                else:
                    lblMapSizeXGood.configure(text="")
                    print(mapSizeXValue)
                    return mapSizeXValue
            except ValueError:
                lblMapSizeXGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 2 -- Validation
        def get_inputMapSizeY():
            try:
                mapSizeYValue = int(txtMapSizeY.get())
                if(mapSizeYValue < 100 or mapSizeYValue > 1000000):
                    lblMapSizeYGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
                else:
                    lblMapSizeYGood.configure(text="")
                    print(mapSizeYValue)
                    return mapSizeYValue
            except ValueError:
                lblMapSizeYGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 3 -- Validation
        def get_inputStartFood():
            try:
                startFoodValue = int(txtStartFood.get())
                try:
                    mapSizeXValue = get_inputMapSizeX()
                    mapSizeYValue = get_inputMapSizeY()
                    maxFood = mapSizeXValue * mapSizeYValue * 0.50
                    if(startFoodValue > maxFood):
                        lblStartFoodGood.configure(text="Cette valeur doit être inférieur ou égal à " 
                                                + str(int(maxFood)) + "\r(Cette valeur dépend de la taille du territoire)", text_color="red")
                    else:
                        lblStartFoodGood.configure(text="")
                        print(startFoodValue)
                        return startFoodValue
                except TypeError:
                    lblStartFoodGood.configure(text="Les tailles du territoire doivent être valide" + 
                                               "\ravant de choisir le nombre de nourriture", text_color="red")
            except ValueError:
                lblStartFoodGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 4 -- Validation
        def get_inputStartLulu():
            try:
                startLuluValue = int(txtStartLulu.get())
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
                lblStartLuluGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 5 -- Validation
        def get_inputEnergy():
            try:
                energyValue = int(txtEnergy.get())
                if(energyValue < 100 or energyValue > 1000000):
                    lblEnergyGood.configure(text="Cette valeur doit être entre 100 et 1 000 000", text_color="red")
                else:
                    lblEnergyGood.configure(text="")
                    print(energyValue)
                    return energyValue
            except ValueError:
                lblEnergyGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 6 -- Validation
        def get_inputSpeed():
            try:
                speedValue = int(txtSpeed.get())
                if(speedValue > 33):
                    lblSpeedGood.configure(text="Cette valeur doit être plus petite ou égal à 33", text_color="red")
                else:
                    lblSpeedGood.configure(text="")
                    print(speedValue)
                    return speedValue
            except ValueError:
                lblSpeedGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 7 -- Validation
        def get_inputSense():
            try:
                senseValue = int(txtSense.get())
                if(senseValue > 33):
                    lblSenseGood.configure(text="Cette valeur doit être plus petite ou égal à 33", text_color="red")
                else:
                    lblSenseGood.configure(text="")
                    print(senseValue)
                    return senseValue
            except ValueError:
                lblSenseGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 8 -- Validation
        def get_inputSize():
            try:
                sizeValue = int(txtSize.get())
                if(sizeValue > 33):
                    lblSizeGood.configure(text="Cette valeur doit être plus petite ou égal à 33", text_color="red")
                else:
                    lblSizeGood.configure(text="")
                    print(sizeValue)
                    return sizeValue
            except ValueError:
                lblSizeGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

        # Enter 9 -- Validation
        def get_inputGeneration():
            try:
                generationValue = int(txtGeneration.get())
                if(generationValue < 1 or generationValue > 1000000):
                    lblGenerationGood.configure(text="Cette valeur doit être entre 1 et 1 000 000", text_color="red")
                else:
                    lblGenerationGood.configure(text="")
                    print(generationValue)
                    return generationValue
            except ValueError:
                lblGenerationGood.configure(text="Ce n'est pas un nombre entier", text_color="red")

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
               and type(validGeneration) is int):
                
                #Simule
                #__run__(validMapSizeX, validMapSizeY, validStartFood, validStartLulu, validSpeed, validSense, validSize, validEnergy, validGeneration)
                lblErrorInForm.configure(text="OK", text_color="green")
            else:
                lblErrorInForm.configure(text="Error: Veuillez remplir convenablement le formulaire", text_color="red")
                  
        btnSimulate = ct.CTkButton(master=self.frame_1, text="Lancer la simulation", command=get_allBeforeSimulation)
        btnSimulate.grid(row=9, column=0, padx=20, pady=10, sticky="we")

        def previous():
            fig = fg.graphGeneration.previous(index)
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        def next():
            fig = fg.graphGeneration.next(index)
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        def last():
            fig = fg.graphGeneration.last(index)
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        def first():
            fig = fg.graphGeneration.first(index)
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().grid(row=0, column=0, columnspan=4, padx=20, pady=10)
    
        # Graph
        def add_Graph():
            # def remove_graph():
            #     canvas.get_tk_widget().destroy()
            #     buttonDestroyGraph.destroy()
            #     btnPreviousGeneration.destroy()
            #     btnNextGeneration.destroy()
            #     btnLastGeneration.destroy()
            #     btnFirstGeneration.destroy()
            first()
            btnPreviousGeneration = ct.CTkButton(self, text="Génération Précédente", command=previous)
            btnPreviousGeneration.grid(row=1, column=0, padx=20, pady=10, sticky="we")

            btnNextGeneration = ct.CTkButton(self, text="Prochaine Génération", command=next)
            btnNextGeneration.grid(row=1, column=1, padx=20, pady=10, sticky="we")

            btnLastGeneration = ct.CTkButton(self, text="Dernière Génération", command=last)
            btnLastGeneration.grid(row=1, column=2, padx=20, pady=10, sticky="we")

            btnFirstGeneration = ct.CTkButton(self, text="Première Génération", command=first)
            btnFirstGeneration.grid(row=1, column=3, padx=20, pady=10, sticky="we")

            # buttonDestroyGraph = ct.CTkButton(self, text="Remove Graph", command=remove_graph)
            # buttonDestroyGraph.grid(row=2, column=0, padx=20, pady=10, sticky="we")

        btnGraph = ct.CTkButton(master=self.frame_1, text="Visualiser les graphiques", command=add_Graph)
        btnGraph.grid(row=9, column=1, padx=20, pady=10, sticky="we")

        lblErrorInForm = ct.CTkLabel(master=self.frame_1, justify=ct.CENTER, text="")
        lblErrorInForm.grid(row=9, column=2, padx=20, pady=10)

if __name__ == "__main__":
    app = Form()
    app.mainloop()