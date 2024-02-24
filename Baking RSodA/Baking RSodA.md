# Baking RSodA

## Problem
This random French guy named Blaise de V…something gave me two packets of suspiciously labelled baking soda. I’m sure it’s nothing…

[Original problem](https://ctf.jonathanw.dev/problem/bts23-crypto3?)

### Attachment

[key.txt](./key.txt)
[crypto3.txt](./crypto3.txt)

## Solution

Opening both files, we see that both are split into block of 8 characters, and each character is either a 1 or a 0, making it probably that it is the ASCII representation of some characters. Using Cyberchef, we convert the characters back into its ASCII characters. All the characters now are ```[a-zA-Z0-9]``` which is similar to the formatting of a base64 string. Converting from base64, we are left with a string, with formatting similar to the flag, with an added note. Trying ROT13, we see that there is no way to properly rotate it. Taking the index of coincidence of the string gives a value of 0.0375, much smaller than the entrophy of a normal english text, giving us the belief that this may be a Vingenere cipher. Taking a look at the other file, key.txt, its name follows our belief.

Similarly, we convert key.txt from binary and it gives us some values for RSA. Taking a look at $n$, it is 128 bits, meaning the two primes are about 64 bits each. These are very small primes, so it is very likely that factoring $n$ is a viable strategy. Using FactorDB, we get our two primes $p,q$. Then, we can solve for the private exponent by taking the modular inverse of $e$ mod $\left(p-1\right)\cdot\left(q-1\right)$. Then taking the ciphertext to the power of the private exponent mod $n$ gives us the plain text ```"vinegar"```. Sounding like a wordplay on Vigenere, we confirm our idea of the Vigenere cipher. In addition, we assume this would be the decryption key.

Using Cyberchef, we decrypt the ```crypto3.txt``` with an additional layer of Vigenere cipher with the key ```vinegar``` to get another encrypted flag, with another hint, saying ```Blaise loves doing everything in twos! Even his encryption!```. In the problem description, we are also introduced to a person ```Blaise de V...```, which is very likely to be Blaise de Vigenere, the person credited with the invention of the Vigenere cipher. Decrypting with the Vigenere cipher with the key ```vinegar``` again, we are left with the flag.


https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=MDEwMDEwMDEgMDExMDExMTAgMDEwMDExMTAgMDExMTAwMDEgMDEwMTEwMTAgMDExMDExMTAgMDExMTAxMDAgMDExMTAwMDEgMDExMDAxMDEgMDEwMDAxMDAgMDEwMTAwMDEgMDExMTEwMDAgMDExMDAwMTEgMDExMTEwMTAgMDEwMDExMTAgMDExMDAxMTAgMDExMDAwMTAgMDEwMDAxMDAgMDEwMDExMTAgMDExMDAxMTAgMDExMDAwMTAgMDEwMDAxMDAgMDEwMDAxMTAgMDExMDEwMTEgMDEwMDExMDEgMDAxMTAwMTAgMDExMDAxMDAgMDExMDAwMDEgMDEwMTAwMTAgMDEwMTAxMDEgMDEwMDAxMTAgMDAxMTEwMDEgMDEwMDEwMDEgMDExMDEwMDEgMDEwMDAwMDEgMDExMTAxMDAgMDEwMTAwMDAgMDExMDEwMDEgMDEwMDAwMDEgMDExMDExMTEgMDEwMTAxMDEgMDAxMTAwMTAgMDExMDAxMDAgMDExMTAwMDAgMDExMDAxMDAgMDExMDExMTAgMDExMDAxMDAgMDExMTAwMTAgMDEwMDEwMDEgMDEwMDAxMTEgMDExMTEwMDAgMDExMDExMDEgMDExMDAwMTEgMDEwMTAxMTEgMDAxMTAwMDEgMDExMDExMDEgMDEwMDEwMDEgMDEwMDAxMTEgMDExMDEwMDAgMDAxMTAwMDEgMDExMDAwMDEgMDEwMTAxMTEgMDEwMTAxMTAgMDExMDEwMDEgMDEwMDEwMDEgMDEwMDAxMTEgMDAxMTAwMDEgMDExMTAwMDAgMDExMDAwMDEgMDEwMTEwMDAgMDExMDEwMDAgMDAxMTAxMDEgMDExMDAwMDEgMDAxMTAwMTAgMDEwMDExMTAgMDExMTEwMDAgMDEwMTEwMDEgMDEwMTAxMTEgMDExMTAwMTEgMDExMDAxMTEgMDExMDAwMTAgMDAxMTAwMTAgMDAxMTAxMDAgMDExMDAxMTEgMDExMDAwMDEgMDAxMTAwMTEgMDEwMDEwMTAgMDAxMTAwMTEgMDEwMTEwMTAgMDExMDEwMDEgMDEwMDAxMDEgMDExMDAxMTEgMDEwMTAwMTEgMDEwMTAxMTEgMDEwMDEwMTAgMDExMDExMDAgMDEwMTEwMTAgMDEwMTAwMTEgMDEwMDAwMTAgMDExMDEwMTAgMDExMDAwMTEgMDEwMTAxMTEgMDEwMTEwMDEgMDExMDAxMTEgMDExMDAwMDEgMDEwMTEwMDAgMDEwMTAwMTAgMDExMDEwMTAgMDExMDAwMDEgMDEwMTEwMDAgMDEwMTAwMTAgMDAxMTAxMDAgMDEwMTEwMTAgMDAxMTAwMTAgMDAxMTAwMDEgMDAxMTAwMDEgMDExMDAwMTAgMDExMDEwMDEgMDEwMDAxMDEgMDExMTAwMDANCg

***
### Flag 
```ctf{bl41s3_d3_v1n3gRSA}```