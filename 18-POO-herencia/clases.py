"""
HERENCIA
- capacidad de compartir atributos y metodos entre clases
- entre padres e hijos
"""

class Persona :
    """ nombre
    apellidos
    altura
    edad """
    # getters
    def getNombre(self):
        """
        get
        """
        return self.nombre
        pass
    def getApellidos(self):
        """
        get
        """
        return self.apellidos
        pass
    def getAltura(self):
        """
        get
        """
        return self.altura
        pass
    def getEdad(self):
        """
        get
        """
        return self.edad
        pass
    # setters
    def setNombre(self, nombre):
        """
        set
        """
        self.nombre = nombre
        pass
    def setApellidos(self, apellidos):
        """
        set
        """
        self.apellidos = apellidos
        pass
    def setAltura(self, altura):
        """
        set
        """
        self.altura = altura
        pass
    def setEdad(self, edad):
        """
        set
        """
        self.edad = edad
        pass
    # metodos
    def caminar(self):
        """
        metodo
        """
        return 'Estoy caminando'
        pass
    def hablar(self):
        """
        metodo
        """
        return 'Estoy hablando'
        pass
    pass
# fin class #

############# HERENCIA ##############
class Informatico(Persona):
    """
    herencia
    """
    def __init__(self):
        """
        constructor:
        - lenguajes
        - Experiencia
        """
        self.lenguajes = ['Java', 'Python', 'Javascript', 'HTML', 'CSS']
        self.experiencia = 2
        pass
    # getters
    def getLenguajes(self):
        """
        getter
        """
        return self.lenguajes
        pass
    def getExperiencia(self):
        """
        getter
        """
        return self.experiencia
        pass

    # setters
    def setExperiencia(self, years):
        """
        setter
        """
        # self.experiencia = years
        self.experiencia = self.experiencia + years
        if self.experiencia < 0 :
            self.experiencia = 0
            pass 
        pass
    # metodos
    def aprenderLenguajes(self, lenguaje):
        """
        metodo
        """
        self.lenguajes.append(lenguaje)
        return self.lenguajes
        pass
    def programar(self):
        """
        metodos
        """
        return 'Soy programador web'
        pass

    pass

class TecnicoRedes(Informatico):
    """
    Herencia
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.auditor = 'esperto'
        self.experienciaRedes = 15
        pass
    def auditoria(self):
        """S
        metodo
        """
        return 'estoy auditando'
        pass
    pass
