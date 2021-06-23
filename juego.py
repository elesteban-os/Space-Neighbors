import pygame
from threading import Thread
import time

"""
Clase de juego
Atributos:
+pausa: boolean 
+sonido_fondo: sonido principal del juego
+tiempo: tiempo que transcurre en los niveles
+canvas:canvas en donde se encuntran ......
+nombre: nombre del jugador
+puntaje: puntaje que va aumentando en el juego
+sonNivel1: sonido para el nivel 1
+sonNivel2: sonido para el nivel 2
+sonNivel3: sonido para el nivel 1
+SN1 = boolean que indica la reproducción del sonido de fondo del nivel 1.
+SN2 = boolean que indica la reproducción del sonido de fondo del nivel 2.
+SN3 = boolean que indica la reproducción del sonido de fondo del nivel 3.
+SNF = boolean que indica la reproducción del sonido de fondo del intercambio entre canvas.
+labelT = label de tiempo del nivel 1.
+label2T = label de tiempo del nivel 2.
+label3T = label de tiempo del nivel 3.
+labelP = label de puntaje del nivel 1.
+labelP2 = label de puntaje del nivel 2.
+labelP3 = label de puntaje del nivel 3.
+valorPunt = valor que va a tener el puntaje según su nivel.
+progressBar1 = barra de progreso para la energía de la nave en el nivel 1.
+progressBar2 = barra de progreso para la energía de la nave en el nivel 2.
+progressBar3 = barra de progreso para la energía de la nave en el nivel 3.
+nave = clase de la nave.
+backup = creación de copia de ciertos datos entre la nave y la clase juego.
+mayor = declara si el puntaje obtenido es mayor que uno de la lista de puntajes altos.

Métodos
-sonar(): Hace sonar la cancion desde el inicio
-stop(): para pausar el sonido o reanudar
-TiempoC(): crea un thread para el temporizadorr
-contadorT(): es la funcion principal que llama a la auxiliar
-contadorTAux(): hace el conteo del temporizador
-jugandoTF(): Funcion para detener el tiempo, cuando finaliza ejecucion
-stop2(): detiene  la cancion principal y suena la del nivel 1
-VolverSon1(): detiene la cancion del nivel y vuelve la cancion principal
-stop3(): detiene  la cancion principal y suena la del nivel 2
-VolverSon2(): detiene la cancion del nivel y vuelve la cancion principal
-stop4(): detiene  la cancion principal y suena la del nivel 3
-VolverSon3(): detiene la cancion del nivel y vuelve la cancion principal
-returnJugando(): retorna el atributo "jugando"
-returnPausa(): retorna el atributo "pausa"
-iniciarHistoria(nombre, nave):Prepara lo que se llegue a necesitar en el modo historia
 E:el nombre del jugador e imagen de la nave
 S:-
 R:-
-returnHistoria():retorna lo atributo historia
-reset():reinicia el puntaje, tiempo
-setPuntaje(num):hace que el puntaje que vaya sumandose
 E:numero
 S:el puntaje sumado con el numero
 R:-
-returnTiempo():retorna el atributo tiempo
-returnNivel():retorna el atributo del nivel
-setBackup( vidaNav, energiaNav):Hace un respaldo de todo lo que se necesita para los siguientes niveles 
-returnBackup(): retorna el respaldo que se hizo
-importBackup( puntaje):importa el respaldo, con el puntaje y labels necesarios
-resetTiempo():restea el tiempo en cero
-returnNave():retorna la imagen de la nave
-sumaNivel():Contador de niveles, segun sea el nivel
-returnDatos():retorna el nombre y puntaje
-terminarHistoria():es un reset del modo historia 
-returnPuntaje():retorna el puntaje obtenido
-puntajeMayor(valor):Si jugador obtiene un puntaje mayor de lo que existe, se obtiene un boolean, true si esta dentro de los mejores 
 puntajes y False si no.
 E: valor del puntaje
-returnMayor():retorna el puntaje mayor
-returnNombre():retorna el nombre del jugador , ademas elimina el nombre del jugador.

    
"""
class Juego:
    def __init__(self, sonido, sonido1, sonido2, sonido3, tiempo, canvas, label1, label2, label3, label4, label5, label6,
                 pg1, pg2, pg3):
        self.pausa = False
        self.sonido_fondo = sonido
        self.tiempo=tiempo
        self.jugando= False
        self.historia= False
        self.canvas= canvas
        self.nombre=0
        self.puntaje=0
        self.nivel=0
        self.sonNivel1=sonido1
        self.sonNivel2=sonido2
        self.sonNivel3=sonido3
        self.SN1 = False
        self.SN2 = False
        self.SN3 = False
        self.SNF = True
        self.labelT = label1
        self.label2T = label2
        self.label3T = label3
        self.labelP = label4
        self.labelP2 = label5
        self.labelP3 = label6
        self.valorPunt = 0
        self.progressBar1 = pg1
        self.progressBar2 = pg2
        self.progressBar3 = pg3
        self.nave = 0
        self.backup = 0
        self.mayor = False

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
            time.sleep(1)
            self.contadorTAux()

    def contadorTAux(self):
        if self.tiempo[1] == 59:
            self.tiempo[1] =0
            self.tiempo[0] += 1
            self.labelT.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.label2T.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.label3T.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.puntaje += self.valorPunt
            self.labelP.config(text=str(self.puntaje))
            self.labelP2.config(text=str(self.puntaje))
            self.labelP3.config(text=str(self.puntaje))

        else:
            self.tiempo[1]+= 1
            self.labelT.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.label2T.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.label3T.config(text=str(self.tiempo[0]) + ":" + str(self.tiempo[1]))
            self.puntaje += self.valorPunt

            self.labelP.config(text=str(self.puntaje))
            self.labelP2.config(text=str(self.puntaje))
            self.labelP3.config(text=str(self.puntaje))

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

    def returnPausa(self):
        return self.pausa

    def iniciarHistoria(self, nombre, nave):
        self.historia = True
        self.nombre = nombre
        self.nivel = 1
        self.nave = nave

    def returnHistoria(self):
        return self.historia

    def reset(self):
        self.tiempo = [0, 0]
        self.labelT.config(text="Time")
        self.label2T.config(text="Time")
        self.label3T.config(text="Time")

        self.puntaje = 0
        self.valorPunt = 0

        self.labelP.config(text="Points")
        self.labelP2.config(text="Points")
        self.labelP3.config(text="Points")

        self.progressBar1["value"] = 100
        self.progressBar2["value"] = 100
        self.progressBar3["value"] = 100


    def setPuntaje(self, num):
        self.valorPunt = num

    def returnTiempo(self):
        return self.tiempo

    def returnNivel(self):
        return self.nivel

    def setBackup(self, vidaNav, energiaNav):
        if vidaNav == -1:
            self.backup = 0
        else:
            self.backup = [self.puntaje, vidaNav, energiaNav]

    def returnBackup(self):
        return self.backup

    def importBackup(self, puntaje):
        self.puntaje = puntaje
        self.labelP.config(text=str(self.puntaje))
        self.labelP2.config(text=str(self.puntaje))
        self.labelP3.config(text=str(self.puntaje))

    def resetTiempo(self):
        self.tiempo = [0,0]

    def returnNave(self):
        return self.nave

    def sumaNivel(self):
        self.nivel += 1

    def returnDatos(self):
        return [self.nombre, self.puntaje]

    def terminarHistoria(self):
        self.historia = False
        self.puntaje = 0
        self.nivel = 0
        self.labelP.config(text=str(self.puntaje))
        self.labelP2.config(text=str(self.puntaje))
        self.labelP3.config(text=str(self.puntaje))

    def returnPuntaje(self):
        return self.puntaje
        self.puntaje = 0

    def puntajeMayor(self, valor):
        self.mayor = valor

    def returnMayor(self):
        return self.mayor

    def returnNombre(self):
        return self.nombre
        self.nombre = ""


