from collections import deque


M, N = map(int, input().split())
table = []
que = deque([])
for i in range(N):
    table.append(list(map(int, input().split())))
    for j, tomato in enumerate(table[i]):
        if tomato == 1:
            que.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while que:
    a, b = que.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and table[x][y] == 0:
            que.append([x, y])
            table[x][y] = table[a][b] + 1

result = 0
for row in table:
    if 0 in row:
        result = 0
        break
    if max(row) > result:
        result = max(row)
print(result - 1)
