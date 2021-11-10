
'''
Desarrollar una función que reciba tres números enteros positivos y verifique si 
corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False 
según la fecha sea correcta o no. Realizar también un programa para verificar el 
comportamiento de la función.
'''


def calcularFecha(d,m,a):
    if(d <= 31):
        if(m <= 12):
            if(a <= 2100):
                return True
    else:
        return False

    

def main():
    d = int(input("Ingrese el dia : "))
    m = int(input("Ingrese el mes : "))
    a = int(input("Ingrese el anio : "))
    
    if(calcularFecha(d,m,a)):
        print("True")
    else:
        print("False")

main()