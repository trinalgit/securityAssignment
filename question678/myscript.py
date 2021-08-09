import hashlib
import sys

value = sys.argv[1]
hashed_value = hashlib.pbkdf2_hmac('sha512',value.encode(),b'Km5d5ivMy8iexuHcZrsD',200000)
print(hashed_value.hex())




