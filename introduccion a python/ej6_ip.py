#ejercicio6
def horario (numero):
    if numero < 60:
        return " 0 horas y " + int(numero) + " minutos"
    else:
        return int(numero)/60 + "horas y  minutos"
    
    


print(horario(73))
s6= input("minutos: ")
horas = (int(s6)//60)
minutos= int(s6) - (int(horas)*60)
print(("horas: ")+ str(horas)+ " y minutos " + str(minutos))