import os
import time
import pgpy
from pgpy import PGPMessage
from pgpy import PGPKey


pubkey, _ = PGPKey.from_file("path/to/publickey.asc")
msg = PGPMessage.new("asdf")
pubkey.encrypt(msg)

username = os.getlogin()

datetime = time.strftime("%Y-%m-%d-%H%M%S")


f = open(f"C:/Users/{username}/Desktop/{datetime}_ENCRYPTED_PGP_Message.txt", "w")
f.write(str(pubkey.encrypt(msg)))
f.close()
