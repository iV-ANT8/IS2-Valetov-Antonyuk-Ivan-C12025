# ⚡ Pruebas

<ins>Siguiendo el flujo del sistema, simulé 4 posibles casos en total:</ins>

1) Un Usuario se registra como socio, realiza un Préstamo y una Reserva, retira el Ejemplar de la Biblioteca y lo devuelve a tiempo sin recibir una Multa.

2) Un Usuario regular que intenta solicitar un Libro de bibliotecas externas sin ser socio

3) Un Usuario regular realiza un Préstamo y una Reserva, retira el Ejemplar de la Biblioteca pero no lo devuelve a tiempo, por lo que recibe una Multa con un monto a pagar.

4) Un Usuario regular intenta realizar un Préstamo sobre un Libro cuyo Ejemplar no está disponible

---

## ⚡ Resultados Deseados en el Código:

Los siguientes son los resultados esperados al ejecutar `pruebas.py`:

```
$ py -m pruebas

Caso 1: Socio devuelve libro a tiempo

Usuario Carla registrado con éxito.
Préstamo creado con éxito para Carla. Libro: 1984
Reserva creada con éxito para Carla. Libro: 1984
La biblioteca 'Av. Siempre Viva 742' otorga el ejemplar 1984 al usuario Carla.
Notificación enviada al usuario ID 2 Carla:
 'Gracias por devolver el libro 1984 a tiempo.'
El préstamo ID 1 con el nombre 1984 ha sido marcado como devuelto.

Caso 2: Usuario regular pide libro externo

❌ Error: Solo los socios pueden solicitar ejemplares de bibliotecas externas.

Caso 3: Usuario regular no devuelve a tiempo

Préstamo creado con éxito para Iván. Libro: Cien Años de Soledad
Reserva creada con éxito para Iván. Libro: Cien Años de Soledad
La biblioteca 'Av. Siempre Viva 742' otorga el ejemplar Cien Años de Soledad al usuario Iván.
Notificación enviada al usuario ID 1 Iván:
 'No ha devuelto el libro Cien Años de Soledad a tiempo. Se aplicará una multa.'
Multa de 1500 enviada al usuario ID 1 Iván. Motivo:
 'Retraso en la devolución del ejemplar.'

Caso 4: Usuario regular pide libro no disponible

❌ Error: El ejemplar 13 no está disponible.
```