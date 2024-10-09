# models/transaccion.py
class Transaccion:
    def __init__(self, id_transaccion, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        self._id_transaccion = id_transaccion
        self._id_usuario = id_usuario
        self._id_accion = id_accion
        self._fecha = fecha
        self._tipo = tipo
        self._cantidad = cantidad
        self._precio = precio
        self._comision = comision

    # Métodos para acceder a los atributos privados
    def get_id_transaccion(self):
        return self._id_transaccion

    def get_id_usuario(self):
        return self._id_usuario

    def get_id_accion(self):
        return self._id_accion

    def get_fecha(self):
        return self._fecha

    def get_tipo(self):
        return self._tipo

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def get_comision(self):
        return self._comision

    # Métodos para modificar los atributos privados
    def set_id_transaccion(self, id_transaccion):
        self._id_transaccion = id_transaccion

    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    def set_id_accion(self, id_accion):
        self._id_accion = id_accion

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def set_comision(self, comision):
        self._comision = comision
