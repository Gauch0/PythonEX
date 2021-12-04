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

# SEGUNDA TABLA

def ejercicioB(matriz):
    cont = 3
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            if f+c == fila-1:
                matriz[f][c] = 3**cont
                cont-=1
    return matriz

# Tercera TABLA

def ejercicioC(matriz):
    contador = 4
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            if f>=c:
                matriz[f][c] = contador
        contador-=1
    return matriz

# CUARTA TABLA

def ejercicioD(matriz):
    contador = 8
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            matriz[f][c] = contador
        contador/=2
    return matriz        

def ejercicioE(matriz):
    contador = 1
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            if f % 2 == 0 and c % 2 != 0: 
                matriz[f][c] = contador
                contador += 1
            if f % 2 != 0 and c % 2 == 0:
                matriz[f][c] = contador
                contador += 1
    return matriz

def ejercicioF(matriz):
    cont = 0
    for f in range(len(matriz)):
        for c in range(4-1,-1,-1):
            if (c >=4-1-f):
                matriz[f][c] = cont
                cont+=1
    return matriz

def main():
    matriz = crearMatriz(4)
    # ejercicioA(matriz)
    # ejercicioB(matriz)
    # ejercicioC(matriz)
    # ejercicioD(matriz)
    # ejercicioE(matriz)
    ejercicioF(matriz)
    imprimirMatriz(matriz)
main()