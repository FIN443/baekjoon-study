# 경로 찾기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
table = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for idx, v in enumerate(map(int, input().split())):
        if v == 1:
            graph[i].append(idx)

for i in range(N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    que = deque([i])
    while que:
        cur_v = que.popleft()
        for to_v in graph[cur_v]:
            if visited[cur_v][to_v]:
                continue
            visited[cur_v][to_v] = True
            table[i][to_v] = 1
            table[cur_v][to_v] = 1
            que.append(to_v)

for row in table:
    print(*row)
