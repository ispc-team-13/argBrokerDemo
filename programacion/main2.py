from dao.usuario_dao import UsuarioDAO
from dao.portafolio_dao import PortafolioDAO
from dao.accion_dao import AccionDAO
def main():
    
    def mostrar_acciones():
        accion_dao = AccionDAO()
        accion_dao.mostrar_acciones()

    def realizar_transaccion(user_id):
        accion_dao = AccionDAO()
        accion_dao.realizar_transaccion(user_id)

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
            (f"Ganancia/Pérdida: {item['Ganancia_Perdida']}")
            print("-" * 50)
            
    usuario_dao = UsuarioDAO()  # Create an instance of UsuarioDAO

    while True:
        print("\nBienvenido a ARGBrokerDemo")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Recuperar contraseña")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            user = usuario_dao.login()  # Call the login method
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
                        realizar_transaccion(user[0])
                    elif opcion == '4':
                        mostrar_portafolio(user[0])
                    elif opcion == '5':
                        print("Has cerrado sesión.")
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")

        elif opcion == '2':
            usuario_dao.registrar_usuario()  # Call the registrar_usuario method

        elif opcion == '3':
            usuario_dao.recuperar_contrasena()  # Call the recuperar_contrasena method

        elif opcion == '4':
            print("Gracias por usar ARGBrokerDemo. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
