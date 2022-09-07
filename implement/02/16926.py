# 배열 돌리기 1
import sys


input = sys.stdin.readline
N, M, R = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(min(N // 2, M // 2)):
    for _ in range(R):
        temp = table[i][i]
        for j in range(1 + i, M - i):
            table[i][j - 1] = table[i][j]

        for j in range(1 + i, N - i):
            table[j - 1][M - 1 - i] = table[j][M - 1 - i]

        for j in range(M - 1 - i, i, -1):
            table[N - 1 - i][j] = table[N - 1 - i][j - 1]

        for j in range(N - 1 - i, i, -1):
            table[j][i] = table[j - 1][i]
        table[i + 1][i] = temp

for i in range(N):
    print(*table[i], sep=" ")
