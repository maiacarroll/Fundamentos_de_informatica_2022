

def sueldo (base, venta):
    if venta >= 4 :
        return base + (0.1* base)*venta
    else:
        return base
print(sueldo(40,5))


