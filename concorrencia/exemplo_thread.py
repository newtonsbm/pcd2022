import time
from threading import Thread

def calcula_exponencial_lentamente(num):
    print("Calculando o quadro de ",num)
    time.sleep(5)
    print(num," * ",num," = ",num*num)
    return


def main():
    print("Iniciando")
    threads = []
    for i in range(5):
        threads.append(Thread(target=calcula_exponencial_lentamente, args=(i,)))
    
    for thread in threads:
        thread.start()

if __name__ == "__main__":
    main()


