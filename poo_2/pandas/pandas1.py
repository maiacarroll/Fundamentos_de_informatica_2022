#ejercicio 4 
import pandas as pd
dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
dict2 = {}
for clave, valor in dict1.items():
    pares=[]
    impares=[]
    potencia=[]
    for i in range(len(valor)):
        if i % 2 == 0:
            pares.append(valor[i])
        else:
            impares.append(valor[i])
    for i in range(len(pares)):
        potencia.append(pares[i] ** impares[i])
    dict2[clave]=potencia
print(dict2)

