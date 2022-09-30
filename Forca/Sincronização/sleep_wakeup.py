from threading import Thread, Event
from random import choice
from time import sleep

buffer = list()
buffer_max = 10
estado_consumidor = Event()
estado_produtor = Event()


def produtor():
    while True:
        # t = choice(range(1, 10))
        # sleep(1 / t)
        
        item = choice(range(100))
        if len(buffer) == buffer_max:
            print('Produtor vai dormir')
            # necessário para "limpar" buffer indesejável
            estado_produtor.clear()
            estado_produtor.wait() # sleep
            print('Produtor acordou')
        buffer.append(item)
        print(f'Produtor inseriu {item} BUFFER TAM: {len(buffer)}')
        if len(buffer) == 1:
            print('Produtor vai acordar Consumidor...')
            estado_consumidor.set()


def consumidor():
    while True:
        #t = choice(range(1, 10)) coloca um espaço de tempo para executar
        #sleep(1 / t)
        
        if len(buffer) == 0:
            print('Consumidor vai dormir')
            estado_consumidor.clear()
            estado_consumidor.wait()
            print('Consumidor acordou')
        item = buffer.pop()
        print(f'Consumidor removeu {item} BUFFER TAM: {len(buffer)}')
        if len(buffer) == buffer_max - 1:
            print('Consumidor vai acordar Produtor...')
            estado_produtor.set()


if __name__ == '__main__':
    p = Thread(target=produtor)
    c = Thread(target=consumidor)
    p.start()
    c.start()