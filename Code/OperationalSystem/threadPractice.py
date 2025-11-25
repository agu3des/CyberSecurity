from threading import Thread, get_ident

class Somador(Thread):
#somador é uma thread
    def __init__(self, inicio, fim):
        Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.somatorio = 0

    def run(self):
        for i in range(self.inicio, self.fim + 1):
            self.somatorio += i
            print('Thread-', get_ident())

s1 = Somador(0, 10)
s2 = Somador(11, 20)

s1.start()
s2.start()
#dá o start e em algum momento haverá o run

s1.join() 
s2.join()
#coloca o join para que aguarde a execução da thread criada

print(s1.somatorio)
print(s2.somatorio)
print('Ananda Guedes do Ó')