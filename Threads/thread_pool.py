from concurrent.futures import ThreadPoolExecutor as TPE
from os import cpu_count
from time import sleep


def task(val):
    sleep(1)
    return f'Tarefa {val} completa!'


if __name__ == '__main__':
    # cria trabalhadores que aguardam para executar tarefas
    print(cpu_count())
    executor = TPE(max_workers=cpu_count())

    # cria uma lista de controle
    ctrl = list()
    for i in range(8):
        ctrl.append(executor.submit(task, i+1))

    for c in ctrl:
        print(c.result())
