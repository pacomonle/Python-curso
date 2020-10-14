"""
MODELO DE NOTA
"""
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    """
    modelo de la tabla nota
    """
    # Constructor
    def __init__(self, usuario_id, titulo = '', descripcion = ''):
        """
        constructor de nota
        """
        self.usuario_id =usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        pass
    # Metodos
    def guardar(self):
        """
        guardar en base de datos
        """
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
        pass
    def listar(self):
        """
        listar notas de un usuario base de datos
        """
        # print(self.usuario_id)
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sql)
        # database.commit()
        result = cursor.fetchall()
        # print(result)
        return result
        pass
    def eliminar(self):
        """
        borrar nota del usuario de la bas de datos
        """
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
        pass

    pass
