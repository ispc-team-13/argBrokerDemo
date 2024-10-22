# models/accion.py
class Accion:
    def __init__(self, id_accion, simbolo, nombre_empresa):
        self.__id_accion = id_accion
        self.__simbolo = simbolo
        self.__nombre_empresa = nombre_empresa
 
    # Métodos para acceder a los atributos privados
    def get_id_accion(self):
        return self.__id_accion
 
    def get_simbolo(self):
        return self.__simbolo
 
    def get_nombre_empresa(self):
        return self.__nombre_empresa
 
    # Métodos para modificar los atributos privados
    def set_id_accion(self, id_accion):
        self.__id_accion = id_accion
 
    def set_simbolo(self, simbolo):
        self.__simbolo = simbolo
 
    def set_nombre_empresa(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa