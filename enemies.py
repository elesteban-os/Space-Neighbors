import random
import pygame
from threading import Thread
import time

"""
Clase de los asteroides
Atriblocidad que va a tener el asteroide
+imagenExp: lutos:
+ejeX: coordenadas del eje X de los asteroides
+ejeY: coordenadas del eje Y de los asteroides
+contarRebote: cuenta cuantas veces ha rebotado el asteroide por la pantalla
+velocidadX: la veas imágenes que se van a utilizar para el efecto de explosión de la nave
+imagen: imagen del asteroide
+canvas: canvas del asteroide

Métodos:
-moveT(): crea un thread para el movimiento de la nave
-move(): hace el movimiento de los asteroides y captura el impacto de los asteroides con los bordes de la pantalla
y del jugador.
-efectoExplosiones(): crea un efecto de explosión para los asteroides si llegan a impactar al jugador
-__del__(): elimina la instancia y la imagen del asteroide para ahorrar recursos
"""
class Asteroides:
    def __init__(self, imagen, canvas, imgExplosiones, nave, sRebote, sExplosion, juego):
        self.ejeX = canvas.coords(imagen)[0]
        self.ejeY = canvas.coords(imagen)[1]
        self.contarRebote= 0
        self.velocidadX = -1 * (random.randint(1, 10)) #definir
        self.imagenExp = imgExplosiones
        self.imagen = imagen
        self.canvas = canvas
        self.nave = nave
        self.reboteS = sRebote
        self.explosionS = sExplosion
        self.jugando = True
        self.claseJuego = juego

    def moveT(self):
        thread = Thread(target = self.move)
        thread.start()

    def move(self):
        direccionY = self.ejeY // random.randint(5, 150)
        while self.ejeX != -30 and self.jugando == True:
            self.canvas.move(self.imagen, self.velocidadX, direccionY)
            time.sleep(0.05)
            self.ejeX = self.canvas.coords(self.imagen)[0]
            self.ejeY = self.canvas.coords(self.imagen)[1]
            if self.nave.returnbbox(0) < self.canvas.bbox(self.imagen)[0] and self.nave.returnbbox(2) > self.canvas.bbox(self.imagen)[2] and \
                    self.nave.returnbbox(1) < self.canvas.bbox(self.imagen)[1] and self.nave.returnbbox(3) > self.canvas.bbox(self.imagen)[3]:
                self.canvas.delete(self.imagen)
                self.nave.quitarEnergía()
                if self.claseJuego.returnPausa() == False:
                    pygame.mixer.Sound.play(self.explosionS, 0)
                self.efectoExplosiones()
                break
            elif self.ejeY <= 0 and self.contarRebote != 2:
                if self.claseJuego.returnPausa() == False:
                    pygame.mixer.Sound.play(self.reboteS, 0)
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeY >= 450 and self.contarRebote != 2:
                if self.claseJuego.returnPausa() == False:
                    pygame.mixer.Sound.play(self.reboteS, 0)
                self.contarRebote += 1
                direccionY *= -1
            elif self.ejeX <= 0 and self.contarRebote != 2:
                if self.claseJuego.returnPausa() == False:
                    pygame.mixer.Sound.play(self.reboteS, 0)
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX >= 730 and self.contarRebote != 2:
                if self.claseJuego.returnPausa() == False:
                    pygame.mixer.Sound.play(self.reboteS, 0)
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX > 750 or self.ejeX < -10:
                self.canvas.delete(self.imagen)
                break
            elif self.claseJuego.returnJugando() == False:
                self.canvas.delete(self.imagen)
                break


    def efectoExplosiones(self):
        for i in self.imagenExp:
            tmp = self.canvas.create_image(self.ejeX, self.ejeY, image = i)
            time.sleep(0.1)
            self.canvas.delete(tmp)

    def detener(self):
        self.jugando = False
        self.canvas.delete(self.imagen)

    def cambiarSonar(self):
        self.sonar = not self.sonar

    def returnSonar(self):
        return self.sonar

    def __del__(self):
        self.canvas.delete(self.imagen)



