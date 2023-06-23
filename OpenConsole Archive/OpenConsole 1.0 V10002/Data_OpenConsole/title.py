import os, platform
try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def title():
    if platform.system() == 'Windows':
        title_input = input(title1)
        if not title_input: pass
        else: os.system('title ' + title_input)
    else:
        print(error3)
        pass