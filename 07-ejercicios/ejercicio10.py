"""
Ejercicio 10
Programa que pida la nota de 10 alumnos y diga cuantos han aprobado y cuanto han suspendido
"""

aprobados = 0
for alumno in range( 1 , 11 ):
    alumno = int(input(f'la nota del alumno {alumno} es : '))
    if (alumno >= 5) :
        aprobados = aprobados + 1
        pass
    pass
supendidos = 10 - aprobados
print(f'RESULTADOS DE LOS EXAMENES : ')
print('Total alumnos presentados -> 10 ' )
print('Total alumnos aprobados -> ' + str(aprobados))
print('Total alumnos suspendidos -> ' + str(supendidos))

