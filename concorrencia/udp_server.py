import time
from socket import *

def realiza_processamento(number):
    time.sleep(3);
    return number * number 

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('',server_port))

def start_server():
    print("Servidor esta pronto para receber conexões")
    while True:
        message , client_address = server_socket.recvfrom(2048)
        number = (int)(message)
        answer = realiza_processamento(number)
        server_socket.sendto(bytes(str(answer), "utf-8"), client_address)

if __name__ == "__main__":
    start_server()