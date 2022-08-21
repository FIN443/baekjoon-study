# 파일 정리
import sys
from collections import Counter


input = sys.stdin.readline
N = int(input())
counter = Counter()
for _ in range(N):
    front, back = input().rstrip().split(".")
    counter[back] += 1

new_lst = list(counter.items())
new_lst.sort(key=lambda x: x[0])

for k, v in new_lst:
    print(k, v)
