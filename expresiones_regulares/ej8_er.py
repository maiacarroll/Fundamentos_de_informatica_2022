import re
def solo_numeros(string):
    return re.findall("[0-9]", string)

print (solo_numeros("123456 sigamos contando desde 12"))