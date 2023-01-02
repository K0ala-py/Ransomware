import os
keys_book = open('keys.txt','r')

listachiavi = []
listafile = []
for line in keys_book:                              # for line in key file
    line = line.replace('\n', '')   
    if 'FILE:' in line:                             # if the "FILE" work is in line 
        listafile.append(line[6:]+'.lock')          # add file name into the "listafile" list
    if 'KEYPASSWORD:' in line:                      # idem for "KEYPASSWORD" word
        listachiavi.append(line[13:])

for i in range(len(listafile)):                     # for any element into "listafile" = any encrypt file
    from cryptography.fernet import Fernet          # import fernet library
    f = Fernet(listachiavi[i])
    with open(listafile[i],'rb') as encrypted_file: 
        encrypted = encrypted_file.read()           # read encrypt file and
        decrypted = f.decrypt(encrypted)            # decrypt here
    with open(listafile[i],'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.rename(listafile[i],listafile[i][:-5])       # rename file from "example.txt.lock" in "example.txt"


keys_book.close()                                   # close key book file
