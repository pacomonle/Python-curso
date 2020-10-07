"""
Ejercicio 6
Mostrar todas las tablas de multiplicar del 5 al 10
"""

for contador in range( 5 , 11 ):
    print(f'La tabla del {contador}')
    for item in range( 1 , 11 ):
        print(str(contador) + ' x ' + str(item) + ' = ' + str(contador*item))
        pass

    pass