#lista de string --> frase
import re
def lista_en_frase(lista,frase):
    return bool(re.search(lista in frase))

lista11 = ["hola", "como va", "chau"]
print(lista_en_frase(lista11, "hola, como va chau"))