"""
Proyecto Python y MySQL:
- Asistente Login o Registro
- Registro - crea un usuario nuevo en la base de datos
- login - identifica al usuario con uno de la base de datos
- Crear nota, Listar notas, Eliminar nota o Salir
"""
from usuarios import acciones

print("""
    Acciones disponibnles: 
        - registro
        - login
""")

ejecuta = acciones.Acciones()
accion = input('Que quieres hacer ?: ')
if accion == 'registro':
    ejecuta.registro()
    pass
elif accion == 'login':
    ejecuta.login()
    pass