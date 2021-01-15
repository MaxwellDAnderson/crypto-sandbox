# This example was taken directly from the Python Documentation for the
# secrets module, which can be found here:
# https://docs.python.org/3/library/secrets.html

import string
import secrets

# Generate a ten-character alphanumeric password with at least 3 numbers:

alphabet10 = string.ascii_letters + string.digits
while True:
    password10 = "".join(secrets.choice(alphabet10) for i in range(10))
    if (any(c.islower() for c in password10)
        and any(c.isupper() for c in password10)
            and sum(c.isdigit() for c in password10) >= 3):
        break

print(password10)
