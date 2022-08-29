import time
from threading import Thread
from concurrent.futures import ProcessPoolExecutor, as_completed

def calcular_media(valores):
    return sum(valores)/len(valores)

def obter_media_sensores(sensores_valores):
    sensores_medias = []
    future_medias = []
    executor = ProcessPoolExecutor(max_workers=5)
    for valores in sensores_valores:
        submmited = executor.submit(calcular_media, valores)
        future_medias.append(submmited)
    
    for future in as_completed(future_medias):
        sensores_medias.append(future.result())

    return sensores_medias

if __name__ == "__main__":
    N = 50000000
    sensores_valores = [range(x) for x in range(N, N+10)]

    start_time = time.time()
    media_sensores = obter_media_sensores(sensores_valores)
    duracao = time.time() - start_time
    print(f"------- Single Thread - Duracao: {duracao} seg")
    print(media_sensores)
