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
import tkinter.ttk as ttk
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
naveHistoria = 0
naveJugando = 0
listaPuntos = []

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
vida100= ImageTk.PhotoImage(Image.open("media/life.png"))
vida50= ImageTk.PhotoImage(Image.open("media/life1.png"))
vida10=ImageTk.PhotoImage(Image.open("media/life2.png"))

listaNave = [N11, N22, N33]

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

def interPuntaje():
    cPrincipal.pack_forget()
    cPuntaje.pack(side="right")

def interNivel1():#intercambia a nivel 1
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        juego.stop2()
        nav1 = cNivel1.create_image(150, 250, image=N11)
        juego.setPuntaje(1)
        iniciarNivel(cNivel1, nav1, 1, juego)

    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        juego.stop2()
        juego.setPuntaje(1)
        nav2 = cNivel1.create_image(150, 250, image=N22)
        iniciarNivel(cNivel1, nav2, 1, juego)

    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        juego.stop2()
        juego.setPuntaje(1)
        nav = cNivel1.create_image(150, 250, image=N33)
        iniciarNivel(cNivel1, nav, 1, juego)

    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel2():#intercambia a nivel 2
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        juego.setPuntaje(3)
        nav1 = cNivel2.create_image(150, 250, image=N11)
        iniciarNivel(cNivel2, nav1, 0.90, juego)

    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        juego.setPuntaje(3)
        nav2 = cNivel2.create_image(150, 250, image=N22)
        iniciarNivel(cNivel2, nav2, 0.90, juego)

    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        juego.stop3()
        juego.setPuntaje(3)
        nav = cNivel2.create_image(150, 250, image=N33)
        iniciarNivel(cNivel2, nav, 0.90, juego)

    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel3():#intercambia a nivel 1
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        juego.setPuntaje(5)
        nav1 = cNivel3.create_image(150, 250, image=N11)
        iniciarNivel(cNivel3, nav1, 0.5, juego)

    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        juego.setPuntaje(5)
        nav2 = cNivel3.create_image(150, 250, image=N22)
        iniciarNivel(cNivel3, nav2, 0.5, juego)

    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        juego.stop4()
        juego.setPuntaje(5)
        nav = cNivel3.create_image(150, 250, image=N33)
        iniciarNivel(cNivel3, nav, 0.5, juego)


    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def volverJuego():
    cHistoria.pack_forget()
    cniveles.pack_forget()
    cJuego.pack(side="right")

def volverNiveles():
    global naveJugando
    if juego.returnJugando() == True:
        juego.jugandoTF()
    cNivel1.pack_forget()
    cNivel2.pack_forget()
    cNivel3.pack_forget()
    cGameOver.pack_forget()
    cWin.pack_forget()
    cWinHis.pack_forget()
    cCargando.pack(side = "right")
    juego.VolverSon1()
    juego.VolverSon2()
    juego.VolverSon3()
    juego.puntajeMayor(False)
    naveJugando.limpieza()
    lPuntosGO.config(text = "")
    juego.terminarHistoria()
    thread = Thread(target = reset)
    thread.start()
    labelPTS.place_forget()
    labelPTSGO.place_forget()

def volverPuntajes():
    cPuntaje.pack_forget()
    cPrincipal.pack(side = "right")

def reset():
    time.sleep(3)
    cNivel1.delete(nav)
    cNivel1.delete(nav1)
    cNivel1.delete(nav2)
    cNivel1.delete(naveHistoria)
    cNivel2.delete(nav)
    cNivel2.delete(nav1)
    cNivel2.delete(nav2)
    cNivel2.delete(naveHistoria)
    cNivel3.delete(nav)
    cNivel3.delete(nav1)
    cNivel3.delete(nav2)
    cNivel3.delete(naveHistoria)
    cPrincipal.pack(side="right")
    cCargando.pack_forget()
    juego.reset()



