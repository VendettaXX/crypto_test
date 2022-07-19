# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)

# derive
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2 ** 14,
    r=8,
    p=1,
)
key = kdf.derive(b"my great password")

# verify
kdf = Scrypt(
    salt=salt,
    length=32,
    n=2 ** 14,
    r=8,
    p=1,
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kdf.verify(b"my great password", key)
    print(key.hex())
    print(len(key))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
