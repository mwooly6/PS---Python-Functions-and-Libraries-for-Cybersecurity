import hashlib
"""
str = "Hello My Name is Michael Woolard"
print("Original Text: " + str)

str = str.encode()

#result = hashlib.sha256(str)
result = hashlib.md5(str)
print("The hexadecimal hashed value : " + result.hexdigest())

"""
print("Hardcoded md5 hash of python file from site: e7062b85c3624af82079794729618eca")
filename = "c:\pluralsight\Exe\python64bit.exe"
with open(filename,"rb") as f:
    bytes = f.read()
    hash_output = hashlib.md5(bytes).hexdigest();
    print("md5 hash of file python64but.exe: " + hash_output)
