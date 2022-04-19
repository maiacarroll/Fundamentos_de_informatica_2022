class NoteBook:
    def __init__ (self, marca, modelo, precio):
        self.marca=marca
        self.modelo= modelo
        self.precio =precio
    def descuento(self,porcentaje):
        desc1 = self.precio* (porcentaje/100)
        print("el valor es de " + str(desc1 + self.precio))
    