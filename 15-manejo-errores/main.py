"""
CAPTURAR EXCEPCIONES Y MANEJAR ERRORES
en codigo
"""
nombre = input('nombre de usuario ? ')
try:
    print(len(nombre))
    if len(nombre) > 4:
        nickname = 'Tu nickname es '+ nombre
        pass
    print(nickname)
    pass
except NameError as msg:
    msg = 'el nickname debe de ser de 5 caracteres como minimo'
    print('error!!!', msg)
    pass
else:
    print('todo ok')
    pass
finally:
    print('the end')
    pass

# multiples excepciones #

try:
    numero = int(input('numero para elevarlo al cuadrado ? '))
    print('el cuadrado de '+ str(numero) + ' es: '+ str(numero+numero))
    pass
except TypeError as err:
    err = 'convierte los string a int'
    print(err)
    pass
except ValueError as err:
    err = 'no uses string, introduce un int'
    print(err)
    pass
except Exception as error:
    print(type(error))
    print('Error!!!', type(error).__name__)
    pass

# Excepciones Personalizadas #
try:
    nombre = input('introduce tu nombre ? ')
    edad = int(input('introduce tu edad ? '))
    if 17 > edad or edad > 65 :
        # excepciones personalizadas usar instruccion "raise"
        raise ValueError('La edad introducida debe de ser laboral')  
        pass
    elif len(nombre) <= 5:
        raise ValueError('el nombre debe de tener comominimo 5 caracteres')
        pass
    else:
        print(f'D.{nombre} con {edad} años estas en edad de trabajar')
        pass
        pass
except ValueError as identifier:
    print(identifier)
    pass
except Exception as error:
    print('error!!!', error)
    pass
