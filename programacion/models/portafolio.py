class Portafolio:
    def __init__(self, id_portafolio, id_usuario, id_accion, cantidad, valor_comprometido, ganancia_perdida):
        self.id_portafolio = id_portafolio
        self.id_usuario = id_usuario
        self.id_accion = id_accion
        self.cantidad = cantidad
        self.valor_comprometido = valor_comprometido
        self.ganancia_perdida = ganancia_perdida

    def __repr__(self):
        return f"Portafolio(ID: {self.id_portafolio}, Usuario: {self.id_usuario}, Acción: {self.id_accion}, Cantidad: {self.cantidad}, Valor Comprometido: {self.valor_comprometido}, Ganancia/Pérdida: {self.ganancia_perdida})"
