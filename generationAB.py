from prostechislo import parochki
from random import  randint
from math import gcd


def chose_e(oyler_n:int):
    while True:
        e=randint(2, oyler_n-1)
        if gcd(e, oyler_n)==1:
            return e

def key_odin(p, q):
    n=p*q
    func_oyler_n=(p-1)*(q-1)
    e=0x10001
    d=pow(e, -1, func_oyler_n)
    return [n, e], [d, p, q]



def keysA_B():
    p, q, p1, q1=parochki()
    keys_a_open, key_a_secret=key_odin(p, q)
    keys_b_open, key_b_secret=key_odin(p1, q1)
    with open("open_keys_A.txt", "w") as f:
        print(hex(keys_a_open[0]), file=f)
        print(hex(keys_a_open[1]), file=f)

    with open("secret_keys_A.txt", "w") as f:
        print(key_a_secret[0], file=f)
        print(key_a_secret[1], file=f)
        print(key_a_secret[2], file=f)

    with open("open_keys_B.txt", "w") as f:
        print(hex(keys_b_open[0]), file=f)
        print(hex(keys_b_open[1]), file=f)

    with open("secret_keys_B.txt", "w") as f:
        print(key_b_secret[0], file=f)
        print(key_b_secret[1], file=f)
        print(key_b_secret[2], file=f)



keysA_B()
