def eliminar (arch1,arch2):
    with open(arch1, "r") as f, open (arch2, "w") as a:
        for linea in f.read():
            a.write(linea.strip("\n"))
    ###STRIP--> ELIMINA CARACTERES