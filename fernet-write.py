# This script requires use of the cryptography module, which can be
# downloaded with "pip install cryptography"
# For more information and documentation check out the devs' GitHub:
# https://github.com/pyca/cryptography

import string
import secrets
import cryptography
from cryptography.fernet import Fernet


# Generates Key and Saves Key to File:
class key_gen:
    key = Fernet.generate_key()
    key_file = open("keys.key", "wb")
    key_file.write(key)
    key_file.close()
    my_key = Fernet(key)


# Encrypts message and saves it to file.
class message_encrypt:
    plaintext = "hello motto".encode()
    f = key_gen.my_key
    ciphertext = f.encrypt(plaintext)
    cipherfile = open("cipher.file", "wb")
    cipherfile.write(ciphertext)
    cipherfile.close()


# Decrypts message and saves it to file. NOTE: decrypted messages should
# not normally be saved in unencrypted files, such as this.
class message_decrypt:
    decrypted_message = message_encrypt.f.decrypt(message_encrypt.ciphertext)
    message_file = open("decrypted.file", "wb")
    message_file.write(decrypted_message)
    message_file.close()
