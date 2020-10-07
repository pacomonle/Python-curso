"""
Ejercicio 1
- crear lista 8 elementos
- recorrer lista y mostrarla
- ordenarla
- mostrar longitud
- buscar elemento introducido por el usuario
"""
# crear lista
listaNumeros = [2,1,8,7,5,6,4,3]
"""
for numero in listaNumeros:
    print(f'EL numero con indice {listaNumeros.index(numero)} es: {numero}')
    pass
"""
# funcion listar
def listarNumeros(arrayNumeros):
    """
    funcion que recorra un listado y devuelva un string
    """
    texto = ''
    # recorrer lista
    for numero in listaNumeros:
        texto = 'EL numero con indice ' + str(listaNumeros.index(numero)) + ' es: ' + str(numero) + '\n' + texto
        pass
    return texto
    pass
print( listarNumeros(listaNumeros))
# ordenar
listaNumeros.sort()
print(f'La lista ordenada es: {listarNumeros(listaNumeros)}')
# len(listaNumeros) -> longitud
print(f'La longitud de la lista es: {len(listaNumeros)}')
# realizar busqueda en el array
busqueda = int(input('dime un numero a buscar ? '))
comprobar = isinstance(busqueda, int)
while not comprobar or  busqueda <= 0:
    busqueda = int(input('dime un numero a buscar valido ? '))
    pass
else :
    if busqueda in listaNumeros:
        print(f'el numero {busqueda} SI esta en la lista')
        indice = listaNumeros.index(busqueda)
        print(f'esta en el indice {indice}')
        pass
    else:
        print(f'el numero {busqueda} NO esta en la lista')
        pass