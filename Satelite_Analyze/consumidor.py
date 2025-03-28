import time
from queue import Empty
from utils import procesar_imagen

def consumidor(id_analista, cola):
    while True:
        try:
            imagen = cola.get(timeout=5)
            procesar_imagen(imagen, id_analista)
        except Empty:
            print(f" Analista(consumidor) {id_analista} esperando imágenes...")
