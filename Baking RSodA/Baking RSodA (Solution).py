from Crypto.Util.number import long_to_bytes

n = 241166910162623952350613501051117544837

e = 65537

c = 12310461619440568871196959567575430942

#From FactorDB (http://factordb.com/index.php?query=241166910162623952350613501051117544837)

p=7841965402532628607
q=30753375943833808891

totient=(p-1)*(q-1)

d=pow(e,-1,totient)

print(long_to_bytes(pow(c,d,n))) #This is the key to the Vigenere cipher