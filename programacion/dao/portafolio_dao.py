import mysql.connector
from models.portafolio import Portafolio

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ARGBrokerDemo'
    )

class PortafolioDAO:
    @staticmethod
    def get_portafolio_by_user_id(user_id):
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT p.ID_Portafolio, a.Simbolo, a.Nombre_Empresa, p.Cantidad, c.Precio_Compra_Actual, c.Precio_Venta_Actual, (p.Cantidad * c.Ultimo_Operado) AS Valor_Comprometido,
                   ((p.Cantidad * c.Ultimo_Operado) - p.Valor_Comprometido) AS Ganancia_Perdida
            FROM Portafolio p
            JOIN Accion a ON p.ID_Accion = a.ID_Accion
            JOIN Cotizacion c ON p.ID_Accion = c.ID_Accion
            WHERE p.ID_Usuario = %s
        """, (user_id,))
        portafolio_items = cursor.fetchall()

        cursor.close()
        conn.close()
        return portafolio_items
