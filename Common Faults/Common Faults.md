# Common Faults

## Problem
lostcactus has a gold vault, but is faulty, so to protect his gold, he encrypted the password with RSA. lostcactus, a fond fan of Euler, generated a list of public keys, until it contained `271828`, the first 6 digits of Euler's number. Unfortunatly for lostcactus, just like his vault, his key generator is also faulty, having a COMMON issue with his vault. Help him find his password again.

[Original problem](https://ctf.mcpt.ca/problem/wxm24crypto2)

### Attachment

[ciphertext](./ciphertext) 

[past-keys](./past_keys)

## Solution

Taking a look at the encryption, the plaintext ```flag``` is ecrupted encrypted using RSA, with the same public exponent $e=65537$, but has a different public key each time, $n_1,n_2,n_3$, respectively. 

When reading the encryption file, we notice that six unique primes are not used to generate the public keys, rather three is used, where each prime is used twice. This removed the difficulty of factoring the public keys, rather we can take the greatest common denominator of two public keys, and find its common prime. After we find the prime $p,q,r$ we can calculate $\phi \left( n_1 \right),\phi \left( n_2 \right),\phi \left( n_3 \right)$, in turn we can calculate the mod inverse of $e$ for $n_1,n_2,n_3$, respectively. From here on, the problem is trivial, and taking the ciphertext to the power of the mod inverses will result in the plaintext.

***
### Flag 
```picoCTF{1_gu3ss_tr1pl3_rs4_1snt_tr1pl3_s3cur3!!!!!!}```