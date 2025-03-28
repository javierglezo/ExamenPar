import time

def servidor(cola_recepcion, cola_procesamiento):
    print("Servidor iniciado y listo para recibir imágenes...")
    while True:
        if not cola_recepcion.empty():
            imagen = cola_recepcion.get()
            cola_procesamiento.put(imagen)
            print(f" Servidor -> Imagen {imagen['id']} enviada a procesamiento")
        else:
            time.sleep(0.2)  # Espera pasiva para no consumir CPU innecesariamente
