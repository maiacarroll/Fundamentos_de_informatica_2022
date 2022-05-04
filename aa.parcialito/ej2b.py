
#Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
#El modelo debe entender estos mensajes:

#arrancar() , se pone en primera con 500 rpm.
#subirCambio()
#bajarCambio()
#subirRPM(cuantos)
#bajarRPM(cuantos)
#velocidad()
#consumoActualPorKm(), calcula el consumo actual y lo devuelve

class Auto():
    def __init__(self):
        self.cambio = 0
        self.rpm = 0
        self.consumo = 0.05
    
    def arrancar(self):
        self.cambio = 1
        self.rpm = 500
    
    def subirCambio(self):
        if self.cambio < 5:
            self.cambio += 1

    def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1
    
    def subirRPM(self, rpm):
        if self.rpm + rpm <= 5000:
            self.rpm += rpm
        else:
            self.rpm = 5000

    def bajarRPM(self, rpm):
        if self.rpm + rpm >= 500:
            self.rpm -= rpm
        else:
            self.rpm = 500

    def velocidad(self):
        velocidad = (self.rpm / 100) * (0.5 + (self.cambio / 2))
        print("La velocidad es:", velocidad)

    def consumoActualPorKm(self):
        if self.rpm > 3000:
            consumo_por_rpm = self.consumo * ((self.rpm - 2500) / 500)
            if self.cambio == 1:
                print("El consumo es: ", consumo_por_rpm * 3)
            elif self.cambio == 2:
                print("El consumo es: ", consumo_por_rpm * 2)
            else:
                print("El consumo es: ", consumo_por_rpm)
        else:
            if self.cambio == 1:
                print("El consumo es: ", self.consumo * 3)
            elif self.cambio == 2:
                print("El consumo es: ", self.consumo * 2)
            else:
                print("El consumo es: ", self.consumo)


auto1 = Auto() 
auto1.arrancar() # cambio 1, 500 rpm 
auto1.subirRPM(3500) # cambio 1, 4000 rpm
auto1.subirCambio() # cambio 2 4000 rpm
auto1.subirCambio() # cambio 3 4000 rpm
auto1.subirCambio() # cambio 4 4000 rpm
auto1.bajarCambio() # cambio 3 4000 rpm

print(auto1.cambio)
print(auto1.rpm)

auto1.velocidad()
auto1.consumoActualPorKm()

print("---------------------------Cambian los valores del auto--------------------------")

auto1.bajarRPM(3000)
print("Cambio del auto: ", auto1.cambio)
print("RPM del auto: ", auto1.rpm)
auto1.velocidad()
auto1.consumoActualPorKm()