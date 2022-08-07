# 프린터 큐
from collections import deque


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    que = deque()
    for idx, i in enumerate(lst):
        que.append((idx, i))
    count = 1
    while que:
        idx, p = que.popleft()
        if que and max(que, key=lambda x: x[1])[1] > p:
            que.append((idx, p))
        elif idx == M:
            print(count)
            break
        else:
            count += 1
