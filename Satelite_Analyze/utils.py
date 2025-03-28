import time
import uuid
import random

def generar_imagen(id_sat):
    return {
        "id": str(uuid.uuid4()),
        "satellite": id_sat,
        "timestamp": time.time(),
        "datos": f"imagen_data_{random.randint(100,999)}"
    }

def procesar_imagen(imagen, id_analista):
    print(f" Analista {id_analista} procesando imagen {imagen['id']}...")
    time.sleep(random.uniform(1, 3))  # Procesamiento costoso
    print(f" Analista {id_analista} terminó con imagen {imagen['id']}")
