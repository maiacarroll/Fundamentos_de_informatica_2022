import re


def con_he(string):
    return bool(re.search("he+",string))

print (con_he("hermosa"))
print(con_he("hola"))