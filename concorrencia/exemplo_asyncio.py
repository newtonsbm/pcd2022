import time
import asyncio

async def calcula_exponencial_lentamente(num):
    print("Calculando o quadro de ",num)
    await asyncio.sleep(5)
    print(num," * ",num," = ",num*num)
    return


async def main():
    print("Iniciando")
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(calcula_exponencial_lentamente(i)))
    
    for task in tasks:
        await task

if __name__ == "__main__":
    asyncio.run(main())



