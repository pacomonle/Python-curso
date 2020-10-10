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
    __color = 'Rojo'
    __marca = 'Ferrari'
    __modelo = 'Aventador'
    velocidad = 280
    __caballaje = 300
    plazas = 2
    # Constructor - 1º metodo , necesario para construir un objeto
    def __init__(self, color, marca, modelo, caballaje):
        """
        Constructor
        """
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__caballaje = caballaje
        pass
    # metodos o funciones
    def setColor(self, color):
        """
        cambiar color del coche
        """
        self.__color = color
        pass
    def getColor(self):
        """
        color del coche
        """
        return self.__color
        pass
    def setMarca(self, marca):
        """
        cambiar marca
        """
        self.__marca = marca
        pass
    def getMarca(self):
        """
        marca del coche
        """
        return self.__marca
        pass
    def setModelo(self, modelo):
        """
        cambiar modelo del coche
        """
        self.__modelo = modelo
        pass
    def getModelo(self):
        """
        modelo coche
        """
        return self.__modelo
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
    def getInfo(self):
        """
        info del coche
        """
        info = '----- informacion del coche -----\n'
        info += 'color: ' + self.getColor() + '\n'
        info += 'marca: ' + self.getMarca() + '\n'
        info += 'modelo: ' + self.getModelo() + '\n'
        info += 'caballaje: ' + str(self.__caballaje) + '\n'
        info += 'velocidad: ' + str(self.getVelocidad()) + '\n'
        info += 'plazas: ' + str(self.plazas) + '\n'
        return info
        pass
    pass
# fin clase #

# visibilidad de los atributos # 
# por defecto son publicos 
# atributo privado: __<nombre atributo>