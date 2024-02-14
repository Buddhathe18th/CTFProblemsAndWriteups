#!/usr/bin/env python3

from random import randint

characters = bytes(range(33, 126))

def rotate(input, key):
    if len(input) == 0:
        return b''
    return bytes([characters[(characters.index(input[0])+key)%len(characters)]])+rotate(input[1:],key-1) #Changed +1 to -1




print(rotate(b'ewjC[+}l]-m<H3,U4BF\'Dl:>kSQRZ_', 59)) #Changed key to 59

