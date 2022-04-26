# 리스트안에서 자신보다 작은 element의 갯수
import sys


T = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().strip().split()))
lst2 = sorted(list(set(lst)))
D = {lst2[i]: i for i in range(len(lst2))}

for i in lst:
    print(D[i], end=" ")

""" 원래 했던거 (시간초과)
T = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().strip().split()))


for num in lst:
    count = 0
    for i in lst:
        if num > i:
            count += 1
    print(count, end=" ")
"""
