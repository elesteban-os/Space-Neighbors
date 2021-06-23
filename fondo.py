import time
from threading import Thread
"""
Clase fondo 
Atributos:
+ejeX:es el eje x tanta de las estrellas y de los planetas del fondo
+canvas: canvas donde se mueve el fondo
+imagen:imagenes de las estrellas y de los planetas 
+velocidadX: velocidad de movimiento en el eje x
+jugando:boolean que determina si se esta jugando o  no
Metodos:
- moveT():Crea un thread para el movimiento del fondo
- move():Funcion que hace el movimiento del fondo de la pantalla
- __del__():Elimina la imagen del canvas
"""

class Fondo:
    def __init__(self, canvas, imagen, velocidad, clasejuego):
        self.ejeX = canvas.coords(imagen)[0]
        self.canvas = canvas
        self.imagen = imagen
        self.velocidadX = -(velocidad)
        self.jugando = clasejuego

    def moveT(self):
        tF = Thread(target = self.move)
        tF.start()

    def move(self):
        while self.ejeX > -50:
            self.canvas.move(self.imagen, self.velocidadX, 0)
            self.ejeX = self.canvas.coords(self.imagen)[0]
            time.sleep(0.1)
            if self.jugando.returnJugando() == False:
                self.canvas.delete(self.imagen)
                break

    def __del__(self):
        self.canvas.delete(self.imagen)
