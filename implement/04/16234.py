# 인구 이동
from collections import deque
import sys


input = sys.stdin.readline
N, L, R = map(int, input().split())
result = 0
table = []
for _ in range(N):
    lst = list(map(int, input().split()))
    table.append(lst)

flag = 1  # 처음은 무조건 수행
while flag:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0  # 탈출 조건
    group = 0  # 그룹 지정
    count = []  # 그룹 내 나라 수
    total = []  # 그룹 total
    total_pos = []  # 그룹 내 나라들 좌표
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                que = deque([[i, j]])
                count.append(1)
                total.append(table[i][j])
                total_pos.append([[i, j]])
                while que:
                    x, y = que.popleft()
                    for dx, dy in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and L <= abs(table[x][y] - table[dx][dy]) <= R:
                            visited[dx][dy] = 1
                            que.append([dx, dy])
                            total[group] += table[dx][dy]
                            total_pos[group].append([dx, dy])
                            count[group] += 1
                            flag = 1
                group += 1

    while flag and count and total and total_pos:
        v = total.pop() // count.pop()
        pos_lst = total_pos.pop()
        for x, y in pos_lst:
            table[x][y] = v

    if flag:
        result += 1

print(result)


"""
import sys
import math
from collections import deque

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, sys.stdin.readline().split())  # n*n, 인구차이 l명 이상, r명 이하

arr = list()
a_list = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    count = arr[i][j]   # 총 연합된 국가 수 
        # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기 
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기 
                union.append((nx, ny))
                visit[nx][ny] = True
                dq.append((nx, ny))
                count += arr[nx][ny]
    # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산  
    for x, y in union:
        arr[x][y] = math.floor(count / len(union))

    return len(union)

result = 0    # 인구 이동이 발생하는 일수 
while True:   # 1. 인구 이동이 없을 때까지 반복 
    visit = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동 존재 유무 플래그 
    # 2. 모든 곳을 bfs로 방문하여 연합 진행 
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:   # 3. 지금까지 인구 이동이 없는 경우, 그만 
        break
    result += 1

print(result)
"""
