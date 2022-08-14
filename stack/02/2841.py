# 외계인의 기타 연주
import sys


input = sys.stdin.readline
N, P = map(int, input().split())
lines = [[] for _ in range(6)]
count = 0
for _ in range(N):
    l, f = map(int, input().split())
    if not lines[l - 1] or f > lines[l - 1][-1]:
        lines[l - 1].append(f)
        count += 1
    else:
        while lines[l - 1] and lines[l - 1][-1] > f:
            lines[l - 1].pop()
            count += 1
        if lines[l - 1] and lines[l - 1][-1] == f:
            continue
        lines[l - 1].append(f)
        count += 1

print(count)
