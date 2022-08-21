# 빈도 정렬
import sys
from collections import Counter

input = sys.stdin.readline
N, C = map(int, input().split())
lst = list(map(int, input().split()))
counter = Counter()
number = []
for i in lst:
    if not i in number:
        number.append(i)
    counter[i] += 1

new_lst = list(counter.items())
new_lst.sort(key=lambda x: (-x[1]))


for k, v in new_lst:
    [print(k, end=" ") for _ in range(v)]
