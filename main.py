"""
#########################################

 Instituto Tecnológico de Costa Rica
 Área Académica de Ing. en Computadores

 Proyecto de Taller de programación con Python

 Estudiantes:
 David A. Leitón Flores - 2021103803
 Kevin E. Chinchilla Rodríguez - 2021101242+

#########################################
"""

# Librerias a utilizar en este proyecto
import tkinter as tk
from PIL import ImageTk, Image

# Creación de la ventana de trabajo.
window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 480)
window.resizable(False, False)
window.config()

# Intercambio entre canvas:
def intInfo():
    cPrincipal.pack_forget()
    cInfo.pack(side = "right")

# Creación de canvas

    # Canvas de la pantalla principal.
cPrincipal = tk.Canvas(window, bg = "blue",  width = 730, height = 450)
cInfo = tk.Canvas(window, bg = "blue",  width = 730, height = 450)

    # Widgets
        # Fondo de la pantalla principal
fondo = ImageTk.PhotoImage(Image.open("media/bgSpace.png"))
lFondo = tk.Label(cPrincipal, image = fondo, bg = "white")
lFondo.place(x = 0, y = 0)

        # Botones
imgJugar = ImageTk.PhotoImage(Image.open("media/botonJugar.png"))
bPlay = tk.Button(cPrincipal, image = imgJugar, width = 150, height = 76, borderwidth = 0, cursor = "hand2")
bPlay.place(x = 290, y = 270)

imgInfo = ImageTk.PhotoImage(Image.open("media/botonAcerca.png"))
bInfo = tk.Button(cPrincipal, image = imgInfo, width = 150, height = 76, borderwidth = 0, cursor = "hand2")
bInfo.place(x = 120, y = 270)

cPrincipal.pack(side = "right")




window.mainloop()