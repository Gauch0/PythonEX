'''

Escribir un programa que calcule la suma acumulada a partir de una lista de números. 
El programa debe generar una nueva lista donde el primer elemento es el mismo de la lista original, el segundo elemento es la suma del primero más el segundo, 
el tercer elemento es la suma del primero más el segundo más el tercero y así 
sucesivamente. 

Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].


'''

def sumaAcumulada(lista):
    aux = []
    for i in lista:
        aux.append(lista[i]+lista[i+1])
    return aux


def main():
    lista = [1,2,3]
    print(sumaAcumulada(lista))
main()