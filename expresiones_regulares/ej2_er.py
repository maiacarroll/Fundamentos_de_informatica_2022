import re 
def tiene_caracteres(string):
    return bool(re.findall("[a-zA-Z0-9.]", string))

print(tiene_caracteres("maia"))
print(tiene_caracteres())


###describí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
def caracteres_prermitidos (palabra):
    return bool(re.findall ("[[a-zA-Z0-9.]", palabra))