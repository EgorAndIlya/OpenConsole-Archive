# -*- coding: utf-8 -*-

# OpenConsole Beta 1, By Wico, GidesPC

try:
    from colorama import init, Fore
    import os, time, platform, datetime, configparser
    cwdget = os.getcwd()
except:
    print('Ошибка | Не удалось импортировать библиотеки!')

help_text = """
Команды OpenConsole:
help -> Список команд OpenConsole
cls -> Очистить экран консоли
title -> Установить заголовок окна
echo -> Вывести любой текст на экран окна
exit -> Выйти из OpenConsole
whoami -> Имя пользователя/Имя компьютера
colors -> Установить цвет вывода текста
openexplorer -> Проводник
info -> Информация о OpenConsole
create_error -> Создать ошибку
"""

info_text = """
OpenConsole - Много функциональная консоль на Python
\nРазработчики:
Wico -> Основной кодер, основатель OpenConsole
GidesPC -> Кодер, помощник Wico
\n\t<-------Ссылки------->
Discord -> discord.gg/zSdaaSzNQ4 

(c) Wico, GidesPC | Все права за кодированы.
"""

init()
cwdget = os.getcwd()

try:
    config = configparser.ConfigParser()
    config.read("Settings.ini", encoding='utf-8')
except:
    print('Ошибка | Файл конфигурации испорчен или же отсутствует')

try:
    # Категория "UserInfo"
    username = (config['UserInfo']['username'])
    pcname = (config['UserInfo']['pcname'])
    # Категория "OpenConsoleSettings"
    check_system = (config['OpenConsoleSettings']['check_platform'])
    null_screen = (config['OpenConsoleSettings']['null_screen'])
    preview_location = (config['OpenConsoleSettings']['preview_location'])
except:
    print('Ошибка | Файл конфигурации испорчен или же отсутствует')

def help(): print(help_text)
def cls(): os.system('cls')
def whoami(): print('\n' + username + '/' + pcname + '\n')
def info(): print(info_text)

def openexplorer():
    print('OpenExplorer - Проводник\n1) Создание новой директории\n2) Чтение существующей директории\n')
    select = input('Напишите нужную цифру --> ')
    if select == '1': mk_dir()
    if select == '2': read_dir()

def read_dir():
    try:
        name_folder = input('\n[ListDir] Введите название директории --> ')
        if not name_folder:
            print('\n[ListDir] Вы не указали название директории!\n')
        else:
            logs = os.listdir(path=name_folder)
            print(f"\n{logs}\n")
    except:
        print('\n[ListDir] Директории не существует!\n')

def mk_dir():
    try:
        name_folder = input('\n[MkDir] Введите название новой директории --> ')
        if not name_folder:
            os.mkdir('Новая директория', mode=0o777, dir_fd=None)
            print('\n[MkDir] Успешно создана новая директория "Новая директория"\n')
        else:
            os.mkdir(name_folder, mode=0o777, dir_fd=None)
            print('\n[MkDir] Успешно создана новая директория "' + name_folder + '"\n')
    except OSError:
        print('\n[MkDir] Директория уже существует!\n')

def title():
    title_input = input('[Title] Введите новое название окна --> ')
    if not title_input: os.system('title Не забудь указать название окна')
    else: os.system('title OpenConsole - ' + title_input)
        
def echo():
    echo_input = input('[Echo] Введите текст, который нужно вывести --> ')
    if not echo_input: print('\n[Echo] Текст не указан.\n')
    else: print('\n' + echo_input + '\n')
        
def custom_color():
    print('\nКастомные цвета вывода текста\n1 - Зелёный\n2 - Красный\n3 - Жёлтый\n4 - Синий\n5 - Сбросить кастомный цвет')
    color_input = input('\nНапишите нужную цифру --> ')
    if color_input == '1': print(Fore.GREEN + '\n[Colors] Успешно установлен цвет "Зелёный"\n')
    elif color_input == '2': print(Fore.RED + '\n[Colors] Успешно установлен цвет "Красный"\n')
    elif color_input == '3': print(Fore.YELLOW + '\n[Colors] Успешно установлен цвет "Жёлтый"\n')
    elif color_input == '4': print(Fore.BLUE + '\n[Colors] Успешно установлен цвет "Синий"\n')
    elif color_input == '5': print(Fore.RESET + '\n[Colors] Успешно сброшены все установленые цвета\n')
    else: print('\n[Colors] Вы не указали цифру либо же указали её не правильно\n')
        
def check_platform():
    if platform.system() == 'Windows': pass
    elif platform.system() == 'Linux': exit()
    elif platform.system() == 'Darwin': exit()

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
    with open('Temp\\_start_vbs_.bat', 'w+', encoding='utf-8') as bat:
        bat.write(bat_text)
    with open('Temp\\_remove_error_.bat', 'w+', encoding='utf-8') as bat_two:
        bat_two.write(bat_two_text)
    with open('Temp\\_create_error_.vbs', 'w+', encoding='utf-16') as vbs:
        vbs.write(vbs_text)

def create_error():
    input_text = input('[CreateError] Введите текст ошибки --> ')
    input_title = input('[CreateError] Введите заголовок ошибки --> ')
    if not input_text:
        print('[CreateError] Вы не указали текст ошибки!')
        return
    if not input_title:
        print('[CreateError] Вы не указали заголовок ошибки!')
        return
    print('[CreateError] Создание ошибки. . .')
    compile_error(text_error=input_text, title_error=input_title)
    os.system('"Temp\_start_vbs_.bat"')
    os.system('"Temp\_remove_error_.bat"')
    os.system('cls')
    os.system('title Укажи новое название окна с помощью команды "title"')
    
def launchercmds():
    if preview_location == 'True':
        cmd_input = input(cwdget + ' --> ')
        if cmd_input.lower() == 'help': help()
        elif cmd_input.lower() == 'cls': cls()
        elif cmd_input.lower() == 'title': title()
        elif cmd_input.lower() == 'echo': echo()
        elif cmd_input.lower() == 'exit': exit()
        elif cmd_input.lower() == 'whoami': whoami()
        elif cmd_input.lower() == 'colors': custom_color()
        elif cmd_input.lower() == 'openexplorer': openexplorer()
        elif cmd_input.lower() == 'info': info()
        elif cmd_input.lower() == 'create_error': create_error()
    else:
        cmd_input = input('OpenConsole --> ')
        if cmd_input.lower() == 'help': help()
        elif cmd_input.lower() == 'cls': cls()
        elif cmd_input.lower() == 'title': title()
        elif cmd_input.lower() == 'echo': echo()
        elif cmd_input.lower() == 'exit': exit()
        elif cmd_input.lower() == 'whoami': whoami()
        elif cmd_input.lower() == 'colors': custom_color()
        elif cmd_input.lower() == 'openexplorer': openexplorer()
        elif cmd_input.lower() == 'info': info()
        elif cmd_input.lower() == 'create_error': create_error()

print(Fore.GREEN + 'OpenConsole [Версия Бета 1]\n(c) Wico & GidesPC | Все права защищены' + '\n' + Fore.YELLOW + 'Вы вошли как: ' + username + '\nВ первый раз в OpenConsole? Пропиши help чтобы получить справку!' + Fore.RESET + '\n')
if check_system == 'True': check_platform()
if null_screen == 'True': os.system('cls')

while True: launchercmds()