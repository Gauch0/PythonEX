
'''

Escribir funciones para:
a. Generar una lista de 50 números aleatorios del 1 al 100.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.



'''


import random

def crearLista():
    lista = []
    for i in range(50):
        numeros = random.randint(1,10)
        lista.append(numeros)
    return lista

def verificaContenedor(lista,num):
    for i in lista:
        if i == num:
            return True
    return False

def devolverUnicos(lista):
    aux = []
    for i in lista:
        if i not in aux:
            aux.append(i)
    return aux


def main():
    lista = crearLista()
    num = 10
    print(lista)
    print(verificaContenedor(lista,num))
    print(devolverUnicos(lista))
main()