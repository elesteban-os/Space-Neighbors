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

# Importación de imágenes
fondo = ImageTk.PhotoImage(Image.open("media/bgSpace.png"))
imgJugar = ImageTk.PhotoImage(Image.open("media/botonJugar.png"))
imgInfo = ImageTk.PhotoImage(Image.open("media/botonAcerca.png"))
imgPuntajes = ImageTk.PhotoImage(Image.open("media/botonPuntajes.png"))
flechas = ImageTk.PhotoImage(Image.open("media/teclas.png"))
imgAtras = ImageTk.PhotoImage(Image.open("media/botonAtras.png"))
imgHistoria = ImageTk.PhotoImage(Image.open("media/botonHistoria.png"))
imgNiveles = ImageTk.PhotoImage(Image.open("media/botonNiveles.png"))
imgNivel1 = ImageTk.PhotoImage(Image.open("media/botonNivel1.png"))
imgNivel2 = ImageTk.PhotoImage(Image.open("media/botonNivel2.png"))
imgNivel3 = ImageTk.PhotoImage(Image.open("media/botonNivel3.png"))

# Intercambio entre canvas:
def interInfo():
    cPrincipal.pack_forget()
    cInfo.pack(side = "right")

def interPrin():
    cInfo.pack_forget()
    cJuego.pack_forget()
    cPrincipal.pack(side = "right")

def interJuego():
    cPrincipal.pack_forget()
    cJuego.pack(side = "right")

def interHistoria():
    cJuego.pack_forget()
    cHistoria.pack(side="right")

def interNiveles():
    cJuego.pack_forget()
    cniveles.pack(side="right")

def interNivel1():
    cniveles.pack_forget()

def interNivel2():
    cniveles.pack_forget()

def interNivel3():
    cniveles.pack_forget()

def volverJuego():
    cHistoria.pack_forget()
    cniveles.pack_forget()
    cJuego.pack(side="right")

def volverNiveles():
    cNivel1.pack_forget()
    cNivel2.pack_forget()
    cNivel3.pack_forget()
    cniveles.pack(side="right")

# Creación de canvas

    # Canvas de la pantalla principal.
cPrincipal = tk.Canvas(window,  width = 730, height = 450)

    # Widgets
        # Fondo de la pantalla principal
lFondo = tk.Label(cPrincipal, image = fondo, bg = "white")
lFondo.place(x = 0, y = 0)

        # Botones
bPlay = tk.Button(cPrincipal, image = imgJugar, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interJuego)
bPlay.place(x = 290, y = 270)

bInfo = tk.Button(cPrincipal, image = imgInfo, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interInfo)
bInfo.place(x = 120, y = 270)

bPuntajes = tk.Button(cPrincipal, image = imgPuntajes, width = 150, height = 76, borderwidth = 0, cursor = "hand2")
bPuntajes.place(x = 460, y = 270)


#-----Configuracion canva About-----
# Canvas
cInfo = tk.Canvas(window,  width = 730, height = 450)

# Widgets
lFondoinf = tk.Label(cInfo, image = fondo, bg = "white")
lFondoinf.place(x = 0, y = 0)

lteclasinf = tk.Label(cInfo, image = flechas, bg = "white", borderwidth = 0)
lteclasinf.place(x = 380, y = 80)

credits_ = tk.Label(cInfo,text = """

País:
Costa Rica

Universidad y carrera:
Instituto Tecnológico de Costa Rica
Computer Engineering

Asignatura, año que cursa y grupo:
Taller de programación
2021
Grupo 1

Profesor:
Jeff Schmidt

Versión programa:
1.0

Desarrolladores:
David Leiton
Kevin Chinchilla

Autores de módulos modificados:--------
""", bg = "black", fg = "white", font = ("fixedsys", 10))
credits_.place(x=25,y=10)

bvolver = tk.Button(cInfo, image = imgAtras, width = 120, height = 60, borderwidth = 0, cursor = "hand2", command = interPrin)
bvolver.place(x = 4, y = 4)

# Configuración de "Jugar"
# Canvas
cJuego = tk.Canvas(window,  width = 730, height = 450, bg= "black")
cniveles  = tk.Canvas(window,  width = 730, height = 450, bg= "black")
cHistoria = tk.Canvas(window,  width = 730, height = 450, bg= "black")

# Widgets
bhistoria = tk.Button(cJuego ,image = imgHistoria, borderwidth = 0, width = 150, height = 76, command = interHistoria)
bhistoria.place(x = 100, y = 270)

bNiveles = tk.Button(cJuego ,image = imgNiveles, width = 150, height = 76, borderwidth = 0, command = interNiveles)
bNiveles.place(x = 300, y = 270)

bvolver1 = tk.Button(cJuego ,image = imgAtras , width = 120, height = 60, borderwidth = 0, command = interPrin)
bvolver1.place(x = 4, y = 4)

bLevel1 = tk.Button(cniveles ,image = imgNivel1, width = 150, height = 76, borderwidth = 0, command = interNivel1)
bLevel1.place(x = 100, y = 270)

bLevel2 = tk.Button(cniveles ,image = imgNivel2, width = 150, height = 76, borderwidth = 0,command = interNivel2)
bLevel2.place(x = 290, y = 270)

bLevel3 = tk.Button(cniveles ,image = imgNivel3, width = 150, height = 76, borderwidth = 0, command = interNivel3)
bLevel3.place(x = 480, y = 270)

#Botenes de atras
bvolverHis = tk.Button(cHistoria ,image = imgAtras , width = 120, height = 60, borderwidth = 0, command = volverJuego)
bvolverHis.place(x = 4, y = 4)

bvolverN = tk.Button(cniveles ,image = imgAtras , width = 120, height = 60, borderwidth = 0, command = volverJuego)
bvolverN.place(x = 4, y = 4)

cPrincipal.pack(side = "right")

window.mainloop()
