"""
Ejercicio 7
Mostrar todos los numeros impares que hay entre dos numeros facilitados por el usuario
"""

numero1 = int(input('introduce el primer numero?'))
numero2 = int(input('introduce el segundo numero?'))

print(f'Los numeros impares que hay entre {numero1} y {numero2} son :')

if numero1 > numero2:
    for contador in range(numero2, (numero1+1)):
        if contador%2 != 0:
            print(contador)
            pass
        pass
    pass
else :
     for contador in range(numero1, (numero2+1)):
        if contador%2 != 0:
            print(contador)
            pass
        pass

