import hashlib

str = input()
res = hashlib.sha256(str.encode())
print(res.hexdigest())