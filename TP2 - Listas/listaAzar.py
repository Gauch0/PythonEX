'''

Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera 
lista cuyos elementos sean el resultado de la intersección de las dos listas dadas. 
Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla.

'''
import random

def crearLista():
    lista = []
    for i in range(10):
        numeros = random.randint(1,50)
        lista.append(numeros)
    return lista

def interseccionLista(primeraLista,segundaLista):
    aux = []
    for i in primeraLista:
        for x in segundaLista:
            if i == x:
                aux.append(i)
    return aux



def main():
    primeraLista = crearLista()
    segundaLista = crearLista()
    print(primeraLista,segundaLista)
    print(interseccionLista(primeraLista,segundaLista))
main()















