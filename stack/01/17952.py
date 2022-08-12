# 과제는 끝나지 않아!
import sys


input = sys.stdin.readline
N = int(input())
result = 0
task_time = []
task_score = []
for _ in range(N):
    lst = list(map(int, input().split()))
    if len(lst) > 1:
        _, score, time = lst
        if time - 1 == 0:
            result += score
        else:
            task_time.append(time - 1)
            task_score.append(score)
    else:
        if task_time:
            if task_time[-1] - 1 == 0:
                task_time.pop()
                result += task_score.pop()
            else:
                task_time[-1] -= 1
print(result)
