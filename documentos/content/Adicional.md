# 🧪 Pruebas con Pytest
Como contenido adicional, quiero compartir un simple ejemplo de cómo se podría usar el `pytest` para realizar pruebas sobre el flujo del modelo del sistema.

## Ejemplo en el Código

Se realiza una prueba tanto para un usuario **socio** que pide un libro externo como para un usuario **regular** que falla en el intento; levantando una excepción capturada por `pytest` y mostrando el mensaje de error correspondiente.

``` python
import pytest
...
def usuario_regular():
    return Usuario(1, "Iván", 20, "ivan@mail.com", "regular")

def usuario_socio():
    return Usuario(2, "Carla", 23, "carla@mail.com", "socio")

def libro_externo():
    return Libro(202, "Dune", "Frank Herbert", "Ciencia Ficción")

def test_prestamo_externo_falla_para_regular(usuario_regular, libro_externo):
    ejemplar = Ejemplar(11, libro_externo, "disponible", fuente_externa=True)
    with pytest.raises(ValueError, match="Solo los socios pueden solicitar ejemplares"): #Se levanta el pytest, muestra error y mensaje
        crear_prestamo(usuario_regular, ejemplar)

def test_prestamo_externo_exitoso_para_socio(usuario_socio, libro_externo):
    ejemplar = Ejemplar(12, libro_externo, "disponible", fuente_externa=True)
    prestamo = crear_prestamo(usuario_socio, ejemplar)
    assert prestamo.usuario.nombre == "Carla" #Se comprueba el nombre correcto del usuario
    assert ejemplar.estado == "prestado" #Se comprueba el estado correcto del ejemplar
```

## Resultado Esperado del Ejemplo

- El primer test falla correctamente para usuarios regulares, levantando un `ValueError`.  
- El segundo test confirma el préstamo exitoso para usuarios socios, verificando tanto el nombre del usuario como el estado del ejemplar.