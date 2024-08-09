import mysql.connector
from mysql.connector import Error


def connect_to_database():
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
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM 	asignatura')  # Cambia esto por tu consulta

            # Obtener los resultados
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except Error as e:
        print(f'Error al conectar a MySQL: {e}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Conexión cerrada')


if __name__ == '__main__':
    connect_to_database()
