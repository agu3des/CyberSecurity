import threading
import time
from threading import Semaphore

numero = 0
mutex = Semaphore(1)

def p1():
    global numero
    while True:
        mutex.acquire()
        numero += 1
        print('P1:', numero)
        mutex.release()
        time.sleep(1) 

def p2():
    global numero
    while True:
        mutex.acquire()
        numero += 1
        print('P2:', numero) 
        mutex.release()
        time.sleep(1)    


print('Aluna: Ananda Guedes do Ó - 20231370020')
t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()