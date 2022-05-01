def no_letra (archivo, letra):
    with open(archivo,"r") as f:
        suma = 0
        for linea in f.read().split("\n"):
            if linea[0] != letra:
                suma += 1
    return suma

print(no_letra(r"Fundamentos_de_informatica_2022\manipulacion de archivos\arch.txt","P"))

