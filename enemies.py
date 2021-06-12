import random
import tkinter as tk
from threading import Thread
import time
from pE2 import navePrueba

#Clase de los asteroides
class Asteroides:
    def __init__(self, coordsX, coordsY, imagen, canvas):
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMove = False
        self.contarRebote= 0
        self.daño = False   #definir
        self.velocidadX = -1 * (random.randint(1, 10)) #definir
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
            if self.ejeY <= 0 and self.contarRebote != 2:
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeY >= 450 and self.contarRebote != 2:
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeX <= 0 and self.contarRebote != 2:
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX >= 730 and self.contarRebote != 2:
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX > 750:
                break

    def __del__(self):
        self.canvas.delete(self.imagen)





    #def Rebote(self):

print("N")