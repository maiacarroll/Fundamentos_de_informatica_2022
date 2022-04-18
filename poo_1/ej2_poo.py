from tkinter.tix import NoteBook
from tkinter.ttk import Notebook
from Fundamentos_informaticaANA.POO.Teoria.materiales.aves import Golondrina


Class Golondrina:
    def __init__ (self,energia):
        self.energia = energia
    def comer_alpiste(self,gramos):
        self.energia+=4 *gramos
    def volar_en_circulos (self):
        self.volar(0)

Class NoteBook:
    def __init__ (self, marca, modelo, precio):
        self.marca=marca
        self.modelo= modelo
        self.precio =precio
    def descuento(self,porcentaje):
        desc1 = self.precio* (porcentaje/100)
        print("el valor es de " + str(desc1 + self.precio))





