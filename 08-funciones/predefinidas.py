"""
funciones PREDEFINIDAS
"""
# funcion print() y type()
nombre = 'Noel Monleon'
print(nombre)
print(type(nombre))

# funcion isinstance()
comprobar = isinstance(nombre, str)
if comprobar:
    print(f'{nombre} es un tipo de dato string')
    pass
else: 
    print(f'{nombre} NO es un tipo de dato string')
    pass

if not isinstance(nombre, float):
    print(f'{nombre} NO es un tipo de dato float')
    pass

# funcion que limpia espacios del string
frase = '   pacomonle@live.com '
print(frase.strip())

# funcion para eliminar variables
year = 2021
print(year)
del year
# print(year)

# funcion comprobar variable vacia
texto = 'abcd'
print(len(texto))

# funcion buscar caracteres dentro de un string
frase = 'la vida es bella'
print(frase.find('vi'))

# funcion reemplazar caracteres en un string
nueva_frase = frase.replace("bella","increible")
print(nueva_frase)

# funcion para pasar a Mayusculas y Minusculas
print(nombre.lower())
print(nombre.upper())