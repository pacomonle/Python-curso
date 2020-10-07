""""
Ejercicio 2
script por pantalla que muestre los numeros pares de 1 al 50
"""

contador = 1
acumulador = '0'

for contador in range(1,51) :

    if contador % 2 == 0 :
        acumulador = acumulador + ' , ' + str(contador)
else :
    print(f'Los numeros pares de 1 al 50: \n {acumulador} \n')
       

        
   