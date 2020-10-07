"""
FOR
bucle for
"""

contador = 0
resultado = 0
for contador in range(0,5) : 
    print('voy por el ', str(contador))
    resultado += contador

print(f'la suma de los numeros es: {resultado}')

# Ejemplo tablas de multiplicar
print('\n########### Ejercicio tabla mulriplicar ##########')

tabla = int(input('introduce un numero?'))

if tabla < 1 :
    tabla = 1
print(f'Tabla del {tabla}\n')
for contador in range(0,10) :
    if tabla == 13 :
        print('no se pueden mostrar numero prohibidos')
        break
    else :
        print(f'{tabla} x {contador} = {tabla*contador}')
else :
   print('...tabla finalizada')