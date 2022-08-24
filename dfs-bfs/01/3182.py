# 한동이는 공부가 하기 싫어!
from collections import deque
import sys


input = sys.stdin.readline
N = int(input())
graph = []

for i in range(N):
    graph.append(int(input()))

result = []
for i in range(N):
    que = deque([i + 1])
    visited = [False for _ in range(N)]
    count = 0
    while que:
        v = que.popleft()
        if visited[v - 1]:
            continue
        visited[v - 1] = True
        count += 1
        que.append(graph[v - 1])
    result.append([i + 1, count])

result.sort(key=lambda x: (-x[1], x[0]))
print(result[0][0])
