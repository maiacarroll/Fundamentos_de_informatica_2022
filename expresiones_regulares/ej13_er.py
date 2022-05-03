import re
def reemplazar(string):
    return re.sub("\W+","_", string,2)

print(reemplazar("hola como est//s"))
print(reemplazar("holac//apa"))