from threading import Thread, Lock

counter = 0
counters = list()
lock = Lock()

def worker():
    soma = 0
    for _ in range(100000):
        # lock.acquire()
        # início da região crítica
        soma += 1 # counter = counter + 1
        '''
        load counter, $a0
        add 1, $a0
        add $a0, counter
        '''
        # fim da região crítica
        # lock.release()
    counters.append(soma)


if __name__ == '__main__':
    
    threads = []

    # um for que não me importa a variável de iteração
    for _ in range(32):
        # construindo a thread
        t = Thread(target=worker)
        # iniciando a thread
        t.start()
        # armazenando seu controle
        threads.append(t)

    for t in threads:
        # esperando pelo fim de uma determinada threads
        t.join()

    counter = sum(counters)
    print(counters)
    print(counter)