"""
Ejercicio 3
script que muestre los cuadrados delos 20 primeros numeros
usando for y while
"""

# while 
print('bucle while -> El cuadrado de los 20 primeros numeros:')
contador = 1
while contador <= 20 :
    print(f'{str(contador)} elevado al cuadrado es : {contador*contador}')
    contador += 1
    pass
else:
    print('...se acabo')
    pass

# for
print('bucle for -> El cuadrado de los 20 primeros numeros:')
contador = 1
for contador in range(1,21) :
    print(f'{str(contador)} elevado al cuadrado es : {contador*contador}')
    pass
else:
    print('...se acabo')
    pass