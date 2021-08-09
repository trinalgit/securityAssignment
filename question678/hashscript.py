import hashlib
import sys
import os

value = sys.argv[1]
salt=os.urandom(32)
hashed_value = hashlib.sha512(str(value.encode()+salt).encode())
print(hashed_value.hexdigest())






