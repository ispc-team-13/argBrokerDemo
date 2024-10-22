class Usuario:
    def __init__(self, nombre, apellido, cuil, email, contrasena, saldo_actual=1000.0, total_invertido=0.0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__email = email
        self.__contrasena = contrasena
        self.__saldo_actual = saldo_actual
        self.__total_invertido = total_invertido
 
    @property
    def nombre(self):
        return self.__nombre
 
    @property
    def apellido(self):
        return self.__apellido
 
    @property
    def cuil(self):
        return self.__cuil
 
    @property
    def email(self):
        return self.__email
 
    @property
    def saldo_actual(self):
        return self.__saldo_actual
 
    @property
    def total_invertido(self):
        return self.__total_invertido
 
    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena
 
    def actualizar_saldo(self, monto):
        self.__saldo_actual += monto
 
    def actualizar_total_invertido(self, monto):
        self.__total_invertido += monto