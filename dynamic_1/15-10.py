T = int(input())

dp = [0] * (T + 1)
lst = [0]
for i in range(T):
    lst.append(int(input()))

if T > 1:
    dp[1] = lst[1]
    dp[2] = dp[1] + lst[2]
    for i in range(3, T + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i])
    print(dp[-1])
else:
    print(lst[-1])
