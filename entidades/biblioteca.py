class Biblioteca:
    def __init__(self, id, reserva=None, nombre="", direccion="", url="", telefono=""):
        self.id = id
        self.reserva = reserva
        self.nombre = nombre
        self.direccion = direccion
        self.url = url
        self.telefono = telefono
    
    def otorgar_ejemplar(self, reserva):
        self.reserva = reserva
        print(f"La biblioteca '{self.nombre}' otorga el ejemplar {reserva.ejemplar.libro.titulo} al usuario {reserva.prestamo.usuario.nombre}.")

    def enviar_notificacion(self, notificacion):
        print(f"Notificación enviada al usuario ID {notificacion.usuario.id} {notificacion.usuario.nombre}: \n {notificacion.mensaje}")

    def enviar_multa(self, multa):
        print(f"Multa de {multa.monto_pagar} enviada al usuario ID {multa.usuario.id} {multa.usuario.nombre}. Motivo: \n {multa.motivo}")