# -*- coding: utf-8 -*-

# OpenConsole Beta Test 3, By Wico

import os, time, platform, datetime, json

with open('Settings.json', 'r') as cfg:
    settings = json.load(cfg)

try:
    from colorama import init, Fore
    from language import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()
    
init()
cwdget = os.getcwd()

# Section "Settings"
username = (settings['username'])
pcname = (settings['pcname'])
check_system = (settings['check_platform'])
null_screen = (settings['null_screen'])
preview_location = (settings['preview_location'])

def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        print(error3)
        
def openexplorer():
    print(openexplorer1)
    select = input(openexplorer2)
    if select == '1': mk_dir()
    if select == '2': read_dir()
    if select == '3': read_file()
    
def read_file():
    try:
        name_file = input(readfile1)
        if not name_file:
            print(readfile2)
        else:
            with open(name_file, 'r', encoding='utf-16') as file:
                logs = file.read()
                print(f'\n{logs}\n')
    except:
        print(readfile3)

def read_dir():
    try:
        name_folder = input(readdir1)
        if not name_folder:
            print(readdir2)
        else:
            logs = os.listdir(path=name_folder)
            print(f"\n{logs}\n")
    except:
        print(readfile3)

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

def title():
    if platform.system() == 'Windows':
        title_input = input(title1)
        if not title_input: os.system("title Don't forget to name the window")
        else: os.system('title OpenConsole - ' + title_input)
    else:
        print(error3)
        pass

def echo():
    echo_input = input(echo1)
    if not echo_input: pass
    else: print('\n' + echo_input + '\n')
        
def custom_color():
    print(color1)
    color_input = input(color2)
    if color_input == '1': print(Fore.GREEN + color3)
    elif color_input == '2': print(Fore.RED + color4)
    elif color_input == '3': print(Fore.YELLOW + color5)
    elif color_input == '4': print(Fore.BLUE + color6)
    elif color_input == '5': print(Fore.RESET + color7)
    else: print(color8)
        
def check_platform():
    if platform.system() == 'Windows': pass
    else:
        print(warning1)
        input(warning2)

def compile_error(text_error, title_error):
        try: os.mkdir('Temp', mode=0o777, dir_fd=None)
        except OSError: pass
        vbs_text = f"""
        x=msgbox("{text_error}", 4+16, "{title_error}")
        """
        bat_text = """
        @echo off
        title Create Error (OpenConsole)
        Temp\_create_error_.vbs
        """
        bat_two_text = """
        @echo off
        title Remove Error (OpenConsole)
        cd...
        del Temp /s /q
        """
        with open('Temp\\_start_vbs_.bat', 'w+', encoding='utf-16') as bat:
            bat.write(bat_text)
        with open('Temp\\_remove_error_.bat', 'w+', encoding='utf-16') as bat_two:
            bat_two.write(bat_two_text)
        with open('Temp\\_create_error_.vbs', 'w+', encoding='utf-16') as vbs:
            vbs.write(vbs_text)

def create_error():
    if platform.system() == 'Windows':
        input_text = input(create_error1)
        input_title = input(create_error2)
        if not input_text:
            print(create_error3)
            return
        if not input_title:
            print(create_error4)
            return
        print(create_error5)
        compile_error(text_error=input_text, title_error=input_title)
        os.system('"Temp\_start_vbs_.bat"')
        os.system('"Temp\_remove_error_.bat"')
        os.system('cls')
        os.system('title Specify a new title for the window using the "title" command')
    else:
        print(error3)
        return

def launchercmds():
    if preview_location == 'True':
        cmd_input = input(cwdget + ' --> ')
        if cmd_input.lower() == 'cls': cls()
        elif cmd_input.lower() == 'title': title()
        elif cmd_input.lower() == 'echo': echo()
        elif cmd_input.lower() == 'exit': exit()
        elif cmd_input.lower() == 'whoami': print('\n' + username + '/' + pcname + '\n')
        elif cmd_input.lower() == 'colors': custom_color()
        elif cmd_input.lower() == 'openexplorer': openexplorer()
        elif cmd_input.lower() == 'create_error': create_error()
    else:
        cmd_input = input('OpenConsole --> ')
        if cmd_input.lower() == 'cls': cls
        elif cmd_input.lower() == 'title': title()
        elif cmd_input.lower() == 'echo': echo()
        elif cmd_input.lower() == 'exit': exit()
        elif cmd_input.lower() == 'whoami': print('\n' + username + '/' + pcname + '\n')
        elif cmd_input.lower() == 'colors': custom_color()
        elif cmd_input.lower() == 'openexplorer': openexplorer()
        elif cmd_input.lower() == 'create_error': create_error()

print(Fore.GREEN + 'OpenConsole [Version Beta Test 3]\n(c) Wico | All rights reserved.' + '\n' + Fore.YELLOW + 'You are logged in as: ' + username + '\nFor the first time in OpenConsole? Type help to get help!' + Fore.RESET + '\n')
if check_system == 'True': check_platform()
if null_screen == 'True': os.system('cls')

while True: launchercmds()