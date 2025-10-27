from entidades.prestamo import Prestamo
from entidades.reserva import Reserva
from entidades.notificacion import Notificacion
from entidades.multa import Multa

# ======== FUNCIONES DE VALIDACIÓN ========

# PRESTAMOS
def crear_prestamo(usuario, ejemplar):
    # 1️⃣ Verificar disponibilidad
    if not ejemplar.estado == "disponible":
        raise ValueError(f"El ejemplar {ejemplar.id} no está disponible.")

    # 2️⃣ Si el ejemplar proviene de una fuente externa y el usuario no es socio
    if ejemplar.fuente_externa and not usuario.tipo_usuario == "socio":
        raise ValueError(f"Solo los socios pueden solicitar ejemplares de bibliotecas externas.")

    # 3️⃣ Si pasa todas las validaciones
    ejemplar.estado = "prestado"
    prestamo = Prestamo(id=1, usuario=usuario, libro=ejemplar.libro)
    prestamo.asignar_fecha_devolucion()
    print(f"Préstamo creado con éxito para {usuario.nombre}. Libro: {ejemplar.libro.titulo}")
    return prestamo

# RESERVAS
def crear_reserva(usuario, ejemplar, prestamo, biblioteca):
    # Lógica para crear una reserva
    reserva = Reserva(id=3, prestamo=prestamo, ejemplar=ejemplar, condicion="pendiente")
    reserva.cond_activa()
    print(f"Reserva creada con éxito para {usuario.nombre}. Libro: {ejemplar.libro.titulo}")
    biblioteca.otorgar_ejemplar(reserva)
    return reserva

# DEVOLUCIONES
def procesar_devolucion(prestamo, biblioteca):
    # Lógica para procesar la devolución
    if prestamo.esta_vencido(): # Si no hubo devolución a tiempo
        notificacion = Notificacion(id=7, usuario=prestamo.usuario, mensaje=f"'No ha devuelto el libro {prestamo.libro.titulo} a tiempo. Se aplicará una multa.'")
        biblioteca.enviar_notificacion(notificacion)
        multa = Multa(id=9, usuario=prestamo.usuario, monto_pagar=1500, motivo="'Retraso en la devolución del ejemplar.'")
        biblioteca.enviar_multa(multa)
    else: # Devolución a tiempo
        notificacion = Notificacion(id=8, usuario=prestamo.usuario, mensaje=f"'Gracias por devolver el libro {prestamo.libro.titulo} a tiempo.'")
        biblioteca.enviar_notificacion(notificacion)
        prestamo.marcar_devuelto()
