'''

 Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.



'''

import random

lista = [i for i in range(100,200)  if i % 2 != 0]
print(lista)