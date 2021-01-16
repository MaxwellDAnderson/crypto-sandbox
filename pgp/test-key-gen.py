# Everything except the username, time, and file operations was copied
# directly from the PGPy documentation, which can be found here:
# https://pgpy.readthedocs.io/en/latest/examples.html#keys
# Also check out the PGPy repository on GitHub:
# https://github.com/SecurityInnovation/PGPy

import pgpy
from pgpy.constants import PubKeyAlgorithm
from pgpy.constants import KeyFlags
from pgpy.constants import HashAlgorithm
from pgpy.constants import SymmetricKeyAlgorithm
from pgpy.constants import CompressionAlgorithm
from pgpy import PGPKey
from pgpy import PGPUID
import os
import time

username = os.getlogin()
time = time.strftime("%Y-%m-%d-%H%M%S")

# Key Generation (RSA)
# Primary Key
key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
uid = PGPUID.new("Abraham Lincoln", comment = "Honest Abe", email = "abraham.lincoln@test.com")
key.add_uid(uid, usage = {KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes = [HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers = [SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression = [CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])

keystr = str(key)

f = open(f"C:/Users/{username}/Desktop/{time}_PGP_Key_1.asc", "w")
f.write(keystr)
f.close()

# Subkey
subkey = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
key.add_subkey(subkey, usage = {KeyFlags.EncryptStorage, KeyFlags.EncryptCommunications, KeyFlags.Sign, KeyFlags.Authentication})

subkeystr = str(subkey)

f = open(f"C:/Users/{username}/Desktop/{time}_PGP_Subkey_1.asc", "w")
f.write(subkeystr)
f.close()
