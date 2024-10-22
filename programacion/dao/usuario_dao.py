import mysql.connector
import sys
from models.usuario import Usuario
from database import connect_db  # Importa la función de conexión
from colorama import Fore, Style, init
 
class UsuarioDAO:
    def __init__(self):
        """Inicializa la conexión a la base de datos."""
        self.connection = connect_db()
 
    # Función para iniciar sesión con un límite de 3 intentos
    def login(self):
        intentos = 0  # Contador de intentos
 
        while intentos < 3:
            email = input("Ingresa tu email: ")
            contrasena = input("Ingresa tu contraseña: ")
 
            try:
                cursor = self.connection.cursor()
                cursor.execute(
                    "SELECT * FROM Usuario WHERE Email = %s AND Contrasena = %s", (email, contrasena))
                user = cursor.fetchone()
                cursor.close()
 
                if user:
                    print(Fore.GREEN + f"\nBienvenido, {user[1]} {user[2]}!" + Style.RESET_ALL)
                    return user  # Retorna todos los datos del usuario si el login es exitoso
                else:
                    print(Fore.RED + "\nCredenciales incorrectas. Inténtalo de nuevo." + Style.RESET_ALL)
                    intentos += 1
                    print(Fore.RED + f"\nIntento {intentos} de 3." + Style.RESET_ALL)
 
            except mysql.connector.Error as err:
                print(Fore.RED + f"\nError de conexión a la base de datos: {err}" + Style.RESET_ALL)
                return None  # En caso de error, retorna None
 
        # Si se alcanzan 3 intentos fallidos, se cierra la aplicación
        print(Fore.RED + "\nDemasiados intentos fallidos. La aplicación se cerrará." + Style.RESET_ALL)
        sys.exit()  # Cierra la aplicación
        
    
    # Función para registrar un nuevo usuario
    def registrar_usuario(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        cuil= input("Ingresa tu cuil: ")
        email = input("Ingresa tu email: ")
        contrasena = input("Ingresa tu contraseña: ")
        saldo_inicial = 10000.0  # Saldo inicial para nuevos usuarios
 
        cursor = self.connection.cursor()
 
        # Insertar el nuevo usuario en la base de datos
        try:
            cursor.execute(
                "INSERT INTO Usuario (Nombre, Apellido, cuil, Email, Contrasena, Saldo_Actual) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido,cuil, email, contrasena, saldo_inicial)
            )
            self.connection.commit()
            print(Fore.YELLOW + f"\nRegistro exitoso. ¡Ahora puedes iniciar sesión!" + Style.RESET_ALL)
 
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al registrar el usuario: {err}" + Style.RESET_ALL)
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
                print(Fore.RED + f"\nNo se encontró ningún usuario con ese email." + Style.RESET_ALL)
 
                intentos += 1
                if intentos < 3:
                    print(Fore.RED + f"\nIntento {intentos} de 3." + Style.RESET_ALL)
 
        print(Fore.RED + f"\nDemasiados intentos fallidos. La aplicación se cerrará." + Style.RESET_ALL)
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
    