from colorama import Fore, Style, init
from dao.usuario_dao import UsuarioDAO
from dao.portafolio_dao import PortafolioDAO
from dao.accion_dao import AccionDAO

# Inicializa colorama
init()


def main():

    def mostrar_acciones():
        accion_dao = AccionDAO()
        accion_dao.mostrar_acciones()

    def realizar_transaccion(user_id):
        accion_dao = AccionDAO()
        accion_dao.realizar_transaccion(user_id)

    # Función para mostrar los datos de la cuenta
    def mostrar_datos_cuenta(user):
        print(Fore.CYAN + "\nDatos de la cuenta:" + Style.RESET_ALL)
        print(f"{'Nombre:':<20} {user[1]}")
        print(f"{'Apellido:':<20} {user[2]}")
        print(f"{'Email:':<20} {user[3]}")
        print(f"{'Cuil:':<20} {user[5]}")
        print(f"{'Saldo inicial:':<20} {user[6]:.2f}")
        print(f"{'Saldo actual:':<20} {user[7]:.2f}")
        print(f"{'Tipo de perfil:':<20} {user[8]}")

    # Función para mostrar el portafolio
    def mostrar_portafolio(user_id):
        """Muestra el portafolio del usuario en la consola."""
        dao = PortafolioDAO()
        portafolio = dao.get_portafolio_by_user_id(user_id)

        if not portafolio:
            print("No se encontraron acciones en el portafolio.")
            return

        print(Fore.GREEN + "\nTu Portafolio:" + Style.RESET_ALL)
        for item in portafolio:
            print(f"ID: {item['ID_Portafolio']}")
            print(f"Símbolo: {item['Simbolo']}")
            print(f"Nombre de la empresa: {item['Nombre_Empresa']}")
            print(f"Cantidad de acciones: {item['Cantidad']}")
            print(f"Precio Compra Actual: {item['Precio_Compra_Actual']}")
            print(f"Precio Venta Actual: {item['Precio_Venta_Actual']}")
            print(f"Valor Comprometido: {item['Valor_Comprometido']}")
            (f"Ganancia/Perdida: {item['Ganancia_Perdida']}")
            print(f"Fecha de la Transacción: {item['Fecha']}")
            print("--------------------------------------------------")

    usuario_dao = UsuarioDAO()  # Create an instance of UsuarioDAO

    while True:
        print(Fore.MAGENTA + "\nBienvenido a ARGBrokerDemo" + Style.RESET_ALL)
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Recuperar contraseña")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            user = usuario_dao.login()  # Call the login method
            if user:
                while True:
                    print(Fore.BLUE + "\nOpciones:" + Style.RESET_ALL)
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
                        print(Fore.YELLOW + "Has cerrado sesión." + Style.RESET_ALL)
                        break
                    else:
                        print(
                            Fore.RED + "Opción no válida. Inténtalo de nuevo." + Style.RESET_ALL)

        elif opcion == '2':
            usuario_dao.registrar_usuario()  # Call the registrar_usuario method

        elif opcion == '3':
            usuario_dao.recuperar_contrasena()  # Call the recuperar_contrasena method

        elif opcion == '4':
            print(
                Fore.YELLOW + "Gracias por usar ARGBrokerDemo. ¡Hasta luego!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
