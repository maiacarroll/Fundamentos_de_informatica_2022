def no_letra (arch, letra):
    with open(arch, "r") as f:
        suma = 0
        for linea in f:
            if linea[0] != letra:
                suma += 1
            else:
                return suma
    
print(no_letra(r"Fundamentos_de_informatica_2022\manipulacion de archivos\arch.txt", "p"))