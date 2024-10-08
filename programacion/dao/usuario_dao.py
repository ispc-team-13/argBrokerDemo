import mysql.connector
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    def register(self, nombre, apellido, cuil, email, contrasena):
        query = "INSERT INTO Usuario (Nombre, Apellido, CUIL, Email, Contrasena, Saldo_Actual, Total_Invertido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (nombre, apellido, cuil, email, contrasena, 1000.0, 0.0))
        self.connection.commit()

    def login(self, email, contrasena):
        query = "SELECT * FROM Usuario WHERE Email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()

        if result:
            usuario = Usuario(result[1], result[2], result[3], result[4], result[5], result[6], result[7])  # Ajusta según tu esquema
            if usuario.verificar_contrasena(contrasena):
                return usuario
        return None

    def get_usuario_data(self, email):
        query = "SELECT Nombre, Apellido, CUIL, Email, Saldo_Actual, Total_Invertido FROM Usuario WHERE Email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
