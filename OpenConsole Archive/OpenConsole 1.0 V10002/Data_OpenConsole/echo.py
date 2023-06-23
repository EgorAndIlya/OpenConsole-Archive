try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def echo():
    echo_input = input(echo1)
    if not echo_input: pass
    else: print('\n' + echo_input + '\n')
