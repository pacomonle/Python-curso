"""
FUNCIONES
1. definir funcion:
def miFuncion(parametros):
    # bloque de codigo o conjunto de instrucciones
2. invocar funcion:
miFuncion(mi_parametros

"""

# Ejemplo 1
print('########## Ejemplo 1 ##########')

def muestraNombre():
    """
    Funcion que muestra mi nombre
    """
    print('Francisco Monleon')
    pass

muestraNombre()

# Ejemplo 2
print('\n########## Ejemplo 2 ##########')

# nombre = input('dime tu nombre ? ')
# edad = int(input('dime tu edad ? '))

def muestraTuNombre(nombre, edad):
    """
     Funcion que muestra tu nombre
    """
    print(f'tu nombre es {nombre}')
    if edad >= 18 :
        print(f'eres mayor de edad, tienes {edad} años')
        pass
    else:
        print(f'eres menor de edad, tienes {edad} años')
    pass

# muestraTuNombre(nombre, edad)

muestraTuNombre('Paco', 50)

# Ejemplo 3
print('\n########## Ejemplo 3 ##########')

# numero = int(input(' de que numero quieres saber la tabla de multiplicar ? '))

def tablaMultiplicar(numero):
    print(f'tabla de multiplicar del {numero}')
    if numero <= 0 :
        numero = 1
        pass
    contador = 1
    for contador in range(1,11):
        print(f'{numero} x {contador} = {numero*contador}')
        pass
    pass

# tablaMultiplicar(numero)

for item in range(1,6):
    tablaMultiplicar(item)
    pass


# Ejemplo 4
print('\n########## Ejemplo 4 ##########')
 

def getEmpleado(nombre, id = None):
    """
    parametros opcionales
    """
    print('### Empleado ###')
    print(f'Nombre: {nombre}')
    if id != None :
        print(f'Id: {id}')
        pass
    pass

getEmpleado('Monleon', 'ABC123')

# Ejemplo 5
print('\n########## Ejemplo 5 ##########')

def calculadora(numero1 , numero2, basicas = False ):
    """
    funciones con return
    """
    print(f'Programm Calculadora de los numeros: {numero1} y {numero2}')
    suma = numero1 + numero2
    resta = numero1 - numero2
    division = numero1 / numero2
    multiplicacion = numero1 * numero2

    cadena = ''
    if basicas == True:
        cadena += "Suma:  " + str(suma) 
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        
        pass
    else: 
        cadena += "Suma:  " + str(suma) 
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
        cadena += "Multiplicacion: " + str(multiplicacion)
    return cadena
    pass
print(calculadora(4, 2, True))
print(calculadora(5, 1))

# Ejemplo 6
print('\n########## Ejemplo 6 ##########')

def getNombre(nombre):
    """
    funciones dentro de otras
    """
    texto = f'El usuario es: {nombre}'
    return texto
    pass

def getApellidos(apellido):
    """
    funciones dentro de otras
    """
    texto = f'El apellido es: {apellido}'
    return texto
    pass

def getAll(nombre, apellidos):
    """
     funciones dentro de otras
    """
    texto = getNombre(nombre) + '\n' + getApellidos(apellidos) 
    return texto
    pass

print(getAll('Francisco', 'Monleon'))

# Ejemplo 7
print('\n########## Ejemplo 7 ##########')
# funciones lambda
dime_year = lambda year : f'Estamos en el año {year}'

print(dime_year(2020))