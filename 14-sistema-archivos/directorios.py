"""
DIRECTORIOS
- se trabaja con el modulo os
"""
import os, pathlib, shutil


# "crear carpeta
if not os.path.isdir('14-sistema-archivos/carpeta'):
    os.makedirs('14-sistema-archivos/carpeta')
    pass
else:
    print('ese folder ya exists')
    pass


# eliminar carpeta

if os.path.isdir('14-sistema-archivos/archivos/carpeta_copiada'):
    os.rmdir('14-sistema-archivos/archivos/carpeta_copiada')
    pass
else:
    print('ese folder no exists')
    pass

# copiar carpeta
rutaOrigen = str(pathlib.Path().absolute()) + '/14-sistema-archivos/carpeta'
rutaDestino = str(pathlib.Path().absolute()) + '/14-sistema-archivos/archivos/carpeta_copiada'
shutil.copytree(rutaOrigen, rutaDestino)

# listar archivos de una carpeta
print('##### Contenido de Mi Carpeta #####')
contenido = os.listdir('14-sistema-archivos/carpeta')
print(contenido)
