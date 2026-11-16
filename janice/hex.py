#!/usr/bin/env python3
import base64
from Crypto.Util.number import *
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print("Here is your flag:")
print((bytes.fromhex(hex_string)))

# ---------------------------------------------------------------------------------------------------
# ex 2 
hex_string2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decode = bytes.fromhex(hex_string2)

print("Here is your flag:")
print((base64.b64encode(decode)))

# ---------------------------------------------------------------------------------------------------
# ex 3
int_msg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
str_msg = long_to_bytes(int_msg)

print("Here is your flag:")
print(str_msg)

# ---------------------------------------------------------------------------------------------------
# ex 4
msg = "label"
m = "".join(chr(ord(m)^13) for m in msg)

print("Here is your flag:")
print(f"crypto{{{m}}}")
