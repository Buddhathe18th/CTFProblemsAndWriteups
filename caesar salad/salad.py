#!/usr/bin/env python3

from random import randint

characters = bytes(range(33, 126))

def rotate(input, key):
    if len(input) == 0:
        return b''
    return bytes([characters[(characters.index(input[0])+key)%len(characters)]])+rotate(input[1:],key+1)


flag = open("flag.txt", "rb").read()


print(rotate(flag, randint(0, 2**128)))

# Output:
# b'ewjC[+}l]-m<H3,U4BF'Dl:>kSQRZ_'
