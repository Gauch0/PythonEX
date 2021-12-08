'''
Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos 
impares de la clave maestra y la segunda con los dígitos pares. Los dígitos se 
numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería 
123 y la clave 2 sería 89.

'''
def claveMaestra(keymaster):
    strKey = str(keymaster)
    key1 = strKey[::2]
    key2 = strKey[1::2]
    return key1,key2


def main():
    keyMaster = int(input("Ingrese la llave maestra: "))
    key1,key2 = claveMaestra(keyMaster)
    print("La primera clave es",key1,"la segunda clave es ",key2,"la clave maestra es ",keyMaster)
main()