"""
Ejercicio 4
- script con 4 variables: lista, boleano, string y entero
- imprimir mensaje con el tipo de variable
- usar funciones
"""
def traducir(tipo):
    """
    tarducir tipo dato
    """
    miTipo = ''
    if tipo == list:
        miTipo = 'list'
        pass
    elif tipo == int:
        miTipo = 'int'
        pass
    elif tipo == str:
        miTipo = 'str'
        pass
    elif tipo == bool:
        miTipo = 'bool'
        pass
    else:
        miTipo ='tipo no valido'
        pass
    pass
    return miTipo

def testTipado(variable, tipoDato):
    """
    comprobar el tipo de dato 
    """
    test = isinstance(variable, tipoDato)
    if test:
        return (f'{variable} SI es un tipo de dato {traducir(tipoDato)}')
        pass
    else:
        return (f'{variable} NO es un tipo de dato {traducir(tipoDato)}')
        pass
    pass

def tipoVariable(variable):
    """
    definir tipo dato
    """
    return type(variable)
    pass


mi_lista = ['Hola Mundo', 7]
print(tipoVariable(mi_lista))

titulo = 'Master en Python'
print(tipoVariable(titulo))

numero = 100
print(tipoVariable(numero))

verdadero = True
print(tipoVariable(verdadero))

print(testTipado(numero, bool)) 
print(testTipado(numero, int))
print(testTipado(verdadero, bool)) 
print(testTipado(mi_lista, list))
print(testTipado(titulo, int))
print(testTipado(titulo, str))



