'''


Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos será un número par también obtenido al azar entre 10 y 50. Luego se solicita partir la lista por la mitad a través de la técnica de las rebanadas, creando dos 
nuevas listas. Imprimir las tres listas por pantalla

'''

import random

def crearLista():
    lista = []
    for i in range(20):
        numeros = random.randint(10,50)
        lista.append(numeros)
    return lista

def rebanarLista(lista):
    aux = []
    nueva = []
    minimo = len(lista)//2
    maximo = len(lista)
    nueva = lista[minimo:maximo:]
    aux = lista[0:10:]
    return aux,nueva



def main():
    lista = crearLista()
    print(lista)
    print(rebanarLista(lista))
    
main()