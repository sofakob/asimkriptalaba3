from test import miller_rabin, trial_division
from l20 import l20
from sympy import isprime

def prostechislo(k:int):
    test=False
    while test==False:
        p=l20(k)
        
        proverochka=trial_division(p)
        if proverochka==True:
            test=miller_rabin(p)
    return p





def parochki():
    k=256
    q=prostechislo(k)
    p=prostechislo(k)
    q1=prostechislo(k)
    p1=prostechislo(k)
    qint=(int(''.join(str(i) for i in q), 2))
    pint=(int(''.join(str(i) for i in p), 2))
    q1int=(int(''.join(str(i) for i in q1), 2))
    p1int=(int(''.join(str(i) for i in p1), 2))
    if qint*pint<=q1int*p1int:
        return qint, pint, q1int, p1int
    else:
        return q1int, p1int, qint, pint
        


#print(int(''.join(str(i) for i in prostechislo(32)), 2))

print(parochki())


