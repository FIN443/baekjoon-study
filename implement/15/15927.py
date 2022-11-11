# 배열 돌리기 2
N, M, R = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

turns = []
for k in range(min(N, M) // 2):
    turns.append(2 * ((N - (2 * k)) + (M - (2 * k))) - 4)


for k in range(min(N, M) // 2):
    for r in range(R % turns[k]):
        temp = lst[k][k]
        for i in range(1 + k, M - k):
            lst[k][i - 1] = lst[k][i]

        for i in range(1 + k, N - k):
            lst[i - 1][M - 1 - k] = lst[i][M - 1 - k]

        for i in range(1 + k, M - k):
            lst[N - 1 - k][M - i] = lst[N - 1 - k][M - 1 - i]

        for i in range(1 + k, N - k):
            lst[N - i][k] = lst[N - 1 - i][k]

        lst[1 + k][k] = temp

for n in lst:
    print(" ".join(map(str, n)))
