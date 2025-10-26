class Ejemplar:
    def __init__(self, id, libro, estado="Disponible", fuente_externa=False):
        self.id = id
        self.libro = libro
        self.estado = estado # Disponible, Reservado, No Disponible
        self.fuente_externa = fuente_externa

    def __str__(self):
        tipo = "Externo" if self.fuente_externa else "Local"
        return f"Ejemplar(ID: {self.id}, Libro: {self.libro.titulo}, Estado: {self.estado}, Fuente: {tipo})"