# 죽음의 게임
from collections import deque
import sys


input = sys.stdin.readline
N, K = map(int, input().split())
graph = []
visited = [False for _ in range(N)]
for i in range(N):
    graph.append(int(input()))

count = 0
que = deque([0])
while que:
    cur_v = que.popleft()
    count += 1
    if visited[cur_v]:
        print(-1)
        exit()
    elif graph[cur_v] == K:
        print(count)
        exit()
    visited[cur_v] = True
    que.append(graph[cur_v])
