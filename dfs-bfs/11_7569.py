from collections import deque


M, N, H = map(int, input().split())
table = [[] for _ in range(H)]
que = deque([])
for i in range(H):
    for j in range(N):
        table[i].append(list(map(int, input().split())))
        for k, tomato in enumerate(table[i][j]):
            if tomato == 1:
                que.append([i, j, k])
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
while que:
    a, b, c = que.popleft()
    for i in range(6):
        x = a + dx[i]
        y = b + dy[i]
        z = c + dz[i]
        if 0 <= x < H and 0 <= y < N and 0 <= z < M and table[x][y][z] == 0:
            que.append([x, y, z])
            table[x][y][z] = table[a][b][c] + 1

result = 0
for matrix in table:
    for row in matrix:
        if 0 in row:
            print(-1)
            exit(0)
        if max(row) > result:
            result = max(row)
print(result - 1)
