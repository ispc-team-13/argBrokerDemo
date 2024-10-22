
import mysql.connector
import configparser

def connect_db():
    # Crear un objeto de configuración
    config = configparser.ConfigParser()
    
    # Leer el archivo de configuración
    config.read('config.ini')
    
    # Obtener la configuración de la base de datos
    db_config = config['database']
    
    return mysql.connector.connect(
        host=db_config['host'],
        port=int(db_config['port']),  # Convertir el puerto a entero
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
