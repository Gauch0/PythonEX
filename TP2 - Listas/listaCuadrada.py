'''

Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 


'''


def crearLista():
    numero = 20
    lista = []
    for i in range(1,numero):
        lista.append(i**2)
    return lista

def ultimosValores(lista):
    aux = []
    for i in range(10,len(lista)-1):
        aux.append(lista[i])
    return aux


def main():
    lista = crearLista()
    print(lista)
    print(ultimosValores(lista))
main()