#intercambio para jugar en modo Historia-----------------------
def InterJugar():
    global naveHistoria
    if varMap.get()==1:
        if name.get() != "":
            cHistoria.pack_forget()
            cNivel1.pack(side="right")
            juego.stop2()
            juego.jugandoTF()
            juego.setPuntaje(1)
            naveHistoria = cNivel1.create_image(150, 250, image=N11)
            juego.iniciarHistoria(name.get(), 1)
            iniciarNivel(cNivel1, naveHistoria, 1, juego)
        else:
            messagebox.showinfo("No puede Jugar", "Ingrese Nombre")
    elif varMap.get()==2:
        if name.get() != "":
            cHistoria.pack_forget()
            cNivel1.pack(side="right")
            juego.stop2()
            juego.jugandoTF()
            juego.setPuntaje(1)
            naveHistoria = cNivel1.create_image(150, 250, image=N22)
            juego.iniciarHistoria(name.get(), 2)
            iniciarNivel(cNivel1, naveHistoria, 1, juego)
        else:
            messagebox.showinfo("No puede Jugar", "Ingrese Nombre")
    elif varMap.get() == 3:
        if name.get() != "":
            cHistoria.pack_forget()
            cNivel1.pack(side="right")
            juego.stop2()
            juego.jugandoTF()
            juego.setPuntaje(1)
            naveHistoria = cNivel1.create_image(150, 250, image=N33)
            juego.iniciarHistoria(name.get(), 3)
            iniciarNivel(cNivel1, naveHistoria, 1, juego)

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


def iniciarNivel(canvas, nave, astTiempo, claseJuego):
    global vida100, vida50, vida10, naveJugando
    if claseJuego.returnHistoria() == False:
        juego.jugandoTF()
    juego.TiempoC()
    vida3 = canvas.create_image(370, 400, image=vida100)
    lvl = Nave(nave, canvas, LiveNivel1, LiveNivel2, LiveNivel3, vida3, vida50, vida10)
    naveJugando = lvl
    if claseJuego.returnBackup() != 0:
        lvl.importBackup(claseJuego.returnBackup()[1], claseJuego.returnBackup()[2])
        claseJuego.importBackup(claseJuego.returnBackup()[0])
        claseJuego.setBackup(-1, -1)
    window.bind("<KeyPress-Right>", lvl.moverDT)
    window.bind("<KeyRelease-Right>", lvl.cancMoveD)
    window.bind("<KeyPress-Left>", lvl.moverIT)
    window.bind("<KeyRelease-Left>", lvl.cancMoveI)
    window.bind("<KeyPress-Up>", lvl.moverArT)
    window.bind("<KeyRelease-Up>", lvl.cancMoveAr)
    window.bind("<KeyPress-Down>", lvl.moverAbT)
    window.bind("<KeyRelease-Down>", lvl.cancMoveAb)
    thread = Thread(target=generarAsteroides, args=(astTiempo, canvas, lvl, claseJuego))
    thread.start()

    thread2 = Thread(target=generarFondo, args=(canvas, claseJuego,))
    thread2.start()

    thread3 = Thread(target=generarFondo2, args=(canvas, claseJuego,))
    thread3.start()

