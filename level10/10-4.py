# 체스판
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 8*8 크기는 아무데서나 골라도 된다.
# 가로
N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(input())
results = []
for i in range(N - 7):
    for j in range(M - 7):
        result1 = 0
        result2 = 0
        for m in range(i, i + 8):
            for n in range(j, j + 8):
                if (m + n) % 2 == 0:
                    if lst[m][n] != "W":
                        result1 += 1
                    if lst[m][n] != "B":
                        result2 += 1
                else:
                    if lst[m][n] != "B":
                        result1 += 1
                    if lst[m][n] != "W":
                        result2 += 1
        results.append(min(result1, result2))

print(min(results))

""" 다른 답안
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
cnt_board = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i+j)%2:
            if board[i][j] == 'B':
                cnt_board[i][j] = 1
        else:
            if board[i][j] == 'W':
                cnt_board[i][j] = 1

res = 64
for i in range(N-7):
    for j in range(M-7):
        total = 0
        for k in range(8):
            total += cnt_board[i+k][j:j+8].count(1)
        res = min(res, total, 64-total)
print(res)
"""
