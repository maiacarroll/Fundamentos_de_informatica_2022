#10
def letra(string):
    diccionario = {}
   
    for letra in string:
        str.upper[letra] != str.lower[letra]
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra("bebet benedetto"))
print(letra("maia"))
print("mAia")

