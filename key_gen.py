from cryptography.fernet import Fernet
def key_gen():
    key = Fernet.generate_key()
    with open('mykey.key','wb') as mykey:
        key = mykey.write(key)