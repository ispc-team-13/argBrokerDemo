# dao/accion_dao.py
import mysql.connector
from models.accion import Accion

class AccionDAO:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)

    def create_accion(self, simbolo, nombre_empresa):
        cursor = self.connection.cursor()
        sql = """INSERT INTO Accion (Simbolo, Nombre_Empresa) VALUES (%s, %s)"""
        cursor.execute(sql, (simbolo, nombre_empresa))
        self.connection.commit()
        cursor.close()

    def get_accion(self, id_accion):
        cursor = self.connection.cursor()
        sql = """SELECT * FROM Accion WHERE ID_Accion = %s"""
        cursor.execute(sql, (id_accion,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Accion(*result)
        return None

    def update_accion(self, id_accion, simbolo, nombre_empresa):
        cursor = self.connection.cursor()
        sql = """UPDATE Accion SET Simbolo = %s, Nombre_Empresa = %s WHERE ID_Accion = %s"""
        cursor.execute(sql, (simbolo, nombre_empresa, id_accion))
        self.connection.commit()
        cursor.close()

    def delete_accion(self, id_accion):
        cursor = self.connection.cursor()
        sql = """DELETE FROM Accion WHERE ID_Accion = %s"""
        cursor.execute(sql, (id_accion,))
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
