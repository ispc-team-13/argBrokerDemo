import mysql.connector
from models.transaccion import Transaccion
from colorama import Fore, Style, init
 
class TransaccionDAO:
    def __init__(self, db_config):
        """Inicializa la conexión a la base de datos."""
        self.connection = mysql.connector.connect(**db_config)
 
    def create_transaccion(self, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        """Crea una nueva transacción en la base de datos."""
        cursor = self.connection.cursor()
        sql = """INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        try:
            cursor.execute(sql, (id_usuario, id_accion, fecha, tipo, cantidad, precio, comision))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al crear la transacción: {err}" + Style.RESET_ALL)
 
            self.connection.rollback()
        finally:
            cursor.close()
 
    def get_transaccion(self, id_transaccion):
        """Obtiene una transacción por su ID."""
        cursor = self.connection.cursor()
        sql = """SELECT * FROM Transaccion WHERE ID_Transaccion = %s"""
        try:
            cursor.execute(sql, (id_transaccion,))
            result = cursor.fetchone()
            if result:
                return Transaccion(*result)
            return None
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al obtener la transacción: {err}" + Style.RESET_ALL)
 
            return None
        finally:
            cursor.close()
 
    def update_transaccion(self, id_transaccion, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        """Actualiza una transacción existente en la base de datos."""
        cursor = self.connection.cursor()
        sql = """UPDATE Transaccion SET ID_Usuario = %s, ID_Accion = %s, Fecha = %s, Tipo = %s,
                 Cantidad = %s, Precio = %s, Comision = %s WHERE ID_Transaccion = %s"""
        try:
            cursor.execute(sql, (id_usuario, id_accion, fecha, tipo, cantidad, precio, comision, id_transaccion))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al actualizar la transacción: {err}" + Style.RESET_ALL)
 
            self.connection.rollback()
        finally:
            cursor.close()
 
    def delete_transaccion(self, id_transaccion):
        """Elimina una transacción de la base de datos."""
        cursor = self.connection.cursor()
        sql = """DELETE FROM Transaccion WHERE ID_Transaccion = %s"""
        try:
            cursor.execute(sql, (id_transaccion,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al eliminar la transacción: {err}" + Style.RESET_ALL)
 
            self.connection.rollback()
        finally:
            cursor.close()
 
    def close(self):
        """Cierra la conexión a la base de datos."""
        self.connection.close()