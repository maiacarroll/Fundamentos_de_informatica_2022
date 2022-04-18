import re 
def reemplazar(string):
    return re.sub("\s",";",string)
print (reemplazar("hola como est/s// /   /"))
