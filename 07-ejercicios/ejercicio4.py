"""
ejercicio 4
Crear programa calculadora -> pidiendo 2 valores al usuario
"""
print('############# PROGRAMA CLACULADORA #############')
numero1 = int(input('introduce el primer numero?'))
numero2 = int(input('introduce el segundo numero?'))
print(f'La calculadora de lo numeros {numero1} y {numero2} es: ')
suma = numero1 + numero2
resta = 0
if numero1 >=  numero2 :
    resta = numero1 - numero2
else : 
    resta = numero2 - numero1
multiplicacion = numero1*numero2
division = 0 
if numero1 / numero2 > 1 :
    division = numero1 / numero2
else : 
    division = numero2 / numero1

print('La suma es : ' + str(suma))
print('La resta es : ' + str(resta))
print(f'La multiplicacion es : {multiplicacion}')
print(f'La division es : {division}')