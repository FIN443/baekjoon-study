lst1 = input()
lst2 = input()

dp = [[0] * (len(lst2) + 1) for _ in range(len(lst1) + 1)]
for i, w1 in enumerate(lst1):
    for j, w2 in enumerate(lst2):
        if w1 == w2:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
print(dp[-1][-1])
