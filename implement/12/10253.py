# 헨리
from math import gcd, lcm


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    while a != 1:
        x = b // a + 1
        denominator = lcm(b, x)
        frac1 = denominator // x
        frac2 = denominator // b

        a = a * frac2 - frac1
        b = denominator

        check = gcd(a, b)
        if check != 1:
            a = a // check
            b = b // check

    print(b)
