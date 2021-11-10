'''
Para un número entero N menor de 100 recibido como parámetro, escribir un programa que utilice una función para devolver la suma de los cuadrados de aquellos 
números entre 1 y N que están separados entre si por cuatro unidades. (12 + 52 + 92 + 132 + …)

'''


def CalcularCuadrado(numero):
    i=1
    for i in range (numero):
        if(i <= numero):
            print(i*2)


def main():
    numero = int(input("Ingrese un numero menor a 100: "))
    if(numero > 100):
        numero = int(input("Ingrese por favor un numero menor a 100: "))
    CalcularCuadrado(numero)
main()