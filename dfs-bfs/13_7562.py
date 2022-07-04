from collections import deque


T = int(input())
for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    table = [[0 for _ in range(I)] for _ in range(I)]
    que = deque([start])
    while que:
        a, b = que.popleft()
        if a == end[0] and b == end[1]:
            print(table[a][b])
            break
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < I and 0 <= y < I and table[x][y] == 0:
                table[x][y] = table[a][b] + 1
                que.append([x, y])
