import string
import secrets
import cryptography
from cryptography.fernet import Fernet


class key_gen:
    key = Fernet.generate_key()
    key_file = open("keys.key", "wb")  # since the key is generate in bytes, I used "ab" to append bytes to the end of the keys.key file
    key_file.write(key)
    key_file.close()
    my_key = Fernet(key)

class message_encrypt:
    plaintext = "hello motto".encode()
    f = key_gen.my_key
    ciphertext = f.encrypt(plaintext)
    cipherfile = open("cipher.file", "wb")
    cipherfile.write(ciphertext)
    cipherfile.close()

class message_decrypt:
    decrypted_message = message_encrypt.f.decrypt(message_encrypt.ciphertext)
    message_file = open("decrypted.file", "wb")
    message_file.write(decrypted_message)
    message_file.close()
