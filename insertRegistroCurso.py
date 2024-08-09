import mysql.connector
from mysql.connector import Error


def update_record():
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

            # Consulta SQL para actualizar el registro
            update_query = """
            UPDATE curso
            SET nombreDescriptivo = %s
            WHERE idCurso = %s
            """

            # Datos para actualizar
            data = ("Tejido", 7)

            # Ejecutar la consulta de actualización
            cursor.execute(update_query, data)
            connection.commit()
            print('Registro actualizado con éxito')

    except Error as e:
        print(f'Error al conectar a MySQL o al actualizar datos: {e}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Conexión cerrada')


if __name__ == '__main__':
    update_record()
