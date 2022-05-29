import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
c = [1] + [0] * (M - 1)
c_sum = 0

for i in range(N):
    c_sum += lst[i]  # 누적합
    c[c_sum % M] += 1  # sum % M 값 저장

result = 0
for i in c:
    result += i * (i - 1) // 2  # nC2

print(result)
# 1 + 2 / 1 + 2 + 3 / 1 + 2 + 3 + 1 + 2
# 2 + 3 + 1
# 3 / 3 + 1 + 2
# 1 + 2

# https://nnnlog.tistory.com/65
