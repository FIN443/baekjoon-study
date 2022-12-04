def convertAlpha(num):
    return chr(num + 65)


def convertNum(alpha):
    return ord(alpha) - 65


def solution(tmp):
    now_c = 4
    val = 0
    for i in range(4):
        val += convertNum(tmp[i][now_c])
        now_c -= 1
    if val + 4 != 26:
        return False

    val = 0
    for i in range(1, 9, 2):
        val += convertNum(tmp[3][i])
    if val + 4 != 26:
        return False

    val = 0
    now_c = 7
    for i in range(3, -1, -1):
        val += convertNum(tmp[i][now_c])
        now_c -= 1
    if val + 4 != 26:
        return False

    val = 0
    now_c = 1

    for i in range(1, 5):
        val += convertNum(tmp[i][now_c])
        now_c += 1
    if val + 4 != 26:
        return False

    val = 0
    now_c = 4
    for i in range(4, 0, -1):
        val += convertNum(tmp[i][now_c])
        now_c += 1
    if val + 4 != 26:
        return False

    val = 0
    for i in range(7, 0, -2):
        val += convertNum(tmp[1][i])
    if val + 4 != 26:
        return False

    ret = ""
    for i in tmp:
        ret += "".join(i)
    answer.append(ret)

    return True


def apply_perm(combi):
    tmp = grid
    for idx, pos in enumerate(x_pos):
        tmp[pos[0]][pos[1]] = str(convertAlpha(combi[idx]))
    return tmp


def dfs(pick):
    if pick == x_cnt:
        if solution(apply_perm(combi)):
            for i in range(0, 45, 9):
                print(answer[0][i : i + 9])
            exit(0)
        return
    for i in range(12):
        if not visited[i]:
            visited[i] = True
            combi.append(i)
            dfs(pick + 1)
            visited[i] = False
            combi.pop()


N = 5
grid = []

for i in range(5):
    data = input()
    grid.append(list(data))
x_cnt = 0
x_pos = []
visited = [False] * 12
answer = []


for i in range(5):
    for j in range(9):
        if grid[i][j] == "x":
            x_cnt += 1
            x_pos.append((i, j))
        if grid[i][j] != "x" and grid[i][j] != ".":
            visited[convertNum(grid[i][j])] = True

combi = []
dfs(0)
