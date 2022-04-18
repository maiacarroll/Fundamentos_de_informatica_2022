import re
def empieza_con(nnumero,string):
    return bool(re.match(str(nnumero),string))
print(empieza_con("7", "vristiano ronaldo"))