def letra(string):
    diccionario = {}
   
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
        
    return diccionario

print(letra("maia"))