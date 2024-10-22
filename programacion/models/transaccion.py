# models/transaccion.py
class Transaccion:
    def __init__(self, id_transaccion, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        self.__id_transaccion = id_transaccion
        self.__id_usuario = id_usuario
        self.__id_accion = id_accion
        self.__fecha = fecha
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__precio = precio
        self.__comision = comision
 
    # Métodos para acceder a los atributos privados
    def get_id_transaccion(self):
        return self.__id_transaccion
 
    def get_id_usuario(self):
        return self.__id_usuario
 
    def get_id_accion(self):
        return self.__id_accion
 
    def get_fecha(self):
        return self.__fecha
 
    def get_tipo(self):
        return self.__tipo
 
    def get_cantidad(self):
        return self.__cantidad
 
    def get_precio(self):
        return self.__precio
 
    def get_comision(self):
        return self.__comision
 
    # Métodos para modificar los atributos privados
    def set_id_transaccion(self, id_transaccion):
        self.__id_transaccion = id_transaccion
 
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
 
    def set_id_accion(self, id_accion):
        self.__id_accion = id_accion
 
    def set_fecha(self, fecha):
        self.__fecha = fecha
 
    def set_tipo(self, tipo):
        self.__tipo = tipo
 
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
 
    def set_precio(self, precio):
        self.__precio = precio
 
    def set_comision(self, comision):
        self.__comision = comision