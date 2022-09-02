# 스티커
import sys


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))

    if N == 1:
        print(max(line1[0], line2[0]))
    else:
        line1[1] += line2[0]
        line2[1] += line1[0]
        for i in range(2, N):
            line1[i] += max(line2[i - 1], line2[i - 2])
            line2[i] += max(line1[i - 1], line1[i - 2])

        print(max(line1[-1], line2[-1]))
