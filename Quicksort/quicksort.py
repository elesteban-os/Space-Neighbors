import random
import time

def partition(array, menor, mayor):
    i = (menor - 1)
    pivot = array[mayor]

    for j in range(menor, mayor):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[mayor] = array[mayor], array[i + 1]
    return (i + 1)

def quickSort(array, menor, mayor):
    if len(array) == 1:
        return array
    if menor < mayor:
        pi = partition(array, menor, mayor)

        quickSort(array, menor, pi - 1)
        quickSort(array, pi + 1, mayor)

i = 1
tiempo = 0
listaTiempo = []
while i != 15:
    tiempo_inicial = time.time()
    listaRandom = random.sample(range(0, 100000), 10000)
    n = len(listaRandom)
    quickSort(listaRandom, 0, n - 1)
    tiempo_final = time.time() - tiempo_inicial
    listaTiempo.append(tiempo_final)
    tiempo += tiempo_final
    i += 1

print("Lista de tiempos:", listaTiempo, "Promedio de tiempo:", tiempo / 5)




quickSort(listaRandom, 0, n - 1)
print(listaRandom)