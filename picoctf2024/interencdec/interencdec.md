# interencdec

## Problem
Can you get the real meaning from this file.

[Original problem](https://play.picoctf.org/practice/challenge/418)

### Attachment

[enc_flag](./enc_flag)

## Solution

Opening the problem file, we see a string `YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==`, with characters from `0-9a-zA-Z+/=`, which is indeed the alphabet of Base 64. Decoding from base 64 gives the string `b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='` which looks just base 64, but with the additional `b''` around it. Removing the additional characters and decoding from base 64 again gives `wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}`, which seems like a rotation of the flag. Rotating this string 19 characters forwards in the alphabet gives us the flag.

***
### Flag 
```picoCTF{caesar_d3cr9pt3d_890d2379}```