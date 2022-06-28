from collections import deque


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()


def dfs(graph, v, visited):
    visited[v] = True
    dfs_list.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs_list = []
visited = [False] * (N + 1)
dfs(graph, V, visited)
print(*dfs_list, sep=" ", end="\n")


def bfs(graph, start, visited):
    visited[start] = True
    bfs_list.append(start)
    que = deque([start])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                bfs_list.append(i)


bfs_list = []
visited = [False] * (N + 1)
bfs(graph, V, visited)
print(*bfs_list, sep=" ", end="\n")
