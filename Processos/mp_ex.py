# import multiprocessing as mp
from multiprocessing import Process
# import time
from time import sleep


def worker(nome, i):
    #time.sleep(5)
    sleep(5)
    #print(nome)
    print(f'Começou a execução do processo {i} com nome {nome}')



def call_mp():
    procs = list()
    nomes = ('Modesto', 'Teruichi', 'Bianca', 'Eduarda', )
    for i, nome in enumerate(nomes):
        print('Criação do processo:', nome)
        #procs.append(mp.Process(target=worker, args=(nome, i)))
        #procs.append(Process(target=worker, args=(nome, i)))
        #proc.start()
        p = Process(target=worker, args=(nome, i))
        procs.append(p)
        p.start()

    for proc in procs:
        proc.join()

    print('qualquer coisa')


if __name__ == '__main__':
    call_mp()
