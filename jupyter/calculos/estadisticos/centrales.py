def media(*valores):
    total=0
    for k,v in enumerate(valores):
        total += v
    print(f"La media es {total/(k+1)}")

def moda(lista):
    frequency = {}
    for value in lista:
        frequency[value] = frequency.get(value, 0) + 1
    most_frequent = max(frequency.values())
    modas = [key for key, value in frequency.items() if value == most_frequent]
    return modas