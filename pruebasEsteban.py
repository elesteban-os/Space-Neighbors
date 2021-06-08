# Librerias a utilizar en este proyecto
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 450)
window.resizable(False, False)
window.config()

# Imagen Nave
imgNave1 = ImageTk.PhotoImage(Image.open("media/imgNave1.png"))



# Canvas del juego
cGameplay = tk.Canvas(window,  width = 730, height = 450, bg= "black")
cGameplay.pack(side= "right")

imgNave23 = cGameplay.create_image(150, 100, image = imgNave1)

#Clase del movimiento de la nave
class Nave:
    def __init__(self, vida, coordsX, coordsY, imgNave, canvas):
        self.vida = vida
        self.ejeX = coordsX
        self.ejeY = coordsY
        self.enMove = False
        self.balaDano = 1 ###
        self.NaveImg = imgNave
        self.canvas = canvas

    def moverD(self):
        self.canvas.move(self.NaveImg, 300, 0)
        print(self.ejeX)
        print(self.ejeY)

navePrueba = Nave(100, cGameplay.coords(imgNave23)[0], cGameplay.coords(imgNave23)[1], imgNave23, cGameplay)
#navePrueba.moverD()

print("oI")
window.mainloop()