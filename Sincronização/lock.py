from threading import Thread, Lock
from time import sleep

counter = 0
lock = Lock()

def worker():
    global counter
    for _ in range(100000):
        
        #lock.acquire()
        # início da região crítica
        counter += 1 # counter = counter + 1
        '''
        load counter, $a0
        add 1, $a0
        add $a0, counter
        '''
        # fim da região crítica
        #lock.release()


if __name__ == '__main__':
    
    threads = list()

    # um for que não me importa a variável de iteração
    for _ in range(64):
        # construindo a thread
        t = Thread(target=worker)
        # iniciando a thread
        t.start()
        # armazenando seu controle
        threads.append(t)

    for t in threads:
        # esperando pelo fim de uma determinada threads
        t.join()

    print(counter)