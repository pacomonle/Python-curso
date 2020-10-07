"""
ejercicio 5
programa que muestre todos los numeros entre dos facilitados por el usuario
"""
numero1 = int(input('introduce un primer numero ? '))
numero2 = int(input('introduce un segundo numero ? '))
print(f'Los numeros que hay entre {numero1} y {numero2} son :')

if numero1 == numero2 :
    print(f'has puesto el mismo numero en los dos casos no hay numeros en ese rango')
    pass
if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
        pass   
    else:
        print('...the end')
        pass
else :
    for contador in range(numero2, (numero1 + 1)):
        print(contador)
        pass
    else:
        print('...the end')
        pass
        
   

