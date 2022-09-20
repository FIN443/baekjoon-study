# 컨베이어 벨트 위의 로봇
from collections import deque


N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque(0 for _ in range(N))
result = 0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    if sum(robot):
        for i in range(N - 2, -1, -1):
            if robot[i] and not robot[i + 1] and belt[i + 1]:
                belt[i + 1] -= 1
                robot[i + 1], robot[i] = robot[i], 0
        robot[-1] = 0

    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1

    result += 1

    if belt.count(0) >= K:
        break

print(result)
