class Notificacion:
    def __init__(self, id, usuario, mensaje):
        self.id = id
        self.usuario = usuario
        self.mensaje = mensaje
    
    def __str__(self):
        return f"Notificación(ID: {self.id}, Usuario: {self.usuario.id}, Fecha: {self.prestamo.fecha_devolucion}, Mensaje: {self.mensaje})"