from tkinter import *

#def F_Credits():

 #   def BackCredits():

       # """ This function returns # to the menu """#

        #Credits.destroy()
        #windows.deiconify()

    #""" Credits screen """

Credits = Toplevel()
Credits.title("Credits")
Credits.minsize(300,450)
Credits.resizable(False, False)
Credits.config( bg= "black")

credits_ = Label(Credits,text = """

País:
Costa Rica

Universidad y carrera:
Instituto Tecnológico de Costa Rica
Computer Engineering

Asignatura, año que cursa y grupo:
Taller de programación
2021
Grupo 1

Profesor:
Jeff Schmidt

Versión programa:
1.0

Desarrolladores:
David Leiton
Kevin Chinchilla

Autores de módulos modificados:--------
2021""", bg = "black", fg = "white", font = ("fixedsys", 10))
credits_.place(x=20,y=0)

#Back = Button(Credits, text = "BACK",bg= "black",fg = "gold",font=("fixedsys"),command = BackCredits)
#Back.place(x=140, y= 400)

Credits.mainloop()