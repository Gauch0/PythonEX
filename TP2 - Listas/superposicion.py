'''

Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo y devuelva True si tienen al menos un elemento en común, o False en 
caso contrario. Desarrollar un programa para verificar su comportamiento

'''

import random

def crearLista():
    lista = []
    for i in range(10):
        numeros = random.randint(1,50)
        lista.append(numeros)
    return lista


def superposicion(primeraLista,segundaLista):
    for i in primeraLista:
        for x in segundaLista:
            if i == x:
                return True
    return False


def main():
    primeraLista = crearLista()
    segundaLista = crearLista()
    print(primeraLista,segundaLista)
    print(superposicion(primeraLista,segundaLista))
main()