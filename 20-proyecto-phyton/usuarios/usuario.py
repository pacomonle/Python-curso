"""
MODELO DE USUARIO
"""

import datetime
import hashlib

import usuarios.conexion as conection

connect = conection.conectar()
cursor = connect[1] 
database = connect[0] 


"""
import mysql.connector
database = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'root',
        database = 'master_python'
    )
cursor = database.cursor(buffered=True)
"""
class Usuario:
    """
    model user
    """
    # constructor
    def __init__(self, nombre, apellidos, email, password):
        """
        constructor
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        pass
    # metodos
    def registrar(self):
        """
        registrar user
        """
        fecha = datetime.datetime.now()
        # cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
            pass
        except:
            result = [0, self]  
            pass
        return result
        pass
    def identificar(self):
        """
        logear user
        """
        # consulta
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
         # cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # datos consulta
        usuario = (self.email, cifrado.hexdigest())
    
        cursor.execute(sql, usuario)
        database.commit()
        result = cursor.fetchone()
        return result
        pass
    pass

