T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

dp = [0 * i for i in range(T)]

if T == 1:
    print(lst[0])
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    for i in range(2, T):
        dp[i] = max(dp[i - 3] + lst[i - 1] + lst[i], dp[i - 2] + lst[i])
    print(dp[-1])
