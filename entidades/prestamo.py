from datetime import date, timedelta

class Prestamo:
    def __init__(self, id, usuario, libro, fecha_retiro=None, fecha_devolucion=None):
        self.id = id
        self.usuario = usuario
        self.libro = libro
        self.fecha_retiro = fecha_retiro if fecha_retiro else date.today()
        self.fecha_devolucion = self.fecha_retiro + timedelta(days=30) if fecha_devolucion is None else fecha_devolucion
        self.devuelto=False

    def asignar_fecha_devolucion(self):
        self.fecha_devolucion = date.today()

    def marcar_devuelto(self):
        self.devuelto = True
        print(f"El préstamo ID {self.id} con el nombre {self.libro.titulo} ha sido marcado como devuelto.")

    def esta_vencido(self):
        return not self.devuelto and date.today() > self.fecha_devolucion

    def __str__(self):
        return f"Préstamo(ID: {self.id}, Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Retiro: {self.fecha_retiro}, Devolución: {self.fecha_devolucion})"
