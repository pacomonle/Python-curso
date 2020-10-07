"""
Ejercicio 8
obtener el x% de un numero, con datos facilitados por el usuario
"""
numero = int(input('introduce un numero ? '))
porcentaje = int(input('introduce el porcentaje a obtener ? '))

print(f'El {porcentaje} % de {numero} es : ')

resultado = ( numero * porcentaje ) / 100

print('el resultado es -> ' + str(resultado))