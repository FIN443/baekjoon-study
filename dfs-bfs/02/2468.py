# 안전 영역
from collections import deque


N = int(input())
table = [[] for _ in range(N)]


for i in range(N):
    table[i] = list(map(int, input().split()))

result = 0
for K in range(0, 101):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and table[i][j] > K:
                count += 1
                que = deque([[i, j]])
                while que:
                    a, b = que.popleft()
                    if visited[a][b]:
                        continue
                    visited[a][b] = True
                    for x, y in [[a - 1, b], [a + 1, b], [a, b - 1], [a, b + 1]]:
                        if 0 <= x < N and 0 <= y < N and not visited[x][y] and table[x][y] > K:
                            que.append([x, y])

    result = max(result, count)

print(result)
