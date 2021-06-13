# Librerias a utilizar en este proyecto
import random
import time
import tkinter as tk
from PIL import ImageTk, Image
from threading import Thread
#import enemies
import pygame

window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 450)
window.resizable(False, False)
window.config()

pygame.mixer.init()
explosionS = pygame.mixer.Sound("media/explosion01.wav")
reboteS = pygame.mixer.Sound("media/rebote.wav")


# Imagenes
imgNave1 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))
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

# Canvas del juego
cGameplay = tk.Canvas(window,  width = 730, height = 450, bg = "black")
cGameplay.pack(side= "right")

# Creación de Imágenes
imgNave23 = cGameplay.create_image(150, 250, image = imgNave1)




#Clase del movimiento de la nave
class Nave:
    def __init__(self, coordsX, coordsY, imgNave, canvas):
        self.vida = 3
        self.energia = 20
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMoveL = False
        self.enMoveR = False
        self.enMoveU = False
        self.enMoveD = False
        self.NaveImg = imgNave
        self.canvas = canvas

    #---------------

    def moverDT(self, bind):
        if self.enMoveR == False:
            self.enMoveR = True
            der = Thread(target = self.moverD)
            der.start()

    def moverD(self):
        while self.enMoveR == True:
            if self.ejeX != 730:
                self.canvas.move(self.NaveImg, 10, 0)
                self.ejeX = self.canvas.coords(self.NaveImg)[0]
                time.sleep(0.02)
            else:
                break

    def cancMoveD(self, bind):
        self.enMoveR = False

    #---------------

    def moverIT(self, bind):
        if self.enMoveL == False:
            self.enMoveL = True
            izq = Thread(target = self.moverI)
            izq.start()

    def moverI(self):
        while self.enMoveL == True:
            if self.ejeX != 0:
                self.canvas.move(self.NaveImg, -10, 0)
                self.ejeX = self.canvas.coords(self.NaveImg)[0]
                time.sleep(0.02)
            else:
                break

    def cancMoveI(self, bind):
        self.enMoveL = False

    # ---------------

    def moverArT(self, bind):
        if self.enMoveU == False:
            self.enMoveU = True
            arr = Thread(target = self.moverAr)
            arr.start()

    def moverAr(self):
        while self.enMoveU == True:
            if self.ejeY != 0:
                self.canvas.move(self.NaveImg, 0, -10)
                self.ejeY = self.canvas.coords(self.NaveImg)[1]
                time.sleep(0.02)
            else:
                break

    def cancMoveAr(self, bind):
        self.enMoveU = False

    # -----------------

    def moverAbT(self, bind):
        if self.enMoveD == False:
            self.enMoveD = True
            aba = Thread(target = self.moverAb)
            aba.start()

    def moverAb(self):
        while self.enMoveD == True:

            if self.ejeY != 450:
                self.canvas.move(self.NaveImg, 0, 10)
                self.ejeY = self.canvas.coords(self.NaveImg)[1]
                time.sleep(0.02)
            else:
                break

    def cancMoveAb(self, bind):
        self.enMoveD = False

    def returnbbox(self, i):
        return self.canvas.bbox(self.NaveImg)[i]

    def quitarEnergía(self):
        self.energia -= 1
        if self.energia == 0:
            self.vida -= 1
            if self.vida == 0:
                print("Game Over")
            else:
                self.energia = 20
        print(self.energia, self.vida)


def generar():
    t = Thread(target= generar_aux)
    t.start()

def generar_aux():
    while True:
        aver = cGameplay.create_image(730, random.randint(0, 450), image = listaAsteroides[random.randint(0, 5)])
        asteroidePrueba = Asteroides(cGameplay.coords(aver)[0], cGameplay.coords(aver)[1], aver, cGameplay, listaExplosiones)
        asteroidePrueba.moveT()
        time.sleep(1.5)

#Clase de los asteroides
class Asteroides:
    def __init__(self, coordsX, coordsY, imagen, canvas, imgExplosiones):
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMove = False
        self.contarRebote= 0
        self.velocidadX = -1 * (random.randint(1, 10)) #definir
        self.imagenExp = imgExplosiones
        self.imagen = imagen
        self.canvas = canvas

    def moveT(self):
        self.enMove = True
        thread = Thread(target = self.move)
        thread.start()

    def move(self):
        direccionY = self.ejeY // random.randint(5, 150)
        while self.ejeX != -30:
            self.canvas.move(self.imagen, self.velocidadX, direccionY)
            time.sleep(0.05)
            self.ejeX = self.canvas.coords(self.imagen)[0]
            self.ejeY = self.canvas.coords(self.imagen)[1]
            if navePrueba.returnbbox(0) < self.canvas.bbox(self.imagen)[0] and navePrueba.returnbbox(2) > self.canvas.bbox(self.imagen)[2] and \
                    navePrueba.returnbbox(1) < self.canvas.bbox(self.imagen)[1] and navePrueba.returnbbox(3) > self.canvas.bbox(self.imagen)[3]:
                self.canvas.delete(self.imagen)
                navePrueba.quitarEnergía()
                pygame.mixer.Sound.play(explosionS, 0)
                self.efectoExplosiones()
                break
            elif self.ejeY <= 0 and self.contarRebote != 2:
                pygame.mixer.Sound.play(reboteS, 0)
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeY >= 450 and self.contarRebote != 2:
                pygame.mixer.Sound.play(reboteS, 0)
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeX <= 0 and self.contarRebote != 2:
                pygame.mixer.Sound.play(reboteS, 0)
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX >= 730 and self.contarRebote != 2:
                pygame.mixer.Sound.play(reboteS, 0)
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX > 750 or self.ejeX < -10:
                self.canvas.delete(self.imagen)
                break


    def efectoExplosiones(self):
        for i in self.imagenExp:
            tmp = cGameplay.create_image(self.ejeX, self.ejeY, image = i)
            time.sleep(0.1)
            self.canvas.delete(tmp)

    def __del__(self):
        self.canvas.delete(self.imagen)

generar()

navePrueba = Nave(cGameplay.coords(imgNave23)[0], cGameplay.coords(imgNave23)[1], imgNave23, cGameplay)
naveenJuego = 0


window.bind("<KeyPress-Right>", navePrueba.moverDT)
window.bind("<KeyRelease-Right>", navePrueba.cancMoveD)
window.bind("<KeyPress-Left>", navePrueba.moverIT)
window.bind("<KeyRelease-Left>", navePrueba.cancMoveI)
window.bind("<KeyPress-Up>", navePrueba.moverArT)
window.bind("<KeyRelease-Up>", navePrueba.cancMoveAr)
window.bind("<KeyPress-Down>", navePrueba.moverAbT)
window.bind("<KeyRelease-Down>", navePrueba.cancMoveAb)




window.mainloop()