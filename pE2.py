# Librerias a utilizar en este proyecto
import time
import tkinter as tk
from PIL import ImageTk, Image
import random
from threading import Thread

window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 450)
window.resizable(False, False)
window.config()

# Imagen Nave
imgNave1 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))


# Canvas del juego
cGameplay = tk.Canvas(window,  width = 730, height = 450, bg= "black")
cGameplay.pack(side= "right")

imgNave23 = cGameplay.create_image(150, 100, image = imgNave1)


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



navePrueba = Nave(cGameplay.coords(imgNave23)[0], cGameplay.coords(imgNave23)[1], imgNave23, cGameplay)



window.bind("<KeyPress-Right>", navePrueba.moverDT)
window.bind("<KeyRelease-Right>", navePrueba.cancMoveD)
window.bind("<KeyPress-Left>", navePrueba.moverIT)
window.bind("<KeyRelease-Left>", navePrueba.cancMoveI)
window.bind("<KeyPress-Up>", navePrueba.moverArT)
window.bind("<KeyRelease-Up>", navePrueba.cancMoveAr)
window.bind("<KeyPress-Down>", navePrueba.moverAbT)
window.bind("<KeyRelease-Down>", navePrueba.cancMoveAb)

#Clase de los asteroides
class Asteroides:
    def __init__(self, coordsX, coordsY, canvas ):
        self.vida = 3
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMove = False
        self.contarRebote=0
        self.daño= False#definir
        self.velocidadX = random.randint(0, 10) #definir
        self.velocidadY = random.randint(0, 10)
       #self.NaveImg = imgNave
        self.canvas = canvas

print("ooI")
window.mainloop()