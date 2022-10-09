import rpyc

class CalculadoraService(rpyc.Service):
    def exposed_soma(self, a, b):
        return a+b
    
    def exposed_subtracao(self, a, b):
        return a-b

    def exposed_teste(self):
        print("Teste da classe de serviços")

if __name__ == "__main__":
    server = rpyc.ThreadedServer(CalculadoraService, port = 18811)
    server.start()