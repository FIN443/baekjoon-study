from collections import deque

n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
que = deque()
que.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while que:
    s = que.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s - 1 < 100001 and visited[s - 1] == -1:
        visited[s - 1] = visited[s] + 1
        que.append(s - 1)
    if 0 < s * 2 < 100001 and visited[s * 2] == -1:
        visited[s * 2] = visited[s]
        que.appendleft(s * 2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s + 1 < 100001 and visited[s + 1] == -1:
        visited[s + 1] = visited[s] + 1
        que.append(s + 1)


""" 
N, K = map(int, input().split())
table = [-1 for _ in range(100001)]
table[N] = 0
que = deque([N])
while que:
    num = que.popleft()
    if num == K:
        print(table[num])
        break
    for idx, calc in enumerate([num - 1, num + 1, num * 2]):
        if 0 <= calc <= 100000 and table[calc] == -1: # 텔포 범위에 0을 넣으면 무한진행됨
            if idx != 2:
                table[calc] = table[num] + 1
                que.append(calc)
            else:
                table[calc] = table[num]
                que.appendleft(calc) 
"""
