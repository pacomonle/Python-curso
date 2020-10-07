"""
Ejercicio 3
- comprobar si una variable esta vacia
- rellenarla con texto en minusculas y mostrarla con texto en mayusculas
"""
variable = ''
if len(variable.strip()) <= 0 :
    variable = input(' introduce una variable ? ')
    print(f'la variable introducida en minusculas es: {variable.lower()}')
    pass
print(f'Es es tu variable en mayusculas : {variable.upper()}')
    
    