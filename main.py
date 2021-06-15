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
import random
from tkinter import messagebox
import pygame, sys
from pygame.locals import *
from threading import Thread
import time
from player import *
from enemies import *
from fondo import *
from juego import *

#------------globales------por el momento
nav=0
nav1=0
nav2=0

# Creación de la ventana de trabajo.
window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 450)
window.resizable(False, False)
window.config()

# Importación de imágenes
fondo = ImageTk.PhotoImage(Image.open("media/bgSpace.png"))
imgJugar = ImageTk.PhotoImage(Image.open("media/botonJugar.png"))
imgInfo = ImageTk.PhotoImage(Image.open("media/botonAcerca.png"))
imgPuntajes = ImageTk.PhotoImage(Image.open("media/botonPuntajes.png"))
flechas = ImageTk.PhotoImage(Image.open("media/teclas.png"))
imgNave1 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))
imgNave2 = ImageTk.PhotoImage(Image.open("media/imgNave2.png"))
imgNave3 = ImageTk.PhotoImage(Image.open("media/imgNave3.png"))
imgAtras = ImageTk.PhotoImage(Image.open("media/botonAtras.png"))
imgHistoria = ImageTk.PhotoImage(Image.open("media/botonHistoria.png"))
imgNiveles = ImageTk.PhotoImage(Image.open("media/botonNiveles.png"))
imgNivel1 = ImageTk.PhotoImage(Image.open("media/botonNivel1.png"))
imgNivel2 = ImageTk.PhotoImage(Image.open("media/botonNivel2.png"))
imgNivel3 = ImageTk.PhotoImage(Image.open("media/botonNivel3.png"))
N1 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))
N2 = ImageTk.PhotoImage(Image.open("media/imgNave2.png"))
N3 = ImageTk.PhotoImage(Image.open("media/imgNave3.png"))
N11 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))
N22 = ImageTk.PhotoImage(Image.open("media/imgNave2.png"))
N33 = ImageTk.PhotoImage(Image.open("media/imgNave3.png"))
song= ImageTk.PhotoImage(Image.open("media/botonSonido.png"))
estrellaF = ImageTk.PhotoImage(Image.open("media/estrella.png"))
listaAsteroides = [ImageTk.PhotoImage(Image.open("media/asteroide1.png")),
                   ImageTk.PhotoImage(Image.open("media/asteroide2.png")),
                   ImageTk.PhotoImage(Image.open("media/asteroide3.png")),
                   ImageTk.PhotoImage(Image.open("media/asteroide4.png")),
                   ImageTk.PhotoImage(Image.open("media/asteroide5.png")),
                   ImageTk.PhotoImage(Image.open("media/asteroide6.png"))]

listaExplosiones = [ImageTk.PhotoImage(Image.open("media/exp01.png")),
                    ImageTk.PhotoImage(Image.open("media/exp02.png")),
                    ImageTk.PhotoImage(Image.open("media/exp03.png")),
                    ImageTk.PhotoImage(Image.open("media/exp04.png")),
                    ImageTk.PhotoImage(Image.open("media/exp05.png")),
                    ImageTk.PhotoImage(Image.open("media/exp06.png"))]

listaPlanetas = [ImageTk.PhotoImage(Image.open("media/planet1.png")),
                 ImageTk.PhotoImage(Image.open("media/planet2.png")),
                 ImageTk.PhotoImage(Image.open("media/planet3.png")),
                 ImageTk.PhotoImage(Image.open("media/planet4.png")),
                 ImageTk.PhotoImage(Image.open("media/astFondo1.png")),
                 ImageTk.PhotoImage(Image.open("media/astFondo2.png"))]

#creacion de clases

#---------------------Clase juego--------------------



pygame.mixer.init()

# Intercambio entre canvas:
def interInfo():
    cPrincipal.pack_forget()
    cInfo.pack(side = "right")

def interInfoAprin():#Se devuelve a principal, este en jugar o en acerca de
    cInfo.pack_forget()
    cJuego.pack_forget()
    cPrincipal.pack(side = "right")

def interJuego():#funcion intercambia a canva juego
    cPrincipal.pack_forget()
    cJuego.pack(side = "right")

def interHistoria():#intercambia a canva de modo historia
    cJuego.pack_forget()
    cHistoria.pack(side="right")

def interNiveles():#intercambia a canva de niveles a escoger
    cJuego.pack_forget()
    cniveles.pack(side="right")

