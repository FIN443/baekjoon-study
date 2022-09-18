# 로봇 청소기
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# d는 0, 3, 2, 1 방향으로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[r][c] = 1
result = 1
turn = 0

while True:
    d = (d - 1) % 4
    nx = r + dx[d]
    ny = c + dy[d]
    if visited[nx][ny] == 0 and table[nx][ny] == 0:
        visited[nx][ny] = 1
        result += 1
        r, c = nx, ny
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if table[nx][ny] == 0:
            r, c = nx, ny
        else:
            break
        turn = 0

print(result)

"""
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# d는 0, 3, 2, 1 방향으로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1

while True:
    cond = True
    for i in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                cond = False
                break

    if cond:
        if table[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]
"""
