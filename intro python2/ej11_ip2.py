def letra(string):
    diccionario = {}
   
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 0
    return diccionario

print(letra("maia"))