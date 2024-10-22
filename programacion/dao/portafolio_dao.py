import mysql.connector
from models.portafolio import Portafolio
from database import connect_db  # Importa la función de conexión
from colorama import Fore, Style, init
 
class PortafolioDAO:
    @staticmethod
    def get_portafolio_by_user_id(user_id):
        """Obtiene el portafolio del usuario por su ID."""
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
 
        try:
            cursor.execute("""
                SELECT p.ID_Portafolio, a.Simbolo, a.Nombre_Empresa, p.Cantidad, c.Precio_Compra_Actual, c.Precio_Venta_Actual,
                       (p.Cantidad * c.Ultimo_Operado) AS Valor_Comprometido,
                       ((p.Cantidad * c.Ultimo_Operado) - p.Valor_Comprometido) AS Ganancia_Perdida,
                       (SELECT MAX(t.Fecha) 
                        FROM Transaccion t 
                        WHERE t.ID_Usuario = p.ID_Usuario AND t.ID_Accion = p.ID_Accion) AS Fecha  -- Solo muestra la fecha más reciente
                FROM Portafolio p
                JOIN Accion a ON p.ID_Accion = a.ID_Accion
                JOIN Cotizacion c ON p.ID_Accion = c.ID_Accion
                WHERE p.ID_Usuario = %s
            """, (user_id,))
 
            # Obtener los resultados
            portafolio_items = cursor.fetchall()
        except mysql.connector.Error as err:
            print(Fore.RED + f"\nError al obtener el portafolio: {err}" + Style.RESET_ALL)
 
            portafolio_items = []
        finally:
            cursor.close()
            conn.close()
 
        return portafolio_items