"""
Diccionarios
- son listas clave:valor con indices alfanumerios
"""
persona = {
'nombre' : 'Francisco',
'apellidos': 'Monleon Leal',
'edad': 50
}
print(type(persona))
print(persona)
print(persona['edad'])

# Listas con dictionary
contactos = [
    {
        'nombre' : 'Francisco',
        'apellidos': 'Monleon Leal',
        'edad': 50
    },
    {
        'nombre' : 'Luis',
        'apellidos': 'Garcia de la Torre',
        'edad': 45
    },
    {
        'nombre' : 'Miguel',
        'apellidos': 'Sanchez Llanera',
        'edad': 37
    },
    {
        'nombre' : 'Alberto',
        'apellidos': 'Ruiz Segura',
        'edad': 24
    },
]

print(contactos[2]['apellidos'])
contactos[3]['nombre'] = 'Veronica'
print(contactos[3])

for contacto in contactos:
    print(f'Nombre: {contacto["nombre"]}')
    pass