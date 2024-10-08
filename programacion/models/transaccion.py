# models/transaccion.py
class Transaccion:
    def __init__(self, id_transaccion, id_usuario, id_accion, fecha, tipo, cantidad, precio, comision):
        self.id_transaccion = id_transaccion
        self.id_usuario = id_usuario
        self.id_accion = id_accion
        self.fecha = fecha
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision
