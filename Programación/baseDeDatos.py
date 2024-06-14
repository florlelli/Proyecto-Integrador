import mysql.connector

HOST = "localhost"
USER = "root" #su usuario
PASSWORD = " " # su contraseña
BD = "ventas_satisfacción"

conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

cursor = conn.cursor()

def cerrarConexion():
    cursor.close()
    conn.close()