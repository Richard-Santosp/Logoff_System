import os

def format_number(num):
    num /= 60
    if num.is_integer():
        num = int(num)
    if num <= 1:
        return f'{num} Hora'
    return f'{num} Horas'

def logoff_windows(campo):
    os.system(f'shutdown -s -f -t {campo}')

def logoff_linux(campo):
    os.system(f'shutdown {campo}')


def encerrar_logoff_windows():
    return os.system('shutdown -a')

def encerrar_logoff_linux():
    return os.system('shutdown -c')
