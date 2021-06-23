import tkinter as tk

window = tk.Tk()
window.title("Space Neighbors")
window.minsize(720, 450)
window.resizable(False, False)
window.config()

listaPuntos = ["Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0, "Name", 0]

cPuntaje= tk.Canvas(window,  width = 730, height = 450, bg = "black")
#Labels puntaje ------------------------------------------
lTitulo = tk.Label(cPuntaje, text = "Mejores puntajes", font = ("fixedsys", "20"), bg = "black", fg = "white")
lTitulo.place(x = 270, y = 10)

ljugador1 = tk.Label(cPuntaje, text = "1:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador1.place(x = 100, y = 90)

ljugador1_1 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador1_1.place(x = 135, y = 90)

ljugador2 = tk.Label(cPuntaje, text = "2:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador2.place(x = 100, y = 130)

ljugador2_2 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador2_2.place(x = 135, y = 130)

ljugador3 = tk.Label(cPuntaje, text = "3:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador3.place(x = 100, y = 170)

ljugador3_3 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador3_3.place(x = 135, y = 170)

ljugador4 = tk.Label(cPuntaje, text = "4:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador4.place(x = 100, y = 210)

ljugador4_4 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador4_4.place(x = 135, y = 210)

ljugador5 = tk.Label(cPuntaje, text = "5:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador5.place(x = 100, y = 250)

ljugador5_5 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador5_5.place(x = 135, y = 250)

ljugador6 = tk.Label(cPuntaje, text = "6:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador6.place(x = 400, y = 90)

ljugador6_6 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador6_6.place(x = 435, y = 90)

ljugador7 = tk.Label(cPuntaje, text = "7:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador7.place(x = 400, y = 130)

ljugador7_7 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador7_7.place(x = 435, y = 130)

ljugador8 = tk.Label(cPuntaje, text = "8:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador8.place(x = 400, y = 170)

ljugador8_8 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador8_8.place(x = 435, y = 170)

ljugador9 = tk.Label(cPuntaje, text = "9:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador9.place(x = 400, y = 210)

ljugador9_9 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador9_9.place(x = 435, y = 210)

ljugador10 = tk.Label(cPuntaje, text = "10:", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador10.place(x = 400, y = 250)

ljugador10_10 = tk.Label(cPuntaje, text = "", font = ("fixedsys", "20"), bg = "black", fg = "white")
ljugador10_10.place(x = 445, y = 250)

cPuntaje.pack(side = "right")





def generadorListaPuntos(lec):
    list = []
    result = ""
    numstr = False
    for i in lec:
        if i == "]":
            list.append(int(result))
            break
        if i == "[":
            continue
        elif i == ",":
            if numstr == True:
                list.append(int(result))
                result = ""
                numstr = False
            else:
                list.append(result)
                result = ""
                numstr = True
        elif i == " " or i == "'":
            continue
        elif numstr == True:
            result += i
        elif numstr == False:
            result += i
    return list


def escriturainicial(listaLabels):
    global listaPuntos
    esc = open("../media/best.txt", "r")

    leer = esc.readlines()[0]
    listaPuntos = generadorListaPuntos(leer)
    result = ""
    next = False
    listaLab = listaLabels
    for i in listaPuntos:
        result += " " + str(i)
        if next == False:
            next = True
        elif next == True:
            listaLab[0].config(text = result)
            listaLab = listaLab[1:]
            result = ""
            next = False
    esc.close()

listaLabelsPuntos = [ljugador1_1, ljugador2_2, ljugador3_3, ljugador4_4, ljugador5_5, ljugador6_6, ljugador7_7, ljugador8_8, ljugador9_9, ljugador10_10]

escriturainicial(listaLabelsPuntos)

print(listaPuntos)

def updatePuntos(puntos, nombre):
    global listaPuntos, listaLabelsPuntos
    resultLista = []
    mayor = False
    for i in listaPuntos:
        if len(resultLista) == 20:
            break
        elif mayor == True:
            resultLista.append(i)
        elif isinstance(i, int):
            if puntos > i:
                resultLista[len(resultLista) - 1] = nombre
                resultLista.append(puntos)
                mayor = True
            else:
                resultLista.append(i)
        else:
            resultLista.append(i)
    if mayor == True:
        esc = open("../media/best.txt", "w")
        esc.write(str(resultLista))
        esc.close()

        result = ""
        next = False
        listaLab = listaLabelsPuntos
        for i in resultLista:
            result += " " + str(i)
            if next == False:
                next = True
            elif next == True:
                listaLab[0].config(text=result)
                listaLab = listaLab[1:]
                result = ""
                next = False
        #juego.verPuntaje
    else:
        print("nou") #juego.verPuntaje



labelPTS = tk.Label(cPuntaje, text="""¡Estás en la 
lista de mejores 
puntajes!""" , font=("Fixedsys", 20), bg='black',fg='white')
labelPTS.place(x = 450, y = 250)

#labelPTS.place_forget()





window.mainloop()