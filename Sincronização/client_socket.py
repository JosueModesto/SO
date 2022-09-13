import re
import socket

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1235))

    event = 0
    while event != '2':
        print('1. Receber dados')
        print('2. Fechar')
        event = input('Escolha: ')
        if event == '1':
            s.send(bytes('data', 'utf-8'))
            msg = s.recv(1024).decode('utf-8')
            freq, n_proc, mem = msg.split('|')
            print(f'\nFrequência (GHz): {freq}')
            print(f'Número de processadores: {n_proc}')
            print(f'Tamanho de memória (GiB): {int(eval(mem) / 10e5)}\n')
        elif event == '2':
            print('Programa encerrado!')
            s.send(bytes('stop', 'utf-8'))

    s.close()
