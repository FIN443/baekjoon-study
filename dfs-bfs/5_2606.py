N = int(input())
M = int(input())


def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
dfs(graph, 1, visited)

print(count)
