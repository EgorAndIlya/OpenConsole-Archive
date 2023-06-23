# -*- coding: utf-8 -*-

# OpenConsole, By Wico

import time
time1 = time.time()

import os, platform, datetime, json

try:
    from colorama import init, Fore
    from asyncio import sleep, create_task
    from Data_OpenConsole.langpack import *
    from Data_OpenConsole.maindata import *
except Exception as error:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

try:
    init()

    with open('Settings.json', 'r') as cfg:
        settings = json.load(cfg)

    # Section "Settings"
    username = (settings['username'])
    pcname = (settings['pcname'])
    check_system = (settings['check_platform'])
    null_screen = (settings['null_screen'])
    preview_location = (settings['preview_location'])

    print(Fore.GREEN + welcome1 + '\n\n' + Fore.YELLOW + welcome2 + username + Fore.RESET + '\n')

        
    if check_system == 'True': check_platform()
    if null_screen == 'True': os.system('cls')

    time_ = int(time.time() - time1)

    print(Fore.GREEN + '[Debugging] OpenConsole started in {} seconds.\n'.format(time_) + Fore.RESET)

    while True: launchercmds()
except Exception as error: stopworking(reason=error) 