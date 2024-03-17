# Common Faults

## Problem
lostcactus has a gold vault, but is faulty, so to protect his gold, he encrypted the password with RSA. lostcactus, a fond fan of Euler, generated a list of public keys, until it contained `271828`, the first 6 digits of Euler's number. Unfortunatly for lostcactus, just like his vault, his key generator is also faulty, having a COMMON issue with his vault. Help him find his password again.

[Original problem](https://ctf.mcpt.ca/problem/wxm24crypto2)

### Attachment

[ciphertext](./ciphertext) 

[past-keys](./past_keys)

## Solution

As the problem tells us, the key generator also has an issue, with emphasize on `COMMON`. This leads us to believe that maybe all the public keys may share a common factor, which has to be a prime. To verify our doubts, we take the gcd of some of the public keys, and notice they all share the same prime. Testing to see if the actual public key is divisible by this leads us to both primes, where then the problem is trivial.

***
### Flag 
```wxmctf{CommOn_F@u1t_0R_cOMm0N_f4ctoR?}```