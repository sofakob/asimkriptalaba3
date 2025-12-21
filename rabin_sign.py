from l20 import l20
from sympy.functions.combinatorial.numbers import jacobi_symbol
from sympy import gcdex
import random 
from secrets import randbits

'''
def parsing_x(x:int, n:int):
    r=l20(64)
    r=int(''.join(str(i) for i in r), 2)
    r=f"{r:016x}"
    l=(n.bit_length()+7)//8
    l_2=(l-10)*2
    m=f"{x:0{l_2}x}"
    x_ret="00"+"ff"+m+r

    return int(x_ret, 16)

def parsing_x(x:int, n:int):
    l=(n.bit_length()+7)//8
    
    nuliki= b'\x00'
    efki=b'\xFF'
    x_bit=x.to_bytes(l-10, "big")
    r= randbits(64).to_bytes(8, "big")
    x_ret= nuliki+efki+x_bit+r
    #print(x_ret)
    return int.from_bytes(x_ret, "big")
'''
def parsing_x(x:int, n:int):
    r=l20(64)
    r=int(''.join(str(i) for i in r), 2)
    l=(n.bit_length()+7)//8
    f=8*(l-8)
    x=255*pow(2, f)+x*pow(2, 64)+r
    return x


def sign(m:int, p:int, q:int):
    while True:
        x=parsing_x(m, p*q)
        print(hex(x))
        a1=jacobi_symbol(x, p)
        a2=jacobi_symbol(x, q)
        print(a1, a2)
        if a1==a2==1:
            break
    y=x
    #y=int(y)
    #y=y%n
    s1=pow(y, (p+1)//4, p)
    s2=pow(y, (q+1)//4, q)
    u, v, _=gcdex(p, q)
    u=int(u)
    v=int(v)
    n=q*p
    print(u*p+v*q, 554327)
    x=[0]*4
    x[0]=(u*p*s1+v*q*s2)
    x[1]=(u*p*s1-v*q*s2)
    x[2]=(-u*p*s1+v*q*s2)
    x[3]=(-u*p*s1-v*q*s2)
    for i in range(4):
        x[i]=(x[i])%n
    s=random.choice(x)
    return s

def SIGN():
    message = input('Введіть назву файла з повідомленням, яке підписати: ')
    secret_key = input('Введіть назву файла з секретним ключем: ')
    text = input('Введіть назву файла куди записати підписане повідомлення: ')
    with open(message, "r") as f:
        m=f.readline().strip()
    #m_int=int.from_bytes(m, "big")
    with open(secret_key, "r") as f:
        p=f.readline().strip()
        q=f.readline().strip()
    
    m=int(m, 16)
    p=int(p, 16)
    q=int(q, 16)
    s=sign(m, p, q)
    with open(text, "w")as f:
        print("(", hex(m),",", hex(s), ")", file=f)


SIGN()