#ejercicio8

s8= [input("respuesta 1: "), input("respuesta 2: "), input("respuesta 3: ")]
nota = 0
for respuesta in s8:
    if respuesta == "correcta":
        nota+= 4
    elif respuesta == "incorrecta":
        nota+=1
    else:
        nota
print(nota)