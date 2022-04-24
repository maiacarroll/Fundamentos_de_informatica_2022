def sexta_quinta (palabra):
    if len( palabra) <= 4:
        return "no tiene ni 5ta ni 6ta letra"
    else:
        return str.upper(palabra [4]), str.upper(palabra[5])

print(sexta_quinta("maiuchisssss"))




#ejercio2
s1= input ("ingresar texto 5ta y 6ta: ")