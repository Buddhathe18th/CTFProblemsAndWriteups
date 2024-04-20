# Parameter Injection

## Problem
You're in a position to not only intercept Alice and Bob's DH key exchange, but also rewrite their messages. Think about how you can play with the DH equation that they calculate, and therefore sidestep the need to crack any discrete logarithm problem.

Connect at `socket.cryptohack.org 13371`

[Original problem](https://cryptohack.org/challenges/diffie-hellman/#:~:text=You%27re%20in%20a%20position%20to%20not%20only%20intercept%20Alice%20and%20Bob%27s%20DH%20key%20exchange%2C%20but%20also%20rewrite%20their%20messages.)

## Solution

We connect to the given port and see a message that Alice is sending to Bob. This message includes a $p,g$ and $A$. Now, we first send Bob exactly what we recieved to see what will happen next. In turn, we recieve $B$, and sending that to Alice will give us the iv and encrypted flag. We are given the decryption script, and all we need is their shared secret. 

What we notice is that when Alice sends the first message, if we tamper with that, only Alice will know the actual values of $p,g$ and $a$. Then, what if we send Bob certain values that makes $b=2$? Then we have access to one person's secret number, allowing us to gain access to the shared secret. Simply enough, we send Bob a message saying $g=2,p=3,A=2$. Then Bob, knowing the mod is 3, will chose a number greater than 1, and less than 3, so $b=2$. As expected, we recieve $B=1$.  

If we send that directly to Alice, Alice will calculate the shared secret to be $B^a\mod p=1^a\mod p=1$. So using 1 as the shared secret and decrypting results in the flag.
***
### Flag 
```crypto{n1c3_0n3_m4ll0ry!!!!!!!!}```