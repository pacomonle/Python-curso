"""
LISTAS (arrays)
- para acceder a elllas mediante un indice numerico
- el primer indice es el 0
"""
# definir lista
peliculas = ['gran torino', 'alcatraz', 'harry el sucio']
print(peliculas)
print(peliculas[0])

heroes = list(('batman', 'superman', 'spiderman')) # esto es igual que una tuple 
print(heroes)
print(heroes[0])

years = list(range(1,5))
print(years)
print(years[0])

variada = ['texto', 'frase', 1, 2]
print(variada)
print(variada[1])
print(variada[2])

# indices
print(peliculas[2])
 # indices negativos se empieza a contar desde el final como -1
print(peliculas[-2])
 # sublistas
print(heroes[1:3])
print(variada[1:])

peliculas[1]= 'Mula'
print(peliculas)

# añadir elementos a una lista
heroes.append('Ironman')
print(heroes)

# Recorres listas
nueva_pelicula = 'y'
print('############# Lista Peliculas ##############')
while nueva_pelicula != 'n':
    pelicula = input('añade una pelicula...')
    peliculas.append(pelicula)
    for pelicula in peliculas:
        print(f'{peliculas.index(pelicula)+1}. {pelicula}')
        pass
    
    nueva_pelicula = input(' quieres añadir otra y/n?')
       

else:
    print('stop')
    pass

# listas multidimensionales
print('############# Listados de Contactos ##############')
contactos = [
    [
        'antonio', 'antonio@antonio.com'  
    ],
    [
        'miguel', 'miguel@miguel.com'
    ],
    [
        'luis', 'luis@luis.com'
    ]
]

# print(contactos[0][1])
for contacto in contactos:
    print(contactos.index(contacto+1))
    len(contacto)
    for item in contacto:
        print(f'{contacto.index(item+1)} - {item}')
        pass
    pass
