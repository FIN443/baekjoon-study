N = 5
grid = []
for i in range(5):
    data = input()
    grid.append(list(data))
x_cnt = 0
x_pos = []
# 0부터 ~ 12 [ A ~~ L]
visited = [False] * 12
answer = []


def convertAlpha(num):
    if num == 0:
        return "A"
    if num == 1:
        return "B"
    if num == 2:
        return "C"
    if num == 3:
        return "D"
    if num == 4:
        return "E"
    if num == 5:
        return "F"
    if num == 6:
        return "G"
    if num == 7:
        return "H"
    if num == 8:
        return "I"
    if num == 9:
        return "J"
    if num == 10:
        return "K"
    if num == 11:
        return "L"


def convertNum(alpha):
    if alpha == "A":
        return 0
    if alpha == "B":
        return 1
    if alpha == "C":
        return 2
    if alpha == "D":
        return 3
    if alpha == "E":
        return 4
    if alpha == "F":
        return 5
    if alpha == "G":
        return 6
    if alpha == "H":
        return 7
    if alpha == "I":
        return 8
    if alpha == "J":
        return 9
    if alpha == "K":
        return 10
    if alpha == "L":
        return 11


for i in range(5):
    for j in range(9):
        if grid[i][j] == "x":
            x_cnt += 1
            x_pos.append((i, j))
        if grid[i][j] != "x" and grid[i][j] != ".":
            visited[convertNum(grid[i][j])] = True

combi = []


def is_ok(tmp):
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


# x의 순열을 뽑는다.
def dfs(pick):
    if pick == x_cnt:
        if is_ok(apply_perm(combi)):
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


dfs(0)
