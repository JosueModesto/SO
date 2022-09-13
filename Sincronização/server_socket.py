import socket
import re
from time import sleep


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1235))
    s.listen(5)

    client, addr = s.accept()
    print(f"Conexão no endereço {addr[0]} na porta {addr[1]} foi estabilizada.")

    msg = ''
    while msg != 'stop':
        msg = client.recv(1024).decode('utf-8')
        if msg == 'data':
            arq_cpu = open("/proc/cpuinfo")
            arq_mem = open("/proc/meminfo")
            texto_cpu = arq_cpu.readlines()
            texto_mem = arq_mem.readlines()
            n_proc = 0
            for linha in texto_cpu:
                if 'model name' in linha:
                    info_freq = re.search(r'@ (?P<f>\d.+)GHz', linha)
                if 'processor' in linha:
                    info_n_proc = re.search(r'processor.+?(?P<p>\d{1,2})', linha)
            freq = info_freq.group('f')
            n_proc = str(int(info_n_proc.group('p')) + 1)
            for linha in texto_mem:
                if 'MemTotal' in linha:
                    info_mem = re.search(r'MemTotal.+    (?P<m>\d+)', linha)
            mem = str(int(info_mem.group('m')) / 1024 * 1024)
            print(f'Servidor enviando informações para {addr[0]}')
            # sleep(1)
            client.send(bytes(f'{freq}|{n_proc}|{mem}', 'utf-8'))
    client.close()