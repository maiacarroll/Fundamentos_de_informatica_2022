#2
def positivo_negativo(numero):
    resultado = ""
    if numero < 0:
        resultado += "Negativo"
    elif numero > 0:
        resultado += "Positivo"
    else:
        resultado += "Cero"
    return resultado + " " + par_o_impar(numero)

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
print(positivo_negativo(4))
print(positivo_negativo(3))
print(positivo_negativo(-9))