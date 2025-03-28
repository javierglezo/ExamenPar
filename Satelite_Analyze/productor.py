import time
import random
from utils import generar_imagen

def productor(id_sat, cola):
    while True:
        imagen = generar_imagen(id_sat)
        cola.put(imagen)
        print(f" Satélite {id_sat} -> Imagen {imagen['id']} enviada")
        time.sleep(random.uniform(1, 3))  # Llegada aleatoria
