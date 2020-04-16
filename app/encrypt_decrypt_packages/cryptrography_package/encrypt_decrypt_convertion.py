from cryptography.fernet import Fernet
import os

#get the key from using os module
salt_key = os.urandom(16)
print(salt_key)

#Encode the message
password ="Spwelcome12345"
encode_password = password.encode()
print("encode_password", encode_password)

#Encrypt the message
f = Fernet(salt_key)
encrypt_password = f.encrypt(f)
print("encrypt_password", encrypt_password)

#Decrypt the encrypted message
decrypt_password = f.decrypt(encrypt_password)

#decode the message
origin_password = decrypt_password.decode()
print("origin_password", origin_password)


