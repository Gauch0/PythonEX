'''
Escribir un programa para generar una lista con los múltiplos de 7 que no sean 
múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.

'''

def crearLista():
    lista = []
    for i in range(2000,3500):
        if i % 5 != 0 and i % 7 == 0:
            lista.append(i)
    return lista


def porComprension():
    lista = [i for i in range(2000,3500) if i % 5 != 0 and i % 7 == 0]
    return lista

def main():
    crearLista()
    print(porComprension())
main()