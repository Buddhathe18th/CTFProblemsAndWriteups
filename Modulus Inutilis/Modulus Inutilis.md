# Modulus Inutilis

## Problem
We have so much faith in RSA we give you not just the product of the primes, but their sum as well! 

[Original problem](https://cryptohack.org/challenges/rsa/#:~:text=My%20primes%20should%20be%20more%20than%20large%20enough%20now!)

### Attachment

[modulus_inutilis.py](./modulus_inutilis.py) 

[output.txt](./output.txt)

## Solution

We notice that the ciphertext is very small, much smaller than the public exponent. This gives us the motivation that the ciphertext was not impacted by the modulo $n$. To verify our hunch, we check if $c$ is a perfect cube, which luckily enough, is indeed a perfect cube. Taking teh cube root will leave us with the the plaintext and flag.

***
### Flag 
```crypto{N33d_m04R_p4dd1ng}```