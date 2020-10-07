"""
modulo personalizado
"""

def saludar(nombre):
    """
    mi funcion Saludar
    """
    return f'Hola {nombre} !!!'
    pass

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