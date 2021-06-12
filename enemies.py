import random
import tkinter as tk
from threading import Thread

#Clase de los asteroides
class Asteroides:
    def __init__(self, coordsX, coordsY, imagen, canvas):
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMove = False
        self.contarRebote= 0
        self.daño = False   #definir
        self.velocidadX = random.randint(1, 10) #definir
        self.imagen = imagen
        self.canvas = canvas

    def moveT(self):
        self.enMove = True
        thread = Thread(target = self.move)
        thread.start()

    def

    #def Rebote(self):