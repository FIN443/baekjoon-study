from math import gcd


a, b = map(int, input().split())
gcd_ab = gcd(a, b)
print(gcd_ab)
print(a * b // gcd_ab)


"""
a, b = map(int, input().split())
mul = 2
lst = []
# GCD 최대공약수
while True:
    if mul > max(a, b) // 2:
        break
    while True:
        if a % mul != 0 or b % mul != 0:
            mul += 1
            break
        else:
            a /= mul
            b /= mul
            lst.append(mul)
gcd_ab = reduce((lambda x, y: x * y), lst)
print(gcd_ab)
print(gcd_ab * a * b)
"""
