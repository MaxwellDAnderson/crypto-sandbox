import string
import secrets

# Generate an eight-character password:
alphabet8 = string.ascii_letters + string.digits
password8 = "".join(secrets.choice(alphabet8) for i in range(8))
print(password8)
