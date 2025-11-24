from sympy.functions.combinatorial.numbers import jacobi_symbol




def Encrypt():
    message = input('Введіть назву файла з повідомленням, яке хочете зашифрувати: ')
    public_key = input('Введіть назву файла з відкритим ключем адресата: ')
    with open(message, "r") as f:
        x= f.readline().strip()
    x=int(x, 16)
    with open(public_key, "r") as f:
        n= f.readline().strip()
        b= f.readline().strip()
    n=int(n, 16)
    b=int(b, 16)
    y_pomeg=x*(x+b)
    y=pow(y_pomeg, 1, n)
    c1_prom=int(x+b/2)
    c1=pow(pow(c1_prom, 1, n), 1, 2)
    c2=jacobi_symbol(c1_prom, n)
    file_shifr=input("Введіть назву файлу для зашифрованого тексту: " )
    with open(file_shifr, "w") as f:
        print(hex(y), file=f)
        print(hex(c1), file=f)
        print(hex(c2), file=f)
    print("Текст успішно зашифрований, мур)")

Encrypt()