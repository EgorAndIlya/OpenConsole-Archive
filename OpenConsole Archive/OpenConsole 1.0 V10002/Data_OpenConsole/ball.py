import os, platform, random
try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def ball():
    q = input(ball1)
    if not q: return
    qq = random.choice(results)
    print(ball2.format(qq))