def interNivel1():#intercambia a nivel 1
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel1.pack(side="left")
        juego.stop2()
        nav1 = cNivel1.create_image(150, 250, image=N11)
        iniciarNivel(cNivel1, nav1, 3)

    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        juego.stop2()
        nav2 = cNivel1.create_image(150, 250, image=N22)
        iniciarNivel(cNivel1, nav2, 3)

    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        juego.stop2()
        nav = cNivel1.create_image(150, 250, image=N33)
        iniciarNivel(cNivel1, nav, 3)

    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel2():#intercambia a nivel 2
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        nav1 = cNivel2.create_image(100, 130, image=N11, anchor="nw")
        iniciarNivel(cNivel2, nav1, 3)

    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        nav2 = cNivel2.create_image(100, 130, image=N22, anchor="nw")
    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        nav = cNivel2.create_image(100, 130, image=N33, anchor="nw")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel3():#intercambia a nivel 1
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        nav1 = cNivel3.create_image(100, 130, image=N11, anchor="nw")
    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        nav2 = cNivel3.create_image(100, 130, image=N22, anchor="nw")
    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        nav = cNivel3.create_image(100, 130, image=N33, anchor="nw")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def volverJuego():
    cHistoria.pack_forget()
    cniveles.pack_forget()
    cJuego.pack(side="right")

def volverNiveles():
    juego.jugandoTF()
    cNivel1.pack_forget()
    cNivel2.pack_forget()
    cNivel3.pack_forget()
    cNivel1.delete(nav)
    cNivel1.delete(nav1)
    cNivel1.delete(nav2)
    cNivel2.delete(nav)
    cNivel2.delete(nav1)
    cNivel2.delete(nav2)
    cNivel3.delete(nav)
    cNivel3.delete(nav1)
    cNivel3.delete(nav2)
    cniveles.pack(side="right")
    juego.VolverSon1()
    juego.VolverSon2()
    juego.VolverSon3()


#intercambio para jugar en modo Historia-----------------------
def InterJugar():
    global nav, nav1, nav2
    if varMap.get()==1:
        if name.get() != "":
            cHistoria.pack_forget()
            cModHis.pack(side = "right")
            nav1 = cModHis.create_image(400, 10, image=N11, anchor="nw")
        else:
            messagebox.showinfo("No puede Jugar", "Ingrese Nombre")
    elif varMap.get()==2:

        if name.get() != "":
            cHistoria.pack_forget()
            cModHis.pack(side = "right")
            nav2 = cModHis.create_image(400, 10, image=N22, anchor="nw")
        else:
            messagebox.showinfo("No puede Jugar", "Ingrese Nombre")
    elif varMap.get() == 3:
        if name.get() != "":
            cHistoria.pack_forget()
            cModHis.pack(side = "right")
            nav=cModHis.create_image(400, 10, image=N33, anchor="nw")
        else:
            messagebox.showinfo("No puede Jugar", "Ingrese Nombre")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")



def InterAHistoria():#funcion retorna a canva Modo historia
    global nav, nav1, nav2
    cModHis.pack_forget()
    cHistoria.pack(side = "right")
    cModHis.delete(nav)
    cModHis.delete(nav1)
    cModHis.delete(nav2)

def iniciarNivel(canvas, nave, astTiempo):
    juego.jugandoTF()
    lvl = Nave(nave, canvas)
    window.bind("<KeyPress-Right>", lvl.moverDT)
    window.bind("<KeyRelease-Right>", lvl.cancMoveD)
    window.bind("<KeyPress-Left>", lvl.moverIT)
    window.bind("<KeyRelease-Left>", lvl.cancMoveI)
    window.bind("<KeyPress-Up>", lvl.moverArT)
    window.bind("<KeyRelease-Up>", lvl.cancMoveAr)
    window.bind("<KeyPress-Down>", lvl.moverAbT)
    window.bind("<KeyRelease-Down>", lvl.cancMoveAb)
    thread = Thread(target=generarAsteroides, args=(astTiempo, canvas, lvl))
    thread.start()

    thread2 = Thread(target=generarFondo, args=(canvas,))
    thread2.start()

    thread3 = Thread(target=generarFondo2, args=(canvas,))
    thread3.start()

# Función que genera asteroides
def generarAsteroides(tiempo, canvas, claseNave):
    global listaAsteroides, listaExplosiones
    while juego.returnJugando() == True:
        imagen = canvas.create_image(730, random.randint(0, 450), image = listaAsteroides[random.randint(0, 5)])
        atributos = Asteroides(imagen, canvas, listaExplosiones, claseNave, pygame.mixer.Sound("media/explosion01.wav"),
                               pygame.mixer.Sound("media/rebote.wav"))
        atributos.moveT()
        time.sleep(tiempo)
    atributos.detener()

