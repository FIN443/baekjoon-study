# 주사위 쌓기
N = int(input())
dices = []

for _ in range(N):
    dices.append(list(map(int, input().split())))


def solution(dice, target):
    global result

    idx = dice.index(target)
    if idx == 0 or idx == 5:
        result += max(dice[1], dice[2], dice[3], dice[4])
        if idx == 0:
            target = dice[5]
        else:
            target = dice[0]
    elif idx == 1 or idx == 3:
        result += max(dice[0], dice[2], dice[4], dice[5])
        if idx == 1:
            target = dice[3]
        else:
            target = dice[1]
    elif idx == 2 or idx == 4:
        result += max(dice[0], dice[1], dice[3], dice[5])
        if idx == 2:
            target = dice[4]
        else:
            target = dice[2]

    return target


results = []
for i in range(6):
    result = 0
    target = dices[0][i]
    for dice in dices:
        target = solution(dice, target)

    results.append(result)

print(max(results))
