'''
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares. Escribir además un programa que permita verificar su 
funcionamiento.


'''


def esCapicua(cad):
    bandera = False
    if cad == cad[::-1]:
        bandera = True
    return bandera

def main():
    cad = input("Ingrese la cadena")
    if esCapicua(cad):
        print("La frase",cad,"es capicua")
    else:
        print("No es capicua")
main()