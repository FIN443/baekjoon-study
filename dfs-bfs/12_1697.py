from collections import deque


N, K = map(int, input().split())

table = [0 for _ in range(100001)]
que = deque([N])
while que:
    num = que.popleft()
    if num == K:
        print(table[num])
        break
    for calc in (num - 1, num + 1, num * 2):
        if 0 <= calc <= 100000 and not table[calc]:
            table[calc] = table[num] + 1
            que.append(calc)


""" dfs 풀이(리스트 터짐)
que = deque([[N, 0]])
while que:
    num, count = que.pop()
    if num == K:
        result.append(count)
        
    if num > 0 and count + 1 < visited[num - 1]:
        visited[num - 1] = count + 1
        que.append([num - 1, count + 1])
    if num <= K // 2 and count + 1 < visited[num * 2]:
        visited[num * 2] = count + 1
        que.append([num * 2, count + 1])
    if count + 1 < visited[num + 1]:
        visited[num + 1] = count + 1
        que.append([num + 1, count + 1])
"""
