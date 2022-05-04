#ejercicio1
import re
def caracteres_permitidos(palabra):
    return bool(re.search("[a-zA-Z0-9.]", palabra))

print(caracteres_permitidos("///"))
print(caracteres_permitidos("maia"))

#bool --> me transforma algo que le paso True o False


####Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
def caracter_permitido (palabra):
    return bool(re.search ("[a-zA-Z0-9]", palabra))

##bool pq hay q ver si es q esta o no --> me retornaria t o f dependiendo lo q sea
##averiguarpq se escribe asi y no de otra manera