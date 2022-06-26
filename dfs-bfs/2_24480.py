import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(graph, v, visited):
    global order
    visited[v] = True
    order_list[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort(reverse=True)

visited = [False] * (N + 1)
order_list = [0] * (N + 1)
order = 1

dfs(graph, R, visited)
for i in order_list[1:]:
    print(i)
