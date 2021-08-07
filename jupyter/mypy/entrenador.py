from mypy.miembroequipo import MiembroEquipo
class Entrenador(MiembroEquipo):
        '''Representa al entrenador'''
        def __init__(self, nombre, edad, salario):
                super().__init__(nombre, edad)
                self.salario = salario
                print (f'Inicializado el entrenador: {self.nombre}')
        def info(self):
                super().info()
                print (f'Salario: {self.salario}')
