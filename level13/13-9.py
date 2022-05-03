from math import comb


T = int(input())
lst = []
for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        lst.append(comb(a, b))
    else:
        lst.append(comb(b, a))

[print(i) for i in lst]
