''' 3. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
aleatorios. Sume los pares y saque el promedio de los impares. '''

import random

tam=random.randint(10,25)
lista=[]
sumapar=0
sumaimpar=0

for indice in range(tam):
    lista.append(round(random.random()*100))
    if indice % 2 == 0:
        sumapar += lista[indice]
    else:
        sumaimpar += lista[indice]
        promedioimpar = sumaimpar//len(lista)
print(lista,"\nla lista tiene un tamaño de: ", len(lista))
print('La suma de los pares es de:',sumaimpar,'\nY el promedio de los impares es de:',promedioimpar)