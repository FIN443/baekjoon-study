# 바닥 장식
from collections import deque


N, M = map(int, input().split())
table = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    table.append(input())

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            count += 1
            que = deque([[i, j]])
            while que:
                a, b = que.popleft()
                if visited[a][b]:
                    continue
                visited[a][b] = True
                if table[a][b] == "-":
                    for y in [b - 1, b + 1]:
                        if 0 <= y and y < M and table[a][y] == "-" and not visited[a][y]:
                            que.append([a, y])
                elif table[a][b] == "|":
                    for x in [a - 1, a + 1]:
                        if 0 <= x and x < N and table[x][b] == "|" and not visited[x][b]:
                            que.append([x, b])

print(count)
