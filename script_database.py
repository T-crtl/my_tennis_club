import pandas as pd
import mysql.connector

# Cargar archivo CSV con pandas
data = pd.read_csv('./database.csv')

# Conectarse a MySQL
conexion = mysql.connector.connect(
    host='localhost',
    user='nombreusuario',
    password='pass',
    database='sae9empre01'
)

# Insertar datos en MySQL
cursor = conexion.cursor()
for i, row in data.iterrows():
    sql = "INSERT INTO members_products (`Clave`, `Descripcion`, `Linea`, `existencias`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))
    conexion.commit()

cursor.close()
conexion.close()
