from math import isqrt, sqrt
from sympy.functions.combinatorial.numbers import jacobi_symbol
from secrets import randbits
from sympy import mod_inverse, sqrt_mod
from sympy import gcdex
from l20 import l20


def parsing_x(x:int, n:int):
    r=l20(64)
    r=int(''.join(str(i) for i in r), 2)
    r=str(hex(r))
    x_str=(hex(x))
#тут виправлю

   # x_ret= 
    return int(x_ret)




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
    c2=c2.encode()
    c2=int(c2, 16)
    p=p.encode()
    p=int(p, 16)
    q=q.encode()
    q=int(q, 16)
    n=n.encode()
    n=int(n, 16)
    b=b.encode()
    b=int(b, 16)
    b_2=b*pow(2, -1, n)%n
    b_4=b*b*pow(4, -1, n)%n
    y=-b_2+isqrt(shifr+b_4)
    #y=int(y)
    y=y%n
    s1=pow(y, (p+1)//4, p)
    s2=pow(y, (q+1)//4, q)
    u, v, _=gcdex(p, q)
    u=int(u)
    v=int(v)
    print(u*p+v*q, 554327)
    x=[0]*4
    x[0]=(u*p*s1+v*q*s2)%n
    x[1]=(u*p*s1-v*q*s2)%n
    x[2]=(-u*p*s1+v*q*s2)%n
    x[3]=(-u*p*s1-v*q*s2)%n


    text=0
    for i in range(4):
        prov=proverca(x[i], b, n, c1, c2)
        x[i]=int(x[i])
        print(hex(x[i]))
        if prov==True:
            text=hex(x[i])
    print(text)
    file_for_text=input('Введіть назву файлу куди вам записати розшифрований текст')
    l=(text.bit_length()+7)//8
    
    text_b=text.to_bytes(l, "big")
    print(text_b)
    text=text_b[2:l-8]
    print(text)
    text=int.from_bytes(text, "big")
    print(hex(parsing_x(1001, n)))
    with open (file_for_text, "w") as f:
        print(hex(text), file=f)
    
     

Decrypt()