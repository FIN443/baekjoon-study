from math import gcd


T = int(input())
lst = []
for _ in range(T):
    a, b = map(int, input().split())
    lst.append(a * b // gcd(a, b))

[print(i) for i in lst]
