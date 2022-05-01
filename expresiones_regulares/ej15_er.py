###Realizá un programa que validar si una cuenta de mail está escrita correctamente
import re
def validar_mail_correcto(mail):
     valido = bool(re.match(r'(\S+)@(\w+).(\w+)', mail))
     print(valido)

validar_mail_correcto("hola@gmail.com")