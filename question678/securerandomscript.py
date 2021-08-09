import hashlib
import sys
import os

value = sys.argv[1]
salt=os.urandom(32)
hashed_value = hashlib.pbkdf2_hmac('sha512',value.encode(),salt,200000)
print(hashed_value.hex())




