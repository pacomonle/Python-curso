from coche import Coche

coche = Coche('Verde', 'Lamborghini', 'Gallardo', 400)

coche.setVelocidad(+50)
print(coche.getVelocidad(), 'km/h')

coche.setMarca('Ferrari')
print(coche.getMarca())

coche.precio = 500000

print(coche.getInfo(), f'{coche.precio} €')

coche2 = Coche('Morado', 'Lamborghini', 'Spider', 220)
coche2.velocidad = 200
coche2.plazas = 4

print(coche2.getInfo())

# comprobar tipado
if type(coche2) == Coche:
    print(type(coche2), 'correcto!!!')
    pass
else:
    print('No es un objeto de la class Coche')
    pass

# print(coche2.color)
