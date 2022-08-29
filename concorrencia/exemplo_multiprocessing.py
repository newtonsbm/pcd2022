import time
from multiprocessing import Process

def calcula_exponencial_lentamente(num):
    print("Calculando o quadro de ",num)
    time.sleep(5)
    print(num," * ",num," = ",num*num)
    return


def main():
    print("Iniciando")
    processos = []
    for i in range(5):
        processos.append(Process(target=calcula_exponencial_lentamente, args=(i,)))
    
    for processo in processos:
        processo.start()

if __name__ == "__main__":
    main()


