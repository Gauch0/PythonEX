'''
Escribir una función que reciba como parámetro número del 1 al 9 y devuelva el 
resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido. Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333). Escribir 
también un programa para verificar el comportamiento de la función. No se 
permite utilizar facilidades de Python no vistas en clase.

'''


def sumarN(num):
    return num+num*11+num*111+num*1111

def main():
    num = int(input("Ingrese un numero entr 1 y 9: "))
    while(num < 0 or num > 10):
        num = int(input("Ingrese un numero entr 1 y 9: "))
    print(sumarN(num))
main()