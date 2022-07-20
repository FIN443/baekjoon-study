import sys


input = sys.stdin.readline
V, E = map(int, input().split())
# 플로이드 와샬 알고리즘
table = [[float("inf") for _ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    table[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]

min_v = float("inf")
for i in range(1, V + 1):
    min_v = min(min_v, table[i][i])

if min_v != float("inf"):
    print(min_v)
else:
    print(-1)
