from collections import deque


que = deque(range(1, int(input()) + 1))

while len(que) != 1:
    que.popleft()
    if len(que) == 1:
        break
    que.append(que.popleft())
print(que.pop())
