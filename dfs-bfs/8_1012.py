from collections import deque
import sys

sys.setrecursionlimit(10**7)


def dfs(i, j):
    if table[i][j] != 1 or visited[i][j]:
        return

    visited[i][j] = True
    if i != 0:
        dfs(i - 1, j)
    if j != 0:
        dfs(i, j - 1)
    if i != len(table) - 1:
        dfs(i + 1, j)
    if j != len(table[0]) - 1:
        dfs(i, j + 1)


def bfs(i, j):
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        if table[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            if x != 0:
                que.append((x - 1, y))
            if y != 0:
                que.append((x, y - 1))
            if x != len(table) - 1:
                que.append((x + 1, y))
            if y != len(table[0]) - 1:
                que.append((x, y + 1))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    table = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        table[y][x] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1 and not visited[i][j]:
                # dfs(i, j)
                bfs(i, j)
                count += 1
    print(count)
