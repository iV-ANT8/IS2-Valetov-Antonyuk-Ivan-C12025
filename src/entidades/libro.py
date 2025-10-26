class Libro:
    def __init__(self, id, titulo, autor, categoria, disponibilidad=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponibilidad = disponibilidad
    
    def __str__(self):
        return f"Libro(ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, Disponible: {self.disponibilidad})"