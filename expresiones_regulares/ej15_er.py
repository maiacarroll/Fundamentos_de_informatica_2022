###Realizá un programa que validar si una cuenta de mail está escrita correctamente
import re
def validar_mail_correcto(mail):
     valido = bool(re.match(r'(\S+)@(\w+).(\w+)', mail))
     print(valido)

validar_mail_correcto("hola@gmail.com")

def mail_correct(mail):
    "[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-z]{1,9}(\.[a-z]{2,9}){1,2}"
print(mail_correct("maiacarroll1@gmail.com"))




def mailco(mail):
    print (bool(re.match(r"(\S+) @ (\w+)) ", mail)))
