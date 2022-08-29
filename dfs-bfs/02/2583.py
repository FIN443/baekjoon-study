# 영역 구하기
import sys
from collections import deque

input = sys.stdin.readline
M, N, K = map(int, input().split())
table = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            table[y][x] = 1

result = 0
results = []
for i in range(M):
    for j in range(N):
        if not table[i][j]:
            result += 1
            que = deque([[i, j]])
            count = 0
            while que:
                a, b = que.popleft()
                if table[a][b]:
                    continue
                table[a][b] = 1
                count += 1
                for x, y in [[a - 1, b], [a + 1, b], [a, b - 1], [a, b + 1]]:
                    if 0 <= x < M and 0 <= y < N and not table[x][y]:
                        que.append([x, y])
            results.append(count)

results.sort()

print(result)
print(*results)
