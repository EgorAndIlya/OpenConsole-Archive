import os, platform
try:
    from colorama import init, Fore
    from Data_OpenConsole.langpack import *
except:
    print('Error -> Failed to import libraries and files!')
    input()
    exit()

def compile_error(text_error, title_error):
        try: os.mkdir('Temp', mode=0o777, dir_fd=None)
        except OSError: pass
        vbs_text = 'x=msgbox("{}", 4+16, "{}")'.format(text_error, title_error)
        bat_text = """
        @echo off
        Temp\_create_error_.vbs
        """
        bat_two_text = """
        @echo off
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
    try:
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
        else:
            print(error3)
            return
    except:
        pass