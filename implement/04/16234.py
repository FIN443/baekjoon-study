# 인구 이동
from collections import deque
import sys


input = sys.stdin.readline
N, L, R = map(int, input().split())
result = 0
table = []
for _ in range(N):
    lst = list(map(int, input().split()))
    table.append(lst)

flag = 1  # 처음은 무조건 수행
while flag:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0  # 탈출 조건
    group = 0
    count = []
    total = []
    total_pos = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                que = deque([[i, j]])
                count.append(1)
                total.append(table[i][j])
                total_pos.append([[i, j]])
                while que:
                    x, y = que.popleft()
                    for dx, dy in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and L <= abs(table[x][y] - table[dx][dy]) <= R:
                            visited[dx][dy] = 1
                            que.append([dx, dy])
                            total[group] += table[dx][dy]
                            total_pos[group].append([dx, dy])
                            count[group] += 1
                            flag = 1
                group += 1

    while flag and count and total and total_pos:
        v = total.pop() // count.pop()
        pos_lst = total_pos.pop()
        for x, y in pos_lst:
            table[x][y] = v

    if flag:
        result += 1

print(result)
