#### Consigna N°3
#Escribir una función que, dado un String, permita validar si este se corresponde o no con un teléfono de CABA.
import re

def telefono_caba(string):
    print(bool(re.match(r'[+](54)(9?)(11)(\d{8}$)', string)))

#bool --> retorna True or False
#match --> casi lo mismo que search --> solo que busca en la primer palabra
# r -->siempre en re para que lea el string
#[+] --> porque es un metacaracter
#(9?) --> puede variar si esta o no
# (\d) --> numero
#{8} --> que sean 8 numeros mas, ni mas ni menos
#$ --> fin de linea


def tiene_h(string):
    print(bool(re.search("he{2,3}", string) and not re.search("heeee+", string)))

tiene_h("hee")



telefono_caba("1167958727")
telefono_caba ("+5491167958727")
telefono_caba("+54911679587277")
telefono_caba("+549111111111111111111111111")
telefono_caba("+5491167958727")
tiene_h("heee")
tiene_h("heeermosa")


import re
def telcorr(num):
    return bool(re.findall("54+(9*)+(\d{10})", num))
print(telcorr("5491167958727"))
print(telcorr("54911679587257"))