import mysql.connector
import pandas as pd
from mysql.connector import Error


def query_to_dataframe():
    try:
        # Establecer la conexión
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto por tu host
            database='u927419088_testing_sql',  # Cambia esto por tu nombre de base de datos
            user='u927419088_admin',  # Cambia esto por tu nombre de usuario
            password='#Admin12345#'  # Cambia esto por tu contraseña
        )

        if connection.is_connected():
            print('Conexión exitosa a la base de datos')

            # Crear un cursor para ejecutar consultas
            query = 'SELECT * FROM asignatura'  # Cambia esto por tu consulta
            df = pd.read_sql(query, connection)
            print(df)

            # Exportar a Excel
            df.to_excel('asignatura_registros.xlsx', index=False, engine='openpyxl')
            print('Datos exportados a Excel con éxito')

    except Error as e:
        print(f'Error al conectar a MySQL: {e}')

    finally:
        if connection.is_connected():
            connection.close()
            print('Conexión cerrada')


if __name__ == '__main__':
    query_to_dataframe()