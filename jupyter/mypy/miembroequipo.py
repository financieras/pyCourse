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