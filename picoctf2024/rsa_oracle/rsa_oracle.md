# rsa_oracle

## Problem
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message (ciphertext) and the password that was used to encrypt the message.

[Original problem](https://play.picoctf.org/practice/challenge/422)

### Attachment

[enc_flag](./enc_flag)

## Solution

We see the problem doesn't give us the public key or public exponent, so we can try to find those first. We know that $p^e-c$ will always be divisble by $n$. Therefore, we can try encrypting a few inputs and find their gcd. So when I encrypt `a`, which is equal to `97`, to get `1894792376935242028465556366618011019548511575881945413668351305441716829547731248120542989065588556431978903597240454296152579184569578379625520200356186`. Similarly, `b`, equal to `98`, is encrypted to `851992879179488480924931526330455538592762608496783380067377309746890611786399664808324043270356878711820024924791940001427666209616488708970666420225203`. Common values of `e` are $3,5,17,65537$, so testing `gcd(97^e-1894792376935242028465556366618011019548511575881945413668351305441716829547731248120542989065588556431978903597240454296152579184569578379625520200356186,98^e-851992879179488480924931526330455538592762608496783380067377309746890611786399664808324043270356878711820024924791940001427666209616488708970666420225203)` for each `e` gives `11,1,1,1,5507598452356422225755194020880876452588463543445995226287547479009566151786764261801368190219042978883834809435145954028371516656752643743433517325277971`. We see that `e=3` cannot work since `11` isn't the product of two primes, so we see that `e=65537`. In addition, plugging that number into [factordb](http://factordb.com/) shows that this does not contain any other smaller prime factors. 

To simply exploit the oracle, we can ask it to decrypt $2^e\cdot c$ since the $2^e$ part will be turned into $2 \mod n$. We take the result and divide by two to get the plaintext of `881d9`. Then we use OpenSSL to decrypt the file using the command `openssl enc -aes-256-cbc -d -in secret.enc -out flag.txt` and inputting `881d9` as the password. This results in the flag

***
### Flag 
```picoCTF{su((3ss_(r@ck1ng_r3@_881d93b6}```