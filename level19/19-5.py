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
    elif order == "pop_back":
        if que:
            print(que.pop())
        else:
            print(-1)
    elif order == "pop_front":
        if que:
            print(que.popleft())
        else:
            print(-1)
    else:
        pos, num = order.split()
        if pos == "push_back":
            que.append(num)
        else:
            que.appendleft(num)
