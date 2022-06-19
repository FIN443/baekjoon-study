N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)


for i in range(1, N + 1):
    dp[i] = (lst[i], 1)
    for j in range(1, i):
        if lst[i] > dp[j][0] and dp[j][1] >= dp[i][1]:
            dp[i] = (lst[i], dp[j][1] + 1)

dp.pop(0)
print(max(dp, key=lambda x: x[1])[1])
