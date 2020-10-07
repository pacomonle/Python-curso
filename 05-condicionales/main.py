"""
CONDICIONALES
if condicion :
  instrucciones
else :
  instrucciones
"""

# Ejemplo 1 
print('############## Ejemplo1 ################')
# color = input('tu color favorito?')
color = 'verde'
if color == 'rojo':
    print('El color es ROJO')
else :
    print('El color NO es ROJO')

"""
OPERADRO COMPARACION
== igual
!= diferente
< menor que
<= menor igual
> mayor que
>= mayor igual

"""

# Ejemplo 2
print('\n############## Ejemplo2 ################')

# year = inti(nput('dime un año?'))
year = 2020

if year >= 2020 :
    print('El año es 2021 o superior')
else :
    print('El año es 2020 o inferior')


# Ejemplo 3
print('\n############## Ejemplo3 ################')

nombre = 'Francisco Monleon'
ciudad = 'Valencia'
continente = 'Europa'
edad = 50
mayorDeEdad = 18

if edad >= mayorDeEdad : 
    print(f'si tienes {edad} años eres mayor de edad')
    if continente != 'Europa' :
        print(f'{nombre} no es europeo')
    else :
         print(f'{nombre}  es europeo y vive en {ciudad}')
else :
    print(f'{nombre} no es mayor de edad')


 # Ejemplo 4
print('\n############## Ejemplo4 ################')   

dia = 7

if dia == 1 :
    print('Lunes')
elif dia == 2 :
    print('Martes')
elif dia == 3 :
    print('Miercoles')
elif dia == 4 :
    print('Jueves')
elif dia == 5 :
    print('Viernes')
elif dia == 6 :
    print('Sabado')
else :
    print('Domingo')


"""
OPERADRO LOGICOS
and -> y
or -> o
! -> negación
NOT -> no
"""

 # Ejemplo 5
print('\n############## Ejemplo5 ################')   

edad_minima = 18 
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65 : 
    print('Estas en edad de trabajar!!!')
else : 
    print('No estas en edad de trabajar')

   # Ejemplo 6
print('\n############## Ejemplo6 ################')   

pais = 'Alemania'

if pais == 'España' or pais == 'Colombia' or pais == 'Mexico' :
    print(f'{pais} es de habla hispana')
else :
    print(f'{pais} NO es de habla hispana')

 # Ejemplo 7
print('\n############## Ejemplo7 ################')   

pais = 'Rusia'

if not (pais == 'España' or pais == 'Colombia' or pais == 'Mexico') :
    print(f'{pais} NO es de habla hispana')
else :
    print(f'{pais} es de habla hispana')

  # Ejemplo 7
print('\n############## Ejemplo8 ################')   

pais = 'España'

if  pais != 'España' or pais != 'Colombia' or pais != 'Mexico' :
    print(f'{pais} es de habla hispana')
else :
    print(f'{pais} NO es de habla hispana')  