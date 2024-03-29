N = int(input())

# 0~9 계단
dp = [[0] * 10 for i in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1

# dp[2][0] =            dp[1][1]
# dp[2][1] = dp[1][0]   dp[1][2]
# dp[2][2] = dp[1][1] + dp[1][3]
# dp[2][3] = dp[1][2] + dp[1][4]
# dp[2][4] = dp[1][3] + dp[1][5]
# dp[2][5] = dp[1][4] + dp[1][6]
# dp[2][6] = dp[1][5] + dp[1][7]
# dp[2][7] = dp[1][6] + dp[1][8]
# dp[2][8] = dp[1][7] + dp[1][9]
# dp[2][9] = dp[1][8]

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]

print(sum(dp[N]) % 1000000000)
