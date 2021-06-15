import pygame
from threading import Thread
import time

class Juego:
    def __init__(self, sonido,sonido1, sonido2, sonido3, tiempo, canvas):
        self.pausa = False
        self.sonido_fondo = sonido
        self.tiempo=tiempo
        self.jugando= True
        self.canvas= canvas
        self.nombre=0
        self.puntaje=0
        self.modoJuego=""
        self.sonNivel1=sonido1
        self.sonNivel2=sonido2
        self.sonNivel3=sonido3
        self.SN1 = False
        self.SN2 = False
        self.SN3 = False
        self.SNF = True

    def sonar(self):
        pygame.mixer.Sound.play(self.sonido_fondo, -1)# el -1 es para que se reproduzca infinitamente

    def stop(self):# para pausar el sonido o despausar
        if self.pausa == True:
            if self.SNF == True:
                pygame.mixer.Sound.play(self.sonido_fondo, -1)
            elif self.SN1 == True:
                pygame.mixer.Sound.play(self.sonNivel1, -1)
            elif self.SN2 == True:
                pygame.mixer.Sound.play(self.sonNivel2, -1)
            elif self.SN3 == True:
                pygame.mixer.Sound.play(self.sonNivel3, -1)
            self.pausa = False
        else:
            pygame.mixer.Sound.stop(self.sonido_fondo)
            pygame.mixer.Sound.stop(self.sonNivel1)
            pygame.mixer.Sound.stop(self.sonNivel2)
            pygame.mixer.Sound.stop(self.sonNivel3)
            self.pausa = True

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
        self.jugando = not self.jugando

    def stop2(self):
        self.SNF = False
        self.SN1 = True
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonido_fondo)
            pygame.mixer.Sound.play(self.sonNivel1, -1)

    def VolverSon1(self):
        self.SNF = True
        self.SN1 = False
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonNivel1)
            pygame.mixer.Sound.play(self.sonido_fondo, -1)

    def stop3(self):
        self.SNF = False
        self.SN2 = True
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonido_fondo)
            pygame.mixer.Sound.play(self.sonNivel2, -1)

    def VolverSon2(self):
        self.SNF = True
        self.SN2 = False
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonNivel2)
            pygame.mixer.Sound.play(self.sonido_fondo, -1)

    def stop4(self):
        self.SNF = False
        self.SN3 = True
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonido_fondo)
            pygame.mixer.Sound.play(self.sonNivel3, -1)

    def VolverSon3(self):
        self.SNF = True
        self.SN3 = False
        if self.pausa == False:
            pygame.mixer.Sound.stop(self.sonNivel3)
            pygame.mixer.Sound.play(self.sonido_fondo, -1)

    def returnJugando(self):
        return self.jugando

    print("j")

