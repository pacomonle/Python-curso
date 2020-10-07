"""
Ejercicio 2
- añadir valores a una lista hasta que su longitud sea menor a 20
- hacerlo con while y con for
"""

print('############# ejercicio Crear una lista dinamica de 20 elementos ##################')
"""
lista = []
for contador in range(1,21):
    lista.append(f'elemento - {contador}')
    print(f'Mostrando el: '+ lista[contador])
    pass
else:
    print('ha has llegado a 20 elementos')
    pass
"""
lista = []
valor  = input(f'Añade un elemento a la lista FOR ? ')
lista.append(valor)
for elemento in lista:  
    if len(lista) != 21 :
        print(f'LLevamos {len(lista)} ud')
        valor  = input(f'Añade un elemento a la lista ? ')
        lista.append(valor)
        pass
    else :
        print(f'esta es tu lista: {lista}')
        break
    pass

lista = []
valor  = input(f'Añade un elemento a la lista WHILE ? ')
lista.append(valor)
while len(lista) != 21:
     print(f'LLevamos {len(lista)} ud')
     valor  = input(f'Añade un elemento a la lista ? ')
     lista.append(valor)
     pass
else:
    print(f'esta es tu lista: {lista}')
    pass