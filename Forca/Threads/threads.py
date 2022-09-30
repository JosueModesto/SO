from threading import Thread, get_ident
from time import sleep

data = list()

class Worker(Thread):
    ''' Utilizando na forma de HERANÇA '''

    def __init__(self, val):
        super().__init__()
        self.val = val

    def run(self):
        sleep(1)
        data.append(self.val)
        print('Identificador da thread:', self.ident)


def worker(val):
    ''' Utilizando na forma de ALVO '''

    #sleep(1)
    print('Identificador da thread:', get_ident())
    print(f'Tarefa {val} completa!')
    data.append(val)


if __name__ == '__main__':
    # onde serão armazenadas as threads
    threads = []

    # for i in range(16):
    #     worker(i+1)

    # criando na forma de herança de Thread
    #for i in range(16):
    #    threads.append(Worker(i+1))

    # criando na forma de alvo da Thread
    for i in range(16):
        t = Thread(target=worker, args=[i+1])
        threads.append(t)
    
    # criando as thread
    for t in threads:
        t.start()

    # # aguardando o final da execução das threads
    for t in threads:
       t.join()

    # # mostra os dados gerados pelas threads
    print(data)