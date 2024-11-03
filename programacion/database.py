import configparser
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        # Crear un objeto de configuración
        config = configparser.ConfigParser()
        
        # Leer el archivo de configuración
        config.read('config.ini')
        
        # Obtener la configuración de la base de datos
        db_config = config['database']
        
        # Intentar conectar a la base de datos
        connection = mysql.connector.connect(
            host=db_config['host'],
            port=int(db_config['port']),  # Convertir el puerto a entero
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        
        print("Conexión exitosa")
        return connection
    
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
