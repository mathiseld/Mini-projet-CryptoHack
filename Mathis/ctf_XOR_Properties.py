from pwn import xor

K1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# KEY2 ^ KEY1 
K2K1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
# KEY2 ^ KEY3
K2K3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# FLAG ^ KEY1 ^ KEY3 ^ KEY2
FK1K3K2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

K2 = xor(K1, K2K1)
K3 = xor(K2K3, K2)
Flag = xor(FK1K3K2, K1, K2, K3).decode()
print(Flag)