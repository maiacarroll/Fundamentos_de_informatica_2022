import re
def substrings (string):
    return (re.search("@(.*)&",string)).span() and (re.search("@(.*)&", string))

print(substrings("hola @maia como estan vos & tus amigos?"))

