class Portafolio:
    def __init__(self, id_portafolio, id_usuario, id_accion, cantidad, valor_comprometido, ganancia_perdida):
        self.__id_portafolio = id_portafolio
        self.__id_usuario = id_usuario
        self.__id_accion = id_accion
        self.__cantidad = cantidad
        self.__valor_comprometido = valor_comprometido
        self.__ganancia_perdida = ganancia_perdida
 
    # Métodos para acceder a los atributos privados
    def get_id_portafolio(self):
        return self.__id_portafolio
 
    def get_id_usuario(self):
        return self.__id_usuario
 
    def get_id_accion(self):
        return self.__id_accion
 
    def get_cantidad(self):
        return self.__cantidad
 
    def get_valor_comprometido(self):
        return self.__valor_comprometido
 
    def get_ganancia_perdida(self):
        return self.__ganancia_perdida
 
    # Métodos para modificar los atributos privados
    def set_id_portafolio(self, id_portafolio):
        self.__id_portafolio = id_portafolio
 
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
 
    def set_id_accion(self, id_accion):
        self.__id_accion = id_accion
 
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
 
    def set_valor_comprometido(self, valor_comprometido):
        self.__valor_comprometido = valor_comprometido
 
    def set_ganancia_perdida(self, ganancia_perdida):
        self.__ganancia_perdida = ganancia_perdida
 
    def __repr__(self):
        return (f"Portafolio(ID: {self.get_id_portafolio()}, "
                f"Usuario: {self.get_id_usuario()}, "
                f"Acción: {self.get_id_accion()}, "
                f"Cantidad: {self.get_cantidad()}, "
                f"Valor Comprometido: {self.get_valor_comprometido()}, "
                f"Ganancia/Pérdida: {self.get_ganancia_perdida()})")