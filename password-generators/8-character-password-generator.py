# This example was taken directly from the Python Documentation for the
# secrets module, which can be found here:
# https://docs.python.org/3/library/secrets.html

import string
import secrets

# Generate an eight-character password:
alphabet8 = string.ascii_letters + string.digits
password8 = "".join(secrets.choice(alphabet8) for i in range(8))
print(password8)
