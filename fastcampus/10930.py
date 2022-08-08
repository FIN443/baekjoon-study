# SHA-256
import hashlib

S = input()
hashed = hashlib.sha256(S.encode())
result = hashed.hexdigest()
print(result)
