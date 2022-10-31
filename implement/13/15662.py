# 톱니바퀴 (2)
from collections import deque


def set_cog_move(cog):
    cog_move = [False for _ in range(T - 1)]
    for i in range(T - 1):
        if cog[i][2] == cog[i + 1][-2]:
            cog_move[i] = True
    return cog_move


def rotate(cog, di):
    if di == 1:
        cog.rotate(1)
    else:
        cog.rotate(-1)


cogs = []
T = int(input())
for _ in range(T):
    cogs.append(deque(list(input())))
K = int(input())
for _ in range(K):
    cog_id, di = map(int, input().split())
    cog_move = set_cog_move(cogs)

    rotate(cogs[cog_id - 1], di)

    temp_di = -di
    right = cog_id - 1
    while right <= T - 2:
        if not cog_move[right]:
            rotate(cogs[right + 1], temp_di)
        else:
            break
        temp_di = -temp_di
        right += 1

    left = cog_id - 2
    temp_di = -di
    while left >= 0:
        if not cog_move[left]:
            rotate(cogs[left], temp_di)
        else:
            break
        temp_di = -temp_di
        left -= 1

count = 0
for cog in cogs:
    if cog[0] == "1":
        count += 1

print(count)
