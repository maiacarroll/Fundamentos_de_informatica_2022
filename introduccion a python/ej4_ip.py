#ejercicio4
def nombre_completo (nombre, apellido, apellido2):
    return str.title (nombre), str.title(apellido),str.title(apellido2)

print(nombre_completo("maia", "carroll", "aramburu"))


def nombre(n, a1, a2):
    return str.upper(n[0]) + " " + str.upper(a1[0]) + " " + str.upper (a2[0])
print(nombre("maia","carroll","aramburu"))