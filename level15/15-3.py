# N=3 -> 100, 111, 001
# N(4) = N(2) + N(3)
# N(5) = N(3) + N(4)
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])
