# 오르막 수

N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N + 1)]

if N > 1:
    for i in range(2, N + 1):
        prev_total = sum(dp[i - 1])
        for j in range(10):
            dp[i][j] = prev_total
            prev_total = prev_total - dp[i - 1][j]

print(sum(dp[N]) % 10007)

"""
a1 =  1 +  1 +  1 +  1 +  1 +  1 +  1 + 1 + 1 + 1 =  10
a2 = 10 +  9 +  8 +  7 +  6 +  5 +  4 + 3 + 2 + 1 =  55
a3 = 55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1 = 220
a4 = a3 + (a3-a3[0]) + ((a3-a3[0])-a3[1]) + ... + (prev_total - a3[9])
"""
