# Librerias a utilizar en este proyecto
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 480)
window.resizable(False, False)
window.config()

cGameplay = tk.Canvas(window,  width = 730, height = 450, bg= "black")