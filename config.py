import os

def format_number(num):
    num /= 60
    if num.is_integer():
        num = int(num)
    if num <= 1:
        return f'{num} Hora'
    return f'{num} Horas'

def logoff(campo):
    os.system(f'shutdown -s -f -t {campo}')


def encerrar_logoff():
    return os.system('shutdown -a')
