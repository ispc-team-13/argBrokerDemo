# dao/transaccion_dao.py
import mysql.connector
from models.transaccion import Transaccion

class TransaccionDAO:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)

    def create_transaccion(self, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        cursor = self.connection.cursor()
        sql = """INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (id_usuario, id_accion, fecha, tipo, cantidad, precio, comision))
        self.connection.commit()
        cursor.close()

    def get_transaccion(self, id_transaccion):
        cursor = self.connection.cursor()
        sql = """SELECT * FROM Transaccion WHERE ID_Transaccion = %s"""
        cursor.execute(sql, (id_transaccion,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Transaccion(*result)
        return None

    def update_transaccion(self, id_transaccion, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        cursor = self.connection.cursor()
        sql = """UPDATE Transaccion SET ID_Usuario = %s, ID_Accion = %s, Fecha = %s, Tipo = %s,
                 Cantidad = %s, Precio = %s, Comision = %s WHERE ID_Transaccion = %s"""
        cursor.execute(sql, (id_usuario, id_accion, fecha, tipo, cantidad, precio, comision, id_transaccion))
        self.connection.commit()
        cursor.close()

    def delete_transaccion(self, id_transaccion):
        cursor = self.connection.cursor()
        sql = """DELETE FROM Transaccion WHERE ID_Transaccion = %s"""
        cursor.execute(sql, (id_transaccion,))
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
