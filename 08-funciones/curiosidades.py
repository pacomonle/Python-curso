"""
CURIOSIDADES
recomendacion buena practica:
Las funciones se colocan en la parte superior del fichero
recomendable que las funciones devuelvan un dato -> return
"""
def mi_funcion_uno(nombre):
    """
    mi funcion
    """
    return 'hola ' + nombre + ' desde mi funcion'
    pass

def mi_funcion_dos(apellidos):
    """
    mi funcion
    """
    return 'hola ' + apellidos + ' desde mi otra funcion'
    pass

# nombre = 'Noel'
# apellidos = 'Monleon'
# print(f'Bienvenido {nombre} {apellidos}')
print (mi_funcion_uno('Noel'))
print (mi_funcion_dos('Monleon'))