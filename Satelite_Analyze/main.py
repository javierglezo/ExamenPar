from multiprocessing import Process, Manager
from servidor import servidor
from productor import productor
from consumidor import consumidor

def main():
    manager = Manager()
    cola_recepcion = manager.Queue(maxsize=100)     # Imágenes recién llegadas
    cola_procesamiento = manager.Queue(maxsize=100) # Imágenes listas para analizar

    # Lanzamos el servidor (flujo entre recepción y procesamiento)
    servidor_proc = Process(target=servidor, args=(cola_recepcion, cola_procesamiento))
    servidor_proc.start()

    # Lanzamos satélites (productores)
    for i in range(3):
        Process(target=productor, args=(i, cola_recepcion)).start()

    # Lanzamos analistas (consumidores)
    for j in range(5):
        Process(target=consumidor, args=(j, cola_procesamiento)).start()

    servidor_proc.join()

if __name__ == '__main__':
    main()
