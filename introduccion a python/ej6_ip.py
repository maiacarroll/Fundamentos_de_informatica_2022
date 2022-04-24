#ejercicio6
def horario (numero):
    if numero < 60:
        return numero + " " + "minutos"
    


print(horario(73))
s6= input("minutos: ")
horas = (int(s6)//60)
minutos= int(s6) - (int(horas)*60)
print(("horas: ")+ str(horas)+ " y minutos " + str(minutos))