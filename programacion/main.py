import mysql.connector
from datetime import datetime
import sys  # Importamos sys para cerrar la aplicación
from dao.portafolio_dao import PortafolioDAO

# Configuración de la conexión a la base de datos


def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='ARGBrokerDemo'
    )

# Función para iniciar sesión


def login():
    email = input("Ingresa tu email: ")
    contrasena = input("Ingresa tu contraseña: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Usuario WHERE Email = %s AND Contrasena = %s", (email, contrasena))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        print(f"Bienvenido, {user[1]} {user[2]}!")
        return user  # Retorna todos los datos del usuario
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")
        return None

# Función para registrar un nuevo usuario


def registrar_usuario():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    email = input("Ingresa tu email: ")
    contrasena = input("Ingresa tu contraseña: ")
    saldo_inicial = 1000.0  # Saldo inicial para nuevos usuarios

    conn = connect_db()
    cursor = conn.cursor()

    # Insertar el nuevo usuario en la base de datos
    try:
        cursor.execute("INSERT INTO Usuario (Nombre, Apellido, Email, Contrasena, Saldo_Actual) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, email, contrasena, saldo_inicial))
        conn.commit()
        print("Registro exitoso. ¡Ahora puedes iniciar sesión!")
    except mysql.connector.Error as err:
        print(f"Error al registrar el usuario: {err}")
    finally:
        cursor.close()
        conn.close()

# Función para recuperar la contraseña


def recuperar_contrasena():
    intentos = 0  # Contador de intentos

    while intentos < 3:
        email = input("Ingresa tu email para recuperar la contraseña: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT Contrasena FROM Usuario WHERE Email = %s", (email,))
        contrasena = cursor.fetchone()

        cursor.close()
        conn.close()

        if contrasena:
            print(f"Tu contraseña es: {contrasena[0]}")
            return  # Sale de la función si se encontró la contraseña
        else:
            print("No se encontró ningún usuario con ese email.")
            intentos += 1
            if intentos < 3:
                print(f"Intento {intentos} de 3.")

    print("Demasiados intentos fallidos. La aplicación se cerrará.")
    sys.exit()  # Cierra la aplicación

# Función para mostrar los datos de la cuenta


def mostrar_datos_cuenta(user):
    print("\nDatos de la cuenta:")
    print(f"Nombre: {user[1]}")
    print(f"Apellido: {user[2]}")
    print(f"Email: {user[3]}")
    print(f"Cuil: {user[5]}")
    print(f"Saldo inicial: {user[6]}")
    print(f"Saldo saldo actual: {user[7]}")
    print(f"Tipo de perfil: {user[8]}")

# Función para mostrar acciones y cotizaciones


def mostrar_acciones():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT a.ID_Accion, a.Simbolo, a.Nombre_Empresa, c.Ultimo_Operado FROM Accion a JOIN Cotizacion c ON a.ID_Accion = c.ID_Accion")
    acciones = cursor.fetchall()

    print("\nAcciones disponibles:")
    for accion in acciones:
        print(f"ID: {accion[0]}, Símbolo: {accion[1]}, Empresa: {
              accion[2]}, Último Operado: {accion[3]}")

    cursor.close()
    conn.close()

# Función para realizar una transacción
def realizar_transaccion(user_id):
    mostrar_acciones()

    accion_id = int(input("\nIngresa el ID de la acción que deseas comprar/vender: "))
    tipo = input("¿Deseas comprar o vender? (compra/venta): ").lower()
    cantidad = int(input("Ingresa la cantidad: "))

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Obtener el precio de la acción
        cursor.execute("SELECT c.Ultimo_Operado FROM Cotizacion c WHERE c.ID_Accion = %s", (accion_id,))
        precio = cursor.fetchone()
        cursor.fetchall()  # Limpiar cualquier resultado pendiente

        if not precio:
            print("No se encontró la acción.")
            return
        
        precio = precio[0]
        comision = float(precio) * 0.01  # Comisión del 1%

        if tipo == 'compra':
            # Verificar el saldo del usuario
            cursor.execute("SELECT Saldo_Actual FROM Usuario WHERE ID_Usuario = %s", (user_id,))
            saldo = cursor.fetchone()
            cursor.fetchall()  # Limpiar cualquier resultado pendiente

            if not saldo:
                print("Error al obtener el saldo del usuario.")
                return
            
            saldo = saldo[0]
            total_compra = float(precio * cantidad) + comision

            if saldo >= total_compra:
                cursor.execute(
                    "INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (user_id, accion_id, datetime.now(), 'compra', cantidad, precio, comision)
                )
                print("Compra realizada con éxito.")

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
                print("Saldo insuficiente para realizar la compra.")

        elif tipo == 'venta':
            # Verificar acciones disponibles en el portafolio
            cursor.execute("SELECT Cantidad FROM Portafolio WHERE ID_Usuario = %s AND ID_Accion = %s",
                           (user_id, accion_id))
            acciones_disponibles = cursor.fetchone()
            cursor.fetchall()  # Limpiar cualquier resultado pendiente

            if not acciones_disponibles or acciones_disponibles[0] < cantidad:
                print("No tienes suficientes acciones para vender.")
                return

            cursor.execute(
                "INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (user_id, accion_id, datetime.now(), 'venta', cantidad, precio, comision)
            )
            print("Venta realizada con éxito.")

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

# Función para mostrar el portafolio
def mostrar_portafolio(user_id):
    portafolio_items = PortafolioDAO.get_portafolio_by_user_id(user_id)

    print("\nTu Portafolio:")
    for item in portafolio_items:
        print(f"ID: {item['ID_Portafolio']}")
        print(f"Símbolo: {item['Simbolo']}")
        print(f"Nombre de la empresa: {item['Nombre_Empresa']}")
        print(f"Cantidad de acciones: {item['Cantidad']}")
        print(f"Precio Compra Actual: {item['Precio_Compra_Actual']}")
        print(f"Precio Venta Actual: {item['Precio_Venta_Actual']}")
        print(f"Valor Comprometido: {item['Valor_Comprometido']}")
        print(f"Ganancia/Pérdida: {item['Ganancia_Perdida']}")
        print("-" * 50)


# Función principal


def main():
    while True:
        print("\nBienvenido a ARGBrokerDemo")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Recuperar contraseña")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            user = login()
            if user:
                while True:
                    print("\nOpciones:")
                    print("1. Mostrar datos de la cuenta")
                    print("2. Mostrar acciones")
                    print("3. Realizar transacción")
                    print("4. Mostrar portafolio")
                    print("5. Cerrar sesión")
                    opcion = input("Selecciona una opción: ")

                    if opcion == '1':
                        mostrar_datos_cuenta(user)
                    elif opcion == '2':
                        mostrar_acciones()
                    elif opcion == '3':
                        # user[0] es el ID del usuario
                        realizar_transaccion(user[0])
                    elif opcion == '4':
                        # user[0] es el ID del usuario
                        mostrar_portafolio(user[0])
                    elif opcion == '5':
                        print("Has cerrado sesión.")
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

        elif opcion == '2':
            registrar_usuario()

        elif opcion == '3':
            recuperar_contrasena()

        elif opcion == '4':
            print("Gracias por usar ARGBrokerDemo. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
