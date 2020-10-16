"""
FILTROS 
PERSONALIZADOS
"""
from django import template

register = template.Library()

# usar decorador par anombrar al filtro
@register.filter(name='saludo')
def saludo(value):
    """
    funcion filtro saludo
    """
    largo = ''
    if len(value) >= 8:
        largo = value[0:7] + '...' + ' ' + ' tu nombre es muy largo. '
        pass
    else:
        largo = value + ' ' + ' este es tu nombre completo. '
        pass
    return f"<h1 style='background:green;color:white;'>Bienvenido {largo.upper()} !!!</h1>"
    pass