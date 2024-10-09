# models/accion.py
class Accion:
    def __init__(self, id_accion, simbolo, nombre_empresa):
        self._id_accion = id_accion
        self._simbolo = simbolo
        self._nombre_empresa = nombre_empresa

    # Métodos para acceder a los atributos privados
    def get_id_accion(self):
        return self._id_accion

    def get_simbolo(self):
        return self._simbolo

    def get_nombre_empresa(self):
        return self._nombre_empresa

    # Métodos para modificar los atributos privados
    def set_id_accion(self, id_accion):
        self._id_accion = id_accion

    def set_simbolo(self, simbolo):
        self._simbolo = simbolo

    def set_nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa
