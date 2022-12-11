from cryptography.fernet import Fernet
def enc_process(file):
    with open('mykey.key','rb') as mykey:
        key = mykey.read()
    f = Fernet(key)
    with open(file,'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open(file+'.lock','wb') as encrypted_file:
        encrypted_file.write(encrypted)
