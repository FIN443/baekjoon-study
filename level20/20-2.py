import sys


input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().rstrip())))


def solution(x, y, N):
    black = lst[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if black != lst[i][j]:
                black = -1
                break
    if black == -1:
        print("(", end="")
        solution(x, y, N // 2)
        solution(x, y + N // 2, N // 2)
        solution(x + N // 2, y, N // 2)
        solution(x + N // 2, y + N // 2, N // 2)
        print(")", end="")
    elif black == 1:
        print(1, end="")
    else:
        print(0, end="")


solution(0, 0, N)
