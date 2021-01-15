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
