import os
print(os.getcwd)

def no_letra (archivo, letra):
    with open(archivo,"r") as f:
        suma = 0
        for linea in f:
            if linea[0] != letra:
                suma += 1
    return suma

print(no_letra(r"Fundamentos_de_informatica_2022\manipulacion de archivos\arch.txt","P"))

def no_letraAA(arch,letra):
    suma = 0
    with open(arch, "r") as f:
        for linea in f:
            if linea[0] != letra:
                suma += 1
    return suma
print(no_letraAA(r"Fundamentos_de_informatica_2022\manipulacion de archivos\arch.txt","P"))


def no_empiezan_con_string(string):
    import os
    archivo = open(os.getcwd() + "", "r")
    lineas = archivo.readlines()
    sum = 0
    for linea in lineas:
        if not linea.startswith(string):
            sum += 1
    archivo.close()
    return print(sum)
 
no_empiezan_con_string("P")
