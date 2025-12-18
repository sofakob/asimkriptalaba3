from l20 import l20
from sympy.functions.combinatorial.numbers import jacobi_symbol
from sympy import gcdex
import random 
from secrets import randbits

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


def secture(m, s, n):
    x=pow(s, 2, n)
    x_m=parsing_x(m, n)
    if x==x_m:
        return True
    else:
        return False
    
def SIGN():
    mes = input('Введіть назву файла з повідомленням, яке треба перевірити: ')
    openf = input('Введіть назву файла з відкритим ключем: ')
    with open(mes, "r") as f:
        m=f.readline().strip()
        s=f.readline().strip()
    with open(openf, "r") as f:
        n=f.readline().strip()
    m=int(m, 16)
    s=int(s, 16)
    n=int(n, 16)
    print(secture(m, s, n))
        

SIGN()