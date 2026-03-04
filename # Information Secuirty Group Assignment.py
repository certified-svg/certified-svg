# Information Secuirty Group Assignment
 
 

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad 
import base64

key = b"thisisasecretkey"

message = input("Enter the maeesage you want to encrypt: ")

data = message.encode()

#print(type(message))
#print(type(data))

cipher = AES.new(key, AES.MODE_CBC)

iv = cipher.iv

padded_data = pad(data, AES.block_size)

ciphertext = cipher.encrypt(padded_data)

encrypted = base64.b64encode(iv + ciphertext)
print("Enrypted:", encrypted.decode())


encrypted = base64.b64encode(iv + ciphertext)
raw = base64.b64decode(encrypted)
iv = raw[:16]
ciphertext = raw[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted_padded = cipher.decrypt(ciphertext)

decrypted = unpad(decrypted_padded, AES.block_size)


print("Decrypted:", decrypted.decode())





#Encrypt


with open("C:/Users/22jus/OneDrive/username&password/sample.txt.docx", "wb") as file:
    data = file.read()

cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv

padded_data = pad(data, AES.block_size)

ciphertext = cipher.encrypt(padded_data)

with open("C:/Users/22jus/OneDrive/username&password/sample_encrypted.docx", "wb") as file:
    file.write(iv + ciphertext)


# Decrypt 

with open("C:/Users/22jus/OneDrive/username&password/sample_encrypted.docx", "wb") as file:
    raw = file.read()

iv = raw[:16]
ciphertext = raw[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted_padded = cipher.decrypt(ciphertext)

decrypted = unpad(decrypted_padded, AES.block_size)

with open("C:/Users/22jus/OneDrive/username&password/sample_decrypted.docx", "wb") as file:
    file.write(decrypted)
