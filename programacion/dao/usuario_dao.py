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

