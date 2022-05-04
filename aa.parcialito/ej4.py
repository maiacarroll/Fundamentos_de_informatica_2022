###Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada Resultado y,
#  por otro, que lea todos los archivos con extensión .txt y escriba el contenido de todos en un único archivo llamado 
# texto_completo.txt, que tiene que estar dentro de la carpeta Resultado. NO se pueden usar rutas absolutas
import os, glob

def unir_txt():
    os.mkdir("Restultado") ######creando carpeta--> me para ahi
    lista_txt = glob.glob("*.txt") ###### carpeta vieja donde estan los txt --> glob glob --> filtrar solo los q terminan con txt
    salida = open("Resultado/texto_completo.txt", "a") ##### me crea el archivoo
    for txt in lista_txt:
        archivo = open(txt, "r")
        salida.write(archivo.read())    ###es tipo "a" --> escribe algo aparte, no arriba
        archivo.close()
    salida.close()

#alternativa
def unir_txt():
    os.mikdir("Restultado")
    lista_txt = glob.glob("*.txt")
    with open("Resultado/texto_completo.txt", "a") as salida:
        for txt in lista_txt:
            with open(txt, "r") as archivo:
                salida.write(archivo.read())

#################################################################################################################

##eldeguada --> esta bien pero es mejor el de arriba




def crear():
    os.chdir(r"Fundamentos_de_informatica_2022\aa.parcialito") #me muevo a la carpeta donde voy a trabajar 
    lista_txt = glob.glob("*txt") #armo lista con nombre de los archivos txt
    os.mkdir("_resultado_") #creo la nueva carpeta
    path_archivos = os.getcwd()
    path_carpeta = os.path.join (path_archivos, r"_resultado_")
    for file_txt in lista_txt:    #por cada archivo
        os.chdir(path_archivos)   #me muevo a la carpeta donde esta el archivo

        with open(file_txt, "r") as archivo_entrada: #lo abro
            archivo = archivo_entrada.read() #lo leo y lo guardo en una variable

            os.chdir(path_carpeta) #me meto en la carpeta nueva

            with open("texto_completo.txt" , "a") as archivo_salida:
                archivo_salida.write(archivo) # lo escribo en el nuevo archivo

    crear ()