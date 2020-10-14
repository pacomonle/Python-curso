import mysql.connector

# conexion base datos #

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'master_python'
)
 
# ¿conexion establecida? 
# print(database)

# CREAR cursor para ejecutar consultas
cursor = database.cursor(buffered=True)

# CREAR database
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# MOSTRAR databases
"""
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
    pass
"""

# CREAR tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos( 
    id int(10) auto_increment not null, 
    marca varchar(40) not null, 
    modelo varchar(40) not null, 
    precio float(10,2) not null, 
    CONSTRAINT pk_vehiculo PRIMARY KEY(id) 
    ) 
""")

# MOSTRAR tablas
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
    pass

# INSERTAR datos en la tabla

# cursor.execute("""
# INSERT INTO vehiculos 
# VALUES(null, 'Opel', 'Astra', 18500)
# """)
# database.commit()


# INSERTAR multiples datos en la tabla
coches =[
    ('Seat', 'Ibiza', 16500),
    ('Ford', 'Focus', 19700),
    ('Renault', 'Megan', 17900),
    ('Citroen', 'C-3', 15990),
]
# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
# database.commit()

# CONSULTAR datos de las tablas #
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for vehiculo in result:
    print(f'id: {vehiculo[0]}')
    print(vehiculo[1], vehiculo[2], vehiculo[3])
    pass

cursor.execute("SELECT marca, precio FROM vehiculos WHERE precio < 17000 AND marca = 'Seat' ")
result = cursor.fetchall()
for vehiculo in result:
    print(f'coche elegido: {vehiculo[0]} - {vehiculo[1]}')
    pass

cursor.execute("SELECT marca, modelo, precio FROM vehiculos")
result = cursor.fetchone()
for vehiculo in result:
    print(vehiculo)
    pass

# BORRAR registros de una tabla
# cursor.execute("DELETE FROM vehiculos WHERE id = 2")
# database.commit()
# print(cursor.rowcount, 'borrado!!!')

# ACTUALIZAR datos de la tabla
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE modelo='Ibiza' ")
database.commit()
print(cursor.rowcount, 'actualizado!!!')
