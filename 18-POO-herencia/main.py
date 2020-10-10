"""
HERENCIA
- capacidad de compartir atributos y metodos entre clases
- entre padres e hijos
"""
from clases import Persona, Informatico, TecnicoRedes

persona = Persona()
persona.setNombre('Francisco')
persona.setApellidos('Monleon')
persona.setAltura(1.80)
persona.setEdad(50)
print('------------ Persona -------------')
print(f'nombre: {persona.getNombre()}')
print(f'apellidos: {persona.getApellidos()}')
print(f'altura: {persona.getAltura()} cm')
print(f'edad: {persona.getEdad()} años')
print(persona.caminar())

informatico = Informatico()
informatico.setNombre('Noel')
informatico.setApellidos('Monleon')
informatico.setAltura(1.80)
informatico.setEdad(18)
print('------------ Informatico -------------')
print(informatico.getExperiencia(),'años - ' , informatico.getLenguajes())
print(f'nombre: {informatico.getNombre()}')
print(f'apellidos: {informatico.getApellidos()}')
print(f'altura: {informatico.getAltura()} cm')
print(f'edad: {informatico.getEdad()} años')
print(informatico.caminar())

informatico.setExperiencia(-1)
print(informatico.getExperiencia(), 'años -', informatico.aprenderLenguajes('mySQL'))

print('---------- tecnico redes -------------')

tecnico = TecnicoRedes()
tecnico.setExperiencia(18)
print(tecnico.getExperiencia(), ' años - ', tecnico.experienciaRedes, ' años')
