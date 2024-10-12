import mysql.connector
import sys
from models.usuario import Usuario
from database import connect_db  # Importa la función de conexión


class UsuarioDAO:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.connection = connect_db()

    # Función para iniciar sesión
    def login(self):
        email = input("Ingresa tu email: ")
        contrasena = input("Ingresa tu contraseña: ")

        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM Usuario WHERE Email = %s AND Contrasena = %s", (email, contrasena))
        user = cursor.fetchone()
        cursor.close()

        if user:
            print(f"Bienvenido, {user[1]} {user[2]}!")
            return user  # Retorna todos los datos del usuario
        else:
            print("Credenciales incorrectas. Inténtalo de nuevo.")
            return None

    # Función para registrar un nuevo usuario
    def registrar_usuario(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        contrasena = input("Ingresa tu contraseña: ")
        saldo_inicial = 1000.0  # Saldo inicial para nuevos usuarios

        cursor = self.connection.cursor()

        # Insertar el nuevo usuario en la base de datos
        try:
            cursor.execute(
                "INSERT INTO Usuario (Nombre, Apellido, Email, Contrasena, Saldo_Actual) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, email, contrasena, saldo_inicial)
            )
            self.connection.commit()
            print("Registro exitoso. ¡Ahora puedes iniciar sesión!")
        except mysql.connector.Error as err:
            print(f"Error al registrar el usuario: {err}")
            self.connection.rollback()
        finally:
            cursor.close()

    # Función para recuperar la contraseña
    def recuperar_contrasena(self):
        intentos = 0  # Contador de intentos

        while intentos < 3:
            email = input("Ingresa tu email para recuperar la contraseña: ")

            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT Contrasena FROM Usuario WHERE Email = %s", (email,))
            contrasena = cursor.fetchone()
            cursor.close()

            if contrasena:
                print(f"Tu contraseña es: {contrasena[0]}")
                return  # Sale de la función si se encontró la contraseña
            else:
                print("No se encontró ningún usuario con ese email.")
                intentos += 1
                if intentos < 3:
                    print(f"Intento {intentos} de 3.")

        print("Demasiados intentos fallidos. La aplicación se cerrará.")
        sys.exit()  # Cierra la aplicación

    def get_usuario_data(self, email):
        """Obtiene los datos de un usuario por su email."""
        query = "SELECT Nombre, Apellido, CUIL, Email, Saldo_Actual, Total_Invertido FROM Usuario WHERE Email = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        cursor.close()
        return user_data

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection.is_connected():
            self.connection.close()
