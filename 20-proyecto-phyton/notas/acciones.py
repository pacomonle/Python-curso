import notas.nota as modelo

class Acciones:
    """
    acciones del modelo nota
    """
    def crear(self, usuario):
        """
        crear nota
        """
        print(f'ok {usuario[1]} vamo a crear una nueva nota...')
        titulo = input('introduce el titulo de la nota : \n')
        descripcion = input('introduce la descripcion de la nota : \n')
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f'La nota {nota.titulo} se guardo correctamente')
            pass
        else:
            print(f'algo ha salido mal, no d¡se ha podido grabar la nota {nota.titulo}')
            pass
        return True
        pass
    def mostrar(self, usuario):
        """
        mostrar notas de usuarios
        """
        print(f'{usuario[1]} este es el listado de tus notas : \n')
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        # print(notas)
        for nota in notas:
            print(f'**************** usuario: {usuario[1]} *******************')
            print(f'titulo     : {nota[2]}')
            print(f'descripcion: {nota[3]}')
            print(f'fecha      : {nota[4]}')
            pass
        else:
            print('\nesas son todas tus notas')
            pass
        pass
    def borrar(self, usuario):
        """
        eliminar nota del usuario
        """
        print(f'{usuario[1]} has elegido eliminar nota')
        titulo = input('Dime el titulo de la nota que quieres eliminar ? : ')
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f'Eliminada correctamente la nota: {nota.titulo}')
            pass
        else:
            print(f'No se ha podido eliminar la nota {titulo}')
            pass
        pass
    pass