import sys


input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

minus = 0
zero = 0
plus = 0


def solution(x, y, N):
    global minus, zero, plus

    check = lst[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != lst[i][j]:
                solution(x, y, N // 3)
                solution(x, y + N // 3, N // 3)
                solution(x, y + (N // 3) * 2, N // 3)

                solution(x + N // 3, y, N // 3)
                solution(x + N // 3, y + N // 3, N // 3)
                solution(x + N // 3, y + (N // 3) * 2, N // 3)

                solution(x + (N // 3) * 2, y, N // 3)
                solution(x + (N // 3) * 2, y + N // 3, N // 3)
                solution(x + (N // 3) * 2, y + (N // 3) * 2, N // 3)
                return

    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1


solution(0, 0, N)
print(minus)
print(zero)
print(plus)
