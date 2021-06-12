import random
import tkinter as tk
from threading import Thread
import time

#Clase de los asteroides
class Asteroides:
    def __init__(self, coordsX, imagen, canvas):
        self.ejeX = coordsX
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
        while self.ejeX != -30:
            self.canvas.move(self.imagen, self.velocidadX, 0)
            time.sleep(0.05)



    #def Rebote(self):