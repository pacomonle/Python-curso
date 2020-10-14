import mysql.connector

def conectar():
    """
    conectar database
    """
    database = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'root',
        database = 'master_python'
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]
    pass
    