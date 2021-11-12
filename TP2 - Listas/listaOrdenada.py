'''

Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función.

'''

def crearLista():
    lista = []
    for i in range(20):
        lista.append(i)
    return lista


def listaOrdenada(lista):
    Ordenada = True
    final = len(lista)-1
    for i in range(1,final):
        if(lista[i] > lista[i+1]):
            Ordenada = False
    return Ordenada



def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(listaOrdenada(lista))
main()
