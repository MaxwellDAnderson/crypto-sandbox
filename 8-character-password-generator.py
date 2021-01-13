import hashlib
import string
import secrets
import cryptography
from cryptography.fernet import Fernet


# Generate an eight-character alphanumeric password:
alphabet8 = string.ascii_letters + string.digits
password8 = "".join(secrets.choice(alphabet8) for i in range(8))
print(password8)
