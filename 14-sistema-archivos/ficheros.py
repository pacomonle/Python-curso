"""
ARCHIVOS EN Python
uso de archivos en python -> utilizar modulo open dentro del paquete io
"""

from io import open
# libreria para rutas absolutas -> pathlib
import pathlib
# para copiar mover o renombrar archivos 
import shutil
# para eliminar/rename archivos
import os
# para comprobar si un archivo existe
import os.path


# Abrir archivos #
# permiso a+
# ruta relativa 
archivo = open('14-sistema-archivos/fichero_texto.txt', 'a+') 
# ruta absoluta
ruta = str(pathlib.Path().absolute()) + '/14-sistema-archivos/fichero2_texto.txt'
print(ruta)
archivo2 = open(ruta, 'a+')

# Escribir archivos #
"""
archivo.write('###### soy un texto desde Python ########\n')
archivo2.write('### Texto desde Pyhton ###')
"""
# Cerrar archivos #
archivo.close()
archivo2.close()

# Leer atchivos #
# permiso r
ruta = str(pathlib.Path().absolute()) + '/14-sistema-archivos/fichero_texto.txt'
archivo_lectura = open(ruta, 'r')
"""
 contenido = archivo_lectura.read()
 print(contenido)
"""
# Leer contenido y guardarlo en lista
# lista = archivo_lectura.readline() -> guarda una linea en concreto y se pone el plural lee todos el documento
lista = archivo_lectura.readlines()

archivo_lectura.close()

print(lista)
for elemento in lista:
    lista_elemento = elemento.split()
    if not elemento.isnumeric() :
        print(f' -  { elemento.capitalize() }')
        pass
    print(lista_elemento)
    pass


# Copiar
"""
rutaOrigen = str(pathlib.Path().absolute()) + '/14-sistema-archivos/fichero_texto.txt'
rutaDestino = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos/ficheroCopiado_texto.txt'
# rutaAlternativa = './13-paquetes/fichero_copiado_texto.txt'
shutil.copyfile(rutaOrigen, rutaDestino)
"""
# Mover.
"""
rutaOrigen = str(pathlib.Path().absolute()) + '/14-sistema-archivos/fichero2_texto.txt'
# mover y renombrar
rutaDestino = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos/ficheroRename.txt'
shutil.move(rutaOrigen, rutaDestino)
"""
# Eliminar
# ruta = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos/fichero2_texto.txt'
# os.remove(ruta)
"""
# Renombrar
rutaOrigen = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos'
rutaRename = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos-carpeta'
os.rename(rutaOrigen, rutaRename)
"""
# Comprobar si un archivo existe

# print(os.path.abspath('./'))
rutaComprobar = os.path.abspath('./')+'/14-sistema-archivos/archivos-carpeta/ficheroRename.txt'
ruta_comprobar = '14-sistema-archivos/fichero_texto.txt'

if os.path.isfile(ruta_comprobar) :
    print('verdadero')
    pass
else :
    print('falso')
    pass






