class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False  
    def arrancar(self):
        self.enmarcha=True   
    def acelerar(self):
        self.acelera=True   
    def frenar(self):
        self.frena=True 
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \
              \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

class Furgoneta(Vehiculo):                          # creamos la clase Furgoneta que hereda de la clase Vehiculo
    def cargada(self,carga):
        self.carga=carga
        if self.carga:
            return "La Furgoneta está cargada"      # en este método usamos un return para informar 
        else:
            return "La Furgoneta no está cargada"

class Moto(Vehiculo):
    hcaballito=""                                    # creamos la nueva variable: haciendo el caballito
    def caballito(self):                             # creamos el método caballito
        self.hcaballito="Voy haciendo el caballito"  # el método modifica el valor de la variable hcaballito

    def estado(self):                                # = nombre y nº de parámetros que el método sobreescrito de la clase padre
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \
              \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}\
              \n{self.hcaballito}")

class VElectrico(Vehiculo):                        # ahora esta clase hereda de Vehiculo 
    def __init__(self,marca,modelo):               # ahora añadimos marca y modelo
        super().__init__(marca,modelo)             # super() va antes que autonomía
        self.autonomia=300
    def cargarEnergia(self):
        self.cargando=True