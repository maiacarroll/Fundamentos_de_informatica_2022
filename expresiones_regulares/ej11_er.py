#lista de strings dos palabras que empiezan con p y las imprima
import re
def empieza_con_p (lista_string):
    return (re.findall("[^p]", lista_string))

Lista_de_ejemplo=["Práctica Python", "Práctica C++", "Práctica Fortran"]

print(empieza_con_p(Lista_de_ejemplo))
