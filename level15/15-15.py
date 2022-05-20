n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [-1001] * (n + 1)

for j in range(1, n + 1):
    dp[j] = max(dp[j - 1] + lst[j], lst[j])


print(max(dp))
