try:
    arch = open("legajo.txt","wt")
    legajo = int(input("Ingrese su numero de legajo (-1 para finalizar): "))
    while legajo != -1:
        nombre = input("Ingrese su nombre: ")
        #escribe un registro en el archivo
        arch.write(str(legajo)+":"+nombre+"\n")
        legajo = int(input("Ingrese su numero de legajo (-1 para finalizar): "))
except IOError:
    print("No se pudo crear el archivo")
except ValueError:
    print("No se pudo convertir el tipo de dato legajo")
finally:
    arch.close()

try:
    archivo = open("legajo.txt","rt")
    linea = archivo.readline()
    while linea:
        legajo, nombre = linea.split(":")
        if int(legajo) > 10000:
            print("Legajo: ",legajo,"nombre: ",nombre)
        linea = archivo.readline()
except IOError:
    print("No se pudo crear el archivo")
finally:
    archivo.close()