from collections import deque
import sys


input = sys.stdin.readline
N = int(input())


que = deque()
for _ in range(N):
    order = input().rstrip()
    if order == "size":
        print(len(que))
    elif order == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif order == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif order == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
    elif order == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    else:
        _, num = order.split()
        que.append(num)
