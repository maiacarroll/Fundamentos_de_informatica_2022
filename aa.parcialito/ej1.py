###Escribir funciones que, dado un String, permitan obtener
#- cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.
# - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

import re
def cuantas_veces (string):
    return len(re.findall("bc9", string))

#def sin_c (string):
 #   return re.findall("aa([^c].*?)gg", string)

    #el ? favorece los matches internos
    # ^c --> desde aa a gg no tiene q haber C
    #* --> ning o mas
    #+ --> 1 o mas
    #? --> cero o una
print(cuantas_veces("maiabc9suhdya8gsbc9"))
