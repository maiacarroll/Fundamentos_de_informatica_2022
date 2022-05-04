import glob
import os
def funcion(arch, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt")
    with open(arch,"a") as s:
        for f in lista_txt:
            file=open(f,"r")
            s.write(file.read())
            file.close()
            
