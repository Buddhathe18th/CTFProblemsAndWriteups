# Manyprime
## Problem
Using one prime factor was definitely a bad idea so I'll try using over 30 instead.

[Original problem](https://cryptohack.org/challenges/rsa/#:~:text=Using%20one%20prime%20factor%20was%20definitely%20a%20bad%20idea%20so%20I%27ll%20try%20using%20over%2030%20instead.)

### Attachment

[output.txt](./output.txt) 

## Solution

At first, this seems to be a daunting task, but after counting the number of digits in $n$, there would be an average of 68 bits for the primes. This means the factors of $n$ are decently small, small enough for an efficient factoring algorithm to fully factor $n$. 

Using the Elliptic Curve Factorization Method on Sage math, we can fully factor $n$ within a minute. Indeed, each prime is around 68 bits long, with 32 primes in total. Let us denote each of these primes as $p_1,p_2,p_3 \dots p_{32}$. Looking all the primes, we see there are no primes that are equal, so using the characteristics of the Euler totient function, $\phi\left(n\right)=\phi\left(\prod_{i=1}^{32}p_i\right)=\prod_{i=1}^{32}\left(p_i-1\right)$. This is a simple calculation, providing us with the totient of $n$. 

With this, we can calculate the private exponent by taking the modular inverse of $e=65537$ mod $\phi\left(n\right)$. Then, taking $c$ to the power of the private exponent mod $n$ gives us our plaintext

***
### Flag 
```crypto{700_m4ny_5m4ll_f4c70r5}```