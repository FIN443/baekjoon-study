from collections import deque


N, M = map(int, input().split())
move = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    move[a] = b
table = [0 for _ in range(101)]

dx = [1, 2, 3, 4, 5, 6]

que = deque([1])
while que:
    a = que.popleft()
    for i in range(6):
        x = a + dx[i]
        if x in move.keys():
            x = move[x]
        if 0 < x <= 100 and table[x] == 0:
            table[x] = table[a] + 1
            que.append(x)

print(table[-1])
