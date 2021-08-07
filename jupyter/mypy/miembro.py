class MiembroEquipo:
        '''Representa a los miembros de un Equipo deportivo
        que son tanto el entrenador como el deportista'''
        def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
                print(f'Inicializado miembro del Equipo: {self.nombre}')
        def info(self):
                '''Proporciona los detalles'''
                print(f'Nombre: {self.nombre}. Edad: {self.edad}.',end=" ")
class Entrenador(MiembroEquipo):
        '''Representa al entrenador'''
        def __init__(self, nombre, edad, salario):
                super().__init__(nombre, edad)
                self.salario = salario
                print (f'Inicializado el entrenador: {self.nombre}')
        def info(self):
                super().info()
                print (f'Salario: {self.salario}')
class Deportista(MiembroEquipo):
        '''Representa a un deportista'''
        def __init__(self, nombre, edad, marca):
                super().__init__(nombre, edad)   
                self.marca = marca
                print (f'Initializado el deportista: {self.nombre}')
        def info(self):
                super().info()
                print (f'Marca: {self.marca}')