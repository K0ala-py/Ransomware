import os
keys_book = open('keys.txt','r')

listachiavi = []
listafile = []
for line in keys_book:
    line = line.replace('\n', '')
    if 'FILE:' in line:
        listafile.append(line[6:]+'.lock')
    if 'KEYPASSWORD:' in line:
        listachiavi.append(line[13:])

for i in range(len(listafile)):
    from cryptography.fernet import Fernet
    f = Fernet(listachiavi[i])
    with open(listafile[i],'rb') as encrypted_file:
        encrypted = encrypted_file.read()
        decrypted = f.decrypt(encrypted)
    with open(listafile[i],'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    os.rename(listafile[i],listafile[i][:-5])


keys_book.close()