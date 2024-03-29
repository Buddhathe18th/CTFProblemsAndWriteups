# Custom encryption

## Problem
Can you get sense of this code file and write the function that will decode the given encrypted file content.

[Original problem](https://play.picoctf.org/practice/challenge/412)

### Attachment

[enc_flag](./enc_flag)
[custom_encryption.py](./custom_encryption.py)

## Solution

Skipping all the method definitions, we see the python program will run `test(message,"trudeau")` which we will assume the `message` variable will contain the flag we are searching for. Looking at the definition of the `test()` method, we see two primes $p,q$ and two random integers $a,b$. Then we set two variables to be $u=g^a \mod p,v=g^b \mod p$. We also see $g^{a,b} \mod p$ should be the shared key. Therefore, the shared key is $31^{90\cdot 26} \mod 97=22$

Then we are introduced to the `semi-cipher` variable, which will encode the plaintext in some way, which we will discover later. Then, we print `encrypt(semi_cipher, shared_key)`. Checking the definition of `encrypt()`, we see each character of the plain text is taken, and is replaced with the ASCII value of that character, multiplied by the key and 311. We already know the shared key is 22, so taking the ciphertext and dividing by $22\cdot 311$ gives us the `semi_cipher` variable.

We see each value of `semi_cipher` is created by taking the ASCII value of the character of the plaintext, then XORed with the ASCII value of the next character of the key. So by the property of XOR $c=a\char`\^b\Longrightarrow a=c\char`\^b$ so we take the XOR of the key again to the `semi_cipher` variable to get the flag.

***
### Flag 
```picoCTF{custom_d2cr0pt6d_49fbee5b}```