"""
variables LOCALES y GLOBALES
"""

# variable global
frase = "Hoy es un buen dia para cumplir tus sueños"
print(frase)

def Hola_Mundo():
    """
    variables globales
    """
    frase = "Hola Mundo"
    print(frase)
    # variable local
    year = 2021
    print(year)
    # convertir una variable local en global
    #  global website
    website = 'nolitoxD.com'
    print(website)
    pass
Hola_Mundo()
print(frase)
