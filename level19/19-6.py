from collections import deque


N, _ = map(int, input().split())
pick_pos = list(map(int, input().split()))

que = deque(range(1, N + 1))

count = 0
for i in pick_pos:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) <= len(que) // 2:
                # 맨앞 아이템을 오른쪽 끝으로 옮겨야 함
                while que[0] != i:
                    que.append(que.popleft())
                    count += 1
            else:
                # 반대로
                while que[0] != i:
                    que.appendleft(que.pop())
                    count += 1
print(count)
