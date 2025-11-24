from math import isqrt
from sympy.functions.combinatorial.numbers import jacobi_symbol



def proverca(x, b, n, c1, c2):
    xc1_prom=int(x+b/2)
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
        shifr=int(f.readline().strip(), 16)
        c1=int(f.readline().strip(), 16)
        c2=int(f.readline().strip(), 16)
    with open(secret_key, "r") as f:
        p=int(f.readline().strip(), 16)
        q=int(f.readline().strip(), 16)
    with open(public_key, "r") as f:
        n=int(f.readline().strip(), 16)
        b=int(f.readline().strip(), 16)

    sredinca=int(-b//2+int(isqrt(shifr+b*b//4)))
    x=[0]*4
    x[0]=pow(sredinca, 1, p)
    x[1]=p-x[0]
    x[2]=pow(sredinca, 1, q)
    x[3]=q-x[2]
    text=0
    for i in range(4):
        prov=proverca(x[i], b, n, c1, c2)
        if prov==True:
            text=x[i]
            break
    file_for_text=input('Введіть назву файлу куди вам записати розшифрований текст')
    with open (file_for_text, "w") as f:
        print(text, file=f)
    print(x)
     

Decrypt()