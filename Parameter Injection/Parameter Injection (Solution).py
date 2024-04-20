from pwn import *
import json
from decrypt import decrypt_flag

r = remote('socket.cryptohack.org', 13371)

aliceFirstMessage=r.readline()[24:]

p="0x3"
g="0x2"
A="0x4"

mes={
  "p": p,
  "g": g,
  "A": A
}
y = json.dumps(mes)

r.send(y)
bobMessage=r.readline()[35:]

b="0x2"
B="0x1"

mes={
  "B": B
}
y = json.dumps(mes)
r.send(y)
encrypt=str(r.readline())[41:-3]
print(encrypt)
val=json.loads(encrypt)

iv=val["iv"]
enc=val["encrypted_flag"]

r.close()

print("\n\n\n\n\nIV is",iv,"\nEncrypted flag is",enc)


shared_secret = 1
iv = "3aaf27455c6f54f173be124ccaefdd8f"
ciphertext = "cf145f943b6ca3b6030d0c0c4b983a566f6df996b5b284aa30056c5ad626375b"

print("\n\n"+decrypt_flag(shared_secret, iv, ciphertext))

