def contar(archivo):
    with open(archivo,"r") as f:
        lista_palabras = f.read().split()
        print(len(lista_palabras))
    
print(contar("bio.txt"))

