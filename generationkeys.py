from secrets import randbits
from prostechislo import parochki
from random import  randint
from math import gcd
from l20 import l20
from test import miller_rabin, trial_division
from random import randint




def prostechislo(k:int):
    test=False
    while test==False:
        p=l20(k)
        
        proverochka=trial_division(p)
        if proverochka==True:
            test=miller_rabin(p)
    return int(''.join(str(i) for i in p), 2)


def  GenerateKeyPair(bits):
    bits_pq=int(((bits/2)-3)/4)
    p=prostechislo(bits_pq)*4+3
    q=prostechislo(bits_pq)*4+3
    n=p*q
    b=randint(2, n-1)
    if b%2!=0:
        b+=1
    return p, q, n, b



p, q, n, b=GenerateKeyPair(2048)
with open("secret_keys.txt", "w") as f:
    print(hex(p), file=f)
    print(hex(q), file=f)
with open("open_keys.txt", "w") as f:
    print(hex(n), file=f)
    print(hex(b), file=f)
