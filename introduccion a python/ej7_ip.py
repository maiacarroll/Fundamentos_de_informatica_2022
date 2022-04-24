

def sueldo (base, venta):
    if venta > 0 :
        return base * (0,1* venta)
    else:
        return base
print(sueldo(40,5))


#ejercicio7
s71= input("sueldo base: ")
s72= input("venta: ")
fin_de_mes= int(s71) + (int(s72)*0.10)
print (fin_de_mes)