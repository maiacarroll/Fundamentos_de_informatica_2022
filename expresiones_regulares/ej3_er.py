import re


def con_he(string):
    return bool(re.search("he+",string))

print (con_he("hermosa"))
print(con_he("hola"))


#Creá un programa que verifique las siguientes condiciones:

###si un string dado tiene una h seguida de ninguna o más e.

###si un string dado tiene una h seguida de una o más e.

###si un string dado tiene una h seguida de una o más e.

###si un string dado tiene una h seguida de dos o tres e

import re
def tiene_he (palabra):
    return bool(re.search("he+", palabra))