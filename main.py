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


#creacion de clases

#---------------------Clase juego--------------------

class Juego:
    def __init__(self, sonido, tiempo, canvas):
        self.pausa = False
        self.sonido_fondo = sonido
        self.tiempo=tiempo
        self.jugando= True
        self.canvas= canvas
        self.nombre=0
        self.puntaje=0
        self.modoJuego=""

    def sonar(self):

        pygame.mixer.Sound.play(self.sonido_fondo, -1)# el -1 es para que se reproduzca infinitamente

    def stop(self):# para pausar el sonido o despausar
        if self.pausa==False :
            pygame.mixer.pause()
            self.pausa=True
        else:
            pygame.mixer.unpause()
            self.pausa=False
    def TiempoC(self):# Thread del contador de tiempo
        tem = Thread(target=self.contadorT)
        tem.start()

    def contadorT(self): #contador de tiempo
        while self.jugando == True:
            time.sleep(0.3)
            self.contadorTAux()
    def contadorTAux(self):
        if self.tiempo[1] == 59:
            self.tiempo[1] =0
            self.tiempo[0] += 1
        else:
            self.tiempo[1]+=1
            print(self.tiempo)

    def jugandoTF(self):#Funcion para detener el tiempo, cuando finaliza ejecucion
        if self.jugando == True:
            self.jugando=False
        else:
            self.jugando = True



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
        cNivel1.pack(side="right")
        nav1 = cNivel1.create_image(400, 10, image=N11, anchor="nw")
    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        nav2 = cNivel1.create_image(400, 10, image=N22, anchor="nw")
    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel1.pack(side="right")
        nav = cNivel1.create_image(400, 10, image=N33, anchor="nw")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel2():#intercambia a nivel 2
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        nav1 = cNivel2.create_image(400, 10, image=N11, anchor="nw")
    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        nav2 = cNivel2.create_image(400, 10, image=N22, anchor="nw")
    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel2.pack(side="right")
        nav = cNivel2.create_image(400, 10, image=N33, anchor="nw")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def interNivel3():#intercambia a nivel 1
    global nav, nav1, nav2
    if varMap.get() == 1:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        nav1 = cNivel3.create_image(400, 10, image=N11, anchor="nw")
    elif varMap.get() == 2:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        nav2 = cNivel3.create_image(400, 10, image=N22, anchor="nw")
    elif varMap.get() == 3:
        cniveles.pack_forget()
        cNivel3.pack(side="right")
        nav = cNivel3.create_image(400, 10, image=N33, anchor="nw")
    else:
        messagebox.showinfo("No puede Jugar", "Seleccione avatar")

def volverJuego():
    cHistoria.pack_forget()
    cniveles.pack_forget()
    cJuego.pack(side="right")

def volverNiveles():
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

lFondo = tk.Label(cPrincipal, image = fondo, bg = "white")
lFondo.place(x = 0, y = 0)

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
juego= Juego(pygame.mixer.Sound("media/Geom.mp3"), [0,0], cPrincipal)
juego.sonar()
juego.TiempoC()
        # Botones
    #Boton para sonido en las diferentes canvas
bstop = tk.Button(cPrincipal ,text="parar audio", borderwidth = 0,font=("Rockwell", 15), command = juego.stop)
bstop.place(x = 600, y = 290)

bstop1 = tk.Button(cniveles ,text="parar audio", borderwidth = 0,font=("Rockwell", 15), command = juego.stop)
bstop1.place(x = 600, y = 300)

bstop2 = tk.Button(cHistoria ,text="parar audio", borderwidth = 0,font=("Rockwell", 15), command = juego.stop)
bstop2.place(x = 600, y = 300)

bstop3 = tk.Button(cJuego ,text="parar audio", borderwidth = 0,font=("Rockwell", 15), command = juego.stop)
bstop3.place(x = 600, y = 290)

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
bvolverHis = tk.Button(cHistoria ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverJuego)
bvolverHis.place(x = 4, y = 4)

bvolverN = tk.Button(cniveles ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverJuego)
bvolverN.place(x = 4, y = 4)

bvolverN1 = tk.Button(cNivel1 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN1.place(x = 4, y = 4)

bvolverN2 = tk.Button(cNivel2 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN2.place(x = 4, y = 4)

bvolverN3 = tk.Button(cNivel3 ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = volverNiveles)
bvolverN3.place(x = 4, y = 4)

#boton Volver del juego a menu
bvolver1 = tk.Button(cJuego ,text="Volver", borderwidth = 0,font=("Rockwell", 15), command = interInfoAprin)
bvolver1.place(x = 4, y = 4)

#botones canva juego modo historia y niveles

bhistoria = tk.Button(cJuego ,text="Modo Historia", borderwidth = 0,font=("Rockwell", 15), command = interHistoria)
bhistoria.place(x = 100, y = 270)

bJugar = tk.Button(cHistoria ,text="Jugar", borderwidth = 0,font=("Rockwell", 15), command = InterJugar)
bJugar.place(x = 100, y = 290)

bvol = tk.Button(cModHis ,text="volver", borderwidth = 0,font=("Rockwell", 15), command = InterAHistoria)
bvol.place(x = 5, y = 5)


bNiveles = tk.Button(cJuego ,text="Niveles", borderwidth = 0,font=("Rockwell", 15), command = interNiveles)
bNiveles.place(x = 300, y = 270)

bLevel1 = tk.Button(cniveles ,image = imgNivel1, width = 150, height = 76, borderwidth = 0, command = interNivel1)
bLevel1.place(x = 100, y = 270)

bLevel2 = tk.Button(cniveles ,image = imgNivel2, width = 150, height = 76, borderwidth = 0,command = interNivel2)
bLevel2.place(x = 290, y = 270)

bLevel3 = tk.Button(cniveles ,text="Nivel 3", borderwidth = 0,font=("Rockwell", 15), command = interNivel3)
bLevel3.place(x = 600, y = 270)

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
name.place(x=1,y=250)

#-----Configuracion canva About-----
# Canvas
cInfo = tk.Canvas(window,  width = 730, height = 450)

# Widgets
lFondoinf = tk.Label(cInfo, image = fondo, bg = "white")
lFondoinf.place(x = 0, y = 0)

lteclasinf = tk.Label(cInfo, image = flechas, bg = "white", borderwidth = 0)
lteclasinf.place(x = 380, y = 80)

bvolverl = tk.Button(cInfo, image = imgAtras, width = 120, height = 60, borderwidth = 0, cursor = "hand2", command = interInfoAprin)
bvolverl.place(x = 4, y = 4)


bLevel1 = tk.Button(cniveles ,image = imgNivel1, width = 150, height = 76, borderwidth = 0, command = interNivel1)
bLevel1.place(x = 100, y = 270)

bLevel2 = tk.Button(cniveles ,image = imgNivel2, width = 150, height = 76, borderwidth = 0,command = interNivel2)
bLevel2.place(x = 290, y = 270)

bLevel3 = tk.Button(cniveles ,image = imgNivel3, width = 150, height = 76, borderwidth = 0, command = interNivel3)
bLevel3.place(x = 480, y = 270)

bvolverN = tk.Button(cniveles ,image = imgAtras , width = 120, height = 60, borderwidth = 0, command = volverJuego)
bvolverN.place(x = 4, y = 4)


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