class Multa:
    def __init__(self, id, usuario, motivo, monto_pagar, estado_pago=False):
        self.id = id
        self.usuario = usuario
        self.motivo = motivo
        self.monto_pagar = monto_pagar
        self.pagada = estado_pago  # True o False
    
    def es_pagada(self):
        return self.pagada
    
    def __str__(self):
        return f"Multa(ID: {self.id}, Usuario: {self.usuario.id}, Motivo: {self.motivo}, Monto a Pagar: {self.monto_pagar}, Pagada: {self.pagada})"