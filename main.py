import platform
import os
from multiprocessing import Process
from time import sleep


def hijoWindows():
    print('Soy el hijo con PID', os.getpid(), 'y voy a empezar a esperar')
    sleep(5)
    print('Me muero con PID', os.getpid())
    os._exit(0)

def padreWindows():
    numero_procesos = int(
        input('Introduce cuantos procesos hijos quieres ejecutar: '))

    n = 1

    while n <= numero_procesos:
        p = Process(target=hijoWindows)
        p.start()
        p.join(0)
        
        n += 1

def hijoLinux():
    print('Soy el hijo con PID', os.getpid(), 'a punto de finalizar')
    sleep(5)
    print('Me muero con PID', os.getpid())
    os._exit(0)


def padreLinux():
    numero_procesos = int(input('Introduce cuantos procesos hijos quieres ejecutar: '))

    n = 1

    while n <= numero_procesos:
        nuevoPid = os.fork()

        if nuevoPid == 0:
            hijoLinux()
        
        
        n += 1
def main():

    sistema = platform.system()

    if sistema == 'Windows':
        padreWindows()
    elif sistema == 'Linux':
        padreLinux()


if __name__ == '__main__':
    main()