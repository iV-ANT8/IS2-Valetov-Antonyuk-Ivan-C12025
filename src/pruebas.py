from datetime import date, timedelta
from entidades.usuario import Usuario
from entidades.libro import Libro
from entidades.ejemplar import Ejemplar
from entidades.biblioteca import Biblioteca
from funciones import crear_prestamo, crear_reserva, procesar_devolucion

# ======== PRUEBAS ========
# LIBROS
libro1 = Libro(101, "Cien Años de Soledad", "Gabriel García Márquez", "Novela")
libro2 = Libro(202, "1984", "George Orwell", "Distopía")
libro3 = Libro(303, "El Principito", "Antoine de Saint-Exupéry", "Fantasía")
libro4 = Libro(404, "Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")

# USUARIOS
usuario_regular = Usuario(1, "Iván", 20, "ivan@mail.com")
usuario_socio = Usuario(2, "Carla", 23, "carla@mail.com")
usuario_regular_no_socio = Usuario(3, "Luis", 30, "luis@mail.com")
usuario_regular_2 = Usuario(4, "Ana", 28, "ana@mail.com")

# EJEMPLARES
ejemplar_local = Ejemplar(10, libro1, "disponible", fuente_externa=False)
ejemplar_externo = Ejemplar(11, libro2, "disponible", fuente_externa=True)
ejemplar_externo_para_socio = Ejemplar(12, libro3, "disponible", fuente_externa=True)
ejemplar_local_no_disponible = Ejemplar(13, libro4, "no disponible", fuente_externa=False)

# BIBLIOTECA
biblioteca_local = Biblioteca(1, "Biblioteca Central", "Av. Siempre Viva 742", "www.biblioteca.com", "555-1234")

print("\nCaso 1: Socio devuelve libro a tiempo \n")
try:
    usuario_socio.registrarse() # Hacer socio al usuario

    prestamo1 = crear_prestamo(usuario_socio, ejemplar_externo)
    reserva1 = crear_reserva(usuario_socio, ejemplar_externo, prestamo1, biblioteca_local)

    prestamo1.fecha_devolucion = date.today() + timedelta(days=1)  # Simular devolución a tiempo, mañana
    procesar_devolucion(prestamo1, biblioteca_local)
except ValueError as e:
    print("❌ Error:", e)

print("\nCaso 2: Usuario regular pide libro externo \n")
try:
    crear_prestamo(usuario_regular_no_socio, ejemplar_externo_para_socio)
except ValueError as e:
    print("❌ Error:", e)

print("\nCaso 3: Usuario regular no devuelve a tiempo \n")
try:
    prestamo3 = crear_prestamo(usuario_regular, ejemplar_local)
    reserva3 = crear_reserva(usuario_regular, ejemplar_local, prestamo3, biblioteca_local)

    prestamo3.fecha_devolucion = date.today() - timedelta(days=5)  # Simular devolución tardía, hace 5 días
    procesar_devolucion(prestamo3, biblioteca_local)
except ValueError as e:
    print("❌ Error:", e)

print("\nCaso 4: Usuario regular pide libro no disponible \n")
try:
    crear_prestamo(usuario_regular_2, ejemplar_local_no_disponible)
except ValueError as e:
    print("❌ Error:", e)
