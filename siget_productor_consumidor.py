import threading
import time
import random

BUFFER_SIZE = 4
buffer = []
espacios = threading.Semaphore(BUFFER_SIZE)
elementos = threading.Semaphore(0)
mutex = threading.Lock()

def productor(nombre, cantidad):
    for i in range(cantidad):
        dato = f"{nombre}-dato-{i+1}"
        espacios.acquire()
        with mutex:
            buffer.append(dato)
            print(f"[PRODUCTOR] {nombre} produjo {dato} | Buffer: {len(buffer)}/{BUFFER_SIZE}")
        elementos.release()
        time.sleep(random.uniform(0.2, 0.6))

def consumidor(nombre, total):
    for _ in range(total):
        elementos.acquire()
        with mutex:
            dato = buffer.pop(0)
            print(f"[CONSUMIDOR] {nombre} proceso {dato} | Buffer: {len(buffer)}/{BUFFER_SIZE}")
        espacios.release()
        time.sleep(random.uniform(0.3, 0.7))

if __name__ == "__main__":
    print("=" * 65)
    print("SIGET - SIMULACION PRODUCTOR-CONSUMIDOR")
    print("=" * 65)
    print("Dos sensores producen datos y un modulo los consume.\n")

    p1 = threading.Thread(target=productor, args=("Sensor-1", 5))
    p2 = threading.Thread(target=productor, args=("Sensor-2", 5))
    c1 = threading.Thread(target=consumidor, args=("Analizador-1", 10))

    p1.start()
    p2.start()
    c1.start()

    p1.join()
    p2.join()
    c1.join()

    print("\n" + "=" * 65)
    print("SIMULACION FINALIZADA CORRECTAMENTE")
    print(f"Elementos pendientes en buffer: {len(buffer)}")
    print("Semaforos y exclusion mutua aplicados correctamente.")
    print("=" * 65)