# Función que genera asteroides
def generarAsteroides(tiempo, canvas, claseNave, claseJuego):
    global listaAsteroides, listaExplosiones, cNivel2, cNivel3, naveHistoria, listaNave
    while juego.returnJugando() == True:
        imagen = canvas.create_image(730, random.randint(0, 450), image = listaAsteroides[random.randint(0, 5)])
        atributos = Asteroides(imagen, canvas, listaExplosiones, claseNave, pygame.mixer.Sound("media/explosion01.wav"),
                               pygame.mixer.Sound("media/rebote.wav"), claseJuego)
        atributos.moveT()
        if claseNave.returnJugando() == False:
            canvas.pack_forget()
            if claseJuego.returnHistoria() == True:
                lPuntosGO.config(text = "Puntaje: " + str(claseJuego.returnDatos()[1]))
                updatePuntos(claseJuego.returnPuntaje(), claseJuego.returnNombre())
                if claseJuego.returnMayor() == True:
                    labelPTSGO.place(x=450, y=250)
                claseJuego.terminarHistoria()
                claseJuego.reset()
                claseJuego.setBackup(-1, -1)
                threadTer = Thread(target=terminarHistoria, args=(canvas, naveHistoria,))
                threadTer.start()
            cGameOver.pack(side = "right")
            claseJuego.jugandoTF()
            claseNave.limpieza()
            break
        if claseJuego.returnTiempo()[0] == 1 and claseJuego.returnHistoria() == False:
            canvas.pack_forget()
            cWin.pack(side = "right")
            claseJuego.jugandoTF()
            claseNave.limpieza()
            break
        if claseJuego.returnTiempo()[0] == 1 and claseJuego.returnHistoria() == True:
            canvas.pack_forget()
            claseJuego.setBackup(claseNave.setBackup()[0], claseNave.setBackup()[1])
            claseJuego.jugandoTF()
            if claseJuego.returnNivel() < 3:
                claseJuego.VolverSon1()
                claseJuego.VolverSon2()
                claseJuego.VolverSon3()
            canvas.pack_forget()
            if claseJuego.returnNivel() != 3:
                cCargando.pack(side="right")
            claseJuego.resetTiempo()
            if claseJuego.returnNivel() == 1:
                threadimg = Thread(target= terminarHistoria, args= (canvas, naveHistoria,))
                threadimg.start()

                naveHistoria = cNivel2.create_image(150, 250, image = listaNave[claseJuego.returnNave() - 1])
                claseJuego.stop3()
                claseNave.limpieza()
                thread = Thread(target= sigHistoria, args= (canvas, cNivel2, naveHistoria, 0.90, claseJuego, 3,))
                thread.start()
            if claseJuego.returnNivel() == 2:
                threadimg = Thread(target=terminarHistoria, args=(canvas, naveHistoria,))
                threadimg.start()

                naveHistoria = cNivel3.create_image(150, 250, image=listaNave[claseJuego.returnNave() - 1])
                claseJuego.stop4()
                claseJuego.setPuntaje(5)
                claseNave.limpieza()
                thread = Thread(target=sigHistoria, args=(canvas, cNivel3, naveHistoria, 0.5, claseJuego, 5,))
                thread.start()
            if claseJuego.returnNivel() == 3:

                claseJuego.jugandoTF()
                lPuntosHis.config(text="Puntaje: " + str(claseJuego.returnDatos()[1]))
                updatePuntos(claseJuego.returnPuntaje(), claseJuego.returnNombre())
                if claseJuego.returnMayor() == True:
                    labelPTS.place(x = 450, y = 250)
                claseJuego.terminarHistoria()
                claseJuego.reset()
                claseJuego.setBackup(-1, -1)
                cWinHis.pack(side= "right")
                claseNave.limpieza()
                threadTer = Thread(target = terminarHistoria, args=(canvas, naveHistoria,))
                threadTer.start()


            claseJuego.sumaNivel()
            break
        time.sleep(tiempo)



def terminarHistoria(canvas, naveHistoria):
    time.sleep(3)
    canvas.delete(naveHistoria)

def sigHistoria(canvas, canvas2, naveHistoria, astTiempo, claseJuego, puntaje):
    time.sleep(3)
    claseJuego.jugandoTF()
    canvas.delete(naveHistoria)
    cCargando.pack_forget()
    canvas2.pack(side = "right")
    juego.reset()
    iniciarNivel(canvas2, naveHistoria, astTiempo, claseJuego)
    claseJuego.setPuntaje(puntaje)



def generarFondo(canvas, claseJuego):
    global estrellaF
    while juego.returnJugando() == True:
        generarImg = canvas.create_image(730, random.randint(0, 450), image= estrellaF)
        hacerFondo = Fondo(canvas, generarImg,  random.randint(10, 15), claseJuego)
        hacerFondo.moveT()
        if juego.returnJugando() == False and juego.returnHistoria() == True:
            break
        time.sleep(0.2)



def generarFondo2(canvas, claseJuego):
    global listaPlanetas
    while juego.returnJugando() == True:
        generarImg = canvas.create_image(730, random.randint(0, 450), image=listaPlanetas[random.randint(0, 5)])
        hacerFondo = Fondo(canvas, generarImg, random.randint(1, 3), claseJuego)
        hacerFondo.moveT()
        if juego.returnJugando() == False and juego.returnHistoria() == True:
            break
        time.sleep(28)



# Creación de canvas

    # Canvas de la pantalla principal.
cPrincipal = tk.Canvas(window,  width = 730, height = 450, bg = "black")

cJuego = tk.Canvas(window,  width = 730, height = 450, bg= "black")

#canvas en jugar
cHistoria = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cModHis = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cniveles  = tk.Canvas(window,  width = 730, height = 450, bg= "black")

cNivel1 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

label_pts1 = tk.Label(cNivel1, text="Points" , font=("Fixedsys", 20), bg='black',fg='white')
label_pts1.place(x=635, y=410)

label_time1=tk.Label(cNivel1, text="Time" , font=("Fixedsys", 20), bg='black',fg='white')
label_time1.place(x=4, y=410)

LiveNivel1=ttk.Progressbar(cNivel1, orient = "horizontal", length=100, mode="determinate")
LiveNivel1.place(x=320, y=420)
LiveNivel1["value"]=100




cNivel2 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

label_pts2 = tk.Label(cNivel2, text="Points" , font=("Fixedsys", 20), bg='black',fg='white')
label_pts2.place(x=635, y=410)

