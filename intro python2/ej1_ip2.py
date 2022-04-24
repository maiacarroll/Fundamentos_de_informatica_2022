print("messi")
print("papa")

#1
def mayuscula_o_minuscula(palabra):
    if palabra[0] == str.upper(palabra[0]):
        return "Mayuscula"
    elif palabra[0] == str.lower(palabra[0]):
        return "Minuscula"
print(mayuscula_o_minuscula("Messi"))
print(mayuscula_o_minuscula("messi"))
print(mayuscula_o_minuscula("maia"))

