# models/cotizacion.py
class Cotizacion:
    def __init__(self, id_cotizacion, id_accion, ultimo_operado, cantidad_compra_diaria, precio_compra_actual,
                 precio_venta_actual, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        self._id_cotizacion = id_cotizacion
        self._id_accion = id_accion
        self._ultimo_operado = ultimo_operado
        self._cantidad_compra_diaria = cantidad_compra_diaria
        self._precio_compra_actual = precio_compra_actual
        self._precio_venta_actual = precio_venta_actual
        self._cantidad_venta_diaria = cantidad_venta_diaria
        self._apertura = apertura
        self._minimo_diario = minimo_diario
        self._maximo_diario = maximo_diario
        self._ultimo_cierre = ultimo_cierre

    # Métodos para acceder a los atributos privados
    def get_id_cotizacion(self):
        return self._id_cotizacion

    def get_id_accion(self):
        return self._id_accion

    def get_ultimo_operado(self):
        return self._ultimo_operado

    def get_cantidad_compra_diaria(self):
        return self._cantidad_compra_diaria

    def get_precio_compra_actual(self):
        return self._precio_compra_actual

    def get_precio_venta_actual(self):
        return self._precio_venta_actual

    def get_cantidad_venta_diaria(self):
        return self._cantidad_venta_diaria

    def get_apertura(self):
        return self._apertura

    def get_minimo_diario(self):
        return self._minimo_diario

    def get_maximo_diario(self):
        return self._maximo_diario

    def get_ultimo_cierre(self):
        return self._ultimo_cierre

    # Métodos para modificar los atributos privados
    def set_id_cotizacion(self, id_cotizacion):
        self._id_cotizacion = id_cotizacion

    def set_id_accion(self, id_accion):
        self._id_accion = id_accion

    def set_ultimo_operado(self, ultimo_operado):
        self._ultimo_operado = ultimo_operado

    def set_cantidad_compra_diaria(self, cantidad_compra_diaria):
        self._cantidad_compra_diaria = cantidad_compra_diaria

    def set_precio_compra_actual(self, precio_compra_actual):
        self._precio_compra_actual = precio_compra_actual

    def set_precio_venta_actual(self, precio_venta_actual):
        self._precio_venta_actual = precio_venta_actual

    def set_cantidad_venta_diaria(self, cantidad_venta_diaria):
        self._cantidad_venta_diaria = cantidad_venta_diaria

    def set_apertura(self, apertura):
        self._apertura = apertura

    def set_minimo_diario(self, minimo_diario):
        self._minimo_diario = minimo_diario

    def set_maximo_diario(self, maximo_diario):
        self._maximo_diario = maximo_diario

    def set_ultimo_cierre(self, ultimo_cierre):
        self._ultimo_cierre = ultimo_cierre
