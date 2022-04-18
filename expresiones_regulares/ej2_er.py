import re 
def tiene_caracteres(string):
    return bool(re.findall("[a-zA-Z0-9.]", string))

print(tiene_caracteres("maia"))
print(tiene_caracteres())