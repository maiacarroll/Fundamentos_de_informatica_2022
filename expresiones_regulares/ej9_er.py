## caracteres entre guiones
import re
def entre_guiones(string):
    return (re.findall("-,-", string))

print (entre_guiones ("nunca dejes atras tus -suenos-"))