table = []
blank = []
for _ in range(9):
    table.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if table[i][j] == 0:
            blank.append((i, j))


def checkRow(x, a):
    for i in range(9):
        if a == table[x][i]:
            return False
    return True


def checkCol(y, a):
    for i in range(9):
        if a == table[i][y]:
            return False
    return True


def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == table[nx + i][ny + j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*table[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            table[x][y] = i
            dfs(idx + 1)
            table[x][y] = 0


dfs(0)
