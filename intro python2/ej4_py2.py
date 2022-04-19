#4
def cobro_paquete(ubicación, peso):
    if peso > 5:
        return "Entrega rechazada"
    elif ubicación == "América del sur":
        return peso * 10.00
    elif ubicación == "América central":
        return peso * 15.00
    elif ubicación == "América del norte":
        return peso * 18.00 
    elif ubicación == "Europa":
        return peso * 24.00 
    elif ubicación == "Asia":
        return peso * 30.00
print(cobro_paquete("Asia", 4))

