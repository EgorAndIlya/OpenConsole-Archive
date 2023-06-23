import os, platform
try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        print(error3)