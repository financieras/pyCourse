import sys
nombre = sys.argv[1]
numero = int(sys.argv[2])
print(f'Hola {nombre} me alegro de que te guste el número {numero}.')
print('Seguro que te agrada ver una lista con tu número favorito ')
print([numero for _ in range(numero)])