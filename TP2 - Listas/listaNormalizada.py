'''
Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. 
Desarrollar también un programa que permita verificar el comportamiento de la función. 
Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].


'''


def crearLista():
    lista = []
    for i in range(1,11):
        lista.append(i)
    return lista

def normalizar(lista):
    aux = []
    for i in (lista):
        aux.append(i/4)
    return aux


def main():
    lista = crearLista()
    print(lista)
    print(normalizar(lista))
main()