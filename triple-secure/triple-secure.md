# triple-secure

## Problem
To get the flag, you must break RSA not once, but three times!

[Original problem](https://play.picoctf.org/practice/challenge/209?category=2&page=3)

### Attachment

[encrypt.py](./encrypt.py) 

[public-key.txt](./public-key.txt)

## Solution

Taking a look at the encryption, the plaintext ```flag``` is ecrupted encrypted using RSA, with the same public exponent $e=65537$, but has a different public key each time, $n_1,n_2,n_3$, respectively. 

When reading the encryption file, we notice that six unique primes are not used to generate the public keys, rather three is used, where each prime is used twice. This removed the difficulty of factoring the public keys, rather we can take the greatest common denominator of two public keys, and find its common prime. After we find the prime $p,q,r$ we can calculate $\phi \left( n_1 \right),\phi \left( n_2 \right),\phi \left( n_3 \right)$, in turn we can calculate the mod inverse of $e$ for $n_1,n_2,n_3$, respectively. From here on, the problem is trivial, and taking the ciphertext to the power of the mod inverses will result in the plaintext.

***
### Flag 
```picoCTF{1_gu3ss_tr1pl3_rs4_1snt_tr1pl3_s3cur3!!!!!!}```