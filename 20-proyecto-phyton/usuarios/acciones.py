import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    """
    acciones del modelo usuario
    """
    def registro(self):
        """
        registro usuario
        """
        print('\nok!!! Vamos a registrate en el sistema...')
        nombre = input('Cual es tu nombre ?: ').strip()
        apellidos = input('Cuales son tus apellidos ?: ').strip()
        email = input('Cual es tu email ?:' ).strip()
        password = input('Cual es tu password ?: ').strip()

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1 :
            print(f'{registro[1].nombre} tu nickname de usuario es {registro[1].email}')
            pass
        else:
            print('No te has registrado correctamente', registro[0], registro[1].nombre)
            pass
        pass

    def login(self):
        """
        login usuario
        """
        try:
            print('\nok!!! Identificate en el sistema...')
            email = input('Cual es tu email ?:' ).strip()
            password = input('Cual es tu password ?: ').strip()
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            # print(login)
            if email == login[3]:
                print(f'Hola {login[1]}, te registraste el {login[5]}')
                self.proximasAcciones(login)
                pass
            else:
                print('Email o Contraseña Incorrectos')
                pass
            pass
        except Exception as error:
            # print(type(error))
            # print(type(error).__name__)
            print('Login Incorrecto, intentalo mas tarde')
            pass
        pass
    def proximasAcciones(self, usuario):
        """
        menu proximos pasos
        """
        # print(f'Hola {usuario[1]}')
        print("""
        Acciones disponibles :
        1. Crear nota (crear)
        2. Listar notas (mostrar)
        3. Eliminar nota (eliminar)
        4. Salir (salir)
        """)
        accion = input('Que quieres hacer ? : ')
        todo = notas.acciones.Acciones()
        if accion == 'crear':
            print('----------- Crear nota ----------')
            todo.crear(usuario)
            self.proximasAcciones(usuario)
            pass
        elif accion == 'mostrar':
            print('----------- Listar notas ----------')
            todo.mostrar(usuario)
            self.proximasAcciones(usuario)
            pass
        elif accion == 'eliminar':
            print('----------- Eliminar nota ----------')
            todo.borrar(usuario)
            self.proximasAcciones(usuario)
            pass
        elif accion == 'salir':
            print(f'hata pronto {usuario[1]}...')
            exit()
            pass
        else:
            print('opcion no valida')
            self.proximasAcciones(usuario)
            pass
        return None
        pass    
    pass

