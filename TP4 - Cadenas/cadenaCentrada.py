'''

.Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.

'''

def esCentrada(cadena):
     cad = cadena.center(80," ")
     return cad

def main():
    cadena = input("Ingrese una frase: ")
    print(esCentrada(cadena))
main()