label_time2=tk.Label(cNivel2, text="Time" , font=("Fixedsys", 20), bg='black',fg='white')
label_time2.place(x=4, y=410)

LiveNivel2=ttk.Progressbar(cNivel2, orient = "horizontal", length=100, mode="determinate")
LiveNivel2.place(x=320, y=420)
LiveNivel2["value"]=100



cNivel3 = tk.Canvas(window,  width = 730, height = 450, bg= "black")

label_pts3 = tk.Label(cNivel3, text="Points" , font=("Fixedsys", 20), bg='black',fg='white')
label_pts3.place(x=635, y=410)

label_time3=tk.Label(cNivel3, text="Time" , font=("Fixedsys", 20), bg='black',fg='white')
label_time3.place(x=4, y=410)

LiveNivel3=ttk.Progressbar(cNivel3, orient = "horizontal", length=100, mode="determinate")
LiveNivel3.place(x=320, y=420)
LiveNivel3["value"]=100



cCargando = tk.Canvas(window,  width = 730, height = 450, bg= "black")
lCargando = tk.Label(cCargando, text = "Por favor, espere...", font = ("fixedsys", "30"), bg = "black", fg = "white")
lCargando.place(x = 150, y = 200)

cGameOver = tk.Canvas(window,  width = 730, height = 450, bg= "black")
lGameOver = tk.Label(cGameOver, text = "¡Has sido derrotado!", font = ("fixedsys", "30"), bg = "black", fg = "white")
lGameOver.place(x = 140, y = 150)
bvolverGO = tk.Button(cGameOver, image = imgAtras, width = 120, height = 60, borderwidth = 0, command = volverNiveles)# se devuelve de informacion a la principal
bvolverGO.place(x = 290, y = 250)

lPuntosGO = tk.Label(cGameOver, text = "", font = ("fixedsys", "30"), bg = "black", fg = "white")
lPuntosGO.place(x = 235, y = 200)

labelPTSGO = tk.Label(cGameOver, text="""¡Estás en la 
lista de mejores 
puntajes!""" , font=("Fixedsys", 20), bg='black',fg='white')


cWin = tk.Canvas(window,  width = 730, height = 450, bg= "black")
lWin = tk.Label(cWin, text = "¡Ganaste!", font = ("fixedsys", "30"), bg = "black", fg = "white")
lWin.place(x = 250, y = 150)

cWinHis = tk.Canvas(window,  width = 730, height = 450, bg= "black")
lWinHis = tk.Label(cWinHis, text = "¡Ganaste!", font = ("fixedsys", "30"), bg = "black", fg = "white")
lWinHis.place(x = 250, y = 150)
lPuntosHis = tk.Label(cWinHis, text = "", font = ("fixedsys", "30"), bg = "black", fg = "white")
lPuntosHis.place(x = 235, y = 200)
bvolverWinHis = tk.Button(cWinHis, image = imgAtras, width = 120, height = 60, borderwidth = 0, command = volverNiveles)# se devuelve de informacion a la principal
bvolverWinHis.place(x = 290, y = 250)

labelPTS = tk.Label(cWinHis, text="""¡Estás en la 
lista de mejores 
puntajes!""" , font=("Fixedsys", 20), bg='black',fg='white')


bvolverWin = tk.Button(cWin, image = imgAtras, width = 120, height = 60, borderwidth = 0, command = volverNiveles)# se devuelve de informacion a la principal
bvolverWin.place(x = 290, y = 250)




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
juego= Juego(pygame.mixer.Sound("media/Geom.mp3"),pygame.mixer.Sound("media/Nivel1S.mp3"),pygame.mixer.Sound("media/Nivel2S.mp3"),pygame.mixer.Sound("media/Nivel3S.mp3"), [0,0], cPrincipal, label_time1,
             label_time2, label_time3, label_pts1, label_pts2, label_pts3, LiveNivel1, LiveNivel2, LiveNivel3)
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
bPuntajes = tk.Button(cPrincipal, image = imgPuntajes, width = 150, height = 76, borderwidth = 0, cursor = "hand2", command = interPuntaje)
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

# Canvas de puntajes
cPuntaje= tk.Canvas(window,  width = 730, height = 450, bg = "black")
#Labels puntaje ------------------------------------------
lTitulo = tk.Label(cPuntaje, text = "Mejores puntajes", font = ("fixedsys", "20"), bg = "black", fg = "white")
lTitulo.place(x = 270, y = 10)

