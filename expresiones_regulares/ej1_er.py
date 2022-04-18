#ejercicio1
import re
def caracteres_permitidos(palabra):
    return bool(re.search("[a-zA-Z0-9.]", palabra))

print(caracteres_permitidos("///"))
print(caracteres_permitidos("maia"))

#bool --> me transforma algo que le paso True o False
