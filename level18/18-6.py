from collections import deque
import sys


input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
stack = deque()
result = [-1] * N
for i in range(N):
    while stack:
        if lst[i] > lst[stack[-1]]:
            result[stack.pop()] = lst[i]
        else:
            break
    stack.append(i)

print(*result)


"""
for i, n1 in enumerate(lst):
    stack = []
    for n2 in lst[i + 1 :]:
        if n2 > n1:
            stack.append(n2)
            break

    if not stack:
        print(-1, end=" ")
    else:
        print(stack.pop(0), end=" ")
"""
