'''


Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.



'''

import random

'''
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado.
'''

def crearMatriz(dimension): # CREAMOS LA MATRIZ #1A
    matriz = []
    for fila in range(dimension):
        matriz.append([])
        for columna in range(dimension):
            numero = random.randint(1,90)
            matriz[fila].append(numero)
    return matriz

def imprimirMatriz(matriz): # IMPRIMIMOS LA MATRIZ
    filas = len(matriz)
    columna = len(matriz[0])
    for f in range(filas):
        for c in range(columna):
            print("%3d" %matriz[f][c], end=" ")
        print()
'''
b. Ordenar en forma ascendente cada una de las filas de la matriz.
'''

def formaAscendente(matriz): # Ordenamos la matriz de forma ascendente
    for fila in range(len(matriz)):
        matriz[fila].sort()
    return matriz

'''
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
'''
def intercambiarFilas(matriz,fila1,fila2):
    filas = len(matriz)
    for f in range(filas):
        aux = matriz[fila1-1][f]
        matriz[fila1-1][f] = matriz[fila2-1][f]
        matriz[fila2-1][f] = aux

'''
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
'''
def intercambiarColumnas(matriz,colum1,colum2): #
    columnas = len(matriz[0])
    filas = len(matriz)
    for f in range(filas):
        for c in range(columnas):
            aux = matriz[f][colum1-1]
            matriz[f][colum1-1] = matriz[f][colum2-1]
            matriz[f][colum2-1] = aux
'''
e. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
'''
def trasponerFilaxColumna(matriz):
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna//2):
            aux = matriz[f][c]
            matriz[f][c] = matriz[c][f]
            matriz[c][f] = aux

'''
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
'''

def calcularProm(matriz,f):
    promedio = 0
    suma = 0
    columna = len(matriz[0])
    for c in range(columna):
        suma += matriz[f][c]
    promedio = suma / columna
    return promedio

'''
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro
'''

def calcularPorcentaje(matriz,f): #1G
    por = 0
    suma = 0
    columna = len(matriz[0])
    for c in range(columna):
        if matriz[f][c] % 2 != 0:
            suma+=1
    por = (suma*100)/len(matriz)
    return print(por,"%")


'''
i. Determinar si la matriz es simétrica con respecto a su diagonal principal
'''

def SimetricaDiagonalPrincipal(matriz): #1H
    fila = len(matriz)
    columna = len(matriz[0])
    for f in range(fila):
        for c in range(columna):
            if matriz[f][c] != matriz[c][f]:
                flag = 1
    if flag == 1:
        print("No es simetrica respecto a la diag ppl")
    else:
        print("Es simetrica respecto a la diag ppl")


def SimetricaDiagonalSecundaria(matriz): #1I
    i=0
    esSim=True
    print(matriz)
    while i<len(matriz)-1 and esSim:
        j=0
        while j <len(matriz)-1-i and esSim:
            if matriz[i][j]!=matriz[len(matriz)-1-j][len(matriz)-1-i]:
                esSim=False
            else:
                j+=1
        i+=1            
    if esSim==False:
        print("No es simetrica respecto a la diag secundaria")
    else:
        print("Es simetrica respecto a la diag secundaria")


def main():
    matriz = crearMatriz(5)
    print("MATRIZ NORMAL: ")
    imprimirMatriz(matriz)
    formaAscendente(matriz)
    print("MATRIZ ORDEN ASC: ")
    imprimirMatriz(matriz)
    intercambiarFilas(matriz,1,3)
    print("MATRIZ FILAS INTERCAMBIADAS: ")
    imprimirMatriz(matriz)
    print("MATRIZ COLUMNAS INTERCAMBIADAS: ")
    intercambiarColumnas(matriz,2,3)
    imprimirMatriz(matriz)
    print("MATRIZ TRASPUESTA: ")
    trasponerFilaxColumna(matriz)
    imprimirMatriz(matriz)
    print("El promedio de la fila es : ",calcularProm(matriz,0))
    print("El porcentaje de la columna es: ",calcularPorcentaje(matriz,1))
    imprimirMatriz(matriz)
    SimetricaDiagonalPrincipal(matriz)
    imprimirMatriz(matriz)
    SimetricaDiagonalSecundaria(matriz)
    imprimirMatriz(matriz)
main()