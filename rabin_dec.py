from math import isqrt, sqrt
from sympy.functions.combinatorial.numbers import jacobi_symbol
from secrets import randbits
from sympy import mod_inverse, sqrt_mod
from sympy import gcdex
from l20 import l20

'''
def parsing_x(x:int, n:int):
    r=l20(64)
    r=int(''.join(str(i) for i in r), 2)
    x_str=(hex(x))
    r=f"{r:016x}"
    l=(n.bit_length()+7)//8
    l_2=(l-10)*2
    m=f"{x:0{l_2}x}"
    x_ret="0x00"+"ff"+m+r



   
    return int(x_ret, 16)
'''
def parsing_x(x:int, n:int):
    r=l20(64)
    r=int(''.join(str(i) for i in r), 2)
    l=(n.bit_length()+7)//8
    f=8*(l-8)
    x=255*pow(2, f)+x*pow(2, 64)+r
    return x


def proverca(x, b, n, c1, c2):
    b_2=b*pow(2, -1, n)%n
    xc1_prom=int(x+b_2)
    xc1=pow(pow(xc1_prom, 1, n), 1, 2)
    xc2=jacobi_symbol(xc1_prom, n)
    if xc1==c1 and xc2==c2:
        return True
    else:
        return False



def Decrypt():
    message = input('Введіть назву файла з повідомленням, яке хочете розшифрувати: ')
    secret_key = input('Введіть назву файла з секретним ключем: ')
    public_key = input('Введіть назву файла з відкритим ключем адресата: ')
    with open(message, "r") as f:
        shifr=f.readline().strip()
        c1=f.readline().strip()
        c2=f.readline().strip()
    with open(secret_key, "r") as f:
        p=f.readline().strip()
        q=f.readline().strip()
    with open(public_key, "r") as f:
        n=f.readline().strip()
        b=f.readline().strip()
    #shifr=shifr.encode()
    shifr=int(shifr, 16)
    #c1=c1.encode()
    print(c1)
    c1=int(c1, 16)
    print(c1)
    #c2=c2.encode()
    c2=int(c2, 16)
    #p=p.encode()
    p=int(p, 16)
    #q=q.encode()
    q=int(q, 16)
    #n=n.encode()
    n=int(n, 16)
    #b=b.encode()
    b=int(b, 16)
    b_2=b*pow(2, -1, n)%n
    b_4=b*b*pow(4, -1, n)%n
    y=shifr+b_4
    #y=int(y)
    #y=y%n
    s1=pow(y, (p+1)//4, p)
    s2=pow(y, (q+1)//4, q)
    u, v, _=gcdex(p, q)
    u=int(u)
    v=int(v)
    print(u*p+v*q, 554327)
    x=[0]*4
    x[0]=(u*p*s1+v*q*s2)
    x[1]=(u*p*s1-v*q*s2)
    x[2]=(-u*p*s1+v*q*s2)
    x[3]=(-u*p*s1-v*q*s2)
    for i in range(4):
        x[i]=(x[i]-b_2)%n

    text=0
    for i in range(4):
        prov=proverca(x[i], b, n, c1, c2)
        x[i]=int(x[i])
        print(hex(x[i]))
        if prov==True:
            text=hex(x[i])
    print(text)
    text=int(text, 16)
    file_for_text=input('Введіть назву файлу куди вам записати розшифрований текст')
    l=(text.bit_length()+7)//8
    text=(str(hex(text)))
    text=text[2:l-8]
    print(hex(parsing_x(1002, n)))
    with open (file_for_text, "w") as f:
        print(text, file=f)
    

Decrypt()