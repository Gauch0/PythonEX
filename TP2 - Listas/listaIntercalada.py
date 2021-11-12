'''

Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].


'''

import random

def crearLista():
    lista = []
    for i in range(20):
        numeros = random.randint(10,99)
        lista.append(numeros)
    return lista
        
def crearRebanada(listaA,listaB):
    largo = len(listaB)

    for i in range(1,largo,2):
        listaA[i:i]=[listaB[i//2]]
    return listaA


def main():
    listaA = crearLista()
    listaB = crearLista()
    print("Lista A",listaA)
    print("Lista B",listaB)
    print("Lista resultante",crearRebanada(listaA,listaB))
main()