# Sistema de Procesamiento de Imágenes Satelitales - Pseudocódigo y mejoras

Link repositorio (https://github.com/javierglezo/ExamenPar.git)
## Objetivo

Simular un centro de procesamiento digital de imágenes satelitales, donde las imágenes llegan de forma **impredecible** desde distintos "satélites" y deben ser **procesadas** por un conjunto de "analistas automáticos", sin perder ninguna imagen, incluso en situaciones de alta carga.

---

## Qué ejecutar
Ejecutar el archivo **main.py**

## Arquitectura General

El sistema está diseñado con un enfoque **server-client combinado con productores-consumidores**:

- **Productores:** representan satélites que generan imágenes constantemente.
- **Cola compartida (buffer):** almacena imágenes temporalmente en orden FIFO.
- **Consumidores (analistas):** procesan una imagen a la vez desde la cola.
- **Servidor:** Cambia las imágenes de la cola recepción a la cola procesamiento.

---

## Conceptos Clave

- `multiprocessing.Queue`: utilizada para compartir imágenes entre procesos de forma segura (thread-safe).
- `Manager().Queue()`: permite que múltiples procesos puedan acceder a una cola compartida.
- `sleep` aleatorio: simula la llegada impredecible de imágenes.
- `get(timeout=...)`: evita que los consumidores se bloqueen indefinidamente si la cola está vacía.
- Sin uso de semáforos: los `Queue` ya gestionan la sincronización interna.

---
**Cambios importantes** Si tuviese que recibir de fuera, utilizaría sockets para establecer la conexión con una ip y poder conectar las imágenes de forma real desde otros ordenadores (idea principal). Al final se va a hacer en local por lo que he decidido cambiar el formato. Al final el servidor coge los satélites de la cola de llegada y la envía a la de procesamiento **(distribuye)**.
