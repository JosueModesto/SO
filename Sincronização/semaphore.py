from threading import Thread, Semaphore
from random import choice
from time import sleep

buffer = list()
buffer_max = 2
sem_mutex = Semaphore(1)
sem_empty = Semaphore(buffer_max)
sem_full = Semaphore(0)


def produtor():
    while True:
        # t = choice(range(1, 10))
        # sleep(1 / t)

        item = choice(range(100))
        sem_empty.acquire() # acquire semaforo down
        # entrando na região crítica
        sem_mutex.acquire()
        buffer.append(item)
        sem_mutex.release() # release é o up
        # saiu da região crítica
        sem_full.release()
        print(f'Produtor inseriu {item}')


def consumidor():
    while True:
        # t = choice(range(1, 10))
        # sleep(1 / t)
        
        sem_full.acquire()
        # entrando na região crítica
        sem_mutex.acquire()
        item = buffer.pop()
        sem_mutex.release()
        # saiu da região crítica
        sem_empty.release()
        print(f'Consumidor removeu {item}')


if __name__ == '__main__':
    p = Thread(target=produtor)
    c = Thread(target=consumidor)
    c.start()
    p.start()