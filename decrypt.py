from cryptography.fernet import Fernet
def dec_process(file,key):                      # this is an funcion used in "ransomware.py" file for encrypt
    f = Fernet(key)
    with open(file,'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open(file,'wb') as decrypted_file:
        decrypted_file.write(decrypted)
