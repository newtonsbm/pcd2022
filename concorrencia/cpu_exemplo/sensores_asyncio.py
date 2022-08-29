import time
import asyncio

async def calcular_media(valores):
    return sum(valores)/len(valores)

async def obter_media_sensores(sensores_valores):
    sensores_medias = []
    for valores in sensores_valores:
        media = await calcular_media(valores)
        sensores_medias.append(media)
    return sensores_medias

if __name__ == "__main__":
    N = 50000000
    sensores_valores = [range(x) for x in range(N, N+10)]

    start_time = time.time()
    media_sensores = asyncio.run(obter_media_sensores(sensores_valores))
    duracao = time.time() - start_time
    print(f"------- Single Thread - Duracao: {duracao} seg")
    print(media_sensores)
