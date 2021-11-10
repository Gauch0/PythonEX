'''
Desarrollar una función que reciba tres números positivos y devuelva el mayor de 
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el 
máximo hallado, o un mensaje informativo si éste no existe.
'''


def mayorStricto(uno,dos,tres):
    if(uno > dos):
        if(uno > tres):
            return True
    if(dos > uno):
        if(dos > tres):
            return True
    if(tres > uno):
        if(tres > dos):
            return True

def main():
    uno = int(input("Ingrese el primer numero: "))
    dos = int(input("Ingrese el segundo numnero: "))
    tres = int(input("Ingrese el tercer numero: "))
    print(mayorStricto(uno,dos,tres))

    if(mayorStricto(uno,dos,tres)):
        print("Hay mayor estricto")
    else:
        print("-1")

main()
