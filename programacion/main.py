import mysql.connector
from datetime import datetime
import sys  # Importamos sys para cerrar la aplicación

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

    accion_id = int(
        input("\nIngresa el ID de la acción que deseas comprar/vender: "))
    tipo = input("¿Deseas comprar o vender? (compra/venta): ").lower()
    cantidad = int(input("Ingresa la cantidad: "))

    conn = connect_db()
    cursor = conn.cursor()

    # Obtener el precio de la acción
    cursor.execute(
        "SELECT c.Ultimo_Operado FROM Cotizacion c WHERE c.ID_Accion = %s", (accion_id,))
    precio = cursor.fetchone()[0]

    comision = precio * 0.01  # Supongamos una comisión del 1%

    if tipo == 'compra':
        cursor.execute("INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (user_id, accion_id, datetime.now(), 'compra', cantidad, precio, comision))
        print("Compra realizada con éxito.")

        # Actualizar el saldo
        cursor.execute("UPDATE Usuario SET Saldo_Actual = Saldo_Actual - %s WHERE ID_Usuario = %s",
                       (precio * cantidad + comision, user_id))

    elif tipo == 'venta':
        cursor.execute("INSERT INTO Transaccion (ID_Usuario, ID_Accion, Fecha, Tipo, Cantidad, Precio, Comision) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (user_id, accion_id, datetime.now(), 'venta', cantidad, precio, comision))
        print("Venta realizada con éxito.")

        # Actualizar el saldo
        cursor.execute("UPDATE Usuario SET Saldo_Actual = Saldo_Actual + %s WHERE ID_Usuario = %s",
                       (precio * cantidad - comision, user_id))

    conn.commit()
    cursor.close()
    conn.close()

# Función para mostrar el portafolio


def mostrar_portafolio(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT p.ID_Portafolio, a.Simbolo, p.Cantidad, p.Valor_Comprometido, p.Ganancia_Perdida FROM Portafolio p JOIN Accion a ON p.ID_Accion = a.ID_Accion WHERE p.ID_Usuario = %s", (user_id,))
    portafolio = cursor.fetchall()

    print("\nTu Portafolio:")
    for item in portafolio:
        print(f"ID: {item[0]}, Símbolo: {item[1]}, Cantidad: {
              item[2]}, Valor Comprometido: {item[3]}, Ganancia/Pérdida: {item[4]}")

    cursor.close()
    conn.close()

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
