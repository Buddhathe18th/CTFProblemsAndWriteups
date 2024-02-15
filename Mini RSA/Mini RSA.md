# Mini RSA

## Problem
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this. 

[Original problem](https://play.picoctf.org/practice/challenge/188?category=2&page=1)

### Attachment

[ciphertext](./ciphertext)

## Solution

Opposed to the commonly used value of $65537$, $e=3$ which means $c$ is the perfect cube of the plaintext, mod $n$. Therefore, we can easily iterate through values of an integer $k$ such that $c+k\cdot n$ is a perfect cube. Running a simple Python program leads to the answer of $k=3533$. Plugging in the numbers we get that $c+k\cdot n=p^3$ where $p$ is the plaintext. Taking the cube root will give us $p$, then the flag.

***
### Flag 
```picoCTF{e_sh0u1d_b3_lArg3r_a166c1e3}```