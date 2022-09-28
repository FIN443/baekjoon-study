# 경쟁적 전염
from collections import deque


N, K = map(int, input().split())
table = []
que = []
for i in range(N):
    row = []
    for j, v in enumerate(map(int, input().split())):
        if v != 0:
            que.append([i, j, v, 0])  # [x, y, kind, day]
        row.append(v)
    table.append(row)
S, A, B = map(int, input().split())

que.sort(key=lambda x: x[2])
que = deque(que)
while que:
    x, y, kind, day = que.popleft()
    if day == S:
        break
    for dx, dy in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        if 0 <= dx < N and 0 <= dy < N and not table[dx][dy]:
            table[dx][dy] = kind
            que.append([dx, dy, kind, day + 1])


print(table[A - 1][B - 1])
