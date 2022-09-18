# 톱니바퀴
from collections import deque

cog = []
for _ in range(4):
    cog.append(deque(list(input())))
K = int(input())
for _ in range(K):
    cog_id, direction = map(int, input().split())
    cog_id -= 1
    cog_d = [0 for _ in range(4)]
    cog_d[cog_id] = direction
    if cog_id == 0:
        if cog[cog_id][2] != cog[cog_id + 1][-2]:
            cog_d[cog_id + 1] = -direction
        if cog_d[cog_id + 1] != 0 and cog[cog_id + 1][2] != cog[cog_id + 2][-2]:
            cog_d[cog_id + 2] = direction
        if cog_d[cog_id + 2] != 0 and cog[cog_id + 2][2] != cog[cog_id + 3][-2]:
            cog_d[cog_id + 3] = -direction
    elif cog_id == 1:
        if cog[cog_id][-2] != cog[cog_id - 1][2]:
            cog_d[cog_id - 1] = -direction
        if cog[cog_id][2] != cog[cog_id + 1][-2]:
            cog_d[cog_id + 1] = -direction
        if cog_d[cog_id + 1] != 0 and cog[cog_id + 1][2] != cog[cog_id + 2][-2]:
            cog_d[cog_id + 2] = direction
    elif cog_id == 2:
        if cog[cog_id][2] != cog[cog_id + 1][-2]:
            cog_d[cog_id + 1] = -direction
        if cog[cog_id][-2] != cog[cog_id - 1][2]:
            cog_d[cog_id - 1] = -direction
        if cog_d[cog_id - 1] != 0 and cog[cog_id - 1][-2] != cog[cog_id - 2][2]:
            cog_d[cog_id - 2] = direction
    elif cog_id == 3:
        if cog[cog_id][-2] != cog[cog_id - 1][2]:
            cog_d[cog_id - 1] = -direction
        if cog_d[cog_id - 1] != 0 and cog[cog_id - 1][-2] != cog[cog_id - 2][2]:
            cog_d[cog_id - 2] = direction
        if cog_d[cog_id - 2] != 0 and cog[cog_id - 2][-2] != cog[cog_id - 3][2]:
            cog_d[cog_id - 3] = -direction

    for i, d in enumerate(cog_d):
        if d != 0:
            cog[i].rotate(d)

result = 0
for i, deq in enumerate(cog):
    if deq.popleft() == "1":
        result += 2**i

print(result)
