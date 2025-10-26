class Reserva:
    def __init__(self, id, prestamo, ejemplar, condicion):
        self.id = id
        self.prestamo = prestamo
        self.ejemplar = ejemplar
        self.condicion = condicion # pendiente, activa, completada o cancelada
    
    def cond_activa(self):
        return self.condicion.lower() == "activa"

    def __str__(self):
        return f"Reserva(ID: {self.id}, Préstamo: {self.prestamo.id}, Ejemplar: {self.ejemplar.id} - {self.ejemplar.libro.titulo}, Condición: {self.condicion})"