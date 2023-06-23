import json
try:
    from colorama import init, Fore
    from asyncio import create_task
    from Data_OpenConsole.langpack import *
    from Data_OpenConsole.openexplorer import *
    from Data_OpenConsole.cls import *
    from Data_OpenConsole.title import *
    from Data_OpenConsole.echo import *
    from Data_OpenConsole.color import *
    from Data_OpenConsole.create_error import *
    from Data_OpenConsole.ball import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

with open('.\Settings.json', 'r') as cfg:
    settings = json.load(cfg)

init()
cwdget = os.getcwd()

username = (settings['username'])
pcname = (settings['pcname'])
check_system = (settings['check_platform'])
null_screen = (settings['null_screen'])
preview_location = (settings['preview_location'])

def stopworking(reason):
    print("""
OpenConsole encountered an error and exited
Reason for stopping OpenConsole: {} (OpenConsole has been stopped.)
    """.format(reason))
    exit()

def check_platform():
    if platform.system() == 'Windows': pass
    else:
        print(warning1)
        input(warning2)

def launchercmds():
    if preview_location == 'True':
        cmd_input = input(cwdget + ' --> ')
    else:
        cmd_input = input('OpenConsole --> ')
    if cmd_input.lower() == 'cls': cls()
    elif cmd_input.lower() == 'title': title()
    elif cmd_input.lower() == 'echo': echo()
    elif cmd_input.lower() == 'exit': exit()
    elif cmd_input.lower() == 'whoami': print('\n' + username + '/' + pcname + '\n')
    elif cmd_input.lower() == 'colors': custom_color()
    elif cmd_input.lower() == 'openexplorer': openexplorer()
    elif cmd_input.lower() == 'create_error': create_error()
    elif cmd_input.lower() == 'ball': ball()
