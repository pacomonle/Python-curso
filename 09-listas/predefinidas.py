"""
Funciones y Metodos para LISTAS
"""
cantantes = ['Nino Bravo', 'Camilo Sexto', 'Isabel Pantoja', 'rocio Jurado']
numeros = [1,8,3,4,10,7,6,2,9,5]

# Ordenar
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.insert(2,'Perales')
print(cantantes)
numeros.append(11)
print(numeros)

# Eliminar elementos
cantantes.pop(-1)
print(cantantes)
numeros.remove(10)
print(numeros)

# invertir lista
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Nino Bravo' in cantantes)

# contar elementos
print(len(numeros))

# cuantas veces aparece un elemento en una lista
print(numeros.count(11))

# conseguir un indice
print(cantantes.index('Nino Bravo'))

# concatenar listas
cantantes.extend(numeros)
print(cantantes)