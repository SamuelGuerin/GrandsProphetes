import tkinter as tk
import customtkinter as ct
import os


import ctypes

s = "42"

u = ctypes.c_uint(int(s)).value

print(u)

def show_info(event, txt):
    x, y = event.x_root, event.y_root
    info_label.configure(text=txt)
    info_label.place(x=x + 10, y=y + 10, anchor="nw")

def hide_info(event):
    info_label.configure(text="")

root = tk.Tk()
root.minsize(830, 700)

# Créer une image pour le bouton
current_path = os.path.dirname(os.path.realpath(__file__))
#circle_image = ct.CTkImage(Image.open(current_path + "/circle.png")
circle_image = tk.PhotoImage(file=current_path +"/circle.png")
# Créer le bouton
info_button = tk.Button(root, image=circle_image)
info_button.config(highlightthickness=0, highlightbackground="black", bd=0, relief="flat")
info_button.pack()

# Lier les actions pour l'apparition et la disparition de la bulle d'aide
info_button.bind("<Enter>", lambda event: show_info(event, "Ceci est une bulle d'aide d'informations."))
info_button.bind("<Leave>", hide_info)

# Créer la bulle d'aide
info_label = ct.CTkLabel(root, text="", text_color="white", bg_color="black")

root.mainloop()

