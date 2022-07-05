from collections import deque

# 함수로 안하니까 시간 초과남
def bfs(x, y, z):
    que = deque([[x, y, z]])
    while que:
        a, b, w = que.popleft()
        if a == N - 1 and b == M - 1:
            return visited[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if table[x][y] == 1 and w == 0:
                    visited[x][y][1] = visited[a][b][0] + 1
                    que.append([x, y, 1])
                elif table[x][y] == 0 and visited[x][y][w] == 0:
                    visited[x][y][w] = visited[a][b][w] + 1
                    que.append([x, y, w])
    return -1


N, M = map(int, input().split())
table = []
for i in range(N):
    table.append(list(map(int, input())))
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0, 0))


""" 시간 초과
from collections import deque
from copy import deepcopy


N, M = map(int, input().split())
table = []
walls = []
for i in range(N):
    table.append(list(map(int, input())))
    for j in range(M):
        if table[i][j] == 1:
            table[i][j] = -1
            walls.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
table[0][0] = 1
results = []
for pos in walls:
    distance = deepcopy(table)
    distance[pos[0]][pos[1]] = 0
    que = deque([[0, 0]])
    while que:
        a, b = que.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and distance[x][y] == 0:
                que.append([x, y])
                distance[x][y] = distance[a][b] + 1

    if distance[N - 1][M - 1] != 0:
        results.append(distance[N - 1][M - 1])

if results:
    print(min(results))
else:
    print(-1)
 """
