'''

Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter


'''
#a. Utilizando sólo ciclos normales

def filtrarPalabras(cadena,n):
    lista = cadena.split(" ")
    nuevaLista = ""
    for i in range(len(lista)):
        if len(lista[i]) >= n:
            nuevaLista += lista[i] + " "
    return nuevaLista.rstrip()

#b. Utilizando listas por comprensión

def filtrarPalabras2(cadena,n):
    lista = cadena.split(" ")
    nuevaLista = [i for i in lista if len(i) >= n]
    nuevaCadena = " ".join(nuevaLista)
    return nuevaCadena

#c. Utilizando la función filter

def filtrarPalabras3(cadena,N):
    lista = cadena.split()
    nuevaLista = list(filter(lambda x: len(x) >= N, lista))
    nuevaCadena = " ".join(nuevaLista)
    return nuevaCadena


def main():
    cadena = "Esto es una prueba"
    print(filtrarPalabras(cadena,5))
    print(filtrarPalabras2(cadena,5))
main()