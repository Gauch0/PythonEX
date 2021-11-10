'''

Desarrollar una función que reciba como parámetros dos números enteros y devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si recibe 
1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no 
vistas en clase.

'''


def concatenarNumeros(num1 , num2):
    return str(num1) + str(num2)


def main():
    num = int(input("Ingrese el primer numero : "))
    num2 = int(input("Ingrese el segundo numero: "))
    print(concatenarNumeros(num , num2))
main()