class Auto():
    def __init__ (self):
        self.consumo = 0.05
        self.RPM = 0
        self.cambio = None
    def arrancar(self):
        self.cambio= 1
        self.RPM= 500
    def subircambio(self):
        if self.cambio <5:
            self.cambio+=1
    def bajarcambio(self):
        if self.cambio>1:
            self.cambio-= 1
    def subirRPM (self, cantidad):
        if self.RPM + cantidad <= 500:
            self.cambio += cantidad
        else:
            self.RPM = 5000
    def bajarRPM (self, RPM):
        if self.RPM -RPM >=0:
            self.RPM =- RPM
        else:
            self.RPM = 0
    def velocidad(self):
        return ((self.RPM / 100)) * (0,5+(self.cambio /2))
    def consumoactualporkm(self):
        if self.RPM > 3000:
            if self.cambio ==1 :
                return(self.consumo*((self.RPM - 2500)/500)*3)
            elif self.cambio ==2:
                return (self.consumo *(self.RPM -  2500) /500 *2)
            elif self.cambio<= 5:
                return (self.consumo *(self.RPM -  2500) /500)
        elif self.cambio == 1:
            return (self.consumo * 3)
        elif self.cambio ==2:
            return (self.consumo * 2)
        else:
            return (self.consumo)
    def cambioactual(self):
        return (self.cambio)
    def RPMactual (self):
        return (self.RPM)

fiat=Auto
fiat.arrancar()
fiat.subirRPM(3500)
fiat.subircambio()


######### el que hice con lucho


    
    
