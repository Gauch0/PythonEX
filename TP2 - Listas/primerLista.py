'''

1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].


'''

import random

def crearLista():
    lista = []
    for i in range(4):
        numeros = random.randint(10,10)
        lista.append(numeros)
    return lista

def sumatoriaLista(lista):
    total = 0
    for i in (lista):
        total += i 
    return total


def eliminarRepetidos(lista , numero):
    for i in (lista):
        if i == numero:
            lista.remove(numero)
    return lista

# def listaCapicua(lista):
#     adelante = 0
#     atras = len(lista)-1
#     esValida = True
#     while adelante < atras:
#         if(lista[adelante] != lista[atras]):
#             esValida = False
#             break
#         adelante += 1
#         atras += 1
#     return esValida

def listaCapicua2(Lista):
    inicio = 0
    final = len(Lista)-1
    while Lista[inicio] == Lista[final]:
        return True
    else:
        return False



def main():
    lista = crearLista()
    print(sumatoriaLista(lista))
    print(lista)
    numero = int(input("Ingrese el numero para eliminarlo. "))
    if(eliminarRepetidos(lista,numero)):
        print("Se elimino el numero",numero,"de la lista satisfactoriamente")
    else:
        print("El numero no se encuentra en la lista")
    print(lista)
    if(listaCapicua2(lista)):
        print("La lista  es capicua")
    else:
        print("La lista no es capicua")    
main()