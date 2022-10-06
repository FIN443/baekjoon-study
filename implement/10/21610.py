# 마법사 상어와 비바라기
N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
que = []
for i, j in [[N - 1, 1], [N - 1, 2], [N, 1], [N, 2]]:
    que.append([i - 1, j - 1])

move = []
for _ in range(M):
    move.append(list(map(int, input().split())))  # 방향, 이동 횟수

dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 오른쪽
dy = [0, -1, -1, -1, 0, 1, 1, 1]  # 아래

for d_i, s_i in move:
    d_i -= 1
    block_lst = []
    for idx, (y, x) in enumerate(que):
        ny, nx = (y + s_i * (dy[d_i])) % N, (x + s_i * (dx[d_i])) % N
        table[ny][nx] += 1
        que[idx] = [ny, nx]
        block_lst.append([ny, nx])

    while que:
        y, x = que.pop()
        check_cnt = 0
        for i, j in [[y - 1, x - 1], [y - 1, x + 1], [y + 1, x - 1], [y + 1, x + 1]]:
            if 0 <= i < N and 0 <= j < N and table[i][j]:
                check_cnt += 1
        table[y][x] += check_cnt

    for i in range(N):
        for j in range(N):
            if table[i][j] >= 2 and not [i, j] in block_lst:
                que.append([i, j])
                table[i][j] -= 2
result = 0
for row in table:
    result += sum(row)

print(result)
