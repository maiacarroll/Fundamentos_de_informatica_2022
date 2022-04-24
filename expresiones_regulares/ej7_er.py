##Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
import re
def palabras_especiales (string):
    return bool(re.findall("[A-Za-z0-9]", string))
print(palabras_especiales("maivavyjdvak"))

