import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        # 방문한 곳인데, 그룹이 동일하면 False
        elif visited[i] == visited[v]:
            return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipatite = True

    for i in range(1, V + 1):
        if visited[i] == 0:
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print("YES" if bipatite else "NO")
