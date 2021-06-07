"""
#########################################

 Instituto Tecnológico de Costa Rica
 Área Académica de Ing. en Computadores

 Proyecto de Taller de programación con Python

 Estudiantes:
 David A. Leitón Flores - 2021103803
 Kevin E. Chinchilla Rodríguez - 2021101242

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

# imagenes:
imgNivel1 = ImageTk.PhotoImage(Image.open("media/botonNivel1.png"))
imgNivel2 = ImageTk.PhotoImage(Image.open("media/botonNivel2.png"))
imgNivel3 = ImageTk.PhotoImage(Image.open("media/botonNivel3.png"))

# Intercambio entre canvas:
def interInfo():
    cPrincipal.pack_forget()
    cInfo.pack(side = "right")


def interInfoAprin():#Se devuelve a principal, este en jugar o en acerca de
    cInfo.pack_forget()
    cJuego.pack_forget()
    cPrincipal.pack(side = "right")

def interJuego():
    cPrincipal.pack_forget()
    cJuego.pack(side = "right")

def interHistoria():
    cJuego.pack_forget()
    cHistoria.pack(side = "right")
def interNiveles():
    cJuego.pack_forget()
    cniveles.pack(side="right")

def interNivel1():
    cniveles.pack_forget()
    cNivel1.pack(side = "right")

def interNivel2():
    cniveles.pack_forget()
    cNivel2.pack(side = "right")

def interNivel3():
    cniveles.pack_forget()
    cNivel3.pack(side = "right")

def volverJuego():
    cHistoria.pack_forget()
    cniveles.pack_forget()
    cJuego.pack(side = "right")

def volverNiveles():
    cNivel1.pack_forget()
    cNivel2.pack_forget()
    cNivel3.pack_forget()
    cniveles.pack(side = "right")


# Creación de canvas

    # Canvas de la pantalla principal.
    
cPrincipal = tk.Canvas(window,  width = 730, height = 450)

cJuego = tk.Canvas(window,  width = 730, height = 450, bg= "black")
    #canvas en jugar
cHistoria = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cniveles  = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel1 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel2 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel3 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cInfo = tk.Canvas(window,  width = 730, height = 450, bg= "black")

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

    # Widgets
        # Fondo de la pantalla principal
fondo = ImageTk.PhotoImage(Image.open("media/bgSpace.png"))
lFondo = tk.Label(cPrincipal, image = fondo, bg = "white")
lFondo.place(x = 0, y = 0)

        # Botones
imgJugar = ImageTk.PhotoImage(Image.open("media/botonJugar.png"))
bPlay = tk.Button(cPrincipal, image = imgJugar, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interJuego)
bPlay.place(x = 290, y = 270)

imgInfo = ImageTk.PhotoImage(Image.open("media/botonAcerca.png"))

bInfo = tk.Button(cPrincipal, image = imgInfo, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interInfo)
bInfo.place(x = 120, y = 270)

bvolver = tk.Button(cInfo ,text="Volver", borderwidth = 0, command = interInfoAprin)
bvolver.place(x = 4, y = 4)

flechas = ImageTk.PhotoImage(Image.open("media/teclas.png"))
fteclas=cInfo.create_image(400, 30, image=flechas, anchor="nw")

#botones canva juego modo historia y niveles

bhistoria = tk.Button(cJuego ,text="Modo Historia", borderwidth = 0,font=("Rockwell", 15), command = interHistoria)
bhistoria.place(x = 100, y = 270)

bNiveles = tk.Button(cJuego ,text="Niveles", borderwidth = 0,font=("Rockwell", 15), command = interNiveles)
bNiveles.place(x = 300, y = 270)

bLevel1 = tk.Button(cniveles ,image = imgNivel1, width = 150, height = 76, borderwidth = 0, command = interNivel1)
bLevel1.place(x = 100, y = 270)

bLevel2 = tk.Button(cniveles ,image = imgNivel2, width = 150, height = 76, borderwidth = 0,command = interNivel2)
bLevel2.place(x = 290, y = 270)

bLevel3 = tk.Button(cniveles ,text="Nivel 3", borderwidth = 0,font=("Rockwell", 15), command = interNivel3)
bLevel3.place(x = 600, y = 270)

#Botenes de atras
bvolverHis = tk.Button(cHistoria ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverJuego)
bvolverHis.place(x = 4, y = 4)

bvolverN = tk.Button(cniveles ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverJuego)
bvolverN.place(x = 4, y = 4)

bvolverN1 = tk.Button(cNivel1 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN1.place(x = 4, y = 4)

bvolverN2 = tk.Button(cNivel2 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN2.place(x = 4, y = 4)

bvolverN2 = tk.Button(cNivel3 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN2.place(x = 4, y = 4)

#boton Volver del juego a menu
bvolver1 = tk.Button(cJuego ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = interInfoAprin)
bvolver1.place(x = 4, y = 4)


cPrincipal.pack(side = "right")

window.mainloop()
