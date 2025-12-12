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

    bits_p=int(((bits//2-2)))
    bits_q=bits_p
    while True:
     print(1)
     p=prostechislo(bits_p)*4+3
     q=prostechislo(bits_q)*4+3
     n=p*q
     print(n.bit_length())
     if n.bit_length()==bits:
         print(0)
         break
     elif n.bit_length()>bits:
         bits_p-=1
         bits_q-=1
    b=randint(2, n-1)
    return p, q, n, b



p, q, n, b=GenerateKeyPair(128)
p=int(p)
n=int(n)
print(p.bit_length(), n.bit_length())
with open("secret_keys.txt", "w") as f:
    print(hex(p), file=f)
    print(hex(q), file=f)
with open("open_keys.txt", "w") as f:
    print(hex(n), file=f)
    print(hex(b), file=f)
