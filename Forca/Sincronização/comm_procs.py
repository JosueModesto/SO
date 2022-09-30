from multiprocessing import Process, Queue, Manager
import time
from random import choice


def worker(comm, i):
    t = choice(range(1, 30))
    time.sleep(1 / t)
    data = i ** t

    # adicionando resultados com fila sincronizada
    # comm.put((i + 1, data))

    # adicionando resultados com managers
    print(comm)
    comm[f'{i}'] = data



if __name__ == '__main__':
    # comunicação por fila sincronizada
    # queue = Queue()
    # comunicação por managers
    manager = Manager()
    d = manager.dict()

    procs = list()
    for i in range(2):
        p = Process(target=worker, args=(d, i))
        p.start()
        procs.append(p)

    # for p in procs:
        # resultados com managers
        # p.join()

        # resultados com fila sincronizada
        # res = queue.get()
        # print(f'Processo {res[0]} gerou {res[1]}')

    # resultados com managers
    #for k, v in d.items():
    #    print(f'Processo {k} gerou {v}')