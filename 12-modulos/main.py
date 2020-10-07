"""
modulos - LIBRERIAS
- modulos por defecto en phyton: en la documentacion oficial python module
- tipos de modulos: del lenguaje, por internet, creados propios
"""

# importar modulo personalizado
import mi_modulo
from mi_modulo import *
from mi_otro_modulo import getAll

print(mi_modulo.saludar('Messi'))
print(mi_modulo.calculadora(8,1))

print(saludar('Ronaldo'))

print(getAll('Paco','Monleon'))

"""
MODULO FECHAS
"""
import datetime

print(datetime.date.today())
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
# formatear fecha
fecha_personalizada = fecha_completa.strftime('%d/%m/%Y, %H:%M:%S')
print(fecha_personalizada)
print(f'\n{ datetime.datetime.now().timestamp() }')
print(f'\n{ datetime.datetime.now().time() }')

"""
MODULO MATH
"""
import math

print(f'Raiz cuadrada de 10: {math.sqrt(10)}')
print('numero Pi: ', float(math.pi))
print('redondear al alta: ', math.ceil(math.pi))
print('redondear a la baja: ', math.floor(math.pi))

"""
MODULO RANDOM
"""
import random

print('Numero aleatorio entre 5 y 25: ', random.randint(5,25))



