from pwn import xor

m = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# cle = xor(m[:7], b"crypto{")
# print(cle)
# flag = xor(m, b"myXORkey").decode()
# print(flag)

cle = xor(m[:7], b"crypto{") + xor(m[-1], b"}")
print(f"La clé est : {cle}")
flag = xor(m, cle).decode()
print(flag)