from threading import Thread
import tkinter
import time
"""
Clase del movimiento de la nave
Atributos:
+vida: vida de la nave
+energia: energía de la nave
+ejeX: ubicación en el eje X
+ejeY: ubicación  = Falsen el eje Y
+enMoveL: indica si se mueve hacia la izquierda
+enMoveR: indica si se mueve hacia la derecha
+enMoveU: indica si se mueve hacia arriba
+enMoveD: indica si se mueve hacia abajo
+NaveImg: imagen de la nave
+canvas: canvas en donde se encuentra posicionada la nave.
+bbox : coordenas de impacto de la nave, que provee la bbox
+progressBar1:la barra de energia 1
+progressBar2:la barra de energia 2
+progressBar3:la barra de energia 3
+vida3: imagenes de las vidas(corazones)
+vida2: imagenes de las vidas(corazones)
+vida1: imagenes de las vidas(corazones)

Métodos
-moverDT(): crea un thread para el movimiento hacia la derecha
-moverD(): mueve hacia la derecha la nave
-cancMoveD(): cancela el movimiento hacia la derecha
-moverIT(): crea un thread para el movimiento hacia la izquierda
-moverI(): mueve hacia la izquierda la nave
-cancMoveI(): cancela el movimiento hacia la izquierda
-moverArT(): crea un thread para el movimiento hacia arriba
-moverAr(): mueve hacia arriba la nave
-cancMoveAr(): cancela el movimiento hacia arriba
-moverAbT(): crea un thread para el movimiento hacia abajo
-moverAb(): mueve hacia abajo la nave
-cancMoveAb(): cancela el movimiento hacia abajo
-returnbbox(): retorna la bbox de la nave
-quitarEnergía(): quita en una unidad la cantidad de energía de la nave, y si fuera el caso quita una unidad de vida
-returnJugando():retorna el valor booleano de jugando
-setBackup():hace el respaldo de la vida, y la energia
-importBackup(vida, energia):importa el respaldo, con la vida y energia 
-limpieza():elimina los atributos de vida

"""

class Nave:
    def __init__(self, imgNave, canvas, pg1, pg2, pg3, vida3, vida2, vida1):
        self.vida = 3
        self.energia = 20
        self.ejeX = canvas.coords(imgNave)[0]
        self.ejeY = canvas.coords(imgNave)[1]
        self.jugando = True
        self.enMoveL = False
        self.enMoveR = False
        self.enMoveU = False
        self.enMoveD = False
        self.NaveImg = imgNave
        self.canvas = canvas
        self.bbox = [canvas.bbox(imgNave)[0], canvas.bbox(imgNave)[1], canvas.bbox(imgNave)[2], canvas.bbox(imgNave)[3]]
        self.progressBar1 = pg1
        self.progressBar2 = pg2
        self.progressBar3 = pg3
        self.vida3 = vida3
        self.vida2 = vida2
        self.vida1 = vida1

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
                self.bbox = [self.canvas.bbox(self.NaveImg)[0], self.canvas.bbox(self.NaveImg)[1],
                             self.canvas.bbox(self.NaveImg)[2], self.canvas.bbox(self.NaveImg)[3]]
            else:
                break

    def cancMoveD(self, bind):
        self.enMoveR = False

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
                self.bbox = [self.canvas.bbox(self.NaveImg)[0], self.canvas.bbox(self.NaveImg)[1],
                             self.canvas.bbox(self.NaveImg)[2], self.canvas.bbox(self.NaveImg)[3]]
            else:
                break

    def cancMoveI(self, bind):
        self.enMoveL = False

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
                self.bbox = [self.canvas.bbox(self.NaveImg)[0], self.canvas.bbox(self.NaveImg)[1],
                             self.canvas.bbox(self.NaveImg)[2], self.canvas.bbox(self.NaveImg)[3]]
            else:
                break

    def cancMoveAr(self, bind):
        self.enMoveU = False

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
                self.bbox = [self.canvas.bbox(self.NaveImg)[0], self.canvas.bbox(self.NaveImg)[1],
                             self.canvas.bbox(self.NaveImg)[2], self.canvas.bbox(self.NaveImg)[3]]
            else:
                break

    def cancMoveAb(self, bind):
        self.enMoveD = False

    def returnbbox(self, i):
        return self.bbox[i]

    def quitarEnergia(self):
        self.energia -= 1
        self.progressBar1["value"] -= 5
        self.progressBar2["value"] -= 5
        self.progressBar3["value"] -= 5

        if self.energia == 0:
            self.vida -= 1
            if self.vida == 2:
                self.canvas.delete(self.vida3)
                self.vida2 = self.canvas.create_image(370, 400, image=self.vida2)
            if self.vida == 1:
                self.canvas.delete(self.vida2)
                self.vida1 = self.canvas.create_image(370, 400, image=self.vida1)
            if self.vida == 0:
                self.canvas.delete(self.vida1)
                self.jugando = False
            else:
                self.energia = 20
                self.progressBar1["value"] = 100
                self.progressBar2["value"] = 100
                self.progressBar3["value"] = 100
        print(self.energia)

    def returnJugando(self):
        return self.jugando

    def setBackup(self):
        return [self.vida, self.energia]

    def importBackup(self, vida, energia):
        self.vida = vida
        self.energia = energia
        self.progressBar1["value"] = (energia * 100) // 20
        self.progressBar2["value"] = (energia * 100) // 20
        self.progressBar3["value"] = (energia * 100) // 20
        if self.vida == 2:
            self.canvas.delete(self.vida3)
            self.vida2 = self.canvas.create_image(370, 400, image=self.vida2)
        if self.vida == 1:
            self.canvas.delete(self.vida3)
            self.vida1 = self.canvas.create_image(370, 400, image=self.vida1)

    def limpieza(self):
        self.canvas.delete(self.vida1)
        self.canvas.delete(self.vida2)
        self.canvas.delete(self.vida3)

