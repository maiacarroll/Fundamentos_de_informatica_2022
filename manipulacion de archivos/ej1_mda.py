def no_p (archivo,letra):
    suma=0
    with open(archivo,"r") as f:
        for linea in f.read().split("\n"):
            if linea [0] != letra:
                suma+=1
    print(suma)

print(no_p("bio.txt","m"))
