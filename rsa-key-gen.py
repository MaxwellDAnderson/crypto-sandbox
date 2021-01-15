'''
Generates and serializes public-private RSA key pair and saves them as .PEM
files on the desktop.
'''


import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
import time

class privatekey:
    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 4096,
    )

    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )

    username = os.getlogin()
    timestamp = time.strftime("%Y-%m-%d-%H%M%S")
    priv_file = open(f"C:\\Users\\{username}\\Desktop\\{timestamp}__PRIVATE__Key.pem", "wb")
    priv_file.write(pem_private)
    priv_file.close()



class publickey:
    public_key = privatekey.private_key.public_key()
    pem_public = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )

    pub_file = open(f"C:\\Users\\{privatekey.username}\\Desktop\\{privatekey.timestamp}__PUBLIC__Key.pem", "wb")
    pub_file.write(pem_public)
    pub_file.close()
