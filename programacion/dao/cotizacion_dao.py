# dao/cotizacion_dao.py
import mysql.connector
from models.cotizacion import Cotizacion

class CotizacionDAO:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)

    def create_cotizacion(self, id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                          precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        cursor = self.connection.cursor()
        sql = """INSERT INTO Cotizacion (ID_Accion, Ultimo_Operado, Cantidad_Compra_Diaria, Precio_Compra_Actual,
                 Precio_Venta_Actual, Cantidad_Venta_Diaria, Apertura, Minimo_Diario, Maximo_Diario, Ultimo_Cierre)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                             precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre))
        self.connection.commit()
        cursor.close()

    def get_cotizacion(self, id_cotizacion):
        cursor = self.connection.cursor()
        sql = """SELECT * FROM Cotizacion WHERE ID_Cotizacion = %s"""
        cursor.execute(sql, (id_cotizacion,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Cotizacion(*result)
        return None

    def update_cotizacion(self, id_cotizacion, id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                          precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        cursor = self.connection.cursor()
        sql = """UPDATE Cotizacion SET ID_Accion = %s, Ultimo_Operado = %s, Cantidad_Compra_Diaria = %s,
                 Precio_Compra_Actual = %s, Precio_Venta_Actual = %s, Cantidad_Venta_Diaria = %s, Apertura = %s,
                 Minimo_Diario = %s, Maximo_Diario = %s, Ultimo_Cierre = %s WHERE ID_Cotizacion = %s"""
        cursor.execute(sql, (id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                             precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre, id_cotizacion))
        self.connection.commit()
        cursor.close()

    def delete_cotizacion(self, id_cotizacion):
        cursor = self.connection.cursor()
        sql = """DELETE FROM Cotizacion WHERE ID_Cotizacion = %s"""
        cursor.execute(sql, (id_cotizacion,))
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
