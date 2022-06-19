from collections import deque


N, K = map(int, input().split())
que = deque(range(1, N + 1))

result = []
count = 0
while que:
    count += 1
    if count == K:
        result.append(que.popleft())
        count = 0
    else:
        que.append(que.popleft())
print("<", end="")
print(*result, sep=", ", end="")
print(">")
""" flow
1(front) 2 3 4 5 6 7 => []

4(front) 5 6 7 1 2 => [3]

7(front) 1 2 4 5 => [3, 6]

4(front) 5 7 1 => [3, 6, 2]

1(front) 4 5 => [3, 6, 2, 7]

1(front) 4 => [3, 6, 2, 7, 5]

4(front) => [3, 6, 2, 7, 5, 1]

=> [3, 6, 2, 7, 5, 1, 4]
"""
