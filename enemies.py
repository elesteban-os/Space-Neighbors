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
            self.ejeX = self.canvas.coords(self.imagen)[0]
            if self.ejeX <= 0 and self.contarRebote != 2:
                self.contarRebote += 1
                self.velocidadX *= -1
            elif self.ejeX > 731 and self.contarRebote != 2:
                self.contarRebote += 1
                self.velocidadX *= -1





    #def Rebote(self):

print("N")