from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, start, visited):
    global order
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        order_list[v] = order
        order += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

visited = [False] * (N + 1)
order_list = [0] * (N + 1)
order = 1

bfs(graph, R, visited)

for i in order_list[1:]:
    print(i)
