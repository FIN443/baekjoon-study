# 사탕 게임
N = int(input())
table = [[] for _ in range(N)]
for i in range(N):
    table[i] = list(input())
result = 0


def row():
    global result

    for k in range(N):
        count = 1
        for l in range(N - 1):
            if table[k][l] == table[k][l + 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1


def column():
    global result

    for k in range(N):
        count = 1
        for l in range(N - 1):
            if table[l][k] == table[l + 1][k]:
                count += 1
                result = max(result, count)
            else:
                count = 1


for i in range(N):
    for j in range(N - 1):
        if table[i][j] != table[i][j + 1]:
            # 좌우로 swap
            table[i][j], table[i][j + 1] = table[i][j + 1], table[i][j]
            # 탐색
            row()
            column()
            # 원래대로
            table[i][j], table[i][j + 1] = table[i][j + 1], table[i][j]
        if table[j][i] != table[j + 1][i]:
            # 상하로 swap
            table[j][i], table[j + 1][i] = table[j + 1][i], table[j][i]
            # 탐색
            row()
            column()
            # 원래대로
            table[j][i], table[j + 1][i] = table[j + 1][i], table[j][i]


print(result)
