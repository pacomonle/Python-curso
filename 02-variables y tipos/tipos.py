# None -> equivalente null
nada = None

# mostrar tipo de dato 
var = 25.2
print(type(var))

# str -> string 
cadena= 'Hola mundo'
print(type(cadena))

# int
entero = 25
print(type(entero))

# float
decimal = 10.5
print(type(decimal))

# bool
booleano = True
print(type(booleano))

# list -> equivalente array
lista = [1, 10, 15, 20]
print(type(lista))

# tuple -> lista de datos que no pueden cambiar
tupla = ('coche', 'casa', 'curso')
print(type(tupla))

# dict -> equivalente a JSON - clave:valor
diccionario = {
    'nombre': 'Francisco',
    'edad': 45
}
print(type(diccionario))

# range
rango = range(9)
print(rango)
print(type(rango))

# bytes
dato_byte = b"probando"
print(dato_byte)
print(type(dato_byte))

# conversion de datos
numero = 50
numerostr= str(50)
print(type(numerostr))

numerostr= int(50)
print(type(numerostr))
