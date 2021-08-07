from mypy.miembroequipo import MiembroEquipo
class Deportista(MiembroEquipo):
        '''Representa a un deportista'''
        def __init__(self, nombre, edad, marca):
                super().__init__(nombre, edad)   
                self.marca = marca
                print (f'Initializado el deportista: {self.nombre}')
        def info(self):
                super().info()
                print (f'Marca: {self.marca}')