def generarFondo(canvas):
    global estrellaF
    while juego.returnJugando() == True:
        generarImg = canvas.create_image(730, random.randint(0, 450), image= estrellaF)
        hacerFondo = Fondo(canvas, generarImg,  random.randint(10, 15))
        hacerFondo.moveT()
        time.sleep(0.2)
    hacerFondo.detener()

def generarFondo2(canvas):
    global listaPlanetas
    while juego.returnJugando() == True:
        generarImg = canvas.create_image(730, random.randint(0, 450), image=listaPlanetas[random.randint(0, 5)])
        hacerFondo = Fondo(canvas, generarImg, random.randint(1, 3))
        hacerFondo.moveT()
        time.sleep(28)
    hacerFondo.detener()


# Creación de canvas

    # Canvas de la pantalla principal.
cPrincipal = tk.Canvas(window,  width = 730, height = 450, bg = "black")

cJuego = tk.Canvas(window,  width = 730, height = 450, bg= "black")

#canvas en jugar
cHistoria = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cModHis = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cniveles  = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel1 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel2 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel3 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cInfo = tk.Canvas(window,  width = 730, height = 450, bg= "black")

    # Widgets
        # Fondo de la pantalla principal

#lFondo = tk.Label(cPrincipal, image = fondo, bg = "white")
#lFondo.place(x = 0, y = 0)

        #Labels con detalles en canva "acerca de"
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
credits_.place(x=25,y=10)  #creacion de label con informacion "acerca de "
#Funciones donde se llama a la clase juego, para sonidos y tiempo
juego= Juego(pygame.mixer.Sound("media/Geom.mp3"),pygame.mixer.Sound("media/Nivel1S.mp3"),pygame.mixer.Sound("media/Nivel2S.mp3"),pygame.mixer.Sound("media/Nivel3S.mp3"), [0,0], cPrincipal)
juego.sonar()
juego.TiempoC()


        # Botones
    #Boton para sonido en las diferentes canvas
bstop = tk.Button(cPrincipal ,image=song, borderwidth = 0,width = 150, height = 76, command = juego.stop)
bstop.place(x = 570, y = 4)

bstop1 = tk.Button(cNivel1 ,image=song, borderwidth = 0,width = 150, height = 76, command = juego.stop)
bstop1.place(x = 570, y = 4)

bstop2 = tk.Button(cNivel2 ,image=song, borderwidth = 0,width = 150, height = 76, command = juego.stop)
bstop2.place(x = 570, y = 4)

bstop3 = tk.Button(cNivel3 ,image=song, borderwidth = 0,width = 150, height = 76, command = juego.stop)
bstop3.place(x = 570, y = 4)

#boton para cambiar a canva juego
bPlay = tk.Button(cPrincipal, image = imgJugar, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interJuego)
bPlay.place(x = 290, y = 270)
#boton para cambiar a canva info
bInfo = tk.Button(cPrincipal, image = imgInfo, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interInfo)
bInfo.place(x = 120, y = 270)

#boton para cambiar a canva de puntajes,------por definir
bPuntajes = tk.Button(cPrincipal, image = imgPuntajes, width = 150, height = 76, borderwidth = 0, cursor = "hand2")
bPuntajes.place(x = 460, y = 270)

#botones para devolverse
bvolver = tk.Button(cInfo ,text="Volver", borderwidth = 0, command = interInfoAprin)# se devuelve de informacion a la principal
bvolver.place(x = 4, y = 4)

#Botenes de atras


bvolverN1 = tk.Button(cNivel1 ,image = imgAtras, width = 120, height = 60,borderwidth = 0, command = volverNiveles)
bvolverN1.place(x = 4, y = 4)

bvolverN2 = tk.Button(cNivel2 ,image = imgAtras,width = 120, height = 60,borderwidth = 0, command = volverNiveles)
bvolverN2.place(x = 4, y = 4)

bvolverN3 = tk.Button(cNivel3 ,image = imgAtras,width = 120, height = 60,borderwidth = 0, command = volverNiveles)
bvolverN3.place(x = 4, y = 4)

#boton Volver del juego a menu
bvolver1 = tk.Button(cJuego , image = imgAtras, borderwidth = 0,width = 120, height = 60,cursor= "hand2", command = interInfoAprin)
bvolver1.place(x = 4, y = 4)

#botones canva juego modo historia y niveles

bhistoria = tk.Button(cJuego ,image = imgHistoria, borderwidth = 0,width = 150, height = 76, command = interHistoria)
bhistoria.place(x = 100, y = 270)

