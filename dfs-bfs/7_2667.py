from collections import deque


N = int(input())
table = []
for _ in range(N):
    table.append(input())
visited = [[False for _ in range(N)] for _ in range(N)]


def dfs(table, visited, x, y):
    if table[x][y] != "1" or visited[x][y]:
        return
    global area
    visited[x][y] = True
    area += 1
    if x != 0:
        dfs(table, visited, x - 1, y)
    if x != len(table) - 1:
        dfs(table, visited, x + 1, y)
    if y != 0:
        dfs(table, visited, x, y - 1)
    if y != len(table[0]) - 1:
        dfs(table, visited, x, y + 1)


def bfs(table, visited, x, y):
    global area
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        if table[x][y] == "1" and not visited[x][y]:
            visited[x][y] = True
            area += 1
            if x != 0:
                que.append((x - 1, y))
            if x != len(table) - 1:
                que.append((x + 1, y))
            if y != 0:
                que.append((x, y - 1))
            if y != len(table[0]) - 1:
                que.append((x, y + 1))


count = 0
lst = []
for i in range(N):
    for j in range(N):
        if table[i][j] == "1" and not visited[i][j]:
            area = 0
            # dfs(table, visited, i, j)
            bfs(table, visited, i, j)
            lst.append(area)
            count += 1

print(count)
lst.sort()
print(*lst, sep="\n")
