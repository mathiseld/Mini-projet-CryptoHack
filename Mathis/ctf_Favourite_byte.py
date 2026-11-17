from pwn import xor

m = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
    msg = xor(m, i)
    if b"crypto{" in msg:
        print(f"La clé est : {i}")
        print(msg.decode())
