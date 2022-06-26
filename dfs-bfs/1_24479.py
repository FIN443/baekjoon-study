import sys


def dfs(graph, v, visited):
    global order
    visited[v] = 1
    order_list[v] = order
    order += 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, M, R = map(int, input().split())
visited = [0] * (N + 1)
order = 1
order_list = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

dfs(graph, R, visited)
for i in order_list[1:]:
    print(i)
