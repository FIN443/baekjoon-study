# 로봇 시뮬레이션
A, B = map(int, input().split())
N, M = map(int, input().split())
table = [[0 for _ in range(A)] for _ in range(B)]


def convert(x):
    if x.isdigit():
        return int(x)
    else:
        return x


di_book = {
    "N": 0,
    "W": 1,
    "S": 2,
    "E": 3,
}
di_reverse = {
    0: "N",
    1: "W",
    2: "S",
    3: "E",
}
di = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # x, y

robots = []
for _ in range(N):
    x, y, c = map(convert, input().split())
    robots.append([x - 1, y - 1])  # x, y
    table[y - 1][x - 1] = c

for _ in range(M):
    r_num, order, move = map(convert, input().split())
    x, y = robots[r_num - 1]

    if order == "F":  # forward
        for i in range(1, move + 1):
            dx, dy = x + di[di_book[table[y][x]]][0], y + di[di_book[table[y][x]]][1]
            if 0 <= dx < A and 0 <= dy < B and table[dy][dx] == 0:
                table[dy][dx] = table[y][x]
                table[y][x] = 0
                robots[r_num - 1] = [dx, dy]
                x, y = dx, dy
                continue
            elif dx < 0 or A <= dx or dy < 0 or B <= dy:
                print(f"Robot {r_num} crashes into the wall")
            else:
                crash = robots.index([dx, dy]) + 1
                print(f"Robot {r_num} crashes into robot {crash}")
            exit()

    elif order == "L":  # left
        table[y][x] = di_reverse[(di_book[table[y][x]] + move) % 4]

    elif order == "R":  # right
        table[y][x] = di_reverse[(di_book[table[y][x]] - move) % 4]

print("OK")
