import multiprocessing as mp


def worker():
    a = 0
    for i in range(8**4):
        for j in range(10**3):
            a += i**j   # a = a + i^j

procs = []
for i in range(4): #numero de cpus
    p = mp.Process(target=worker)
    procs.append(p)
    p.start()


for p in procs:
    p.join()

print('Processos finalizados!')


# Comandos para alteração de prioridades
# $ [sudo] nice -n NICE{-20 <-> 19} [time] python3 proc_lento.py
# $ [sudo] renice <prioridade> -p PID

