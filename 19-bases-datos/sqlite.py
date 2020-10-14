"""
sqlite
sistema base de datos ligero pre instalado en el lenguaje python
"""

# 1. importar modulo
import sqlite3

# 2. conexion
conexion = sqlite3.connect('./19-bases-datos/pruebas.db') # pasar el nombre de la data base

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
)""")

# guardar cambios
conexion.commit()

# insertar datos
# cursor.execute("INSERT INTO productos VALUES(null, 'producto 1', 'descripcion producto 1', 550 )")
# conexion.commit()


# insertar multiples registros
"""
productos = [
    ('producto 4', 'descripcion producto 4', 800 ),
    ('producto 2', 'descripcion producto 2', 200 ),
    ('producto 3', 'descripcion producto 3', 180 )
]
cursor.executemany("INSERT INTO productos VALUES(null, ?, ?, ?)", productos)
conexion.commit()
"""

# borrar registros
# cursor.execute("DELETE FROM productos")  # borrar tofa la tabla
# conexion.commit()

# actualizar datos
cursor.execute("UPDATE productos SET precio = 505 WHERE precio = 800;")
conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
   # print(producto[0])
    print(producto)
    pass

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)


# filtrar
cursor.execute("SELECT * FROM productos WHERE precio < 400;")
productos = cursor.fetchall()
for producto in productos:
   # print(producto[0])
    print(producto)
    pass

#  cerrar conexion
conexion.close()