"""
POO o OOP
programacion orientacion objetos
"""

# CLASES - molde para crear mas objetos #
class Coche:
    """
    definir las propiedaes o atributod de la class
    """
    # atributos o propiedades
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 280
    caballaje = 300
    plazas = 2
    # metodos o funciones
    def setColor(self, color):
        """
        cambiar color del coche
        """
        self.color = color
        pass
    def getColor(self):
        """
        color del coche
        """
        return self.color
        pass
    def setModelo(self, modelo):
        """
        cambiar modelo del coche
        """
        self.modelo = modelo
        pass
    def getModelo(self):
        """
        modelo coche
        """
        return self.modelo
        pass
    def setVelocidad(self, velocidad):
        """
        cambiar la velocidad
        """
        self.velocidad = self.velocidad + velocidad
        pass   
    def getVelocidad(self):
        """
        velocidad del coche
        """
        return self.velocidad
        pass
    pass
# fin clase #

# Instanciar la class #
coche = Coche()

print(coche.caballaje, coche.marca)

coche.setColor('azul')
print(coche.getColor())

coche.setVelocidad(-5)
print(coche.getVelocidad())

# crear multiples objetos #
coche2 = Coche()

coche2.setColor('Amarillo')
coche2.setModelo('Murcielago')
print(coche2.getModelo(), coche2.getColor())
print(coche.getModelo(), coche.getColor())

print(type(coche2))