from random import randint
from math import gcd

def attack(n_hex):
    
    n = int(n_hex, 16)

    k = 1
    while True:
        print(f'\nСпроба {k}')

        t = randint(2, n - 2)
        y = pow(t, 2, n)
        print('Надіслати серверу y =', hex(y))
        z_hex = input('Ввести отримане z: ')
        z = int(z_hex, 16)

        p1 = gcd(t - z, n)
        if 1 < p1 < n:
            p = p1
            q = n // p
            print('Знайдено p =', hex(p))
            print('І маємо q =', hex(q))
            return

        p2 = gcd(t + z, n)
        if 1 < p2 < n:
            p = p2
            q = n // p
            print('Знайдено p =', hex(p))
            print('І маємо q =', hex(q))
            return

        print('Не пощастило')
        k += 1



attack('')
