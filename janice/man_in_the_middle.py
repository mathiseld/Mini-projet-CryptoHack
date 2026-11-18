import socket
import json
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "socket.cryptohack.org"
PORT = 13371

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def recv_until_json():
    """Lit les lignes du serveur jusqu'à trouver une ligne contenant un objet JSON {...}"""
    while True:
        buffer = b""
        while not buffer.endswith(b"\n"):
            chunk = s.recv(1)
            if not chunk:
                break
            buffer += chunk
        line = buffer.decode().strip()
        print("[SERVEUR] ->", line)
        idx = line.find("{")
        if idx != -1:
            return json.loads(line[idx:])

# réception des parametre d'alice (p, g, A)
data_alice = recv_until_json()
p = int(data_alice["p"], 16)
g = int(data_alice["g"], 16)

# injection vers bob : on remplace A par 1 (ce qui force le secret partagé à 1^b mod p =1)
payload_bob = json.dumps({
    "p": hex(p),
    "g": hex(g),
    "A": "0x01"
}) + "\n"
s.sendall(payload_bob.encode())

# réception de la réponse de bob (B)
data_bob = recv_until_json()

# injection vers alice : on remplace B par 1 (ce qui force le secret partagé à 1^a mod p= 1)
payload_alice = json.dumps({
    "B": "0x01"
}) + "\n"
s.sendall(payload_alice.encode())

# réception du message chiffré d'alice
response = recv_until_json()
iv = bytes.fromhex(response["iv"])
encrypted_flag = bytes.fromhex(response["encrypted_flag"])

# dérivation de la clé aes avec shared_secret= 1
shared_secret = 1
sha1 = hashlib.sha1()
sha1.update(str(shared_secret).encode('ascii'))
key = sha1.digest()[:16]

# déchiffrement aes cbc
cipher = AES.new(key, AES.MODE_CBC, iv)
flag = unpad(cipher.decrypt(encrypted_flag), AES.block_size)

print("\nflag :", flag.decode())
s.close()