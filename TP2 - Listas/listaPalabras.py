'''

Eliminar de una lista de palabras las palabras que se encuentren en una segunda 
lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.


'''

def eliminarRepetidas(remover,ListaPalabras):
    aux = []
    for i in (remover):
        for x in (ListaPalabras):
            if i == x:
                ListaPalabras.remove(i)
    return ListaPalabras
    


def main():
    ListaPalabras = ['Juan','Matias','Nicolas','Esteban','Matias','Lucas']
    remover = ['Matias','Nicolas']
    print(eliminarRepetidas(remover,ListaPalabras))
main()