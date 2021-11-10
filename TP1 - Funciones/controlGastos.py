'''

Escribir dos funciones para imprimir por pantalla cada uno de los siguientes 
patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
**********
**********
**********
**********
**********

**
****
******
********
**********


'''

def primerFila(num):
    for i in range(num+1):
        print("*"*num)

def segundaFila(num):
    ast = ''
    for i in range(num+1):
        ast = '*'*i
        print(ast)


def main():
    num = int(input("Ingrese el numero de asteriscos a imprimir: "))
    primerFila(num)
    segundaFila(num)
main()