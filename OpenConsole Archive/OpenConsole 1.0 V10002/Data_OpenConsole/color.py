try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

init()

def custom_color():
    print(color1)
    color_input = input(color2)
    if color_input == '1': print(Fore.GREEN + color3)
    elif color_input == '2': print(Fore.RED + color4)
    elif color_input == '3': print(Fore.YELLOW + color5)
    elif color_input == '4': print(Fore.BLUE + color6)
    elif color_input == '5': print(Fore.RESET + color7)
    else: print(color8)
