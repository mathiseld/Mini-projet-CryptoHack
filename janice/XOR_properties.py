import base64
from Crypto.Util.number import *
import sys

K1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
K2_K1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
K2_K3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_K1_K3_K2_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1 = int(K1_hex, 16)
k2_k1 = int(K2_K1_hex, 16)
k2_k3 = int(K2_K3_hex, 16)
flag_chiffre = int(FLAG_K1_K3_K2_hex, 16)

k2 = k2_k1 ^ k1
k3 = k2_k3 ^ k2

flag_int = flag_chiffre ^ k1 ^ k2 ^ k3

flag = long_to_bytes(flag_int)

print(f"KEY1 en chiffres: {k1}")
print(f"KEY2 XOR KEY1 en chiffres: {k2_k1}")
print(f"KEY 2 XOR KEY3 en chiffres: {k2_k3}")

print(flag)

# proposition de correction que j'ai trouvé sympa

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2 = key1 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key3 = key2 ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
flag = key1 ^ key2 ^ key3 ^ 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
print(flag.to_bytes(100, 'big'))