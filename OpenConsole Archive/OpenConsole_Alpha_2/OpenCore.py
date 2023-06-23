import os

config_text = """
username = 'OpenUser'
pcname = 'OpenPC'
"""

import Commands
from Commands import help

onecoredir = os.getcwd()

def OpenLauncher():
    input_cmd = input(onecoredir + ' --> ')
    if input_cmd == 'help': help()
    
def pyerror(error):
    print('OpenConsole обнаружил ошибку и приостановил данный сеанс!\nКод остановки: ', + error)
    print('Нажмите Enter, чтобы возобновить сеанс.')
    
def config_restore():
    print('[OpenRestore] Восстановление конфигурации, подождите...')
    config = open('config_console.py', 'w+', encoding='utf-8')
    config.write(config_text)
