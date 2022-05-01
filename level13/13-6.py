from fractions import Fraction

T = int(input())
lst = list(map(int, input().split()))

for n in lst[1:]:
    if lst[0] % n == 0:
        print(f"{lst[0] // n}/1")
    else:
        print(Fraction(lst[0], n))

""" 정석 풀이
import math as m
input()
l = list(map(int, input().split()))
cir = l[0] # 기준
del l[0] # 기준제외
ans = []

for i in l:
  gcd = m.gcd(cir, i) # 약분값
  ans.append(f'{cir//gcd}/{i//gcd}') # 분모, 분자에 최소공배수 나누면 약분

print(*ans)
"""
