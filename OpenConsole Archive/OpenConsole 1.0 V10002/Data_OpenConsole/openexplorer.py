import os
try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def openexplorer():
    print(openexplorer1)
    select = input(openexplorer2)
    if select == '1': mk_dir()
    if select == '2': read_dir()
    if select == '3': read_file()

def mk_dir():
    try:
        name_folder = input(mkdir1)
        if not name_folder:
            os.mkdir('Folder', mode=0o777, dir_fd=None)
            print(mkdir2)
        else:
            os.mkdir(name_folder, mode=0o777, dir_fd=None)
            print(mkdir3)
    except OSError:
        print(mkdir4)

def read_file():
    try:
        name_file = input(readfile1)
        if not name_file:
            print(readfile2)
        else:
            with open(name_file, 'r', encoding='utf-8') as file:
                logs = file.read()
                print('\n{}\n'.format(logs))
    except:
        print(readfile3)

def read_dir():
    try:
        name_folder = input(readdir1)
        if not name_folder:
            print(readdir2)
        else:
            logs = os.listdir(path=name_folder)
            print("\n{}\n".format(logs))
    except:
        print(readfile3)