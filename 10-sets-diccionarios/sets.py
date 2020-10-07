"""
SET - coleccion de valores, sin indice ni orden
"""

personas = {
    "Victor",
    "Manuel",
    "Jesus",
    "Alberto"
}

print(personas)
print(type(personas))

personas.add('Julio')
personas.remove('Manuel')
print(personas)