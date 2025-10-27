# 🧬 PATRÓN DE DISEÑO: ADAPTER

## Problema del Sistema:
El problema identificado en mi sistema es la falta de integración con los posibles ejemplares que provienen de una biblioteca externa virtual, lo que podría provocar incompatibilidades e incoherencias en la lógica principal en caso de que el ejemplar externo tenga un formato distinto al manejado por el sistema.

👉 Para evitar este problema, usaría el Patrón de Diseño **ADAPTER**.

## ¿Cómo se aplicaría en este caso?
El patrón *Adapter* permite conectar 2 interfaces incompatibles, haciendo que trabajen de forma coordinada sin necesidad de modificar su código interno. En mi caso, este patrón de adaptación seleccionaría el formato usado por el ejemplar externo y lo transformaría en el formato estándar utilizado por el sistema, evitando la necesidad de modificar la estructura interna y/o la lógica de negocio cada vez que un ejemplar externo interactúe con el flujo principal.

## Resultados esperados
Luego de la aplicación del patrón, el sistema manejaría de manera uniforme tanto los ejemplares propios de la biblioteca como los ejemplares obtenidos de bibliotecas externas, manteniendo la coherencia en la capa de negocio y en la capa de API, y reduciendo el acoplamiento entre los módulos por el uso de formatos distintos dentro del sistema. 

## Ejemplo en el Código
Este sería un ejemplo dado en el contexto del sistema, utilizando el lenguaje `Python`:

```python
    ====== ADAPTER PARA FUENTES EXTERNAS ======
    # Clase de Adaptador

    class AdaptadorEjemplarExterno:
        def __init__(self, external_data):
            self.external_data = external_data

        def modelo_interno(self):
            libro = Libro(
                id=self.external_data["external_id"],
                titulo=self.external_data["book_title"],
                autor=self.external_data["book_author"],
                categoria=self.external_data["category"]
            )
            return Ejemplar(
                id=self.external_data["external_id"],
                libro=libro,
                fuente_externa=True
            )

    # Datos externos simulados

    external_data = {
        "external_id": 200,
        "book_title": "1984",
        "book_author": "George Orwell",
        "category": "Distopía"
    }

    # Adaptamos el ejemplar externo

    adapter = AdaptadorEjemplarExterno(external_data)
    ejemplar_externo = adapter.modelo_interno()
```

Definiendo la clase del adaptador, transformamos mediante un **mapeo de campos** los datos externos recibidos en datos internos conocidos y manipulables: 
- "external_id" ➡ id.
- "book_title" ➡ titulo.
- "book_author" ➡ autor.
- "category" ➡ categoría.

Posteriormente se crea una instancia del adaptador, se pasan los datos externos simulados y se llama a la función para obtener el `Ejemplar` ya adaptado y listo para usar.