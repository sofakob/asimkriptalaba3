from sympy.functions.combinatorial.numbers import jacobi_symbol
from secrets import randbits




def parsing_x(x:int, n:int):
    l=(n.bit_length()+7)//8
    
    nuliki= b'\x00'
    efki=b'\xFF'
    x_bit=x.to_bytes(l-10, "big")
    r= randbits(64).to_bytes(8, "big")
    x_ret= nuliki+efki+x_bit+r
    #print(x_ret)
    return x_ret


def Encrypt():
    message = input('Введіть назву файла з повідомленням, яке хочете зашифрувати: ')
    public_key = input('Введіть назву файла з відкритим ключем адресата: ')
    with open(message, "r") as f:
        x= f.readline().strip()
    x=x.encode()
    x=int(x, 16)
    
    with open(public_key, "r") as f:
        n= f.readline().strip()
        b= f.readline().strip()
    n=int(n, 16)
    b=int(b, 16)
    x=int.from_bytes(parsing_x(x, n), "big")
    y_pomeg=x*(x+b)
    y=pow(y_pomeg, 1, n)
    b_2=b*pow(2, -1, n)%n
    c1_prom=int(x+b_2)
    c1=pow(pow(c1_prom, 1, n), 1, 2)
    c2=jacobi_symbol(c1_prom, n)
    file_shifr=input("Введіть назву файлу для зашифрованого тексту: " )
    with open(file_shifr, "w") as f:
        print(hex(y), file=f)
        print(hex(c1), file=f)
        print(hex(c2), file=f)
    print("Текст успішно зашифрований, мур)")
#print(parsing_x(5, 10000000000000000000000000))
Encrypt()