# 수 찾기
from collections import Counter


N = int(input())
lst = Counter(map(int, input().split()))
M = int(input())
check = map(int, input().split())

for i in check:
    if lst[i]:
        print(1)
    else:
        print(0)
