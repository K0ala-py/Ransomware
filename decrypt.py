from cryptography.fernet import Fernet
def dec_process(file,key):
    f = Fernet(key)
    with open(file,'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open(file,'wb') as decrypted_file:
        decrypted_file.write(decrypted)