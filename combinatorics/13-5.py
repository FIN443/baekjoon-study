# 연속하는 두 요소 차들의 최소공배수

import math

T = int(input())
lst = []
gcd = 0
for i in range(T):
    lst.append(int(input()))
    if i == 1:
        gcd = abs(lst[1] - lst[0])
    gcd = math.gcd(abs(lst[i] - lst[i - 1]), gcd)
cond = int(gcd**0.5)

results = []
for i in range(2, cond + 1):
    if gcd % i == 0:
        results.append(i)
        results.append(gcd // i)
results.append(gcd)
results = list(set(results))
results.sort()
[print(i, end=" ") for i in results]

""" 시간초과
T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

for mul in range(2, min(lst) + 1):
    lst2 = [n % mul for n in lst]
    if len(set(lst2)) == 1:
        print(mul, end=" ")
"""

""" 모든 차들의 공배수를 안 구함
T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

lst.sort(reverse=True)
lst2 = [i - j for i, j in zip(lst, lst[1:])]

m = min(lst2)

divisors = []

for i in range(1, m + 1):
    if m % i == 0:
        divisors.append(i)

[print(i, end=" ") for i in divisors[1:]]
"""