ljugador1 = tk.Label(cPuntaje, text = "1:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador1.place(x = 100, y = 90)

ljugador1_1 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador1_1.place(x = 135, y = 90)

ljugador2 = tk.Label(cPuntaje, text = "2:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador2.place(x = 100, y = 130)

ljugador2_2 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador2_2.place(x = 135, y = 130)

ljugador3 = tk.Label(cPuntaje, text = "3:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador3.place(x = 100, y = 170)

ljugador3_3 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador3_3.place(x = 135, y = 170)

ljugador4 = tk.Label(cPuntaje, text = "4:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador4.place(x = 100, y = 210)

ljugador4_4 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador4_4.place(x = 135, y = 210)

ljugador5 = tk.Label(cPuntaje, text = "5:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador5.place(x = 100, y = 250)

ljugador5_5 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador5_5.place(x = 135, y = 250)

ljugador6 = tk.Label(cPuntaje, text = "6:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador6.place(x = 400, y = 90)

ljugador6_6 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador6_6.place(x = 435, y = 90)

ljugador7 = tk.Label(cPuntaje, text = "7:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador7.place(x = 400, y = 130)

ljugador7_7 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador7_7.place(x = 435, y = 130)

ljugador8 = tk.Label(cPuntaje, text = "8:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador8.place(x = 400, y = 170)

ljugador8_8 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador8_8.place(x = 435, y = 170)

ljugador9 = tk.Label(cPuntaje, text = "9:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador9.place(x = 400, y = 210)

ljugador9_9 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador9_9.place(x = 435, y = 210)

ljugador10 = tk.Label(cPuntaje, text = "10:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador10.place(x = 400, y = 250)

ljugador10_10 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador10_10.place(x = 445, y = 250)

bvolverPunt = tk.Button(cPuntaje, image = imgAtras, width = 120, height = 60,borderwidth = 0, command = volverPuntajes)
bvolverPunt.place(x = 4, y = 4)

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

# Funciones para lectura/escritura:
listaLabelsPuntos = [ljugador1_1, ljugador2_2, ljugador3_3, ljugador4_4, ljugador5_5, ljugador6_6, ljugador7_7, ljugador8_8, ljugador9_9, ljugador10_10]

def generadorListaPuntos(lec):
    list = []
    result = ""
    numstr = False
    for i in lec:
        if i == "]":
            list.append(int(result))
            break
        if i == "[":
            continue
        elif i == ",":
            if numstr == True:
                list.append(int(result))
                result = ""
                numstr = False
            else:
                list.append(result)
                result = ""
                numstr = True
        elif i == " " or i == "'":
            continue
        elif numstr == True:
            result += i
        elif numstr == False:
            result += i
    return list

def escriturainicial(listaLabels):
    global listaPuntos
    esc = open("media/best.txt", "r")

    leer = esc.readlines()[0]
    listaPuntos = generadorListaPuntos(leer)
    result = ""
    next = False
    listaLab = listaLabels
    for i in listaPuntos:
        result += " " + str(i)
        if next == False:
            next = True
        elif next == True:
            listaLab[0].config(text = result)
            listaLab = listaLab[1:]
            result = ""
            next = False
    esc.close()

escriturainicial(listaLabelsPuntos)

def updatePuntos(puntos, nombre):
    global listaPuntos, listaLabelsPuntos, juego
    resultLista = []
    mayor = False
    for i in listaPuntos:
        if len(resultLista) == 20:
            break
        elif mayor == True:
            resultLista.append(i)
        elif isinstance(i, int):
            if puntos > i:
                resultLista[len(resultLista) - 1] = nombre
                resultLista.append(puntos)
                mayor = True
            else:
                resultLista.append(i)
        else:
            resultLista.append(i)
    if mayor == True:
        esc = open("media/best.txt", "w")
        esc.write(str(resultLista))
        esc.close()

        result = ""
        next = False
        listaLab = listaLabelsPuntos
        for i in resultLista:
            result += " " + str(i)
            if next == False:
                next = True
            elif next == True:
                listaLab[0].config(text=result)
                listaLab = listaLab[1:]
                result = ""
                next = False
        juego.puntajeMayor(True)
    else:
        juego.puntajeMayor(False)



cPrincipal.pack(side = "right")
#cierra lo de tkinter y lo de pygame
window.mainloop()
juego.jugandoTF()
pygame.mixer.quit()
pygame.quit()
print("Jeff Buen profe")