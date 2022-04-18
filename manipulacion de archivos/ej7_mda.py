def palabra_larga(arch):
    caracteres = 0
    palabra = " "
    with open(arch,"r") as f:
        lista_palabras= f.read().split()
        for word in lista_palabras:
            if len(word)> caracteres:
                caracteres= len(word)
                palabra = word
    return palabra, caracteres
