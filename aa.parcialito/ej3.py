nueva_lista = []

def obtener_media(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria+= valor
    longitud = len(lista)

    try:
        return sumatoria/longitud
    except ZeroDivisionError:
        print("no se puede dividir por 0") #0 la lista esta vacia o algo del estilo
        


    

