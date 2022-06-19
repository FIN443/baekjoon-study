import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
acc = [0]
temp = 0
for i in nums:
    temp += i
    acc.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j] - acc[i - 1])
