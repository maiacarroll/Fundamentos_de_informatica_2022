#ejercicio8
def ejercicio (respuesta):
    nota=0
    if respuesta == "correcta":
        nota+= 4
    elif respuesta == "incorrecta":
        nota-= 1
    else:
        nota += 0
print(ejercicio("incorrecta"))
print(ejercicio("correcta"))

def nota_final (respuesta,nota):
  if respuesta == "correcta":
    return nota + 4
  elif respuesta == "incorrecta":
    return nota - 1
  else:
    return nota

print(nota_final("correcta", 3))




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