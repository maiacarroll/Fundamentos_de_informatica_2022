def imprimir(archivo,lineas):
    contador=lineas-1
    with open(archivo,"r") as f:
        listas = f.readlines()
        print(listas[:contador +1])
    
    print(imprimir("bio.txt",1))
    

  
