from decimal import Decimal
from math import gcd
from random import randint
from labanta import r_i_sequence



def miller_rabin(a:list):
    k=100
    p=int(''.join(str(i) for i in a), 2)
    #a=Decimal(int(''.join(str(i) for i in a), 2))
    #p_1=a-Decimal(1)
    p_1=p-1

    s=0
    d=p_1
    psevdosila=False
    while d%2==0:
        s+=1
        #d=d/Decimal(2)
        d=d//2
        print(d)
    for _ in range(k):
        x=randint(2, p-1)
        gcdx=gcd(x, p)
        if gcdx>1:
            return False
        if pow(x, d, p)==1 or pow(x, d, p)==p-1:
            psevdosila=True
        else:
            for _ in range(s-1):
                x=pow(x, 2, p)
                if x==p-1:
                    psevdosila=True
                    break
                elif x==1:
                    psevdosila=False
                    break
        if psevdosila==False:
            return False
    

    return True





def trial_division(n:list):
    
    n=Decimal(int(''.join(str(i) for i in n), 2))
    
    prime =  [Decimal(2), Decimal(3), Decimal(5), Decimal(7), Decimal(11), Decimal(13), Decimal(17), Decimal(19), Decimal(23), Decimal(29), Decimal(31), Decimal(37), Decimal(41), Decimal(43), Decimal(47)]

    n_digits = [int(d) for d in str(n)]
    a_i = n_digits[::-1] #список з цифр n в оберненому порядку

    
    for p in prime:       
        r_i_p_seq = r_i_sequence(p, len(a_i)) #послідовність r_i для р

        sum_ = 0 #сума для а_i * r_i
         
        for i, a in enumerate(a_i):
            sum_ += a * r_i_p_seq[i]

        if sum_ % p == 0:
            return False

    return True

