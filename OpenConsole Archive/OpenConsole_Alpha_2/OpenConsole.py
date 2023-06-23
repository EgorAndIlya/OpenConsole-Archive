# -*- coding: utf-8 -*-

# OpenConsole, By Wico
import os, time, Commands, Config
from Commands import check_platform, launchercmds
from colorama import Fore

check_platform()
print('[OpenConsole] Загрузка OpenConsole, пожалуйста подождите...')
username = Config.username
pcname = Config.pcname
cwdget = os.getcwd()
os.system('cls')
print(Fore.GREEN + 'OpenConsole [Version Alpha Test 2]\n(c) Wico | Все права не защищены\n' + Fore.YELLOW + '\n' + 'В первый раз в OpenConsole? Пропиши help чтобы получить справку!' + Fore.RESET + '\n')
while True: launchercmds()
