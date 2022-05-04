def guardar(archivo, lineas):
    lista=[]
    with open(archivo,"r") as f:
        for i in f:
            list.append (i)
    print (lista[lineas:])
print(guardar("bio.txt",3))