from collections import deque

N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(input()))
table[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
que = deque([(0, 0)])
while que:
    a, b = que.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and table[x][y] == "1":
            que.append([x, y])
            table[x][y] = table[a][b] + 1
print(table[N - 1][M - 1])
