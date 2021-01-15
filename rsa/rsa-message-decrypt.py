'''
This script requires use of the cryptography module, which can be
downloaded with "pip install cryptography" in the command line.
For more information and documentation check out the devs' GitHub page:
    https://github.com/pyca/cryptography
'''

import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


ciphertext = open("path\\to\\ciphertext\\file", "rb")


with open("path\\to\\private\\key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
    )

plaintext = private_key.decrypt(
    ciphertext.read(),
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)

ciphertext.close()

f = open("path\\where\\you\\want\\to\\save\\plaintext\\file", "wb")
f.write(plaintext)
f.close()
