import time
from threading import Thread

class Fondo:
    def __init__(self, canvas, imagen, velocidad):
        self.ejeX = canvas.coords(imagen)[0]
        self.canvas = canvas
        self.imagen = imagen
        self.velocidadX = -(velocidad)
        self.jugando = True

    def moveT(self):
        tF = Thread(target = self.move)
        tF.start()

    def move(self):
        while self.ejeX > -50 and self.jugando == True:
            self.canvas.move(self.imagen, self.velocidadX, 0)
            self.ejeX = self.canvas.coords(self.imagen)[0]
            time.sleep(0.1)

    def detener(self):
        self.jugando = False

    def __del__(self):
        self.canvas.delete(self.imagen)
