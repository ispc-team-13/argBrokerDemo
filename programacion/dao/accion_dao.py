# dao/accion_dao.py
import mysql.connector
from models.accion import Accion
from database import connect_db  # Importa la función de conexión
from datetime import datetime  # Importar datetime para la fecha de las transacciones
from colorama import Fore, Style, init
 
 
class AccionDAO:
    # Función para mostrar acciones y cotizaciones
    def mostrar_acciones(self):
        conn = connect_db()
        cursor = conn.cursor()
 
        cursor.execute(
            "SELECT a.ID_Accion, a.Simbolo, a.Nombre_Empresa, c.Ultimo_Operado "
            "FROM Accion a JOIN Cotizacion c ON a.ID_Accion = c.ID_Accion"
        )
        acciones = cursor.fetchall()
 
        print(Fore.MAGENTA + "\nAcciones disponibles:" + Style.RESET_ALL)
 
        for accion in acciones:
            print(f"ID: {accion[0]}, Símbolo: {accion[1]}, Empresa: {accion[2]}, Último Operado: {accion[3]}")
 
        cursor.close()
        conn.close()
 
    # Función para realizar una transacción
    def realizar_transaccion(self, user_id):
        self.mostrar_acciones()
 
        accion_id = int(input("\nIngresa el ID de la acción que deseas comprar/vender: "))
        tipo = input("¿Deseas comprar o vender? (compra/venta): ").lower()
        cantidad = int(input("Ingresa la cantidad: "))
 
        conn = connect_db()
        cursor = conn.cursor()
 
        try:
            # Obtener el precio de la acción
            cursor.execute("SELECT c.Ultimo_Operado FROM Cotizacion c WHERE c.ID_Accion = %s", (accion_id,))
            precio = cursor.fetchone()
 
            if not precio:
                print(Fore.RED + "\nNo se encontró la acción." + Style.RESET_ALL)
 
                return
 
            precio = precio[0]
            comision = float(precio) * 0.01  # Comisión del 1%
 
            if tipo == 'compra':
                # Verificar el saldo del usuario
                cursor.execute("SELECT Saldo_Actual FROM Usuario WHERE ID_Usuario = %s", (user_id,))
                saldo = cursor.fetchone()
 
                if not saldo:
                    print(Fore.RED + "\nError al obtener el saldo del usuario." + Style.RESET_ALL)
 
                    return
 
                saldo = saldo[0]
                total_compra = float(precio * cantidad) + comision
 
                if saldo >= total_compra:
                    cursor.execute(
                        "INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (user_id, accion_id, datetime.now(), 'compra', cantidad, precio, comision)
                    )
                    print(Fore.YELLOW + "\nCompra realizada con éxito." + Style.RESET_ALL)
 
                    # Actualizar el saldo del usuario
                    cursor.execute("UPDATE Usuario SET Saldo_Actual = Saldo_Actual - %s WHERE ID_Usuario = %s",
                                   (total_compra, user_id))
 
                    # Actualizar el portafolio del usuario
                    cursor.execute(
                        "INSERT INTO Portafolio (ID_Usuario, ID_Accion, Cantidad) VALUES (%s, %s, %s) "
                        "ON DUPLICATE KEY UPDATE Cantidad = Cantidad + %s",
                        (user_id, accion_id, cantidad, cantidad)
                    )
                else:
                    print(Fore.RED + "\nSaldo insuficiente para realizar la compra." + Style.RESET_ALL)
 
 
            elif tipo == 'venta':
                # Verificar acciones disponibles en el portafolio
                cursor.execute("SELECT Cantidad FROM Portafolio WHERE ID_Usuario = %s AND ID_Accion = %s",
                               (user_id, accion_id))
                acciones_disponibles = cursor.fetchone()
 
                if not acciones_disponibles or acciones_disponibles[0] < cantidad:
                    print(Fore.RED + "\nNo tienes suficientes acciones para vender." + Style.RESET_ALL)
 
                    return
 
                cursor.execute(
                    "INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (user_id, accion_id, datetime.now(), 'venta', cantidad, precio, comision)
                )
                print(Fore.YELLOW + "\nVenta realizada con éxito." + Style.RESET_ALL)
 
                total_venta = float(precio * cantidad) - comision
                cursor.execute("UPDATE Usuario SET Saldo_Actual = Saldo_Actual + %s WHERE ID_Usuario = %s",
                               (total_venta, user_id))
 
                # Actualizar la cantidad de acciones en el portafolio
                cursor.execute(
                    "UPDATE Portafolio SET Cantidad = Cantidad - %s WHERE ID_Usuario = %s AND ID_Accion = %s",
                    (cantidad, user_id, accion_id)
                )
 
                # Eliminar de portafolio si la cantidad es cero
                cursor.execute(
                    "DELETE FROM Portafolio WHERE ID_Usuario = %s AND ID_Accion = %s AND Cantidad <= 0",
                    (user_id, accion_id)
                )
 
            # Confirmar cambios
            conn.commit()
        except mysql.connector.Error as e:
            print("Error en la base de datos:", e)
            conn.rollback()  # Rollback en caso de error
        finally:
            cursor.close()
            conn.close()