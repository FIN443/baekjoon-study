# 봄버맨
from collections import deque


R, C, N = map(int, input().split())
table = [list(input()) for _ in range(R)]
count = 1

while count < N:
    bomb = deque()
    # 폭탄 위치 정보
    for i in range(R):
        for j in range(C):
            if table[i][j] == 'O':
                bomb.append([i, j])
                
    # 폭탄 설치
    for i in range(R):
        for j in range(C):
            if table[i][j] != "O":
                table[i][j] = "O" 
    count += 1
    if count == N:
        break
    
    # 폭탄 터뜨림
    while bomb:
        a, b = bomb.popleft()
        table[a][b] = "."
        for x, y in [[a-1, b], [a+1, b], [a, b-1], [a, b+1]]:
            if 0 <= x < R and 0 <= y < C and table[x][y] == "O":
                table[x][y] = "."
    count += 1
    
    
for row in table:
    print("".join(row))