"""
Ejercicio 9
Pedir y mostrar numeros al usuario hasta que introduzca el 111
"""

print('Acierta el numero secreto!!!')

key = int(input('introduce un numero ? '))

while key != 111:
    print(f'el {key} no es')
    key = int(input('introduce otro numero ? '))
    pass
else:
    print(f'acertaste es el {key} , enhorabuena!!!')
    pass