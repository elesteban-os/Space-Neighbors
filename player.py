"""
Clase del movimiento de la nave
Atributos:
+vida: vida de la nave
+energia: energía de la nave
+ejeX: ubicación en el eje X
+ejeY: ubicación  = Falseen el eje Y
+enMoveL: indica si se mueve hacia la izquierda
+enMoveR: indica si se mueve hacia la derecha
+enMoveU: indica si se mueve hacia arriba
+enMoveD: indica si se mueve hacia abajo
+NaveImg: imagen de la nave
+canvas: canvas en donde se encuentra posicionada la nave.

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
"""

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

    def returnbbox(self, i):
        return self.canvas.bbox(self.NaveImg)[i]

    def quitarEnergía(self):
        self.energia -= 1
        if self.energia == 0:
            self.vida -= 1
            if self.vida == 0:
                print("Game Over")
            else:
                self.energia = 20

#Detección de teclas
window.bind("<KeyPress-Right>", navePrueba.moverDT)
window.bind("<KeyRelease-Right>", navePrueba.cancMoveD)
window.bind("<KeyPress-Left>", navePrueba.moverIT)
window.bind("<KeyRelease-Left>", navePrueba.cancMoveI)
window.bind("<KeyPress-Up>", navePrueba.moverArT)
window.bind("<KeyRelease-Up>", navePrueba.cancMoveAr)
window.bind("<KeyPress-Down>", navePrueba.moverAbT)
window.bind("<KeyRelease-Down>", navePrueba.cancMoveAb)