bJugar = tk.Button(cHistoria ,image=imgJugar, borderwidth = 0,width = 150, height = 76, cursor= "hand2", command = InterJugar)
bJugar.place(x = 100, y = 300)

bvol = tk.Button(cModHis , image = imgAtras,width = 120, height = 60, borderwidth = 0,cursor= "hand2",command = InterAHistoria)
bvol.place(x = 5, y = 5)


bNiveles = tk.Button(cJuego ,image=imgNiveles, borderwidth = 0,width = 150, height = 76, command = interNiveles)
bNiveles.place(x = 300, y = 270)

bLevel1 = tk.Button(cniveles ,image = imgNivel1, width = 150, height = 76, borderwidth = 0,cursor = "hand2",  command = interNivel1)
bLevel1.place(x = 100, y = 270)

bLevel2 = tk.Button(cniveles ,image = imgNivel2, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interNivel2)
bLevel2.place(x = 290, y = 270)

bLevel3 = tk.Button(cniveles ,image = imgNivel3, width = 150, height = 76, borderwidth = 0,cursor = "hand2",  command = interNivel3)
bLevel3.place(x = 480, y = 270)

bvolverN = tk.Button(cniveles ,image = imgAtras , width = 120, height = 60, borderwidth = 0,cursor = "hand2",  command = volverJuego)
bvolverN.place(x = 4, y = 4)
#labels que indican que selecciones un avatar

Lselec= tk.Label(cHistoria,text = "Seleccione avatar para poder jugar " , bg = "black", fg = "white", font = ("fixedsys", 10))
Lselec.place(x=410,y=50)

LselecN= tk.Label(cniveles,text = "Seleccione avatar para poder jugar " , bg = "black", fg = "white", font = ("fixedsys", 10))
LselecN.place(x=230,y=230)

#radioboton para seleccionar avatar

varMap = tk.IntVar()

#varVel = tk.IntVar()

B1 = tk.Radiobutton(cHistoria, text="1", variable = varMap, value=1, bg="black", fg="blue", font=("fixedsys"))
B1.place(x=400,y=300)

B2 = tk.Radiobutton(cHistoria, text="2", value=2 , variable = varMap, bg="black", fg="blue", font=("fixedsys"))
B2.place(x=500,y=300)

B3 = tk.Radiobutton(cHistoria, text="3",value=3,variable = varMap, bg="black", fg="blue", font=("fixedsys"))
B3.place(x=600,y=300)

Escoge1 = tk.Radiobutton(cniveles, text="1", value=1, variable = varMap,bg="black", fg="blue", font=("fixedsys"))
Escoge1.place(x=210,y=200)

Escoge2 = tk.Radiobutton(cniveles, text="2", value=2, variable = varMap, bg="black", fg="blue", font=("fixedsys"))
Escoge2.place(x=350,y=200)

Escoge3 = tk.Radiobutton(cniveles, text="3",value=3, variable = varMap,bg="black", fg="blue", font=("fixedsys"))
Escoge3.place(x=500,y=200)

#Entry para Modo historia

name = tk.Entry(cHistoria,fg = "black",font=("fixedsys"))
name.place(x=100,y=250)

#-----Configuracion canva About-----


lteclasinf = tk.Label(cInfo, image = flechas, bg = "white", borderwidth = 0)
lteclasinf.place(x = 380, y = 80)

bvolverl = tk.Button(cInfo, image = imgAtras, width = 120, height = 60, borderwidth = 0, cursor = "hand2", command = interInfoAprin)
bvolverl.place(x = 4, y = 4)



nave1=cniveles.create_image(130, 10, image=N1, anchor="nw")
nave2=cniveles.create_image(270, 10, image=N2, anchor="nw")
nave3= cniveles.create_image(400, 10, image=N3, anchor="nw")

#Botenes de atras
bvolverHis = tk.Button(cHistoria ,image = imgAtras , width = 120, height = 60, borderwidth = 0, command = volverJuego)
bvolverHis.place(x = 4, y = 4)


nave1 = cHistoria.create_image(330, 100, image=N1, anchor="nw")
nave2 = cHistoria.create_image(450, 100, image=N2, anchor="nw")
nave3 = cHistoria.create_image(550, 100, image=N3, anchor="nw")



cPrincipal.pack(side = "right")
#cierra lo de tkinter y lo de pygame
window.mainloop()
juego.jugandoTF()
pygame.mixer.quit()
pygame.quit()
print("Jeff Buen profe")