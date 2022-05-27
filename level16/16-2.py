from itertools import accumulate
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

acc = [0] + list(accumulate(nums))
results = []
for i, _ in enumerate(nums[K - 1 :]):
    results.append(acc[K + i] - acc[i])  # 이 부분 버그
print(max(results))
