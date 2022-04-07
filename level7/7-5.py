# T = 테스트 케이스
# H = 층
# W = 방
# N = 몇번쨰 손님?

import math


def solution():
    H, W, N = map(int, input().split())
    room = math.ceil(N / H)
    if N % H == 0:
        layer = H * 100
    else:
        layer = (N % H) * 100
    return layer + room


T = int(input())
results = []
for _ in range(T):
    results.append(solution())
print(*results, sep="\n")
