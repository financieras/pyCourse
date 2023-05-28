import sys
if len(sys.argv) == 3:
    nombre = sys.argv[1]
    numero = int(sys.argv[2])
    print(f'Hola {nombre} me alegro de que te guste el número {numero}.')
    print('Seguro que te agrada ver una lista con tu número favorito ')
    print([numero for _ in range(numero)])
else:
    print("ERROR: se necesitan dos argumentos, 1º su nombre y 2º su número favorito.")
    print("Ejemplo: pyhton ejemplo1_0040.py \"Ana Vega\" 4")