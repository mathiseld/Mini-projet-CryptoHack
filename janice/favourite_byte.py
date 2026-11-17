import base64
from Crypto.Util.number import *
import sys

hidden = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

hidden_decode = bytes.fromhex(hidden).decode()
flag = "".join(chr(ord(f)^16) for f in hidden_decode)

print(hidden_decode)
print(flag)