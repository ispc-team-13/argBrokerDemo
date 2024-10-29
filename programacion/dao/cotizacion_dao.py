import mysql.connector
from models.cotizacion import Cotizacion
from colorama import Fore, Style, init

class CotizacionDAO:
    def __init__(self, db_config):
        """Inicializa el DAO con la configuración de la base de datos."""
        self.connection = mysql.connector.connect(**db_config)

    def create_cotizacion(self, id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                          precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        """Crea una nueva cotización en la base de datos."""
        sql = """INSERT INTO Cotizacion (ID_Accion, Ultimo_Operado, Cantidad_Compra_Diaria, Precio_Compra_Actual,
                 Precio_Venta_Actual, Cantidad_Venta_Diaria, Apertura, Minimo_Diario, Maximo_Diario, Ultimo_Cierre)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, (id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                                     precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre))
                self.connection.commit()
            except mysql.connector.Error as err:
                print(Fore.RED + f"\nError al crear la cotización: {err}" + Style.RESET_ALL)


    def get_cotizacion(self, id_cotizacion):
        """Obtiene una cotización por su ID."""
        sql = """SELECT * FROM Cotizacion WHERE ID_Cotizacion = %s"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (id_cotizacion,))
            result = cursor.fetchone()

        if result:
            return Cotizacion(*result)
        return None

    def update_cotizacion(self, id_cotizacion, id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                          precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        """Actualiza una cotización existente en la base de datos."""
        sql = """UPDATE Cotizacion SET ID_Accion = %s, Ultimo_Operado = %s, Cantidad_Compra_Diaria = %s,
                 Precio_Compra_Actual = %s, Precio_Venta_Actual = %s, Cantidad_Venta_Diaria = %s, Apertura = %s,
                 Minimo_Diario = %s, Maximo_Diario = %s, Ultimo_Cierre = %s WHERE ID_Cotizacion = %s"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, (id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                                     precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre, id_cotizacion))
                self.connection.commit()
            except mysql.connector.Error as err:
                print(Fore.RED + f"\nError al actualizar la cotización: {err}" + Style.RESET_ALL)


    def delete_cotizacion(self, id_cotizacion):
        """Elimina una cotización de la base de datos."""
        sql = """DELETE FROM Cotizacion WHERE ID_Cotizacion = %s"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, (id_cotizacion,))
                self.connection.commit()
            except mysql.connector.Error as err:
                print(Fore.RED + f"\nError al eliminar la cotización: {err}" + Style.RESET_ALL)

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection.is_connected():
            self.connection.close()
