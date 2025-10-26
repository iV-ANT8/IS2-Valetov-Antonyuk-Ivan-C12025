class Usuario:
    def __init__(self, id, nombre, edad, email, tipo_usuario="regular"):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.tipo_usuario = tipo_usuario # Regular o socio
        self.pedir_prestamos = []
    
    def registrarse(self):
        self.tipo_usuario = "socio"
        print(f"Usuario {self.nombre} registrado con éxito.")
        return True

    def __str__(self):
        return f"Usuario(ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo_usuario})"