"""
WHILE
bucle while
"""

contador = 0
while contador <= 10 :
    print(f'estoy en el nuemro {contador}')
    contador += 1

print('-------------------------')
item = 1
muestrame = str(0)
while item <= 10 :
    muestrame= muestrame + ' , ' + str(item)
    item += 1
print(muestrame)


# Ejemplo tablas de multiplicar
print('\n########### Ejercicio tabla multiplicar ##########')

tabla = int(input('introduce un numero?'))

if tabla < 1 :
    tabla = 1
print(f'Tabla del {tabla}\n')
element = 0
while element <= 10 :
    print(f'{tabla} x {element} = {tabla*element}')
    element += 1
else :
    print('tabla terminada')