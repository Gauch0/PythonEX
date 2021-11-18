'''
Para cada una de las siguientes matrices, desarrollar una función que la genere y 
escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
matriz obtenida. El tamaño de las matrices debe establecerse como N x N, y las 
funciones deben servir aunque este valor se modifique.

'''

from typing import Container


def crearMatriz(dimension):
    matriz = []    
    for fila in range(dimension):
        matriz.append([])
        for columna in range(dimension):
            matriz[fila].append(0)
    return matriz


def imprimirMatriz(matriz):
    columna = len(matriz[0])
    fila = len(matriz)
    for f in range(fila):
        for c in range(columna):
            print("%3d" %matriz[f][c],end=" ")
        print()

# PRIMERA TABLA

def ejercicioA(matriz):
    contador = 1
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            if f == c:
                matriz[f][c] = contador
        contador+=2
    return matriz



def main():
    matriz = crearMatriz(5)
    ejercicioA(matriz)
    imprimirMatriz(matriz)
main()