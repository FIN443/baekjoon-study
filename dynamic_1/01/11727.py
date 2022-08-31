# 2xn 타일링 2
n = int(input())

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]

print(dp[n] % 10007)

"""
a1 = 1          1
a2 = 1 + 1 + 1  3
a3 = 1 + 2 + 2  5
a4 = 3 + 6 + 2  11
a5 = 2*a3 + a4  21
"""
