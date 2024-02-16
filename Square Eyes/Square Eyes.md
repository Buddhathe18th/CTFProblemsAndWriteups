# Square Eyes
## Problem
It was taking forever to get a 2048 bit prime, so I just generated one and used it twice.

[Original problem](https://cryptohack.org/challenges/rsa/#:~:text=%C2%B7%2018%20Solutions-,Square%20Eyes,-35%20pts%20%C2%B7)

### Attachment

[output.txt](./output.txt) 

## Solution

The security of RSA comes from the fact that without knowing the prime factors of $n$, it is impossible to find $\phi \left( n \right)=\left( p-1\right) \cdot \left( q-1\right)$. To find $p,q$, we must factor $n$, which is very computationally heavy.

In this problem, we see that instead of two unique primes $p,q$, the problem uses the same prime twice, so $n=p^2$. We know it is a lot faster to use a square root operation, rather than factoring, so we can easily find the values of $n,p$. Then, we can find $\phi\left(n\right)=p^2-p$. After this, the solution is trivial as we can find the modular inverse of $e=65537$ in respect to $\phi\left(n\right)$ as the private exponent. Then, simply taking the power of the ciphertext to the power of the private exponent in mod $n$ gives the plaintext.

***
### Flag 
```crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}```