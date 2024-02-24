# Sum-O-Primes

## Problem
We have so much faith in RSA we give you not just the product of the primes, but their sum as well! 

[Original problem](https://play.picoctf.org/practice/challenge/310?category=2&page=5)

### Attachment

[gen.py](./gen.py) 

[output.txt](./output.txt)

## Solution

The difficulty in decrypting RSA comes from not knowing $\phi \left( n\right)=\left(p-1\right)\cdot\left(q-1\right)$ since it is impossible to find $p,q$ or $p-1,q-1$ from $n=p\cdot q$. Yet, in this problem we are also given $x=p+q$ which, other than providing us with a more efficiet way of factoring $n$, we can entirely skip the step of finding $p,q$ and directly find $\phi\left(n\right)=\left(p-1\right)\cdot\left(q-1\right)=p\cdot q-\left(p+q\right)+1=n-x+1$.

In turn we can calculate the mod inverse of $e=65537$ to find the private exponent $d$. From here on, the problem is trivial, and taking the ciphertext to the power of $d \mod n$  will result in the plaintext.

***
### Flag 
```picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_92fe3557}```