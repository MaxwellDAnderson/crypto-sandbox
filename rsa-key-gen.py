'''
Generates and serializes public-private RSA key pair and saves them as .PEM
files on the desktop. You should not keep these files on the desktop. The
keys are initially saved to the desktop for convenience.
'''


import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os
import time

class privatekey:

    # Private key generation
    private_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = 4096,
    )

    # Private key serialization
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )

    # Gets username for use in file creation
    username = os.getlogin()

    # Date and time format for the file
    timestamp = time.strftime("%Y-%m-%d-%H%M%S")

    # Creates file on Desktop with the date and time in proper format.
    # Since the keys are byte-like objects, "wb" (write bytes) is used.
    priv_file = open(f"C:\\Users\\{username}\\Desktop\\{timestamp}__PRIVATE__Key.pem", "wb")

    # Writes the private key to the file
    priv_file.write(pem_private)

    # Closes the private key file.
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
