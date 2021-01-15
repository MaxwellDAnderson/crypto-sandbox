'''
This script encrypts and decrypts an RSA message. There is not really a use
for a script that both encrypts a message and then decrypts that same
message, but I used this file for testing to make sure the script would
work, and thought I would share it anyway.
For the individual scripts in separate files, see:
    rsa-message-encrypt.py
    rsa-message-encrypt.py

This script requires use of the cryptography module, which can be
downloaded with "pip install cryptography" in the command line.
For more information and documentation check out the devs' GitHub page:
    https://github.com/pyca/cryptography
'''

import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding



message = b"super duper secret message"

with open("path\\to\\public\\key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
    )

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

key_file.close()


f = open("path\\where\\you\\want\\to\\save\\ciphertext\\file", "wb")
f.write(ciphertext)
f.close()



f = open("path\\to\\ciphertext\\file", "rb")
f.read()

with open("path\\to\\private\\key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
    )

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

f.close()

f = open("path\\where\\you\\want\\to\\save\\plaintext\\file", "wb")
f.write(plaintext)
f.close()
